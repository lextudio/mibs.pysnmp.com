# SNMP MIB module (ASCEND-MIBFRMRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBFRMRL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:35 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibframeRelayProfile_ObjectIdentity = ObjectIdentity
mibframeRelayProfile = _MibframeRelayProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 2)
)
_MibframeRelayProfileTable_Object = MibTable
mibframeRelayProfileTable = _MibframeRelayProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1)
)
if mibBuilder.loadTexts:
    mibframeRelayProfileTable.setStatus("mandatory")
_MibframeRelayProfileEntry_Object = MibTableRow
mibframeRelayProfileEntry = _MibframeRelayProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1)
)
mibframeRelayProfileEntry.setIndexNames(
    (0, "ASCEND-MIBFRMRL-MIB", "frameRelayProfile-FrName"),
)
if mibBuilder.loadTexts:
    mibframeRelayProfileEntry.setStatus("mandatory")
_FrameRelayProfile_FrName_Type = DisplayString
_FrameRelayProfile_FrName_Object = MibScalar
frameRelayProfile_FrName = _FrameRelayProfile_FrName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 1),
    _FrameRelayProfile_FrName_Type()
)
frameRelayProfile_FrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frameRelayProfile_FrName.setStatus("mandatory")


class _FrameRelayProfile_Active_Type(Integer32):
    """Custom type frameRelayProfile_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrameRelayProfile_Active_Type.__name__ = "Integer32"
_FrameRelayProfile_Active_Object = MibScalar
frameRelayProfile_Active = _FrameRelayProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 2),
    _FrameRelayProfile_Active_Type()
)
frameRelayProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_Active.setStatus("mandatory")
_FrameRelayProfile_NailedUpGroup_Type = Integer32
_FrameRelayProfile_NailedUpGroup_Object = MibScalar
frameRelayProfile_NailedUpGroup = _FrameRelayProfile_NailedUpGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 3),
    _FrameRelayProfile_NailedUpGroup_Type()
)
frameRelayProfile_NailedUpGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_NailedUpGroup.setStatus("mandatory")


class _FrameRelayProfile_NailedMode_Type(Integer32):
    """Custom type frameRelayProfile_NailedMode based on Integer32"""
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
        *(("aodi", 7),
          ("bri", 4),
          ("dChan", 6),
          ("ft1", 2),
          ("ft1Bo", 5),
          ("ft1Mpp", 3),
          ("megamax", 8),
          ("off", 1))
    )


_FrameRelayProfile_NailedMode_Type.__name__ = "Integer32"
_FrameRelayProfile_NailedMode_Object = MibScalar
frameRelayProfile_NailedMode = _FrameRelayProfile_NailedMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 4),
    _FrameRelayProfile_NailedMode_Type()
)
frameRelayProfile_NailedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_NailedMode.setStatus("mandatory")
_FrameRelayProfile_CalledNumberType_Type = Integer32
_FrameRelayProfile_CalledNumberType_Object = MibScalar
frameRelayProfile_CalledNumberType = _FrameRelayProfile_CalledNumberType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 5),
    _FrameRelayProfile_CalledNumberType_Type()
)
frameRelayProfile_CalledNumberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_CalledNumberType.setStatus("mandatory")


class _FrameRelayProfile_SwitchedCallType_Type(Integer32):
    """Custom type frameRelayProfile_SwitchedCallType based on Integer32"""
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
              39,
              40,
              41,
              42,
              43,
              44,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              255,
              263)
        )
    )
    namedValues = NamedValues(
        *(("atmSvc", 70),
          ("atmodem", 44),
          ("dws384Clear", 14),
          ("frameRelaySvc", 71),
          ("iptoip", 263),
          ("modem", 43),
          ("modem31khzAudio", 82),
          ("n-1024Clear", 24),
          ("n-1088Clear", 25),
          ("n-1152Clear", 26),
          ("n-1216Clear", 27),
          ("n-1280Clear", 28),
          ("n-128kClear", 10),
          ("n-1344Clear", 29),
          ("n-1408Clear", 30),
          ("n-14456kV110", 74),
          ("n-14456krV110", 76),
          ("n-14464kV110", 78),
          ("n-14464krV110", 80),
          ("n-144kClear", 255),
          ("n-1472Clear", 31),
          ("n-1536kClear", 8),
          ("n-1536kRestricted", 9),
          ("n-1600Clear", 32),
          ("n-1664Clear", 33),
          ("n-1728Clear", 34),
          ("n-1792Clear", 35),
          ("n-1856Clear", 36),
          ("n-1920Clear", 37),
          ("n-19256kV110", 49),
          ("n-19256krV110", 54),
          ("n-19264kV110", 59),
          ("n-19264krV110", 64),
          ("n-192kClear", 11),
          ("n-2456kV110", 46),
          ("n-2456krV110", 51),
          ("n-2464kV110", 56),
          ("n-2464krV110", 61),
          ("n-256kClear", 12),
          ("n-28856kV110", 75),
          ("n-28856krV110", 77),
          ("n-28864kV110", 79),
          ("n-28864krV110", 81),
          ("n-320kClear", 13),
          ("n-38456kV110", 50),
          ("n-38456krV110", 55),
          ("n-38464kV110", 60),
          ("n-38464krV110", 65),
          ("n-384kClear", 7),
          ("n-384kRestricted", 6),
          ("n-448Clear", 15),
          ("n-4856kV110", 47),
          ("n-4856krV110", 52),
          ("n-4864kV110", 57),
          ("n-4864krV110", 62),
          ("n-512Clear", 16),
          ("n-56kClear", 5),
          ("n-56kRestricted", 2),
          ("n-56kV110Clear", 42),
          ("n-576Clear", 17),
          ("n-640Clear", 18),
          ("n-64kClear", 3),
          ("n-64kRestricted", 4),
          ("n-64kX30Restricted", 41),
          ("n-704Clear", 19),
          ("n-768Clear", 20),
          ("n-832Clear", 21),
          ("n-896Clear", 22),
          ("n-960Clear", 23),
          ("n-9656kV110", 48),
          ("n-9656krV110", 53),
          ("n-9664kV110", 58),
          ("n-9664krV110", 63),
          ("phs64k", 67),
          ("v110ClearBearer", 40),
          ("v32", 66),
          ("voice", 1),
          ("voiceOverIp", 68),
          ("vpnTunnel", 72),
          ("wormarq", 73),
          ("x25Svc", 83),
          ("x30RestrictedBearer", 39))
    )


_FrameRelayProfile_SwitchedCallType_Type.__name__ = "Integer32"
_FrameRelayProfile_SwitchedCallType_Object = MibScalar
frameRelayProfile_SwitchedCallType = _FrameRelayProfile_SwitchedCallType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 6),
    _FrameRelayProfile_SwitchedCallType_Type()
)
frameRelayProfile_SwitchedCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_SwitchedCallType.setStatus("mandatory")
_FrameRelayProfile_PhoneNumber_Type = DisplayString
_FrameRelayProfile_PhoneNumber_Object = MibScalar
frameRelayProfile_PhoneNumber = _FrameRelayProfile_PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 7),
    _FrameRelayProfile_PhoneNumber_Type()
)
frameRelayProfile_PhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_PhoneNumber.setStatus("mandatory")
_FrameRelayProfile_BillingNumber_Type = DisplayString
_FrameRelayProfile_BillingNumber_Object = MibScalar
frameRelayProfile_BillingNumber = _FrameRelayProfile_BillingNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 8),
    _FrameRelayProfile_BillingNumber_Type()
)
frameRelayProfile_BillingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_BillingNumber.setStatus("mandatory")
_FrameRelayProfile_TransitNumber_Type = DisplayString
_FrameRelayProfile_TransitNumber_Object = MibScalar
frameRelayProfile_TransitNumber = _FrameRelayProfile_TransitNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 9),
    _FrameRelayProfile_TransitNumber_Type()
)
frameRelayProfile_TransitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_TransitNumber.setStatus("mandatory")


class _FrameRelayProfile_LinkMgmt_Type(Integer32):
    """Custom type frameRelayProfile_LinkMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ansiT1617d", 2),
          ("ccittQ933a", 3),
          ("none", 1))
    )


