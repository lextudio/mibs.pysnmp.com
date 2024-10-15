# SNMP MIB module (COM21-HCXVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COM21-HCXVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:40 2024
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

(com21,
 com21Hcx) = mibBuilder.importSymbols(
    "COM21-HCX-MIB",
    "com21",
    "com21Hcx")

(hcxAlmSeverity,
 hcxEventLogTime) = mibBuilder.importSymbols(
    "COM21-HCXALM-MIB",
    "hcxAlmSeverity",
    "hcxEventLogTime")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

com21HcxVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 80)
)


# Types definitions



class PrimServiceState(Integer32):
    """Custom type PrimServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2))
    )





class Com21RowStatus(Integer32):
    """Custom type Com21RowStatus based on Integer32"""
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
        *(("active", 1),
          ("create", 2),
          ("deactive", 4),
          ("destroy", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Com21HcxVlanCtrlGroup_ObjectIdentity = ObjectIdentity
com21HcxVlanCtrlGroup = _Com21HcxVlanCtrlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81)
)
_Com21HcxVlanCtrlTable_Object = MibTable
com21HcxVlanCtrlTable = _Com21HcxVlanCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1)
)
if mibBuilder.loadTexts:
    com21HcxVlanCtrlTable.setStatus("current")
_Com21HcxVlanCtrlEntry_Object = MibTableRow
com21HcxVlanCtrlEntry = _Com21HcxVlanCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1)
)
com21HcxVlanCtrlEntry.setIndexNames(
    (0, "COM21-HCXVLAN-MIB", "hcxVlanCtrlId"),
)
if mibBuilder.loadTexts:
    com21HcxVlanCtrlEntry.setStatus("current")


class _HcxVlanCtrlId_Type(Integer32):
    """Custom type hcxVlanCtrlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HcxVlanCtrlId_Type.__name__ = "Integer32"
_HcxVlanCtrlId_Object = MibTableColumn
hcxVlanCtrlId = _HcxVlanCtrlId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 1),
    _HcxVlanCtrlId_Type()
)
hcxVlanCtrlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanCtrlId.setStatus("current")


class _HcxVlanCtrlName_Type(DisplayString):
    """Custom type hcxVlanCtrlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxVlanCtrlName_Type.__name__ = "DisplayString"
_HcxVlanCtrlName_Object = MibTableColumn
hcxVlanCtrlName = _HcxVlanCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 2),
    _HcxVlanCtrlName_Type()
)
hcxVlanCtrlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanCtrlName.setStatus("current")


class _HcxVlanShelf_Type(Integer32):
    """Custom type hcxVlanShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HcxVlanShelf_Type.__name__ = "Integer32"
_HcxVlanShelf_Object = MibTableColumn
hcxVlanShelf = _HcxVlanShelf_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 3),
    _HcxVlanShelf_Type()
)
hcxVlanShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanShelf.setStatus("current")
_HcxVlanSlot_Type = Integer32
_HcxVlanSlot_Object = MibTableColumn
hcxVlanSlot = _HcxVlanSlot_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 4),
    _HcxVlanSlot_Type()
)
hcxVlanSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanSlot.setStatus("current")


class _HcxVlanCardType_Type(Integer32):
    """Custom type hcxVlanCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oc3", 3),
          ("onehundredBaseT", 2),
          ("tenBaseT", 1))
    )


_HcxVlanCardType_Type.__name__ = "Integer32"
_HcxVlanCardType_Object = MibTableColumn
hcxVlanCardType = _HcxVlanCardType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 5),
    _HcxVlanCardType_Type()
)
hcxVlanCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanCardType.setStatus("current")
_HcxVlanPort_Type = Integer32
_HcxVlanPort_Object = MibTableColumn
hcxVlanPort = _HcxVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 6),
    _HcxVlanPort_Type()
)
hcxVlanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanPort.setStatus("current")
_HcxVlanPriStatus_Type = Com21RowStatus
_HcxVlanPriStatus_Object = MibTableColumn
hcxVlanPriStatus = _HcxVlanPriStatus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 7),
    _HcxVlanPriStatus_Type()
)
hcxVlanPriStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcxVlanPriStatus.setStatus("current")


class _HcxVlanSecStatus_Type(Integer32):
    """Custom type hcxVlanSecStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_HcxVlanSecStatus_Type.__name__ = "Integer32"
_HcxVlanSecStatus_Object = MibTableColumn
hcxVlanSecStatus = _HcxVlanSecStatus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 8),
    _HcxVlanSecStatus_Type()
)
hcxVlanSecStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanSecStatus.setStatus("current")


class _HcxVlanType_Type(Integer32):
    """Custom type hcxVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_HcxVlanType_Type.__name__ = "Integer32"
_HcxVlanType_Object = MibTableColumn
hcxVlanType = _HcxVlanType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 9),
    _HcxVlanType_Type()
)
hcxVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanType.setStatus("current")


class _HcxVlanPeerToPeerFlag_Type(Integer32):
    """Custom type hcxVlanPeerToPeerFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanPeerToPeerFlag_Type.__name__ = "Integer32"
_HcxVlanPeerToPeerFlag_Object = MibTableColumn
hcxVlanPeerToPeerFlag = _HcxVlanPeerToPeerFlag_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 10),
    _HcxVlanPeerToPeerFlag_Type()
)
hcxVlanPeerToPeerFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanPeerToPeerFlag.setStatus("current")


class _HcxVlanMcastDnstrmRate_Type(Integer32):
    """Custom type hcxVlanMcastDnstrmRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_HcxVlanMcastDnstrmRate_Type.__name__ = "Integer32"
_HcxVlanMcastDnstrmRate_Object = MibTableColumn
hcxVlanMcastDnstrmRate = _HcxVlanMcastDnstrmRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 11),
    _HcxVlanMcastDnstrmRate_Type()
)
hcxVlanMcastDnstrmRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanMcastDnstrmRate.setStatus("current")


class _HcxVlanIpArpFiltEnbl_Type(Integer32):
    """Custom type hcxVlanIpArpFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanIpArpFiltEnbl_Type.__name__ = "Integer32"
