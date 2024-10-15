# SNMP MIB module (CISCO-802-TAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-802-TAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:21 2024
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

cisco802TapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 395)
)
cisco802TapMIB.setRevisions(
        ("2004-03-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cisco802TapMIBNotifs_ObjectIdentity = ObjectIdentity
cisco802TapMIBNotifs = _Cisco802TapMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 0)
)
_Cisco802TapMIBObjects_ObjectIdentity = ObjectIdentity
cisco802TapMIBObjects = _Cisco802TapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 1)
)
_C802tapStreamEncodePacket_ObjectIdentity = ObjectIdentity
c802tapStreamEncodePacket = _C802tapStreamEncodePacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1)
)


class _C802tapStreamCapabilities_Type(Bits):
    """Custom type c802tapStreamCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dstLlcSap", 5),
          ("dstMacAddr", 2),
          ("ethernetPid", 4),
          ("interface", 1),
          ("srcLlcSap", 6),
          ("srcMacAddr", 3),
          ("tapEnable", 0))
    )

_C802tapStreamCapabilities_Type.__name__ = "Bits"
_C802tapStreamCapabilities_Object = MibScalar
c802tapStreamCapabilities = _C802tapStreamCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 1),
    _C802tapStreamCapabilities_Type()
)
c802tapStreamCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    c802tapStreamCapabilities.setStatus("current")
_C802tapStreamTable_Object = MibTable
c802tapStreamTable = _C802tapStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2)
)
if mibBuilder.loadTexts:
    c802tapStreamTable.setStatus("current")
_C802tapStreamEntry_Object = MibTableRow
c802tapStreamEntry = _C802tapStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1)
)
c802tapStreamEntry.setIndexNames(
    (0, "CISCO-TAP2-MIB", "cTap2MediationContentId"),
    (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"),
)
if mibBuilder.loadTexts:
    c802tapStreamEntry.setStatus("current")


class _C802tapStreamFields_Type(Bits):
    """Custom type c802tapStreamFields based on Bits"""
    namedValues = NamedValues(
        *(("dstLlcSap", 4),
          ("dstMacAddress", 1),
          ("ethernetPid", 3),
          ("interface", 0),
          ("srcLlcSap", 5),
          ("srcMacAddress", 2))
    )

_C802tapStreamFields_Type.__name__ = "Bits"
_C802tapStreamFields_Object = MibTableColumn
c802tapStreamFields = _C802tapStreamFields_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 1),
    _C802tapStreamFields_Type()
)
c802tapStreamFields.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c802tapStreamFields.setStatus("current")


class _C802tapStreamInterface_Type(Integer32):
    """Custom type c802tapStreamInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_C802tapStreamInterface_Type.__name__ = "Integer32"
