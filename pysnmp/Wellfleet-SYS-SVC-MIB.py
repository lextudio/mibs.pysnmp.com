# SNMP MIB module (Wellfleet-SYS-SVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-SYS-SVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:13 2024
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

(wfNetBootGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfNetBootGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfNetbootCfgGroup_ObjectIdentity = ObjectIdentity
wfNetbootCfgGroup = _WfNetbootCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1)
)


class _WfNetbootImage_Type(Integer32):
    """Custom type wfNetbootImage based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("imageoff", 1),
          ("imageon", 2))
    )


_WfNetbootImage_Type.__name__ = "Integer32"
_WfNetbootImage_Object = MibScalar
wfNetbootImage = _WfNetbootImage_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1, 1),
    _WfNetbootImage_Type()
)
wfNetbootImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootImage.setStatus("mandatory")


class _WfNetbootConfig_Type(Integer32):
    """Custom type wfNetbootConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configoff", 1),
          ("configon", 2))
    )


_WfNetbootConfig_Type.__name__ = "Integer32"
_WfNetbootConfig_Object = MibScalar
wfNetbootConfig = _WfNetbootConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1, 2),
    _WfNetbootConfig_Type()
)
wfNetbootConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootConfig.setStatus("mandatory")
_WfNetbootServerAddress_Type = IpAddress
_WfNetbootServerAddress_Object = MibScalar
wfNetbootServerAddress = _WfNetbootServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1, 3),
    _WfNetbootServerAddress_Type()
)
wfNetbootServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootServerAddress.setStatus("mandatory")
_WfNetbootImageName_Type = DisplayString
_WfNetbootImageName_Object = MibScalar
wfNetbootImageName = _WfNetbootImageName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1, 4),
    _WfNetbootImageName_Type()
)
wfNetbootImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootImageName.setStatus("mandatory")
_WfNetbootConfigName_Type = DisplayString
_WfNetbootConfigName_Object = MibScalar
wfNetbootConfigName = _WfNetbootConfigName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1, 5),
    _WfNetbootConfigName_Type()
)
wfNetbootConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootConfigName.setStatus("mandatory")


class _WfNetbootCfgDelete_Type(Integer32):
    """Custom type wfNetbootCfgDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfNetbootCfgDelete_Type.__name__ = "Integer32"
_WfNetbootCfgDelete_Object = MibScalar
wfNetbootCfgDelete = _WfNetbootCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 1, 6),
    _WfNetbootCfgDelete_Type()
)
wfNetbootCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootCfgDelete.setStatus("mandatory")
_WfNetbootCurrGroup_ObjectIdentity = ObjectIdentity
wfNetbootCurrGroup = _WfNetbootCurrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 2)
)


class _WfNetbootImageCurr_Type(Integer32):
    """Custom type wfNetbootImageCurr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("imagecurroff", 1),
          ("imagecurron", 2))
    )


_WfNetbootImageCurr_Type.__name__ = "Integer32"
_WfNetbootImageCurr_Object = MibScalar
wfNetbootImageCurr = _WfNetbootImageCurr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 2, 1),
    _WfNetbootImageCurr_Type()
)
wfNetbootImageCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootImageCurr.setStatus("mandatory")


class _WfNetbootConfigCurr_Type(Integer32):
    """Custom type wfNetbootConfigCurr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configcurroff", 1),
          ("configcurron", 2))
    )


_WfNetbootConfigCurr_Type.__name__ = "Integer32"
_WfNetbootConfigCurr_Object = MibScalar
wfNetbootConfigCurr = _WfNetbootConfigCurr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 2, 2),
    _WfNetbootConfigCurr_Type()
)
wfNetbootConfigCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootConfigCurr.setStatus("mandatory")
_WfNetbootServerAddressCurr_Type = IpAddress
_WfNetbootServerAddressCurr_Object = MibScalar
wfNetbootServerAddressCurr = _WfNetbootServerAddressCurr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 2, 3),
    _WfNetbootServerAddressCurr_Type()
)
wfNetbootServerAddressCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootServerAddressCurr.setStatus("mandatory")
_WfNetbootImageNameCurr_Type = DisplayString
_WfNetbootImageNameCurr_Object = MibScalar
wfNetbootImageNameCurr = _WfNetbootImageNameCurr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 2, 4),
    _WfNetbootImageNameCurr_Type()
)
wfNetbootImageNameCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootImageNameCurr.setStatus("mandatory")
_WfNetbootConfigNameCurr_Type = DisplayString
_WfNetbootConfigNameCurr_Object = MibScalar
wfNetbootConfigNameCurr = _WfNetbootConfigNameCurr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 2, 5),
    _WfNetbootConfigNameCurr_Type()
)
wfNetbootConfigNameCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootConfigNameCurr.setStatus("mandatory")
_WfNetbootCfgTable_Object = MibTable
wfNetbootCfgTable = _WfNetbootCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3)
)
if mibBuilder.loadTexts:
    wfNetbootCfgTable.setStatus("mandatory")
_WfNetbootCfgEntry_Object = MibTableRow
wfNetbootCfgEntry = _WfNetbootCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1)
)
wfNetbootCfgEntry.setIndexNames(
    (0, "Wellfleet-SYS-SVC-MIB", "wfNetbootSlot"),
    (0, "Wellfleet-SYS-SVC-MIB", "wfNetbootConnector"),
)
if mibBuilder.loadTexts:
    wfNetbootCfgEntry.setStatus("mandatory")


class _WfNetbootDelete_Type(Integer32):
    """Custom type wfNetbootDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfNetbootDelete_Type.__name__ = "Integer32"
