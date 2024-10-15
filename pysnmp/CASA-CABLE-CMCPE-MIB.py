# SNMP MIB module (CASA-CABLE-CMCPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CASA-CABLE-CMCPE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:37 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

casaCmtsCmCpeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CasaMgmt_ObjectIdentity = ObjectIdentity
casaMgmt = _CasaMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10)
)
_CasaCmtsCmCpeObjects_ObjectIdentity = ObjectIdentity
casaCmtsCmCpeObjects = _CasaCmtsCmCpeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1)
)
_CasaCmtsUSModemTable_Object = MibTable
casaCmtsUSModemTable = _CasaCmtsUSModemTable_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 1)
)
if mibBuilder.loadTexts:
    casaCmtsUSModemTable.setStatus("current")
_CasaCmtsUSModemEntry_Object = MibTableRow
casaCmtsUSModemEntry = _CasaCmtsUSModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 1, 1)
)
casaCmtsUSModemEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    casaCmtsUSModemEntry.setStatus("current")
_CasaCmtsUSActiveModemCount_Type = Unsigned32
_CasaCmtsUSActiveModemCount_Object = MibTableColumn
casaCmtsUSActiveModemCount = _CasaCmtsUSActiveModemCount_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 1, 1, 1),
    _CasaCmtsUSActiveModemCount_Type()
)
casaCmtsUSActiveModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaCmtsUSActiveModemCount.setStatus("current")
_CasaCmtsUSRegisteredModemCount_Type = Unsigned32
_CasaCmtsUSRegisteredModemCount_Object = MibTableColumn
casaCmtsUSRegisteredModemCount = _CasaCmtsUSRegisteredModemCount_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 1, 1, 2),
    _CasaCmtsUSRegisteredModemCount_Type()
)
casaCmtsUSRegisteredModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaCmtsUSRegisteredModemCount.setStatus("current")
_CasaCmtsUSTotalModemCount_Type = Unsigned32
_CasaCmtsUSTotalModemCount_Object = MibTableColumn
casaCmtsUSTotalModemCount = _CasaCmtsUSTotalModemCount_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 1, 1, 3),
    _CasaCmtsUSTotalModemCount_Type()
)
casaCmtsUSTotalModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaCmtsUSTotalModemCount.setStatus("current")
_CasaCmtsDSModemTable_Object = MibTable
casaCmtsDSModemTable = _CasaCmtsDSModemTable_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 2)
)
if mibBuilder.loadTexts:
    casaCmtsDSModemTable.setStatus("current")
_CasaCmtsDSModemEntry_Object = MibTableRow
casaCmtsDSModemEntry = _CasaCmtsDSModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 2, 1)
)
casaCmtsDSModemEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    casaCmtsDSModemEntry.setStatus("current")
_CasaCmtsDSActiveModemCount_Type = Unsigned32
_CasaCmtsDSActiveModemCount_Object = MibTableColumn
casaCmtsDSActiveModemCount = _CasaCmtsDSActiveModemCount_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 2, 1, 1),
    _CasaCmtsDSActiveModemCount_Type()
)
casaCmtsDSActiveModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaCmtsDSActiveModemCount.setStatus("current")
_CasaCmtsDSRegisteredModemCount_Type = Unsigned32
_CasaCmtsDSRegisteredModemCount_Object = MibTableColumn
casaCmtsDSRegisteredModemCount = _CasaCmtsDSRegisteredModemCount_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 2, 1, 2),
    _CasaCmtsDSRegisteredModemCount_Type()
)
casaCmtsDSRegisteredModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaCmtsDSRegisteredModemCount.setStatus("current")
_CasaCmtsDSTotalModemCount_Type = Unsigned32
_CasaCmtsDSTotalModemCount_Object = MibTableColumn
casaCmtsDSTotalModemCount = _CasaCmtsDSTotalModemCount_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 2, 1, 3),
    _CasaCmtsDSTotalModemCount_Type()
)
casaCmtsDSTotalModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaCmtsDSTotalModemCount.setStatus("current")
_CasaCmtsCmCpeTable_Object = MibTable
casaCmtsCmCpeTable = _CasaCmtsCmCpeTable_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 3)
)
if mibBuilder.loadTexts:
    casaCmtsCmCpeTable.setStatus("current")
_CasaCmtsCmCpeEntry_Object = MibTableRow
casaCmtsCmCpeEntry = _CasaCmtsCmCpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 3, 1)
)
casaCmtsCmCpeEntry.setIndexNames(
    (0, "CASA-CABLE-CMCPE-MIB", "casaCmtsCmCpeMacAddress"),
)
if mibBuilder.loadTexts:
    casaCmtsCmCpeEntry.setStatus("current")