_FrameRelayProfile_LinkMgmt_Type.__name__ = "Integer32"
_FrameRelayProfile_LinkMgmt_Object = MibScalar
frameRelayProfile_LinkMgmt = _FrameRelayProfile_LinkMgmt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 10),
    _FrameRelayProfile_LinkMgmt_Type()
)
frameRelayProfile_LinkMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_LinkMgmt.setStatus("mandatory")
_FrameRelayProfile_CallByCallId_Type = Integer32
_FrameRelayProfile_CallByCallId_Object = MibScalar
frameRelayProfile_CallByCallId = _FrameRelayProfile_CallByCallId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 11),
    _FrameRelayProfile_CallByCallId_Type()
)
frameRelayProfile_CallByCallId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_CallByCallId.setStatus("mandatory")


class _FrameRelayProfile_LinkType_Type(Integer32):
    """Custom type frameRelayProfile_LinkType based on Integer32"""
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


_FrameRelayProfile_LinkType_Type.__name__ = "Integer32"
_FrameRelayProfile_LinkType_Object = MibScalar
frameRelayProfile_LinkType = _FrameRelayProfile_LinkType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 12),
    _FrameRelayProfile_LinkType_Type()
)
frameRelayProfile_LinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_LinkType.setStatus("mandatory")
_FrameRelayProfile_N391Val_Type = Integer32
_FrameRelayProfile_N391Val_Object = MibScalar
frameRelayProfile_N391Val = _FrameRelayProfile_N391Val_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 13),
    _FrameRelayProfile_N391Val_Type()
)
frameRelayProfile_N391Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_N391Val.setStatus("mandatory")
_FrameRelayProfile_N392Val_Type = Integer32
_FrameRelayProfile_N392Val_Object = MibScalar
frameRelayProfile_N392Val = _FrameRelayProfile_N392Val_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 14),
    _FrameRelayProfile_N392Val_Type()
)
frameRelayProfile_N392Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_N392Val.setStatus("mandatory")
_FrameRelayProfile_N393Val_Type = Integer32
_FrameRelayProfile_N393Val_Object = MibScalar
frameRelayProfile_N393Val = _FrameRelayProfile_N393Val_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 15),
    _FrameRelayProfile_N393Val_Type()
)
frameRelayProfile_N393Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_N393Val.setStatus("mandatory")
_FrameRelayProfile_T391Val_Type = Integer32
_FrameRelayProfile_T391Val_Object = MibScalar
frameRelayProfile_T391Val = _FrameRelayProfile_T391Val_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 16),
    _FrameRelayProfile_T391Val_Type()
)
frameRelayProfile_T391Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_T391Val.setStatus("mandatory")
_FrameRelayProfile_T392Val_Type = Integer32
_FrameRelayProfile_T392Val_Object = MibScalar
frameRelayProfile_T392Val = _FrameRelayProfile_T392Val_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 17),
    _FrameRelayProfile_T392Val_Type()
)
frameRelayProfile_T392Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_T392Val.setStatus("mandatory")
_FrameRelayProfile_oMRU_Type = Integer32
_FrameRelayProfile_oMRU_Object = MibScalar
frameRelayProfile_oMRU = _FrameRelayProfile_oMRU_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 18),
    _FrameRelayProfile_oMRU_Type()
)
frameRelayProfile_oMRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_oMRU.setStatus("mandatory")
_FrameRelayProfile_DceN392Val_Type = Integer32
_FrameRelayProfile_DceN392Val_Object = MibScalar
frameRelayProfile_DceN392Val = _FrameRelayProfile_DceN392Val_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 19),
    _FrameRelayProfile_DceN392Val_Type()
)
frameRelayProfile_DceN392Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_DceN392Val.setStatus("mandatory")
_FrameRelayProfile_DceN393Val_Type = Integer32
_FrameRelayProfile_DceN393Val_Object = MibScalar
frameRelayProfile_DceN393Val = _FrameRelayProfile_DceN393Val_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 20),
    _FrameRelayProfile_DceN393Val_Type()
)
frameRelayProfile_DceN393Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_DceN393Val.setStatus("mandatory")