_WfNetbootDelete_Object = MibTableColumn
wfNetbootDelete = _WfNetbootDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 1),
    _WfNetbootDelete_Type()
)
wfNetbootDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootDelete.setStatus("mandatory")


class _WfNetbootSlot_Type(Integer32):
    """Custom type wfNetbootSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfNetbootSlot_Type.__name__ = "Integer32"
_WfNetbootSlot_Object = MibTableColumn
wfNetbootSlot = _WfNetbootSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 2),
    _WfNetbootSlot_Type()
)
wfNetbootSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootSlot.setStatus("mandatory")


class _WfNetbootConnector_Type(Integer32):
    """Custom type wfNetbootConnector based on Integer32"""
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40)
        )
    )
    namedValues = NamedValues(
        *(("arncom1", 26),
          ("arncom2", 27),
          ("arncom3", 28),
          ("arncom4", 29),
          ("arncom5", 30),
          ("arnmau1", 31),
          ("arnmau2", 32),
          ("arnxcvr1", 24),
          ("arnxcvr2", 25),
          ("com1", 2),
          ("com11", 7),
          ("com12", 8),
          ("com13", 33),
          ("com14", 34),
          ("com2", 3),
          ("com21", 11),
          ("com22", 12),
          ("com23", 35),
          ("com24", 36),
          ("com3", 4),
          ("com31", 15),
          ("com32", 16),
          ("com33", 37),
          ("com34", 38),
          ("com41", 19),
          ("com42", 20),
          ("com43", 39),
          ("com44", 40),
          ("xcvr1", 1),
          ("xcvr11", 5),
          ("xcvr12", 6),
          ("xcvr2", 21),
          ("xcvr21", 9),
          ("xcvr22", 10),
          ("xcvr31", 13),
          ("xcvr32", 14),
          ("xcvr33", 22),
          ("xcvr34", 23),
          ("xcvr41", 17),
          ("xcvr42", 18))
    )


_WfNetbootConnector_Type.__name__ = "Integer32"
_WfNetbootConnector_Object = MibTableColumn
wfNetbootConnector = _WfNetbootConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 3),
    _WfNetbootConnector_Type()
)
wfNetbootConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootConnector.setStatus("mandatory")
_WfNetbootIpAddr_Type = IpAddress
_WfNetbootIpAddr_Object = MibTableColumn
wfNetbootIpAddr = _WfNetbootIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 4),
    _WfNetbootIpAddr_Type()
)
wfNetbootIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootIpAddr.setStatus("mandatory")
_WfNetbootIpMask_Type = IpAddress
_WfNetbootIpMask_Object = MibTableColumn
wfNetbootIpMask = _WfNetbootIpMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 5),
    _WfNetbootIpMask_Type()
)
wfNetbootIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootIpMask.setStatus("mandatory")
_WfNetbootNextHop_Type = IpAddress
_WfNetbootNextHop_Object = MibTableColumn
wfNetbootNextHop = _WfNetbootNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 6),
    _WfNetbootNextHop_Type()
)
wfNetbootNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootNextHop.setStatus("mandatory")


class _WfNetbootProtoMask_Type(Integer32):
    """Custom type wfNetbootProtoMask based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("annexaon", 5),
          ("fron", 1),
          ("intrnclkon", 3),
          ("lmion", 6),
          ("noton", 4),
          ("ppp", 7),
          ("x25on", 2))
    )


