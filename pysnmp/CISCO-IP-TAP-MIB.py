# SNMP MIB module (CISCO-IP-TAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IP-TAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:46 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(cTap2MediationContentId,
 cTap2StreamIndex) = mibBuilder.importSymbols(
    "CISCO-TAP2-MIB",
    "cTap2MediationContentId",
    "cTap2StreamIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoIpTapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 394)
)
ciscoIpTapMIB.setRevisions(
        ("2004-03-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIpTapMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIpTapMIBNotifs = _CiscoIpTapMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 0)
)
_CiscoIpTapMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpTapMIBObjects = _CiscoIpTapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1)
)
_CitapStreamEncodePacket_ObjectIdentity = ObjectIdentity
citapStreamEncodePacket = _CitapStreamEncodePacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1)
)


class _CitapStreamCapabilities_Type(Bits):
    """Custom type citapStreamCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dscp", 5),
          ("interface", 1),
          ("ipV4", 2),
          ("ipV6", 3),
          ("l4Port", 4),
          ("tapEnable", 0),
          ("voip", 6))
    )

_CitapStreamCapabilities_Type.__name__ = "Bits"
_CitapStreamCapabilities_Object = MibScalar
citapStreamCapabilities = _CitapStreamCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 1),
    _CitapStreamCapabilities_Type()
)
citapStreamCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    citapStreamCapabilities.setStatus("current")
_CitapStreamTable_Object = MibTable
citapStreamTable = _CitapStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2)
)
if mibBuilder.loadTexts:
    citapStreamTable.setStatus("current")
_CitapStreamEntry_Object = MibTableRow
citapStreamEntry = _CitapStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1)
)
citapStreamEntry.setIndexNames(
    (0, "CISCO-TAP2-MIB", "cTap2MediationContentId"),
    (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"),
)
if mibBuilder.loadTexts:
    citapStreamEntry.setStatus("current")


class _CitapStreamInterface_Type(Integer32):
    """Custom type citapStreamInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_CitapStreamInterface_Type.__name__ = "Integer32"
_CitapStreamInterface_Object = MibTableColumn
citapStreamInterface = _CitapStreamInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 1),
    _CitapStreamInterface_Type()
)
citapStreamInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamInterface.setStatus("current")


class _CitapStreamAddrType_Type(InetAddressType):
    """Custom type citapStreamAddrType based on InetAddressType"""


_CitapStreamAddrType_Object = MibTableColumn
citapStreamAddrType = _CitapStreamAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 2),
    _CitapStreamAddrType_Type()
)
citapStreamAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamAddrType.setStatus("current")


class _CitapStreamDestinationAddress_Type(InetAddress):
    """Custom type citapStreamDestinationAddress based on InetAddress"""
    defaultHexValue = "00000000"


_CitapStreamDestinationAddress_Object = MibTableColumn
citapStreamDestinationAddress = _CitapStreamDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 3),
    _CitapStreamDestinationAddress_Type()
)
citapStreamDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamDestinationAddress.setStatus("current")


class _CitapStreamDestinationLength_Type(InetAddressPrefixLength):
    """Custom type citapStreamDestinationLength based on InetAddressPrefixLength"""
    defaultValue = 0


_CitapStreamDestinationLength_Object = MibTableColumn
citapStreamDestinationLength = _CitapStreamDestinationLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 4),
    _CitapStreamDestinationLength_Type()
)
citapStreamDestinationLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamDestinationLength.setStatus("current")


class _CitapStreamSourceAddress_Type(InetAddress):
    """Custom type citapStreamSourceAddress based on InetAddress"""
    defaultHexValue = "00000000"


_CitapStreamSourceAddress_Object = MibTableColumn
citapStreamSourceAddress = _CitapStreamSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 5),
    _CitapStreamSourceAddress_Type()
)
citapStreamSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamSourceAddress.setStatus("current")


class _CitapStreamSourceLength_Type(InetAddressPrefixLength):
    """Custom type citapStreamSourceLength based on InetAddressPrefixLength"""
    defaultValue = 0


