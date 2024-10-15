# SNMP MIB module (CISCO-FRAME-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FRAME-RELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:32 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(frCircuitDlci,
 frCircuitEntry,
 frCircuitIfIndex,
 frDlcmiEntry) = mibBuilder.importSymbols(
    "RFC1315-MIB",
    "frCircuitDlci",
    "frCircuitEntry",
    "frCircuitIfIndex",
    "frDlcmiEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoFrameRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 49)
)
ciscoFrameRelayMIB.setRevisions(
        ("2000-10-13 00:00",
         "2000-05-22 00:00",
         "2000-05-16 00:00",
         "2000-04-26 00:00",
         "1999-08-21 00:00",
         "1996-08-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DlciNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )



class CfrMapProtocols(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              10,
              11,
              12,
              13,
              16,
              18,
              22,
              25,
              37,
              38,
              39,
              40,
              47,
              48,
              49,
              53,
              63,
              74,
              83,
              999)
        )
    )
    namedValues = NamedValues(
        *(("apollo", 12),
          ("appletalk", 16),
          ("arp", 1),
          ("bridge", 38),
          ("clns", 25),
          ("compressedRtp", 83),
          ("compressedTcp", 48),
          ("decnet", 22),
          ("dlsw", 63),
          ("frArp", 40),
          ("frSwitch", 53),
          ("ieeeSpanning", 18),
          ("ip", 7),
          ("llc2", 49),
          ("nhrp", 74),
          ("novell", 11),
          ("rsrb", 37),
          ("serialArp", 6),
          ("stun", 39),
          ("uncompressedTcp", 47),
          ("vines", 13),
          ("wildcard", 999),
          ("xns", 10))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFrMIBObjects = _CiscoFrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1)
)
_CfrLmiObjs_ObjectIdentity = ObjectIdentity
cfrLmiObjs = _CfrLmiObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1)
)
_CfrLmiTable_Object = MibTable
cfrLmiTable = _CfrLmiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfrLmiTable.setStatus("current")
_CfrLmiEntry_Object = MibTableRow
cfrLmiEntry = _CfrLmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfrLmiEntry.setStatus("current")


class _CfrLmiLinkstatus_Type(Integer32):
    """Custom type cfrLmiLinkstatus based on Integer32"""
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


_CfrLmiLinkstatus_Type.__name__ = "Integer32"
_CfrLmiLinkstatus_Object = MibTableColumn
cfrLmiLinkstatus = _CfrLmiLinkstatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1, 1),
    _CfrLmiLinkstatus_Type()
)
cfrLmiLinkstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrLmiLinkstatus.setStatus("current")


class _CfrLmiLinkType_Type(Integer32):
    """Custom type cfrLmiLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1),
          ("nni", 3))
    )


_CfrLmiLinkType_Type.__name__ = "Integer32"
_CfrLmiLinkType_Object = MibTableColumn
cfrLmiLinkType = _CfrLmiLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1, 2),
    _CfrLmiLinkType_Type()
)
cfrLmiLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrLmiLinkType.setStatus("current")
_CfrLmiEnquiryIns_Type = Counter32
_CfrLmiEnquiryIns_Object = MibTableColumn
cfrLmiEnquiryIns = _CfrLmiEnquiryIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1, 3),
    _CfrLmiEnquiryIns_Type()
)
cfrLmiEnquiryIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrLmiEnquiryIns.setStatus("current")
if mibBuilder.loadTexts:
    cfrLmiEnquiryIns.setUnits("messages")
_CfrLmiEnquiryOuts_Type = Counter32
_CfrLmiEnquiryOuts_Object = MibTableColumn
cfrLmiEnquiryOuts = _CfrLmiEnquiryOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1, 4),
    _CfrLmiEnquiryOuts_Type()
)
cfrLmiEnquiryOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrLmiEnquiryOuts.setStatus("current")
if mibBuilder.loadTexts:
    cfrLmiEnquiryOuts.setUnits("messages")
_CfrLmiStatusIns_Type = Counter32
_CfrLmiStatusIns_Object = MibTableColumn
cfrLmiStatusIns = _CfrLmiStatusIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1, 5),
    _CfrLmiStatusIns_Type()
)
cfrLmiStatusIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrLmiStatusIns.setStatus("current")
if mibBuilder.loadTexts:
    cfrLmiStatusIns.setUnits("messages")
_CfrLmiStatusOuts_Type = Counter32
_CfrLmiStatusOuts_Object = MibTableColumn
cfrLmiStatusOuts = _CfrLmiStatusOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1, 6),
    _CfrLmiStatusOuts_Type()
)
cfrLmiStatusOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrLmiStatusOuts.setStatus("current")
if mibBuilder.loadTexts:
    cfrLmiStatusOuts.setUnits("messages")
_CfrLmiUpdateStatusIns_Type = Counter32
_CfrLmiUpdateStatusIns_Object = MibTableColumn
cfrLmiUpdateStatusIns = _CfrLmiUpdateStatusIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1, 7),
    _CfrLmiUpdateStatusIns_Type()
)
cfrLmiUpdateStatusIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrLmiUpdateStatusIns.setStatus("current")
if mibBuilder.loadTexts:
    cfrLmiUpdateStatusIns.setUnits("messages")
_CfrLmiUpdateStatusOuts_Type = Counter32
_CfrLmiUpdateStatusOuts_Object = MibTableColumn
cfrLmiUpdateStatusOuts = _CfrLmiUpdateStatusOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1, 8),
    _CfrLmiUpdateStatusOuts_Type()
)
cfrLmiUpdateStatusOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrLmiUpdateStatusOuts.setStatus("current")
if mibBuilder.loadTexts:
    cfrLmiUpdateStatusOuts.setUnits("messages")
_CfrLmiStatusTimeouts_Type = Counter32
_CfrLmiStatusTimeouts_Object = MibTableColumn
cfrLmiStatusTimeouts = _CfrLmiStatusTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1, 9),
    _CfrLmiStatusTimeouts_Type()
)
cfrLmiStatusTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrLmiStatusTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    cfrLmiStatusTimeouts.setUnits("times")
_CfrLmiStatusEnqTimeouts_Type = Counter32
_CfrLmiStatusEnqTimeouts_Object = MibTableColumn
cfrLmiStatusEnqTimeouts = _CfrLmiStatusEnqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1, 10),
    _CfrLmiStatusEnqTimeouts_Type()
)
cfrLmiStatusEnqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrLmiStatusEnqTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    cfrLmiStatusEnqTimeouts.setUnits("times")


class _CfrLmiN392Dce_Type(Integer32):
    """Custom type cfrLmiN392Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CfrLmiN392Dce_Type.__name__ = "Integer32"
_CfrLmiN392Dce_Object = MibTableColumn
cfrLmiN392Dce = _CfrLmiN392Dce_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1, 11),
    _CfrLmiN392Dce_Type()
)
cfrLmiN392Dce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrLmiN392Dce.setStatus("current")


class _CfrLmiN393Dce_Type(Integer32):
    """Custom type cfrLmiN393Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CfrLmiN393Dce_Type.__name__ = "Integer32"
_CfrLmiN393Dce_Object = MibTableColumn
cfrLmiN393Dce = _CfrLmiN393Dce_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1, 12),
    _CfrLmiN393Dce_Type()
)
cfrLmiN393Dce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrLmiN393Dce.setStatus("current")


class _CfrLmiT392Dce_Type(Integer32):
    """Custom type cfrLmiT392Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CfrLmiT392Dce_Type.__name__ = "Integer32"
_CfrLmiT392Dce_Object = MibTableColumn
cfrLmiT392Dce = _CfrLmiT392Dce_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 1, 1, 1, 13),
    _CfrLmiT392Dce_Type()
)
cfrLmiT392Dce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrLmiT392Dce.setStatus("current")
if mibBuilder.loadTexts:
    cfrLmiT392Dce.setUnits("seconds")
_CfrCircuitObjs_ObjectIdentity = ObjectIdentity
cfrCircuitObjs = _CfrCircuitObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2)
)
_CfrCircuitTable_Object = MibTable
cfrCircuitTable = _CfrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfrCircuitTable.setStatus("current")
_CfrCircuitEntry_Object = MibTableRow
cfrCircuitEntry = _CfrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cfrCircuitEntry.setStatus("current")
_CfrCircuitDEins_Type = Counter32
_CfrCircuitDEins_Object = MibTableColumn
cfrCircuitDEins = _CfrCircuitDEins_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 1, 1, 1),
    _CfrCircuitDEins_Type()
)
cfrCircuitDEins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrCircuitDEins.setStatus("current")
if mibBuilder.loadTexts:
    cfrCircuitDEins.setUnits("packets")
_CfrCircuitDEouts_Type = Counter32
_CfrCircuitDEouts_Object = MibTableColumn
cfrCircuitDEouts = _CfrCircuitDEouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 1, 1, 2),
    _CfrCircuitDEouts_Type()
)
cfrCircuitDEouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrCircuitDEouts.setStatus("current")
if mibBuilder.loadTexts:
    cfrCircuitDEouts.setUnits("packets")
_CfrCircuitDropPktsOuts_Type = Counter32
_CfrCircuitDropPktsOuts_Object = MibTableColumn
cfrCircuitDropPktsOuts = _CfrCircuitDropPktsOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 1, 1, 3),
    _CfrCircuitDropPktsOuts_Type()
)
cfrCircuitDropPktsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrCircuitDropPktsOuts.setStatus("current")
if mibBuilder.loadTexts:
    cfrCircuitDropPktsOuts.setUnits("packets")


