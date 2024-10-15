# SNMP MIB module (CISCO-CABLE-DSG-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CABLE-DSG-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:35 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoCableDsgIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999)
)
ciscoCableDsgIfMIB.setRevisions(
        ("2004-03-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CcdsgIfCaVendor_ObjectIdentity = ObjectIdentity
ccdsgIfCaVendor = _CcdsgIfCaVendor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1)
)
_CcdsgIfCaVendorTable_Object = MibTable
ccdsgIfCaVendorTable = _CcdsgIfCaVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 1)
)
if mibBuilder.loadTexts:
    ccdsgIfCaVendorTable.setStatus("current")
_CcdsgIfCaVendorEntry_Object = MibTableRow
ccdsgIfCaVendorEntry = _CcdsgIfCaVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 1, 1)
)
ccdsgIfCaVendorEntry.setIndexNames(
    (0, "CISCO-CABLE-DSG-IF-MIB", "ccdsgIfCaVendorIndex"),
)
if mibBuilder.loadTexts:
    ccdsgIfCaVendorEntry.setStatus("current")


class _CcdsgIfCaVendorIndex_Type(Unsigned32):
    """Custom type ccdsgIfCaVendorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcdsgIfCaVendorIndex_Type.__name__ = "Unsigned32"
_CcdsgIfCaVendorIndex_Object = MibTableColumn
ccdsgIfCaVendorIndex = _CcdsgIfCaVendorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 1, 1, 1),
    _CcdsgIfCaVendorIndex_Type()
)
ccdsgIfCaVendorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccdsgIfCaVendorIndex.setStatus("current")


class _CcdsgIfCaVendorName_Type(SnmpAdminString):
    """Custom type ccdsgIfCaVendorName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CcdsgIfCaVendorName_Type.__name__ = "SnmpAdminString"
_CcdsgIfCaVendorName_Object = MibTableColumn
ccdsgIfCaVendorName = _CcdsgIfCaVendorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 1, 1, 2),
    _CcdsgIfCaVendorName_Type()
)
ccdsgIfCaVendorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccdsgIfCaVendorName.setStatus("current")


class _CcdsgIfCaVendorTunnelCnt_Type(Integer32):
    """Custom type ccdsgIfCaVendorTunnelCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CcdsgIfCaVendorTunnelCnt_Type.__name__ = "Integer32"
_CcdsgIfCaVendorTunnelCnt_Object = MibTableColumn
ccdsgIfCaVendorTunnelCnt = _CcdsgIfCaVendorTunnelCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 1, 1, 3),
    _CcdsgIfCaVendorTunnelCnt_Type()
)
ccdsgIfCaVendorTunnelCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsgIfCaVendorTunnelCnt.setStatus("current")
_CcdsgIfCaVendorRowStatus_Type = RowStatus
_CcdsgIfCaVendorRowStatus_Object = MibTableColumn
ccdsgIfCaVendorRowStatus = _CcdsgIfCaVendorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 1, 1, 4),
    _CcdsgIfCaVendorRowStatus_Type()
)
ccdsgIfCaVendorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccdsgIfCaVendorRowStatus.setStatus("current")
_CcdsgIfTunnel_ObjectIdentity = ObjectIdentity
ccdsgIfTunnel = _CcdsgIfTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2)
)
_CcdsgIfTunnelTable_Object = MibTable
ccdsgIfTunnelTable = _CcdsgIfTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1)
)
if mibBuilder.loadTexts:
    ccdsgIfTunnelTable.setStatus("current")
_CcdsgIfTunnelEntry_Object = MibTableRow
ccdsgIfTunnelEntry = _CcdsgIfTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1)
)
ccdsgIfTunnelEntry.setIndexNames(
    (0, "CISCO-CABLE-DSG-IF-MIB", "ccdsgIfTunnelIndex"),
)
if mibBuilder.loadTexts:
    ccdsgIfTunnelEntry.setStatus("current")


class _CcdsgIfTunnelIndex_Type(Unsigned32):
    """Custom type ccdsgIfTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcdsgIfTunnelIndex_Type.__name__ = "Unsigned32"