_CasaCmtsCmCpeMacAddress_Type = MacAddress
_CasaCmtsCmCpeMacAddress_Object = MibTableColumn
casaCmtsCmCpeMacAddress = _CasaCmtsCmCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 3, 1, 1),
    _CasaCmtsCmCpeMacAddress_Type()
)
casaCmtsCmCpeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casaCmtsCmCpeMacAddress.setStatus("current")


class _CasaCmtsCmCpeType_Type(Integer32):
    """Custom type casaCmtsCmCpeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cm", 1),
          ("cpe", 2))
    )


_CasaCmtsCmCpeType_Type.__name__ = "Integer32"
_CasaCmtsCmCpeType_Object = MibTableColumn
casaCmtsCmCpeType = _CasaCmtsCmCpeType_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 3, 1, 2),
    _CasaCmtsCmCpeType_Type()
)
casaCmtsCmCpeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaCmtsCmCpeType.setStatus("current")
_CasaCmtsCmCpeIpAddress_Type = IpAddress
_CasaCmtsCmCpeIpAddress_Object = MibTableColumn
casaCmtsCmCpeIpAddress = _CasaCmtsCmCpeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 3, 1, 3),
    _CasaCmtsCmCpeIpAddress_Type()
)
casaCmtsCmCpeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaCmtsCmCpeIpAddress.setStatus("current")
_CasaCmtsCmCpeIfIndex_Type = InterfaceIndex
_CasaCmtsCmCpeIfIndex_Object = MibTableColumn
casaCmtsCmCpeIfIndex = _CasaCmtsCmCpeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 3, 1, 4),
    _CasaCmtsCmCpeIfIndex_Type()
)
casaCmtsCmCpeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaCmtsCmCpeIfIndex.setStatus("current")


class _CasaCmtsCmCpeCmtsServiceId_Type(Integer32):
    """Custom type casaCmtsCmCpeCmtsServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_CasaCmtsCmCpeCmtsServiceId_Type.__name__ = "Integer32"
_CasaCmtsCmCpeCmtsServiceId_Object = MibTableColumn
casaCmtsCmCpeCmtsServiceId = _CasaCmtsCmCpeCmtsServiceId_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 3, 1, 5),
    _CasaCmtsCmCpeCmtsServiceId_Type()
)
casaCmtsCmCpeCmtsServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaCmtsCmCpeCmtsServiceId.setStatus("current")