class _CfrCircuitType_Type(Integer32):
    """Custom type cfrCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_CfrCircuitType_Type.__name__ = "Integer32"
_CfrCircuitType_Object = MibTableColumn
cfrCircuitType = _CfrCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 1, 1, 4),
    _CfrCircuitType_Type()
)
cfrCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrCircuitType.setStatus("current")
_CfrExtCircuitTable_Object = MibTable
cfrExtCircuitTable = _CfrExtCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cfrExtCircuitTable.setStatus("current")
_CfrExtCircuitEntry_Object = MibTableRow
cfrExtCircuitEntry = _CfrExtCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cfrExtCircuitEntry.setStatus("current")
_CfrExtCircuitIfName_Type = DisplayString
_CfrExtCircuitIfName_Object = MibTableColumn
cfrExtCircuitIfName = _CfrExtCircuitIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 1),
    _CfrExtCircuitIfName_Type()
)
cfrExtCircuitIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitIfName.setStatus("current")


class _CfrExtCircuitIfType_Type(Integer32):
    """Custom type cfrExtCircuitIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mainInterface", 1),
          ("multipoint", 3),
          ("pointToPoint", 2))
    )


_CfrExtCircuitIfType_Type.__name__ = "Integer32"
_CfrExtCircuitIfType_Object = MibTableColumn
cfrExtCircuitIfType = _CfrExtCircuitIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 2),
    _CfrExtCircuitIfType_Type()
)
cfrExtCircuitIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitIfType.setStatus("current")
_CfrExtCircuitSubifIndex_Type = InterfaceIndex
_CfrExtCircuitSubifIndex_Object = MibTableColumn
cfrExtCircuitSubifIndex = _CfrExtCircuitSubifIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 3),
    _CfrExtCircuitSubifIndex_Type()
)
cfrExtCircuitSubifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitSubifIndex.setStatus("current")


class _CfrExtCircuitMapStatus_Type(Integer32):
    """Custom type cfrExtCircuitMapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_CfrExtCircuitMapStatus_Type.__name__ = "Integer32"
_CfrExtCircuitMapStatus_Object = MibTableColumn
cfrExtCircuitMapStatus = _CfrExtCircuitMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 4),
    _CfrExtCircuitMapStatus_Type()
)
cfrExtCircuitMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitMapStatus.setStatus("current")


class _CfrExtCircuitCreateType_Type(Integer32):
    """Custom type cfrExtCircuitCreateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_CfrExtCircuitCreateType_Type.__name__ = "Integer32"
_CfrExtCircuitCreateType_Object = MibTableColumn
cfrExtCircuitCreateType = _CfrExtCircuitCreateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 5),
    _CfrExtCircuitCreateType_Type()
)
cfrExtCircuitCreateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitCreateType.setStatus("current")
_CfrExtCircuitMulticast_Type = TruthValue
_CfrExtCircuitMulticast_Object = MibTableColumn
cfrExtCircuitMulticast = _CfrExtCircuitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 6),
    _CfrExtCircuitMulticast_Type()
)
cfrExtCircuitMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitMulticast.setStatus("current")
_CfrExtCircuitRoutedDlci_Type = DlciNumber
_CfrExtCircuitRoutedDlci_Object = MibTableColumn
cfrExtCircuitRoutedDlci = _CfrExtCircuitRoutedDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 7),
    _CfrExtCircuitRoutedDlci_Type()
)
cfrExtCircuitRoutedDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitRoutedDlci.setStatus("current")
_CfrExtCircuitRoutedIf_Type = InterfaceIndex
_CfrExtCircuitRoutedIf_Object = MibTableColumn
cfrExtCircuitRoutedIf = _CfrExtCircuitRoutedIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 8),
    _CfrExtCircuitRoutedIf_Type()
)
cfrExtCircuitRoutedIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitRoutedIf.setStatus("current")
_CfrExtCircuitUncompressIns_Type = Counter32
_CfrExtCircuitUncompressIns_Object = MibTableColumn
cfrExtCircuitUncompressIns = _CfrExtCircuitUncompressIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 9),
    _CfrExtCircuitUncompressIns_Type()
)
cfrExtCircuitUncompressIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitUncompressIns.setStatus("current")
if mibBuilder.loadTexts:
    cfrExtCircuitUncompressIns.setUnits("octets")
_CfrExtCircuitUncompressOuts_Type = Counter32
_CfrExtCircuitUncompressOuts_Object = MibTableColumn
cfrExtCircuitUncompressOuts = _CfrExtCircuitUncompressOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 10),
    _CfrExtCircuitUncompressOuts_Type()
)
cfrExtCircuitUncompressOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitUncompressOuts.setStatus("current")
if mibBuilder.loadTexts:
    cfrExtCircuitUncompressOuts.setUnits("octets")
_CfrExtCircuitFECNOuts_Type = Counter32
_CfrExtCircuitFECNOuts_Object = MibTableColumn
cfrExtCircuitFECNOuts = _CfrExtCircuitFECNOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 11),
    _CfrExtCircuitFECNOuts_Type()
)
cfrExtCircuitFECNOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitFECNOuts.setStatus("current")
_CfrExtCircuitBECNOuts_Type = Counter32
_CfrExtCircuitBECNOuts_Object = MibTableColumn
cfrExtCircuitBECNOuts = _CfrExtCircuitBECNOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 12),
    _CfrExtCircuitBECNOuts_Type()
)
cfrExtCircuitBECNOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitBECNOuts.setStatus("current")


class _CfrExtCircuitMinThruputOut_Type(Integer32):
    """Custom type cfrExtCircuitMinThruputOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_CfrExtCircuitMinThruputOut_Type.__name__ = "Integer32"
_CfrExtCircuitMinThruputOut_Object = MibTableColumn
cfrExtCircuitMinThruputOut = _CfrExtCircuitMinThruputOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 13),
    _CfrExtCircuitMinThruputOut_Type()
)
cfrExtCircuitMinThruputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitMinThruputOut.setStatus("current")
if mibBuilder.loadTexts:
    cfrExtCircuitMinThruputOut.setUnits("bits per second")


class _CfrExtCircuitMinThruputIn_Type(Integer32):
    """Custom type cfrExtCircuitMinThruputIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_CfrExtCircuitMinThruputIn_Type.__name__ = "Integer32"
_CfrExtCircuitMinThruputIn_Object = MibTableColumn
cfrExtCircuitMinThruputIn = _CfrExtCircuitMinThruputIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 14),
    _CfrExtCircuitMinThruputIn_Type()
)
cfrExtCircuitMinThruputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitMinThruputIn.setStatus("current")
if mibBuilder.loadTexts:
    cfrExtCircuitMinThruputIn.setUnits("bits per second")
_CfrExtCircuitBcastPktOuts_Type = Counter32
_CfrExtCircuitBcastPktOuts_Object = MibTableColumn
cfrExtCircuitBcastPktOuts = _CfrExtCircuitBcastPktOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 15),
    _CfrExtCircuitBcastPktOuts_Type()
)
cfrExtCircuitBcastPktOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitBcastPktOuts.setStatus("current")
_CfrExtCircuitBcastByteOuts_Type = Counter32
_CfrExtCircuitBcastByteOuts_Object = MibTableColumn
cfrExtCircuitBcastByteOuts = _CfrExtCircuitBcastByteOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 16),
    _CfrExtCircuitBcastByteOuts_Type()
)
cfrExtCircuitBcastByteOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitBcastByteOuts.setStatus("current")


class _CfrExtCircuitBandwidth_Type(Integer32):
    """Custom type cfrExtCircuitBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CfrExtCircuitBandwidth_Type.__name__ = "Integer32"
_CfrExtCircuitBandwidth_Object = MibTableColumn
cfrExtCircuitBandwidth = _CfrExtCircuitBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 17),
    _CfrExtCircuitBandwidth_Type()
)
cfrExtCircuitBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cfrExtCircuitBandwidth.setUnits("bits per second")


class _CfrExtCircuitShapeByteLimit_Type(Integer32):
    """Custom type cfrExtCircuitShapeByteLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125, 2147483647),
    )


_CfrExtCircuitShapeByteLimit_Type.__name__ = "Integer32"
_CfrExtCircuitShapeByteLimit_Object = MibTableColumn
cfrExtCircuitShapeByteLimit = _CfrExtCircuitShapeByteLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 18),
    _CfrExtCircuitShapeByteLimit_Type()
)
cfrExtCircuitShapeByteLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitShapeByteLimit.setStatus("current")
if mibBuilder.loadTexts:
    cfrExtCircuitShapeByteLimit.setUnits("octets")


class _CfrExtCircuitShapeInterval_Type(Integer32):
    """Custom type cfrExtCircuitShapeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 125),
    )


_CfrExtCircuitShapeInterval_Type.__name__ = "Integer32"
_CfrExtCircuitShapeInterval_Object = MibTableColumn
cfrExtCircuitShapeInterval = _CfrExtCircuitShapeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 19),
    _CfrExtCircuitShapeInterval_Type()
)
cfrExtCircuitShapeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitShapeInterval.setStatus("current")
if mibBuilder.loadTexts:
    cfrExtCircuitShapeInterval.setUnits("milliseconds")


class _CfrExtCircuitShapeByteIncrement_Type(Integer32):
    """Custom type cfrExtCircuitShapeByteIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125, 2147483647),
    )


