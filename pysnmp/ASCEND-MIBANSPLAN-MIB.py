# SNMP MIB module (ASCEND-MIBANSPLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBANSPLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:02 2024
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

_MibanswerPlanProfile_ObjectIdentity = ObjectIdentity
mibanswerPlanProfile = _MibanswerPlanProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 34)
)
_MibanswerPlanProfileTable_Object = MibTable
mibanswerPlanProfileTable = _MibanswerPlanProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 34, 1)
)
if mibBuilder.loadTexts:
    mibanswerPlanProfileTable.setStatus("mandatory")
_MibanswerPlanProfileEntry_Object = MibTableRow
mibanswerPlanProfileEntry = _MibanswerPlanProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1)
)
mibanswerPlanProfileEntry.setIndexNames(
    (0, "ASCEND-MIBANSPLAN-MIB", "answerPlanProfile-Name"),
)
if mibBuilder.loadTexts:
    mibanswerPlanProfileEntry.setStatus("mandatory")
_AnswerPlanProfile_Name_Type = DisplayString
_AnswerPlanProfile_Name_Object = MibScalar
answerPlanProfile_Name = _AnswerPlanProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1, 1),
    _AnswerPlanProfile_Name_Type()
)
answerPlanProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    answerPlanProfile_Name.setStatus("mandatory")
_AnswerPlanProfile_AnswerNumber_Type = DisplayString
_AnswerPlanProfile_AnswerNumber_Object = MibScalar
answerPlanProfile_AnswerNumber = _AnswerPlanProfile_AnswerNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1, 2),
    _AnswerPlanProfile_AnswerNumber_Type()
)
answerPlanProfile_AnswerNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerPlanProfile_AnswerNumber.setStatus("mandatory")


class _AnswerPlanProfile_AnswerCallType_Type(Integer32):
    """Custom type answerPlanProfile_AnswerCallType based on Integer32"""
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


_AnswerPlanProfile_AnswerCallType_Type.__name__ = "Integer32"
_AnswerPlanProfile_AnswerCallType_Object = MibScalar
answerPlanProfile_AnswerCallType = _AnswerPlanProfile_AnswerCallType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1, 3),
    _AnswerPlanProfile_AnswerCallType_Type()
)
answerPlanProfile_AnswerCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerPlanProfile_AnswerCallType.setStatus("mandatory")
_AnswerPlanProfile_DestChanGroup_Type = Integer32
_AnswerPlanProfile_DestChanGroup_Object = MibScalar
answerPlanProfile_DestChanGroup = _AnswerPlanProfile_DestChanGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1, 4),
    _AnswerPlanProfile_DestChanGroup_Type()
)
answerPlanProfile_DestChanGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerPlanProfile_DestChanGroup.setStatus("mandatory")
_AnswerPlanProfile_DialPlanNumber_Type = Integer32
_AnswerPlanProfile_DialPlanNumber_Object = MibScalar
answerPlanProfile_DialPlanNumber = _AnswerPlanProfile_DialPlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1, 5),
    _AnswerPlanProfile_DialPlanNumber_Type()
)
answerPlanProfile_DialPlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerPlanProfile_DialPlanNumber.setStatus("mandatory")


class _AnswerPlanProfile_Action_o_Type(Integer32):
    """Custom type answerPlanProfile_Action_o based on Integer32"""
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


_AnswerPlanProfile_Action_o_Type.__name__ = "Integer32"
_AnswerPlanProfile_Action_o_Object = MibScalar
answerPlanProfile_Action_o = _AnswerPlanProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 34, 1, 1, 6),
    _AnswerPlanProfile_Action_o_Type()
)
answerPlanProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerPlanProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBANSPLAN-MIB",
    **{"DisplayString": DisplayString,
       "mibanswerPlanProfile": mibanswerPlanProfile,
       "mibanswerPlanProfileTable": mibanswerPlanProfileTable,
       "mibanswerPlanProfileEntry": mibanswerPlanProfileEntry,
       "answerPlanProfile-Name": answerPlanProfile_Name,
       "answerPlanProfile-AnswerNumber": answerPlanProfile_AnswerNumber,
       "answerPlanProfile-AnswerCallType": answerPlanProfile_AnswerCallType,
       "answerPlanProfile-DestChanGroup": answerPlanProfile_DestChanGroup,
       "answerPlanProfile-DialPlanNumber": answerPlanProfile_DialPlanNumber,
       "answerPlanProfile-Action-o": answerPlanProfile_Action_o}
)