class _CasaCmtsCmCpeCmStatusIndex_Type(Integer32):
    """Custom type casaCmtsCmCpeCmStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CasaCmtsCmCpeCmStatusIndex_Type.__name__ = "Integer32"
_CasaCmtsCmCpeCmStatusIndex_Object = MibTableColumn
casaCmtsCmCpeCmStatusIndex = _CasaCmtsCmCpeCmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 3, 1, 6),
    _CasaCmtsCmCpeCmStatusIndex_Type()
)
casaCmtsCmCpeCmStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaCmtsCmCpeCmStatusIndex.setStatus("current")
_CasaCmtsCmCpeResetNow_Type = TruthValue
_CasaCmtsCmCpeResetNow_Object = MibTableColumn
casaCmtsCmCpeResetNow = _CasaCmtsCmCpeResetNow_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 3, 1, 7),
    _CasaCmtsCmCpeResetNow_Type()
)
casaCmtsCmCpeResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casaCmtsCmCpeResetNow.setStatus("current")
_CasaCmtsCpeIpNetToPhysicalTable_Object = MibTable
casaCmtsCpeIpNetToPhysicalTable = _CasaCmtsCpeIpNetToPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 4)
)
if mibBuilder.loadTexts:
    casaCmtsCpeIpNetToPhysicalTable.setStatus("current")
_CasaCmtsCpeIpNetToPhysicalEntry_Object = MibTableRow
casaCmtsCpeIpNetToPhysicalEntry = _CasaCmtsCpeIpNetToPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 4, 1)
)
casaCmtsCpeIpNetToPhysicalEntry.setIndexNames(
    (0, "CASA-CABLE-CMCPE-MIB", "casaCmtsCpeIpNetToPhysicalIfIndex"),
    (0, "CASA-CABLE-CMCPE-MIB", "casaCmtsCpeIpNetToPhysicalNetAddressType"),
    (0, "CASA-CABLE-CMCPE-MIB", "casaCmtsCpeIpNetToPhysicalNetAddress"),
)
if mibBuilder.loadTexts:
    casaCmtsCpeIpNetToPhysicalEntry.setStatus("current")
_CasaCmtsCpeIpNetToPhysicalIfIndex_Type = InterfaceIndex
_CasaCmtsCpeIpNetToPhysicalIfIndex_Object = MibTableColumn
casaCmtsCpeIpNetToPhysicalIfIndex = _CasaCmtsCpeIpNetToPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 4, 1, 1),
    _CasaCmtsCpeIpNetToPhysicalIfIndex_Type()
)
casaCmtsCpeIpNetToPhysicalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casaCmtsCpeIpNetToPhysicalIfIndex.setStatus("current")
_CasaCmtsCpeIpNetToPhysicalNetAddressType_Type = InetAddressType
_CasaCmtsCpeIpNetToPhysicalNetAddressType_Object = MibTableColumn
casaCmtsCpeIpNetToPhysicalNetAddressType = _CasaCmtsCpeIpNetToPhysicalNetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 4, 1, 2),
    _CasaCmtsCpeIpNetToPhysicalNetAddressType_Type()
)
casaCmtsCpeIpNetToPhysicalNetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casaCmtsCpeIpNetToPhysicalNetAddressType.setStatus("current")
_CasaCmtsCpeIpNetToPhysicalNetAddress_Type = InetAddress
_CasaCmtsCpeIpNetToPhysicalNetAddress_Object = MibTableColumn
casaCmtsCpeIpNetToPhysicalNetAddress = _CasaCmtsCpeIpNetToPhysicalNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 4, 1, 3),
    _CasaCmtsCpeIpNetToPhysicalNetAddress_Type()
)
casaCmtsCpeIpNetToPhysicalNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casaCmtsCpeIpNetToPhysicalNetAddress.setStatus("current")
_CasaCmtsCpeIpNetToPhysicalCmPhysAddress_Type = PhysAddress
_CasaCmtsCpeIpNetToPhysicalCmPhysAddress_Object = MibTableColumn
casaCmtsCpeIpNetToPhysicalCmPhysAddress = _CasaCmtsCpeIpNetToPhysicalCmPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 4, 1, 5),
    _CasaCmtsCpeIpNetToPhysicalCmPhysAddress_Type()
)
casaCmtsCpeIpNetToPhysicalCmPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaCmtsCpeIpNetToPhysicalCmPhysAddress.setStatus("current")


class _CasaCmtsCpeIpNetToPhysicalType_Type(Integer32):
    """Custom type casaCmtsCpeIpNetToPhysicalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_CasaCmtsCpeIpNetToPhysicalType_Type.__name__ = "Integer32"
_CasaCmtsCpeIpNetToPhysicalType_Object = MibTableColumn
casaCmtsCpeIpNetToPhysicalType = _CasaCmtsCpeIpNetToPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 4, 1, 7),
    _CasaCmtsCpeIpNetToPhysicalType_Type()
)
casaCmtsCpeIpNetToPhysicalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaCmtsCpeIpNetToPhysicalType.setStatus("current")
_CasaCmtsCmReset_ObjectIdentity = ObjectIdentity
casaCmtsCmReset = _CasaCmtsCmReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 5)
)
_CasaCmtsCmResetByIpAddr_Type = IpAddress
_CasaCmtsCmResetByIpAddr_Object = MibScalar
casaCmtsCmResetByIpAddr = _CasaCmtsCmResetByIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 5, 1),
    _CasaCmtsCmResetByIpAddr_Type()
)
casaCmtsCmResetByIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casaCmtsCmResetByIpAddr.setStatus("current")
_CasaCmtsCmResetByMacAddr_Type = MacAddress
_CasaCmtsCmResetByMacAddr_Object = MibScalar
casaCmtsCmResetByMacAddr = _CasaCmtsCmResetByMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 5, 2),
    _CasaCmtsCmResetByMacAddr_Type()
)
casaCmtsCmResetByMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casaCmtsCmResetByMacAddr.setStatus("current")


class _CasaCmtsCmResetAll_Type(TruthValue):
    """Custom type casaCmtsCmResetAll based on TruthValue"""


_CasaCmtsCmResetAll_Object = MibScalar
casaCmtsCmResetAll = _CasaCmtsCmResetAll_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 1, 5, 3),
    _CasaCmtsCmResetAll_Type()
)
casaCmtsCmResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casaCmtsCmResetAll.setStatus("current")
_CasaCmCpeGroups_ObjectIdentity = ObjectIdentity
casaCmCpeGroups = _CasaCmCpeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 2)
)
_CasaCmCpeCompliances_ObjectIdentity = ObjectIdentity
casaCmCpeCompliances = _CasaCmCpeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 3)
)

