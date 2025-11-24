'use client'

import { motion } from 'framer-motion'
import { User, Bot, Loader2 } from 'lucide-react'
import { cn } from '@/lib/utils'
import { formatTimestamp } from '@/lib/utils'

interface MessageProps {
  message: {
    id: string
    role: 'user' | 'assistant'
    content: string
    timestamp: Date
    isStreaming?: boolean
  }
  index: number
}

export default function Message({ message, index }: MessageProps) {
  const isUser = message.role === 'user'

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -10 }}
      transition={{ duration: 0.3, delay: index * 0.05 }}
      className={cn(
        "flex gap-3 p-4 rounded-xl",
        isUser ? "bg-primary/5 ml-8" : "bg-gray-50 mr-8"
      )}
    >
      {/* Avatar */}
      <div
        className={cn(
          "flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center",
          isUser ? "bg-primary" : "bg-accent-red"
        )}
      >
        {isUser ? (
          <User className="w-5 h-5 text-white" />
        ) : (
          <Bot className="w-5 h-5 text-white" />
        )}
      </div>

      {/* Content */}
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2 mb-1">
          <span className="font-semibold text-sm text-text-primary">
            {isUser ? 'You' : 'Assistant'}
          </span>
          <span className="text-xs text-text-light">
            {formatTimestamp(message.timestamp)}
          </span>
          {message.isStreaming && (
            <Loader2 className="w-3 h-3 text-primary animate-spin" />
          )}
        </div>
        <div className="text-text-primary whitespace-pre-wrap break-words">
          {message.content}
          {message.isStreaming && !message.content && (
            <span className="inline-flex gap-1">
              <span className="w-2 h-2 bg-primary rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
              <span className="w-2 h-2 bg-primary rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
              <span className="w-2 h-2 bg-primary rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
            </span>
          )}
        </div>
      </div>
    </motion.div>
  )
}
