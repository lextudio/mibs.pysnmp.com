# SNMP MIB module (Wellfleet-VINES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-VINES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:23 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfVinesGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfVinesGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfVinesBase_ObjectIdentity = ObjectIdentity
wfVinesBase = _WfVinesBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1)
)


class _WfVinesBaseDelete_Type(Integer32):
    """Custom type wfVinesBaseDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfVinesBaseDelete_Type.__name__ = "Integer32"
_WfVinesBaseDelete_Object = MibScalar
wfVinesBaseDelete = _WfVinesBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 1),
    _WfVinesBaseDelete_Type()
)
wfVinesBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesBaseDelete.setStatus("mandatory")


class _WfVinesBaseDisable_Type(Integer32):
    """Custom type wfVinesBaseDisable based on Integer32"""
    defaultValue = 1

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


_WfVinesBaseDisable_Type.__name__ = "Integer32"
_WfVinesBaseDisable_Object = MibScalar
wfVinesBaseDisable = _WfVinesBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 2),
    _WfVinesBaseDisable_Type()
)
wfVinesBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesBaseDisable.setStatus("mandatory")


class _WfVinesBaseState_Type(Integer32):
    """Custom type wfVinesBaseState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfVinesBaseState_Type.__name__ = "Integer32"
_WfVinesBaseState_Object = MibScalar
wfVinesBaseState = _WfVinesBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 3),
    _WfVinesBaseState_Type()
)
wfVinesBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesBaseState.setStatus("mandatory")


class _WfVinesBaseUserNetid_Type(Integer32):
    """Custom type wfVinesBaseUserNetid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2097151),
    )


_WfVinesBaseUserNetid_Type.__name__ = "Integer32"
_WfVinesBaseUserNetid_Object = MibScalar
wfVinesBaseUserNetid = _WfVinesBaseUserNetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 4),
    _WfVinesBaseUserNetid_Type()
)
wfVinesBaseUserNetid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesBaseUserNetid.setStatus("mandatory")
_WfVinesBaseRouterNetid_Type = Counter32
_WfVinesBaseRouterNetid_Object = MibScalar
wfVinesBaseRouterNetid = _WfVinesBaseRouterNetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 5),
    _WfVinesBaseRouterNetid_Type()
)
wfVinesBaseRouterNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesBaseRouterNetid.setStatus("mandatory")


class _WfVinesBaseBcastClass_Type(Integer32):
    """Custom type wfVinesBaseBcastClass based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alllans", 8),
          ("bcast", 1),
          ("chrg", 2),
          ("cost", 3),
          ("lans", 4),
          ("locost", 7),
          ("nochrg", 6),
          ("srvr", 5))
    )


_WfVinesBaseBcastClass_Type.__name__ = "Integer32"
_WfVinesBaseBcastClass_Object = MibScalar
wfVinesBaseBcastClass = _WfVinesBaseBcastClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 6),
    _WfVinesBaseBcastClass_Type()
)
wfVinesBaseBcastClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesBaseBcastClass.setStatus("mandatory")
_WfVinesBaseNetworkSize_Type = Integer32
_WfVinesBaseNetworkSize_Object = MibScalar
wfVinesBaseNetworkSize = _WfVinesBaseNetworkSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 7),
    _WfVinesBaseNetworkSize_Type()
)
wfVinesBaseNetworkSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesBaseNetworkSize.setStatus("mandatory")
_WfVinesBaseHostSize_Type = Integer32
_WfVinesBaseHostSize_Object = MibScalar
wfVinesBaseHostSize = _WfVinesBaseHostSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 8),
    _WfVinesBaseHostSize_Type()
)
wfVinesBaseHostSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesBaseHostSize.setStatus("mandatory")


class _WfVinesBaseRtpMode_Type(Integer32):
    """Custom type wfVinesBaseRtpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automode", 1),
          ("seq", 2),
          ("sequenced", 3))
    )


_WfVinesBaseRtpMode_Type.__name__ = "Integer32"
_WfVinesBaseRtpMode_Object = MibScalar
wfVinesBaseRtpMode = _WfVinesBaseRtpMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 9),
    _WfVinesBaseRtpMode_Type()
)
wfVinesBaseRtpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesBaseRtpMode.setStatus("mandatory")


class _WfVinesBaseLogFilter_Type(Integer32):
    """Custom type wfVinesBaseLogFilter based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              16,
              17,
              18,
              19,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("debug", 1),
          ("debuginfo", 3),
          ("debuginfotrace", 19),
          ("debugtrace", 17),
          ("info", 2),
          ("infotrace", 18),
          ("nothing", 2147483647),
          ("trace", 16))
    )


_WfVinesBaseLogFilter_Type.__name__ = "Integer32"
_WfVinesBaseLogFilter_Object = MibScalar
wfVinesBaseLogFilter = _WfVinesBaseLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 10),
    _WfVinesBaseLogFilter_Type()
)
wfVinesBaseLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesBaseLogFilter.setStatus("mandatory")
_WfVinesBaseRouterSeqNumber_Type = Counter32
_WfVinesBaseRouterSeqNumber_Object = MibScalar
wfVinesBaseRouterSeqNumber = _WfVinesBaseRouterSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 11),
    _WfVinesBaseRouterSeqNumber_Type()
)
wfVinesBaseRouterSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesBaseRouterSeqNumber.setStatus("mandatory")


class _WfVinesBaseSoloSlotMask_Type(Gauge32):
    """Custom type wfVinesBaseSoloSlotMask based on Gauge32"""
    defaultValue = 4294705152


_WfVinesBaseSoloSlotMask_Object = MibScalar
wfVinesBaseSoloSlotMask = _WfVinesBaseSoloSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 12),
    _WfVinesBaseSoloSlotMask_Type()
)
wfVinesBaseSoloSlotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesBaseSoloSlotMask.setStatus("mandatory")
_WfVinesBaseSoloistSlot_Type = Integer32
_WfVinesBaseSoloistSlot_Object = MibScalar
wfVinesBaseSoloistSlot = _WfVinesBaseSoloistSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 1, 13),
    _WfVinesBaseSoloistSlot_Type()
)
wfVinesBaseSoloistSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesBaseSoloistSlot.setStatus("mandatory")
_WfVinesIp_ObjectIdentity = ObjectIdentity
wfVinesIp = _WfVinesIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2)
)
_WfVinesIpTotIn_Type = Counter32
_WfVinesIpTotIn_Object = MibScalar
wfVinesIpTotIn = _WfVinesIpTotIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 1),
    _WfVinesIpTotIn_Type()
)
wfVinesIpTotIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpTotIn.setStatus("mandatory")
_WfVinesIpTotOut_Type = Counter32
_WfVinesIpTotOut_Object = MibScalar
wfVinesIpTotOut = _WfVinesIpTotOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 2),
    _WfVinesIpTotOut_Type()
)
wfVinesIpTotOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpTotOut.setStatus("mandatory")
_WfVinesIpBad_Type = Counter32
_WfVinesIpBad_Object = MibScalar
wfVinesIpBad = _WfVinesIpBad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 3),
    _WfVinesIpBad_Type()
)
wfVinesIpBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpBad.setStatus("mandatory")
_WfVinesIpRouted_Type = Counter32
_WfVinesIpRouted_Object = MibScalar
wfVinesIpRouted = _WfVinesIpRouted_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 4),
    _WfVinesIpRouted_Type()
)
wfVinesIpRouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpRouted.setStatus("mandatory")
_WfVinesIpRoutedHWM_Type = Integer32
_WfVinesIpRoutedHWM_Object = MibScalar
wfVinesIpRoutedHWM = _WfVinesIpRoutedHWM_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 5),
    _WfVinesIpRoutedHWM_Type()
)
wfVinesIpRoutedHWM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpRoutedHWM.setStatus("mandatory")
_WfVinesIpBcast_Type = Counter32
_WfVinesIpBcast_Object = MibScalar
wfVinesIpBcast = _WfVinesIpBcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 6),
    _WfVinesIpBcast_Type()
)
wfVinesIpBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpBcast.setStatus("mandatory")
_WfVinesIpBcastHWM_Type = Integer32
_WfVinesIpBcastHWM_Object = MibScalar
wfVinesIpBcastHWM = _WfVinesIpBcastHWM_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 7),
    _WfVinesIpBcastHWM_Type()
)
wfVinesIpBcastHWM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpBcastHWM.setStatus("mandatory")
_WfVinesIpReass_Type = Counter32
_WfVinesIpReass_Object = MibScalar
wfVinesIpReass = _WfVinesIpReass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 8),
    _WfVinesIpReass_Type()
)
wfVinesIpReass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpReass.setStatus("mandatory")
_WfVinesIpFrags_Type = Counter32
_WfVinesIpFrags_Object = MibScalar
wfVinesIpFrags = _WfVinesIpFrags_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 9),
    _WfVinesIpFrags_Type()
)
wfVinesIpFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpFrags.setStatus("mandatory")
_WfVinesIpToDodIP_Type = Counter32
_WfVinesIpToDodIP_Object = MibScalar
wfVinesIpToDodIP = _WfVinesIpToDodIP_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 10),
    _WfVinesIpToDodIP_Type()
)
wfVinesIpToDodIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpToDodIP.setStatus("mandatory")
_WfVinesIpFromDodIP_Type = Counter32
_WfVinesIpFromDodIP_Object = MibScalar
wfVinesIpFromDodIP = _WfVinesIpFromDodIP_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 2, 11),
    _WfVinesIpFromDodIP_Type()
)
wfVinesIpFromDodIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIpFromDodIP.setStatus("mandatory")
_WfVinesRtpNbr_ObjectIdentity = ObjectIdentity
wfVinesRtpNbr = _WfVinesRtpNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 3)
)
_WfVinesRtpNbrNumber_Type = Integer32
_WfVinesRtpNbrNumber_Object = MibScalar
wfVinesRtpNbrNumber = _WfVinesRtpNbrNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 3, 1),
    _WfVinesRtpNbrNumber_Type()
)
wfVinesRtpNbrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrNumber.setStatus("mandatory")
_WfVinesRtpNbrTable_Object = MibTable
wfVinesRtpNbrTable = _WfVinesRtpNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4)
)
if mibBuilder.loadTexts:
    wfVinesRtpNbrTable.setStatus("mandatory")
_WfVinesRtpNbrEntry_Object = MibTableRow
wfVinesRtpNbrEntry = _WfVinesRtpNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1)
)
wfVinesRtpNbrEntry.setIndexNames(
    (0, "Wellfleet-VINES-MIB", "wfVinesRtpNbrNetId"),
    (0, "Wellfleet-VINES-MIB", "wfVinesRtpNbrSubNetId"),
)
if mibBuilder.loadTexts:
    wfVinesRtpNbrEntry.setStatus("mandatory")
_WfVinesRtpNbrNetId_Type = Counter32
_WfVinesRtpNbrNetId_Object = MibTableColumn
wfVinesRtpNbrNetId = _WfVinesRtpNbrNetId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 1),
    _WfVinesRtpNbrNetId_Type()
)
wfVinesRtpNbrNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrNetId.setStatus("mandatory")
_WfVinesRtpNbrSubNetId_Type = Integer32
_WfVinesRtpNbrSubNetId_Object = MibTableColumn
wfVinesRtpNbrSubNetId = _WfVinesRtpNbrSubNetId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 2),
    _WfVinesRtpNbrSubNetId_Type()
)
wfVinesRtpNbrSubNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrSubNetId.setStatus("mandatory")