_CfrExtCircuitShapeByteIncrement_Type.__name__ = "Integer32"
_CfrExtCircuitShapeByteIncrement_Object = MibTableColumn
cfrExtCircuitShapeByteIncrement = _CfrExtCircuitShapeByteIncrement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 20),
    _CfrExtCircuitShapeByteIncrement_Type()
)
cfrExtCircuitShapeByteIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitShapeByteIncrement.setStatus("current")
if mibBuilder.loadTexts:
    cfrExtCircuitShapeByteIncrement.setUnits("octets")
_CfrExtCircuitShapePkts_Type = Counter32
_CfrExtCircuitShapePkts_Object = MibTableColumn
cfrExtCircuitShapePkts = _CfrExtCircuitShapePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 21),
    _CfrExtCircuitShapePkts_Type()
)
cfrExtCircuitShapePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitShapePkts.setStatus("current")
_CfrExtCircuitShapeBytes_Type = Counter32
_CfrExtCircuitShapeBytes_Object = MibTableColumn
cfrExtCircuitShapeBytes = _CfrExtCircuitShapeBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 22),
    _CfrExtCircuitShapeBytes_Type()
)
cfrExtCircuitShapeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitShapeBytes.setStatus("current")
if mibBuilder.loadTexts:
    cfrExtCircuitShapeBytes.setUnits("octets")
_CfrExtCircuitShapePktsDelay_Type = Counter32
_CfrExtCircuitShapePktsDelay_Object = MibTableColumn
cfrExtCircuitShapePktsDelay = _CfrExtCircuitShapePktsDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 23),
    _CfrExtCircuitShapePktsDelay_Type()
)
cfrExtCircuitShapePktsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitShapePktsDelay.setStatus("current")
_CfrExtCircuitShapeBytesDelay_Type = Counter32
_CfrExtCircuitShapeBytesDelay_Object = MibTableColumn
cfrExtCircuitShapeBytesDelay = _CfrExtCircuitShapeBytesDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 24),
    _CfrExtCircuitShapeBytesDelay_Type()
)
cfrExtCircuitShapeBytesDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitShapeBytesDelay.setStatus("current")
if mibBuilder.loadTexts:
    cfrExtCircuitShapeBytesDelay.setUnits("octets")
_CfrExtCircuitShapeActive_Type = TruthValue
_CfrExtCircuitShapeActive_Object = MibTableColumn
cfrExtCircuitShapeActive = _CfrExtCircuitShapeActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 25),
    _CfrExtCircuitShapeActive_Type()
)
cfrExtCircuitShapeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitShapeActive.setStatus("current")


class _CfrExtCircuitShapeAdapting_Type(Integer32):
    """Custom type cfrExtCircuitShapeAdapting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("becn", 2),
          ("foreSight", 3),
          ("none", 1))
    )


_CfrExtCircuitShapeAdapting_Type.__name__ = "Integer32"
_CfrExtCircuitShapeAdapting_Object = MibTableColumn
cfrExtCircuitShapeAdapting = _CfrExtCircuitShapeAdapting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 26),
    _CfrExtCircuitShapeAdapting_Type()
)
cfrExtCircuitShapeAdapting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitShapeAdapting.setStatus("current")


class _CfrExtCircuitTxDataRate_Type(Integer32):
    """Custom type cfrExtCircuitTxDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_CfrExtCircuitTxDataRate_Type.__name__ = "Integer32"
_CfrExtCircuitTxDataRate_Object = MibTableColumn
cfrExtCircuitTxDataRate = _CfrExtCircuitTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 27),
    _CfrExtCircuitTxDataRate_Type()
)
cfrExtCircuitTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitTxDataRate.setStatus("current")


class _CfrExtCircuitTxPktRate_Type(Integer32):
    """Custom type cfrExtCircuitTxPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_CfrExtCircuitTxPktRate_Type.__name__ = "Integer32"
_CfrExtCircuitTxPktRate_Object = MibTableColumn
cfrExtCircuitTxPktRate = _CfrExtCircuitTxPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 28),
    _CfrExtCircuitTxPktRate_Type()
)
cfrExtCircuitTxPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitTxPktRate.setStatus("current")


class _CfrExtCircuitRcvDataRate_Type(Integer32):
    """Custom type cfrExtCircuitRcvDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_CfrExtCircuitRcvDataRate_Type.__name__ = "Integer32"
_CfrExtCircuitRcvDataRate_Object = MibTableColumn
cfrExtCircuitRcvDataRate = _CfrExtCircuitRcvDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 29),
    _CfrExtCircuitRcvDataRate_Type()
)
cfrExtCircuitRcvDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitRcvDataRate.setStatus("current")


class _CfrExtCircuitRcvPktRate_Type(Integer32):
    """Custom type cfrExtCircuitRcvPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_CfrExtCircuitRcvPktRate_Type.__name__ = "Integer32"
_CfrExtCircuitRcvPktRate_Object = MibTableColumn
cfrExtCircuitRcvPktRate = _CfrExtCircuitRcvPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 2, 2, 1, 30),
    _CfrExtCircuitRcvPktRate_Type()
)
cfrExtCircuitRcvPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrExtCircuitRcvPktRate.setStatus("current")
_CfrMapObjs_ObjectIdentity = ObjectIdentity
cfrMapObjs = _CfrMapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 3)
)
_CfrMapTable_Object = MibTable
cfrMapTable = _CfrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cfrMapTable.setStatus("current")
_CfrMapEntry_Object = MibTableRow
cfrMapEntry = _CfrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 3, 1, 1)
)
cfrMapEntry.setIndexNames(
    (0, "RFC1315-MIB", "frCircuitIfIndex"),
    (0, "RFC1315-MIB", "frCircuitDlci"),
    (0, "CISCO-FRAME-RELAY-MIB", "cfrMapIndex"),
)
if mibBuilder.loadTexts:
    cfrMapEntry.setStatus("current")


class _CfrMapIndex_Type(Integer32):
    """Custom type cfrMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_CfrMapIndex_Type.__name__ = "Integer32"
_CfrMapIndex_Object = MibTableColumn
cfrMapIndex = _CfrMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 3, 1, 1, 1),
    _CfrMapIndex_Type()
)
cfrMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrMapIndex.setStatus("current")
_CfrMapProtocol_Type = CfrMapProtocols
_CfrMapProtocol_Object = MibTableColumn
cfrMapProtocol = _CfrMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 3, 1, 1, 2),
    _CfrMapProtocol_Type()
)
cfrMapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrMapProtocol.setStatus("current")


class _CfrMapAddress_Type(OctetString):
    """Custom type cfrMapAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CfrMapAddress_Type.__name__ = "OctetString"
_CfrMapAddress_Object = MibTableColumn
cfrMapAddress = _CfrMapAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 3, 1, 1, 3),
    _CfrMapAddress_Type()
)
cfrMapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrMapAddress.setStatus("current")


class _CfrMapType_Type(Integer32):
    """Custom type cfrMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1),
          ("svc", 3))
    )


_CfrMapType_Type.__name__ = "Integer32"
_CfrMapType_Object = MibTableColumn
cfrMapType = _CfrMapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 3, 1, 1, 4),
    _CfrMapType_Type()
)
cfrMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrMapType.setStatus("current")


class _CfrMapEncaps_Type(Integer32):
    """Custom type cfrMapEncaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cisco", 2),
          ("ietf", 1))
    )


_CfrMapEncaps_Type.__name__ = "Integer32"
_CfrMapEncaps_Object = MibTableColumn
cfrMapEncaps = _CfrMapEncaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 3, 1, 1, 5),
    _CfrMapEncaps_Type()
)
cfrMapEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrMapEncaps.setStatus("current")
_CfrMapBroadcast_Type = TruthValue
_CfrMapBroadcast_Object = MibTableColumn
cfrMapBroadcast = _CfrMapBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 3, 1, 1, 6),
    _CfrMapBroadcast_Type()
)
cfrMapBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrMapBroadcast.setStatus("current")
_CfrMapPayloadCompress_Type = TruthValue
_CfrMapPayloadCompress_Object = MibTableColumn
cfrMapPayloadCompress = _CfrMapPayloadCompress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 3, 1, 1, 7),
    _CfrMapPayloadCompress_Type()
)
cfrMapPayloadCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrMapPayloadCompress.setStatus("deprecated")


class _CfrMapTcpHdrCompress_Type(Integer32):
    """Custom type cfrMapTcpHdrCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inapplicable", 1),
          ("passive", 2))
    )


_CfrMapTcpHdrCompress_Type.__name__ = "Integer32"
_CfrMapTcpHdrCompress_Object = MibTableColumn
cfrMapTcpHdrCompress = _CfrMapTcpHdrCompress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 3, 1, 1, 8),
    _CfrMapTcpHdrCompress_Type()
)
cfrMapTcpHdrCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrMapTcpHdrCompress.setStatus("current")


