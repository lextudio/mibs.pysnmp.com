# SNMP MIB module (ASCEND-MIBX25-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBX25-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:35 2024
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

_Mibx25Profile_ObjectIdentity = ObjectIdentity
mibx25Profile = _Mibx25Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 140)
)
_Mibx25ProfileTable_Object = MibTable
mibx25ProfileTable = _Mibx25ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1)
)
if mibBuilder.loadTexts:
    mibx25ProfileTable.setStatus("mandatory")
_Mibx25ProfileEntry_Object = MibTableRow
mibx25ProfileEntry = _Mibx25ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1)
)
mibx25ProfileEntry.setIndexNames(
    (0, "ASCEND-MIBX25-MIB", "x25Profile-X25Name"),
)
if mibBuilder.loadTexts:
    mibx25ProfileEntry.setStatus("mandatory")
_X25Profile_X25Name_Type = DisplayString
_X25Profile_X25Name_Object = MibScalar
x25Profile_X25Name = _X25Profile_X25Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 1),
    _X25Profile_X25Name_Type()
)
x25Profile_X25Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25Profile_X25Name.setStatus("mandatory")


class _X25Profile_Active_Type(Integer32):
    """Custom type x25Profile_Active based on Integer32"""
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


_X25Profile_Active_Type.__name__ = "Integer32"
_X25Profile_Active_Object = MibScalar
x25Profile_Active = _X25Profile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 2),
    _X25Profile_Active_Type()
)
x25Profile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_Active.setStatus("mandatory")


class _X25Profile_Kludge_Type(Integer32):
    """Custom type x25Profile_Kludge based on Integer32"""
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


_X25Profile_Kludge_Type.__name__ = "Integer32"
_X25Profile_Kludge_Object = MibScalar
x25Profile_Kludge = _X25Profile_Kludge_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 3),
    _X25Profile_Kludge_Type()
)
x25Profile_Kludge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_Kludge.setStatus("mandatory")
_X25Profile_NailedUpGroup_Type = Integer32
_X25Profile_NailedUpGroup_Object = MibScalar
x25Profile_NailedUpGroup = _X25Profile_NailedUpGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 4),
    _X25Profile_NailedUpGroup_Type()
)
x25Profile_NailedUpGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_NailedUpGroup.setStatus("mandatory")


class _X25Profile_NailedMode_Type(Integer32):
    """Custom type x25Profile_NailedMode based on Integer32"""
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


_X25Profile_NailedMode_Type.__name__ = "Integer32"
_X25Profile_NailedMode_Object = MibScalar
x25Profile_NailedMode = _X25Profile_NailedMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 5),
    _X25Profile_NailedMode_Type()
)
x25Profile_NailedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_NailedMode.setStatus("mandatory")
_X25Profile_CalledNumberType_Type = Integer32
_X25Profile_CalledNumberType_Object = MibScalar
x25Profile_CalledNumberType = _X25Profile_CalledNumberType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 6),
    _X25Profile_CalledNumberType_Type()
)
x25Profile_CalledNumberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_CalledNumberType.setStatus("mandatory")


class _X25Profile_SwitchedCallType_Type(Integer32):
    """Custom type x25Profile_SwitchedCallType based on Integer32"""
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


