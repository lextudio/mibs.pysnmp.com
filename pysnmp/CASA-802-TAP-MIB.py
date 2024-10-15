# SNMP MIB module (CASA-802-TAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CASA-802-TAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:36 2024
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

(pktcEScTapMediationContentId,) = mibBuilder.importSymbols(
    "PKTC-ES-TAP-MIB",
    "pktcEScTapMediationContentId")

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

casa802TapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19)
)
casa802TapMIB.setRevisions(
        ("2008-11-19 11:11",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CasaMgmt_ObjectIdentity = ObjectIdentity
casaMgmt = _CasaMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10)
)
_Casa802TapMIBNotifs_ObjectIdentity = ObjectIdentity
casa802TapMIBNotifs = _Casa802TapMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 0)
)
_Casa802TapMIBObjects_ObjectIdentity = ObjectIdentity
casa802TapMIBObjects = _Casa802TapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1)
)
_Casa802tapStreamEncodePacket_ObjectIdentity = ObjectIdentity
casa802tapStreamEncodePacket = _Casa802tapStreamEncodePacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1)
)


class _Casa802tapStreamCapabilities_Type(Bits):
    """Custom type casa802tapStreamCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dstLlcSap", 5),
          ("dstMacAddr", 2),
          ("ethernetPid", 4),
          ("interface", 1),
          ("srcLlcSap", 6),
          ("srcMacAddr", 3),
          ("tapEnable", 0))
    )

_Casa802tapStreamCapabilities_Type.__name__ = "Bits"
_Casa802tapStreamCapabilities_Object = MibScalar
casa802tapStreamCapabilities = _Casa802tapStreamCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 1),
    _Casa802tapStreamCapabilities_Type()
)
casa802tapStreamCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casa802tapStreamCapabilities.setStatus("current")
_Casa802tapStreamTable_Object = MibTable
casa802tapStreamTable = _Casa802tapStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2)
)
if mibBuilder.loadTexts:
    casa802tapStreamTable.setStatus("current")
_Casa802tapStreamEntry_Object = MibTableRow
casa802tapStreamEntry = _Casa802tapStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1)
)
casa802tapStreamEntry.setIndexNames(
    (0, "PKTC-ES-TAP-MIB", "pktcEScTapMediationContentId"),
    (0, "CASA-802-TAP-MIB", "casa802tapStreamIndex"),
)
if mibBuilder.loadTexts:
    casa802tapStreamEntry.setStatus("current")


class _Casa802tapStreamIndex_Type(Integer32):
    """Custom type casa802tapStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Casa802tapStreamIndex_Type.__name__ = "Integer32"
_Casa802tapStreamIndex_Object = MibTableColumn
casa802tapStreamIndex = _Casa802tapStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 1),
    _Casa802tapStreamIndex_Type()
)
casa802tapStreamIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    casa802tapStreamIndex.setStatus("current")


class _Casa802tapStreamFields_Type(Bits):
    """Custom type casa802tapStreamFields based on Bits"""
    namedValues = NamedValues(
        *(("dstLlcSap", 4),
          ("dstMacAddress", 1),
          ("ethernetPid", 3),
          ("interface", 0),
          ("srcLlcSap", 5),
          ("srcMacAddress", 2))
    )

_Casa802tapStreamFields_Type.__name__ = "Bits"
_Casa802tapStreamFields_Object = MibTableColumn
casa802tapStreamFields = _Casa802tapStreamFields_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 2),
    _Casa802tapStreamFields_Type()
)
casa802tapStreamFields.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casa802tapStreamFields.setStatus("current")


class _Casa802tapStreamInterface_Type(Integer32):
    """Custom type casa802tapStreamInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_Casa802tapStreamInterface_Type.__name__ = "Integer32"
_Casa802tapStreamInterface_Object = MibTableColumn
casa802tapStreamInterface = _Casa802tapStreamInterface_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 3),
    _Casa802tapStreamInterface_Type()
)
casa802tapStreamInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casa802tapStreamInterface.setStatus("current")
_Casa802tapStreamDestinationAddress_Type = MacAddress
_Casa802tapStreamDestinationAddress_Object = MibTableColumn
casa802tapStreamDestinationAddress = _Casa802tapStreamDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 4),
    _Casa802tapStreamDestinationAddress_Type()
)
casa802tapStreamDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casa802tapStreamDestinationAddress.setStatus("current")
_Casa802tapStreamSourceAddress_Type = MacAddress
_Casa802tapStreamSourceAddress_Object = MibTableColumn
casa802tapStreamSourceAddress = _Casa802tapStreamSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 5),
    _Casa802tapStreamSourceAddress_Type()
)
casa802tapStreamSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casa802tapStreamSourceAddress.setStatus("current")
_Casa802tapStreamEthernetPid_Type = Unsigned32
_Casa802tapStreamEthernetPid_Object = MibTableColumn
casa802tapStreamEthernetPid = _Casa802tapStreamEthernetPid_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 6),
    _Casa802tapStreamEthernetPid_Type()
)
casa802tapStreamEthernetPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casa802tapStreamEthernetPid.setStatus("current")
_Casa802tapStreamDestinationLlcSap_Type = Unsigned32
_Casa802tapStreamDestinationLlcSap_Object = MibTableColumn
casa802tapStreamDestinationLlcSap = _Casa802tapStreamDestinationLlcSap_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 7),
    _Casa802tapStreamDestinationLlcSap_Type()
)
casa802tapStreamDestinationLlcSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casa802tapStreamDestinationLlcSap.setStatus("current")
_Casa802tapStreamSourceLlcSap_Type = Unsigned32
_Casa802tapStreamSourceLlcSap_Object = MibTableColumn
casa802tapStreamSourceLlcSap = _Casa802tapStreamSourceLlcSap_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 8),
    _Casa802tapStreamSourceLlcSap_Type()
)
casa802tapStreamSourceLlcSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casa802tapStreamSourceLlcSap.setStatus("current")


class _Casa802tapStreamInterceptEnable_Type(Integer32):
    """Custom type casa802tapStreamInterceptEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Casa802tapStreamInterceptEnable_Type.__name__ = "Integer32"