_CcdsgIfTunnelIndex_Object = MibTableColumn
ccdsgIfTunnelIndex = _CcdsgIfTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1, 1),
    _CcdsgIfTunnelIndex_Type()
)
ccdsgIfTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccdsgIfTunnelIndex.setStatus("current")
_CcdsgIfTunnelInAddressType_Type = InetAddressType
_CcdsgIfTunnelInAddressType_Object = MibTableColumn
ccdsgIfTunnelInAddressType = _CcdsgIfTunnelInAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1, 2),
    _CcdsgIfTunnelInAddressType_Type()
)
ccdsgIfTunnelInAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccdsgIfTunnelInAddressType.setStatus("current")
_CcdsgIfTunnelInIpAddress_Type = InetAddress
_CcdsgIfTunnelInIpAddress_Object = MibTableColumn
ccdsgIfTunnelInIpAddress = _CcdsgIfTunnelInIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1, 3),
    _CcdsgIfTunnelInIpAddress_Type()
)
ccdsgIfTunnelInIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccdsgIfTunnelInIpAddress.setStatus("current")
_CcdsgIfTunnelMacAddress_Type = MacAddress
_CcdsgIfTunnelMacAddress_Object = MibTableColumn
ccdsgIfTunnelMacAddress = _CcdsgIfTunnelMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1, 4),
    _CcdsgIfTunnelMacAddress_Type()
)
ccdsgIfTunnelMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccdsgIfTunnelMacAddress.setStatus("current")


class _CcdsgIfTunnelCaVendorIndex_Type(Unsigned32):
    """Custom type ccdsgIfTunnelCaVendorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcdsgIfTunnelCaVendorIndex_Type.__name__ = "Unsigned32"
_CcdsgIfTunnelCaVendorIndex_Object = MibTableColumn
ccdsgIfTunnelCaVendorIndex = _CcdsgIfTunnelCaVendorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1, 5),
    _CcdsgIfTunnelCaVendorIndex_Type()
)
ccdsgIfTunnelCaVendorIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccdsgIfTunnelCaVendorIndex.setStatus("current")
_CcdsgIfTunnelRowStatus_Type = RowStatus
_CcdsgIfTunnelRowStatus_Object = MibTableColumn
ccdsgIfTunnelRowStatus = _CcdsgIfTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1, 6),
    _CcdsgIfTunnelRowStatus_Type()
)
ccdsgIfTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccdsgIfTunnelRowStatus.setStatus("current")
_CcdsgIfDownstream_ObjectIdentity = ObjectIdentity
ccdsgIfDownstream = _CcdsgIfDownstream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3)
)
_CcdsgIfDownstreamTable_Object = MibTable
ccdsgIfDownstreamTable = _CcdsgIfDownstreamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 1)
)
if mibBuilder.loadTexts:
    ccdsgIfDownstreamTable.setStatus("current")
_CcdsgIfDownstreamEntry_Object = MibTableRow
ccdsgIfDownstreamEntry = _CcdsgIfDownstreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 1, 1)
)
ccdsgIfDownstreamEntry.setIndexNames(
    (0, "CISCO-CABLE-DSG-IF-MIB", "ccdsgIfDownDsgIndex"),
)
if mibBuilder.loadTexts:
    ccdsgIfDownstreamEntry.setStatus("current")


class _CcdsgIfDownDsgIndex_Type(Unsigned32):
    """Custom type ccdsgIfDownDsgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcdsgIfDownDsgIndex_Type.__name__ = "Unsigned32"
_CcdsgIfDownDsgIndex_Object = MibTableColumn
ccdsgIfDownDsgIndex = _CcdsgIfDownDsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 1, 1, 1),
    _CcdsgIfDownDsgIndex_Type()
)
ccdsgIfDownDsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccdsgIfDownDsgIndex.setStatus("current")