class _CfrMapRtpHdrCompress_Type(Integer32):
    """Custom type cfrMapRtpHdrCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inapplicable", 1),
          ("passive", 2))
    )


_CfrMapRtpHdrCompress_Type.__name__ = "Integer32"
_CfrMapRtpHdrCompress_Object = MibTableColumn
cfrMapRtpHdrCompress = _CfrMapRtpHdrCompress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 3, 1, 1, 9),
    _CfrMapRtpHdrCompress_Type()
)
cfrMapRtpHdrCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrMapRtpHdrCompress.setStatus("current")


class _CfrMapPayloadCompressType_Type(Integer32):
    """Custom type cfrMapPayloadCompressType based on Integer32"""
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
        *(("cisco", 2),
          ("frf9Hardware", 4),
          ("frf9Software", 3),
          ("inapplicable", 1))
    )


_CfrMapPayloadCompressType_Type.__name__ = "Integer32"
_CfrMapPayloadCompressType_Object = MibTableColumn
cfrMapPayloadCompressType = _CfrMapPayloadCompressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 3, 1, 1, 10),
    _CfrMapPayloadCompressType_Type()
)
cfrMapPayloadCompressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrMapPayloadCompressType.setStatus("current")
_CfrSvcObjs_ObjectIdentity = ObjectIdentity
cfrSvcObjs = _CfrSvcObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 4)
)
_CfrSvcTable_Object = MibTable
cfrSvcTable = _CfrSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cfrSvcTable.setStatus("current")
_CfrSvcEntry_Object = MibTableRow
cfrSvcEntry = _CfrSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 4, 1, 1)
)
cfrSvcEntry.setIndexNames(
    (0, "RFC1315-MIB", "frCircuitIfIndex"),
    (0, "RFC1315-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    cfrSvcEntry.setStatus("current")


class _CfrSvcAddrLocal_Type(OctetString):
    """Custom type cfrSvcAddrLocal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CfrSvcAddrLocal_Type.__name__ = "OctetString"
_CfrSvcAddrLocal_Object = MibTableColumn
cfrSvcAddrLocal = _CfrSvcAddrLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 4, 1, 1, 1),
    _CfrSvcAddrLocal_Type()
)
cfrSvcAddrLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrSvcAddrLocal.setStatus("current")


class _CfrSvcAddrRemote_Type(OctetString):
    """Custom type cfrSvcAddrRemote based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CfrSvcAddrRemote_Type.__name__ = "OctetString"
_CfrSvcAddrRemote_Object = MibTableColumn
cfrSvcAddrRemote = _CfrSvcAddrRemote_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 4, 1, 1, 2),
    _CfrSvcAddrRemote_Type()
)
cfrSvcAddrRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrSvcAddrRemote.setStatus("current")


class _CfrSvcThroughputIn_Type(Integer32):
    """Custom type cfrSvcThroughputIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_CfrSvcThroughputIn_Type.__name__ = "Integer32"
_CfrSvcThroughputIn_Object = MibTableColumn
cfrSvcThroughputIn = _CfrSvcThroughputIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 4, 1, 1, 3),
    _CfrSvcThroughputIn_Type()
)
cfrSvcThroughputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrSvcThroughputIn.setStatus("current")
if mibBuilder.loadTexts:
    cfrSvcThroughputIn.setUnits("bits per second")


class _CfrSvcMinThruputOut_Type(Integer32):
    """Custom type cfrSvcMinThruputOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_CfrSvcMinThruputOut_Type.__name__ = "Integer32"
_CfrSvcMinThruputOut_Object = MibTableColumn
cfrSvcMinThruputOut = _CfrSvcMinThruputOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 4, 1, 1, 4),
    _CfrSvcMinThruputOut_Type()
)
cfrSvcMinThruputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrSvcMinThruputOut.setStatus("deprecated")
if mibBuilder.loadTexts:
    cfrSvcMinThruputOut.setUnits("bits per second")


class _CfrSvcMinThruputIn_Type(Integer32):
    """Custom type cfrSvcMinThruputIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_CfrSvcMinThruputIn_Type.__name__ = "Integer32"
_CfrSvcMinThruputIn_Object = MibTableColumn
cfrSvcMinThruputIn = _CfrSvcMinThruputIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 4, 1, 1, 5),
    _CfrSvcMinThruputIn_Type()
)
cfrSvcMinThruputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrSvcMinThruputIn.setStatus("deprecated")
if mibBuilder.loadTexts:
    cfrSvcMinThruputIn.setUnits("bits per second")


class _CfrSvcCommitBurstIn_Type(Integer32):
    """Custom type cfrSvcCommitBurstIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_CfrSvcCommitBurstIn_Type.__name__ = "Integer32"
_CfrSvcCommitBurstIn_Object = MibTableColumn
cfrSvcCommitBurstIn = _CfrSvcCommitBurstIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 4, 1, 1, 6),
    _CfrSvcCommitBurstIn_Type()
)
cfrSvcCommitBurstIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrSvcCommitBurstIn.setStatus("current")


class _CfrSvcExcessBurstIn_Type(Integer32):
    """Custom type cfrSvcExcessBurstIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 2440000),
    )


_CfrSvcExcessBurstIn_Type.__name__ = "Integer32"
_CfrSvcExcessBurstIn_Object = MibTableColumn
cfrSvcExcessBurstIn = _CfrSvcExcessBurstIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 4, 1, 1, 7),
    _CfrSvcExcessBurstIn_Type()
)
cfrSvcExcessBurstIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrSvcExcessBurstIn.setStatus("current")
_CfrSvcIdleTime_Type = Integer32
_CfrSvcIdleTime_Object = MibTableColumn
cfrSvcIdleTime = _CfrSvcIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 4, 1, 1, 8),
    _CfrSvcIdleTime_Type()
)
cfrSvcIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrSvcIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    cfrSvcIdleTime.setUnits("seconds")
_CfrElmiObjs_ObjectIdentity = ObjectIdentity
cfrElmiObjs = _CfrElmiObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5)
)
_CfrElmiIpAddr_Type = IpAddress
_CfrElmiIpAddr_Object = MibScalar
cfrElmiIpAddr = _CfrElmiIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 1),
    _CfrElmiIpAddr_Type()
)
cfrElmiIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrElmiIpAddr.setStatus("current")
_CfrElmiTable_Object = MibTable
cfrElmiTable = _CfrElmiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cfrElmiTable.setStatus("current")
_CfrElmiEntry_Object = MibTableRow
cfrElmiEntry = _CfrElmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 2, 1)
)
cfrElmiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfrElmiEntry.setStatus("current")


class _CfrElmiLinkStatus_Type(Integer32):
    """Custom type cfrElmiLinkStatus based on Integer32"""
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


_CfrElmiLinkStatus_Type.__name__ = "Integer32"
_CfrElmiLinkStatus_Object = MibTableColumn
cfrElmiLinkStatus = _CfrElmiLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 2, 1, 1),
    _CfrElmiLinkStatus_Type()
)
cfrElmiLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrElmiLinkStatus.setStatus("current")


class _CfrElmiArStatus_Type(Integer32):
    """Custom type cfrElmiArStatus based on Integer32"""
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


_CfrElmiArStatus_Type.__name__ = "Integer32"
_CfrElmiArStatus_Object = MibTableColumn
cfrElmiArStatus = _CfrElmiArStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 2, 1, 2),
    _CfrElmiArStatus_Type()
)
cfrElmiArStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrElmiArStatus.setStatus("current")


class _CfrElmiRemoteStatus_Type(Integer32):
    """Custom type cfrElmiRemoteStatus based on Integer32"""
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


_CfrElmiRemoteStatus_Type.__name__ = "Integer32"
_CfrElmiRemoteStatus_Object = MibTableColumn
cfrElmiRemoteStatus = _CfrElmiRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 2, 1, 3),
    _CfrElmiRemoteStatus_Type()
)
cfrElmiRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrElmiRemoteStatus.setStatus("current")
_CfrElmiNeighborTable_Object = MibTable
cfrElmiNeighborTable = _CfrElmiNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cfrElmiNeighborTable.setStatus("current")
_CfrElmiNeighborEntry_Object = MibTableRow
cfrElmiNeighborEntry = _CfrElmiNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 3, 1)
)
cfrElmiNeighborEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfrElmiNeighborEntry.setStatus("current")


class _CfrElmiNeighborArStatus_Type(Integer32):
    """Custom type cfrElmiNeighborArStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("notsupported", 1))
    )


_CfrElmiNeighborArStatus_Type.__name__ = "Integer32"
_CfrElmiNeighborArStatus_Object = MibTableColumn
cfrElmiNeighborArStatus = _CfrElmiNeighborArStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 3, 1, 1),
    _CfrElmiNeighborArStatus_Type()
)
cfrElmiNeighborArStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrElmiNeighborArStatus.setStatus("current")
_CfrElmiNeighborIpAddress_Type = IpAddress
_CfrElmiNeighborIpAddress_Object = MibTableColumn
cfrElmiNeighborIpAddress = _CfrElmiNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 3, 1, 2),
    _CfrElmiNeighborIpAddress_Type()
)
cfrElmiNeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrElmiNeighborIpAddress.setStatus("current")
_CfrElmiNeighborIfIndex_Type = InterfaceIndex
_CfrElmiNeighborIfIndex_Object = MibTableColumn
cfrElmiNeighborIfIndex = _CfrElmiNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 3, 1, 3),
    _CfrElmiNeighborIfIndex_Type()
)
cfrElmiNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrElmiNeighborIfIndex.setStatus("current")
_CfrElmiNeighborVendorName_Type = DisplayString
_CfrElmiNeighborVendorName_Object = MibTableColumn
cfrElmiNeighborVendorName = _CfrElmiNeighborVendorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 3, 1, 4),
    _CfrElmiNeighborVendorName_Type()
)
cfrElmiNeighborVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrElmiNeighborVendorName.setStatus("current")
_CfrElmiNeighborPlatformName_Type = DisplayString
_CfrElmiNeighborPlatformName_Object = MibTableColumn
cfrElmiNeighborPlatformName = _CfrElmiNeighborPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 3, 1, 5),
    _CfrElmiNeighborPlatformName_Type()
)
cfrElmiNeighborPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrElmiNeighborPlatformName.setStatus("current")
_CfrElmiNeighborDeviceName_Type = DisplayString
_CfrElmiNeighborDeviceName_Object = MibTableColumn
cfrElmiNeighborDeviceName = _CfrElmiNeighborDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 5, 3, 1, 6),
    _CfrElmiNeighborDeviceName_Type()
)
cfrElmiNeighborDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrElmiNeighborDeviceName.setStatus("current")
_CfrFragObjs_ObjectIdentity = ObjectIdentity
cfrFragObjs = _CfrFragObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6)
)
_CfrFragTable_Object = MibTable
cfrFragTable = _CfrFragTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cfrFragTable.setStatus("current")
_CfrFragEntry_Object = MibTableRow
cfrFragEntry = _CfrFragEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1)
)
cfrFragEntry.setIndexNames(
    (0, "RFC1315-MIB", "frCircuitIfIndex"),
    (0, "RFC1315-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    cfrFragEntry.setStatus("current")


class _CfrFragSize_Type(Integer32):
    """Custom type cfrFragSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1600),
    )