_CitapStreamSourceLength_Object = MibTableColumn
citapStreamSourceLength = _CitapStreamSourceLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 6),
    _CitapStreamSourceLength_Type()
)
citapStreamSourceLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamSourceLength.setStatus("current")


class _CitapStreamTosByte_Type(Integer32):
    """Custom type citapStreamTosByte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CitapStreamTosByte_Type.__name__ = "Integer32"
_CitapStreamTosByte_Object = MibTableColumn
citapStreamTosByte = _CitapStreamTosByte_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 7),
    _CitapStreamTosByte_Type()
)
citapStreamTosByte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamTosByte.setStatus("current")


class _CitapStreamTosByteMask_Type(Integer32):
    """Custom type citapStreamTosByteMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CitapStreamTosByteMask_Type.__name__ = "Integer32"
_CitapStreamTosByteMask_Object = MibTableColumn
citapStreamTosByteMask = _CitapStreamTosByteMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 8),
    _CitapStreamTosByteMask_Type()
)
citapStreamTosByteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamTosByteMask.setStatus("current")


class _CitapStreamFlowId_Type(Integer32):
    """Custom type citapStreamFlowId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )


_CitapStreamFlowId_Type.__name__ = "Integer32"
_CitapStreamFlowId_Object = MibTableColumn
citapStreamFlowId = _CitapStreamFlowId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 9),
    _CitapStreamFlowId_Type()
)
citapStreamFlowId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamFlowId.setStatus("current")


class _CitapStreamProtocol_Type(Integer32):
    """Custom type citapStreamProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_CitapStreamProtocol_Type.__name__ = "Integer32"
_CitapStreamProtocol_Object = MibTableColumn
citapStreamProtocol = _CitapStreamProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 10),
    _CitapStreamProtocol_Type()
)
citapStreamProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamProtocol.setStatus("current")


class _CitapStreamDestL4PortMin_Type(InetPortNumber):
    """Custom type citapStreamDestL4PortMin based on InetPortNumber"""
    defaultValue = 0


_CitapStreamDestL4PortMin_Object = MibTableColumn
citapStreamDestL4PortMin = _CitapStreamDestL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 11),
    _CitapStreamDestL4PortMin_Type()
)
citapStreamDestL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamDestL4PortMin.setStatus("current")


class _CitapStreamDestL4PortMax_Type(InetPortNumber):
    """Custom type citapStreamDestL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_CitapStreamDestL4PortMax_Object = MibTableColumn
citapStreamDestL4PortMax = _CitapStreamDestL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 12),
    _CitapStreamDestL4PortMax_Type()
)
citapStreamDestL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamDestL4PortMax.setStatus("current")


class _CitapStreamSourceL4PortMin_Type(InetPortNumber):
    """Custom type citapStreamSourceL4PortMin based on InetPortNumber"""
    defaultValue = 0


_CitapStreamSourceL4PortMin_Object = MibTableColumn
citapStreamSourceL4PortMin = _CitapStreamSourceL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 13),
    _CitapStreamSourceL4PortMin_Type()
)
citapStreamSourceL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamSourceL4PortMin.setStatus("current")


class _CitapStreamSourceL4PortMax_Type(InetPortNumber):
    """Custom type citapStreamSourceL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_CitapStreamSourceL4PortMax_Object = MibTableColumn
citapStreamSourceL4PortMax = _CitapStreamSourceL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 14),
    _CitapStreamSourceL4PortMax_Type()
)
citapStreamSourceL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamSourceL4PortMax.setStatus("current")
_CitapStreamVRF_Type = SnmpAdminString
_CitapStreamVRF_Object = MibTableColumn
citapStreamVRF = _CitapStreamVRF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 15),
    _CitapStreamVRF_Type()
)
citapStreamVRF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamVRF.setStatus("current")
_CitapStreamStatus_Type = RowStatus
_CitapStreamStatus_Object = MibTableColumn
citapStreamStatus = _CitapStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 1, 1, 2, 1, 16),
    _CitapStreamStatus_Type()
)
citapStreamStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    citapStreamStatus.setStatus("current")
_CiscoIpTapMIBConform_ObjectIdentity = ObjectIdentity
ciscoIpTapMIBConform = _CiscoIpTapMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 2)
)
_CiscoIpTapMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpTapMIBCompliances = _CiscoIpTapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 2, 1)
)
_CiscoIpTapMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpTapMIBGroups = _CiscoIpTapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 2, 2)
)