class _CcdsgIfDownTunnelIndex_Type(Unsigned32):
    """Custom type ccdsgIfDownTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcdsgIfDownTunnelIndex_Type.__name__ = "Unsigned32"
_CcdsgIfDownTunnelIndex_Object = MibTableColumn
ccdsgIfDownTunnelIndex = _CcdsgIfDownTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 1, 1, 2),
    _CcdsgIfDownTunnelIndex_Type()
)
ccdsgIfDownTunnelIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccdsgIfDownTunnelIndex.setStatus("current")
_CcdsgIfDownIfIndex_Type = InterfaceIndex
_CcdsgIfDownIfIndex_Object = MibTableColumn
ccdsgIfDownIfIndex = _CcdsgIfDownIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 1, 1, 3),
    _CcdsgIfDownIfIndex_Type()
)
ccdsgIfDownIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccdsgIfDownIfIndex.setStatus("current")
_CcdsgIfDownRowStatus_Type = RowStatus
_CcdsgIfDownRowStatus_Object = MibTableColumn
ccdsgIfDownRowStatus = _CcdsgIfDownRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 3, 1, 1, 4),
    _CcdsgIfDownRowStatus_Type()
)
ccdsgIfDownRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccdsgIfDownRowStatus.setStatus("current")
_CiscoCableDsgIfConformance_ObjectIdentity = ObjectIdentity
ciscoCableDsgIfConformance = _CiscoCableDsgIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 4)
)
_CiscoCableDsgIfCompliances_ObjectIdentity = ObjectIdentity
ciscoCableDsgIfCompliances = _CiscoCableDsgIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 4, 1)
)
_CiscoCableDsgIfGroups_ObjectIdentity = ObjectIdentity
ciscoCableDsgIfGroups = _CiscoCableDsgIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 4, 2)
)

# Managed Objects groups

ccdsgIfCaVendorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 4, 2, 1)
)
ccdsgIfCaVendorGroup.setObjects(
      *(("CISCO-CABLE-DSG-IF-MIB", "ccdsgIfCaVendorName"),
        ("CISCO-CABLE-DSG-IF-MIB", "ccdsgIfCaVendorTunnelCnt"),
        ("CISCO-CABLE-DSG-IF-MIB", "ccdsgIfCaVendorRowStatus"))
)
if mibBuilder.loadTexts:
    ccdsgIfCaVendorGroup.setStatus("current")

ccdsgIfTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 4, 2, 2)
)
ccdsgIfTunnelGroup.setObjects(
      *(("CISCO-CABLE-DSG-IF-MIB", "ccdsgIfTunnelInAddressType"),
        ("CISCO-CABLE-DSG-IF-MIB", "ccdsgIfTunnelInIpAddress"),
        ("CISCO-CABLE-DSG-IF-MIB", "ccdsgIfTunnelMacAddress"),
        ("CISCO-CABLE-DSG-IF-MIB", "ccdsgIfTunnelCaVendorIndex"),
        ("CISCO-CABLE-DSG-IF-MIB", "ccdsgIfTunnelRowStatus"))
)
if mibBuilder.loadTexts:
    ccdsgIfTunnelGroup.setStatus("current")

ccdsgIfDownstreamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 4, 2, 3)
)
ccdsgIfDownstreamGroup.setObjects(
      *(("CISCO-CABLE-DSG-IF-MIB", "ccdsgIfDownTunnelIndex"),
        ("CISCO-CABLE-DSG-IF-MIB", "ccdsgIfDownIfIndex"),
        ("CISCO-CABLE-DSG-IF-MIB", "ccdsgIfDownRowStatus"))
)
if mibBuilder.loadTexts:
    ccdsgIfDownstreamGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ccdsgIfBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ccdsgIfBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CABLE-DSG-IF-MIB",
    **{"ciscoCableDsgIfMIB": ciscoCableDsgIfMIB,
       "ccdsgIfCaVendor": ccdsgIfCaVendor,
       "ccdsgIfCaVendorTable": ccdsgIfCaVendorTable,
       "ccdsgIfCaVendorEntry": ccdsgIfCaVendorEntry,
       "ccdsgIfCaVendorIndex": ccdsgIfCaVendorIndex,
       "ccdsgIfCaVendorName": ccdsgIfCaVendorName,
       "ccdsgIfCaVendorTunnelCnt": ccdsgIfCaVendorTunnelCnt,
       "ccdsgIfCaVendorRowStatus": ccdsgIfCaVendorRowStatus,
       "ccdsgIfTunnel": ccdsgIfTunnel,
       "ccdsgIfTunnelTable": ccdsgIfTunnelTable,
       "ccdsgIfTunnelEntry": ccdsgIfTunnelEntry,
       "ccdsgIfTunnelIndex": ccdsgIfTunnelIndex,
       "ccdsgIfTunnelInAddressType": ccdsgIfTunnelInAddressType,
       "ccdsgIfTunnelInIpAddress": ccdsgIfTunnelInIpAddress,
       "ccdsgIfTunnelMacAddress": ccdsgIfTunnelMacAddress,
       "ccdsgIfTunnelCaVendorIndex": ccdsgIfTunnelCaVendorIndex,
       "ccdsgIfTunnelRowStatus": ccdsgIfTunnelRowStatus,
       "ccdsgIfDownstream": ccdsgIfDownstream,
       "ccdsgIfDownstreamTable": ccdsgIfDownstreamTable,
       "ccdsgIfDownstreamEntry": ccdsgIfDownstreamEntry,
       "ccdsgIfDownDsgIndex": ccdsgIfDownDsgIndex,
       "ccdsgIfDownTunnelIndex": ccdsgIfDownTunnelIndex,
       "ccdsgIfDownIfIndex": ccdsgIfDownIfIndex,
       "ccdsgIfDownRowStatus": ccdsgIfDownRowStatus,
       "ciscoCableDsgIfConformance": ciscoCableDsgIfConformance,
       "ciscoCableDsgIfCompliances": ciscoCableDsgIfCompliances,
       "ccdsgIfBasicCompliance": ccdsgIfBasicCompliance,
       "ciscoCableDsgIfGroups": ciscoCableDsgIfGroups,
       "ccdsgIfCaVendorGroup": ccdsgIfCaVendorGroup,
       "ccdsgIfTunnelGroup": ccdsgIfTunnelGroup,
       "ccdsgIfDownstreamGroup": ccdsgIfDownstreamGroup}
)