_X25Profile_SwitchedCallType_Type.__name__ = "Integer32"
_X25Profile_SwitchedCallType_Object = MibScalar
x25Profile_SwitchedCallType = _X25Profile_SwitchedCallType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 7),
    _X25Profile_SwitchedCallType_Type()
)
x25Profile_SwitchedCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_SwitchedCallType.setStatus("mandatory")
_X25Profile_PhoneNumber_Type = DisplayString
_X25Profile_PhoneNumber_Object = MibScalar
x25Profile_PhoneNumber = _X25Profile_PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 8),
    _X25Profile_PhoneNumber_Type()
)
x25Profile_PhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_PhoneNumber.setStatus("mandatory")
_X25Profile_BillingNumber_Type = DisplayString
_X25Profile_BillingNumber_Object = MibScalar
x25Profile_BillingNumber = _X25Profile_BillingNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 9),
    _X25Profile_BillingNumber_Type()
)
x25Profile_BillingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_BillingNumber.setStatus("mandatory")
_X25Profile_TransitNumber_Type = DisplayString
_X25Profile_TransitNumber_Object = MibScalar
x25Profile_TransitNumber = _X25Profile_TransitNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 10),
    _X25Profile_TransitNumber_Type()
)
x25Profile_TransitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_TransitNumber.setStatus("mandatory")
_X25Profile_CallByCallId_Type = Integer32
_X25Profile_CallByCallId_Object = MibScalar
x25Profile_CallByCallId = _X25Profile_CallByCallId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 11),
    _X25Profile_CallByCallId_Type()
)
x25Profile_CallByCallId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_CallByCallId.setStatus("mandatory")
_X25Profile_oT1Val_Type = Integer32
_X25Profile_oT1Val_Object = MibScalar
x25Profile_oT1Val = _X25Profile_oT1Val_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 12),
    _X25Profile_oT1Val_Type()
)
x25Profile_oT1Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_oT1Val.setStatus("mandatory")
_X25Profile_oT2Val_Type = Integer32
_X25Profile_oT2Val_Object = MibScalar
x25Profile_oT2Val = _X25Profile_oT2Val_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 13),
    _X25Profile_oT2Val_Type()
)
x25Profile_oT2Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_oT2Val.setStatus("mandatory")
_X25Profile_oN2Val_Type = Integer32
_X25Profile_oN2Val_Object = MibScalar
x25Profile_oN2Val = _X25Profile_oN2Val_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 14),
    _X25Profile_oN2Val_Type()
)
x25Profile_oN2Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_oN2Val.setStatus("mandatory")
_X25Profile_KVal_Type = Integer32
_X25Profile_KVal_Object = MibScalar
x25Profile_KVal = _X25Profile_KVal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 15),
    _X25Profile_KVal_Type()
)
x25Profile_KVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_KVal.setStatus("mandatory")
_X25Profile_oPktWindow_Type = Integer32
_X25Profile_oPktWindow_Object = MibScalar
x25Profile_oPktWindow = _X25Profile_oPktWindow_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 16),
    _X25Profile_oPktWindow_Type()
)
x25Profile_oPktWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_oPktWindow.setStatus("mandatory")
_X25Profile_oPktSize_Type = Integer32
_X25Profile_oPktSize_Object = MibScalar
x25Profile_oPktSize = _X25Profile_oPktSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 17),
    _X25Profile_oPktSize_Type()
)
x25Profile_oPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_oPktSize.setStatus("mandatory")


class _X25Profile_oMinPktSize_Type(Integer32):
    """Custom type x25Profile_oMinPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("n-10", 11),
          ("n-11", 12),
          ("n-12", 13),
          ("n-6", 7),
          ("n-7", 8),
          ("n-8", 9),
          ("n-9", 10))
    )


_X25Profile_oMinPktSize_Type.__name__ = "Integer32"
_X25Profile_oMinPktSize_Object = MibScalar
x25Profile_oMinPktSize = _X25Profile_oMinPktSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 18),
    _X25Profile_oMinPktSize_Type()
)
x25Profile_oMinPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_oMinPktSize.setStatus("mandatory")


class _X25Profile_oMaxPktSize_Type(Integer32):
    """Custom type x25Profile_oMaxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("n-10", 11),
          ("n-11", 12),
          ("n-12", 13),
          ("n-6", 7),
          ("n-7", 8),
          ("n-8", 9),
          ("n-9", 10))
    )