class _FrameRelayProfile_LinkMgmtDlci_Type(Integer32):
    """Custom type frameRelayProfile_LinkMgmtDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("dlci0", 1),
          ("dlci1023", 1024))
    )


_FrameRelayProfile_LinkMgmtDlci_Type.__name__ = "Integer32"
_FrameRelayProfile_LinkMgmtDlci_Object = MibScalar
frameRelayProfile_LinkMgmtDlci = _FrameRelayProfile_LinkMgmtDlci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 21),
    _FrameRelayProfile_LinkMgmtDlci_Type()
)
frameRelayProfile_LinkMgmtDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_LinkMgmtDlci.setStatus("mandatory")


class _FrameRelayProfile_Action_o_Type(Integer32):
    """Custom type frameRelayProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_FrameRelayProfile_Action_o_Type.__name__ = "Integer32"
_FrameRelayProfile_Action_o_Object = MibScalar
frameRelayProfile_Action_o = _FrameRelayProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 22),
    _FrameRelayProfile_Action_o_Type()
)
frameRelayProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_Action_o.setStatus("mandatory")
_FrameRelayProfile_MfrBundleName_Type = DisplayString
_FrameRelayProfile_MfrBundleName_Object = MibScalar
frameRelayProfile_MfrBundleName = _FrameRelayProfile_MfrBundleName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 24),
    _FrameRelayProfile_MfrBundleName_Type()
)
frameRelayProfile_MfrBundleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_MfrBundleName.setStatus("mandatory")


