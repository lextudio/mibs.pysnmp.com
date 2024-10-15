# SNMP MIB module (PKTC-ES-IPTAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PKTC-ES-IPTAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:52 2024
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

(pktcESSupportMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcESSupportMibs")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(pktcEScTapMediationContentId,
 pktcEScTapStreamIndex) = mibBuilder.importSymbols(
    "PKTC-ES-TAP-MIB",
    "pktcEScTapMediationContentId",
    "pktcEScTapStreamIndex")

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

pktcESIpTapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2)
)
pktcESIpTapMIB.setRevisions(
        ("2008-04-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PktcESIpTapMIBNotifs_ObjectIdentity = ObjectIdentity
pktcESIpTapMIBNotifs = _PktcESIpTapMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 0)
)
_PktcESIpTapMIBObjects_ObjectIdentity = ObjectIdentity
pktcESIpTapMIBObjects = _PktcESIpTapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1)
)
_PktcESTapStreamEncodePacket_ObjectIdentity = ObjectIdentity
pktcESTapStreamEncodePacket = _PktcESTapStreamEncodePacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1)
)


class _PktcESTapStreamCapabilities_Type(Bits):
    """Custom type pktcESTapStreamCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dscp", 5),
          ("interface", 1),
          ("ipV4", 2),
          ("ipV6", 3),
          ("l4Port", 4),
          ("tapEnable", 0),
          ("voip", 6))
    )

_PktcESTapStreamCapabilities_Type.__name__ = "Bits"
_PktcESTapStreamCapabilities_Object = MibScalar
pktcESTapStreamCapabilities = _PktcESTapStreamCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 1),
    _PktcESTapStreamCapabilities_Type()
)
pktcESTapStreamCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcESTapStreamCapabilities.setStatus("current")
_PktcESTapStreamTable_Object = MibTable
pktcESTapStreamTable = _PktcESTapStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pktcESTapStreamTable.setStatus("current")
_PktcESTapStreamEntry_Object = MibTableRow
pktcESTapStreamEntry = _PktcESTapStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1)
)
pktcESTapStreamEntry.setIndexNames(
    (0, "PKTC-ES-TAP-MIB", "pktcEScTapMediationContentId"),
    (0, "PKTC-ES-TAP-MIB", "pktcEScTapStreamIndex"),
)
if mibBuilder.loadTexts:
    pktcESTapStreamEntry.setStatus("current")


class _PktcESTapStreamInterface_Type(Integer32):
    """Custom type pktcESTapStreamInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483647),
    )


_PktcESTapStreamInterface_Type.__name__ = "Integer32"
_PktcESTapStreamInterface_Object = MibTableColumn
pktcESTapStreamInterface = _PktcESTapStreamInterface_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 1),
    _PktcESTapStreamInterface_Type()
)
pktcESTapStreamInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamInterface.setStatus("current")


class _PktcESTapStreamAddrType_Type(InetAddressType):
    """Custom type pktcESTapStreamAddrType based on InetAddressType"""


_PktcESTapStreamAddrType_Object = MibTableColumn
pktcESTapStreamAddrType = _PktcESTapStreamAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 2),
    _PktcESTapStreamAddrType_Type()
)
pktcESTapStreamAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamAddrType.setStatus("current")


class _PktcESTapStreamDestinationAddress_Type(InetAddress):
    """Custom type pktcESTapStreamDestinationAddress based on InetAddress"""
    defaultHexValue = "00000000"


_PktcESTapStreamDestinationAddress_Object = MibTableColumn
pktcESTapStreamDestinationAddress = _PktcESTapStreamDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 3),
    _PktcESTapStreamDestinationAddress_Type()
)
pktcESTapStreamDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamDestinationAddress.setStatus("current")


class _PktcESTapStreamDestinationLength_Type(InetAddressPrefixLength):
    """Custom type pktcESTapStreamDestinationLength based on InetAddressPrefixLength"""
    defaultValue = 0


_PktcESTapStreamDestinationLength_Object = MibTableColumn
pktcESTapStreamDestinationLength = _PktcESTapStreamDestinationLength_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 4),
    _PktcESTapStreamDestinationLength_Type()
)
pktcESTapStreamDestinationLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamDestinationLength.setStatus("current")


class _PktcESTapStreamSourceAddress_Type(InetAddress):
    """Custom type pktcESTapStreamSourceAddress based on InetAddress"""
    defaultHexValue = "00000000"


