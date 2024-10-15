# SNMP MIB module (EXTREME-SNMPV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(snmpTargetAddrEntry,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetAddrEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeSnmpv3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeTarget_ObjectIdentity = ObjectIdentity
extremeTarget = _ExtremeTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1)
)
_ExtremeTargetAddrExtTable_Object = MibTable
extremeTargetAddrExtTable = _ExtremeTargetAddrExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1)
)
if mibBuilder.loadTexts:
    extremeTargetAddrExtTable.setStatus("current")
_ExtremeTargetAddrExtEntry_Object = MibTableRow
extremeTargetAddrExtEntry = _ExtremeTargetAddrExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    extremeTargetAddrExtEntry.setStatus("current")


class _ExtremeTargetAddrExtIgnoreMPModel_Type(TruthValue):
    """Custom type extremeTargetAddrExtIgnoreMPModel based on TruthValue"""


_ExtremeTargetAddrExtIgnoreMPModel_Object = MibTableColumn
extremeTargetAddrExtIgnoreMPModel = _ExtremeTargetAddrExtIgnoreMPModel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 1),
    _ExtremeTargetAddrExtIgnoreMPModel_Type()
)
extremeTargetAddrExtIgnoreMPModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeTargetAddrExtIgnoreMPModel.setStatus("current")


class _ExtremeTargetAddrExtStandardMode_Type(TruthValue):
    """Custom type extremeTargetAddrExtStandardMode based on TruthValue"""


_ExtremeTargetAddrExtStandardMode_Object = MibTableColumn
extremeTargetAddrExtStandardMode = _ExtremeTargetAddrExtStandardMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 2),
    _ExtremeTargetAddrExtStandardMode_Type()
)
extremeTargetAddrExtStandardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeTargetAddrExtStandardMode.setStatus("current")
_ExtremeTargetAddrExtTrapDestIndex_Type = Integer32
_ExtremeTargetAddrExtTrapDestIndex_Object = MibTableColumn
extremeTargetAddrExtTrapDestIndex = _ExtremeTargetAddrExtTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 3),
    _ExtremeTargetAddrExtTrapDestIndex_Type()
)
extremeTargetAddrExtTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTargetAddrExtTrapDestIndex.setStatus("current")


class _ExtremeTargetAddrExtUseEventComm_Type(TruthValue):
    """Custom type extremeTargetAddrExtUseEventComm based on TruthValue"""


_ExtremeTargetAddrExtUseEventComm_Object = MibTableColumn
extremeTargetAddrExtUseEventComm = _ExtremeTargetAddrExtUseEventComm_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23, 1, 1, 1, 4),
    _ExtremeTargetAddrExtUseEventComm_Type()
)
extremeTargetAddrExtUseEventComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeTargetAddrExtUseEventComm.setStatus("current")
snmpTargetAddrEntry.registerAugmentions(
    ("EXTREME-SNMPV3-MIB",
     "extremeTargetAddrExtEntry")
)
extremeTargetAddrExtEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-SNMPV3-MIB",
    **{"extremeSnmpv3": extremeSnmpv3,
       "extremeTarget": extremeTarget,
       "extremeTargetAddrExtTable": extremeTargetAddrExtTable,
       "extremeTargetAddrExtEntry": extremeTargetAddrExtEntry,
       "extremeTargetAddrExtIgnoreMPModel": extremeTargetAddrExtIgnoreMPModel,
       "extremeTargetAddrExtStandardMode": extremeTargetAddrExtStandardMode,
       "extremeTargetAddrExtTrapDestIndex": extremeTargetAddrExtTrapDestIndex,
       "extremeTargetAddrExtUseEventComm": extremeTargetAddrExtUseEventComm}
)
