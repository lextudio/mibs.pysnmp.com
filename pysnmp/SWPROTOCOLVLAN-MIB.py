# SNMP MIB module (SWPROTOCOLVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWPROTOCOLVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:32 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(dot1vProtocolPortEntry,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1vProtocolPortEntry")

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

swProtocolVLANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 16)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwProtocolVLANCtrl_ObjectIdentity = ObjectIdentity
swProtocolVLANCtrl = _SwProtocolVLANCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 16, 1)
)
_SwProtocolVLANTable_Object = MibTable
swProtocolVLANTable = _SwProtocolVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1)
)
if mibBuilder.loadTexts:
    swProtocolVLANTable.setStatus("obsolete")
_SwProtocolVLANEntry_Object = MibTableRow
swProtocolVLANEntry = _SwProtocolVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1)
)
swProtocolVLANEntry.setIndexNames(
    (0, "SWPROTOCOLVLAN-MIB", "swProtocolVLANIndex"),
)
if mibBuilder.loadTexts:
    swProtocolVLANEntry.setStatus("obsolete")


class _SwProtocolVLANIndex_Type(Integer32):
    """Custom type swProtocolVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwProtocolVLANIndex_Type.__name__ = "Integer32"
_SwProtocolVLANIndex_Object = MibTableColumn
swProtocolVLANIndex = _SwProtocolVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 1),
    _SwProtocolVLANIndex_Type()
)
swProtocolVLANIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swProtocolVLANIndex.setStatus("obsolete")


class _SwProtocolVLANName_Type(DisplayString):
    """Custom type swProtocolVLANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwProtocolVLANName_Type.__name__ = "DisplayString"
_SwProtocolVLANName_Object = MibTableColumn
swProtocolVLANName = _SwProtocolVLANName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 2),
    _SwProtocolVLANName_Type()
)
swProtocolVLANName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swProtocolVLANName.setStatus("obsolete")


class _SwProtocolVLANProtocolType_Type(Integer32):
    """Custom type swProtocolVLANProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("dot1q-vlan", 1),
          ("protocol-appleTalk", 7),
          ("protocol-decLat", 8),
          ("protocol-dexOther", 9),
          ("protocol-ip", 2),
          ("protocol-ipV6", 15),
          ("protocol-ipx802dot2", 4),
          ("protocol-ipx803dot3", 3),
          ("protocol-ipxEthernet2", 6),
          ("protocol-ipxSnap", 5),
          ("protocol-netBios", 12),
          ("protocol-rarp", 17),
          ("protocol-sna802dot2", 10),
          ("protocol-snaEthernet2", 11),
          ("protocol-userDefined", 16),
          ("protocol-vines", 14),
          ("protocol-xns", 13))
    )


_SwProtocolVLANProtocolType_Type.__name__ = "Integer32"
_SwProtocolVLANProtocolType_Object = MibTableColumn
swProtocolVLANProtocolType = _SwProtocolVLANProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 3),
    _SwProtocolVLANProtocolType_Type()
)
swProtocolVLANProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swProtocolVLANProtocolType.setStatus("obsolete")


class _SwProtocolVLANAdvertisement_Type(Integer32):
    """Custom type swProtocolVLANAdvertisement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwProtocolVLANAdvertisement_Type.__name__ = "Integer32"
_SwProtocolVLANAdvertisement_Object = MibTableColumn
swProtocolVLANAdvertisement = _SwProtocolVLANAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 4),
    _SwProtocolVLANAdvertisement_Type()
)
swProtocolVLANAdvertisement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swProtocolVLANAdvertisement.setStatus("obsolete")


class _SwProtocolVLANUserDefinedProtocol_Type(Integer32):
    """Custom type swProtocolVLANUserDefinedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwProtocolVLANUserDefinedProtocol_Type.__name__ = "Integer32"
_SwProtocolVLANUserDefinedProtocol_Object = MibTableColumn
swProtocolVLANUserDefinedProtocol = _SwProtocolVLANUserDefinedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 5),
    _SwProtocolVLANUserDefinedProtocol_Type()
)
swProtocolVLANUserDefinedProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swProtocolVLANUserDefinedProtocol.setStatus("obsolete")


class _SwProtocolVLANencap_Type(Integer32):
    """Custom type swProtocolVLANencap based on Integer32"""
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
        *(("all", 4),
          ("ethernet", 1),
          ("llc", 2),
          ("snap", 3))
    )


_SwProtocolVLANencap_Type.__name__ = "Integer32"
_SwProtocolVLANencap_Object = MibTableColumn
swProtocolVLANencap = _SwProtocolVLANencap_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 6),
    _SwProtocolVLANencap_Type()
)
swProtocolVLANencap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swProtocolVLANencap.setStatus("obsolete")
_SwProtocolVLANRowStatus_Type = RowStatus
_SwProtocolVLANRowStatus_Object = MibTableColumn
swProtocolVLANRowStatus = _SwProtocolVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 1, 1, 7),
    _SwProtocolVLANRowStatus_Type()
)
swProtocolVLANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swProtocolVLANRowStatus.setStatus("obsolete")
_Swdot1vProtocolPortTable_Object = MibTable
swdot1vProtocolPortTable = _Swdot1vProtocolPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 2)
)
if mibBuilder.loadTexts:
    swdot1vProtocolPortTable.setStatus("current")
_Swdot1vProtocolPortEntry_Object = MibTableRow
swdot1vProtocolPortEntry = _Swdot1vProtocolPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    swdot1vProtocolPortEntry.setStatus("current")


class _Swdot1vProtocolPortGroupPriority_Type(Integer32):
    """Custom type swdot1vProtocolPortGroupPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Swdot1vProtocolPortGroupPriority_Type.__name__ = "Integer32"
_Swdot1vProtocolPortGroupPriority_Object = MibTableColumn
swdot1vProtocolPortGroupPriority = _Swdot1vProtocolPortGroupPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 16, 1, 2, 1, 1),
    _Swdot1vProtocolPortGroupPriority_Type()
)
swdot1vProtocolPortGroupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swdot1vProtocolPortGroupPriority.setStatus("current")
dot1vProtocolPortEntry.registerAugmentions(
    ("SWPROTOCOLVLAN-MIB",
     "swdot1vProtocolPortEntry")
)
swdot1vProtocolPortEntry.setIndexNames(*dot1vProtocolPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWPROTOCOLVLAN-MIB",
    **{"PortList": PortList,
       "swProtocolVLANMIB": swProtocolVLANMIB,
       "swProtocolVLANCtrl": swProtocolVLANCtrl,
       "swProtocolVLANTable": swProtocolVLANTable,
       "swProtocolVLANEntry": swProtocolVLANEntry,
       "swProtocolVLANIndex": swProtocolVLANIndex,
       "swProtocolVLANName": swProtocolVLANName,
       "swProtocolVLANProtocolType": swProtocolVLANProtocolType,
       "swProtocolVLANAdvertisement": swProtocolVLANAdvertisement,
       "swProtocolVLANUserDefinedProtocol": swProtocolVLANUserDefinedProtocol,
       "swProtocolVLANencap": swProtocolVLANencap,
       "swProtocolVLANRowStatus": swProtocolVLANRowStatus,
       "swdot1vProtocolPortTable": swdot1vProtocolPortTable,
       "swdot1vProtocolPortEntry": swdot1vProtocolPortEntry,
       "swdot1vProtocolPortGroupPriority": swdot1vProtocolPortGroupPriority}
)