_HcxVlanIpArpFiltEnbl_Object = MibTableColumn
hcxVlanIpArpFiltEnbl = _HcxVlanIpArpFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 12),
    _HcxVlanIpArpFiltEnbl_Type()
)
hcxVlanIpArpFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanIpArpFiltEnbl.setStatus("current")


class _HcxVlanIpSrcFiltEnbl_Type(Integer32):
    """Custom type hcxVlanIpSrcFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanIpSrcFiltEnbl_Type.__name__ = "Integer32"
_HcxVlanIpSrcFiltEnbl_Object = MibTableColumn
hcxVlanIpSrcFiltEnbl = _HcxVlanIpSrcFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 13),
    _HcxVlanIpSrcFiltEnbl_Type()
)
hcxVlanIpSrcFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanIpSrcFiltEnbl.setStatus("current")


class _HcxVlanIpDstFiltEnbl_Type(Integer32):
    """Custom type hcxVlanIpDstFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanIpDstFiltEnbl_Type.__name__ = "Integer32"
_HcxVlanIpDstFiltEnbl_Object = MibTableColumn
hcxVlanIpDstFiltEnbl = _HcxVlanIpDstFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 14),
    _HcxVlanIpDstFiltEnbl_Type()
)
hcxVlanIpDstFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanIpDstFiltEnbl.setStatus("current")


class _HcxVlanIpBootpReqFiltEnbl_Type(Integer32):
    """Custom type hcxVlanIpBootpReqFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanIpBootpReqFiltEnbl_Type.__name__ = "Integer32"
_HcxVlanIpBootpReqFiltEnbl_Object = MibTableColumn
hcxVlanIpBootpReqFiltEnbl = _HcxVlanIpBootpReqFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 15),
    _HcxVlanIpBootpReqFiltEnbl_Type()
)
hcxVlanIpBootpReqFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanIpBootpReqFiltEnbl.setStatus("current")


class _HcxVlanIpBootpReplyFiltEnbl_Type(Integer32):
    """Custom type hcxVlanIpBootpReplyFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanIpBootpReplyFiltEnbl_Type.__name__ = "Integer32"
_HcxVlanIpBootpReplyFiltEnbl_Object = MibTableColumn
hcxVlanIpBootpReplyFiltEnbl = _HcxVlanIpBootpReplyFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 16),
    _HcxVlanIpBootpReplyFiltEnbl_Type()
)
hcxVlanIpBootpReplyFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanIpBootpReplyFiltEnbl.setStatus("current")


class _HcxVlanIpDhcpSnoopFiltEnbl_Type(Integer32):
    """Custom type hcxVlanIpDhcpSnoopFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanIpDhcpSnoopFiltEnbl_Type.__name__ = "Integer32"
_HcxVlanIpDhcpSnoopFiltEnbl_Object = MibTableColumn
hcxVlanIpDhcpSnoopFiltEnbl = _HcxVlanIpDhcpSnoopFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 17),
    _HcxVlanIpDhcpSnoopFiltEnbl_Type()
)
hcxVlanIpDhcpSnoopFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanIpDhcpSnoopFiltEnbl.setStatus("current")


class _HcxVlanL2SnapFiltEnbl_Type(Integer32):
    """Custom type hcxVlanL2SnapFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanL2SnapFiltEnbl_Type.__name__ = "Integer32"
_HcxVlanL2SnapFiltEnbl_Object = MibTableColumn
hcxVlanL2SnapFiltEnbl = _HcxVlanL2SnapFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 18),
    _HcxVlanL2SnapFiltEnbl_Type()
)
hcxVlanL2SnapFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanL2SnapFiltEnbl.setStatus("current")


class _HcxVlanL2NonSnapFiltEnbl_Type(Integer32):
    """Custom type hcxVlanL2NonSnapFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanL2NonSnapFiltEnbl_Type.__name__ = "Integer32"
_HcxVlanL2NonSnapFiltEnbl_Object = MibTableColumn
hcxVlanL2NonSnapFiltEnbl = _HcxVlanL2NonSnapFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 19),
    _HcxVlanL2NonSnapFiltEnbl_Type()
)
hcxVlanL2NonSnapFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanL2NonSnapFiltEnbl.setStatus("current")


class _HcxVlanL2EnetFiltEnbl_Type(Integer32):
    """Custom type hcxVlanL2EnetFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanL2EnetFiltEnbl_Type.__name__ = "Integer32"
_HcxVlanL2EnetFiltEnbl_Object = MibTableColumn
hcxVlanL2EnetFiltEnbl = _HcxVlanL2EnetFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 20),
    _HcxVlanL2EnetFiltEnbl_Type()
)
hcxVlanL2EnetFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanL2EnetFiltEnbl.setStatus("deprecated")


class _HcxVlanL2ArpIpv4FiltEnbl_Type(Integer32):
    """Custom type hcxVlanL2ArpIpv4FiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanL2ArpIpv4FiltEnbl_Type.__name__ = "Integer32"
_HcxVlanL2ArpIpv4FiltEnbl_Object = MibTableColumn
hcxVlanL2ArpIpv4FiltEnbl = _HcxVlanL2ArpIpv4FiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 21),
    _HcxVlanL2ArpIpv4FiltEnbl_Type()
)
hcxVlanL2ArpIpv4FiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanL2ArpIpv4FiltEnbl.setStatus("deprecated")


class _HcxVlanL2Ipv4FiltEnbl_Type(Integer32):
    """Custom type hcxVlanL2Ipv4FiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanL2Ipv4FiltEnbl_Type.__name__ = "Integer32"