_CfrFragSize_Type.__name__ = "Integer32"
_CfrFragSize_Object = MibTableColumn
cfrFragSize = _CfrFragSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 1),
    _CfrFragSize_Type()
)
cfrFragSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragSize.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragSize.setUnits("octets")
_CfrFragType_Type = DisplayString
_CfrFragType_Object = MibTableColumn
cfrFragType = _CfrFragType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 2),
    _CfrFragType_Type()
)
cfrFragType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragType.setStatus("current")
_CfrFragInPkts_Type = Counter32
_CfrFragInPkts_Object = MibTableColumn
cfrFragInPkts = _CfrFragInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 3),
    _CfrFragInPkts_Type()
)
cfrFragInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragInPkts.setUnits("packets")
_CfrFragOutPkts_Type = Counter32
_CfrFragOutPkts_Object = MibTableColumn
cfrFragOutPkts = _CfrFragOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 4),
    _CfrFragOutPkts_Type()
)
cfrFragOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragOutPkts.setUnits("packets")
_CfrFragInOctets_Type = Counter32
_CfrFragInOctets_Object = MibTableColumn
cfrFragInOctets = _CfrFragInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 5),
    _CfrFragInOctets_Type()
)
cfrFragInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragInOctets.setUnits("octets")
_CfrFragOutOctets_Type = Counter32
_CfrFragOutOctets_Object = MibTableColumn
cfrFragOutOctets = _CfrFragOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 6),
    _CfrFragOutOctets_Type()
)
cfrFragOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragOutOctets.setUnits("octets")
_CfrFragNotInPkts_Type = Counter32
_CfrFragNotInPkts_Object = MibTableColumn
cfrFragNotInPkts = _CfrFragNotInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 7),
    _CfrFragNotInPkts_Type()
)
cfrFragNotInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragNotInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragNotInPkts.setUnits("packets")
_CfrFragNotOutPkts_Type = Counter32
_CfrFragNotOutPkts_Object = MibTableColumn
cfrFragNotOutPkts = _CfrFragNotOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 8),
    _CfrFragNotOutPkts_Type()
)
cfrFragNotOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragNotOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragNotOutPkts.setUnits("packets")
_CfrFragNotInOctets_Type = Counter32
_CfrFragNotInOctets_Object = MibTableColumn
cfrFragNotInOctets = _CfrFragNotInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 9),
    _CfrFragNotInOctets_Type()
)
cfrFragNotInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragNotInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragNotInOctets.setUnits("octets")
_CfrFragNotOutOctets_Type = Counter32
_CfrFragNotOutOctets_Object = MibTableColumn
cfrFragNotOutOctets = _CfrFragNotOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 10),
    _CfrFragNotOutOctets_Type()
)
cfrFragNotOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragNotOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragNotOutOctets.setUnits("octets")
_CfrFragAssembledInPkts_Type = Counter32
_CfrFragAssembledInPkts_Object = MibTableColumn
cfrFragAssembledInPkts = _CfrFragAssembledInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 11),
    _CfrFragAssembledInPkts_Type()
)
cfrFragAssembledInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragAssembledInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragAssembledInPkts.setUnits("packets")
_CfrFragAssembledInOctets_Type = Counter32
_CfrFragAssembledInOctets_Object = MibTableColumn
cfrFragAssembledInOctets = _CfrFragAssembledInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 12),
    _CfrFragAssembledInOctets_Type()
)
cfrFragAssembledInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragAssembledInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragAssembledInOctets.setUnits("octets")
_CfrFragPreOutPkts_Type = Counter32
_CfrFragPreOutPkts_Object = MibTableColumn
cfrFragPreOutPkts = _CfrFragPreOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 13),
    _CfrFragPreOutPkts_Type()
)
cfrFragPreOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragPreOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragPreOutPkts.setUnits("packets")
_CfrFragPreOutOctets_Type = Counter32
_CfrFragPreOutOctets_Object = MibTableColumn
cfrFragPreOutOctets = _CfrFragPreOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 14),
    _CfrFragPreOutOctets_Type()
)
cfrFragPreOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragPreOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragPreOutOctets.setUnits("octets")
_CfrFragDroppedReAssembledInPkts_Type = Counter32
_CfrFragDroppedReAssembledInPkts_Object = MibTableColumn
cfrFragDroppedReAssembledInPkts = _CfrFragDroppedReAssembledInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 15),
    _CfrFragDroppedReAssembledInPkts_Type()
)
cfrFragDroppedReAssembledInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragDroppedReAssembledInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragDroppedReAssembledInPkts.setUnits("packets")
_CfrFragDroppedFragmentedOutPkts_Type = Counter32
_CfrFragDroppedFragmentedOutPkts_Object = MibTableColumn
cfrFragDroppedFragmentedOutPkts = _CfrFragDroppedFragmentedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 16),
    _CfrFragDroppedFragmentedOutPkts_Type()
)
cfrFragDroppedFragmentedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragDroppedFragmentedOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragDroppedFragmentedOutPkts.setUnits("packets")


class _CfrFragTimeoutsIn_Type(Integer32):
    """Custom type cfrFragTimeoutsIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CfrFragTimeoutsIn_Type.__name__ = "Integer32"
_CfrFragTimeoutsIn_Object = MibTableColumn
cfrFragTimeoutsIn = _CfrFragTimeoutsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 17),
    _CfrFragTimeoutsIn_Type()
)
cfrFragTimeoutsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragTimeoutsIn.setStatus("current")
_CfrFragOutOfSeqFragPkts_Type = Counter32
_CfrFragOutOfSeqFragPkts_Object = MibTableColumn
cfrFragOutOfSeqFragPkts = _CfrFragOutOfSeqFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 18),
    _CfrFragOutOfSeqFragPkts_Type()
)
cfrFragOutOfSeqFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragOutOfSeqFragPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragOutOfSeqFragPkts.setUnits("packets")
_CfrFragUnexpectedBBitSetPkts_Type = Counter32
_CfrFragUnexpectedBBitSetPkts_Object = MibTableColumn
cfrFragUnexpectedBBitSetPkts = _CfrFragUnexpectedBBitSetPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 19),
    _CfrFragUnexpectedBBitSetPkts_Type()
)
cfrFragUnexpectedBBitSetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragUnexpectedBBitSetPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragUnexpectedBBitSetPkts.setUnits("packets")
_CfrFragSeqMissedPkts_Type = Counter32
_CfrFragSeqMissedPkts_Object = MibTableColumn
cfrFragSeqMissedPkts = _CfrFragSeqMissedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 20),
    _CfrFragSeqMissedPkts_Type()
)
cfrFragSeqMissedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragSeqMissedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragSeqMissedPkts.setUnits("packets")
_CfrFragInterleavedOutPkts_Type = Counter32
_CfrFragInterleavedOutPkts_Object = MibTableColumn
cfrFragInterleavedOutPkts = _CfrFragInterleavedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 6, 1, 1, 21),
    _CfrFragInterleavedOutPkts_Type()
)
cfrFragInterleavedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrFragInterleavedOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfrFragInterleavedOutPkts.setUnits("packets")
_CfrConnectionObjs_ObjectIdentity = ObjectIdentity
cfrConnectionObjs = _CfrConnectionObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7)
)
_CfrConnectionTable_Object = MibTable
cfrConnectionTable = _CfrConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cfrConnectionTable.setStatus("current")
_CfrConnectionEntry_Object = MibTableRow
cfrConnectionEntry = _CfrConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1)
)
cfrConnectionEntry.setIndexNames(
    (0, "RFC1315-MIB", "frCircuitIfIndex"),
    (0, "RFC1315-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    cfrConnectionEntry.setStatus("current")
_CfrConnName_Type = DisplayString
_CfrConnName_Object = MibTableColumn
cfrConnName = _CfrConnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 1),
    _CfrConnName_Type()
)
cfrConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnName.setStatus("current")


class _CfrConnID_Type(Integer32):
    """Custom type cfrConnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_CfrConnID_Type.__name__ = "Integer32"