class _WfVinesRtpNbrType_Type(Integer32):
    """Custom type wfVinesRtpNbrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("server", 2),
          ("workst", 1))
    )


_WfVinesRtpNbrType_Type.__name__ = "Integer32"
_WfVinesRtpNbrType_Object = MibTableColumn
wfVinesRtpNbrType = _WfVinesRtpNbrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 3),
    _WfVinesRtpNbrType_Type()
)
wfVinesRtpNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrType.setStatus("mandatory")


class _WfVinesRtpNbrIfType_Type(Integer32):
    """Custom type wfVinesRtpNbrIfType based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("async1200", 8),
          ("async4800", 9),
          ("async56000", 11),
          ("async9600", 10),
          ("enet", 1),
          ("fddi", 31),
          ("hdlc1200", 4),
          ("hdlc4800", 5),
          ("hdlc56000", 7),
          ("hdlc9600", 6),
          ("t11088k", 28),
          ("t1128k", 17),
          ("t11344k", 29),
          ("t1192k", 18),
          ("t1256k", 19),
          ("t1320k", 20),
          ("t1384k", 21),
          ("t1448k", 22),
          ("t145k", 16),
          ("t1512k", 23),
          ("t1576k", 24),
          ("t1640k", 25),
          ("t1704k", 26),
          ("t1896k", 27),
          ("tr16k", 3),
          ("tr4k", 2),
          ("tunnel", 30),
          ("x251200", 12),
          ("x254800", 13),
          ("x2556000", 15),
          ("x259600", 14))
    )


_WfVinesRtpNbrIfType_Type.__name__ = "Integer32"
_WfVinesRtpNbrIfType_Object = MibTableColumn
wfVinesRtpNbrIfType = _WfVinesRtpNbrIfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 4),
    _WfVinesRtpNbrIfType_Type()
)
wfVinesRtpNbrIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrIfType.setStatus("mandatory")
_WfVinesRtpNbrRemAdr_Type = OctetString
_WfVinesRtpNbrRemAdr_Object = MibTableColumn
wfVinesRtpNbrRemAdr = _WfVinesRtpNbrRemAdr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 5),
    _WfVinesRtpNbrRemAdr_Type()
)
wfVinesRtpNbrRemAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrRemAdr.setStatus("mandatory")
_WfVinesRtpNbrLocAdr_Type = OctetString
_WfVinesRtpNbrLocAdr_Object = MibTableColumn
wfVinesRtpNbrLocAdr = _WfVinesRtpNbrLocAdr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 6),
    _WfVinesRtpNbrLocAdr_Type()
)
wfVinesRtpNbrLocAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrLocAdr.setStatus("mandatory")
_WfVinesRtpNbrLocSlot_Type = Integer32
_WfVinesRtpNbrLocSlot_Object = MibTableColumn
wfVinesRtpNbrLocSlot = _WfVinesRtpNbrLocSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 7),
    _WfVinesRtpNbrLocSlot_Type()
)
wfVinesRtpNbrLocSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrLocSlot.setStatus("mandatory")
_WfVinesRtpNbrLocLine_Type = Integer32
_WfVinesRtpNbrLocLine_Object = MibTableColumn
wfVinesRtpNbrLocLine = _WfVinesRtpNbrLocLine_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 8),
    _WfVinesRtpNbrLocLine_Type()
)
wfVinesRtpNbrLocLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrLocLine.setStatus("mandatory")
_WfVinesRtpNbrSvrName_Type = OctetString
_WfVinesRtpNbrSvrName_Object = MibTableColumn
wfVinesRtpNbrSvrName = _WfVinesRtpNbrSvrName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 9),
    _WfVinesRtpNbrSvrName_Type()
)
wfVinesRtpNbrSvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrSvrName.setStatus("mandatory")
_WfVinesRtpNbrCost_Type = Integer32
_WfVinesRtpNbrCost_Object = MibTableColumn
wfVinesRtpNbrCost = _WfVinesRtpNbrCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 10),
    _WfVinesRtpNbrCost_Type()
)
wfVinesRtpNbrCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrCost.setStatus("mandatory")


class _WfVinesSeqRtpNbrState_Type(Integer32):
    """Custom type wfVinesSeqRtpNbrState based on Integer32"""
    defaultValue = 4

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
        *(("chgrqst", 3),
          ("fullrqst", 2),
          ("init", 1),
          ("up", 4))
    )


_WfVinesSeqRtpNbrState_Type.__name__ = "Integer32"
_WfVinesSeqRtpNbrState_Object = MibTableColumn
wfVinesSeqRtpNbrState = _WfVinesSeqRtpNbrState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 11),
    _WfVinesSeqRtpNbrState_Type()
)
wfVinesSeqRtpNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesSeqRtpNbrState.setStatus("mandatory")
_WfVinesSeqRtpNbrSeqNumber_Type = Counter32
_WfVinesSeqRtpNbrSeqNumber_Object = MibTableColumn
wfVinesSeqRtpNbrSeqNumber = _WfVinesSeqRtpNbrSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 12),
    _WfVinesSeqRtpNbrSeqNumber_Type()
)
wfVinesSeqRtpNbrSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesSeqRtpNbrSeqNumber.setStatus("mandatory")


class _WfVinesRtpNbrRtType_Type(Integer32):
    """Custom type wfVinesRtpNbrRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("seq", 1),
          ("sequenced", 2))
    )


_WfVinesRtpNbrRtType_Type.__name__ = "Integer32"
_WfVinesRtpNbrRtType_Object = MibTableColumn
wfVinesRtpNbrRtType = _WfVinesRtpNbrRtType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 13),
    _WfVinesRtpNbrRtType_Type()
)
wfVinesRtpNbrRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrRtType.setStatus("mandatory")
_WfVinesRtpNbrNumPaths_Type = Counter32
_WfVinesRtpNbrNumPaths_Object = MibTableColumn
wfVinesRtpNbrNumPaths = _WfVinesRtpNbrNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 4, 1, 14),
    _WfVinesRtpNbrNumPaths_Type()
)
wfVinesRtpNbrNumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpNbrNumPaths.setStatus("mandatory")
_WfVinesRtpRt_ObjectIdentity = ObjectIdentity
wfVinesRtpRt = _WfVinesRtpRt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 5)
)
_WfVinesRtpRtNumber_Type = Integer32
_WfVinesRtpRtNumber_Object = MibScalar
wfVinesRtpRtNumber = _WfVinesRtpRtNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 5, 1),
    _WfVinesRtpRtNumber_Type()
)
wfVinesRtpRtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtNumber.setStatus("mandatory")
_WfVinesRtpRtTable_Object = MibTable
wfVinesRtpRtTable = _WfVinesRtpRtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6)
)
if mibBuilder.loadTexts:
    wfVinesRtpRtTable.setStatus("mandatory")
_WfVinesRtpRtEntry_Object = MibTableRow
wfVinesRtpRtEntry = _WfVinesRtpRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1)
)
wfVinesRtpRtEntry.setIndexNames(
    (0, "Wellfleet-VINES-MIB", "wfVinesRtpRtNetid"),
)
if mibBuilder.loadTexts:
    wfVinesRtpRtEntry.setStatus("mandatory")
_WfVinesRtpRtNetid_Type = Counter32
_WfVinesRtpRtNetid_Object = MibTableColumn
wfVinesRtpRtNetid = _WfVinesRtpRtNetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 1),
    _WfVinesRtpRtNetid_Type()
)
wfVinesRtpRtNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtNetid.setStatus("mandatory")
_WfVinesRtpRtMetric_Type = Integer32
_WfVinesRtpRtMetric_Object = MibTableColumn
wfVinesRtpRtMetric = _WfVinesRtpRtMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 2),
    _WfVinesRtpRtMetric_Type()
)
wfVinesRtpRtMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtMetric.setStatus("mandatory")
_WfVinesRtpRtIdle_Type = Integer32
_WfVinesRtpRtIdle_Object = MibTableColumn
wfVinesRtpRtIdle = _WfVinesRtpRtIdle_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 3),
    _WfVinesRtpRtIdle_Type()
)
wfVinesRtpRtIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtIdle.setStatus("mandatory")
_WfVinesRtpRtGateNetid_Type = Counter32
_WfVinesRtpRtGateNetid_Object = MibTableColumn
wfVinesRtpRtGateNetid = _WfVinesRtpRtGateNetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 4),
    _WfVinesRtpRtGateNetid_Type()
)
wfVinesRtpRtGateNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtGateNetid.setStatus("mandatory")
_WfVinesRtpRtSvrName_Type = OctetString
_WfVinesRtpRtSvrName_Object = MibTableColumn
wfVinesRtpRtSvrName = _WfVinesRtpRtSvrName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 5),
    _WfVinesRtpRtSvrName_Type()
)
wfVinesRtpRtSvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtSvrName.setStatus("mandatory")
_WfVinesRtpRtGateSvrName_Type = OctetString
_WfVinesRtpRtGateSvrName_Object = MibTableColumn
wfVinesRtpRtGateSvrName = _WfVinesRtpRtGateSvrName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 6),
    _WfVinesRtpRtGateSvrName_Type()
)
wfVinesRtpRtGateSvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtGateSvrName.setStatus("mandatory")
_WfVinesRtpRtLocSlot_Type = Integer32
_WfVinesRtpRtLocSlot_Object = MibTableColumn
wfVinesRtpRtLocSlot = _WfVinesRtpRtLocSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 7),
    _WfVinesRtpRtLocSlot_Type()
)
wfVinesRtpRtLocSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtLocSlot.setStatus("mandatory")
_WfVinesRtpRtLocLine_Type = Integer32
_WfVinesRtpRtLocLine_Object = MibTableColumn
wfVinesRtpRtLocLine = _WfVinesRtpRtLocLine_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 8),
    _WfVinesRtpRtLocLine_Type()
)
wfVinesRtpRtLocLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtLocLine.setStatus("mandatory")


class _WfVinesRtpRtIfType_Type(Integer32):
    """Custom type wfVinesRtpRtIfType based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("async1200", 8),
          ("async4800", 9),
          ("async56000", 11),
          ("async9600", 10),
          ("enet", 1),
          ("fddi", 31),
          ("hdlc1200", 4),
          ("hdlc4800", 5),
          ("hdlc56000", 7),
          ("hdlc9600", 6),
          ("t11088k", 28),
          ("t1128k", 17),
          ("t11344k", 29),
          ("t1192k", 18),
          ("t1256k", 19),
          ("t1320k", 20),
          ("t1384k", 21),
          ("t1448k", 22),
          ("t145k", 16),
          ("t1512k", 23),
          ("t1576k", 24),
          ("t1640k", 25),
          ("t1704k", 26),
          ("t1896k", 27),
          ("tr16k", 3),
          ("tr4k", 2),
          ("tunnel", 30),
          ("x251200", 12),
          ("x254800", 13),
          ("x2556000", 15),
          ("x259600", 14))
    )


_WfVinesRtpRtIfType_Type.__name__ = "Integer32"
_WfVinesRtpRtIfType_Object = MibTableColumn
wfVinesRtpRtIfType = _WfVinesRtpRtIfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 9),
    _WfVinesRtpRtIfType_Type()
)
wfVinesRtpRtIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtIfType.setStatus("mandatory")
_WfVinesRtpRtGateHwAddr_Type = OctetString
_WfVinesRtpRtGateHwAddr_Object = MibTableColumn
wfVinesRtpRtGateHwAddr = _WfVinesRtpRtGateHwAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 10),
    _WfVinesRtpRtGateHwAddr_Type()
)
wfVinesRtpRtGateHwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtGateHwAddr.setStatus("mandatory")