_PktcESTapStreamSourceAddress_Object = MibTableColumn
pktcESTapStreamSourceAddress = _PktcESTapStreamSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 5),
    _PktcESTapStreamSourceAddress_Type()
)
pktcESTapStreamSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamSourceAddress.setStatus("current")


class _PktcESTapStreamSourceLength_Type(InetAddressPrefixLength):
    """Custom type pktcESTapStreamSourceLength based on InetAddressPrefixLength"""
    defaultValue = 0


_PktcESTapStreamSourceLength_Object = MibTableColumn
pktcESTapStreamSourceLength = _PktcESTapStreamSourceLength_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 6),
    _PktcESTapStreamSourceLength_Type()
)
pktcESTapStreamSourceLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamSourceLength.setStatus("current")


class _PktcESTapStreamTosByte_Type(Integer32):
    """Custom type pktcESTapStreamTosByte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PktcESTapStreamTosByte_Type.__name__ = "Integer32"
_PktcESTapStreamTosByte_Object = MibTableColumn
pktcESTapStreamTosByte = _PktcESTapStreamTosByte_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 7),
    _PktcESTapStreamTosByte_Type()
)
pktcESTapStreamTosByte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamTosByte.setStatus("current")


class _PktcESTapStreamTosByteMask_Type(Integer32):
    """Custom type pktcESTapStreamTosByteMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PktcESTapStreamTosByteMask_Type.__name__ = "Integer32"
_PktcESTapStreamTosByteMask_Object = MibTableColumn
pktcESTapStreamTosByteMask = _PktcESTapStreamTosByteMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 8),
    _PktcESTapStreamTosByteMask_Type()
)
pktcESTapStreamTosByteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamTosByteMask.setStatus("current")


class _PktcESTapStreamFlowId_Type(Integer32):
    """Custom type pktcESTapStreamFlowId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )


_PktcESTapStreamFlowId_Type.__name__ = "Integer32"
_PktcESTapStreamFlowId_Object = MibTableColumn
pktcESTapStreamFlowId = _PktcESTapStreamFlowId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 9),
    _PktcESTapStreamFlowId_Type()
)
pktcESTapStreamFlowId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamFlowId.setStatus("current")


class _PktcESTapStreamProtocol_Type(Integer32):
    """Custom type pktcESTapStreamProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_PktcESTapStreamProtocol_Type.__name__ = "Integer32"
_PktcESTapStreamProtocol_Object = MibTableColumn
pktcESTapStreamProtocol = _PktcESTapStreamProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 10),
    _PktcESTapStreamProtocol_Type()
)
pktcESTapStreamProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamProtocol.setStatus("current")


class _PktcESTapStreamDestL4PortMin_Type(InetPortNumber):
    """Custom type pktcESTapStreamDestL4PortMin based on InetPortNumber"""
    defaultValue = 0


_PktcESTapStreamDestL4PortMin_Object = MibTableColumn
pktcESTapStreamDestL4PortMin = _PktcESTapStreamDestL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 11),
    _PktcESTapStreamDestL4PortMin_Type()
)
pktcESTapStreamDestL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamDestL4PortMin.setStatus("current")