class _FrameRelayProfile_SvcOptions_Enabled_Type(Integer32):
    """Custom type frameRelayProfile_SvcOptions_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrameRelayProfile_SvcOptions_Enabled_Type.__name__ = "Integer32"
_FrameRelayProfile_SvcOptions_Enabled_Object = MibScalar
frameRelayProfile_SvcOptions_Enabled = _FrameRelayProfile_SvcOptions_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 25),
    _FrameRelayProfile_SvcOptions_Enabled_Type()
)
frameRelayProfile_SvcOptions_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_SvcOptions_Enabled.setStatus("mandatory")
_FrameRelayProfile_SvcOptions_FrAddress_Type = DisplayString
_FrameRelayProfile_SvcOptions_FrAddress_Object = MibScalar
frameRelayProfile_SvcOptions_FrAddress = _FrameRelayProfile_SvcOptions_FrAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 26),
    _FrameRelayProfile_SvcOptions_FrAddress_Type()
)
frameRelayProfile_SvcOptions_FrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_SvcOptions_FrAddress.setStatus("mandatory")


class _FrameRelayProfile_Frf5Options_Enable_Type(Integer32):
    """Custom type frameRelayProfile_Frf5Options_Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrameRelayProfile_Frf5Options_Enable_Type.__name__ = "Integer32"
_FrameRelayProfile_Frf5Options_Enable_Object = MibScalar
frameRelayProfile_Frf5Options_Enable = _FrameRelayProfile_Frf5Options_Enable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 27),
    _FrameRelayProfile_Frf5Options_Enable_Type()
)
frameRelayProfile_Frf5Options_Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_Frf5Options_Enable.setStatus("mandatory")
_FrameRelayProfile_Frf5Options_Vpi_Type = Integer32
_FrameRelayProfile_Frf5Options_Vpi_Object = MibScalar
frameRelayProfile_Frf5Options_Vpi = _FrameRelayProfile_Frf5Options_Vpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 28),
    _FrameRelayProfile_Frf5Options_Vpi_Type()
)
frameRelayProfile_Frf5Options_Vpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_Frf5Options_Vpi.setStatus("mandatory")
_FrameRelayProfile_Frf5Options_Vci_Type = Integer32
_FrameRelayProfile_Frf5Options_Vci_Object = MibScalar
frameRelayProfile_Frf5Options_Vci = _FrameRelayProfile_Frf5Options_Vci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 29),
    _FrameRelayProfile_Frf5Options_Vci_Type()
)
frameRelayProfile_Frf5Options_Vci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_Frf5Options_Vci.setStatus("mandatory")
_FrameRelayProfile_Frf5Options_Shaper_Type = Integer32
_FrameRelayProfile_Frf5Options_Shaper_Object = MibScalar
frameRelayProfile_Frf5Options_Shaper = _FrameRelayProfile_Frf5Options_Shaper_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 30),
    _FrameRelayProfile_Frf5Options_Shaper_Type()
)
frameRelayProfile_Frf5Options_Shaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_Frf5Options_Shaper.setStatus("mandatory")