_X25Profile_oMaxPktSize_Type.__name__ = "Integer32"
_X25Profile_oMaxPktSize_Object = MibScalar
x25Profile_oMaxPktSize = _X25Profile_oMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 19),
    _X25Profile_oMaxPktSize_Type()
)
x25Profile_oMaxPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_oMaxPktSize.setStatus("mandatory")
_X25Profile_LowestPVC_Type = Integer32
_X25Profile_LowestPVC_Object = MibScalar
x25Profile_LowestPVC = _X25Profile_LowestPVC_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 20),
    _X25Profile_LowestPVC_Type()
)
x25Profile_LowestPVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_LowestPVC.setStatus("mandatory")
_X25Profile_HighestPVC_Type = Integer32
_X25Profile_HighestPVC_Object = MibScalar
x25Profile_HighestPVC = _X25Profile_HighestPVC_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 21),
    _X25Profile_HighestPVC_Type()
)
x25Profile_HighestPVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_HighestPVC.setStatus("mandatory")
_X25Profile_LowestSVC_Type = Integer32
_X25Profile_LowestSVC_Object = MibScalar
x25Profile_LowestSVC = _X25Profile_LowestSVC_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 22),
    _X25Profile_LowestSVC_Type()
)
x25Profile_LowestSVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_LowestSVC.setStatus("mandatory")
_X25Profile_HighestSVC_Type = Integer32
_X25Profile_HighestSVC_Object = MibScalar
x25Profile_HighestSVC = _X25Profile_HighestSVC_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 23),
    _X25Profile_HighestSVC_Type()
)
x25Profile_HighestSVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_HighestSVC.setStatus("mandatory")


class _X25Profile_ClearDiag_Type(Integer32):
    """Custom type x25Profile_ClearDiag based on Integer32"""
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


_X25Profile_ClearDiag_Type.__name__ = "Integer32"
_X25Profile_ClearDiag_Object = MibScalar
x25Profile_ClearDiag = _X25Profile_ClearDiag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 24),
    _X25Profile_ClearDiag_Type()
)
x25Profile_ClearDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_ClearDiag.setStatus("mandatory")


class _X25Profile_ResetDiag_Type(Integer32):
    """Custom type x25Profile_ResetDiag based on Integer32"""
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


_X25Profile_ResetDiag_Type.__name__ = "Integer32"
_X25Profile_ResetDiag_Object = MibScalar
x25Profile_ResetDiag = _X25Profile_ResetDiag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 25),
    _X25Profile_ResetDiag_Type()
)
x25Profile_ResetDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_ResetDiag.setStatus("mandatory")


class _X25Profile_RestartDiag_Type(Integer32):
    """Custom type x25Profile_RestartDiag based on Integer32"""
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


_X25Profile_RestartDiag_Type.__name__ = "Integer32"
_X25Profile_RestartDiag_Object = MibScalar
x25Profile_RestartDiag = _X25Profile_RestartDiag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 26),
    _X25Profile_RestartDiag_Type()
)
x25Profile_RestartDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_RestartDiag.setStatus("mandatory")


class _X25Profile_PktOptions_Type(Integer32):
    """Custom type x25Profile_PktOptions based on Integer32"""
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
        *(("afna", 3),
          ("none", 1),
          ("npws", 2),
          ("npwsAfna", 4))
    )


_X25Profile_PktOptions_Type.__name__ = "Integer32"
_X25Profile_PktOptions_Object = MibScalar
x25Profile_PktOptions = _X25Profile_PktOptions_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 27),
    _X25Profile_PktOptions_Type()
)
x25Profile_PktOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_PktOptions.setStatus("mandatory")
_X25Profile_PktT20_Type = Integer32
_X25Profile_PktT20_Object = MibScalar
x25Profile_PktT20 = _X25Profile_PktT20_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 28),
    _X25Profile_PktT20_Type()
)
x25Profile_PktT20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_PktT20.setStatus("mandatory")
_X25Profile_PktR20_Type = Integer32
_X25Profile_PktR20_Object = MibScalar
x25Profile_PktR20 = _X25Profile_PktR20_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 29),
    _X25Profile_PktR20_Type()
)
x25Profile_PktR20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_PktR20.setStatus("mandatory")
_X25Profile_PktT21_Type = Integer32
_X25Profile_PktT21_Object = MibScalar
x25Profile_PktT21 = _X25Profile_PktT21_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 30),
    _X25Profile_PktT21_Type()
)
x25Profile_PktT21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_PktT21.setStatus("mandatory")
_X25Profile_PktT22_Type = Integer32
_X25Profile_PktT22_Object = MibScalar
x25Profile_PktT22 = _X25Profile_PktT22_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 31),
    _X25Profile_PktT22_Type()
)
x25Profile_PktT22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_PktT22.setStatus("mandatory")
_X25Profile_PktR22_Type = Integer32
_X25Profile_PktR22_Object = MibScalar
x25Profile_PktR22 = _X25Profile_PktR22_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 32),
    _X25Profile_PktR22_Type()
)
x25Profile_PktR22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_PktR22.setStatus("mandatory")
_X25Profile_PktT23_Type = Integer32
_X25Profile_PktT23_Object = MibScalar
x25Profile_PktT23 = _X25Profile_PktT23_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 33),
    _X25Profile_PktT23_Type()
)
x25Profile_PktT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_PktT23.setStatus("mandatory")
_X25Profile_PktR23_Type = Integer32
_X25Profile_PktR23_Object = MibScalar
x25Profile_PktR23 = _X25Profile_PktR23_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 34),
    _X25Profile_PktR23_Type()
)
x25Profile_PktR23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_PktR23.setStatus("mandatory")