class _WfVinesRtpRtType_Type(Integer32):
    """Custom type wfVinesRtpRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("seq", 1),
          ("sequenced", 2))
    )


_WfVinesRtpRtType_Type.__name__ = "Integer32"
_WfVinesRtpRtType_Object = MibTableColumn
wfVinesRtpRtType = _WfVinesRtpRtType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 11),
    _WfVinesRtpRtType_Type()
)
wfVinesRtpRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtType.setStatus("mandatory")
_WfVinesRtpRtSeqNumber_Type = Counter32
_WfVinesRtpRtSeqNumber_Object = MibTableColumn
wfVinesRtpRtSeqNumber = _WfVinesRtpRtSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 12),
    _WfVinesRtpRtSeqNumber_Type()
)
wfVinesRtpRtSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtSeqNumber.setStatus("mandatory")
_WfVinesRtpRtTimeStamp_Type = Counter32
_WfVinesRtpRtTimeStamp_Object = MibTableColumn
wfVinesRtpRtTimeStamp = _WfVinesRtpRtTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 13),
    _WfVinesRtpRtTimeStamp_Type()
)
wfVinesRtpRtTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtTimeStamp.setStatus("mandatory")
_WfVinesRtpRtNumPaths_Type = Counter32
_WfVinesRtpRtNumPaths_Object = MibTableColumn
wfVinesRtpRtNumPaths = _WfVinesRtpRtNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 6, 1, 14),
    _WfVinesRtpRtNumPaths_Type()
)
wfVinesRtpRtNumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesRtpRtNumPaths.setStatus("mandatory")
_WfVinesIf_ObjectIdentity = ObjectIdentity
wfVinesIf = _WfVinesIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 7)
)
_WfVinesIfNumber_Type = Integer32
_WfVinesIfNumber_Object = MibScalar
wfVinesIfNumber = _WfVinesIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 7, 1),
    _WfVinesIfNumber_Type()
)
wfVinesIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfNumber.setStatus("mandatory")
_WfVinesIfTable_Object = MibTable
wfVinesIfTable = _WfVinesIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8)
)
if mibBuilder.loadTexts:
    wfVinesIfTable.setStatus("mandatory")
_WfVinesIfEntry_Object = MibTableRow
wfVinesIfEntry = _WfVinesIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1)
)
wfVinesIfEntry.setIndexNames(
    (0, "Wellfleet-VINES-MIB", "wfVinesIfCct"),
)
if mibBuilder.loadTexts:
    wfVinesIfEntry.setStatus("mandatory")


class _WfVinesIfDelete_Type(Integer32):
    """Custom type wfVinesIfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfVinesIfDelete_Type.__name__ = "Integer32"
_WfVinesIfDelete_Object = MibTableColumn
wfVinesIfDelete = _WfVinesIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 1),
    _WfVinesIfDelete_Type()
)
wfVinesIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfDelete.setStatus("mandatory")


class _WfVinesIfDisable_Type(Integer32):
    """Custom type wfVinesIfDisable based on Integer32"""
    defaultValue = 1

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


_WfVinesIfDisable_Type.__name__ = "Integer32"
_WfVinesIfDisable_Object = MibTableColumn
wfVinesIfDisable = _WfVinesIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 2),
    _WfVinesIfDisable_Type()
)
wfVinesIfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfDisable.setStatus("mandatory")


class _WfVinesIfState_Type(Integer32):
    """Custom type wfVinesIfState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfVinesIfState_Type.__name__ = "Integer32"
_WfVinesIfState_Object = MibTableColumn
wfVinesIfState = _WfVinesIfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 3),
    _WfVinesIfState_Type()
)
wfVinesIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfState.setStatus("mandatory")
_WfVinesIfSlot_Type = Integer32
_WfVinesIfSlot_Object = MibTableColumn
wfVinesIfSlot = _WfVinesIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 4),
    _WfVinesIfSlot_Type()
)
wfVinesIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfSlot.setStatus("mandatory")
_WfVinesIfLine_Type = Integer32
_WfVinesIfLine_Object = MibTableColumn
wfVinesIfLine = _WfVinesIfLine_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 5),
    _WfVinesIfLine_Type()
)
wfVinesIfLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfLine.setStatus("mandatory")
_WfVinesIfCct_Type = Integer32
_WfVinesIfCct_Object = MibTableColumn
wfVinesIfCct = _WfVinesIfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 6),
    _WfVinesIfCct_Type()
)
wfVinesIfCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfCct.setStatus("mandatory")
_WfVinesIfSession_Type = Integer32
_WfVinesIfSession_Object = MibTableColumn
wfVinesIfSession = _WfVinesIfSession_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 7),
    _WfVinesIfSession_Type()
)
wfVinesIfSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfSession.setStatus("mandatory")


class _WfVinesIfType_Type(Integer32):
    """Custom type wfVinesIfType based on Integer32"""
    defaultValue = 1

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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("async1200", 8),
          ("async4800", 9),
          ("async56000", 11),
          ("async9600", 10),
          ("enet", 1),
          ("fddi", 31),
          ("hdlc1200", 4),
          ("hdlc4800", 5),
          ("hdlc56000", 7),
          ("hdlc9600", 6),
          ("t11088k", 28),
          ("t1128k", 17),
          ("t11344k", 29),
          ("t1192k", 18),
          ("t1256k", 19),
          ("t1320k", 20),
          ("t1384k", 21),
          ("t1448k", 22),
          ("t145k", 16),
          ("t1512k", 23),
          ("t1576k", 24),
          ("t1640k", 25),
          ("t1704k", 26),
          ("t1896k", 27),
          ("tr16k", 3),
          ("tr4k", 2),
          ("tunnel", 30),
          ("x251200", 12),
          ("x254800", 13),
          ("x2556000", 15),
          ("x259600", 14))
    )


_WfVinesIfType_Type.__name__ = "Integer32"
_WfVinesIfType_Object = MibTableColumn
wfVinesIfType = _WfVinesIfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 8),
    _WfVinesIfType_Type()
)
wfVinesIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfType.setStatus("mandatory")
_WfVinesIfDescr_Type = OctetString
_WfVinesIfDescr_Object = MibTableColumn
wfVinesIfDescr = _WfVinesIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 9),
    _WfVinesIfDescr_Type()
)
wfVinesIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfDescr.setStatus("mandatory")
_WfVinesIfAdr_Type = OctetString
_WfVinesIfAdr_Object = MibTableColumn
wfVinesIfAdr = _WfVinesIfAdr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 10),
    _WfVinesIfAdr_Type()
)
wfVinesIfAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfAdr.setStatus("mandatory")


class _WfVinesIfDodIpDisable_Type(Integer32):
    """Custom type wfVinesIfDodIpDisable based on Integer32"""
    defaultValue = 2

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


_WfVinesIfDodIpDisable_Type.__name__ = "Integer32"
_WfVinesIfDodIpDisable_Object = MibTableColumn
wfVinesIfDodIpDisable = _WfVinesIfDodIpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 11),
    _WfVinesIfDodIpDisable_Type()
)
wfVinesIfDodIpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfDodIpDisable.setStatus("mandatory")


class _WfVinesIfArpDisable_Type(Integer32):
    """Custom type wfVinesIfArpDisable based on Integer32"""
    defaultValue = 2

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


_WfVinesIfArpDisable_Type.__name__ = "Integer32"
_WfVinesIfArpDisable_Object = MibTableColumn
wfVinesIfArpDisable = _WfVinesIfArpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 12),
    _WfVinesIfArpDisable_Type()
)
wfVinesIfArpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfArpDisable.setStatus("mandatory")


class _WfVinesIfTrEndStation_Type(Integer32):
    """Custom type wfVinesIfTrEndStation based on Integer32"""
    defaultValue = 2

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


_WfVinesIfTrEndStation_Type.__name__ = "Integer32"
_WfVinesIfTrEndStation_Object = MibTableColumn
wfVinesIfTrEndStation = _WfVinesIfTrEndStation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 13),
    _WfVinesIfTrEndStation_Type()
)
wfVinesIfTrEndStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfTrEndStation.setStatus("mandatory")
_WfVinesIfInPkts_Type = Counter32
_WfVinesIfInPkts_Object = MibTableColumn
wfVinesIfInPkts = _WfVinesIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 14),
    _WfVinesIfInPkts_Type()
)
wfVinesIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfInPkts.setStatus("mandatory")
_WfVinesIfInErrs_Type = Counter32
_WfVinesIfInErrs_Object = MibTableColumn
wfVinesIfInErrs = _WfVinesIfInErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 15),
    _WfVinesIfInErrs_Type()
)
wfVinesIfInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfInErrs.setStatus("mandatory")
_WfVinesIfOutPkts_Type = Counter32
_WfVinesIfOutPkts_Object = MibTableColumn
wfVinesIfOutPkts = _WfVinesIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 16),
    _WfVinesIfOutPkts_Type()
)
wfVinesIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfOutPkts.setStatus("mandatory")
_WfVinesIfOutErrs_Type = Counter32
_WfVinesIfOutErrs_Object = MibTableColumn
wfVinesIfOutErrs = _WfVinesIfOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 17),
    _WfVinesIfOutErrs_Type()
)
wfVinesIfOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfOutErrs.setStatus("mandatory")
_WfVinesIfInMsgs_Type = Counter32
_WfVinesIfInMsgs_Object = MibTableColumn
wfVinesIfInMsgs = _WfVinesIfInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 18),
    _WfVinesIfInMsgs_Type()
)
wfVinesIfInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfInMsgs.setStatus("mandatory")


class _WfVinesIfMux_Type(Integer32):
    """Custom type wfVinesIfMux based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enet", 1),
          ("snap", 2))
    )