class _FrameRelayProfile_FastPathEnabled_Type(Integer32):
    """Custom type frameRelayProfile_FastPathEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrameRelayProfile_FastPathEnabled_Type.__name__ = "Integer32"
_FrameRelayProfile_FastPathEnabled_Object = MibScalar
frameRelayProfile_FastPathEnabled = _FrameRelayProfile_FastPathEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 2, 1, 1, 31),
    _FrameRelayProfile_FastPathEnabled_Type()
)
frameRelayProfile_FastPathEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frameRelayProfile_FastPathEnabled.setStatus("mandatory")
_MibmfrProfile_ObjectIdentity = ObjectIdentity
mibmfrProfile = _MibmfrProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 78)
)
_MibmfrProfileTable_Object = MibTable
mibmfrProfileTable = _MibmfrProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 78, 1)
)
if mibBuilder.loadTexts:
    mibmfrProfileTable.setStatus("mandatory")
_MibmfrProfileEntry_Object = MibTableRow
mibmfrProfileEntry = _MibmfrProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1)
)
mibmfrProfileEntry.setIndexNames(
    (0, "ASCEND-MIBFRMRL-MIB", "mfrProfile-MfrBundleName"),
)
if mibBuilder.loadTexts:
    mibmfrProfileEntry.setStatus("mandatory")
_MfrProfile_MfrBundleName_Type = DisplayString
_MfrProfile_MfrBundleName_Object = MibScalar
mfrProfile_MfrBundleName = _MfrProfile_MfrBundleName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1, 1),
    _MfrProfile_MfrBundleName_Type()
)
mfrProfile_MfrBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrProfile_MfrBundleName.setStatus("mandatory")


class _MfrProfile_Active_Type(Integer32):
    """Custom type mfrProfile_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MfrProfile_Active_Type.__name__ = "Integer32"
_MfrProfile_Active_Object = MibScalar
mfrProfile_Active = _MfrProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1, 2),
    _MfrProfile_Active_Type()
)
mfrProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrProfile_Active.setStatus("mandatory")


class _MfrProfile_MfrBundleType_Type(Integer32):
    """Custom type mfrProfile_MfrBundleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mfrDte", 1)
    )


_MfrProfile_MfrBundleType_Type.__name__ = "Integer32"
_MfrProfile_MfrBundleType_Object = MibScalar
mfrProfile_MfrBundleType = _MfrProfile_MfrBundleType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1, 3),
    _MfrProfile_MfrBundleType_Type()
)
mfrProfile_MfrBundleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrProfile_MfrBundleType.setStatus("mandatory")
_MfrProfile_MaxBundleMembers_Type = Integer32
_MfrProfile_MaxBundleMembers_Object = MibScalar
mfrProfile_MaxBundleMembers = _MfrProfile_MaxBundleMembers_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1, 4),
    _MfrProfile_MaxBundleMembers_Type()
)
mfrProfile_MaxBundleMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrProfile_MaxBundleMembers.setStatus("mandatory")
_MfrProfile_MinBandwidth_Type = Integer32
_MfrProfile_MinBandwidth_Object = MibScalar
mfrProfile_MinBandwidth = _MfrProfile_MinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1, 5),
    _MfrProfile_MinBandwidth_Type()
)
mfrProfile_MinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrProfile_MinBandwidth.setStatus("mandatory")


class _MfrProfile_Action_o_Type(Integer32):
    """Custom type mfrProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_MfrProfile_Action_o_Type.__name__ = "Integer32"