_CfrConnID_Object = MibTableColumn
cfrConnID = _CfrConnID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 2),
    _CfrConnID_Type()
)
cfrConnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnID.setStatus("current")
_CfrConnState_Type = DisplayString
_CfrConnState_Object = MibTableColumn
cfrConnState = _CfrConnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 3),
    _CfrConnState_Type()
)
cfrConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnState.setStatus("current")
_CfrConnSegment1Name_Type = DisplayString
_CfrConnSegment1Name_Object = MibTableColumn
cfrConnSegment1Name = _CfrConnSegment1Name_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 4),
    _CfrConnSegment1Name_Type()
)
cfrConnSegment1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnSegment1Name.setStatus("current")
_CfrConnSegment1VCGroup_Type = DisplayString
_CfrConnSegment1VCGroup_Object = MibTableColumn
cfrConnSegment1VCGroup = _CfrConnSegment1VCGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 5),
    _CfrConnSegment1VCGroup_Type()
)
cfrConnSegment1VCGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnSegment1VCGroup.setStatus("current")
_CfrConnSegment1Dlci_Type = DlciNumber
_CfrConnSegment1Dlci_Object = MibTableColumn
cfrConnSegment1Dlci = _CfrConnSegment1Dlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 6),
    _CfrConnSegment1Dlci_Type()
)
cfrConnSegment1Dlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnSegment1Dlci.setStatus("current")
_CfrConnSegment2Name_Type = DisplayString
_CfrConnSegment2Name_Object = MibTableColumn
cfrConnSegment2Name = _CfrConnSegment2Name_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 7),
    _CfrConnSegment2Name_Type()
)
cfrConnSegment2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnSegment2Name.setStatus("current")


class _CfrConnSegment2Vpi_Type(Integer32):
    """Custom type cfrConnSegment2Vpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CfrConnSegment2Vpi_Type.__name__ = "Integer32"
_CfrConnSegment2Vpi_Object = MibTableColumn
cfrConnSegment2Vpi = _CfrConnSegment2Vpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 8),
    _CfrConnSegment2Vpi_Type()
)
cfrConnSegment2Vpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnSegment2Vpi.setStatus("current")


class _CfrConnSegment2Vci_Type(Integer32):
    """Custom type cfrConnSegment2Vci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CfrConnSegment2Vci_Type.__name__ = "Integer32"
_CfrConnSegment2Vci_Object = MibTableColumn
cfrConnSegment2Vci = _CfrConnSegment2Vci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 9),
    _CfrConnSegment2Vci_Type()
)
cfrConnSegment2Vci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnSegment2Vci.setStatus("current")


class _CfrConnServiceTranslation_Type(Integer32):
    """Custom type cfrConnServiceTranslation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("serviceTranslationEnabled", 1),
          ("serviceTranslationNotEnabled", 2))
    )


_CfrConnServiceTranslation_Type.__name__ = "Integer32"
_CfrConnServiceTranslation_Object = MibTableColumn
cfrConnServiceTranslation = _CfrConnServiceTranslation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 10),
    _CfrConnServiceTranslation_Type()
)
cfrConnServiceTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnServiceTranslation.setStatus("current")
_CfrConnFrSscsDlci_Type = DlciNumber
_CfrConnFrSscsDlci_Object = MibTableColumn
cfrConnFrSscsDlci = _CfrConnFrSscsDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 11),
    _CfrConnFrSscsDlci_Type()
)
cfrConnFrSscsDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnFrSscsDlci.setStatus("current")


class _CfrConnEfciBit_Type(Integer32):
    """Custom type cfrConnEfciBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mapFecn", 1),
          ("notMapFecn", 2))
    )


_CfrConnEfciBit_Type.__name__ = "Integer32"
_CfrConnEfciBit_Object = MibTableColumn
cfrConnEfciBit = _CfrConnEfciBit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 12),
    _CfrConnEfciBit_Type()
)
cfrConnEfciBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnEfciBit.setStatus("current")


class _CfrConnDeBit_Type(Integer32):
    """Custom type cfrConnDeBit based on Integer32"""
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
        *(("mapClp", 2),
          ("noMapClp", 1),
          ("setDe0", 3),
          ("setDe1", 4))
    )


_CfrConnDeBit_Type.__name__ = "Integer32"
_CfrConnDeBit_Object = MibTableColumn
cfrConnDeBit = _CfrConnDeBit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 13),
    _CfrConnDeBit_Type()
)
cfrConnDeBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnDeBit.setStatus("current")