_WfVinesIfMux_Type.__name__ = "Integer32"
_WfVinesIfMux_Object = MibTableColumn
wfVinesIfMux = _WfVinesIfMux_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 19),
    _WfVinesIfMux_Type()
)
wfVinesIfMux.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfMux.setStatus("mandatory")
_WfVinesIfFwdDrops_Type = Counter32
_WfVinesIfFwdDrops_Object = MibTableColumn
wfVinesIfFwdDrops = _WfVinesIfFwdDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 20),
    _WfVinesIfFwdDrops_Type()
)
wfVinesIfFwdDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfFwdDrops.setStatus("mandatory")
_WfVinesIfZeroHopDrops_Type = Counter32
_WfVinesIfZeroHopDrops_Object = MibTableColumn
wfVinesIfZeroHopDrops = _WfVinesIfZeroHopDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 21),
    _WfVinesIfZeroHopDrops_Type()
)
wfVinesIfZeroHopDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfZeroHopDrops.setStatus("mandatory")
_WfVinesIfIcpInErrorNotifs_Type = Counter32
_WfVinesIfIcpInErrorNotifs_Object = MibTableColumn
wfVinesIfIcpInErrorNotifs = _WfVinesIfIcpInErrorNotifs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 22),
    _WfVinesIfIcpInErrorNotifs_Type()
)
wfVinesIfIcpInErrorNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfIcpInErrorNotifs.setStatus("mandatory")
_WfVinesIfIcpInMetricNotifs_Type = Counter32
_WfVinesIfIcpInMetricNotifs_Object = MibTableColumn
wfVinesIfIcpInMetricNotifs = _WfVinesIfIcpInMetricNotifs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 23),
    _WfVinesIfIcpInMetricNotifs_Type()
)
wfVinesIfIcpInMetricNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfIcpInMetricNotifs.setStatus("mandatory")
_WfVinesIfIcpInErrors_Type = Counter32
_WfVinesIfIcpInErrors_Object = MibTableColumn
wfVinesIfIcpInErrors = _WfVinesIfIcpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 24),
    _WfVinesIfIcpInErrors_Type()
)
wfVinesIfIcpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfIcpInErrors.setStatus("mandatory")
_WfVinesIfIcpOutErrorNotifs_Type = Counter32
_WfVinesIfIcpOutErrorNotifs_Object = MibTableColumn
wfVinesIfIcpOutErrorNotifs = _WfVinesIfIcpOutErrorNotifs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 25),
    _WfVinesIfIcpOutErrorNotifs_Type()
)
wfVinesIfIcpOutErrorNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfIcpOutErrorNotifs.setStatus("mandatory")
_WfVinesIfIcpOutMetricNotifs_Type = Counter32
_WfVinesIfIcpOutMetricNotifs_Object = MibTableColumn
wfVinesIfIcpOutMetricNotifs = _WfVinesIfIcpOutMetricNotifs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 26),
    _WfVinesIfIcpOutMetricNotifs_Type()
)
wfVinesIfIcpOutMetricNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfIcpOutMetricNotifs.setStatus("mandatory")
_WfVinesIfArpInQueries_Type = Counter32
_WfVinesIfArpInQueries_Object = MibTableColumn
wfVinesIfArpInQueries = _WfVinesIfArpInQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 27),
    _WfVinesIfArpInQueries_Type()
)
wfVinesIfArpInQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfArpInQueries.setStatus("mandatory")
_WfVinesIfArpInAssgReqs_Type = Counter32
_WfVinesIfArpInAssgReqs_Object = MibTableColumn
wfVinesIfArpInAssgReqs = _WfVinesIfArpInAssgReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 28),
    _WfVinesIfArpInAssgReqs_Type()
)
wfVinesIfArpInAssgReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfArpInAssgReqs.setStatus("mandatory")
_WfVinesIfArpInErrors_Type = Counter32
_WfVinesIfArpInErrors_Object = MibTableColumn
wfVinesIfArpInErrors = _WfVinesIfArpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 29),
    _WfVinesIfArpInErrors_Type()
)
wfVinesIfArpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfArpInErrors.setStatus("mandatory")
_WfVinesIfArpOutServRsps_Type = Counter32
_WfVinesIfArpOutServRsps_Object = MibTableColumn
wfVinesIfArpOutServRsps = _WfVinesIfArpOutServRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 30),
    _WfVinesIfArpOutServRsps_Type()
)
wfVinesIfArpOutServRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfArpOutServRsps.setStatus("mandatory")
_WfVinesIfArpOutAssgRsps_Type = Counter32
_WfVinesIfArpOutAssgRsps_Object = MibTableColumn
wfVinesIfArpOutAssgRsps = _WfVinesIfArpOutAssgRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 31),
    _WfVinesIfArpOutAssgRsps_Type()
)
wfVinesIfArpOutAssgRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfArpOutAssgRsps.setStatus("mandatory")
_WfVinesIfInRedirects_Type = Counter32
_WfVinesIfInRedirects_Object = MibTableColumn
wfVinesIfInRedirects = _WfVinesIfInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 32),
    _WfVinesIfInRedirects_Type()
)
wfVinesIfInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfInRedirects.setStatus("mandatory")
_WfVinesIfOutRedirects_Type = Counter32
_WfVinesIfOutRedirects_Object = MibTableColumn
wfVinesIfOutRedirects = _WfVinesIfOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 33),
    _WfVinesIfOutRedirects_Type()
)
wfVinesIfOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfOutRedirects.setStatus("mandatory")
_WfVinesIfEchoInPkts_Type = Counter32
_WfVinesIfEchoInPkts_Object = MibTableColumn
wfVinesIfEchoInPkts = _WfVinesIfEchoInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 34),
    _WfVinesIfEchoInPkts_Type()
)
wfVinesIfEchoInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfEchoInPkts.setStatus("mandatory")
_WfVinesIfEchoOutPkts_Type = Counter32
_WfVinesIfEchoOutPkts_Object = MibTableColumn
wfVinesIfEchoOutPkts = _WfVinesIfEchoOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 35),
    _WfVinesIfEchoOutPkts_Type()
)
wfVinesIfEchoOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfEchoOutPkts.setStatus("mandatory")
_WfVinesIfReassFails_Type = Counter32
_WfVinesIfReassFails_Object = MibTableColumn
wfVinesIfReassFails = _WfVinesIfReassFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 36),
    _WfVinesIfReassFails_Type()
)
wfVinesIfReassFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfReassFails.setStatus("mandatory")


class _WfVinesIfRemClientPrivDisable_Type(Integer32):
    """Custom type wfVinesIfRemClientPrivDisable based on Integer32"""
    defaultValue = 2

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


_WfVinesIfRemClientPrivDisable_Type.__name__ = "Integer32"
_WfVinesIfRemClientPrivDisable_Object = MibTableColumn
wfVinesIfRemClientPrivDisable = _WfVinesIfRemClientPrivDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 37),
    _WfVinesIfRemClientPrivDisable_Type()
)
wfVinesIfRemClientPrivDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfRemClientPrivDisable.setStatus("mandatory")


class _WfVinesIfSplitHorizonDisable_Type(Integer32):
    """Custom type wfVinesIfSplitHorizonDisable based on Integer32"""
    defaultValue = 2

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


_WfVinesIfSplitHorizonDisable_Type.__name__ = "Integer32"
_WfVinesIfSplitHorizonDisable_Object = MibTableColumn
wfVinesIfSplitHorizonDisable = _WfVinesIfSplitHorizonDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 38),
    _WfVinesIfSplitHorizonDisable_Type()
)
wfVinesIfSplitHorizonDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfSplitHorizonDisable.setStatus("mandatory")
_WfVinesIfCost_Type = Integer32
_WfVinesIfCost_Object = MibTableColumn
wfVinesIfCost = _WfVinesIfCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 39),
    _WfVinesIfCost_Type()
)
wfVinesIfCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfCost.setStatus("obsolete")
_WfVinesIfSyncPortNumber_Type = Integer32
_WfVinesIfSyncPortNumber_Object = MibTableColumn
wfVinesIfSyncPortNumber = _WfVinesIfSyncPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 40),
    _WfVinesIfSyncPortNumber_Type()
)
wfVinesIfSyncPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfSyncPortNumber.setStatus("obsolete")
_WfVinesIfInLackRescError_Type = Counter32
_WfVinesIfInLackRescError_Object = MibTableColumn
wfVinesIfInLackRescError = _WfVinesIfInLackRescError_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 41),
    _WfVinesIfInLackRescError_Type()
)
wfVinesIfInLackRescError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfInLackRescError.setStatus("mandatory")
_WfVinesIfOutLackRescError_Type = Counter32
_WfVinesIfOutLackRescError_Object = MibTableColumn
wfVinesIfOutLackRescError = _WfVinesIfOutLackRescError_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 42),
    _WfVinesIfOutLackRescError_Type()
)
wfVinesIfOutLackRescError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfOutLackRescError.setStatus("mandatory")
_WfVinesIfRtpRecv_Type = Counter32
_WfVinesIfRtpRecv_Object = MibTableColumn
wfVinesIfRtpRecv = _WfVinesIfRtpRecv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 43),
    _WfVinesIfRtpRecv_Type()
)
wfVinesIfRtpRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfRtpRecv.setStatus("mandatory")
_WfVinesIfRtpSent_Type = Counter32
_WfVinesIfRtpSent_Object = MibTableColumn
wfVinesIfRtpSent = _WfVinesIfRtpSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 44),
    _WfVinesIfRtpSent_Type()
)
wfVinesIfRtpSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfRtpSent.setStatus("mandatory")
_WfVinesIfSMDSGroupAddress_Type = OctetString
_WfVinesIfSMDSGroupAddress_Object = MibTableColumn
wfVinesIfSMDSGroupAddress = _WfVinesIfSMDSGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 45),
    _WfVinesIfSMDSGroupAddress_Type()
)
wfVinesIfSMDSGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfSMDSGroupAddress.setStatus("mandatory")
_WfVinesIfFRBcastDlci_Type = OctetString
_WfVinesIfFRBcastDlci_Object = MibTableColumn
wfVinesIfFRBcastDlci = _WfVinesIfFRBcastDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 46),
    _WfVinesIfFRBcastDlci_Type()
)
wfVinesIfFRBcastDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfFRBcastDlci.setStatus("mandatory")
_WfVinesIfCfgAdr_Type = OctetString
_WfVinesIfCfgAdr_Object = MibTableColumn
wfVinesIfCfgAdr = _WfVinesIfCfgAdr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 47),
    _WfVinesIfCfgAdr_Type()
)
wfVinesIfCfgAdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfCfgAdr.setStatus("mandatory")
_WfVinesIfNumRoutes_Type = Counter32
_WfVinesIfNumRoutes_Object = MibTableColumn
wfVinesIfNumRoutes = _WfVinesIfNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 48),
    _WfVinesIfNumRoutes_Type()
)
wfVinesIfNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfNumRoutes.setStatus("obsolete")
_WfVinesIfCfgCost_Type = Integer32
_WfVinesIfCfgCost_Object = MibTableColumn
wfVinesIfCfgCost = _WfVinesIfCfgCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 49),
    _WfVinesIfCfgCost_Type()
)
wfVinesIfCfgCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfCfgCost.setStatus("mandatory")
_WfVinesIfCostUsed_Type = Integer32
_WfVinesIfCostUsed_Object = MibTableColumn
wfVinesIfCostUsed = _WfVinesIfCostUsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 50),
    _WfVinesIfCostUsed_Type()
)
wfVinesIfCostUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfCostUsed.setStatus("mandatory")


class _WfVinesIfFrpEnable_Type(Integer32):
    """Custom type wfVinesIfFrpEnable based on Integer32"""
    defaultValue = 1

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