class _X25Profile_DteFlag_Type(Integer32):
    """Custom type x25Profile_DteFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_X25Profile_DteFlag_Type.__name__ = "Integer32"
_X25Profile_DteFlag_Object = MibScalar
x25Profile_DteFlag = _X25Profile_DteFlag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 36),
    _X25Profile_DteFlag_Type()
)
x25Profile_DteFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_DteFlag.setStatus("mandatory")


class _X25Profile_NetType_Type(Integer32):
    """Custom type x25Profile_NetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccitt", 1),
          ("ddn", 2))
    )


_X25Profile_NetType_Type.__name__ = "Integer32"
_X25Profile_NetType_Object = MibScalar
x25Profile_NetType = _X25Profile_NetType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 37),
    _X25Profile_NetType_Type()
)
x25Profile_NetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_NetType.setStatus("mandatory")


class _X25Profile_oDiscMode_Type(Integer32):
    """Custom type x25Profile_oDiscMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passive", 1))
    )


_X25Profile_oDiscMode_Type.__name__ = "Integer32"
_X25Profile_oDiscMode_Object = MibScalar
x25Profile_oDiscMode = _X25Profile_oDiscMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 38),
    _X25Profile_oDiscMode_Type()
)
x25Profile_oDiscMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_oDiscMode.setStatus("mandatory")


class _X25Profile_oSeqNumbers_Type(Integer32):
    """Custom type x25Profile_oSeqNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("normal", 1))
    )


_X25Profile_oSeqNumbers_Type.__name__ = "Integer32"
_X25Profile_oSeqNumbers_Object = MibScalar
x25Profile_oSeqNumbers = _X25Profile_oSeqNumbers_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 39),
    _X25Profile_oSeqNumbers_Type()
)
x25Profile_oSeqNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_oSeqNumbers.setStatus("mandatory")


class _X25Profile_ReverseChargeAcceptance_Type(Integer32):
    """Custom type x25Profile_ReverseChargeAcceptance based on Integer32"""
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


_X25Profile_ReverseChargeAcceptance_Type.__name__ = "Integer32"
_X25Profile_ReverseChargeAcceptance_Object = MibScalar
x25Profile_ReverseChargeAcceptance = _X25Profile_ReverseChargeAcceptance_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 40),
    _X25Profile_ReverseChargeAcceptance_Type()
)
x25Profile_ReverseChargeAcceptance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_ReverseChargeAcceptance.setStatus("mandatory")
_X25Profile_oVceTimerVal_Type = Integer32
_X25Profile_oVceTimerVal_Object = MibScalar
x25Profile_oVceTimerVal = _X25Profile_oVceTimerVal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 41),
    _X25Profile_oVceTimerVal_Type()
)
x25Profile_oVceTimerVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_oVceTimerVal.setStatus("mandatory")
_X25Profile_oX25DTeiValue_Type = Integer32
_X25Profile_oX25DTeiValue_Object = MibScalar
x25Profile_oX25DTeiValue = _X25Profile_oX25DTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 42),
    _X25Profile_oX25DTeiValue_Type()
)
x25Profile_oX25DTeiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_oX25DTeiValue.setStatus("mandatory")
_X25Profile_oPriNumberValue_Type = DisplayString
_X25Profile_oPriNumberValue_Object = MibScalar
x25Profile_oPriNumberValue = _X25Profile_oPriNumberValue_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 43),
    _X25Profile_oPriNumberValue_Type()
)
x25Profile_oPriNumberValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_oPriNumberValue.setStatus("mandatory")