class _PktcESTapStreamDestL4PortMax_Type(InetPortNumber):
    """Custom type pktcESTapStreamDestL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_PktcESTapStreamDestL4PortMax_Object = MibTableColumn
pktcESTapStreamDestL4PortMax = _PktcESTapStreamDestL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 12),
    _PktcESTapStreamDestL4PortMax_Type()
)
pktcESTapStreamDestL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamDestL4PortMax.setStatus("current")


class _PktcESTapStreamSourceL4PortMin_Type(InetPortNumber):
    """Custom type pktcESTapStreamSourceL4PortMin based on InetPortNumber"""
    defaultValue = 0


_PktcESTapStreamSourceL4PortMin_Object = MibTableColumn
pktcESTapStreamSourceL4PortMin = _PktcESTapStreamSourceL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 13),
    _PktcESTapStreamSourceL4PortMin_Type()
)
pktcESTapStreamSourceL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamSourceL4PortMin.setStatus("current")


class _PktcESTapStreamSourceL4PortMax_Type(InetPortNumber):
    """Custom type pktcESTapStreamSourceL4PortMax based on InetPortNumber"""
    defaultValue = 65535


_PktcESTapStreamSourceL4PortMax_Object = MibTableColumn
pktcESTapStreamSourceL4PortMax = _PktcESTapStreamSourceL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 14),
    _PktcESTapStreamSourceL4PortMax_Type()
)
pktcESTapStreamSourceL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamSourceL4PortMax.setStatus("current")
_PktcESTapStreamVRF_Type = SnmpAdminString
_PktcESTapStreamVRF_Object = MibTableColumn
pktcESTapStreamVRF = _PktcESTapStreamVRF_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 15),
    _PktcESTapStreamVRF_Type()
)
pktcESTapStreamVRF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamVRF.setStatus("current")
_PktcESTapStreamStatus_Type = RowStatus
_PktcESTapStreamStatus_Object = MibTableColumn
pktcESTapStreamStatus = _PktcESTapStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 1, 1, 2, 1, 16),
    _PktcESTapStreamStatus_Type()
)
pktcESTapStreamStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcESTapStreamStatus.setStatus("current")
_PktcESIpTapMIBConform_ObjectIdentity = ObjectIdentity
pktcESIpTapMIBConform = _PktcESIpTapMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 2)
)
_PktcESIpTapMIBCompliances_ObjectIdentity = ObjectIdentity
pktcESIpTapMIBCompliances = _PktcESIpTapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 2, 1)
)
_PktcESIpTapMIBGroups_ObjectIdentity = ObjectIdentity
pktcESIpTapMIBGroups = _PktcESIpTapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 2, 2)
)

# Managed Objects groups

pktcESIpTapStreamComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 2, 2, 1)
)
pktcESIpTapStreamComplianceGroup.setObjects(
      *(("PKTC-ES-IPTAP-MIB", "pktcESTapStreamCapabilities"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamInterface"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamAddrType"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamDestinationAddress"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamDestinationLength"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamSourceAddress"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamSourceLength"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamTosByte"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamTosByteMask"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamFlowId"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamProtocol"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamDestL4PortMin"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamDestL4PortMax"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamSourceL4PortMin"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamSourceL4PortMax"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamVRF"),
        ("PKTC-ES-IPTAP-MIB", "pktcESTapStreamStatus"))
)
if mibBuilder.loadTexts:
    pktcESIpTapStreamComplianceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcESIpTapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcESIpTapMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-ES-IPTAP-MIB",
    **{"pktcESIpTapMIB": pktcESIpTapMIB,
       "pktcESIpTapMIBNotifs": pktcESIpTapMIBNotifs,
       "pktcESIpTapMIBObjects": pktcESIpTapMIBObjects,
       "pktcESTapStreamEncodePacket": pktcESTapStreamEncodePacket,
       "pktcESTapStreamCapabilities": pktcESTapStreamCapabilities,
       "pktcESTapStreamTable": pktcESTapStreamTable,
       "pktcESTapStreamEntry": pktcESTapStreamEntry,
       "pktcESTapStreamInterface": pktcESTapStreamInterface,
       "pktcESTapStreamAddrType": pktcESTapStreamAddrType,
       "pktcESTapStreamDestinationAddress": pktcESTapStreamDestinationAddress,
       "pktcESTapStreamDestinationLength": pktcESTapStreamDestinationLength,
       "pktcESTapStreamSourceAddress": pktcESTapStreamSourceAddress,
       "pktcESTapStreamSourceLength": pktcESTapStreamSourceLength,
       "pktcESTapStreamTosByte": pktcESTapStreamTosByte,
       "pktcESTapStreamTosByteMask": pktcESTapStreamTosByteMask,
       "pktcESTapStreamFlowId": pktcESTapStreamFlowId,
       "pktcESTapStreamProtocol": pktcESTapStreamProtocol,
       "pktcESTapStreamDestL4PortMin": pktcESTapStreamDestL4PortMin,
       "pktcESTapStreamDestL4PortMax": pktcESTapStreamDestL4PortMax,
       "pktcESTapStreamSourceL4PortMin": pktcESTapStreamSourceL4PortMin,
       "pktcESTapStreamSourceL4PortMax": pktcESTapStreamSourceL4PortMax,
       "pktcESTapStreamVRF": pktcESTapStreamVRF,
       "pktcESTapStreamStatus": pktcESTapStreamStatus,
       "pktcESIpTapMIBConform": pktcESIpTapMIBConform,
       "pktcESIpTapMIBCompliances": pktcESIpTapMIBCompliances,
       "pktcESIpTapMIBCompliance": pktcESIpTapMIBCompliance,
       "pktcESIpTapMIBGroups": pktcESIpTapMIBGroups,
       "pktcESIpTapStreamComplianceGroup": pktcESIpTapStreamComplianceGroup}
)