_WfVinesIfFrpEnable_Type.__name__ = "Integer32"
_WfVinesIfFrpEnable_Object = MibTableColumn
wfVinesIfFrpEnable = _WfVinesIfFrpEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 51),
    _WfVinesIfFrpEnable_Type()
)
wfVinesIfFrpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfFrpEnable.setStatus("mandatory")
_WfVinesIfSeqArpInQueries_Type = Counter32
_WfVinesIfSeqArpInQueries_Object = MibTableColumn
wfVinesIfSeqArpInQueries = _WfVinesIfSeqArpInQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 52),
    _WfVinesIfSeqArpInQueries_Type()
)
wfVinesIfSeqArpInQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfSeqArpInQueries.setStatus("mandatory")
_WfVinesIfSeqArpInAssgReqs_Type = Counter32
_WfVinesIfSeqArpInAssgReqs_Object = MibTableColumn
wfVinesIfSeqArpInAssgReqs = _WfVinesIfSeqArpInAssgReqs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 53),
    _WfVinesIfSeqArpInAssgReqs_Type()
)
wfVinesIfSeqArpInAssgReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfSeqArpInAssgReqs.setStatus("mandatory")
_WfVinesIfSeqArpInErrors_Type = Counter32
_WfVinesIfSeqArpInErrors_Object = MibTableColumn
wfVinesIfSeqArpInErrors = _WfVinesIfSeqArpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 54),
    _WfVinesIfSeqArpInErrors_Type()
)
wfVinesIfSeqArpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfSeqArpInErrors.setStatus("mandatory")
_WfVinesIfSeqArpOutServRsps_Type = Counter32
_WfVinesIfSeqArpOutServRsps_Object = MibTableColumn
wfVinesIfSeqArpOutServRsps = _WfVinesIfSeqArpOutServRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 55),
    _WfVinesIfSeqArpOutServRsps_Type()
)
wfVinesIfSeqArpOutServRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfSeqArpOutServRsps.setStatus("mandatory")
_WfVinesIfSeqArpOutAssgRsps_Type = Counter32
_WfVinesIfSeqArpOutAssgRsps_Object = MibTableColumn
wfVinesIfSeqArpOutAssgRsps = _WfVinesIfSeqArpOutAssgRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 56),
    _WfVinesIfSeqArpOutAssgRsps_Type()
)
wfVinesIfSeqArpOutAssgRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfSeqArpOutAssgRsps.setStatus("mandatory")
_WfVinesIfInSeqRedirects_Type = Counter32
_WfVinesIfInSeqRedirects_Object = MibTableColumn
wfVinesIfInSeqRedirects = _WfVinesIfInSeqRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 57),
    _WfVinesIfInSeqRedirects_Type()
)
wfVinesIfInSeqRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfInSeqRedirects.setStatus("mandatory")
_WfVinesIfOutSeqRedirects_Type = Counter32
_WfVinesIfOutSeqRedirects_Object = MibTableColumn
wfVinesIfOutSeqRedirects = _WfVinesIfOutSeqRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 58),
    _WfVinesIfOutSeqRedirects_Type()
)
wfVinesIfOutSeqRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfOutSeqRedirects.setStatus("mandatory")
_WfVinesIfSeqRtpRecv_Type = Counter32
_WfVinesIfSeqRtpRecv_Object = MibTableColumn
wfVinesIfSeqRtpRecv = _WfVinesIfSeqRtpRecv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 59),
    _WfVinesIfSeqRtpRecv_Type()
)
wfVinesIfSeqRtpRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfSeqRtpRecv.setStatus("mandatory")
_WfVinesIfSeqRtpSent_Type = Counter32
_WfVinesIfSeqRtpSent_Object = MibTableColumn
wfVinesIfSeqRtpSent = _WfVinesIfSeqRtpSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 60),
    _WfVinesIfSeqRtpSent_Type()
)
wfVinesIfSeqRtpSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfSeqRtpSent.setStatus("mandatory")


class _WfVinesIfRtpGenerationDisable_Type(Integer32):
    """Custom type wfVinesIfRtpGenerationDisable based on Integer32"""
    defaultValue = 1

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


_WfVinesIfRtpGenerationDisable_Type.__name__ = "Integer32"
_WfVinesIfRtpGenerationDisable_Object = MibTableColumn
wfVinesIfRtpGenerationDisable = _WfVinesIfRtpGenerationDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 61),
    _WfVinesIfRtpGenerationDisable_Type()
)
wfVinesIfRtpGenerationDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfRtpGenerationDisable.setStatus("mandatory")


class _WfVinesIfInverseArpEnable_Type(Integer32):
    """Custom type wfVinesIfInverseArpEnable based on Integer32"""
    defaultValue = 2

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


_WfVinesIfInverseArpEnable_Type.__name__ = "Integer32"
_WfVinesIfInverseArpEnable_Object = MibTableColumn
wfVinesIfInverseArpEnable = _WfVinesIfInverseArpEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 62),
    _WfVinesIfInverseArpEnable_Type()
)
wfVinesIfInverseArpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfInverseArpEnable.setStatus("mandatory")


class _WfVinesIfSTalkSplitHorizon_Type(Integer32):
    """Custom type wfVinesIfSTalkSplitHorizon based on Integer32"""
    defaultValue = 1

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


_WfVinesIfSTalkSplitHorizon_Type.__name__ = "Integer32"
_WfVinesIfSTalkSplitHorizon_Object = MibTableColumn
wfVinesIfSTalkSplitHorizon = _WfVinesIfSTalkSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 63),
    _WfVinesIfSTalkSplitHorizon_Type()
)
wfVinesIfSTalkSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfSTalkSplitHorizon.setStatus("mandatory")


class _WfVinesIfPermWanNbr_Type(Integer32):
    """Custom type wfVinesIfPermWanNbr based on Integer32"""
    defaultValue = 2

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


_WfVinesIfPermWanNbr_Type.__name__ = "Integer32"
_WfVinesIfPermWanNbr_Object = MibTableColumn
wfVinesIfPermWanNbr = _WfVinesIfPermWanNbr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 64),
    _WfVinesIfPermWanNbr_Type()
)
wfVinesIfPermWanNbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfPermWanNbr.setStatus("mandatory")
_WfVinesIfNumFwdEntries_Type = Counter32
_WfVinesIfNumFwdEntries_Object = MibTableColumn
wfVinesIfNumFwdEntries = _WfVinesIfNumFwdEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 65),
    _WfVinesIfNumFwdEntries_Type()
)
wfVinesIfNumFwdEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfNumFwdEntries.setStatus("mandatory")
_WfVinesIfNumNonSeqNbrs_Type = Counter32
_WfVinesIfNumNonSeqNbrs_Object = MibTableColumn
wfVinesIfNumNonSeqNbrs = _WfVinesIfNumNonSeqNbrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 66),
    _WfVinesIfNumNonSeqNbrs_Type()
)
wfVinesIfNumNonSeqNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfNumNonSeqNbrs.setStatus("mandatory")
_WfVinesIfNumSeqNbrs_Type = Counter32
_WfVinesIfNumSeqNbrs_Object = MibTableColumn
wfVinesIfNumSeqNbrs = _WfVinesIfNumSeqNbrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 67),
    _WfVinesIfNumSeqNbrs_Type()
)
wfVinesIfNumSeqNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfNumSeqNbrs.setStatus("mandatory")


class _WfVinesIfRedirectEnable_Type(Integer32):
    """Custom type wfVinesIfRedirectEnable based on Integer32"""
    defaultValue = 1

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


_WfVinesIfRedirectEnable_Type.__name__ = "Integer32"
_WfVinesIfRedirectEnable_Object = MibTableColumn
wfVinesIfRedirectEnable = _WfVinesIfRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 8, 1, 68),
    _WfVinesIfRedirectEnable_Type()
)
wfVinesIfRedirectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesIfRedirectEnable.setStatus("mandatory")
_WfVinesIfX25VC_ObjectIdentity = ObjectIdentity
wfVinesIfX25VC = _WfVinesIfX25VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 9)
)
_WfVinesIfX25VCNumber_Type = Integer32
_WfVinesIfX25VCNumber_Object = MibScalar
wfVinesIfX25VCNumber = _WfVinesIfX25VCNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 9, 1),
    _WfVinesIfX25VCNumber_Type()
)
wfVinesIfX25VCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCNumber.setStatus("mandatory")
_WfVinesIfX25VCTable_Object = MibTable
wfVinesIfX25VCTable = _WfVinesIfX25VCTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10)
)
if mibBuilder.loadTexts:
    wfVinesIfX25VCTable.setStatus("mandatory")
_WfVinesIfX25VCEntry_Object = MibTableRow
wfVinesIfX25VCEntry = _WfVinesIfX25VCEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1)
)
wfVinesIfX25VCEntry.setIndexNames(
    (0, "Wellfleet-VINES-MIB", "wfVinesIfX25VCCct"),
)
if mibBuilder.loadTexts:
    wfVinesIfX25VCEntry.setStatus("mandatory")
_WfVinesIfX25VCSlot_Type = Integer32
_WfVinesIfX25VCSlot_Object = MibTableColumn
wfVinesIfX25VCSlot = _WfVinesIfX25VCSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 1),
    _WfVinesIfX25VCSlot_Type()
)
wfVinesIfX25VCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCSlot.setStatus("mandatory")
_WfVinesIfX25VCLine_Type = Integer32
_WfVinesIfX25VCLine_Object = MibTableColumn
wfVinesIfX25VCLine = _WfVinesIfX25VCLine_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 2),
    _WfVinesIfX25VCLine_Type()
)
wfVinesIfX25VCLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCLine.setStatus("mandatory")
_WfVinesIfX25VCCct_Type = Integer32
_WfVinesIfX25VCCct_Object = MibTableColumn
wfVinesIfX25VCCct = _WfVinesIfX25VCCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 3),
    _WfVinesIfX25VCCct_Type()
)
wfVinesIfX25VCCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCCct.setStatus("mandatory")
_WfVinesIfX25VCSession_Type = Integer32
_WfVinesIfX25VCSession_Object = MibTableColumn
wfVinesIfX25VCSession = _WfVinesIfX25VCSession_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 4),
    _WfVinesIfX25VCSession_Type()
)
wfVinesIfX25VCSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCSession.setStatus("mandatory")
_WfVinesIfX25VCTotIn_Type = Counter32
_WfVinesIfX25VCTotIn_Object = MibTableColumn
wfVinesIfX25VCTotIn = _WfVinesIfX25VCTotIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 5),
    _WfVinesIfX25VCTotIn_Type()
)
wfVinesIfX25VCTotIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCTotIn.setStatus("mandatory")
_WfVinesIfX25VCTotOut_Type = Counter32
_WfVinesIfX25VCTotOut_Object = MibTableColumn
wfVinesIfX25VCTotOut = _WfVinesIfX25VCTotOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 6),
    _WfVinesIfX25VCTotOut_Type()
)
wfVinesIfX25VCTotOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCTotOut.setStatus("mandatory")
_WfVinesIfX25VCInErrs_Type = Counter32
_WfVinesIfX25VCInErrs_Object = MibTableColumn
wfVinesIfX25VCInErrs = _WfVinesIfX25VCInErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 7),
    _WfVinesIfX25VCInErrs_Type()
)
wfVinesIfX25VCInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCInErrs.setStatus("mandatory")
_WfVinesIfX25VCOutErrs_Type = Counter32
_WfVinesIfX25VCOutErrs_Object = MibTableColumn
wfVinesIfX25VCOutErrs = _WfVinesIfX25VCOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 8),
    _WfVinesIfX25VCOutErrs_Type()
)
wfVinesIfX25VCOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCOutErrs.setStatus("mandatory")
_WfVinesIfX25VCPktsOut_Type = Counter32
_WfVinesIfX25VCPktsOut_Object = MibTableColumn
wfVinesIfX25VCPktsOut = _WfVinesIfX25VCPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 9),
    _WfVinesIfX25VCPktsOut_Type()
)
wfVinesIfX25VCPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCPktsOut.setStatus("mandatory")
_WfVinesIfX25VCPktsAwaitAck_Type = Integer32
_WfVinesIfX25VCPktsAwaitAck_Object = MibTableColumn
wfVinesIfX25VCPktsAwaitAck = _WfVinesIfX25VCPktsAwaitAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 10),
    _WfVinesIfX25VCPktsAwaitAck_Type()
)
wfVinesIfX25VCPktsAwaitAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCPktsAwaitAck.setStatus("mandatory")
_WfVinesIfX25VCBytesOut_Type = Counter32
_WfVinesIfX25VCBytesOut_Object = MibTableColumn
wfVinesIfX25VCBytesOut = _WfVinesIfX25VCBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 11),
    _WfVinesIfX25VCBytesOut_Type()
)
wfVinesIfX25VCBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCBytesOut.setStatus("mandatory")
_WfVinesIfX25VCBytesAwaitAck_Type = Integer32
_WfVinesIfX25VCBytesAwaitAck_Object = MibTableColumn
wfVinesIfX25VCBytesAwaitAck = _WfVinesIfX25VCBytesAwaitAck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 12),
    _WfVinesIfX25VCBytesAwaitAck_Type()
)
wfVinesIfX25VCBytesAwaitAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCBytesAwaitAck.setStatus("mandatory")
_WfVinesIfX25VCPktsIn_Type = Counter32
_WfVinesIfX25VCPktsIn_Object = MibTableColumn
wfVinesIfX25VCPktsIn = _WfVinesIfX25VCPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 13),
    _WfVinesIfX25VCPktsIn_Type()
)
wfVinesIfX25VCPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCPktsIn.setStatus("mandatory")
_WfVinesIfX25VCBytesIn_Type = Counter32
_WfVinesIfX25VCBytesIn_Object = MibTableColumn
wfVinesIfX25VCBytesIn = _WfVinesIfX25VCBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 14),
    _WfVinesIfX25VCBytesIn_Type()
)
wfVinesIfX25VCBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCBytesIn.setStatus("mandatory")
_WfVinesIfX25VCResetsIn_Type = Counter32
_WfVinesIfX25VCResetsIn_Object = MibTableColumn
wfVinesIfX25VCResetsIn = _WfVinesIfX25VCResetsIn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 15),
    _WfVinesIfX25VCResetsIn_Type()
)
wfVinesIfX25VCResetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCResetsIn.setStatus("mandatory")
_WfVinesIfX25VCResetsOut_Type = Counter32
_WfVinesIfX25VCResetsOut_Object = MibTableColumn
wfVinesIfX25VCResetsOut = _WfVinesIfX25VCResetsOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 10, 1, 16),
    _WfVinesIfX25VCResetsOut_Type()
)
wfVinesIfX25VCResetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesIfX25VCResetsOut.setStatus("mandatory")
_WfVinesTrafficFilterTable_Object = MibTable
wfVinesTrafficFilterTable = _WfVinesTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11)
)
if mibBuilder.loadTexts:
    wfVinesTrafficFilterTable.setStatus("mandatory")