class _X25Profile_Action_o_Type(Integer32):
    """Custom type x25Profile_Action_o based on Integer32"""
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


_X25Profile_Action_o_Type.__name__ = "Integer32"
_X25Profile_Action_o_Object = MibScalar
x25Profile_Action_o = _X25Profile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 44),
    _X25Profile_Action_o_Type()
)
x25Profile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_Action_o.setStatus("mandatory")
_X25Profile_IdleVal_Type = Integer32
_X25Profile_IdleVal_Object = MibScalar
x25Profile_IdleVal = _X25Profile_IdleVal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 45),
    _X25Profile_IdleVal_Type()
)
x25Profile_IdleVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_IdleVal.setStatus("mandatory")
_X25Profile_Maxwinsize_Type = Integer32
_X25Profile_Maxwinsize_Object = MibScalar
x25Profile_Maxwinsize = _X25Profile_Maxwinsize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 46),
    _X25Profile_Maxwinsize_Type()
)
x25Profile_Maxwinsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_Maxwinsize.setStatus("mandatory")
_X25Profile_Defwinsize_Type = Integer32
_X25Profile_Defwinsize_Object = MibScalar
x25Profile_Defwinsize = _X25Profile_Defwinsize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 47),
    _X25Profile_Defwinsize_Type()
)
x25Profile_Defwinsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_Defwinsize.setStatus("mandatory")