class _CfrConnClpBit_Type(Integer32):
    """Custom type cfrConnClpBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("copyDeToClp", 4),
          ("copyDeToFrsscsDeAndClp", 3),
          ("setClp0", 6),
          ("setClp1", 5),
          ("setClpTo0AndCopyDeToFrsscsDe", 1),
          ("setClpTo1AndCopyDeToFrsscsDe", 2))
    )


_CfrConnClpBit_Type.__name__ = "Integer32"
_CfrConnClpBit_Object = MibTableColumn
cfrConnClpBit = _CfrConnClpBit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 1, 7, 1, 1, 14),
    _CfrConnClpBit_Type()
)
cfrConnClpBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfrConnClpBit.setStatus("current")
_CiscoFrMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFrMIBConformance = _CiscoFrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3)
)
_CiscoFrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFrMIBCompliances = _CiscoFrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 1)
)
_CiscoFrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFrMIBGroups = _CiscoFrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2)
)
frDlcmiEntry.registerAugmentions(
    ("CISCO-FRAME-RELAY-MIB",
     "cfrLmiEntry")
)
cfrLmiEntry.setIndexNames(*frDlcmiEntry.getIndexNames())
frCircuitEntry.registerAugmentions(
    ("CISCO-FRAME-RELAY-MIB",
     "cfrCircuitEntry")
)
cfrCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())
frCircuitEntry.registerAugmentions(
    ("CISCO-FRAME-RELAY-MIB",
     "cfrExtCircuitEntry")
)
cfrExtCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())

# Managed Objects groups

ciscoFrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2, 1)
)
ciscoFrMIBGroup.setObjects(
      *(("CISCO-FRAME-RELAY-MIB", "cfrLmiLinkstatus"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiLinkType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiEnquiryIns"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiEnquiryOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiStatusIns"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiStatusOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiUpdateStatusIns"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiUpdateStatusOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiStatusTimeouts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiStatusEnqTimeouts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiN392Dce"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiN393Dce"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiT392Dce"),
        ("CISCO-FRAME-RELAY-MIB", "cfrCircuitDEins"),
        ("CISCO-FRAME-RELAY-MIB", "cfrCircuitDEouts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrCircuitDropPktsOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrCircuitType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitIfName"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitIfType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitSubifIndex"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitMapStatus"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitCreateType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitMulticast"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitRoutedDlci"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitRoutedIf"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapIndex"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapProtocol"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapAddress"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapEncaps"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapBroadcast"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapPayloadCompress"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapTcpHdrCompress"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcAddrLocal"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcAddrRemote"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcThroughputIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcMinThruputOut"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcMinThruputIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcCommitBurstIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcExcessBurstIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcIdleTime"))
)
if mibBuilder.loadTexts:
    ciscoFrMIBGroup.setStatus("deprecated")

ciscoFrMIBGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2, 2)
)
ciscoFrMIBGroupRev1.setObjects(
      *(("CISCO-FRAME-RELAY-MIB", "cfrLmiLinkstatus"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiLinkType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiEnquiryIns"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiEnquiryOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiStatusIns"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiStatusOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiUpdateStatusIns"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiUpdateStatusOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiStatusTimeouts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiStatusEnqTimeouts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiN392Dce"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiN393Dce"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiT392Dce"),
        ("CISCO-FRAME-RELAY-MIB", "cfrCircuitDEins"),
        ("CISCO-FRAME-RELAY-MIB", "cfrCircuitDEouts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrCircuitDropPktsOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrCircuitType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitIfName"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitIfType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitSubifIndex"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitMapStatus"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitCreateType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitMulticast"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitRoutedDlci"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitRoutedIf"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitUncompressIns"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitUncompressOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapIndex"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapProtocol"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapAddress"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapEncaps"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapBroadcast"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapTcpHdrCompress"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapRtpHdrCompress"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapPayloadCompressType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcAddrLocal"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcAddrRemote"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcThroughputIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcMinThruputOut"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcMinThruputIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcCommitBurstIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcExcessBurstIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcIdleTime"))
)
if mibBuilder.loadTexts:
    ciscoFrMIBGroupRev1.setStatus("deprecated")

ciscoFrLmiMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2, 3)
)
ciscoFrLmiMIBGroup.setObjects(
      *(("CISCO-FRAME-RELAY-MIB", "cfrLmiLinkstatus"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiLinkType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiEnquiryIns"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiEnquiryOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiStatusIns"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiStatusOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiUpdateStatusIns"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiUpdateStatusOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiStatusTimeouts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiStatusEnqTimeouts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiN392Dce"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiN393Dce"),
        ("CISCO-FRAME-RELAY-MIB", "cfrLmiT392Dce"))
)
if mibBuilder.loadTexts:
    ciscoFrLmiMIBGroup.setStatus("current")

ciscoFrCircuitMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2, 4)
)
ciscoFrCircuitMIBGroup.setObjects(
      *(("CISCO-FRAME-RELAY-MIB", "cfrCircuitDEins"),
        ("CISCO-FRAME-RELAY-MIB", "cfrCircuitDEouts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrCircuitDropPktsOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrCircuitType"))
)
if mibBuilder.loadTexts:
    ciscoFrCircuitMIBGroup.setStatus("current")

ciscoExtCircuitMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2, 5)
)
ciscoExtCircuitMIBGroup.setObjects(
      *(("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitIfName"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitIfType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitSubifIndex"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitMapStatus"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitCreateType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitMulticast"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitRoutedDlci"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitRoutedIf"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitUncompressIns"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitUncompressOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitFECNOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitBECNOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitMinThruputOut"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitMinThruputIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitBcastPktOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitBcastByteOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitBandwidth"))
)
if mibBuilder.loadTexts:
    ciscoExtCircuitMIBGroup.setStatus("deprecated")

ciscoFrTsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2, 6)
)
ciscoFrTsMIBGroup.setObjects(
      *(("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitShapeByteLimit"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitShapeInterval"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitShapeByteIncrement"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitShapePkts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitShapeBytes"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitShapePktsDelay"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitShapeBytesDelay"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitShapeActive"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitShapeAdapting"))
)
if mibBuilder.loadTexts:
    ciscoFrTsMIBGroup.setStatus("current")

ciscoFrMapMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2, 7)
)
ciscoFrMapMIBGroup.setObjects(
      *(("CISCO-FRAME-RELAY-MIB", "cfrMapIndex"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapProtocol"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapAddress"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapEncaps"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapBroadcast"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapTcpHdrCompress"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapRtpHdrCompress"),
        ("CISCO-FRAME-RELAY-MIB", "cfrMapPayloadCompressType"))
)
if mibBuilder.loadTexts:
    ciscoFrMapMIBGroup.setStatus("current")

ciscoFrSvcMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2, 8)
)
ciscoFrSvcMIBGroup.setObjects(
      *(("CISCO-FRAME-RELAY-MIB", "cfrSvcAddrLocal"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcAddrRemote"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcThroughputIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcCommitBurstIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcExcessBurstIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrSvcIdleTime"))
)
if mibBuilder.loadTexts:
    ciscoFrSvcMIBGroup.setStatus("current")

ciscoFrElmiMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2, 9)
)
ciscoFrElmiMIBGroup.setObjects(
      *(("CISCO-FRAME-RELAY-MIB", "cfrElmiIpAddr"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiArStatus"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiRemoteStatus"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiNeighborArStatus"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiNeighborIpAddress"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiNeighborIfIndex"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiNeighborVendorName"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiNeighborPlatformName"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiNeighborDeviceName"))
)
if mibBuilder.loadTexts:
    ciscoFrElmiMIBGroup.setStatus("deprecated")

ciscoFrElmiMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2, 10)
)
ciscoFrElmiMIBGroup1.setObjects(
      *(("CISCO-FRAME-RELAY-MIB", "cfrElmiIpAddr"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiArStatus"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiRemoteStatus"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiNeighborArStatus"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiNeighborIpAddress"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiNeighborIfIndex"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiNeighborVendorName"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiNeighborPlatformName"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiNeighborDeviceName"),
        ("CISCO-FRAME-RELAY-MIB", "cfrElmiLinkStatus"))
)
if mibBuilder.loadTexts:
    ciscoFrElmiMIBGroup1.setStatus("current")

ciscoFrFragMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2, 11)
)
ciscoFrFragMIBGroup.setObjects(
      *(("CISCO-FRAME-RELAY-MIB", "cfrFragSize"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragInPkts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragOutPkts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragInOctets"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragOutOctets"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragNotInPkts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragNotOutPkts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragNotInOctets"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragNotOutOctets"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragAssembledInPkts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragAssembledInOctets"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragPreOutPkts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragPreOutOctets"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragDroppedReAssembledInPkts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragDroppedFragmentedOutPkts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragTimeoutsIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragOutOfSeqFragPkts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragUnexpectedBBitSetPkts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragSeqMissedPkts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrFragInterleavedOutPkts"))
)
if mibBuilder.loadTexts:
    ciscoFrFragMIBGroup.setStatus("current")

ciscoFrConnMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2, 12)
)
ciscoFrConnMIBGroup.setObjects(
      *(("CISCO-FRAME-RELAY-MIB", "cfrConnName"),
        ("CISCO-FRAME-RELAY-MIB", "cfrConnID"),
        ("CISCO-FRAME-RELAY-MIB", "cfrConnState"),
        ("CISCO-FRAME-RELAY-MIB", "cfrConnSegment1Name"),
        ("CISCO-FRAME-RELAY-MIB", "cfrConnSegment1VCGroup"),
        ("CISCO-FRAME-RELAY-MIB", "cfrConnSegment1Dlci"),
        ("CISCO-FRAME-RELAY-MIB", "cfrConnSegment2Name"),
        ("CISCO-FRAME-RELAY-MIB", "cfrConnSegment2Vpi"),
        ("CISCO-FRAME-RELAY-MIB", "cfrConnSegment2Vci"),
        ("CISCO-FRAME-RELAY-MIB", "cfrConnServiceTranslation"),
        ("CISCO-FRAME-RELAY-MIB", "cfrConnFrSscsDlci"),
        ("CISCO-FRAME-RELAY-MIB", "cfrConnEfciBit"),
        ("CISCO-FRAME-RELAY-MIB", "cfrConnDeBit"),
        ("CISCO-FRAME-RELAY-MIB", "cfrConnClpBit"))
)
if mibBuilder.loadTexts:
    ciscoFrConnMIBGroup.setStatus("current")

ciscoExtCircuitMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 2, 13)
)
ciscoExtCircuitMIBGroup1.setObjects(
      *(("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitIfName"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitIfType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitSubifIndex"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitMapStatus"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitCreateType"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitMulticast"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitRoutedDlci"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitRoutedIf"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitUncompressIns"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitUncompressOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitFECNOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitBECNOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitMinThruputOut"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitMinThruputIn"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitBcastPktOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitBcastByteOuts"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitBandwidth"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitTxDataRate"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitTxPktRate"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitRcvDataRate"),
        ("CISCO-FRAME-RELAY-MIB", "cfrExtCircuitRcvPktRate"))
)
if mibBuilder.loadTexts:
    ciscoExtCircuitMIBGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoFrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFrMIBCompliance.setStatus(
        "obsolete"
    )

ciscoFrMIBCompliancesRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoFrMIBCompliancesRev1.setStatus(
        "obsolete"
    )

ciscoFrMIBCompliancesRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoFrMIBCompliancesRev2.setStatus(
        "obsolete"
    )

ciscoFrMIBCompliancesRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoFrMIBCompliancesRev3.setStatus(
        "deprecated"
    )

ciscoFrMIBCompliancesRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 49, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoFrMIBCompliancesRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FRAME-RELAY-MIB",
    **{"DlciNumber": DlciNumber,
       "CfrMapProtocols": CfrMapProtocols,
       "ciscoFrameRelayMIB": ciscoFrameRelayMIB,
       "ciscoFrMIBObjects": ciscoFrMIBObjects,
       "cfrLmiObjs": cfrLmiObjs,
       "cfrLmiTable": cfrLmiTable,
       "cfrLmiEntry": cfrLmiEntry,
       "cfrLmiLinkstatus": cfrLmiLinkstatus,
       "cfrLmiLinkType": cfrLmiLinkType,
       "cfrLmiEnquiryIns": cfrLmiEnquiryIns,
       "cfrLmiEnquiryOuts": cfrLmiEnquiryOuts,
       "cfrLmiStatusIns": cfrLmiStatusIns,
       "cfrLmiStatusOuts": cfrLmiStatusOuts,
       "cfrLmiUpdateStatusIns": cfrLmiUpdateStatusIns,
       "cfrLmiUpdateStatusOuts": cfrLmiUpdateStatusOuts,
       "cfrLmiStatusTimeouts": cfrLmiStatusTimeouts,
       "cfrLmiStatusEnqTimeouts": cfrLmiStatusEnqTimeouts,
       "cfrLmiN392Dce": cfrLmiN392Dce,
       "cfrLmiN393Dce": cfrLmiN393Dce,
       "cfrLmiT392Dce": cfrLmiT392Dce,
       "cfrCircuitObjs": cfrCircuitObjs,
       "cfrCircuitTable": cfrCircuitTable,
       "cfrCircuitEntry": cfrCircuitEntry,
       "cfrCircuitDEins": cfrCircuitDEins,
       "cfrCircuitDEouts": cfrCircuitDEouts,
       "cfrCircuitDropPktsOuts": cfrCircuitDropPktsOuts,
       "cfrCircuitType": cfrCircuitType,
       "cfrExtCircuitTable": cfrExtCircuitTable,
       "cfrExtCircuitEntry": cfrExtCircuitEntry,
       "cfrExtCircuitIfName": cfrExtCircuitIfName,
       "cfrExtCircuitIfType": cfrExtCircuitIfType,
       "cfrExtCircuitSubifIndex": cfrExtCircuitSubifIndex,
       "cfrExtCircuitMapStatus": cfrExtCircuitMapStatus,
       "cfrExtCircuitCreateType": cfrExtCircuitCreateType,
       "cfrExtCircuitMulticast": cfrExtCircuitMulticast,
       "cfrExtCircuitRoutedDlci": cfrExtCircuitRoutedDlci,
       "cfrExtCircuitRoutedIf": cfrExtCircuitRoutedIf,
       "cfrExtCircuitUncompressIns": cfrExtCircuitUncompressIns,
       "cfrExtCircuitUncompressOuts": cfrExtCircuitUncompressOuts,
       "cfrExtCircuitFECNOuts": cfrExtCircuitFECNOuts,
       "cfrExtCircuitBECNOuts": cfrExtCircuitBECNOuts,
       "cfrExtCircuitMinThruputOut": cfrExtCircuitMinThruputOut,
       "cfrExtCircuitMinThruputIn": cfrExtCircuitMinThruputIn,
       "cfrExtCircuitBcastPktOuts": cfrExtCircuitBcastPktOuts,
       "cfrExtCircuitBcastByteOuts": cfrExtCircuitBcastByteOuts,
       "cfrExtCircuitBandwidth": cfrExtCircuitBandwidth,
       "cfrExtCircuitShapeByteLimit": cfrExtCircuitShapeByteLimit,
       "cfrExtCircuitShapeInterval": cfrExtCircuitShapeInterval,
       "cfrExtCircuitShapeByteIncrement": cfrExtCircuitShapeByteIncrement,
       "cfrExtCircuitShapePkts": cfrExtCircuitShapePkts,
       "cfrExtCircuitShapeBytes": cfrExtCircuitShapeBytes,
       "cfrExtCircuitShapePktsDelay": cfrExtCircuitShapePktsDelay,
       "cfrExtCircuitShapeBytesDelay": cfrExtCircuitShapeBytesDelay,
       "cfrExtCircuitShapeActive": cfrExtCircuitShapeActive,
       "cfrExtCircuitShapeAdapting": cfrExtCircuitShapeAdapting,
       "cfrExtCircuitTxDataRate": cfrExtCircuitTxDataRate,
       "cfrExtCircuitTxPktRate": cfrExtCircuitTxPktRate,
       "cfrExtCircuitRcvDataRate": cfrExtCircuitRcvDataRate,
       "cfrExtCircuitRcvPktRate": cfrExtCircuitRcvPktRate,
       "cfrMapObjs": cfrMapObjs,
       "cfrMapTable": cfrMapTable,
       "cfrMapEntry": cfrMapEntry,
       "cfrMapIndex": cfrMapIndex,
       "cfrMapProtocol": cfrMapProtocol,
       "cfrMapAddress": cfrMapAddress,
       "cfrMapType": cfrMapType,
       "cfrMapEncaps": cfrMapEncaps,
       "cfrMapBroadcast": cfrMapBroadcast,
       "cfrMapPayloadCompress": cfrMapPayloadCompress,
       "cfrMapTcpHdrCompress": cfrMapTcpHdrCompress,
       "cfrMapRtpHdrCompress": cfrMapRtpHdrCompress,
       "cfrMapPayloadCompressType": cfrMapPayloadCompressType,
       "cfrSvcObjs": cfrSvcObjs,
       "cfrSvcTable": cfrSvcTable,
       "cfrSvcEntry": cfrSvcEntry,
       "cfrSvcAddrLocal": cfrSvcAddrLocal,
       "cfrSvcAddrRemote": cfrSvcAddrRemote,
       "cfrSvcThroughputIn": cfrSvcThroughputIn,
       "cfrSvcMinThruputOut": cfrSvcMinThruputOut,
       "cfrSvcMinThruputIn": cfrSvcMinThruputIn,
       "cfrSvcCommitBurstIn": cfrSvcCommitBurstIn,
       "cfrSvcExcessBurstIn": cfrSvcExcessBurstIn,
       "cfrSvcIdleTime": cfrSvcIdleTime,
       "cfrElmiObjs": cfrElmiObjs,
       "cfrElmiIpAddr": cfrElmiIpAddr,
       "cfrElmiTable": cfrElmiTable,
       "cfrElmiEntry": cfrElmiEntry,
       "cfrElmiLinkStatus": cfrElmiLinkStatus,
       "cfrElmiArStatus": cfrElmiArStatus,
       "cfrElmiRemoteStatus": cfrElmiRemoteStatus,
       "cfrElmiNeighborTable": cfrElmiNeighborTable,
       "cfrElmiNeighborEntry": cfrElmiNeighborEntry,
       "cfrElmiNeighborArStatus": cfrElmiNeighborArStatus,
       "cfrElmiNeighborIpAddress": cfrElmiNeighborIpAddress,
       "cfrElmiNeighborIfIndex": cfrElmiNeighborIfIndex,
       "cfrElmiNeighborVendorName": cfrElmiNeighborVendorName,
       "cfrElmiNeighborPlatformName": cfrElmiNeighborPlatformName,
       "cfrElmiNeighborDeviceName": cfrElmiNeighborDeviceName,
       "cfrFragObjs": cfrFragObjs,
       "cfrFragTable": cfrFragTable,
       "cfrFragEntry": cfrFragEntry,
       "cfrFragSize": cfrFragSize,
       "cfrFragType": cfrFragType,
       "cfrFragInPkts": cfrFragInPkts,
       "cfrFragOutPkts": cfrFragOutPkts,
       "cfrFragInOctets": cfrFragInOctets,
       "cfrFragOutOctets": cfrFragOutOctets,
       "cfrFragNotInPkts": cfrFragNotInPkts,
       "cfrFragNotOutPkts": cfrFragNotOutPkts,
       "cfrFragNotInOctets": cfrFragNotInOctets,
       "cfrFragNotOutOctets": cfrFragNotOutOctets,
       "cfrFragAssembledInPkts": cfrFragAssembledInPkts,
       "cfrFragAssembledInOctets": cfrFragAssembledInOctets,
       "cfrFragPreOutPkts": cfrFragPreOutPkts,
       "cfrFragPreOutOctets": cfrFragPreOutOctets,
       "cfrFragDroppedReAssembledInPkts": cfrFragDroppedReAssembledInPkts,
       "cfrFragDroppedFragmentedOutPkts": cfrFragDroppedFragmentedOutPkts,
       "cfrFragTimeoutsIn": cfrFragTimeoutsIn,
       "cfrFragOutOfSeqFragPkts": cfrFragOutOfSeqFragPkts,
       "cfrFragUnexpectedBBitSetPkts": cfrFragUnexpectedBBitSetPkts,
       "cfrFragSeqMissedPkts": cfrFragSeqMissedPkts,
       "cfrFragInterleavedOutPkts": cfrFragInterleavedOutPkts,
       "cfrConnectionObjs": cfrConnectionObjs,
       "cfrConnectionTable": cfrConnectionTable,
       "cfrConnectionEntry": cfrConnectionEntry,
       "cfrConnName": cfrConnName,
       "cfrConnID": cfrConnID,
       "cfrConnState": cfrConnState,
       "cfrConnSegment1Name": cfrConnSegment1Name,
       "cfrConnSegment1VCGroup": cfrConnSegment1VCGroup,
       "cfrConnSegment1Dlci": cfrConnSegment1Dlci,
       "cfrConnSegment2Name": cfrConnSegment2Name,
       "cfrConnSegment2Vpi": cfrConnSegment2Vpi,
       "cfrConnSegment2Vci": cfrConnSegment2Vci,
       "cfrConnServiceTranslation": cfrConnServiceTranslation,
       "cfrConnFrSscsDlci": cfrConnFrSscsDlci,
       "cfrConnEfciBit": cfrConnEfciBit,
       "cfrConnDeBit": cfrConnDeBit,
       "cfrConnClpBit": cfrConnClpBit,
       "ciscoFrMIBConformance": ciscoFrMIBConformance,
       "ciscoFrMIBCompliances": ciscoFrMIBCompliances,
       "ciscoFrMIBCompliance": ciscoFrMIBCompliance,
       "ciscoFrMIBCompliancesRev1": ciscoFrMIBCompliancesRev1,
       "ciscoFrMIBCompliancesRev2": ciscoFrMIBCompliancesRev2,
       "ciscoFrMIBCompliancesRev3": ciscoFrMIBCompliancesRev3,
       "ciscoFrMIBCompliancesRev4": ciscoFrMIBCompliancesRev4,
       "ciscoFrMIBGroups": ciscoFrMIBGroups,
       "ciscoFrMIBGroup": ciscoFrMIBGroup,
       "ciscoFrMIBGroupRev1": ciscoFrMIBGroupRev1,
       "ciscoFrLmiMIBGroup": ciscoFrLmiMIBGroup,
       "ciscoFrCircuitMIBGroup": ciscoFrCircuitMIBGroup,
       "ciscoExtCircuitMIBGroup": ciscoExtCircuitMIBGroup,
       "ciscoFrTsMIBGroup": ciscoFrTsMIBGroup,
       "ciscoFrMapMIBGroup": ciscoFrMapMIBGroup,
       "ciscoFrSvcMIBGroup": ciscoFrSvcMIBGroup,
       "ciscoFrElmiMIBGroup": ciscoFrElmiMIBGroup,
       "ciscoFrElmiMIBGroup1": ciscoFrElmiMIBGroup1,
       "ciscoFrFragMIBGroup": ciscoFrFragMIBGroup,
       "ciscoFrConnMIBGroup": ciscoFrConnMIBGroup,
       "ciscoExtCircuitMIBGroup1": ciscoExtCircuitMIBGroup1}
)