_MfrProfile_Action_o_Object = MibScalar
mfrProfile_Action_o = _MfrProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 78, 1, 1, 6),
    _MfrProfile_Action_o_Type()
)
mfrProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBFRMRL-MIB",
    **{"DisplayString": DisplayString,
       "mibframeRelayProfile": mibframeRelayProfile,
       "mibframeRelayProfileTable": mibframeRelayProfileTable,
       "mibframeRelayProfileEntry": mibframeRelayProfileEntry,
       "frameRelayProfile-FrName": frameRelayProfile_FrName,
       "frameRelayProfile-Active": frameRelayProfile_Active,
       "frameRelayProfile-NailedUpGroup": frameRelayProfile_NailedUpGroup,
       "frameRelayProfile-NailedMode": frameRelayProfile_NailedMode,
       "frameRelayProfile-CalledNumberType": frameRelayProfile_CalledNumberType,
       "frameRelayProfile-SwitchedCallType": frameRelayProfile_SwitchedCallType,
       "frameRelayProfile-PhoneNumber": frameRelayProfile_PhoneNumber,
       "frameRelayProfile-BillingNumber": frameRelayProfile_BillingNumber,
       "frameRelayProfile-TransitNumber": frameRelayProfile_TransitNumber,
       "frameRelayProfile-LinkMgmt": frameRelayProfile_LinkMgmt,
       "frameRelayProfile-CallByCallId": frameRelayProfile_CallByCallId,
       "frameRelayProfile-LinkType": frameRelayProfile_LinkType,
       "frameRelayProfile-N391Val": frameRelayProfile_N391Val,
       "frameRelayProfile-N392Val": frameRelayProfile_N392Val,
       "frameRelayProfile-N393Val": frameRelayProfile_N393Val,
       "frameRelayProfile-T391Val": frameRelayProfile_T391Val,
       "frameRelayProfile-T392Val": frameRelayProfile_T392Val,
       "frameRelayProfile-oMRU": frameRelayProfile_oMRU,
       "frameRelayProfile-DceN392Val": frameRelayProfile_DceN392Val,
       "frameRelayProfile-DceN393Val": frameRelayProfile_DceN393Val,
       "frameRelayProfile-LinkMgmtDlci": frameRelayProfile_LinkMgmtDlci,
       "frameRelayProfile-Action-o": frameRelayProfile_Action_o,
       "frameRelayProfile-MfrBundleName": frameRelayProfile_MfrBundleName,
       "frameRelayProfile-SvcOptions-Enabled": frameRelayProfile_SvcOptions_Enabled,
       "frameRelayProfile-SvcOptions-FrAddress": frameRelayProfile_SvcOptions_FrAddress,
       "frameRelayProfile-Frf5Options-Enable": frameRelayProfile_Frf5Options_Enable,
       "frameRelayProfile-Frf5Options-Vpi": frameRelayProfile_Frf5Options_Vpi,
       "frameRelayProfile-Frf5Options-Vci": frameRelayProfile_Frf5Options_Vci,
       "frameRelayProfile-Frf5Options-Shaper": frameRelayProfile_Frf5Options_Shaper,
       "frameRelayProfile-FastPathEnabled": frameRelayProfile_FastPathEnabled,
       "mibmfrProfile": mibmfrProfile,
       "mibmfrProfileTable": mibmfrProfileTable,
       "mibmfrProfileEntry": mibmfrProfileEntry,
       "mfrProfile-MfrBundleName": mfrProfile_MfrBundleName,
       "mfrProfile-Active": mfrProfile_Active,
       "mfrProfile-MfrBundleType": mfrProfile_MfrBundleType,
       "mfrProfile-MaxBundleMembers": mfrProfile_MaxBundleMembers,
       "mfrProfile-MinBandwidth": mfrProfile_MinBandwidth,
       "mfrProfile-Action-o": mfrProfile_Action_o}
)