_HcxVlanL2Ipv4FiltEnbl_Object = MibTableColumn
hcxVlanL2Ipv4FiltEnbl = _HcxVlanL2Ipv4FiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 22),
    _HcxVlanL2Ipv4FiltEnbl_Type()
)
hcxVlanL2Ipv4FiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanL2Ipv4FiltEnbl.setStatus("deprecated")


class _HcxVlanL2Ipv6FiltEnbl_Type(Integer32):
    """Custom type hcxVlanL2Ipv6FiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanL2Ipv6FiltEnbl_Type.__name__ = "Integer32"
_HcxVlanL2Ipv6FiltEnbl_Object = MibTableColumn
hcxVlanL2Ipv6FiltEnbl = _HcxVlanL2Ipv6FiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 23),
    _HcxVlanL2Ipv6FiltEnbl_Type()
)
hcxVlanL2Ipv6FiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanL2Ipv6FiltEnbl.setStatus("deprecated")


class _HcxVlanL2IpxFiltEnbl_Type(Integer32):
    """Custom type hcxVlanL2IpxFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanL2IpxFiltEnbl_Type.__name__ = "Integer32"
_HcxVlanL2IpxFiltEnbl_Object = MibTableColumn
hcxVlanL2IpxFiltEnbl = _HcxVlanL2IpxFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 24),
    _HcxVlanL2IpxFiltEnbl_Type()
)
hcxVlanL2IpxFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanL2IpxFiltEnbl.setStatus("deprecated")


class _HcxVlanL2AppletalkFiltEnbl_Type(Integer32):
    """Custom type hcxVlanL2AppletalkFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanL2AppletalkFiltEnbl_Type.__name__ = "Integer32"
_HcxVlanL2AppletalkFiltEnbl_Object = MibTableColumn
hcxVlanL2AppletalkFiltEnbl = _HcxVlanL2AppletalkFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 25),
    _HcxVlanL2AppletalkFiltEnbl_Type()
)
hcxVlanL2AppletalkFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanL2AppletalkFiltEnbl.setStatus("deprecated")


class _HcxVlanL2OthersFiltEnbl_Type(Integer32):
    """Custom type hcxVlanL2OthersFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanL2OthersFiltEnbl_Type.__name__ = "Integer32"
_HcxVlanL2OthersFiltEnbl_Object = MibTableColumn
hcxVlanL2OthersFiltEnbl = _HcxVlanL2OthersFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 26),
    _HcxVlanL2OthersFiltEnbl_Type()
)
hcxVlanL2OthersFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanL2OthersFiltEnbl.setStatus("deprecated")


class _HcxVlanIpNetbiosFiltEnbl_Type(Integer32):
    """Custom type hcxVlanIpNetbiosFiltEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxVlanIpNetbiosFiltEnbl_Type.__name__ = "Integer32"
_HcxVlanIpNetbiosFiltEnbl_Object = MibTableColumn
hcxVlanIpNetbiosFiltEnbl = _HcxVlanIpNetbiosFiltEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 27),
    _HcxVlanIpNetbiosFiltEnbl_Type()
)
hcxVlanIpNetbiosFiltEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanIpNetbiosFiltEnbl.setStatus("current")
_HcxVPNNum_Type = Integer32
_HcxVPNNum_Object = MibTableColumn
hcxVPNNum = _HcxVPNNum_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 28),
    _HcxVPNNum_Type()
)
hcxVPNNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVPNNum.setStatus("current")


class _HcxVlanVpi_Type(Integer32):
    """Custom type hcxVlanVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HcxVlanVpi_Type.__name__ = "Integer32"
_HcxVlanVpi_Object = MibTableColumn
hcxVlanVpi = _HcxVlanVpi_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 29),
    _HcxVlanVpi_Type()
)
hcxVlanVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanVpi.setStatus("current")


class _HcxVlanVci_Type(Integer32):
    """Custom type hcxVlanVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HcxVlanVci_Type.__name__ = "Integer32"
_HcxVlanVci_Object = MibTableColumn
hcxVlanVci = _HcxVlanVci_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 30),
    _HcxVlanVci_Type()
)
hcxVlanVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanVci.setStatus("current")
_HcxVlanRate_Type = Integer32
_HcxVlanRate_Object = MibTableColumn
hcxVlanRate = _HcxVlanRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 81, 1, 1, 31),
    _HcxVlanRate_Type()
)
hcxVlanRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanRate.setStatus("current")
_Com21HcxVlanStatsGroup_ObjectIdentity = ObjectIdentity
com21HcxVlanStatsGroup = _Com21HcxVlanStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82)
)
_Com21HcxVlanStatsTable_Object = MibTable
com21HcxVlanStatsTable = _Com21HcxVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1)
)
if mibBuilder.loadTexts:
    com21HcxVlanStatsTable.setStatus("current")
_Com21HcxVlanStatsEntry_Object = MibTableRow
com21HcxVlanStatsEntry = _Com21HcxVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1)
)
com21HcxVlanStatsEntry.setIndexNames(
    (0, "COM21-HCXVLAN-MIB", "hcxVlanStatsId"),
)
if mibBuilder.loadTexts:
    com21HcxVlanStatsEntry.setStatus("current")


class _HcxVlanStatsId_Type(Integer32):
    """Custom type hcxVlanStatsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HcxVlanStatsId_Type.__name__ = "Integer32"