_Casa802tapStreamInterceptEnable_Object = MibTableColumn
casa802tapStreamInterceptEnable = _Casa802tapStreamInterceptEnable_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 9),
    _Casa802tapStreamInterceptEnable_Type()
)
casa802tapStreamInterceptEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casa802tapStreamInterceptEnable.setStatus("current")
_Casa802tapStreamStatus_Type = RowStatus
_Casa802tapStreamStatus_Object = MibTableColumn
casa802tapStreamStatus = _Casa802tapStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 1, 1, 2, 1, 10),
    _Casa802tapStreamStatus_Type()
)
casa802tapStreamStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    casa802tapStreamStatus.setStatus("current")
_Casa802TapMIBConform_ObjectIdentity = ObjectIdentity
casa802TapMIBConform = _Casa802TapMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 2)
)
_Casa802TapMIBCompliances_ObjectIdentity = ObjectIdentity
casa802TapMIBCompliances = _Casa802TapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 2, 1)
)
_Casa802TapMIBGroups_ObjectIdentity = ObjectIdentity
casa802TapMIBGroups = _Casa802TapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 2, 2)
)

# Managed Objects groups

casa802TapStreamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 2, 2, 1)
)
casa802TapStreamGroup.setObjects(
      *(("CASA-802-TAP-MIB", "casa802tapStreamCapabilities"),
        ("CASA-802-TAP-MIB", "casa802tapStreamFields"),
        ("CASA-802-TAP-MIB", "casa802tapStreamInterface"),
        ("CASA-802-TAP-MIB", "casa802tapStreamDestinationAddress"),
        ("CASA-802-TAP-MIB", "casa802tapStreamSourceAddress"),
        ("CASA-802-TAP-MIB", "casa802tapStreamEthernetPid"),
        ("CASA-802-TAP-MIB", "casa802tapStreamSourceLlcSap"),
        ("CASA-802-TAP-MIB", "casa802tapStreamDestinationLlcSap"),
        ("CASA-802-TAP-MIB", "casa802tapStreamStatus"))
)
if mibBuilder.loadTexts:
    casa802TapStreamGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

casa802TapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20858, 10, 19, 2, 1, 1)
)
if mibBuilder.loadTexts:
    casa802TapMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CASA-802-TAP-MIB",
    **{"casaMgmt": casaMgmt,
       "casa802TapMIB": casa802TapMIB,
       "casa802TapMIBNotifs": casa802TapMIBNotifs,
       "casa802TapMIBObjects": casa802TapMIBObjects,
       "casa802tapStreamEncodePacket": casa802tapStreamEncodePacket,
       "casa802tapStreamCapabilities": casa802tapStreamCapabilities,
       "casa802tapStreamTable": casa802tapStreamTable,
       "casa802tapStreamEntry": casa802tapStreamEntry,
       "casa802tapStreamIndex": casa802tapStreamIndex,
       "casa802tapStreamFields": casa802tapStreamFields,
       "casa802tapStreamInterface": casa802tapStreamInterface,
       "casa802tapStreamDestinationAddress": casa802tapStreamDestinationAddress,
       "casa802tapStreamSourceAddress": casa802tapStreamSourceAddress,
       "casa802tapStreamEthernetPid": casa802tapStreamEthernetPid,
       "casa802tapStreamDestinationLlcSap": casa802tapStreamDestinationLlcSap,
       "casa802tapStreamSourceLlcSap": casa802tapStreamSourceLlcSap,
       "casa802tapStreamInterceptEnable": casa802tapStreamInterceptEnable,
       "casa802tapStreamStatus": casa802tapStreamStatus,
       "casa802TapMIBConform": casa802TapMIBConform,
       "casa802TapMIBCompliances": casa802TapMIBCompliances,
       "casa802TapMIBCompliance": casa802TapMIBCompliance,
       "casa802TapMIBGroups": casa802TapMIBGroups,
       "casa802TapStreamGroup": casa802TapStreamGroup}
)