# Managed Objects groups

ciscoIpTapStreamComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 2, 2, 1)
)
ciscoIpTapStreamComplianceGroup.setObjects(
      *(("CISCO-IP-TAP-MIB", "citapStreamCapabilities"),
        ("CISCO-IP-TAP-MIB", "citapStreamInterface"),
        ("CISCO-IP-TAP-MIB", "citapStreamAddrType"),
        ("CISCO-IP-TAP-MIB", "citapStreamDestinationAddress"),
        ("CISCO-IP-TAP-MIB", "citapStreamDestinationLength"),
        ("CISCO-IP-TAP-MIB", "citapStreamSourceAddress"),
        ("CISCO-IP-TAP-MIB", "citapStreamSourceLength"),
        ("CISCO-IP-TAP-MIB", "citapStreamTosByte"),
        ("CISCO-IP-TAP-MIB", "citapStreamTosByteMask"),
        ("CISCO-IP-TAP-MIB", "citapStreamFlowId"),
        ("CISCO-IP-TAP-MIB", "citapStreamProtocol"),
        ("CISCO-IP-TAP-MIB", "citapStreamDestL4PortMin"),
        ("CISCO-IP-TAP-MIB", "citapStreamDestL4PortMax"),
        ("CISCO-IP-TAP-MIB", "citapStreamSourceL4PortMin"),
        ("CISCO-IP-TAP-MIB", "citapStreamSourceL4PortMax"),
        ("CISCO-IP-TAP-MIB", "citapStreamVRF"),
        ("CISCO-IP-TAP-MIB", "citapStreamStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpTapStreamComplianceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIpTapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 394, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpTapMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IP-TAP-MIB",
    **{"ciscoIpTapMIB": ciscoIpTapMIB,
       "ciscoIpTapMIBNotifs": ciscoIpTapMIBNotifs,
       "ciscoIpTapMIBObjects": ciscoIpTapMIBObjects,
       "citapStreamEncodePacket": citapStreamEncodePacket,
       "citapStreamCapabilities": citapStreamCapabilities,
       "citapStreamTable": citapStreamTable,
       "citapStreamEntry": citapStreamEntry,
       "citapStreamInterface": citapStreamInterface,
       "citapStreamAddrType": citapStreamAddrType,
       "citapStreamDestinationAddress": citapStreamDestinationAddress,
       "citapStreamDestinationLength": citapStreamDestinationLength,
       "citapStreamSourceAddress": citapStreamSourceAddress,
       "citapStreamSourceLength": citapStreamSourceLength,
       "citapStreamTosByte": citapStreamTosByte,
       "citapStreamTosByteMask": citapStreamTosByteMask,
       "citapStreamFlowId": citapStreamFlowId,
       "citapStreamProtocol": citapStreamProtocol,
       "citapStreamDestL4PortMin": citapStreamDestL4PortMin,
       "citapStreamDestL4PortMax": citapStreamDestL4PortMax,
       "citapStreamSourceL4PortMin": citapStreamSourceL4PortMin,
       "citapStreamSourceL4PortMax": citapStreamSourceL4PortMax,
       "citapStreamVRF": citapStreamVRF,
       "citapStreamStatus": citapStreamStatus,
       "ciscoIpTapMIBConform": ciscoIpTapMIBConform,
       "ciscoIpTapMIBCompliances": ciscoIpTapMIBCompliances,
       "ciscoIpTapMIBCompliance": ciscoIpTapMIBCompliance,
       "ciscoIpTapMIBGroups": ciscoIpTapMIBGroups,
       "ciscoIpTapStreamComplianceGroup": ciscoIpTapStreamComplianceGroup}
)