# Managed Objects groups

casaCmCpeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 2, 1)
)
casaCmCpeGroup.setObjects(
      *(("CASA-CABLE-CMCPE-MIB", "casaCmtsUSActiveModemCount"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsUSRegisteredModemCount"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsUSTotalModemCount"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsDSActiveModemCount"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsDSRegisteredModemCount"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsDSTotalModemCount"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsCmResetAll"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsCmResetByMacAddr"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsCmResetByIpAddr"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsCmCpeResetNow"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsCmCpeCmStatusIndex"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsCmCpeCmtsServiceId"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsCmCpeIfIndex"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsCpeIpNetToPhysicalType"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsCmCpeType"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsCmCpeIpAddress"),
        ("CASA-CABLE-CMCPE-MIB", "casaCmtsCpeIpNetToPhysicalCmPhysAddress"))
)
if mibBuilder.loadTexts:
    casaCmCpeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

casaCmCpeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20858, 10, 12, 3, 1)
)
if mibBuilder.loadTexts:
    casaCmCpeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CASA-CABLE-CMCPE-MIB",
    **{"casaMgmt": casaMgmt,
       "casaCmtsCmCpeMib": casaCmtsCmCpeMib,
       "casaCmtsCmCpeObjects": casaCmtsCmCpeObjects,
       "casaCmtsUSModemTable": casaCmtsUSModemTable,
       "casaCmtsUSModemEntry": casaCmtsUSModemEntry,
       "casaCmtsUSActiveModemCount": casaCmtsUSActiveModemCount,
       "casaCmtsUSRegisteredModemCount": casaCmtsUSRegisteredModemCount,
       "casaCmtsUSTotalModemCount": casaCmtsUSTotalModemCount,
       "casaCmtsDSModemTable": casaCmtsDSModemTable,
       "casaCmtsDSModemEntry": casaCmtsDSModemEntry,
       "casaCmtsDSActiveModemCount": casaCmtsDSActiveModemCount,
       "casaCmtsDSRegisteredModemCount": casaCmtsDSRegisteredModemCount,
       "casaCmtsDSTotalModemCount": casaCmtsDSTotalModemCount,
       "casaCmtsCmCpeTable": casaCmtsCmCpeTable,
       "casaCmtsCmCpeEntry": casaCmtsCmCpeEntry,
       "casaCmtsCmCpeMacAddress": casaCmtsCmCpeMacAddress,
       "casaCmtsCmCpeType": casaCmtsCmCpeType,
       "casaCmtsCmCpeIpAddress": casaCmtsCmCpeIpAddress,
       "casaCmtsCmCpeIfIndex": casaCmtsCmCpeIfIndex,
       "casaCmtsCmCpeCmtsServiceId": casaCmtsCmCpeCmtsServiceId,
       "casaCmtsCmCpeCmStatusIndex": casaCmtsCmCpeCmStatusIndex,
       "casaCmtsCmCpeResetNow": casaCmtsCmCpeResetNow,
       "casaCmtsCpeIpNetToPhysicalTable": casaCmtsCpeIpNetToPhysicalTable,
       "casaCmtsCpeIpNetToPhysicalEntry": casaCmtsCpeIpNetToPhysicalEntry,
       "casaCmtsCpeIpNetToPhysicalIfIndex": casaCmtsCpeIpNetToPhysicalIfIndex,
       "casaCmtsCpeIpNetToPhysicalNetAddressType": casaCmtsCpeIpNetToPhysicalNetAddressType,
       "casaCmtsCpeIpNetToPhysicalNetAddress": casaCmtsCpeIpNetToPhysicalNetAddress,
       "casaCmtsCpeIpNetToPhysicalCmPhysAddress": casaCmtsCpeIpNetToPhysicalCmPhysAddress,
       "casaCmtsCpeIpNetToPhysicalType": casaCmtsCpeIpNetToPhysicalType,
       "casaCmtsCmReset": casaCmtsCmReset,
       "casaCmtsCmResetByIpAddr": casaCmtsCmResetByIpAddr,
       "casaCmtsCmResetByMacAddr": casaCmtsCmResetByMacAddr,
       "casaCmtsCmResetAll": casaCmtsCmResetAll,
       "casaCmCpeGroups": casaCmCpeGroups,
       "casaCmCpeGroup": casaCmCpeGroup,
       "casaCmCpeCompliances": casaCmCpeCompliances,
       "casaCmCpeCompliance": casaCmCpeCompliance}
)