_WfNetbootProtoMask_Type.__name__ = "Integer32"
_WfNetbootProtoMask_Object = MibTableColumn
wfNetbootProtoMask = _WfNetbootProtoMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 7),
    _WfNetbootProtoMask_Type()
)
wfNetbootProtoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootProtoMask.setStatus("mandatory")


class _WfNetbootDisable_Type(Integer32):
    """Custom type wfNetbootDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfNetbootDisable_Type.__name__ = "Integer32"
_WfNetbootDisable_Object = MibTableColumn
wfNetbootDisable = _WfNetbootDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 8),
    _WfNetbootDisable_Type()
)
wfNetbootDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootDisable.setStatus("mandatory")
_WfNetbootConnName_Type = DisplayString
_WfNetbootConnName_Object = MibTableColumn
wfNetbootConnName = _WfNetbootConnName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 9),
    _WfNetbootConnName_Type()
)
wfNetbootConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootConnName.setStatus("mandatory")


class _WfNetbootTokenRingSpeed_Type(Integer32):
    """Custom type wfNetbootTokenRingSpeed based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("mbps16", 16),
          ("mbps4", 4))
    )


_WfNetbootTokenRingSpeed_Type.__name__ = "Integer32"
_WfNetbootTokenRingSpeed_Object = MibTableColumn
wfNetbootTokenRingSpeed = _WfNetbootTokenRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 10),
    _WfNetbootTokenRingSpeed_Type()
)
wfNetbootTokenRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootTokenRingSpeed.setStatus("mandatory")


class _WfNetbootBchanRate_Type(Integer32):
    """Custom type wfNetbootBchanRate based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("rate128k", 128),
          ("rate64k", 64))
    )


_WfNetbootBchanRate_Type.__name__ = "Integer32"
_WfNetbootBchanRate_Object = MibTableColumn
wfNetbootBchanRate = _WfNetbootBchanRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 11),
    _WfNetbootBchanRate_Type()
)
wfNetbootBchanRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootBchanRate.setStatus("mandatory")


class _WfNetbootDsuCsuOpMode_Type(Integer32):
    """Custom type wfNetbootDsuCsuOpMode based on Integer32"""
    defaultValue = 56

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(56,
              64)
        )
    )
    namedValues = NamedValues(
        *(("rate56k", 56),
          ("rate64k", 64))
    )


_WfNetbootDsuCsuOpMode_Type.__name__ = "Integer32"
_WfNetbootDsuCsuOpMode_Object = MibTableColumn
wfNetbootDsuCsuOpMode = _WfNetbootDsuCsuOpMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 3, 1, 12),
    _WfNetbootDsuCsuOpMode_Type()
)
wfNetbootDsuCsuOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootDsuCsuOpMode.setStatus("mandatory")
_WfNetbootCurrTable_Object = MibTable
wfNetbootCurrTable = _WfNetbootCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4)
)
if mibBuilder.loadTexts:
    wfNetbootCurrTable.setStatus("mandatory")
_WfNetbootCurrEntry_Object = MibTableRow
wfNetbootCurrEntry = _WfNetbootCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1)
)
wfNetbootCurrEntry.setIndexNames(
    (0, "Wellfleet-SYS-SVC-MIB", "wfNetbootCurrSlot"),
    (0, "Wellfleet-SYS-SVC-MIB", "wfNetbootCurrConnector"),
)
if mibBuilder.loadTexts:
    wfNetbootCurrEntry.setStatus("mandatory")


class _WfNetbootCurrSlot_Type(Integer32):
    """Custom type wfNetbootCurrSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfNetbootCurrSlot_Type.__name__ = "Integer32"
_WfNetbootCurrSlot_Object = MibTableColumn
wfNetbootCurrSlot = _WfNetbootCurrSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 1),
    _WfNetbootCurrSlot_Type()
)
wfNetbootCurrSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootCurrSlot.setStatus("mandatory")