class _X25Profile_Defpktsize_Type(Integer32):
    """Custom type x25Profile_Defpktsize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("n-10", 11),
          ("n-11", 12),
          ("n-12", 13),
          ("n-6", 7),
          ("n-7", 8),
          ("n-8", 9),
          ("n-9", 10))
    )


_X25Profile_Defpktsize_Type.__name__ = "Integer32"
_X25Profile_Defpktsize_Object = MibScalar
x25Profile_Defpktsize = _X25Profile_Defpktsize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 48),
    _X25Profile_Defpktsize_Type()
)
x25Profile_Defpktsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_Defpktsize.setStatus("mandatory")


class _X25Profile_Pktdiag_Type(Integer32):
    """Custom type x25Profile_Pktdiag based on Integer32"""
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


_X25Profile_Pktdiag_Type.__name__ = "Integer32"
_X25Profile_Pktdiag_Object = MibScalar
x25Profile_Pktdiag = _X25Profile_Pktdiag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 49),
    _X25Profile_Pktdiag_Type()
)
x25Profile_Pktdiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_Pktdiag.setStatus("mandatory")
_X25Profile_X25SrcAddress_Type = DisplayString
_X25Profile_X25SrcAddress_Object = MibScalar
x25Profile_X25SrcAddress = _X25Profile_X25SrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 50),
    _X25Profile_X25SrcAddress_Type()
)
x25Profile_X25SrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_X25SrcAddress.setStatus("mandatory")


class _X25Profile_ClosedUserGroups_Type(Integer32):
    """Custom type x25Profile_ClosedUserGroups based on Integer32"""
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
        *(("noiob", 2),
          ("noioe", 3),
          ("none", 1),
          ("oab", 6),
          ("oae", 7),
          ("prefb", 4),
          ("prefe", 5))
    )


_X25Profile_ClosedUserGroups_Type.__name__ = "Integer32"
_X25Profile_ClosedUserGroups_Object = MibScalar
x25Profile_ClosedUserGroups = _X25Profile_ClosedUserGroups_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 140, 1, 1, 51),
    _X25Profile_ClosedUserGroups_Type()
)
x25Profile_ClosedUserGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Profile_ClosedUserGroups.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBX25-MIB",
    **{"DisplayString": DisplayString,
       "mibx25Profile": mibx25Profile,
       "mibx25ProfileTable": mibx25ProfileTable,
       "mibx25ProfileEntry": mibx25ProfileEntry,
       "x25Profile-X25Name": x25Profile_X25Name,
       "x25Profile-Active": x25Profile_Active,
       "x25Profile-Kludge": x25Profile_Kludge,
       "x25Profile-NailedUpGroup": x25Profile_NailedUpGroup,
       "x25Profile-NailedMode": x25Profile_NailedMode,
       "x25Profile-CalledNumberType": x25Profile_CalledNumberType,
       "x25Profile-SwitchedCallType": x25Profile_SwitchedCallType,
       "x25Profile-PhoneNumber": x25Profile_PhoneNumber,
       "x25Profile-BillingNumber": x25Profile_BillingNumber,
       "x25Profile-TransitNumber": x25Profile_TransitNumber,
       "x25Profile-CallByCallId": x25Profile_CallByCallId,
       "x25Profile-oT1Val": x25Profile_oT1Val,
       "x25Profile-oT2Val": x25Profile_oT2Val,
       "x25Profile-oN2Val": x25Profile_oN2Val,
       "x25Profile-KVal": x25Profile_KVal,
       "x25Profile-oPktWindow": x25Profile_oPktWindow,
       "x25Profile-oPktSize": x25Profile_oPktSize,
       "x25Profile-oMinPktSize": x25Profile_oMinPktSize,
       "x25Profile-oMaxPktSize": x25Profile_oMaxPktSize,
       "x25Profile-LowestPVC": x25Profile_LowestPVC,
       "x25Profile-HighestPVC": x25Profile_HighestPVC,
       "x25Profile-LowestSVC": x25Profile_LowestSVC,
       "x25Profile-HighestSVC": x25Profile_HighestSVC,
       "x25Profile-ClearDiag": x25Profile_ClearDiag,
       "x25Profile-ResetDiag": x25Profile_ResetDiag,
       "x25Profile-RestartDiag": x25Profile_RestartDiag,
       "x25Profile-PktOptions": x25Profile_PktOptions,
       "x25Profile-PktT20": x25Profile_PktT20,
       "x25Profile-PktR20": x25Profile_PktR20,
       "x25Profile-PktT21": x25Profile_PktT21,
       "x25Profile-PktT22": x25Profile_PktT22,
       "x25Profile-PktR22": x25Profile_PktR22,
       "x25Profile-PktT23": x25Profile_PktT23,
       "x25Profile-PktR23": x25Profile_PktR23,
       "x25Profile-DteFlag": x25Profile_DteFlag,
       "x25Profile-NetType": x25Profile_NetType,
       "x25Profile-oDiscMode": x25Profile_oDiscMode,
       "x25Profile-oSeqNumbers": x25Profile_oSeqNumbers,
       "x25Profile-ReverseChargeAcceptance": x25Profile_ReverseChargeAcceptance,
       "x25Profile-oVceTimerVal": x25Profile_oVceTimerVal,
       "x25Profile-oX25DTeiValue": x25Profile_oX25DTeiValue,
       "x25Profile-oPriNumberValue": x25Profile_oPriNumberValue,
       "x25Profile-Action-o": x25Profile_Action_o,
       "x25Profile-IdleVal": x25Profile_IdleVal,
       "x25Profile-Maxwinsize": x25Profile_Maxwinsize,
       "x25Profile-Defwinsize": x25Profile_Defwinsize,
       "x25Profile-Defpktsize": x25Profile_Defpktsize,
       "x25Profile-Pktdiag": x25Profile_Pktdiag,
       "x25Profile-X25SrcAddress": x25Profile_X25SrcAddress,
       "x25Profile-ClosedUserGroups": x25Profile_ClosedUserGroups}
)