_HcxVlanStatsId_Object = MibTableColumn
hcxVlanStatsId = _HcxVlanStatsId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 1),
    _HcxVlanStatsId_Type()
)
hcxVlanStatsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanStatsId.setStatus("current")
_HcxVlanCurrMcastTxPkts_Type = Gauge32
_HcxVlanCurrMcastTxPkts_Object = MibTableColumn
hcxVlanCurrMcastTxPkts = _HcxVlanCurrMcastTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 2),
    _HcxVlanCurrMcastTxPkts_Type()
)
hcxVlanCurrMcastTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanCurrMcastTxPkts.setStatus("current")
_HcxVlanCurrMcastDroppedPkts_Type = Gauge32
_HcxVlanCurrMcastDroppedPkts_Object = MibTableColumn
hcxVlanCurrMcastDroppedPkts = _HcxVlanCurrMcastDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 3),
    _HcxVlanCurrMcastDroppedPkts_Type()
)
hcxVlanCurrMcastDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanCurrMcastDroppedPkts.setStatus("current")
_HcxVlanIpCurrArpFiltStat_Type = Gauge32
_HcxVlanIpCurrArpFiltStat_Object = MibTableColumn
hcxVlanIpCurrArpFiltStat = _HcxVlanIpCurrArpFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 4),
    _HcxVlanIpCurrArpFiltStat_Type()
)
hcxVlanIpCurrArpFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpCurrArpFiltStat.setStatus("current")
_HcxVlanIpCurrSrcFiltStat_Type = Gauge32
_HcxVlanIpCurrSrcFiltStat_Object = MibTableColumn
hcxVlanIpCurrSrcFiltStat = _HcxVlanIpCurrSrcFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 5),
    _HcxVlanIpCurrSrcFiltStat_Type()
)
hcxVlanIpCurrSrcFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpCurrSrcFiltStat.setStatus("current")
_HcxVlanIpCurrDstFiltStat_Type = Gauge32
_HcxVlanIpCurrDstFiltStat_Object = MibTableColumn
hcxVlanIpCurrDstFiltStat = _HcxVlanIpCurrDstFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 6),
    _HcxVlanIpCurrDstFiltStat_Type()
)
hcxVlanIpCurrDstFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpCurrDstFiltStat.setStatus("current")
_HcxVlanIpCurrBootpReqFiltStat_Type = Gauge32
_HcxVlanIpCurrBootpReqFiltStat_Object = MibTableColumn
hcxVlanIpCurrBootpReqFiltStat = _HcxVlanIpCurrBootpReqFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 7),
    _HcxVlanIpCurrBootpReqFiltStat_Type()
)
hcxVlanIpCurrBootpReqFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpCurrBootpReqFiltStat.setStatus("current")
_HcxVlanIpCurrBootpReplyFiltStat_Type = Gauge32
_HcxVlanIpCurrBootpReplyFiltStat_Object = MibTableColumn
hcxVlanIpCurrBootpReplyFiltStat = _HcxVlanIpCurrBootpReplyFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 8),
    _HcxVlanIpCurrBootpReplyFiltStat_Type()
)
hcxVlanIpCurrBootpReplyFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpCurrBootpReplyFiltStat.setStatus("current")
_HcxVlanIpCurrDhcpSnoopFiltStat_Type = Gauge32
_HcxVlanIpCurrDhcpSnoopFiltStat_Object = MibTableColumn
hcxVlanIpCurrDhcpSnoopFiltStat = _HcxVlanIpCurrDhcpSnoopFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 9),
    _HcxVlanIpCurrDhcpSnoopFiltStat_Type()
)
hcxVlanIpCurrDhcpSnoopFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpCurrDhcpSnoopFiltStat.setStatus("current")
_HcxVlanPrevMcastTxPkts_Type = Gauge32
_HcxVlanPrevMcastTxPkts_Object = MibTableColumn
hcxVlanPrevMcastTxPkts = _HcxVlanPrevMcastTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 10),
    _HcxVlanPrevMcastTxPkts_Type()
)
hcxVlanPrevMcastTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanPrevMcastTxPkts.setStatus("current")
_HcxVlanPrevMcastDroppedPkts_Type = Gauge32
_HcxVlanPrevMcastDroppedPkts_Object = MibTableColumn
hcxVlanPrevMcastDroppedPkts = _HcxVlanPrevMcastDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 11),
    _HcxVlanPrevMcastDroppedPkts_Type()
)
hcxVlanPrevMcastDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanPrevMcastDroppedPkts.setStatus("current")
_HcxVlanIpPrevArpFiltStat_Type = Gauge32
_HcxVlanIpPrevArpFiltStat_Object = MibTableColumn
hcxVlanIpPrevArpFiltStat = _HcxVlanIpPrevArpFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 12),
    _HcxVlanIpPrevArpFiltStat_Type()
)
hcxVlanIpPrevArpFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpPrevArpFiltStat.setStatus("current")
_HcxVlanIpPrevSrcFiltStat_Type = Gauge32
_HcxVlanIpPrevSrcFiltStat_Object = MibTableColumn
hcxVlanIpPrevSrcFiltStat = _HcxVlanIpPrevSrcFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 13),
    _HcxVlanIpPrevSrcFiltStat_Type()
)
hcxVlanIpPrevSrcFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpPrevSrcFiltStat.setStatus("current")
_HcxVlanIpPrevDstFiltStat_Type = Gauge32
_HcxVlanIpPrevDstFiltStat_Object = MibTableColumn
hcxVlanIpPrevDstFiltStat = _HcxVlanIpPrevDstFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 14),
    _HcxVlanIpPrevDstFiltStat_Type()
)
hcxVlanIpPrevDstFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpPrevDstFiltStat.setStatus("current")
_HcxVlanIpPrevBootpReqFiltStat_Type = Gauge32
_HcxVlanIpPrevBootpReqFiltStat_Object = MibTableColumn
hcxVlanIpPrevBootpReqFiltStat = _HcxVlanIpPrevBootpReqFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 15),
    _HcxVlanIpPrevBootpReqFiltStat_Type()
)
hcxVlanIpPrevBootpReqFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpPrevBootpReqFiltStat.setStatus("current")
_HcxVlanIpPrevBootpReplyFiltStat_Type = Gauge32
_HcxVlanIpPrevBootpReplyFiltStat_Object = MibTableColumn
hcxVlanIpPrevBootpReplyFiltStat = _HcxVlanIpPrevBootpReplyFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 16),
    _HcxVlanIpPrevBootpReplyFiltStat_Type()
)
hcxVlanIpPrevBootpReplyFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpPrevBootpReplyFiltStat.setStatus("current")
_HcxVlanIpPrevDhcpSnoopFiltStat_Type = Gauge32
_HcxVlanIpPrevDhcpSnoopFiltStat_Object = MibTableColumn
hcxVlanIpPrevDhcpSnoopFiltStat = _HcxVlanIpPrevDhcpSnoopFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 17),
    _HcxVlanIpPrevDhcpSnoopFiltStat_Type()
)
hcxVlanIpPrevDhcpSnoopFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpPrevDhcpSnoopFiltStat.setStatus("current")


