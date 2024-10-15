# SNMP MIB module (MANTRA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MANTRA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:00 2024
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
 ObjectName,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "ObjectName",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mantraAdmin = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_SoftSwitch_ObjectIdentity = ObjectIdentity
softSwitch = _SoftSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198)
)
_ModuleSummary_Type = DisplayString
_ModuleSummary_Object = MibScalar
moduleSummary = _ModuleSummary_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 1),
    _ModuleSummary_Type()
)
moduleSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSummary.setStatus("current")
_MantraUpTime_Type = TimeTicks
_MantraUpTime_Object = MibScalar
mantraUpTime = _MantraUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 2),
    _MantraUpTime_Type()
)
mantraUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mantraUpTime.setStatus("current")


class _MantraRetryCount_Type(Integer32):
    """Custom type mantraRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_MantraRetryCount_Type.__name__ = "Integer32"
_MantraRetryCount_Object = MibScalar
mantraRetryCount = _MantraRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 3),
    _MantraRetryCount_Type()
)
mantraRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mantraRetryCount.setStatus("current")


class _MantraRetryInterval_Type(Integer32):
    """Custom type mantraRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_MantraRetryInterval_Type.__name__ = "Integer32"
_MantraRetryInterval_Object = MibScalar
mantraRetryInterval = _MantraRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 4),
    _MantraRetryInterval_Type()
)
mantraRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mantraRetryInterval.setStatus("current")


class _MantraReboot_Type(Integer32):
    """Custom type mantraReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MantraReboot_Type.__name__ = "Integer32"
_MantraReboot_Object = MibScalar
mantraReboot = _MantraReboot_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 5),
    _MantraReboot_Type()
)
mantraReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mantraReboot.setStatus("current")


class _MantraTurnoff_Type(Integer32):
    """Custom type mantraTurnoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MantraTurnoff_Type.__name__ = "Integer32"
_MantraTurnoff_Object = MibScalar
mantraTurnoff = _MantraTurnoff_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 6),
    _MantraTurnoff_Type()
)
mantraTurnoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mantraTurnoff.setStatus("current")
_StartProcess_Type = DisplayString
_StartProcess_Object = MibScalar
startProcess = _StartProcess_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 7),
    _StartProcess_Type()
)
startProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startProcess.setStatus("current")
_StopProcess_Type = DisplayString
_StopProcess_Object = MibScalar
stopProcess = _StopProcess_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 8),
    _StopProcess_Type()
)
stopProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stopProcess.setStatus("current")
_CurrentProcess_Type = DisplayString
_CurrentProcess_Object = MibScalar
currentProcess = _CurrentProcess_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 9),
    _CurrentProcess_Type()
)
currentProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentProcess.setStatus("current")
_ProcessState_Type = DisplayString
_ProcessState_Object = MibScalar
processState = _ProcessState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 10),
    _ProcessState_Type()
)
processState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MANTRA-MIB",
    **{"lucent": lucent,
       "products": products,
       "softSwitch": softSwitch,
       "mantraAdmin": mantraAdmin,
       "moduleSummary": moduleSummary,
       "mantraUpTime": mantraUpTime,
       "mantraRetryCount": mantraRetryCount,
       "mantraRetryInterval": mantraRetryInterval,
       "mantraReboot": mantraReboot,
       "mantraTurnoff": mantraTurnoff,
       "startProcess": startProcess,
       "stopProcess": stopProcess,
       "currentProcess": currentProcess,
       "processState": processState}
)