class _WfNetbootCurrConnector_Type(Integer32):
    """Custom type wfNetbootCurrConnector based on Integer32"""
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40)
        )
    )
    namedValues = NamedValues(
        *(("currarncom1", 26),
          ("currarncom2", 27),
          ("currarncom3", 28),
          ("currarncom4", 29),
          ("currarncom5", 30),
          ("currarnmau1", 31),
          ("currarnmau2", 32),
          ("currarnxcvr1", 24),
          ("currarnxcvr2", 25),
          ("currcom1", 2),
          ("currcom11", 7),
          ("currcom12", 8),
          ("currcom13", 33),
          ("currcom14", 34),
          ("currcom2", 3),
          ("currcom21", 11),
          ("currcom22", 12),
          ("currcom23", 35),
          ("currcom24", 36),
          ("currcom3", 4),
          ("currcom31", 15),
          ("currcom32", 16),
          ("currcom33", 37),
          ("currcom34", 38),
          ("currcom41", 19),
          ("currcom42", 20),
          ("currcom43", 39),
          ("currcom44", 40),
          ("currxcvr1", 1),
          ("currxcvr11", 5),
          ("currxcvr12", 6),
          ("currxcvr2", 21),
          ("currxcvr21", 9),
          ("currxcvr22", 10),
          ("currxcvr31", 13),
          ("currxcvr32", 14),
          ("currxcvr33", 22),
          ("currxcvr34", 23),
          ("currxcvr41", 17),
          ("currxcvr42", 18))
    )


_WfNetbootCurrConnector_Type.__name__ = "Integer32"
_WfNetbootCurrConnector_Object = MibTableColumn
wfNetbootCurrConnector = _WfNetbootCurrConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 2),
    _WfNetbootCurrConnector_Type()
)
wfNetbootCurrConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootCurrConnector.setStatus("mandatory")
_WfNetbootCurrIpAddr_Type = IpAddress
_WfNetbootCurrIpAddr_Object = MibTableColumn
wfNetbootCurrIpAddr = _WfNetbootCurrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 3),
    _WfNetbootCurrIpAddr_Type()
)
wfNetbootCurrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootCurrIpAddr.setStatus("mandatory")
_WfNetbootCurrIpMask_Type = IpAddress
_WfNetbootCurrIpMask_Object = MibTableColumn
wfNetbootCurrIpMask = _WfNetbootCurrIpMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 4),
    _WfNetbootCurrIpMask_Type()
)
wfNetbootCurrIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootCurrIpMask.setStatus("mandatory")
_WfNetbootCurrNextHop_Type = IpAddress
_WfNetbootCurrNextHop_Object = MibTableColumn
wfNetbootCurrNextHop = _WfNetbootCurrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 5),
    _WfNetbootCurrNextHop_Type()
)
wfNetbootCurrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootCurrNextHop.setStatus("mandatory")


class _WfNetbootCurrProtoMask_Type(Integer32):
    """Custom type wfNetbootCurrProtoMask based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("annexaon", 5),
          ("frcurron", 1),
          ("intrnclkcurron", 3),
          ("lmion", 6),
          ("notcurron", 4),
          ("ppp", 7),
          ("x25curron", 2))
    )


_WfNetbootCurrProtoMask_Type.__name__ = "Integer32"
_WfNetbootCurrProtoMask_Object = MibTableColumn
wfNetbootCurrProtoMask = _WfNetbootCurrProtoMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 6),
    _WfNetbootCurrProtoMask_Type()
)
wfNetbootCurrProtoMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootCurrProtoMask.setStatus("mandatory")


class _WfNetbootCurrDisable_Type(Integer32):
    """Custom type wfNetbootCurrDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfNetbootCurrDisable_Type.__name__ = "Integer32"
_WfNetbootCurrDisable_Object = MibTableColumn
wfNetbootCurrDisable = _WfNetbootCurrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 7),
    _WfNetbootCurrDisable_Type()
)
wfNetbootCurrDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootCurrDisable.setStatus("mandatory")
_WfNetbootCurrConnName_Type = DisplayString
_WfNetbootCurrConnName_Object = MibTableColumn
wfNetbootCurrConnName = _WfNetbootCurrConnName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 8),
    _WfNetbootCurrConnName_Type()
)
wfNetbootCurrConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootCurrConnName.setStatus("mandatory")


class _WfNetbootCurrTokenRingSpeed_Type(Integer32):
    """Custom type wfNetbootCurrTokenRingSpeed based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("mbps16", 16),
          ("mbps4", 4))
    )


_WfNetbootCurrTokenRingSpeed_Type.__name__ = "Integer32"
_WfNetbootCurrTokenRingSpeed_Object = MibTableColumn
wfNetbootCurrTokenRingSpeed = _WfNetbootCurrTokenRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 9),
    _WfNetbootCurrTokenRingSpeed_Type()
)
wfNetbootCurrTokenRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNetbootCurrTokenRingSpeed.setStatus("mandatory")


class _WfNetbootCurrBchanRate_Type(Integer32):
    """Custom type wfNetbootCurrBchanRate based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("rate128k", 128),
          ("rate64k", 64))
    )