class _HcxVlanClearStats_Type(Integer32):
    """Custom type hcxVlanClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_HcxVlanClearStats_Type.__name__ = "Integer32"
_HcxVlanClearStats_Object = MibTableColumn
hcxVlanClearStats = _HcxVlanClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 18),
    _HcxVlanClearStats_Type()
)
hcxVlanClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxVlanClearStats.setStatus("current")
_HcxVlanL2CurrSnapFiltStat_Type = Gauge32
_HcxVlanL2CurrSnapFiltStat_Object = MibTableColumn
hcxVlanL2CurrSnapFiltStat = _HcxVlanL2CurrSnapFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 19),
    _HcxVlanL2CurrSnapFiltStat_Type()
)
hcxVlanL2CurrSnapFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2CurrSnapFiltStat.setStatus("current")
_HcxVlanL2CurrNonSnapFiltStat_Type = Gauge32
_HcxVlanL2CurrNonSnapFiltStat_Object = MibTableColumn
hcxVlanL2CurrNonSnapFiltStat = _HcxVlanL2CurrNonSnapFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 20),
    _HcxVlanL2CurrNonSnapFiltStat_Type()
)
hcxVlanL2CurrNonSnapFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2CurrNonSnapFiltStat.setStatus("current")
_HcxVlanL2CurrEnetFiltStat_Type = Gauge32
_HcxVlanL2CurrEnetFiltStat_Object = MibTableColumn
hcxVlanL2CurrEnetFiltStat = _HcxVlanL2CurrEnetFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 21),
    _HcxVlanL2CurrEnetFiltStat_Type()
)
hcxVlanL2CurrEnetFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2CurrEnetFiltStat.setStatus("deprecated")
_HcxVlanL2CurrArpIpv4FiltStat_Type = Gauge32
_HcxVlanL2CurrArpIpv4FiltStat_Object = MibTableColumn
hcxVlanL2CurrArpIpv4FiltStat = _HcxVlanL2CurrArpIpv4FiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 22),
    _HcxVlanL2CurrArpIpv4FiltStat_Type()
)
hcxVlanL2CurrArpIpv4FiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2CurrArpIpv4FiltStat.setStatus("deprecated")
_HcxVlanL2CurrIpv4FiltStat_Type = Gauge32
_HcxVlanL2CurrIpv4FiltStat_Object = MibTableColumn
hcxVlanL2CurrIpv4FiltStat = _HcxVlanL2CurrIpv4FiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 23),
    _HcxVlanL2CurrIpv4FiltStat_Type()
)
hcxVlanL2CurrIpv4FiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2CurrIpv4FiltStat.setStatus("deprecated")
_HcxVlanL2CurrIpv6FiltStat_Type = Gauge32
_HcxVlanL2CurrIpv6FiltStat_Object = MibTableColumn
hcxVlanL2CurrIpv6FiltStat = _HcxVlanL2CurrIpv6FiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 24),
    _HcxVlanL2CurrIpv6FiltStat_Type()
)
hcxVlanL2CurrIpv6FiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2CurrIpv6FiltStat.setStatus("deprecated")
_HcxVlanL2CurrIpxFiltStat_Type = Gauge32
_HcxVlanL2CurrIpxFiltStat_Object = MibTableColumn
hcxVlanL2CurrIpxFiltStat = _HcxVlanL2CurrIpxFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 25),
    _HcxVlanL2CurrIpxFiltStat_Type()
)
hcxVlanL2CurrIpxFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2CurrIpxFiltStat.setStatus("deprecated")
_HcxVlanL2CurrAppletalkFiltStat_Type = Gauge32
_HcxVlanL2CurrAppletalkFiltStat_Object = MibTableColumn
hcxVlanL2CurrAppletalkFiltStat = _HcxVlanL2CurrAppletalkFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 26),
    _HcxVlanL2CurrAppletalkFiltStat_Type()
)
hcxVlanL2CurrAppletalkFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2CurrAppletalkFiltStat.setStatus("deprecated")
_HcxVlanL2CurrOthersFiltStat_Type = Gauge32
_HcxVlanL2CurrOthersFiltStat_Object = MibTableColumn
hcxVlanL2CurrOthersFiltStat = _HcxVlanL2CurrOthersFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 27),
    _HcxVlanL2CurrOthersFiltStat_Type()
)
hcxVlanL2CurrOthersFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2CurrOthersFiltStat.setStatus("deprecated")
_HcxVlanIpCurrNetbiosFiltStat_Type = Gauge32
_HcxVlanIpCurrNetbiosFiltStat_Object = MibTableColumn
hcxVlanIpCurrNetbiosFiltStat = _HcxVlanIpCurrNetbiosFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 28),
    _HcxVlanIpCurrNetbiosFiltStat_Type()
)
hcxVlanIpCurrNetbiosFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpCurrNetbiosFiltStat.setStatus("current")
_HcxVlanL2PrevSnapFiltStat_Type = Gauge32
_HcxVlanL2PrevSnapFiltStat_Object = MibTableColumn
hcxVlanL2PrevSnapFiltStat = _HcxVlanL2PrevSnapFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 29),
    _HcxVlanL2PrevSnapFiltStat_Type()
)
hcxVlanL2PrevSnapFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2PrevSnapFiltStat.setStatus("current")
_HcxVlanL2PrevNonSnapFiltStat_Type = Gauge32
_HcxVlanL2PrevNonSnapFiltStat_Object = MibTableColumn
hcxVlanL2PrevNonSnapFiltStat = _HcxVlanL2PrevNonSnapFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 30),
    _HcxVlanL2PrevNonSnapFiltStat_Type()
)
hcxVlanL2PrevNonSnapFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2PrevNonSnapFiltStat.setStatus("current")
_HcxVlanL2PrevEnetFiltStat_Type = Gauge32
_HcxVlanL2PrevEnetFiltStat_Object = MibTableColumn
hcxVlanL2PrevEnetFiltStat = _HcxVlanL2PrevEnetFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 31),
    _HcxVlanL2PrevEnetFiltStat_Type()
)
hcxVlanL2PrevEnetFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2PrevEnetFiltStat.setStatus("deprecated")
_HcxVlanL2PrevArpIpv4FiltStat_Type = Gauge32
_HcxVlanL2PrevArpIpv4FiltStat_Object = MibTableColumn
hcxVlanL2PrevArpIpv4FiltStat = _HcxVlanL2PrevArpIpv4FiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 32),
    _HcxVlanL2PrevArpIpv4FiltStat_Type()
)
hcxVlanL2PrevArpIpv4FiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2PrevArpIpv4FiltStat.setStatus("deprecated")
_HcxVlanL2PrevIpv4FiltStat_Type = Gauge32
_HcxVlanL2PrevIpv4FiltStat_Object = MibTableColumn
hcxVlanL2PrevIpv4FiltStat = _HcxVlanL2PrevIpv4FiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 33),
    _HcxVlanL2PrevIpv4FiltStat_Type()
)
hcxVlanL2PrevIpv4FiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2PrevIpv4FiltStat.setStatus("deprecated")
_HcxVlanL2PrevIpv6FiltStat_Type = Gauge32
_HcxVlanL2PrevIpv6FiltStat_Object = MibTableColumn
hcxVlanL2PrevIpv6FiltStat = _HcxVlanL2PrevIpv6FiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 34),
    _HcxVlanL2PrevIpv6FiltStat_Type()
)
hcxVlanL2PrevIpv6FiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2PrevIpv6FiltStat.setStatus("deprecated")
_HcxVlanL2PrevIpxFiltStat_Type = Gauge32
_HcxVlanL2PrevIpxFiltStat_Object = MibTableColumn
hcxVlanL2PrevIpxFiltStat = _HcxVlanL2PrevIpxFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 35),
    _HcxVlanL2PrevIpxFiltStat_Type()
)
hcxVlanL2PrevIpxFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2PrevIpxFiltStat.setStatus("deprecated")
_HcxVlanL2PrevAppletalkFiltStat_Type = Gauge32
_HcxVlanL2PrevAppletalkFiltStat_Object = MibTableColumn
hcxVlanL2PrevAppletalkFiltStat = _HcxVlanL2PrevAppletalkFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 36),
    _HcxVlanL2PrevAppletalkFiltStat_Type()
)
hcxVlanL2PrevAppletalkFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2PrevAppletalkFiltStat.setStatus("deprecated")
_HcxVlanL2PrevOthersFiltStat_Type = Gauge32
_HcxVlanL2PrevOthersFiltStat_Object = MibTableColumn
hcxVlanL2PrevOthersFiltStat = _HcxVlanL2PrevOthersFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 37),
    _HcxVlanL2PrevOthersFiltStat_Type()
)
hcxVlanL2PrevOthersFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanL2PrevOthersFiltStat.setStatus("deprecated")
_HcxVlanIpPrevNetbiosFiltStat_Type = Gauge32
_HcxVlanIpPrevNetbiosFiltStat_Object = MibTableColumn
hcxVlanIpPrevNetbiosFiltStat = _HcxVlanIpPrevNetbiosFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 82, 1, 1, 38),
    _HcxVlanIpPrevNetbiosFiltStat_Type()
)
hcxVlanIpPrevNetbiosFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxVlanIpPrevNetbiosFiltStat.setStatus("current")
_Com21HcxOc3VlanStatsGroup_ObjectIdentity = ObjectIdentity
com21HcxOc3VlanStatsGroup = _Com21HcxOc3VlanStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 83)
)
_Com21HcxOc3VlanStatsTable_Object = MibTable
com21HcxOc3VlanStatsTable = _Com21HcxOc3VlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 83, 1)
)
if mibBuilder.loadTexts:
    com21HcxOc3VlanStatsTable.setStatus("current")
_Com21HcxOc3VlanStatsEntry_Object = MibTableRow
com21HcxOc3VlanStatsEntry = _Com21HcxOc3VlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1)
)
com21HcxOc3VlanStatsEntry.setIndexNames(
    (0, "COM21-HCXVLAN-MIB", "hcxOc3VlanStatsVlanId"),
)
if mibBuilder.loadTexts:
    com21HcxOc3VlanStatsEntry.setStatus("current")


class _HcxOc3VlanStatsVlanId_Type(Integer32):
    """Custom type hcxOc3VlanStatsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HcxOc3VlanStatsVlanId_Type.__name__ = "Integer32"