_WfVinesTrafficFilterEntry_Object = MibTableRow
wfVinesTrafficFilterEntry = _WfVinesTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1)
)
wfVinesTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-VINES-MIB", "wfVinesTrafficFilterCircuit"),
    (0, "Wellfleet-VINES-MIB", "wfVinesTrafficFilterRuleNumber"),
    (0, "Wellfleet-VINES-MIB", "wfVinesTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfVinesTrafficFilterEntry.setStatus("mandatory")


class _WfVinesTrafficFilterCreate_Type(Integer32):
    """Custom type wfVinesTrafficFilterCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfVinesTrafficFilterCreate_Type.__name__ = "Integer32"
_WfVinesTrafficFilterCreate_Object = MibTableColumn
wfVinesTrafficFilterCreate = _WfVinesTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 1),
    _WfVinesTrafficFilterCreate_Type()
)
wfVinesTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterCreate.setStatus("mandatory")


class _WfVinesTrafficFilterEnable_Type(Integer32):
    """Custom type wfVinesTrafficFilterEnable based on Integer32"""
    defaultValue = 1

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


_WfVinesTrafficFilterEnable_Type.__name__ = "Integer32"
_WfVinesTrafficFilterEnable_Object = MibTableColumn
wfVinesTrafficFilterEnable = _WfVinesTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 2),
    _WfVinesTrafficFilterEnable_Type()
)
wfVinesTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterEnable.setStatus("mandatory")


class _WfVinesTrafficFilterStatus_Type(Integer32):
    """Custom type wfVinesTrafficFilterStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfVinesTrafficFilterStatus_Type.__name__ = "Integer32"
_WfVinesTrafficFilterStatus_Object = MibTableColumn
wfVinesTrafficFilterStatus = _WfVinesTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 3),
    _WfVinesTrafficFilterStatus_Type()
)
wfVinesTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterStatus.setStatus("mandatory")
_WfVinesTrafficFilterCounter_Type = Counter32
_WfVinesTrafficFilterCounter_Object = MibTableColumn
wfVinesTrafficFilterCounter = _WfVinesTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 4),
    _WfVinesTrafficFilterCounter_Type()
)
wfVinesTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterCounter.setStatus("mandatory")
_WfVinesTrafficFilterDefinition_Type = OctetString
_WfVinesTrafficFilterDefinition_Object = MibTableColumn
wfVinesTrafficFilterDefinition = _WfVinesTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 5),
    _WfVinesTrafficFilterDefinition_Type()
)
wfVinesTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterDefinition.setStatus("mandatory")
_WfVinesTrafficFilterReserved_Type = Integer32
_WfVinesTrafficFilterReserved_Object = MibTableColumn
wfVinesTrafficFilterReserved = _WfVinesTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 6),
    _WfVinesTrafficFilterReserved_Type()
)
wfVinesTrafficFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterReserved.setStatus("mandatory")
_WfVinesTrafficFilterCircuit_Type = Integer32
_WfVinesTrafficFilterCircuit_Object = MibTableColumn
wfVinesTrafficFilterCircuit = _WfVinesTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 7),
    _WfVinesTrafficFilterCircuit_Type()
)
wfVinesTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterCircuit.setStatus("mandatory")
_WfVinesTrafficFilterRuleNumber_Type = Integer32
_WfVinesTrafficFilterRuleNumber_Object = MibTableColumn
wfVinesTrafficFilterRuleNumber = _WfVinesTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 8),
    _WfVinesTrafficFilterRuleNumber_Type()
)
wfVinesTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterRuleNumber.setStatus("mandatory")
_WfVinesTrafficFilterFragment_Type = Integer32
_WfVinesTrafficFilterFragment_Object = MibTableColumn
wfVinesTrafficFilterFragment = _WfVinesTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 9),
    _WfVinesTrafficFilterFragment_Type()
)
wfVinesTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterFragment.setStatus("mandatory")
_WfVinesTrafficFilterName_Type = DisplayString
_WfVinesTrafficFilterName_Object = MibTableColumn
wfVinesTrafficFilterName = _WfVinesTrafficFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 11, 1, 10),
    _WfVinesTrafficFilterName_Type()
)
wfVinesTrafficFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesTrafficFilterName.setStatus("mandatory")
_WfVinesNameTable_Object = MibTable
wfVinesNameTable = _WfVinesNameTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12)
)
if mibBuilder.loadTexts:
    wfVinesNameTable.setStatus("mandatory")
_WfVinesNameEntry_Object = MibTableRow
wfVinesNameEntry = _WfVinesNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12, 1)
)
wfVinesNameEntry.setIndexNames(
    (0, "Wellfleet-VINES-MIB", "wfVinesNameNetid"),
)
if mibBuilder.loadTexts:
    wfVinesNameEntry.setStatus("mandatory")


class _WfVinesNameDelete_Type(Integer32):
    """Custom type wfVinesNameDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfVinesNameDelete_Type.__name__ = "Integer32"
_WfVinesNameDelete_Object = MibTableColumn
wfVinesNameDelete = _WfVinesNameDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12, 1, 1),
    _WfVinesNameDelete_Type()
)
wfVinesNameDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesNameDelete.setStatus("mandatory")


class _WfVinesNameDisable_Type(Integer32):
    """Custom type wfVinesNameDisable based on Integer32"""
    defaultValue = 1

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


_WfVinesNameDisable_Type.__name__ = "Integer32"
_WfVinesNameDisable_Object = MibTableColumn
wfVinesNameDisable = _WfVinesNameDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12, 1, 2),
    _WfVinesNameDisable_Type()
)
wfVinesNameDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesNameDisable.setStatus("mandatory")
_WfVinesNameNetid_Type = Counter32
_WfVinesNameNetid_Object = MibTableColumn
wfVinesNameNetid = _WfVinesNameNetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12, 1, 3),
    _WfVinesNameNetid_Type()
)
wfVinesNameNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesNameNetid.setStatus("mandatory")
_WfVinesNameHost_Type = DisplayString
_WfVinesNameHost_Object = MibTableColumn
wfVinesNameHost = _WfVinesNameHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12, 1, 4),
    _WfVinesNameHost_Type()
)
wfVinesNameHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesNameHost.setStatus("mandatory")
_WfVinesNameSubNetid_Type = Integer32
_WfVinesNameSubNetid_Object = MibTableColumn
wfVinesNameSubNetid = _WfVinesNameSubNetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 12, 1, 5),
    _WfVinesNameSubNetid_Type()
)
wfVinesNameSubNetid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesNameSubNetid.setStatus("mandatory")
_WfVinesArp_ObjectIdentity = ObjectIdentity
wfVinesArp = _WfVinesArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13)
)


class _WfVinesArpDelete_Type(Integer32):
    """Custom type wfVinesArpDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfVinesArpDelete_Type.__name__ = "Integer32"
_WfVinesArpDelete_Object = MibScalar
wfVinesArpDelete = _WfVinesArpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13, 1),
    _WfVinesArpDelete_Type()
)
wfVinesArpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesArpDelete.setStatus("mandatory")


class _WfVinesArpDisable_Type(Integer32):
    """Custom type wfVinesArpDisable based on Integer32"""
    defaultValue = 1

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


_WfVinesArpDisable_Type.__name__ = "Integer32"
_WfVinesArpDisable_Object = MibScalar
wfVinesArpDisable = _WfVinesArpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13, 2),
    _WfVinesArpDisable_Type()
)
wfVinesArpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesArpDisable.setStatus("mandatory")


class _WfVinesArpState_Type(Integer32):
    """Custom type wfVinesArpState based on Integer32"""
    defaultValue = 2

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


_WfVinesArpState_Type.__name__ = "Integer32"
_WfVinesArpState_Object = MibScalar
wfVinesArpState = _WfVinesArpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13, 3),
    _WfVinesArpState_Type()
)
wfVinesArpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesArpState.setStatus("mandatory")
_WfVinesArpSubnetid_Type = Integer32
_WfVinesArpSubnetid_Object = MibScalar
wfVinesArpSubnetid = _WfVinesArpSubnetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13, 4),
    _WfVinesArpSubnetid_Type()
)
wfVinesArpSubnetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesArpSubnetid.setStatus("mandatory")