_WfNetbootCurrBchanRate_Type.__name__ = "Integer32"
_WfNetbootCurrBchanRate_Object = MibTableColumn
wfNetbootCurrBchanRate = _WfNetbootCurrBchanRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 10),
    _WfNetbootCurrBchanRate_Type()
)
wfNetbootCurrBchanRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootCurrBchanRate.setStatus("mandatory")


class _WfNetbootCurrDsuCsuOpMode_Type(Integer32):
    """Custom type wfNetbootCurrDsuCsuOpMode based on Integer32"""
    defaultValue = 56

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(56,
              64)
        )
    )
    namedValues = NamedValues(
        *(("rate56k", 56),
          ("rate64k", 64))
    )


_WfNetbootCurrDsuCsuOpMode_Type.__name__ = "Integer32"
_WfNetbootCurrDsuCsuOpMode_Object = MibTableColumn
wfNetbootCurrDsuCsuOpMode = _WfNetbootCurrDsuCsuOpMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 10, 4, 1, 11),
    _WfNetbootCurrDsuCsuOpMode_Type()
)
wfNetbootCurrDsuCsuOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNetbootCurrDsuCsuOpMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-SYS-SVC-MIB",
    **{"wfNetbootCfgGroup": wfNetbootCfgGroup,
       "wfNetbootImage": wfNetbootImage,
       "wfNetbootConfig": wfNetbootConfig,
       "wfNetbootServerAddress": wfNetbootServerAddress,
       "wfNetbootImageName": wfNetbootImageName,
       "wfNetbootConfigName": wfNetbootConfigName,
       "wfNetbootCfgDelete": wfNetbootCfgDelete,
       "wfNetbootCurrGroup": wfNetbootCurrGroup,
       "wfNetbootImageCurr": wfNetbootImageCurr,
       "wfNetbootConfigCurr": wfNetbootConfigCurr,
       "wfNetbootServerAddressCurr": wfNetbootServerAddressCurr,
       "wfNetbootImageNameCurr": wfNetbootImageNameCurr,
       "wfNetbootConfigNameCurr": wfNetbootConfigNameCurr,
       "wfNetbootCfgTable": wfNetbootCfgTable,
       "wfNetbootCfgEntry": wfNetbootCfgEntry,
       "wfNetbootDelete": wfNetbootDelete,
       "wfNetbootSlot": wfNetbootSlot,
       "wfNetbootConnector": wfNetbootConnector,
       "wfNetbootIpAddr": wfNetbootIpAddr,
       "wfNetbootIpMask": wfNetbootIpMask,
       "wfNetbootNextHop": wfNetbootNextHop,
       "wfNetbootProtoMask": wfNetbootProtoMask,
       "wfNetbootDisable": wfNetbootDisable,
       "wfNetbootConnName": wfNetbootConnName,
       "wfNetbootTokenRingSpeed": wfNetbootTokenRingSpeed,
       "wfNetbootBchanRate": wfNetbootBchanRate,
       "wfNetbootDsuCsuOpMode": wfNetbootDsuCsuOpMode,
       "wfNetbootCurrTable": wfNetbootCurrTable,
       "wfNetbootCurrEntry": wfNetbootCurrEntry,
       "wfNetbootCurrSlot": wfNetbootCurrSlot,
       "wfNetbootCurrConnector": wfNetbootCurrConnector,
       "wfNetbootCurrIpAddr": wfNetbootCurrIpAddr,
       "wfNetbootCurrIpMask": wfNetbootCurrIpMask,
       "wfNetbootCurrNextHop": wfNetbootCurrNextHop,
       "wfNetbootCurrProtoMask": wfNetbootCurrProtoMask,
       "wfNetbootCurrDisable": wfNetbootCurrDisable,
       "wfNetbootCurrConnName": wfNetbootCurrConnName,
       "wfNetbootCurrTokenRingSpeed": wfNetbootCurrTokenRingSpeed,
       "wfNetbootCurrBchanRate": wfNetbootCurrBchanRate,
       "wfNetbootCurrDsuCsuOpMode": wfNetbootCurrDsuCsuOpMode}
)
