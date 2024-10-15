# SNMP MIB module (A3COM-AUDL-R1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-AUDL-R1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:09 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_A3ComAuditLog_ObjectIdentity = ObjectIdentity
a3ComAuditLog = _A3ComAuditLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 29)
)
_A3ComAudlControl_ObjectIdentity = ObjectIdentity
a3ComAudlControl = _A3ComAudlControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 29, 1)
)


class _A3ComAudlControlAuditTrail_Type(Integer32):
    """Custom type a3ComAudlControlAuditTrail based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auditTrail", 1),
          ("noAuditTrail", 2))
    )


_A3ComAudlControlAuditTrail_Type.__name__ = "Integer32"
_A3ComAudlControlAuditTrail_Object = MibScalar
a3ComAudlControlAuditTrail = _A3ComAudlControlAuditTrail_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 29, 1, 1),
    _A3ComAudlControlAuditTrail_Type()
)
a3ComAudlControlAuditTrail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComAudlControlAuditTrail.setStatus("mandatory")


class _A3ComAudlControlConfig_Type(Integer32):
    """Custom type a3ComAudlControlConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("noConfig", 2))
    )


_A3ComAudlControlConfig_Type.__name__ = "Integer32"
_A3ComAudlControlConfig_Object = MibScalar
a3ComAudlControlConfig = _A3ComAudlControlConfig_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 29, 1, 2),
    _A3ComAudlControlConfig_Type()
)
a3ComAudlControlConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComAudlControlConfig.setStatus("mandatory")


class _A3ComAudlControlMessages_Type(Integer32):
    """Custom type a3ComAudlControlMessages based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("messages", 1),
          ("noMessages", 2))
    )


_A3ComAudlControlMessages_Type.__name__ = "Integer32"
_A3ComAudlControlMessages_Object = MibScalar
a3ComAudlControlMessages = _A3ComAudlControlMessages_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 29, 1, 3),
    _A3ComAudlControlMessages_Type()
)
a3ComAudlControlMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComAudlControlMessages.setStatus("mandatory")


class _A3ComAudlControlSecurity_Type(Integer32):
    """Custom type a3ComAudlControlSecurity based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSecurity", 2),
          ("security", 1))
    )


_A3ComAudlControlSecurity_Type.__name__ = "Integer32"
_A3ComAudlControlSecurity_Object = MibScalar
a3ComAudlControlSecurity = _A3ComAudlControlSecurity_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 29, 1, 4),
    _A3ComAudlControlSecurity_Type()
)
a3ComAudlControlSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComAudlControlSecurity.setStatus("mandatory")
_A3ComAudlConfig_ObjectIdentity = ObjectIdentity
a3ComAudlConfig = _A3ComAudlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 29, 2)
)
_A3ComAudlLogServerAddr_Type = IpAddress
_A3ComAudlLogServerAddr_Object = MibScalar
a3ComAudlLogServerAddr = _A3ComAudlLogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 29, 2, 1),
    _A3ComAudlLogServerAddr_Type()
)
a3ComAudlLogServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComAudlLogServerAddr.setStatus("mandatory")


class _A3ComAudlPriorityLevel_Type(Integer32):
    """Custom type a3ComAudlPriorityLevel based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("log_ALERT", 2),
          ("log_CRITICAL", 3),
          ("log_DEBUG", 8),
          ("log_EMERG", 1),
          ("log_ERROR", 4),
          ("log_INFO", 7),
          ("log_NOTICE", 6),
          ("log_WARNING", 5))
    )


_A3ComAudlPriorityLevel_Type.__name__ = "Integer32"
_A3ComAudlPriorityLevel_Object = MibScalar
a3ComAudlPriorityLevel = _A3ComAudlPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 29, 2, 2),
    _A3ComAudlPriorityLevel_Type()
)
a3ComAudlPriorityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComAudlPriorityLevel.setStatus("mandatory")


class _A3ComAudlMaxLog_Type(Integer32):
    """Custom type a3ComAudlMaxLog based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_A3ComAudlMaxLog_Type.__name__ = "Integer32"
_A3ComAudlMaxLog_Object = MibScalar
a3ComAudlMaxLog = _A3ComAudlMaxLog_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 29, 2, 3),
    _A3ComAudlMaxLog_Type()
)
a3ComAudlMaxLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComAudlMaxLog.setStatus("mandatory")


class _A3ComAudlIdleTime_Type(Integer32):
    """Custom type a3ComAudlIdleTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 480),
    )


_A3ComAudlIdleTime_Type.__name__ = "Integer32"
_A3ComAudlIdleTime_Object = MibScalar
a3ComAudlIdleTime = _A3ComAudlIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 29, 2, 4),
    _A3ComAudlIdleTime_Type()
)
a3ComAudlIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComAudlIdleTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-AUDL-R1-MIB",
    **{"a3Com": a3Com,
       "brouterMIB": brouterMIB,
       "a3ComAuditLog": a3ComAuditLog,
       "a3ComAudlControl": a3ComAudlControl,
       "a3ComAudlControlAuditTrail": a3ComAudlControlAuditTrail,
       "a3ComAudlControlConfig": a3ComAudlControlConfig,
       "a3ComAudlControlMessages": a3ComAudlControlMessages,
       "a3ComAudlControlSecurity": a3ComAudlControlSecurity,
       "a3ComAudlConfig": a3ComAudlConfig,
       "a3ComAudlLogServerAddr": a3ComAudlLogServerAddr,
       "a3ComAudlPriorityLevel": a3ComAudlPriorityLevel,
       "a3ComAudlMaxLog": a3ComAudlMaxLog,
       "a3ComAudlIdleTime": a3ComAudlIdleTime}
)