class _WfVinesArpSubnetBlock_Type(Integer32):
    """Custom type wfVinesArpSubnetBlock based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WfVinesArpSubnetBlock_Type.__name__ = "Integer32"
_WfVinesArpSubnetBlock_Object = MibScalar
wfVinesArpSubnetBlock = _WfVinesArpSubnetBlock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13, 5),
    _WfVinesArpSubnetBlock_Type()
)
wfVinesArpSubnetBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVinesArpSubnetBlock.setStatus("mandatory")
_WfVinesArpAssignDeniedPkts_Type = Counter32
_WfVinesArpAssignDeniedPkts_Object = MibScalar
wfVinesArpAssignDeniedPkts = _WfVinesArpAssignDeniedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 13, 6),
    _WfVinesArpAssignDeniedPkts_Type()
)
wfVinesArpAssignDeniedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesArpAssignDeniedPkts.setStatus("mandatory")
_WfVinesSeqRtpNbr_ObjectIdentity = ObjectIdentity
wfVinesSeqRtpNbr = _WfVinesSeqRtpNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 14)
)
_WfVinesSeqRtpNbrNumber_Type = Integer32
_WfVinesSeqRtpNbrNumber_Object = MibScalar
wfVinesSeqRtpNbrNumber = _WfVinesSeqRtpNbrNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 14, 1),
    _WfVinesSeqRtpNbrNumber_Type()
)
wfVinesSeqRtpNbrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesSeqRtpNbrNumber.setStatus("mandatory")
_WfVinesAggrStats_ObjectIdentity = ObjectIdentity
wfVinesAggrStats = _WfVinesAggrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15)
)
_WfVinesAggrInPkts_Type = Counter32
_WfVinesAggrInPkts_Object = MibScalar
wfVinesAggrInPkts = _WfVinesAggrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 1),
    _WfVinesAggrInPkts_Type()
)
wfVinesAggrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrInPkts.setStatus("mandatory")
_WfVinesAggrOutPkts_Type = Counter32
_WfVinesAggrOutPkts_Object = MibScalar
wfVinesAggrOutPkts = _WfVinesAggrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 2),
    _WfVinesAggrOutPkts_Type()
)
wfVinesAggrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrOutPkts.setStatus("mandatory")
_WfVinesAggrFwdPkts_Type = Counter32
_WfVinesAggrFwdPkts_Object = MibScalar
wfVinesAggrFwdPkts = _WfVinesAggrFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 3),
    _WfVinesAggrFwdPkts_Type()
)
wfVinesAggrFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrFwdPkts.setStatus("mandatory")
_WfVinesAggrInXsumErrs_Type = Counter32
_WfVinesAggrInXsumErrs_Object = MibScalar
wfVinesAggrInXsumErrs = _WfVinesAggrInXsumErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 4),
    _WfVinesAggrInXsumErrs_Type()
)
wfVinesAggrInXsumErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrInXsumErrs.setStatus("mandatory")
_WfVinesAggrBcastPkts_Type = Counter32
_WfVinesAggrBcastPkts_Object = MibScalar
wfVinesAggrBcastPkts = _WfVinesAggrBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 5),
    _WfVinesAggrBcastPkts_Type()
)
wfVinesAggrBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrBcastPkts.setStatus("mandatory")
_WfVinesAggrOutNoRoutes_Type = Counter32
_WfVinesAggrOutNoRoutes_Object = MibScalar
wfVinesAggrOutNoRoutes = _WfVinesAggrOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 6),
    _WfVinesAggrOutNoRoutes_Type()
)
wfVinesAggrOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrOutNoRoutes.setStatus("mandatory")
_WfVinesAggrInHopCountErrs_Type = Counter32
_WfVinesAggrInHopCountErrs_Object = MibScalar
wfVinesAggrInHopCountErrs = _WfVinesAggrInHopCountErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 7),
    _WfVinesAggrInHopCountErrs_Type()
)
wfVinesAggrInHopCountErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrInHopCountErrs.setStatus("mandatory")
_WfVinesAggrInIcpErrs_Type = Counter32
_WfVinesAggrInIcpErrs_Object = MibScalar
wfVinesAggrInIcpErrs = _WfVinesAggrInIcpErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 8),
    _WfVinesAggrInIcpErrs_Type()
)
wfVinesAggrInIcpErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrInIcpErrs.setStatus("mandatory")
_WfVinesAggrInIcpMetrics_Type = Counter32
_WfVinesAggrInIcpMetrics_Object = MibScalar
wfVinesAggrInIcpMetrics = _WfVinesAggrInIcpMetrics_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 9),
    _WfVinesAggrInIcpMetrics_Type()
)
wfVinesAggrInIcpMetrics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrInIcpMetrics.setStatus("mandatory")
_WfVinesAggrOutIcpErrs_Type = Counter32
_WfVinesAggrOutIcpErrs_Object = MibScalar
wfVinesAggrOutIcpErrs = _WfVinesAggrOutIcpErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 10),
    _WfVinesAggrOutIcpErrs_Type()
)
wfVinesAggrOutIcpErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrOutIcpErrs.setStatus("mandatory")
_WfVinesAggrOutIcpMetrics_Type = Counter32
_WfVinesAggrOutIcpMetrics_Object = MibScalar
wfVinesAggrOutIcpMetrics = _WfVinesAggrOutIcpMetrics_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 11),
    _WfVinesAggrOutIcpMetrics_Type()
)
wfVinesAggrOutIcpMetrics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrOutIcpMetrics.setStatus("mandatory")
_WfVinesAggrInArpQueries_Type = Counter32
_WfVinesAggrInArpQueries_Object = MibScalar
wfVinesAggrInArpQueries = _WfVinesAggrInArpQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 12),
    _WfVinesAggrInArpQueries_Type()
)
wfVinesAggrInArpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrInArpQueries.setStatus("mandatory")
_WfVinesAggrInArpAssigns_Type = Counter32
_WfVinesAggrInArpAssigns_Object = MibScalar
wfVinesAggrInArpAssigns = _WfVinesAggrInArpAssigns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 13),
    _WfVinesAggrInArpAssigns_Type()
)
wfVinesAggrInArpAssigns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrInArpAssigns.setStatus("mandatory")
_WfVinesAggrInArpErrs_Type = Counter32
_WfVinesAggrInArpErrs_Object = MibScalar
wfVinesAggrInArpErrs = _WfVinesAggrInArpErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 14),
    _WfVinesAggrInArpErrs_Type()
)
wfVinesAggrInArpErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrInArpErrs.setStatus("mandatory")
_WfVinesAggrOutArpServResps_Type = Counter32
_WfVinesAggrOutArpServResps_Object = MibScalar
wfVinesAggrOutArpServResps = _WfVinesAggrOutArpServResps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 15),
    _WfVinesAggrOutArpServResps_Type()
)
wfVinesAggrOutArpServResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrOutArpServResps.setStatus("mandatory")
_WfVinesAggrOutArpAssigns_Type = Counter32
_WfVinesAggrOutArpAssigns_Object = MibScalar
wfVinesAggrOutArpAssigns = _WfVinesAggrOutArpAssigns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 16),
    _WfVinesAggrOutArpAssigns_Type()
)
wfVinesAggrOutArpAssigns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrOutArpAssigns.setStatus("mandatory")
_WfVinesAggrInRedirects_Type = Counter32
_WfVinesAggrInRedirects_Object = MibScalar
wfVinesAggrInRedirects = _WfVinesAggrInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 17),
    _WfVinesAggrInRedirects_Type()
)
wfVinesAggrInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrInRedirects.setStatus("mandatory")
_WfVinesAggrOutRedirects_Type = Counter32
_WfVinesAggrOutRedirects_Object = MibScalar
wfVinesAggrOutRedirects = _WfVinesAggrOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 18),
    _WfVinesAggrOutRedirects_Type()
)
wfVinesAggrOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrOutRedirects.setStatus("mandatory")
_WfVinesAggrInEchos_Type = Counter32
_WfVinesAggrInEchos_Object = MibScalar
wfVinesAggrInEchos = _WfVinesAggrInEchos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 19),
    _WfVinesAggrInEchos_Type()
)
wfVinesAggrInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrInEchos.setStatus("mandatory")
_WfVinesAggrOutEchos_Type = Counter32
_WfVinesAggrOutEchos_Object = MibScalar
wfVinesAggrOutEchos = _WfVinesAggrOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 8, 15, 20),
    _WfVinesAggrOutEchos_Type()
)
wfVinesAggrOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVinesAggrOutEchos.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-VINES-MIB",
    **{"wfVinesBase": wfVinesBase,
       "wfVinesBaseDelete": wfVinesBaseDelete,
       "wfVinesBaseDisable": wfVinesBaseDisable,
       "wfVinesBaseState": wfVinesBaseState,
       "wfVinesBaseUserNetid": wfVinesBaseUserNetid,
       "wfVinesBaseRouterNetid": wfVinesBaseRouterNetid,
       "wfVinesBaseBcastClass": wfVinesBaseBcastClass,
       "wfVinesBaseNetworkSize": wfVinesBaseNetworkSize,
       "wfVinesBaseHostSize": wfVinesBaseHostSize,
       "wfVinesBaseRtpMode": wfVinesBaseRtpMode,
       "wfVinesBaseLogFilter": wfVinesBaseLogFilter,
       "wfVinesBaseRouterSeqNumber": wfVinesBaseRouterSeqNumber,
       "wfVinesBaseSoloSlotMask": wfVinesBaseSoloSlotMask,
       "wfVinesBaseSoloistSlot": wfVinesBaseSoloistSlot,
       "wfVinesIp": wfVinesIp,
       "wfVinesIpTotIn": wfVinesIpTotIn,
       "wfVinesIpTotOut": wfVinesIpTotOut,
       "wfVinesIpBad": wfVinesIpBad,
       "wfVinesIpRouted": wfVinesIpRouted,
       "wfVinesIpRoutedHWM": wfVinesIpRoutedHWM,
       "wfVinesIpBcast": wfVinesIpBcast,
       "wfVinesIpBcastHWM": wfVinesIpBcastHWM,
       "wfVinesIpReass": wfVinesIpReass,
       "wfVinesIpFrags": wfVinesIpFrags,
       "wfVinesIpToDodIP": wfVinesIpToDodIP,
       "wfVinesIpFromDodIP": wfVinesIpFromDodIP,
       "wfVinesRtpNbr": wfVinesRtpNbr,
       "wfVinesRtpNbrNumber": wfVinesRtpNbrNumber,
       "wfVinesRtpNbrTable": wfVinesRtpNbrTable,
       "wfVinesRtpNbrEntry": wfVinesRtpNbrEntry,
       "wfVinesRtpNbrNetId": wfVinesRtpNbrNetId,
       "wfVinesRtpNbrSubNetId": wfVinesRtpNbrSubNetId,
       "wfVinesRtpNbrType": wfVinesRtpNbrType,
       "wfVinesRtpNbrIfType": wfVinesRtpNbrIfType,
       "wfVinesRtpNbrRemAdr": wfVinesRtpNbrRemAdr,
       "wfVinesRtpNbrLocAdr": wfVinesRtpNbrLocAdr,
       "wfVinesRtpNbrLocSlot": wfVinesRtpNbrLocSlot,
       "wfVinesRtpNbrLocLine": wfVinesRtpNbrLocLine,
       "wfVinesRtpNbrSvrName": wfVinesRtpNbrSvrName,
       "wfVinesRtpNbrCost": wfVinesRtpNbrCost,
       "wfVinesSeqRtpNbrState": wfVinesSeqRtpNbrState,
       "wfVinesSeqRtpNbrSeqNumber": wfVinesSeqRtpNbrSeqNumber,
       "wfVinesRtpNbrRtType": wfVinesRtpNbrRtType,
       "wfVinesRtpNbrNumPaths": wfVinesRtpNbrNumPaths,
       "wfVinesRtpRt": wfVinesRtpRt,
       "wfVinesRtpRtNumber": wfVinesRtpRtNumber,
       "wfVinesRtpRtTable": wfVinesRtpRtTable,
       "wfVinesRtpRtEntry": wfVinesRtpRtEntry,
       "wfVinesRtpRtNetid": wfVinesRtpRtNetid,
       "wfVinesRtpRtMetric": wfVinesRtpRtMetric,
       "wfVinesRtpRtIdle": wfVinesRtpRtIdle,
       "wfVinesRtpRtGateNetid": wfVinesRtpRtGateNetid,
       "wfVinesRtpRtSvrName": wfVinesRtpRtSvrName,
       "wfVinesRtpRtGateSvrName": wfVinesRtpRtGateSvrName,
       "wfVinesRtpRtLocSlot": wfVinesRtpRtLocSlot,
       "wfVinesRtpRtLocLine": wfVinesRtpRtLocLine,
       "wfVinesRtpRtIfType": wfVinesRtpRtIfType,
       "wfVinesRtpRtGateHwAddr": wfVinesRtpRtGateHwAddr,
       "wfVinesRtpRtType": wfVinesRtpRtType,
       "wfVinesRtpRtSeqNumber": wfVinesRtpRtSeqNumber,
       "wfVinesRtpRtTimeStamp": wfVinesRtpRtTimeStamp,
       "wfVinesRtpRtNumPaths": wfVinesRtpRtNumPaths,
       "wfVinesIf": wfVinesIf,
       "wfVinesIfNumber": wfVinesIfNumber,
       "wfVinesIfTable": wfVinesIfTable,
       "wfVinesIfEntry": wfVinesIfEntry,
       "wfVinesIfDelete": wfVinesIfDelete,
       "wfVinesIfDisable": wfVinesIfDisable,
       "wfVinesIfState": wfVinesIfState,
       "wfVinesIfSlot": wfVinesIfSlot,
       "wfVinesIfLine": wfVinesIfLine,
       "wfVinesIfCct": wfVinesIfCct,
       "wfVinesIfSession": wfVinesIfSession,
       "wfVinesIfType": wfVinesIfType,
       "wfVinesIfDescr": wfVinesIfDescr,
       "wfVinesIfAdr": wfVinesIfAdr,
       "wfVinesIfDodIpDisable": wfVinesIfDodIpDisable,
       "wfVinesIfArpDisable": wfVinesIfArpDisable,
       "wfVinesIfTrEndStation": wfVinesIfTrEndStation,
       "wfVinesIfInPkts": wfVinesIfInPkts,
       "wfVinesIfInErrs": wfVinesIfInErrs,
       "wfVinesIfOutPkts": wfVinesIfOutPkts,
       "wfVinesIfOutErrs": wfVinesIfOutErrs,
       "wfVinesIfInMsgs": wfVinesIfInMsgs,
       "wfVinesIfMux": wfVinesIfMux,
       "wfVinesIfFwdDrops": wfVinesIfFwdDrops,
       "wfVinesIfZeroHopDrops": wfVinesIfZeroHopDrops,
       "wfVinesIfIcpInErrorNotifs": wfVinesIfIcpInErrorNotifs,
       "wfVinesIfIcpInMetricNotifs": wfVinesIfIcpInMetricNotifs,
       "wfVinesIfIcpInErrors": wfVinesIfIcpInErrors,
       "wfVinesIfIcpOutErrorNotifs": wfVinesIfIcpOutErrorNotifs,
       "wfVinesIfIcpOutMetricNotifs": wfVinesIfIcpOutMetricNotifs,
       "wfVinesIfArpInQueries": wfVinesIfArpInQueries,
       "wfVinesIfArpInAssgReqs": wfVinesIfArpInAssgReqs,
       "wfVinesIfArpInErrors": wfVinesIfArpInErrors,
       "wfVinesIfArpOutServRsps": wfVinesIfArpOutServRsps,
       "wfVinesIfArpOutAssgRsps": wfVinesIfArpOutAssgRsps,
       "wfVinesIfInRedirects": wfVinesIfInRedirects,
       "wfVinesIfOutRedirects": wfVinesIfOutRedirects,
       "wfVinesIfEchoInPkts": wfVinesIfEchoInPkts,
       "wfVinesIfEchoOutPkts": wfVinesIfEchoOutPkts,
       "wfVinesIfReassFails": wfVinesIfReassFails,
       "wfVinesIfRemClientPrivDisable": wfVinesIfRemClientPrivDisable,
       "wfVinesIfSplitHorizonDisable": wfVinesIfSplitHorizonDisable,
       "wfVinesIfCost": wfVinesIfCost,
       "wfVinesIfSyncPortNumber": wfVinesIfSyncPortNumber,
       "wfVinesIfInLackRescError": wfVinesIfInLackRescError,
       "wfVinesIfOutLackRescError": wfVinesIfOutLackRescError,
       "wfVinesIfRtpRecv": wfVinesIfRtpRecv,
       "wfVinesIfRtpSent": wfVinesIfRtpSent,
       "wfVinesIfSMDSGroupAddress": wfVinesIfSMDSGroupAddress,
       "wfVinesIfFRBcastDlci": wfVinesIfFRBcastDlci,
       "wfVinesIfCfgAdr": wfVinesIfCfgAdr,
       "wfVinesIfNumRoutes": wfVinesIfNumRoutes,
       "wfVinesIfCfgCost": wfVinesIfCfgCost,
       "wfVinesIfCostUsed": wfVinesIfCostUsed,
       "wfVinesIfFrpEnable": wfVinesIfFrpEnable,
       "wfVinesIfSeqArpInQueries": wfVinesIfSeqArpInQueries,
       "wfVinesIfSeqArpInAssgReqs": wfVinesIfSeqArpInAssgReqs,
       "wfVinesIfSeqArpInErrors": wfVinesIfSeqArpInErrors,
       "wfVinesIfSeqArpOutServRsps": wfVinesIfSeqArpOutServRsps,
       "wfVinesIfSeqArpOutAssgRsps": wfVinesIfSeqArpOutAssgRsps,
       "wfVinesIfInSeqRedirects": wfVinesIfInSeqRedirects,
       "wfVinesIfOutSeqRedirects": wfVinesIfOutSeqRedirects,
       "wfVinesIfSeqRtpRecv": wfVinesIfSeqRtpRecv,
       "wfVinesIfSeqRtpSent": wfVinesIfSeqRtpSent,
       "wfVinesIfRtpGenerationDisable": wfVinesIfRtpGenerationDisable,
       "wfVinesIfInverseArpEnable": wfVinesIfInverseArpEnable,
       "wfVinesIfSTalkSplitHorizon": wfVinesIfSTalkSplitHorizon,
       "wfVinesIfPermWanNbr": wfVinesIfPermWanNbr,
       "wfVinesIfNumFwdEntries": wfVinesIfNumFwdEntries,
       "wfVinesIfNumNonSeqNbrs": wfVinesIfNumNonSeqNbrs,
       "wfVinesIfNumSeqNbrs": wfVinesIfNumSeqNbrs,
       "wfVinesIfRedirectEnable": wfVinesIfRedirectEnable,
       "wfVinesIfX25VC": wfVinesIfX25VC,
       "wfVinesIfX25VCNumber": wfVinesIfX25VCNumber,
       "wfVinesIfX25VCTable": wfVinesIfX25VCTable,
       "wfVinesIfX25VCEntry": wfVinesIfX25VCEntry,
       "wfVinesIfX25VCSlot": wfVinesIfX25VCSlot,
       "wfVinesIfX25VCLine": wfVinesIfX25VCLine,
       "wfVinesIfX25VCCct": wfVinesIfX25VCCct,
       "wfVinesIfX25VCSession": wfVinesIfX25VCSession,
       "wfVinesIfX25VCTotIn": wfVinesIfX25VCTotIn,
       "wfVinesIfX25VCTotOut": wfVinesIfX25VCTotOut,
       "wfVinesIfX25VCInErrs": wfVinesIfX25VCInErrs,
       "wfVinesIfX25VCOutErrs": wfVinesIfX25VCOutErrs,
       "wfVinesIfX25VCPktsOut": wfVinesIfX25VCPktsOut,
       "wfVinesIfX25VCPktsAwaitAck": wfVinesIfX25VCPktsAwaitAck,
       "wfVinesIfX25VCBytesOut": wfVinesIfX25VCBytesOut,
       "wfVinesIfX25VCBytesAwaitAck": wfVinesIfX25VCBytesAwaitAck,
       "wfVinesIfX25VCPktsIn": wfVinesIfX25VCPktsIn,
       "wfVinesIfX25VCBytesIn": wfVinesIfX25VCBytesIn,
       "wfVinesIfX25VCResetsIn": wfVinesIfX25VCResetsIn,
       "wfVinesIfX25VCResetsOut": wfVinesIfX25VCResetsOut,
       "wfVinesTrafficFilterTable": wfVinesTrafficFilterTable,
       "wfVinesTrafficFilterEntry": wfVinesTrafficFilterEntry,
       "wfVinesTrafficFilterCreate": wfVinesTrafficFilterCreate,
       "wfVinesTrafficFilterEnable": wfVinesTrafficFilterEnable,
       "wfVinesTrafficFilterStatus": wfVinesTrafficFilterStatus,
       "wfVinesTrafficFilterCounter": wfVinesTrafficFilterCounter,
       "wfVinesTrafficFilterDefinition": wfVinesTrafficFilterDefinition,
       "wfVinesTrafficFilterReserved": wfVinesTrafficFilterReserved,
       "wfVinesTrafficFilterCircuit": wfVinesTrafficFilterCircuit,
       "wfVinesTrafficFilterRuleNumber": wfVinesTrafficFilterRuleNumber,
       "wfVinesTrafficFilterFragment": wfVinesTrafficFilterFragment,
       "wfVinesTrafficFilterName": wfVinesTrafficFilterName,
       "wfVinesNameTable": wfVinesNameTable,
       "wfVinesNameEntry": wfVinesNameEntry,
       "wfVinesNameDelete": wfVinesNameDelete,
       "wfVinesNameDisable": wfVinesNameDisable,
       "wfVinesNameNetid": wfVinesNameNetid,
       "wfVinesNameHost": wfVinesNameHost,
       "wfVinesNameSubNetid": wfVinesNameSubNetid,
       "wfVinesArp": wfVinesArp,
       "wfVinesArpDelete": wfVinesArpDelete,
       "wfVinesArpDisable": wfVinesArpDisable,
       "wfVinesArpState": wfVinesArpState,
       "wfVinesArpSubnetid": wfVinesArpSubnetid,
       "wfVinesArpSubnetBlock": wfVinesArpSubnetBlock,
       "wfVinesArpAssignDeniedPkts": wfVinesArpAssignDeniedPkts,
       "wfVinesSeqRtpNbr": wfVinesSeqRtpNbr,
       "wfVinesSeqRtpNbrNumber": wfVinesSeqRtpNbrNumber,
       "wfVinesAggrStats": wfVinesAggrStats,
       "wfVinesAggrInPkts": wfVinesAggrInPkts,
       "wfVinesAggrOutPkts": wfVinesAggrOutPkts,
       "wfVinesAggrFwdPkts": wfVinesAggrFwdPkts,
       "wfVinesAggrInXsumErrs": wfVinesAggrInXsumErrs,
       "wfVinesAggrBcastPkts": wfVinesAggrBcastPkts,
       "wfVinesAggrOutNoRoutes": wfVinesAggrOutNoRoutes,
       "wfVinesAggrInHopCountErrs": wfVinesAggrInHopCountErrs,
       "wfVinesAggrInIcpErrs": wfVinesAggrInIcpErrs,
       "wfVinesAggrInIcpMetrics": wfVinesAggrInIcpMetrics,
       "wfVinesAggrOutIcpErrs": wfVinesAggrOutIcpErrs,
       "wfVinesAggrOutIcpMetrics": wfVinesAggrOutIcpMetrics,
       "wfVinesAggrInArpQueries": wfVinesAggrInArpQueries,
       "wfVinesAggrInArpAssigns": wfVinesAggrInArpAssigns,
       "wfVinesAggrInArpErrs": wfVinesAggrInArpErrs,
       "wfVinesAggrOutArpServResps": wfVinesAggrOutArpServResps,
       "wfVinesAggrOutArpAssigns": wfVinesAggrOutArpAssigns,
       "wfVinesAggrInRedirects": wfVinesAggrInRedirects,
       "wfVinesAggrOutRedirects": wfVinesAggrOutRedirects,
       "wfVinesAggrInEchos": wfVinesAggrInEchos,
       "wfVinesAggrOutEchos": wfVinesAggrOutEchos}
)