_C802tapStreamInterface_Object = MibTableColumn
c802tapStreamInterface = _C802tapStreamInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 2),
    _C802tapStreamInterface_Type()
)
c802tapStreamInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c802tapStreamInterface.setStatus("current")
_C802tapStreamDestinationAddress_Type = MacAddress
_C802tapStreamDestinationAddress_Object = MibTableColumn
c802tapStreamDestinationAddress = _C802tapStreamDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 3),
    _C802tapStreamDestinationAddress_Type()
)
c802tapStreamDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c802tapStreamDestinationAddress.setStatus("current")
_C802tapStreamSourceAddress_Type = MacAddress
_C802tapStreamSourceAddress_Object = MibTableColumn
c802tapStreamSourceAddress = _C802tapStreamSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 4),
    _C802tapStreamSourceAddress_Type()
)
c802tapStreamSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c802tapStreamSourceAddress.setStatus("current")
_C802tapStreamEthernetPid_Type = Unsigned32
_C802tapStreamEthernetPid_Object = MibTableColumn
c802tapStreamEthernetPid = _C802tapStreamEthernetPid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 5),
    _C802tapStreamEthernetPid_Type()
)
c802tapStreamEthernetPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c802tapStreamEthernetPid.setStatus("current")
_C802tapStreamDestinationLlcSap_Type = Unsigned32
_C802tapStreamDestinationLlcSap_Object = MibTableColumn
c802tapStreamDestinationLlcSap = _C802tapStreamDestinationLlcSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 6),
    _C802tapStreamDestinationLlcSap_Type()
)
c802tapStreamDestinationLlcSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c802tapStreamDestinationLlcSap.setStatus("current")
_C802tapStreamSourceLlcSap_Type = Unsigned32
_C802tapStreamSourceLlcSap_Object = MibTableColumn
c802tapStreamSourceLlcSap = _C802tapStreamSourceLlcSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 7),
    _C802tapStreamSourceLlcSap_Type()
)
c802tapStreamSourceLlcSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c802tapStreamSourceLlcSap.setStatus("current")
_C802tapStreamStatus_Type = RowStatus
_C802tapStreamStatus_Object = MibTableColumn
c802tapStreamStatus = _C802tapStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 8),
    _C802tapStreamStatus_Type()
)
c802tapStreamStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    c802tapStreamStatus.setStatus("current")
_Cisco802TapMIBConform_ObjectIdentity = ObjectIdentity
cisco802TapMIBConform = _Cisco802TapMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 2)
)
_Cisco802TapMIBCompliances_ObjectIdentity = ObjectIdentity
cisco802TapMIBCompliances = _Cisco802TapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 2, 1)
)
_Cisco802TapMIBGroups_ObjectIdentity = ObjectIdentity
cisco802TapMIBGroups = _Cisco802TapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 2, 2)
)

# Managed Objects groups

cisco802TapStreamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 2, 2, 1)
)
cisco802TapStreamGroup.setObjects(
      *(("CISCO-802-TAP-MIB", "c802tapStreamCapabilities"),
        ("CISCO-802-TAP-MIB", "c802tapStreamFields"),
        ("CISCO-802-TAP-MIB", "c802tapStreamInterface"),
        ("CISCO-802-TAP-MIB", "c802tapStreamDestinationAddress"),
        ("CISCO-802-TAP-MIB", "c802tapStreamSourceAddress"),
        ("CISCO-802-TAP-MIB", "c802tapStreamEthernetPid"),
        ("CISCO-802-TAP-MIB", "c802tapStreamSourceLlcSap"),
        ("CISCO-802-TAP-MIB", "c802tapStreamDestinationLlcSap"),
        ("CISCO-802-TAP-MIB", "c802tapStreamStatus"))
)
if mibBuilder.loadTexts:
    cisco802TapStreamGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cisco802TapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 395, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cisco802TapMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-802-TAP-MIB",
    **{"cisco802TapMIB": cisco802TapMIB,
       "cisco802TapMIBNotifs": cisco802TapMIBNotifs,
       "cisco802TapMIBObjects": cisco802TapMIBObjects,
       "c802tapStreamEncodePacket": c802tapStreamEncodePacket,
       "c802tapStreamCapabilities": c802tapStreamCapabilities,
       "c802tapStreamTable": c802tapStreamTable,
       "c802tapStreamEntry": c802tapStreamEntry,
       "c802tapStreamFields": c802tapStreamFields,
       "c802tapStreamInterface": c802tapStreamInterface,
       "c802tapStreamDestinationAddress": c802tapStreamDestinationAddress,
       "c802tapStreamSourceAddress": c802tapStreamSourceAddress,
       "c802tapStreamEthernetPid": c802tapStreamEthernetPid,
       "c802tapStreamDestinationLlcSap": c802tapStreamDestinationLlcSap,
       "c802tapStreamSourceLlcSap": c802tapStreamSourceLlcSap,
       "c802tapStreamStatus": c802tapStreamStatus,
       "cisco802TapMIBConform": cisco802TapMIBConform,
       "cisco802TapMIBCompliances": cisco802TapMIBCompliances,
       "cisco802TapMIBCompliance": cisco802TapMIBCompliance,
       "cisco802TapMIBGroups": cisco802TapMIBGroups,
       "cisco802TapStreamGroup": cisco802TapStreamGroup}
)
