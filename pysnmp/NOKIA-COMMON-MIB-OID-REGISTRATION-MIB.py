# SNMP MIB module (NOKIA-COMMON-MIB-OID-REGISTRATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-COMMON-MIB-OID-REGISTRATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:35 2024
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

(ntcCommon,) = mibBuilder.importSymbols(
    "NOKIA-OID-REGISTRATION-MIB",
    "ntcCommon")

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

_NtcCommonAlarm_ObjectIdentity = ObjectIdentity
ntcCommonAlarm = _NtcCommonAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1)
)
_NtcCommonAlarmTrap_ObjectIdentity = ObjectIdentity
ntcCommonAlarmTrap = _NtcCommonAlarmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 2)
)
_NtcCommonTrapDest_ObjectIdentity = ObjectIdentity
ntcCommonTrapDest = _NtcCommonTrapDest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 3)
)
_NtcRS_ObjectIdentity = ObjectIdentity
ntcRS = _NtcRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 4)
)
_NtcCommonModules_ObjectIdentity = ObjectIdentity
ntcCommonModules = _NtcCommonModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 5)
)
_NtcHWModule_ObjectIdentity = ObjectIdentity
ntcHWModule = _NtcHWModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 1)
)
_NtcNtpModule_ObjectIdentity = ObjectIdentity
ntcNtpModule = _NtcNtpModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 2)
)
_NtcHWUnitTypeModule_ObjectIdentity = ObjectIdentity
ntcHWUnitTypeModule = _NtcHWUnitTypeModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 3)
)
_NtcACModule_ObjectIdentity = ObjectIdentity
ntcACModule = _NtcACModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 4)
)
_NtcGprsTracingModule_ObjectIdentity = ObjectIdentity
ntcGprsTracingModule = _NtcGprsTracingModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 5)
)
_NtcCommonAgentCaps_ObjectIdentity = ObjectIdentity
ntcCommonAgentCaps = _NtcCommonAgentCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 6)
)
_NtcHWAgentCap_ObjectIdentity = ObjectIdentity
ntcHWAgentCap = _NtcHWAgentCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 6, 1)
)
_NtcNtpAgentCap_ObjectIdentity = ObjectIdentity
ntcNtpAgentCap = _NtcNtpAgentCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 6, 2)
)
_NtcHWUnitTypeAgentCap_ObjectIdentity = ObjectIdentity
ntcHWUnitTypeAgentCap = _NtcHWUnitTypeAgentCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 6, 3)
)
_NtcACAgentCap_ObjectIdentity = ObjectIdentity
ntcACAgentCap = _NtcACAgentCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 6, 4)
)
_NtcGprsTracingAgentCap_ObjectIdentity = ObjectIdentity
ntcGprsTracingAgentCap = _NtcGprsTracingAgentCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 6, 5)
)
_NtcCommonMibs_ObjectIdentity = ObjectIdentity
ntcCommonMibs = _NtcCommonMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7)
)
_NtcHWMibs_ObjectIdentity = ObjectIdentity
ntcHWMibs = _NtcHWMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1)
)
_NtcNtpMibs_ObjectIdentity = ObjectIdentity
ntcNtpMibs = _NtcNtpMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2)
)
_NtcHWUnitTypeMibs_ObjectIdentity = ObjectIdentity
ntcHWUnitTypeMibs = _NtcHWUnitTypeMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 3)
)
_NtcACMibs_ObjectIdentity = ObjectIdentity
ntcACMibs = _NtcACMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 4)
)
_NtcGprsTracingMibs_ObjectIdentity = ObjectIdentity
ntcGprsTracingMibs = _NtcGprsTracingMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 5)
)
_NtcCommonReqs_ObjectIdentity = ObjectIdentity
ntcCommonReqs = _NtcCommonReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8)
)
_NtcHWReqs_ObjectIdentity = ObjectIdentity
ntcHWReqs = _NtcHWReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 1)
)
_NtcNtpReqs_ObjectIdentity = ObjectIdentity
ntcNtpReqs = _NtcNtpReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2)
)
_NtcHWUnitTypeReqs_ObjectIdentity = ObjectIdentity
ntcHWUnitTypeReqs = _NtcHWUnitTypeReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 3)
)
_NtcACReqs_ObjectIdentity = ObjectIdentity
ntcACReqs = _NtcACReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 4)
)
_NtcGprsTracingReqs_ObjectIdentity = ObjectIdentity
ntcGprsTracingReqs = _NtcGprsTracingReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-COMMON-MIB-OID-REGISTRATION-MIB",
    **{"ntcCommonAlarm": ntcCommonAlarm,
       "ntcCommonAlarmTrap": ntcCommonAlarmTrap,
       "ntcCommonTrapDest": ntcCommonTrapDest,
       "ntcRS": ntcRS,
       "ntcCommonModules": ntcCommonModules,
       "ntcHWModule": ntcHWModule,
       "ntcNtpModule": ntcNtpModule,
       "ntcHWUnitTypeModule": ntcHWUnitTypeModule,
       "ntcACModule": ntcACModule,
       "ntcGprsTracingModule": ntcGprsTracingModule,
       "ntcCommonAgentCaps": ntcCommonAgentCaps,
       "ntcHWAgentCap": ntcHWAgentCap,
       "ntcNtpAgentCap": ntcNtpAgentCap,
       "ntcHWUnitTypeAgentCap": ntcHWUnitTypeAgentCap,
       "ntcACAgentCap": ntcACAgentCap,
       "ntcGprsTracingAgentCap": ntcGprsTracingAgentCap,
       "ntcCommonMibs": ntcCommonMibs,
       "ntcHWMibs": ntcHWMibs,
       "ntcNtpMibs": ntcNtpMibs,
       "ntcHWUnitTypeMibs": ntcHWUnitTypeMibs,
       "ntcACMibs": ntcACMibs,
       "ntcGprsTracingMibs": ntcGprsTracingMibs,
       "ntcCommonReqs": ntcCommonReqs,
       "ntcHWReqs": ntcHWReqs,
       "ntcNtpReqs": ntcNtpReqs,
       "ntcHWUnitTypeReqs": ntcHWUnitTypeReqs,
       "ntcACReqs": ntcACReqs,
       "ntcGprsTracingReqs": ntcGprsTracingReqs}
)
