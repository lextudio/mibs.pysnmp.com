# SNMP MIB module (CASA-CABLE-CMQUERY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CASA-CABLE-CMQUERY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:38 2024
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

(casa,) = mibBuilder.importSymbols(
    "CASA-MIB",
    "casa")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

casaCmQueryMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TenthdBmV(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class TenthdB(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


# MIB Managed Objects in the order of their OIDs

_CasaMgmt_ObjectIdentity = ObjectIdentity
casaMgmt = _CasaMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10)
)
_CasaCmQueryMibObjects_ObjectIdentity = ObjectIdentity
casaCmQueryMibObjects = _CasaCmQueryMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 1)
)
_CasaCmQueryTable_Object = MibTable
casaCmQueryTable = _CasaCmQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1)
)
if mibBuilder.loadTexts:
    casaCmQueryTable.setStatus("current")
_CasaCmQueryEntry_Object = MibTableRow
casaCmQueryEntry = _CasaCmQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1)
)
casaCmQueryEntry.setIndexNames(
    (0, "CASA-CABLE-CMQUERY-MIB", "casaQueryCmMacAddress"),
)
if mibBuilder.loadTexts:
    casaCmQueryEntry.setStatus("current")
_CasaQueryCmMacAddress_Type = MacAddress
_CasaQueryCmMacAddress_Object = MibTableColumn
casaQueryCmMacAddress = _CasaQueryCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 1),
    _CasaQueryCmMacAddress_Type()
)
casaQueryCmMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casaQueryCmMacAddress.setStatus("current")
_CasaQueryCmIpAddress_Type = IpAddress
_CasaQueryCmIpAddress_Object = MibTableColumn
casaQueryCmIpAddress = _CasaQueryCmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 2),
    _CasaQueryCmIpAddress_Type()
)
casaQueryCmIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaQueryCmIpAddress.setStatus("current")
_CasaQueryCmTxTimeOffset_Type = Unsigned32
_CasaQueryCmTxTimeOffset_Object = MibTableColumn
casaQueryCmTxTimeOffset = _CasaQueryCmTxTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 3),
    _CasaQueryCmTxTimeOffset_Type()
)
casaQueryCmTxTimeOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaQueryCmTxTimeOffset.setStatus("current")


class _CasaQueryCmMicroReflection_Type(Integer32):
    """Custom type casaQueryCmMicroReflection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CasaQueryCmMicroReflection_Type.__name__ = "Integer32"
_CasaQueryCmMicroReflection_Object = MibTableColumn
casaQueryCmMicroReflection = _CasaQueryCmMicroReflection_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 4),
    _CasaQueryCmMicroReflection_Type()
)
casaQueryCmMicroReflection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaQueryCmMicroReflection.setStatus("current")
if mibBuilder.loadTexts:
    casaQueryCmMicroReflection.setUnits("dBc")
_CasaQueryCmStatusTxPower_Type = TenthdBmV
_CasaQueryCmStatusTxPower_Object = MibTableColumn
casaQueryCmStatusTxPower = _CasaQueryCmStatusTxPower_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 5),
    _CasaQueryCmStatusTxPower_Type()
)
casaQueryCmStatusTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaQueryCmStatusTxPower.setStatus("current")
if mibBuilder.loadTexts:
    casaQueryCmStatusTxPower.setUnits("dBmV")
_CasaQueryCmStatusRxPower_Type = TenthdBmV
_CasaQueryCmStatusRxPower_Object = MibTableColumn
casaQueryCmStatusRxPower = _CasaQueryCmStatusRxPower_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 6),
    _CasaQueryCmStatusRxPower_Type()
)
casaQueryCmStatusRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaQueryCmStatusRxPower.setStatus("current")
if mibBuilder.loadTexts:
    casaQueryCmStatusRxPower.setUnits("dBmV")
_CasaQueryCmSigQSignalNoise_Type = TenthdB
_CasaQueryCmSigQSignalNoise_Object = MibTableColumn
casaQueryCmSigQSignalNoise = _CasaQueryCmSigQSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 7),
    _CasaQueryCmSigQSignalNoise_Type()
)
casaQueryCmSigQSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaQueryCmSigQSignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    casaQueryCmSigQSignalNoise.setUnits("dB")
_CasaQueryCmtsSigQSignalNoise_Type = TenthdB
_CasaQueryCmtsSigQSignalNoise_Object = MibTableColumn
casaQueryCmtsSigQSignalNoise = _CasaQueryCmtsSigQSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 8),
    _CasaQueryCmtsSigQSignalNoise_Type()
)
casaQueryCmtsSigQSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaQueryCmtsSigQSignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    casaQueryCmtsSigQSignalNoise.setUnits("dB")
_CasaCmQueryGroups_ObjectIdentity = ObjectIdentity
casaCmQueryGroups = _CasaCmQueryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 2)
)
_CasaCmQueryCompliances_ObjectIdentity = ObjectIdentity
casaCmQueryCompliances = _CasaCmQueryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 3)
)

# Managed Objects groups

casaCmQueryroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 2, 1)
)
casaCmQueryroup.setObjects(
      *(("CASA-CABLE-CMQUERY-MIB", "casaQueryCmIpAddress"),
        ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmTxTimeOffset"),
        ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmMicroReflection"),
        ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmStatusTxPower"),
        ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmStatusRxPower"),
        ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmSigQSignalNoise"),
        ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmtsSigQSignalNoise"))
)
if mibBuilder.loadTexts:
    casaCmQueryroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

casaCmQueryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20858, 10, 18, 3, 1)
)
if mibBuilder.loadTexts:
    casaCmQueryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CASA-CABLE-CMQUERY-MIB",
    **{"TenthdBmV": TenthdBmV,
       "TenthdB": TenthdB,
       "casaMgmt": casaMgmt,
       "casaCmQueryMib": casaCmQueryMib,
       "casaCmQueryMibObjects": casaCmQueryMibObjects,
       "casaCmQueryTable": casaCmQueryTable,
       "casaCmQueryEntry": casaCmQueryEntry,
       "casaQueryCmMacAddress": casaQueryCmMacAddress,
       "casaQueryCmIpAddress": casaQueryCmIpAddress,
       "casaQueryCmTxTimeOffset": casaQueryCmTxTimeOffset,
       "casaQueryCmMicroReflection": casaQueryCmMicroReflection,
       "casaQueryCmStatusTxPower": casaQueryCmStatusTxPower,
       "casaQueryCmStatusRxPower": casaQueryCmStatusRxPower,
       "casaQueryCmSigQSignalNoise": casaQueryCmSigQSignalNoise,
       "casaQueryCmtsSigQSignalNoise": casaQueryCmtsSigQSignalNoise,
       "casaCmQueryGroups": casaCmQueryGroups,
       "casaCmQueryroup": casaCmQueryroup,
       "casaCmQueryCompliances": casaCmQueryCompliances,
       "casaCmQueryCompliance": casaCmQueryCompliance}
)