_HcxOc3VlanStatsVlanId_Object = MibTableColumn
hcxOc3VlanStatsVlanId = _HcxOc3VlanStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 1),
    _HcxOc3VlanStatsVlanId_Type()
)
hcxOc3VlanStatsVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3VlanStatsVlanId.setStatus("current")
_HcxOc3VlanStatsCurrTxPkts_Type = Integer32
_HcxOc3VlanStatsCurrTxPkts_Object = MibTableColumn
hcxOc3VlanStatsCurrTxPkts = _HcxOc3VlanStatsCurrTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 2),
    _HcxOc3VlanStatsCurrTxPkts_Type()
)
hcxOc3VlanStatsCurrTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3VlanStatsCurrTxPkts.setStatus("current")
_HcxOc3VlanStatsCurrRxPkts_Type = Integer32
_HcxOc3VlanStatsCurrRxPkts_Object = MibTableColumn
hcxOc3VlanStatsCurrRxPkts = _HcxOc3VlanStatsCurrRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 3),
    _HcxOc3VlanStatsCurrRxPkts_Type()
)
hcxOc3VlanStatsCurrRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3VlanStatsCurrRxPkts.setStatus("current")
_HcxOc3VlanStatsCurrCrcPkts_Type = Integer32
_HcxOc3VlanStatsCurrCrcPkts_Object = MibTableColumn
hcxOc3VlanStatsCurrCrcPkts = _HcxOc3VlanStatsCurrCrcPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 4),
    _HcxOc3VlanStatsCurrCrcPkts_Type()
)
hcxOc3VlanStatsCurrCrcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3VlanStatsCurrCrcPkts.setStatus("current")
_HcxOc3VlanStatsPrevTxPkts_Type = Integer32
_HcxOc3VlanStatsPrevTxPkts_Object = MibTableColumn
hcxOc3VlanStatsPrevTxPkts = _HcxOc3VlanStatsPrevTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 5),
    _HcxOc3VlanStatsPrevTxPkts_Type()
)
hcxOc3VlanStatsPrevTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3VlanStatsPrevTxPkts.setStatus("current")
_HcxOc3VlanStatsPrevRxPkts_Type = Integer32
_HcxOc3VlanStatsPrevRxPkts_Object = MibTableColumn
hcxOc3VlanStatsPrevRxPkts = _HcxOc3VlanStatsPrevRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 6),
    _HcxOc3VlanStatsPrevRxPkts_Type()
)
hcxOc3VlanStatsPrevRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3VlanStatsPrevRxPkts.setStatus("current")
_HcxOc3VlanStatsPrevCrcPkts_Type = Integer32
_HcxOc3VlanStatsPrevCrcPkts_Object = MibTableColumn
hcxOc3VlanStatsPrevCrcPkts = _HcxOc3VlanStatsPrevCrcPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 7),
    _HcxOc3VlanStatsPrevCrcPkts_Type()
)
hcxOc3VlanStatsPrevCrcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3VlanStatsPrevCrcPkts.setStatus("current")


class _HcxOc3VlanStatsClear_Type(Integer32):
    """Custom type hcxOc3VlanStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_HcxOc3VlanStatsClear_Type.__name__ = "Integer32"
_HcxOc3VlanStatsClear_Object = MibTableColumn
hcxOc3VlanStatsClear = _HcxOc3VlanStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 83, 1, 1, 8),
    _HcxOc3VlanStatsClear_Type()
)
hcxOc3VlanStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxOc3VlanStatsClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COM21-HCXVLAN-MIB",
    **{"PrimServiceState": PrimServiceState,
       "Com21RowStatus": Com21RowStatus,
       "com21HcxVlan": com21HcxVlan,
       "com21HcxVlanCtrlGroup": com21HcxVlanCtrlGroup,
       "com21HcxVlanCtrlTable": com21HcxVlanCtrlTable,
       "com21HcxVlanCtrlEntry": com21HcxVlanCtrlEntry,
       "hcxVlanCtrlId": hcxVlanCtrlId,
       "hcxVlanCtrlName": hcxVlanCtrlName,
       "hcxVlanShelf": hcxVlanShelf,
       "hcxVlanSlot": hcxVlanSlot,
       "hcxVlanCardType": hcxVlanCardType,
       "hcxVlanPort": hcxVlanPort,
       "hcxVlanPriStatus": hcxVlanPriStatus,
       "hcxVlanSecStatus": hcxVlanSecStatus,
       "hcxVlanType": hcxVlanType,
       "hcxVlanPeerToPeerFlag": hcxVlanPeerToPeerFlag,
       "hcxVlanMcastDnstrmRate": hcxVlanMcastDnstrmRate,
       "hcxVlanIpArpFiltEnbl": hcxVlanIpArpFiltEnbl,
       "hcxVlanIpSrcFiltEnbl": hcxVlanIpSrcFiltEnbl,
       "hcxVlanIpDstFiltEnbl": hcxVlanIpDstFiltEnbl,
       "hcxVlanIpBootpReqFiltEnbl": hcxVlanIpBootpReqFiltEnbl,
       "hcxVlanIpBootpReplyFiltEnbl": hcxVlanIpBootpReplyFiltEnbl,
       "hcxVlanIpDhcpSnoopFiltEnbl": hcxVlanIpDhcpSnoopFiltEnbl,
       "hcxVlanL2SnapFiltEnbl": hcxVlanL2SnapFiltEnbl,
       "hcxVlanL2NonSnapFiltEnbl": hcxVlanL2NonSnapFiltEnbl,
       "hcxVlanL2EnetFiltEnbl": hcxVlanL2EnetFiltEnbl,
       "hcxVlanL2ArpIpv4FiltEnbl": hcxVlanL2ArpIpv4FiltEnbl,
       "hcxVlanL2Ipv4FiltEnbl": hcxVlanL2Ipv4FiltEnbl,
       "hcxVlanL2Ipv6FiltEnbl": hcxVlanL2Ipv6FiltEnbl,
       "hcxVlanL2IpxFiltEnbl": hcxVlanL2IpxFiltEnbl,
       "hcxVlanL2AppletalkFiltEnbl": hcxVlanL2AppletalkFiltEnbl,
       "hcxVlanL2OthersFiltEnbl": hcxVlanL2OthersFiltEnbl,
       "hcxVlanIpNetbiosFiltEnbl": hcxVlanIpNetbiosFiltEnbl,
       "hcxVPNNum": hcxVPNNum,
       "hcxVlanVpi": hcxVlanVpi,
       "hcxVlanVci": hcxVlanVci,
       "hcxVlanRate": hcxVlanRate,
       "com21HcxVlanStatsGroup": com21HcxVlanStatsGroup,
       "com21HcxVlanStatsTable": com21HcxVlanStatsTable,
       "com21HcxVlanStatsEntry": com21HcxVlanStatsEntry,
       "hcxVlanStatsId": hcxVlanStatsId,
       "hcxVlanCurrMcastTxPkts": hcxVlanCurrMcastTxPkts,
       "hcxVlanCurrMcastDroppedPkts": hcxVlanCurrMcastDroppedPkts,
       "hcxVlanIpCurrArpFiltStat": hcxVlanIpCurrArpFiltStat,
       "hcxVlanIpCurrSrcFiltStat": hcxVlanIpCurrSrcFiltStat,
       "hcxVlanIpCurrDstFiltStat": hcxVlanIpCurrDstFiltStat,
       "hcxVlanIpCurrBootpReqFiltStat": hcxVlanIpCurrBootpReqFiltStat,
       "hcxVlanIpCurrBootpReplyFiltStat": hcxVlanIpCurrBootpReplyFiltStat,
       "hcxVlanIpCurrDhcpSnoopFiltStat": hcxVlanIpCurrDhcpSnoopFiltStat,
       "hcxVlanPrevMcastTxPkts": hcxVlanPrevMcastTxPkts,
       "hcxVlanPrevMcastDroppedPkts": hcxVlanPrevMcastDroppedPkts,
       "hcxVlanIpPrevArpFiltStat": hcxVlanIpPrevArpFiltStat,
       "hcxVlanIpPrevSrcFiltStat": hcxVlanIpPrevSrcFiltStat,
       "hcxVlanIpPrevDstFiltStat": hcxVlanIpPrevDstFiltStat,
       "hcxVlanIpPrevBootpReqFiltStat": hcxVlanIpPrevBootpReqFiltStat,
       "hcxVlanIpPrevBootpReplyFiltStat": hcxVlanIpPrevBootpReplyFiltStat,
       "hcxVlanIpPrevDhcpSnoopFiltStat": hcxVlanIpPrevDhcpSnoopFiltStat,
       "hcxVlanClearStats": hcxVlanClearStats,
       "hcxVlanL2CurrSnapFiltStat": hcxVlanL2CurrSnapFiltStat,
       "hcxVlanL2CurrNonSnapFiltStat": hcxVlanL2CurrNonSnapFiltStat,
       "hcxVlanL2CurrEnetFiltStat": hcxVlanL2CurrEnetFiltStat,
       "hcxVlanL2CurrArpIpv4FiltStat": hcxVlanL2CurrArpIpv4FiltStat,
       "hcxVlanL2CurrIpv4FiltStat": hcxVlanL2CurrIpv4FiltStat,
       "hcxVlanL2CurrIpv6FiltStat": hcxVlanL2CurrIpv6FiltStat,
       "hcxVlanL2CurrIpxFiltStat": hcxVlanL2CurrIpxFiltStat,
       "hcxVlanL2CurrAppletalkFiltStat": hcxVlanL2CurrAppletalkFiltStat,
       "hcxVlanL2CurrOthersFiltStat": hcxVlanL2CurrOthersFiltStat,
       "hcxVlanIpCurrNetbiosFiltStat": hcxVlanIpCurrNetbiosFiltStat,
       "hcxVlanL2PrevSnapFiltStat": hcxVlanL2PrevSnapFiltStat,
       "hcxVlanL2PrevNonSnapFiltStat": hcxVlanL2PrevNonSnapFiltStat,
       "hcxVlanL2PrevEnetFiltStat": hcxVlanL2PrevEnetFiltStat,
       "hcxVlanL2PrevArpIpv4FiltStat": hcxVlanL2PrevArpIpv4FiltStat,
       "hcxVlanL2PrevIpv4FiltStat": hcxVlanL2PrevIpv4FiltStat,
       "hcxVlanL2PrevIpv6FiltStat": hcxVlanL2PrevIpv6FiltStat,
       "hcxVlanL2PrevIpxFiltStat": hcxVlanL2PrevIpxFiltStat,
       "hcxVlanL2PrevAppletalkFiltStat": hcxVlanL2PrevAppletalkFiltStat,
       "hcxVlanL2PrevOthersFiltStat": hcxVlanL2PrevOthersFiltStat,
       "hcxVlanIpPrevNetbiosFiltStat": hcxVlanIpPrevNetbiosFiltStat,
       "com21HcxOc3VlanStatsGroup": com21HcxOc3VlanStatsGroup,
       "com21HcxOc3VlanStatsTable": com21HcxOc3VlanStatsTable,
       "com21HcxOc3VlanStatsEntry": com21HcxOc3VlanStatsEntry,
       "hcxOc3VlanStatsVlanId": hcxOc3VlanStatsVlanId,
       "hcxOc3VlanStatsCurrTxPkts": hcxOc3VlanStatsCurrTxPkts,
       "hcxOc3VlanStatsCurrRxPkts": hcxOc3VlanStatsCurrRxPkts,
       "hcxOc3VlanStatsCurrCrcPkts": hcxOc3VlanStatsCurrCrcPkts,
       "hcxOc3VlanStatsPrevTxPkts": hcxOc3VlanStatsPrevTxPkts,
       "hcxOc3VlanStatsPrevRxPkts": hcxOc3VlanStatsPrevRxPkts,
       "hcxOc3VlanStatsPrevCrcPkts": hcxOc3VlanStatsPrevCrcPkts,
       "hcxOc3VlanStatsClear": hcxOc3VlanStatsClear}
)
