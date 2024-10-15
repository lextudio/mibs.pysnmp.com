# SNMP MIB module (AIX1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIX1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:27 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class IfIndexType(Integer32):
    """Custom type IfIndexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSystemOID_ObjectIdentity = ObjectIdentity
aiSystemOID = _AiSystemOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2)
)
_Ai192_ObjectIdentity = ObjectIdentity
ai192 = _Ai192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192)
)
_Ai192Ver7_ObjectIdentity = ObjectIdentity
ai192Ver7 = _Ai192Ver7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7)
)
_Ai192Ver70_ObjectIdentity = ObjectIdentity
ai192Ver70 = _Ai192Ver70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 0)
)
_Ai192Ver708_ObjectIdentity = ObjectIdentity
ai192Ver708 = _Ai192Ver708_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 0, 8)
)
_Ai192Ver709_ObjectIdentity = ObjectIdentity
ai192Ver709 = _Ai192Ver709_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 0, 9)
)
_Ai192Ver71_ObjectIdentity = ObjectIdentity
ai192Ver71 = _Ai192Ver71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 1)
)
_Ai192Ver710_ObjectIdentity = ObjectIdentity
ai192Ver710 = _Ai192Ver710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 1, 0)
)
_Ai192Ver711_ObjectIdentity = ObjectIdentity
ai192Ver711 = _Ai192Ver711_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 1, 1)
)
_Ai192Ver72_ObjectIdentity = ObjectIdentity
ai192Ver72 = _Ai192Ver72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 2)
)
_Ai192Ver720_ObjectIdentity = ObjectIdentity
ai192Ver720 = _Ai192Ver720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 2, 0)
)
_Ai192Ver721_ObjectIdentity = ObjectIdentity
ai192Ver721 = _Ai192Ver721_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 2, 1)
)
_Ai192Ver77_ObjectIdentity = ObjectIdentity
ai192Ver77 = _Ai192Ver77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 192, 7, 7)
)
_Ai196_ObjectIdentity = ObjectIdentity
ai196 = _Ai196_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196)
)
_Ai196Ver7_ObjectIdentity = ObjectIdentity
ai196Ver7 = _Ai196Ver7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7)
)
_Ai196Ver70_ObjectIdentity = ObjectIdentity
ai196Ver70 = _Ai196Ver70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 0)
)
_Ai196Ver708_ObjectIdentity = ObjectIdentity
ai196Ver708 = _Ai196Ver708_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 0, 8)
)
_Ai196Ver709_ObjectIdentity = ObjectIdentity
ai196Ver709 = _Ai196Ver709_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 0, 9)
)
_Ai196Ver71_ObjectIdentity = ObjectIdentity
ai196Ver71 = _Ai196Ver71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 1)
)
_Ai196Ver710_ObjectIdentity = ObjectIdentity
ai196Ver710 = _Ai196Ver710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 1, 0)
)
_Ai196Ver711_ObjectIdentity = ObjectIdentity
ai196Ver711 = _Ai196Ver711_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 1, 1)
)
_Ai196Ver72_ObjectIdentity = ObjectIdentity
ai196Ver72 = _Ai196Ver72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 2)
)
_Ai196Ver720_ObjectIdentity = ObjectIdentity
ai196Ver720 = _Ai196Ver720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 2, 0)
)
_Ai196Ver721_ObjectIdentity = ObjectIdentity
ai196Ver721 = _Ai196Ver721_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 2, 1)
)
_Ai196Ver77_ObjectIdentity = ObjectIdentity
ai196Ver77 = _Ai196Ver77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 196, 7, 7)
)
_AiX1_ObjectIdentity = ObjectIdentity
aiX1 = _AiX1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12)
)
_AiX1System_ObjectIdentity = ObjectIdentity
aiX1System = _AiX1System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12, 1)
)


class _Aix1AdminGbufXoffThreshold_Type(Integer32):
    """Custom type aix1AdminGbufXoffThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Aix1AdminGbufXoffThreshold_Type.__name__ = "Integer32"
_Aix1AdminGbufXoffThreshold_Object = MibScalar
aix1AdminGbufXoffThreshold = _Aix1AdminGbufXoffThreshold_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 1),
    _Aix1AdminGbufXoffThreshold_Type()
)
aix1AdminGbufXoffThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1AdminGbufXoffThreshold.setStatus("mandatory")


class _Aix1AdminGbufRecovThreshold_Type(Integer32):
    """Custom type aix1AdminGbufRecovThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Aix1AdminGbufRecovThreshold_Type.__name__ = "Integer32"
_Aix1AdminGbufRecovThreshold_Object = MibScalar
aix1AdminGbufRecovThreshold = _Aix1AdminGbufRecovThreshold_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 2),
    _Aix1AdminGbufRecovThreshold_Type()
)
aix1AdminGbufRecovThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1AdminGbufRecovThreshold.setStatus("mandatory")


class _Aix1AdminRollover_Type(Integer32):
    """Custom type aix1AdminRollover based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("roll", 2))
    )


_Aix1AdminRollover_Type.__name__ = "Integer32"
_Aix1AdminRollover_Object = MibScalar
aix1AdminRollover = _Aix1AdminRollover_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 3),
    _Aix1AdminRollover_Type()
)
aix1AdminRollover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1AdminRollover.setStatus("mandatory")


class _Aix1Bx25AdminCallDown_Type(Integer32):
    """Custom type aix1Bx25AdminCallDown based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Aix1Bx25AdminCallDown_Type.__name__ = "Integer32"
_Aix1Bx25AdminCallDown_Object = MibScalar
aix1Bx25AdminCallDown = _Aix1Bx25AdminCallDown_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 4),
    _Aix1Bx25AdminCallDown_Type()
)
aix1Bx25AdminCallDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1Bx25AdminCallDown.setStatus("mandatory")


class _Aix1Bx25AdminDMlock_Type(Integer32):
    """Custom type aix1Bx25AdminDMlock based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 4294967295),
    )


_Aix1Bx25AdminDMlock_Type.__name__ = "Integer32"
_Aix1Bx25AdminDMlock_Object = MibScalar
aix1Bx25AdminDMlock = _Aix1Bx25AdminDMlock_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 5),
    _Aix1Bx25AdminDMlock_Type()
)
aix1Bx25AdminDMlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1Bx25AdminDMlock.setStatus("mandatory")


class _Aix1Bx25AdminLinkUp_Type(Integer32):
    """Custom type aix1Bx25AdminLinkUp based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 4294967295),
    )


_Aix1Bx25AdminLinkUp_Type.__name__ = "Integer32"
_Aix1Bx25AdminLinkUp_Object = MibScalar
aix1Bx25AdminLinkUp = _Aix1Bx25AdminLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 6),
    _Aix1Bx25AdminLinkUp_Type()
)
aix1Bx25AdminLinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1Bx25AdminLinkUp.setStatus("mandatory")
_Aix1StatErrX25InData_Type = Counter32
_Aix1StatErrX25InData_Object = MibScalar
aix1StatErrX25InData = _Aix1StatErrX25InData_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 7),
    _Aix1StatErrX25InData_Type()
)
aix1StatErrX25InData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatErrX25InData.setStatus("mandatory")
_Aix1StatErrX25OutData_Type = Counter32
_Aix1StatErrX25OutData_Object = MibScalar
aix1StatErrX25OutData = _Aix1StatErrX25OutData_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 8),
    _Aix1StatErrX25OutData_Type()
)
aix1StatErrX25OutData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatErrX25OutData.setStatus("mandatory")
_Aix1StatErrX25OutPkt_Type = Counter32
_Aix1StatErrX25OutPkt_Object = MibScalar
aix1StatErrX25OutPkt = _Aix1StatErrX25OutPkt_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 9),
    _Aix1StatErrX25OutPkt_Type()
)
aix1StatErrX25OutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatErrX25OutPkt.setStatus("mandatory")
_Aix1StatErrX25OutChoked_Type = Counter32
_Aix1StatErrX25OutChoked_Object = MibScalar
aix1StatErrX25OutChoked = _Aix1StatErrX25OutChoked_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 10),
    _Aix1StatErrX25OutChoked_Type()
)
aix1StatErrX25OutChoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatErrX25OutChoked.setStatus("mandatory")
_Aix1StatErrPlogCount_Type = Counter32
_Aix1StatErrPlogCount_Object = MibScalar
aix1StatErrPlogCount = _Aix1StatErrPlogCount_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 11),
    _Aix1StatErrPlogCount_Type()
)
aix1StatErrPlogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatErrPlogCount.setStatus("mandatory")
_Aix1StatErrGfctlXoffs_Type = Counter32
_Aix1StatErrGfctlXoffs_Object = MibScalar
aix1StatErrGfctlXoffs = _Aix1StatErrGfctlXoffs_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 12),
    _Aix1StatErrGfctlXoffs_Type()
)
aix1StatErrGfctlXoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatErrGfctlXoffs.setStatus("mandatory")
_Aix1StatErrGfctlDiscards_Type = Counter32
_Aix1StatErrGfctlDiscards_Object = MibScalar
aix1StatErrGfctlDiscards = _Aix1StatErrGfctlDiscards_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 13),
    _Aix1StatErrGfctlDiscards_Type()
)
aix1StatErrGfctlDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatErrGfctlDiscards.setStatus("mandatory")
_Aix1StatErrUwteBadTrans_Type = Counter32
_Aix1StatErrUwteBadTrans_Object = MibScalar
aix1StatErrUwteBadTrans = _Aix1StatErrUwteBadTrans_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 14),
    _Aix1StatErrUwteBadTrans_Type()
)
aix1StatErrUwteBadTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatErrUwteBadTrans.setStatus("mandatory")
_Aix1StatErrUwteBadFlds_Type = Counter32
_Aix1StatErrUwteBadFlds_Object = MibScalar
aix1StatErrUwteBadFlds = _Aix1StatErrUwteBadFlds_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 15),
    _Aix1StatErrUwteBadFlds_Type()
)
aix1StatErrUwteBadFlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatErrUwteBadFlds.setStatus("mandatory")
_Aix1StatErrUwteMissingFlds_Type = Counter32
_Aix1StatErrUwteMissingFlds_Object = MibScalar
aix1StatErrUwteMissingFlds = _Aix1StatErrUwteMissingFlds_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 16),
    _Aix1StatErrUwteMissingFlds_Type()
)
aix1StatErrUwteMissingFlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatErrUwteMissingFlds.setStatus("mandatory")
_Aix1StatErrLogOutLost_Type = Counter32
_Aix1StatErrLogOutLost_Object = MibScalar
aix1StatErrLogOutLost = _Aix1StatErrLogOutLost_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 17),
    _Aix1StatErrLogOutLost_Type()
)
aix1StatErrLogOutLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatErrLogOutLost.setStatus("mandatory")
_Aix1StatErrVcMuxErrs_Type = Counter32
_Aix1StatErrVcMuxErrs_Object = MibScalar
aix1StatErrVcMuxErrs = _Aix1StatErrVcMuxErrs_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 18),
    _Aix1StatErrVcMuxErrs_Type()
)
aix1StatErrVcMuxErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatErrVcMuxErrs.setStatus("mandatory")
_Aix1StatErrEmptyPktsRcv_Type = Counter32
_Aix1StatErrEmptyPktsRcv_Object = MibScalar
aix1StatErrEmptyPktsRcv = _Aix1StatErrEmptyPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 19),
    _Aix1StatErrEmptyPktsRcv_Type()
)
aix1StatErrEmptyPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatErrEmptyPktsRcv.setStatus("mandatory")
_Aix1StatInCharsPerSec80s_Type = Counter32
_Aix1StatInCharsPerSec80s_Object = MibScalar
aix1StatInCharsPerSec80s = _Aix1StatInCharsPerSec80s_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 20),
    _Aix1StatInCharsPerSec80s_Type()
)
aix1StatInCharsPerSec80s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatInCharsPerSec80s.setStatus("mandatory")
_Aix1StatOutCharsPerSec80s_Type = Counter32
_Aix1StatOutCharsPerSec80s_Object = MibScalar
aix1StatOutCharsPerSec80s = _Aix1StatOutCharsPerSec80s_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 1, 21),
    _Aix1StatOutCharsPerSec80s_Type()
)
aix1StatOutCharsPerSec80s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1StatOutCharsPerSec80s.setStatus("mandatory")
_AiX1Appl_ObjectIdentity = ObjectIdentity
aiX1Appl = _AiX1Appl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12, 2)
)
_Aix1ApplAdminTable_Object = MibTable
aix1ApplAdminTable = _Aix1ApplAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 1)
)
if mibBuilder.loadTexts:
    aix1ApplAdminTable.setStatus("mandatory")
_Aix1ApplAdminEntry_Object = MibTableRow
aix1ApplAdminEntry = _Aix1ApplAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 1, 1)
)
aix1ApplAdminEntry.setIndexNames(
    (0, "AIX1-MIB", "aix1ApplAdminIndex"),
)
if mibBuilder.loadTexts:
    aix1ApplAdminEntry.setStatus("mandatory")
_Aix1ApplAdminIndex_Type = IfIndexType
_Aix1ApplAdminIndex_Object = MibTableColumn
aix1ApplAdminIndex = _Aix1ApplAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 1, 1, 1),
    _Aix1ApplAdminIndex_Type()
)
aix1ApplAdminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1ApplAdminIndex.setStatus("mandatory")


class _Aix1ApplAdminLinkStart_Type(Integer32):
    """Custom type aix1ApplAdminLinkStart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("started", 1),
          ("stopped", 2))
    )


_Aix1ApplAdminLinkStart_Type.__name__ = "Integer32"
_Aix1ApplAdminLinkStart_Object = MibTableColumn
aix1ApplAdminLinkStart = _Aix1ApplAdminLinkStart_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 1, 1, 2),
    _Aix1ApplAdminLinkStart_Type()
)
aix1ApplAdminLinkStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1ApplAdminLinkStart.setStatus("mandatory")


class _Aix1ApplAdminLinkMode_Type(Integer32):
    """Custom type aix1ApplAdminLinkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("passive", 2))
    )


_Aix1ApplAdminLinkMode_Type.__name__ = "Integer32"
_Aix1ApplAdminLinkMode_Object = MibTableColumn
aix1ApplAdminLinkMode = _Aix1ApplAdminLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 1, 1, 3),
    _Aix1ApplAdminLinkMode_Type()
)
aix1ApplAdminLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1ApplAdminLinkMode.setStatus("mandatory")


class _Aix1ApplAdminResetErrs_Type(Integer32):
    """Custom type aix1ApplAdminResetErrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("resetCounters", 2))
    )


_Aix1ApplAdminResetErrs_Type.__name__ = "Integer32"
_Aix1ApplAdminResetErrs_Object = MibTableColumn
aix1ApplAdminResetErrs = _Aix1ApplAdminResetErrs_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 1, 1, 4),
    _Aix1ApplAdminResetErrs_Type()
)
aix1ApplAdminResetErrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1ApplAdminResetErrs.setStatus("mandatory")


class _Aix1ApplAdminXONXOFFProto_Type(Integer32):
    """Custom type aix1ApplAdminXONXOFFProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Aix1ApplAdminXONXOFFProto_Type.__name__ = "Integer32"
_Aix1ApplAdminXONXOFFProto_Object = MibTableColumn
aix1ApplAdminXONXOFFProto = _Aix1ApplAdminXONXOFFProto_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 1, 1, 5),
    _Aix1ApplAdminXONXOFFProto_Type()
)
aix1ApplAdminXONXOFFProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1ApplAdminXONXOFFProto.setStatus("mandatory")


class _Aix1ApplAdminNMAProto_Type(Integer32):
    """Custom type aix1ApplAdminNMAProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Aix1ApplAdminNMAProto_Type.__name__ = "Integer32"
_Aix1ApplAdminNMAProto_Object = MibTableColumn
aix1ApplAdminNMAProto = _Aix1ApplAdminNMAProto_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 1, 1, 6),
    _Aix1ApplAdminNMAProto_Type()
)
aix1ApplAdminNMAProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1ApplAdminNMAProto.setStatus("mandatory")


class _Aix1ApplAdminOPSINEProto_Type(Integer32):
    """Custom type aix1ApplAdminOPSINEProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Aix1ApplAdminOPSINEProto_Type.__name__ = "Integer32"
_Aix1ApplAdminOPSINEProto_Object = MibTableColumn
aix1ApplAdminOPSINEProto = _Aix1ApplAdminOPSINEProto_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 1, 1, 7),
    _Aix1ApplAdminOPSINEProto_Type()
)
aix1ApplAdminOPSINEProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1ApplAdminOPSINEProto.setStatus("mandatory")


class _Aix1ApplAdminTL1Proto_Type(Integer32):
    """Custom type aix1ApplAdminTL1Proto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Aix1ApplAdminTL1Proto_Type.__name__ = "Integer32"
_Aix1ApplAdminTL1Proto_Object = MibTableColumn
aix1ApplAdminTL1Proto = _Aix1ApplAdminTL1Proto_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 1, 1, 8),
    _Aix1ApplAdminTL1Proto_Type()
)
aix1ApplAdminTL1Proto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1ApplAdminTL1Proto.setStatus("mandatory")


class _Aix1ApplAdminLinkDescription_Type(DisplayString):
    """Custom type aix1ApplAdminLinkDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Aix1ApplAdminLinkDescription_Type.__name__ = "DisplayString"
_Aix1ApplAdminLinkDescription_Object = MibTableColumn
aix1ApplAdminLinkDescription = _Aix1ApplAdminLinkDescription_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 1, 1, 9),
    _Aix1ApplAdminLinkDescription_Type()
)
aix1ApplAdminLinkDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1ApplAdminLinkDescription.setStatus("mandatory")


class _Aix1ApplAdminLinkConnectionMode_Type(Integer32):
    """Custom type aix1ApplAdminLinkConnectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disabled", 4),
          ("disconnected", 2))
    )


_Aix1ApplAdminLinkConnectionMode_Type.__name__ = "Integer32"
_Aix1ApplAdminLinkConnectionMode_Object = MibTableColumn
aix1ApplAdminLinkConnectionMode = _Aix1ApplAdminLinkConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 1, 1, 10),
    _Aix1ApplAdminLinkConnectionMode_Type()
)
aix1ApplAdminLinkConnectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1ApplAdminLinkConnectionMode.setStatus("mandatory")
_Aix1ApplOperTable_Object = MibTable
aix1ApplOperTable = _Aix1ApplOperTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 2)
)
if mibBuilder.loadTexts:
    aix1ApplOperTable.setStatus("mandatory")
_Aix1ApplOperEntry_Object = MibTableRow
aix1ApplOperEntry = _Aix1ApplOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 2, 1)
)
aix1ApplOperEntry.setIndexNames(
    (0, "AIX1-MIB", "aix1ApplOperIndex"),
)
if mibBuilder.loadTexts:
    aix1ApplOperEntry.setStatus("mandatory")
_Aix1ApplOperIndex_Type = IfIndexType
_Aix1ApplOperIndex_Object = MibTableColumn
aix1ApplOperIndex = _Aix1ApplOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 2, 1, 1),
    _Aix1ApplOperIndex_Type()
)
aix1ApplOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1ApplOperIndex.setStatus("mandatory")


class _Aix1ApplOperLinkMode_Type(Integer32):
    """Custom type aix1ApplOperLinkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("passive", 2))
    )


_Aix1ApplOperLinkMode_Type.__name__ = "Integer32"
_Aix1ApplOperLinkMode_Object = MibTableColumn
aix1ApplOperLinkMode = _Aix1ApplOperLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 2, 1, 2),
    _Aix1ApplOperLinkMode_Type()
)
aix1ApplOperLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1ApplOperLinkMode.setStatus("mandatory")


class _Aix1ApplOperXONXOFFProto_Type(Integer32):
    """Custom type aix1ApplOperXONXOFFProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Aix1ApplOperXONXOFFProto_Type.__name__ = "Integer32"
_Aix1ApplOperXONXOFFProto_Object = MibTableColumn
aix1ApplOperXONXOFFProto = _Aix1ApplOperXONXOFFProto_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 2, 1, 3),
    _Aix1ApplOperXONXOFFProto_Type()
)
aix1ApplOperXONXOFFProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1ApplOperXONXOFFProto.setStatus("mandatory")


class _Aix1ApplOperNMAProto_Type(Integer32):
    """Custom type aix1ApplOperNMAProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Aix1ApplOperNMAProto_Type.__name__ = "Integer32"
_Aix1ApplOperNMAProto_Object = MibTableColumn
aix1ApplOperNMAProto = _Aix1ApplOperNMAProto_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 2, 1, 4),
    _Aix1ApplOperNMAProto_Type()
)
aix1ApplOperNMAProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1ApplOperNMAProto.setStatus("mandatory")


class _Aix1ApplOperOPSINEProto_Type(Integer32):
    """Custom type aix1ApplOperOPSINEProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Aix1ApplOperOPSINEProto_Type.__name__ = "Integer32"
_Aix1ApplOperOPSINEProto_Object = MibTableColumn
aix1ApplOperOPSINEProto = _Aix1ApplOperOPSINEProto_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 2, 1, 6),
    _Aix1ApplOperOPSINEProto_Type()
)
aix1ApplOperOPSINEProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1ApplOperOPSINEProto.setStatus("mandatory")


class _Aix1ApplOperTL1Proto_Type(Integer32):
    """Custom type aix1ApplOperTL1Proto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Aix1ApplOperTL1Proto_Type.__name__ = "Integer32"
_Aix1ApplOperTL1Proto_Object = MibTableColumn
aix1ApplOperTL1Proto = _Aix1ApplOperTL1Proto_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 2, 1, 7),
    _Aix1ApplOperTL1Proto_Type()
)
aix1ApplOperTL1Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1ApplOperTL1Proto.setStatus("mandatory")


class _Aix1ApplOperLinkDescription_Type(DisplayString):
    """Custom type aix1ApplOperLinkDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Aix1ApplOperLinkDescription_Type.__name__ = "DisplayString"
_Aix1ApplOperLinkDescription_Object = MibTableColumn
aix1ApplOperLinkDescription = _Aix1ApplOperLinkDescription_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 2, 1, 8),
    _Aix1ApplOperLinkDescription_Type()
)
aix1ApplOperLinkDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1ApplOperLinkDescription.setStatus("mandatory")


class _Aix1ApplOperLinkConnectionMode_Type(Integer32):
    """Custom type aix1ApplOperLinkConnectionMode based on Integer32"""
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
        *(("connected", 1),
          ("disabled", 4),
          ("disconnected", 2),
          ("linkdown", 5),
          ("linkup", 6),
          ("reconnected", 3))
    )


_Aix1ApplOperLinkConnectionMode_Type.__name__ = "Integer32"
_Aix1ApplOperLinkConnectionMode_Object = MibTableColumn
aix1ApplOperLinkConnectionMode = _Aix1ApplOperLinkConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 2, 2, 1, 9),
    _Aix1ApplOperLinkConnectionMode_Type()
)
aix1ApplOperLinkConnectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1ApplOperLinkConnectionMode.setStatus("mandatory")
_AiX1Pkt_ObjectIdentity = ObjectIdentity
aiX1Pkt = _AiX1Pkt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12, 3)
)
_Aix1PktAdminTable_Object = MibTable
aix1PktAdminTable = _Aix1PktAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1)
)
if mibBuilder.loadTexts:
    aix1PktAdminTable.setStatus("mandatory")
_Aix1PktAdminEntry_Object = MibTableRow
aix1PktAdminEntry = _Aix1PktAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1)
)
aix1PktAdminEntry.setIndexNames(
    (0, "AIX1-MIB", "aix1PktAdminIndex"),
)
if mibBuilder.loadTexts:
    aix1PktAdminEntry.setStatus("mandatory")
_Aix1PktAdminIndex_Type = IfIndexType
_Aix1PktAdminIndex_Object = MibTableColumn
aix1PktAdminIndex = _Aix1PktAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 1),
    _Aix1PktAdminIndex_Type()
)
aix1PktAdminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktAdminIndex.setStatus("mandatory")


class _Aix1PktAdminConformanceMode_Type(Integer32):
    """Custom type aix1PktAdminConformanceMode based on Integer32"""
    defaultValue = 1

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


_Aix1PktAdminConformanceMode_Type.__name__ = "Integer32"
_Aix1PktAdminConformanceMode_Object = MibTableColumn
aix1PktAdminConformanceMode = _Aix1PktAdminConformanceMode_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 2),
    _Aix1PktAdminConformanceMode_Type()
)
aix1PktAdminConformanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminConformanceMode.setStatus("mandatory")


class _Aix1PktAdminDBit_Type(Integer32):
    """Custom type aix1PktAdminDBit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dbitAllowed", 2),
          ("dbitNotAllowed", 1))
    )


_Aix1PktAdminDBit_Type.__name__ = "Integer32"
_Aix1PktAdminDBit_Object = MibTableColumn
aix1PktAdminDBit = _Aix1PktAdminDBit_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 3),
    _Aix1PktAdminDBit_Type()
)
aix1PktAdminDBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminDBit.setStatus("mandatory")


class _Aix1PktAdminQBitMBit_Type(Integer32):
    """Custom type aix1PktAdminQBitMBit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noQMCheck", 1),
          ("qmCheck", 2))
    )


_Aix1PktAdminQBitMBit_Type.__name__ = "Integer32"
_Aix1PktAdminQBitMBit_Object = MibTableColumn
aix1PktAdminQBitMBit = _Aix1PktAdminQBitMBit_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 4),
    _Aix1PktAdminQBitMBit_Type()
)
aix1PktAdminQBitMBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminQBitMBit.setStatus("mandatory")


class _Aix1PktAdminUseRejectPkts_Type(Integer32):
    """Custom type aix1PktAdminUseRejectPkts based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPktRetrans", 1),
          ("pktRetrans", 2))
    )


_Aix1PktAdminUseRejectPkts_Type.__name__ = "Integer32"
_Aix1PktAdminUseRejectPkts_Object = MibTableColumn
aix1PktAdminUseRejectPkts = _Aix1PktAdminUseRejectPkts_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 5),
    _Aix1PktAdminUseRejectPkts_Type()
)
aix1PktAdminUseRejectPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminUseRejectPkts.setStatus("mandatory")


class _Aix1PktAdminSendInitialRestart_Type(Integer32):
    """Custom type aix1PktAdminSendInitialRestart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initialRestart", 1),
          ("noInitialRestart", 2))
    )


_Aix1PktAdminSendInitialRestart_Type.__name__ = "Integer32"
_Aix1PktAdminSendInitialRestart_Object = MibTableColumn
aix1PktAdminSendInitialRestart = _Aix1PktAdminSendInitialRestart_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 6),
    _Aix1PktAdminSendInitialRestart_Type()
)
aix1PktAdminSendInitialRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminSendInitialRestart.setStatus("mandatory")


class _Aix1PktAdminStdsBody_Type(Integer32):
    """Custom type aix1PktAdminStdsBody based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccittPktLvl", 1),
          ("isoPktLvl", 2))
    )


_Aix1PktAdminStdsBody_Type.__name__ = "Integer32"
_Aix1PktAdminStdsBody_Object = MibTableColumn
aix1PktAdminStdsBody = _Aix1PktAdminStdsBody_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 7),
    _Aix1PktAdminStdsBody_Type()
)
aix1PktAdminStdsBody.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminStdsBody.setStatus("mandatory")


class _Aix1PktAdminFacilChecking_Type(Integer32):
    """Custom type aix1PktAdminFacilChecking based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checkFacils", 1),
          ("noCheckFacils", 2))
    )


_Aix1PktAdminFacilChecking_Type.__name__ = "Integer32"
_Aix1PktAdminFacilChecking_Object = MibTableColumn
aix1PktAdminFacilChecking = _Aix1PktAdminFacilChecking_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 8),
    _Aix1PktAdminFacilChecking_Type()
)
aix1PktAdminFacilChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminFacilChecking.setStatus("mandatory")


class _Aix1PktAdminUndefinedFacils_Type(Integer32):
    """Custom type aix1PktAdminUndefinedFacils based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noUndefFacils", 1),
          ("undefFacils", 2))
    )


_Aix1PktAdminUndefinedFacils_Type.__name__ = "Integer32"
_Aix1PktAdminUndefinedFacils_Object = MibTableColumn
aix1PktAdminUndefinedFacils = _Aix1PktAdminUndefinedFacils_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 9),
    _Aix1PktAdminUndefinedFacils_Type()
)
aix1PktAdminUndefinedFacils.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminUndefinedFacils.setStatus("mandatory")


class _Aix1PktAdminDefMaxPktSize_Type(Integer32):
    """Custom type aix1PktAdminDefMaxPktSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              256,
              512,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("pkt1024", 1024),
          ("pkt128", 128),
          ("pkt256", 256),
          ("pkt512", 512))
    )


_Aix1PktAdminDefMaxPktSize_Type.__name__ = "Integer32"
_Aix1PktAdminDefMaxPktSize_Object = MibTableColumn
aix1PktAdminDefMaxPktSize = _Aix1PktAdminDefMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 10),
    _Aix1PktAdminDefMaxPktSize_Type()
)
aix1PktAdminDefMaxPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminDefMaxPktSize.setStatus("mandatory")


class _Aix1PktAdminDefWindowSize_Type(Integer32):
    """Custom type aix1PktAdminDefWindowSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Aix1PktAdminDefWindowSize_Type.__name__ = "Integer32"
_Aix1PktAdminDefWindowSize_Object = MibTableColumn
aix1PktAdminDefWindowSize = _Aix1PktAdminDefWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 11),
    _Aix1PktAdminDefWindowSize_Type()
)
aix1PktAdminDefWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminDefWindowSize.setStatus("mandatory")


class _Aix1PktAdminNegMaxPktSize_Type(Integer32):
    """Custom type aix1PktAdminNegMaxPktSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negotiate", 2),
          ("noNegotiation", 1))
    )


_Aix1PktAdminNegMaxPktSize_Type.__name__ = "Integer32"
_Aix1PktAdminNegMaxPktSize_Object = MibTableColumn
aix1PktAdminNegMaxPktSize = _Aix1PktAdminNegMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 12),
    _Aix1PktAdminNegMaxPktSize_Type()
)
aix1PktAdminNegMaxPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminNegMaxPktSize.setStatus("mandatory")


class _Aix1PktAdminNegWindowSize_Type(Integer32):
    """Custom type aix1PktAdminNegWindowSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negotiate", 2),
          ("noNegotiation", 1))
    )


_Aix1PktAdminNegWindowSize_Type.__name__ = "Integer32"
_Aix1PktAdminNegWindowSize_Object = MibTableColumn
aix1PktAdminNegWindowSize = _Aix1PktAdminNegWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 13),
    _Aix1PktAdminNegWindowSize_Type()
)
aix1PktAdminNegWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminNegWindowSize.setStatus("mandatory")


class _Aix1PktAdminPacketizingTimer_Type(Integer32):
    """Custom type aix1PktAdminPacketizingTimer based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Aix1PktAdminPacketizingTimer_Type.__name__ = "Integer32"
_Aix1PktAdminPacketizingTimer_Object = MibTableColumn
aix1PktAdminPacketizingTimer = _Aix1PktAdminPacketizingTimer_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 14),
    _Aix1PktAdminPacketizingTimer_Type()
)
aix1PktAdminPacketizingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminPacketizingTimer.setStatus("mandatory")


class _Aix1PktAdminPVCOffset_Type(Integer32):
    """Custom type aix1PktAdminPVCOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Aix1PktAdminPVCOffset_Type.__name__ = "Integer32"
_Aix1PktAdminPVCOffset_Object = MibTableColumn
aix1PktAdminPVCOffset = _Aix1PktAdminPVCOffset_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 15),
    _Aix1PktAdminPVCOffset_Type()
)
aix1PktAdminPVCOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminPVCOffset.setStatus("mandatory")


class _Aix1PktAdminSVCOffset_Type(Integer32):
    """Custom type aix1PktAdminSVCOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Aix1PktAdminSVCOffset_Type.__name__ = "Integer32"
_Aix1PktAdminSVCOffset_Object = MibTableColumn
aix1PktAdminSVCOffset = _Aix1PktAdminSVCOffset_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 1, 1, 16),
    _Aix1PktAdminSVCOffset_Type()
)
aix1PktAdminSVCOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PktAdminSVCOffset.setStatus("mandatory")
_Aix1PktOperTable_Object = MibTable
aix1PktOperTable = _Aix1PktOperTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2)
)
if mibBuilder.loadTexts:
    aix1PktOperTable.setStatus("mandatory")
_Aix1PktOperEntry_Object = MibTableRow
aix1PktOperEntry = _Aix1PktOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1)
)
aix1PktOperEntry.setIndexNames(
    (0, "AIX1-MIB", "aix1PktOperIndex"),
)
if mibBuilder.loadTexts:
    aix1PktOperEntry.setStatus("mandatory")
_Aix1PktOperIndex_Type = IfIndexType
_Aix1PktOperIndex_Object = MibTableColumn
aix1PktOperIndex = _Aix1PktOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 1),
    _Aix1PktOperIndex_Type()
)
aix1PktOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperIndex.setStatus("mandatory")


class _Aix1PktOperConformanceMode_Type(Integer32):
    """Custom type aix1PktOperConformanceMode based on Integer32"""
    defaultValue = 1

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


_Aix1PktOperConformanceMode_Type.__name__ = "Integer32"
_Aix1PktOperConformanceMode_Object = MibTableColumn
aix1PktOperConformanceMode = _Aix1PktOperConformanceMode_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 2),
    _Aix1PktOperConformanceMode_Type()
)
aix1PktOperConformanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperConformanceMode.setStatus("mandatory")


class _Aix1PktOperDBit_Type(Integer32):
    """Custom type aix1PktOperDBit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dbitAllowed", 2),
          ("dbitNotAllowed", 1))
    )


_Aix1PktOperDBit_Type.__name__ = "Integer32"
_Aix1PktOperDBit_Object = MibTableColumn
aix1PktOperDBit = _Aix1PktOperDBit_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 3),
    _Aix1PktOperDBit_Type()
)
aix1PktOperDBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperDBit.setStatus("mandatory")


class _Aix1PktOperQBitMBit_Type(Integer32):
    """Custom type aix1PktOperQBitMBit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noQMCheck", 1),
          ("qmCheck", 2))
    )


_Aix1PktOperQBitMBit_Type.__name__ = "Integer32"
_Aix1PktOperQBitMBit_Object = MibTableColumn
aix1PktOperQBitMBit = _Aix1PktOperQBitMBit_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 4),
    _Aix1PktOperQBitMBit_Type()
)
aix1PktOperQBitMBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperQBitMBit.setStatus("mandatory")


class _Aix1PktOperUseRejectPkts_Type(Integer32):
    """Custom type aix1PktOperUseRejectPkts based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPktRetrans", 1),
          ("pktRetrans", 2))
    )


_Aix1PktOperUseRejectPkts_Type.__name__ = "Integer32"
_Aix1PktOperUseRejectPkts_Object = MibTableColumn
aix1PktOperUseRejectPkts = _Aix1PktOperUseRejectPkts_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 5),
    _Aix1PktOperUseRejectPkts_Type()
)
aix1PktOperUseRejectPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperUseRejectPkts.setStatus("mandatory")


class _Aix1PktOperSendInitialRestart_Type(Integer32):
    """Custom type aix1PktOperSendInitialRestart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initialRestart", 1),
          ("noInitialRestart", 2))
    )


_Aix1PktOperSendInitialRestart_Type.__name__ = "Integer32"
_Aix1PktOperSendInitialRestart_Object = MibTableColumn
aix1PktOperSendInitialRestart = _Aix1PktOperSendInitialRestart_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 6),
    _Aix1PktOperSendInitialRestart_Type()
)
aix1PktOperSendInitialRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperSendInitialRestart.setStatus("mandatory")


class _Aix1PktOperStdsBody_Type(Integer32):
    """Custom type aix1PktOperStdsBody based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccittPktLvl", 1),
          ("isoPktLvl", 2))
    )


_Aix1PktOperStdsBody_Type.__name__ = "Integer32"
_Aix1PktOperStdsBody_Object = MibTableColumn
aix1PktOperStdsBody = _Aix1PktOperStdsBody_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 7),
    _Aix1PktOperStdsBody_Type()
)
aix1PktOperStdsBody.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperStdsBody.setStatus("mandatory")


class _Aix1PktOperFacilChecking_Type(Integer32):
    """Custom type aix1PktOperFacilChecking based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checkFacils", 1),
          ("noCheckFacils", 2))
    )


_Aix1PktOperFacilChecking_Type.__name__ = "Integer32"
_Aix1PktOperFacilChecking_Object = MibTableColumn
aix1PktOperFacilChecking = _Aix1PktOperFacilChecking_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 8),
    _Aix1PktOperFacilChecking_Type()
)
aix1PktOperFacilChecking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperFacilChecking.setStatus("mandatory")


class _Aix1PktOperUndefinedFacils_Type(Integer32):
    """Custom type aix1PktOperUndefinedFacils based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noUndefFacils", 1),
          ("undefFacils", 2))
    )


_Aix1PktOperUndefinedFacils_Type.__name__ = "Integer32"
_Aix1PktOperUndefinedFacils_Object = MibTableColumn
aix1PktOperUndefinedFacils = _Aix1PktOperUndefinedFacils_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 9),
    _Aix1PktOperUndefinedFacils_Type()
)
aix1PktOperUndefinedFacils.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperUndefinedFacils.setStatus("mandatory")


class _Aix1PktOperDefMaxPktSize_Type(Integer32):
    """Custom type aix1PktOperDefMaxPktSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              256,
              512,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("pkt1024", 1024),
          ("pkt128", 128),
          ("pkt256", 256),
          ("pkt512", 512))
    )


_Aix1PktOperDefMaxPktSize_Type.__name__ = "Integer32"
_Aix1PktOperDefMaxPktSize_Object = MibTableColumn
aix1PktOperDefMaxPktSize = _Aix1PktOperDefMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 10),
    _Aix1PktOperDefMaxPktSize_Type()
)
aix1PktOperDefMaxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperDefMaxPktSize.setStatus("mandatory")


class _Aix1PktOperDefWindowSize_Type(Integer32):
    """Custom type aix1PktOperDefWindowSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Aix1PktOperDefWindowSize_Type.__name__ = "Integer32"
_Aix1PktOperDefWindowSize_Object = MibTableColumn
aix1PktOperDefWindowSize = _Aix1PktOperDefWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 11),
    _Aix1PktOperDefWindowSize_Type()
)
aix1PktOperDefWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperDefWindowSize.setStatus("mandatory")


class _Aix1PktOperNegMaxPktSize_Type(Integer32):
    """Custom type aix1PktOperNegMaxPktSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negotiate", 2),
          ("noNegotiation", 1))
    )


_Aix1PktOperNegMaxPktSize_Type.__name__ = "Integer32"
_Aix1PktOperNegMaxPktSize_Object = MibTableColumn
aix1PktOperNegMaxPktSize = _Aix1PktOperNegMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 12),
    _Aix1PktOperNegMaxPktSize_Type()
)
aix1PktOperNegMaxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperNegMaxPktSize.setStatus("mandatory")


class _Aix1PktOperNegWindowSize_Type(Integer32):
    """Custom type aix1PktOperNegWindowSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negotiate", 2),
          ("noNegotiation", 1))
    )


_Aix1PktOperNegWindowSize_Type.__name__ = "Integer32"
_Aix1PktOperNegWindowSize_Object = MibTableColumn
aix1PktOperNegWindowSize = _Aix1PktOperNegWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 13),
    _Aix1PktOperNegWindowSize_Type()
)
aix1PktOperNegWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperNegWindowSize.setStatus("mandatory")


class _Aix1PktOperPacketizingTimer_Type(Integer32):
    """Custom type aix1PktOperPacketizingTimer based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Aix1PktOperPacketizingTimer_Type.__name__ = "Integer32"
_Aix1PktOperPacketizingTimer_Object = MibTableColumn
aix1PktOperPacketizingTimer = _Aix1PktOperPacketizingTimer_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 14),
    _Aix1PktOperPacketizingTimer_Type()
)
aix1PktOperPacketizingTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperPacketizingTimer.setStatus("mandatory")


class _Aix1PktOperPVCOffset_Type(Integer32):
    """Custom type aix1PktOperPVCOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Aix1PktOperPVCOffset_Type.__name__ = "Integer32"
_Aix1PktOperPVCOffset_Object = MibTableColumn
aix1PktOperPVCOffset = _Aix1PktOperPVCOffset_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 15),
    _Aix1PktOperPVCOffset_Type()
)
aix1PktOperPVCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperPVCOffset.setStatus("mandatory")


class _Aix1PktOperSVCOffset_Type(Integer32):
    """Custom type aix1PktOperSVCOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Aix1PktOperSVCOffset_Type.__name__ = "Integer32"
_Aix1PktOperSVCOffset_Object = MibTableColumn
aix1PktOperSVCOffset = _Aix1PktOperSVCOffset_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 2, 1, 16),
    _Aix1PktOperSVCOffset_Type()
)
aix1PktOperSVCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktOperSVCOffset.setStatus("mandatory")
_Aix1PktStatTable_Object = MibTable
aix1PktStatTable = _Aix1PktStatTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 3)
)
if mibBuilder.loadTexts:
    aix1PktStatTable.setStatus("mandatory")
_Aix1PktStatEntry_Object = MibTableRow
aix1PktStatEntry = _Aix1PktStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 3, 1)
)
aix1PktStatEntry.setIndexNames(
    (0, "AIX1-MIB", "aix1PktStatIndex"),
)
if mibBuilder.loadTexts:
    aix1PktStatEntry.setStatus("mandatory")
_Aix1PktStatIndex_Type = IfIndexType
_Aix1PktStatIndex_Object = MibTableColumn
aix1PktStatIndex = _Aix1PktStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 3, 1, 1),
    _Aix1PktStatIndex_Type()
)
aix1PktStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktStatIndex.setStatus("mandatory")
_Aix1PktStatInCharsPerSec80s_Type = Counter32
_Aix1PktStatInCharsPerSec80s_Object = MibTableColumn
aix1PktStatInCharsPerSec80s = _Aix1PktStatInCharsPerSec80s_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 3, 1, 2),
    _Aix1PktStatInCharsPerSec80s_Type()
)
aix1PktStatInCharsPerSec80s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktStatInCharsPerSec80s.setStatus("mandatory")
_Aix1PktStatOutCharsPerSec80s_Type = Counter32
_Aix1PktStatOutCharsPerSec80s_Object = MibTableColumn
aix1PktStatOutCharsPerSec80s = _Aix1PktStatOutCharsPerSec80s_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 3, 3, 1, 3),
    _Aix1PktStatOutCharsPerSec80s_Type()
)
aix1PktStatOutCharsPerSec80s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PktStatOutCharsPerSec80s.setStatus("mandatory")
_AiX1Frm_ObjectIdentity = ObjectIdentity
aiX1Frm = _AiX1Frm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12, 4)
)
_Aix1FrmAdminTable_Object = MibTable
aix1FrmAdminTable = _Aix1FrmAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 4, 1)
)
if mibBuilder.loadTexts:
    aix1FrmAdminTable.setStatus("mandatory")
_Aix1FrmAdminEntry_Object = MibTableRow
aix1FrmAdminEntry = _Aix1FrmAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 4, 1, 1)
)
aix1FrmAdminEntry.setIndexNames(
    (0, "AIX1-MIB", "aix1FrmAdminIndex"),
)
if mibBuilder.loadTexts:
    aix1FrmAdminEntry.setStatus("mandatory")
_Aix1FrmAdminIndex_Type = IfIndexType
_Aix1FrmAdminIndex_Object = MibTableColumn
aix1FrmAdminIndex = _Aix1FrmAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 4, 1, 1, 1),
    _Aix1FrmAdminIndex_Type()
)
aix1FrmAdminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1FrmAdminIndex.setStatus("mandatory")


class _Aix1FrmAdminIdleRRs_Type(Integer32):
    """Custom type aix1FrmAdminIdleRRs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idleRRs", 1),
          ("noIdleRRs", 2))
    )


_Aix1FrmAdminIdleRRs_Type.__name__ = "Integer32"
_Aix1FrmAdminIdleRRs_Object = MibTableColumn
aix1FrmAdminIdleRRs = _Aix1FrmAdminIdleRRs_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 4, 1, 1, 2),
    _Aix1FrmAdminIdleRRs_Type()
)
aix1FrmAdminIdleRRs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1FrmAdminIdleRRs.setStatus("mandatory")


class _Aix1FrmAdminRandomizeT1_Type(Integer32):
    """Custom type aix1FrmAdminRandomizeT1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRandomT1", 2),
          ("randomT1", 1))
    )


_Aix1FrmAdminRandomizeT1_Type.__name__ = "Integer32"
_Aix1FrmAdminRandomizeT1_Object = MibTableColumn
aix1FrmAdminRandomizeT1 = _Aix1FrmAdminRandomizeT1_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 4, 1, 1, 3),
    _Aix1FrmAdminRandomizeT1_Type()
)
aix1FrmAdminRandomizeT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1FrmAdminRandomizeT1.setStatus("mandatory")
_Aix1FrmOperTable_Object = MibTable
aix1FrmOperTable = _Aix1FrmOperTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 4, 2)
)
if mibBuilder.loadTexts:
    aix1FrmOperTable.setStatus("mandatory")
_Aix1FrmOperEntry_Object = MibTableRow
aix1FrmOperEntry = _Aix1FrmOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 4, 2, 1)
)
aix1FrmOperEntry.setIndexNames(
    (0, "AIX1-MIB", "aix1FrmOperIndex"),
)
if mibBuilder.loadTexts:
    aix1FrmOperEntry.setStatus("mandatory")
_Aix1FrmOperIndex_Type = IfIndexType
_Aix1FrmOperIndex_Object = MibTableColumn
aix1FrmOperIndex = _Aix1FrmOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 4, 2, 1, 1),
    _Aix1FrmOperIndex_Type()
)
aix1FrmOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1FrmOperIndex.setStatus("mandatory")


class _Aix1FrmOperIdleRRs_Type(Integer32):
    """Custom type aix1FrmOperIdleRRs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idleRRs", 1),
          ("noIdleRRs", 2))
    )


_Aix1FrmOperIdleRRs_Type.__name__ = "Integer32"
_Aix1FrmOperIdleRRs_Object = MibTableColumn
aix1FrmOperIdleRRs = _Aix1FrmOperIdleRRs_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 4, 2, 1, 2),
    _Aix1FrmOperIdleRRs_Type()
)
aix1FrmOperIdleRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1FrmOperIdleRRs.setStatus("mandatory")


class _Aix1FrmOperRandomizeT1_Type(Integer32):
    """Custom type aix1FrmOperRandomizeT1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRandomT1", 2),
          ("randomT1", 1))
    )


_Aix1FrmOperRandomizeT1_Type.__name__ = "Integer32"
_Aix1FrmOperRandomizeT1_Object = MibTableColumn
aix1FrmOperRandomizeT1 = _Aix1FrmOperRandomizeT1_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 4, 2, 1, 3),
    _Aix1FrmOperRandomizeT1_Type()
)
aix1FrmOperRandomizeT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1FrmOperRandomizeT1.setStatus("mandatory")
_AiX1Phys_ObjectIdentity = ObjectIdentity
aiX1Phys = _AiX1Phys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12, 5)
)
_Aix1PhysAdminTable_Object = MibTable
aix1PhysAdminTable = _Aix1PhysAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 1)
)
if mibBuilder.loadTexts:
    aix1PhysAdminTable.setStatus("mandatory")
_Aix1PhysAdminEntry_Object = MibTableRow
aix1PhysAdminEntry = _Aix1PhysAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 1, 1)
)
aix1PhysAdminEntry.setIndexNames(
    (0, "AIX1-MIB", "aix1PhysAdminIndex"),
)
if mibBuilder.loadTexts:
    aix1PhysAdminEntry.setStatus("mandatory")
_Aix1PhysAdminIndex_Type = IfIndexType
_Aix1PhysAdminIndex_Object = MibTableColumn
aix1PhysAdminIndex = _Aix1PhysAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 1, 1, 1),
    _Aix1PhysAdminIndex_Type()
)
aix1PhysAdminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PhysAdminIndex.setStatus("mandatory")


class _Aix1PhysAdminInterFrameDelayStatus_Type(Integer32):
    """Custom type aix1PhysAdminInterFrameDelayStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifdDisabled", 1),
          ("ifdEnabled", 2))
    )


_Aix1PhysAdminInterFrameDelayStatus_Type.__name__ = "Integer32"
_Aix1PhysAdminInterFrameDelayStatus_Object = MibTableColumn
aix1PhysAdminInterFrameDelayStatus = _Aix1PhysAdminInterFrameDelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 1, 1, 2),
    _Aix1PhysAdminInterFrameDelayStatus_Type()
)
aix1PhysAdminInterFrameDelayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PhysAdminInterFrameDelayStatus.setStatus("mandatory")


class _Aix1PhysAdminInterFrameDelayInterval_Type(Integer32):
    """Custom type aix1PhysAdminInterFrameDelayInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Aix1PhysAdminInterFrameDelayInterval_Type.__name__ = "Integer32"
_Aix1PhysAdminInterFrameDelayInterval_Object = MibTableColumn
aix1PhysAdminInterFrameDelayInterval = _Aix1PhysAdminInterFrameDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 1, 1, 3),
    _Aix1PhysAdminInterFrameDelayInterval_Type()
)
aix1PhysAdminInterFrameDelayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PhysAdminInterFrameDelayInterval.setStatus("mandatory")


class _Aix1PhysAdminT1LineBuildOut_Type(Integer32):
    """Custom type aix1PhysAdminT1LineBuildOut based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("lbo0to133", 1),
          ("lbo133to266", 2),
          ("lbo266to399", 3),
          ("lbo399to533", 4),
          ("lbo533to655", 5))
    )


_Aix1PhysAdminT1LineBuildOut_Type.__name__ = "Integer32"
_Aix1PhysAdminT1LineBuildOut_Object = MibTableColumn
aix1PhysAdminT1LineBuildOut = _Aix1PhysAdminT1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 1, 1, 4),
    _Aix1PhysAdminT1LineBuildOut_Type()
)
aix1PhysAdminT1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1PhysAdminT1LineBuildOut.setStatus("mandatory")
_Aix1PhysOperTable_Object = MibTable
aix1PhysOperTable = _Aix1PhysOperTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 2)
)
if mibBuilder.loadTexts:
    aix1PhysOperTable.setStatus("mandatory")
_Aix1PhysOperEntry_Object = MibTableRow
aix1PhysOperEntry = _Aix1PhysOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 2, 1)
)
aix1PhysOperEntry.setIndexNames(
    (0, "AIX1-MIB", "aix1PhysOperIndex"),
)
if mibBuilder.loadTexts:
    aix1PhysOperEntry.setStatus("mandatory")
_Aix1PhysOperIndex_Type = IfIndexType
_Aix1PhysOperIndex_Object = MibTableColumn
aix1PhysOperIndex = _Aix1PhysOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 2, 1, 1),
    _Aix1PhysOperIndex_Type()
)
aix1PhysOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PhysOperIndex.setStatus("mandatory")


class _Aix1PhysOperInterFrameDelayStatus_Type(Integer32):
    """Custom type aix1PhysOperInterFrameDelayStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifdDisabled", 1),
          ("ifdEnabled", 2))
    )


_Aix1PhysOperInterFrameDelayStatus_Type.__name__ = "Integer32"
_Aix1PhysOperInterFrameDelayStatus_Object = MibTableColumn
aix1PhysOperInterFrameDelayStatus = _Aix1PhysOperInterFrameDelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 2, 1, 2),
    _Aix1PhysOperInterFrameDelayStatus_Type()
)
aix1PhysOperInterFrameDelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PhysOperInterFrameDelayStatus.setStatus("mandatory")


class _Aix1PhysOperInterFrameDelayInterval_Type(Integer32):
    """Custom type aix1PhysOperInterFrameDelayInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Aix1PhysOperInterFrameDelayInterval_Type.__name__ = "Integer32"
_Aix1PhysOperInterFrameDelayInterval_Object = MibTableColumn
aix1PhysOperInterFrameDelayInterval = _Aix1PhysOperInterFrameDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 2, 1, 3),
    _Aix1PhysOperInterFrameDelayInterval_Type()
)
aix1PhysOperInterFrameDelayInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PhysOperInterFrameDelayInterval.setStatus("mandatory")


class _Aix1PhysOperT1LineBuildOut_Type(Integer32):
    """Custom type aix1PhysOperT1LineBuildOut based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("lbo0to133", 1),
          ("lbo133to266", 2),
          ("lbo266to399", 3),
          ("lbo399to533", 4),
          ("lbo533to655", 5))
    )


_Aix1PhysOperT1LineBuildOut_Type.__name__ = "Integer32"
_Aix1PhysOperT1LineBuildOut_Object = MibTableColumn
aix1PhysOperT1LineBuildOut = _Aix1PhysOperT1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 2, 1, 4),
    _Aix1PhysOperT1LineBuildOut_Type()
)
aix1PhysOperT1LineBuildOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PhysOperT1LineBuildOut.setStatus("mandatory")
_Aix1PhysStatTable_Object = MibTable
aix1PhysStatTable = _Aix1PhysStatTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 3)
)
if mibBuilder.loadTexts:
    aix1PhysStatTable.setStatus("mandatory")
_Aix1PhysStatEntry_Object = MibTableRow
aix1PhysStatEntry = _Aix1PhysStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 3, 1)
)
aix1PhysStatEntry.setIndexNames(
    (0, "AIX1-MIB", "aix1PhysStatIndex"),
)
if mibBuilder.loadTexts:
    aix1PhysStatEntry.setStatus("mandatory")
_Aix1PhysStatIndex_Type = IfIndexType
_Aix1PhysStatIndex_Object = MibTableColumn
aix1PhysStatIndex = _Aix1PhysStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 3, 1, 1),
    _Aix1PhysStatIndex_Type()
)
aix1PhysStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PhysStatIndex.setStatus("mandatory")
_Aix1PhysStatTxAborts_Type = Counter32
_Aix1PhysStatTxAborts_Object = MibTableColumn
aix1PhysStatTxAborts = _Aix1PhysStatTxAborts_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 5, 3, 1, 2),
    _Aix1PhysStatTxAborts_Type()
)
aix1PhysStatTxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1PhysStatTxAborts.setStatus("mandatory")
_AiX1VC_ObjectIdentity = ObjectIdentity
aiX1VC = _AiX1VC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 12, 6)
)
_Aix1CircuitTable_Object = MibTable
aix1CircuitTable = _Aix1CircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1)
)
if mibBuilder.loadTexts:
    aix1CircuitTable.setStatus("mandatory")
_Aix1CircuitEntry_Object = MibTableRow
aix1CircuitEntry = _Aix1CircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1, 1)
)
aix1CircuitEntry.setIndexNames(
    (0, "AIX1-MIB", "aix1CircuitLinkId"),
    (0, "AIX1-MIB", "aix1CircuitChannelNumber"),
)
if mibBuilder.loadTexts:
    aix1CircuitEntry.setStatus("mandatory")
_Aix1CircuitLinkId_Type = IfIndexType
_Aix1CircuitLinkId_Object = MibTableColumn
aix1CircuitLinkId = _Aix1CircuitLinkId_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1, 1, 1),
    _Aix1CircuitLinkId_Type()
)
aix1CircuitLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1CircuitLinkId.setStatus("mandatory")


class _Aix1CircuitChannelNumber_Type(Integer32):
    """Custom type aix1CircuitChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Aix1CircuitChannelNumber_Type.__name__ = "Integer32"
_Aix1CircuitChannelNumber_Object = MibTableColumn
aix1CircuitChannelNumber = _Aix1CircuitChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1, 1, 2),
    _Aix1CircuitChannelNumber_Type()
)
aix1CircuitChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1CircuitChannelNumber.setStatus("mandatory")


class _Aix1CircuitState_Type(Integer32):
    """Custom type aix1CircuitState based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("csCall", 3),
          ("csCancel", 5),
          ("csCol", 7),
          ("csDisco", 4),
          ("csReject", 6),
          ("csSuspend", 16),
          ("csUncol", 8),
          ("idle", 1),
          ("npCall", 9),
          ("npCancel", 11),
          ("npCol", 13),
          ("npDisco", 10),
          ("npReject", 12),
          ("npUncol", 14),
          ("trapped", 15))
    )


_Aix1CircuitState_Type.__name__ = "Integer32"
_Aix1CircuitState_Object = MibTableColumn
aix1CircuitState = _Aix1CircuitState_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1, 1, 3),
    _Aix1CircuitState_Type()
)
aix1CircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1CircuitState.setStatus("mandatory")


class _Aix1CircuitConType_Type(Integer32):
    """Custom type aix1CircuitConType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("background", 6),
          ("debug", 5),
          ("lmux", 1),
          ("pvc", 11),
          ("rmux", 2),
          ("svc", 12))
    )


_Aix1CircuitConType_Type.__name__ = "Integer32"
_Aix1CircuitConType_Object = MibTableColumn
aix1CircuitConType = _Aix1CircuitConType_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1, 1, 4),
    _Aix1CircuitConType_Type()
)
aix1CircuitConType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1CircuitConType.setStatus("mandatory")


class _Aix1CircuitBCNumber_Type(Integer32):
    """Custom type aix1CircuitBCNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Aix1CircuitBCNumber_Type.__name__ = "Integer32"
_Aix1CircuitBCNumber_Object = MibTableColumn
aix1CircuitBCNumber = _Aix1CircuitBCNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1, 1, 5),
    _Aix1CircuitBCNumber_Type()
)
aix1CircuitBCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1CircuitBCNumber.setStatus("mandatory")


class _Aix1CircuitUserData_Type(DisplayString):
    """Custom type aix1CircuitUserData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Aix1CircuitUserData_Type.__name__ = "DisplayString"
_Aix1CircuitUserData_Object = MibTableColumn
aix1CircuitUserData = _Aix1CircuitUserData_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1, 1, 6),
    _Aix1CircuitUserData_Type()
)
aix1CircuitUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1CircuitUserData.setStatus("mandatory")


class _Aix1CircuitRemoteBasePort_Type(Integer32):
    """Custom type aix1CircuitRemoteBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 256),
    )


_Aix1CircuitRemoteBasePort_Type.__name__ = "Integer32"
_Aix1CircuitRemoteBasePort_Object = MibTableColumn
aix1CircuitRemoteBasePort = _Aix1CircuitRemoteBasePort_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1, 1, 7),
    _Aix1CircuitRemoteBasePort_Type()
)
aix1CircuitRemoteBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1CircuitRemoteBasePort.setStatus("mandatory")


class _Aix1CircuitRemoteVCNumber_Type(Integer32):
    """Custom type aix1CircuitRemoteVCNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Aix1CircuitRemoteVCNumber_Type.__name__ = "Integer32"
_Aix1CircuitRemoteVCNumber_Object = MibTableColumn
aix1CircuitRemoteVCNumber = _Aix1CircuitRemoteVCNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1, 1, 8),
    _Aix1CircuitRemoteVCNumber_Type()
)
aix1CircuitRemoteVCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1CircuitRemoteVCNumber.setStatus("mandatory")
_Aix1CircuitPktsSent_Type = Counter32
_Aix1CircuitPktsSent_Object = MibTableColumn
aix1CircuitPktsSent = _Aix1CircuitPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1, 1, 9),
    _Aix1CircuitPktsSent_Type()
)
aix1CircuitPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1CircuitPktsSent.setStatus("mandatory")
_Aix1CircuitPktsRcvd_Type = Counter32
_Aix1CircuitPktsRcvd_Object = MibTableColumn
aix1CircuitPktsRcvd = _Aix1CircuitPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1, 1, 10),
    _Aix1CircuitPktsRcvd_Type()
)
aix1CircuitPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1CircuitPktsRcvd.setStatus("mandatory")


class _Aix1CircuitOperPVCType_Type(Integer32):
    """Custom type aix1CircuitOperPVCType based on Integer32"""
    defaultValue = 2

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
        *(("active", 2),
          ("connectOnActivity", 3),
          ("none", 1),
          ("passive", 4))
    )


_Aix1CircuitOperPVCType_Type.__name__ = "Integer32"
_Aix1CircuitOperPVCType_Object = MibTableColumn
aix1CircuitOperPVCType = _Aix1CircuitOperPVCType_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1, 1, 11),
    _Aix1CircuitOperPVCType_Type()
)
aix1CircuitOperPVCType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1CircuitOperPVCType.setStatus("mandatory")


class _Aix1CircuitOperPVCTimer_Type(Integer32):
    """Custom type aix1CircuitOperPVCTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_Aix1CircuitOperPVCTimer_Type.__name__ = "Integer32"
_Aix1CircuitOperPVCTimer_Object = MibTableColumn
aix1CircuitOperPVCTimer = _Aix1CircuitOperPVCTimer_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 1, 1, 12),
    _Aix1CircuitOperPVCTimer_Type()
)
aix1CircuitOperPVCTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1CircuitOperPVCTimer.setStatus("mandatory")
_Aix1VCTable_Object = MibTable
aix1VCTable = _Aix1VCTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 2)
)
if mibBuilder.loadTexts:
    aix1VCTable.setStatus("mandatory")
_Aix1VCEntry_Object = MibTableRow
aix1VCEntry = _Aix1VCEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 2, 1)
)
aix1VCEntry.setIndexNames(
    (0, "AIX1-MIB", "aix1VCVCNumber"),
)
if mibBuilder.loadTexts:
    aix1VCEntry.setStatus("mandatory")


class _Aix1VCVCNumber_Type(Integer32):
    """Custom type aix1VCVCNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 287),
    )


_Aix1VCVCNumber_Type.__name__ = "Integer32"
_Aix1VCVCNumber_Object = MibTableColumn
aix1VCVCNumber = _Aix1VCVCNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 2, 1, 1),
    _Aix1VCVCNumber_Type()
)
aix1VCVCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1VCVCNumber.setStatus("mandatory")


class _Aix1VCState_Type(Integer32):
    """Custom type aix1VCState based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("csCall", 3),
          ("csCancel", 5),
          ("csCol", 7),
          ("csDisco", 4),
          ("csReject", 6),
          ("csSuspend", 16),
          ("csUncol", 8),
          ("idle", 1),
          ("npCall", 9),
          ("npCancel", 11),
          ("npCol", 13),
          ("npDisco", 10),
          ("npReject", 12),
          ("npUncol", 14),
          ("trapped", 15))
    )


_Aix1VCState_Type.__name__ = "Integer32"
_Aix1VCState_Object = MibTableColumn
aix1VCState = _Aix1VCState_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 2, 1, 2),
    _Aix1VCState_Type()
)
aix1VCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1VCState.setStatus("mandatory")


class _Aix1VCConType_Type(Integer32):
    """Custom type aix1VCConType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("background", 6),
          ("debug", 5),
          ("lmux", 1),
          ("pvc", 11),
          ("rmux", 2),
          ("svc", 12))
    )


_Aix1VCConType_Type.__name__ = "Integer32"
_Aix1VCConType_Object = MibTableColumn
aix1VCConType = _Aix1VCConType_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 2, 1, 3),
    _Aix1VCConType_Type()
)
aix1VCConType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1VCConType.setStatus("mandatory")


class _Aix1VCBCNumber_Type(Integer32):
    """Custom type aix1VCBCNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Aix1VCBCNumber_Type.__name__ = "Integer32"
_Aix1VCBCNumber_Object = MibTableColumn
aix1VCBCNumber = _Aix1VCBCNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 2, 1, 4),
    _Aix1VCBCNumber_Type()
)
aix1VCBCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1VCBCNumber.setStatus("mandatory")


class _Aix1VCUserData_Type(DisplayString):
    """Custom type aix1VCUserData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Aix1VCUserData_Type.__name__ = "DisplayString"
_Aix1VCUserData_Object = MibTableColumn
aix1VCUserData = _Aix1VCUserData_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 2, 1, 5),
    _Aix1VCUserData_Type()
)
aix1VCUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1VCUserData.setStatus("mandatory")


class _Aix1VCRemoteBasePort_Type(Integer32):
    """Custom type aix1VCRemoteBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 256),
    )


_Aix1VCRemoteBasePort_Type.__name__ = "Integer32"
_Aix1VCRemoteBasePort_Object = MibTableColumn
aix1VCRemoteBasePort = _Aix1VCRemoteBasePort_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 2, 1, 6),
    _Aix1VCRemoteBasePort_Type()
)
aix1VCRemoteBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1VCRemoteBasePort.setStatus("mandatory")


class _Aix1VCRemoteVCNumber_Type(Integer32):
    """Custom type aix1VCRemoteVCNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Aix1VCRemoteVCNumber_Type.__name__ = "Integer32"
_Aix1VCRemoteVCNumber_Object = MibTableColumn
aix1VCRemoteVCNumber = _Aix1VCRemoteVCNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 2, 1, 7),
    _Aix1VCRemoteVCNumber_Type()
)
aix1VCRemoteVCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1VCRemoteVCNumber.setStatus("mandatory")
_Aix1VCPktsSent_Type = Counter32
_Aix1VCPktsSent_Object = MibTableColumn
aix1VCPktsSent = _Aix1VCPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 2, 1, 8),
    _Aix1VCPktsSent_Type()
)
aix1VCPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1VCPktsSent.setStatus("mandatory")
_Aix1VCPktsRcvd_Type = Counter32
_Aix1VCPktsRcvd_Object = MibTableColumn
aix1VCPktsRcvd = _Aix1VCPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 2, 1, 9),
    _Aix1VCPktsRcvd_Type()
)
aix1VCPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1VCPktsRcvd.setStatus("mandatory")


class _Aix1VCOperPVCType_Type(Integer32):
    """Custom type aix1VCOperPVCType based on Integer32"""
    defaultValue = 2

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
        *(("active", 2),
          ("connectOnActivity", 3),
          ("none", 1),
          ("passive", 4))
    )


_Aix1VCOperPVCType_Type.__name__ = "Integer32"
_Aix1VCOperPVCType_Object = MibTableColumn
aix1VCOperPVCType = _Aix1VCOperPVCType_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 2, 1, 10),
    _Aix1VCOperPVCType_Type()
)
aix1VCOperPVCType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1VCOperPVCType.setStatus("mandatory")


class _Aix1VCOperPVCTimer_Type(Integer32):
    """Custom type aix1VCOperPVCTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_Aix1VCOperPVCTimer_Type.__name__ = "Integer32"
_Aix1VCOperPVCTimer_Object = MibTableColumn
aix1VCOperPVCTimer = _Aix1VCOperPVCTimer_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 2, 1, 11),
    _Aix1VCOperPVCTimer_Type()
)
aix1VCOperPVCTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1VCOperPVCTimer.setStatus("mandatory")
_Aix1AdminPVCTable_Object = MibTable
aix1AdminPVCTable = _Aix1AdminPVCTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 3)
)
if mibBuilder.loadTexts:
    aix1AdminPVCTable.setStatus("mandatory")
_Aix1AdminPVCEntry_Object = MibTableRow
aix1AdminPVCEntry = _Aix1AdminPVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 3, 1)
)
aix1AdminPVCEntry.setIndexNames(
    (0, "AIX1-MIB", "aix1AdminPVCLinkId"),
    (0, "AIX1-MIB", "aix1AdminPVCChannelNumber"),
)
if mibBuilder.loadTexts:
    aix1AdminPVCEntry.setStatus("mandatory")
_Aix1AdminPVCLinkId_Type = IfIndexType
_Aix1AdminPVCLinkId_Object = MibTableColumn
aix1AdminPVCLinkId = _Aix1AdminPVCLinkId_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 3, 1, 1),
    _Aix1AdminPVCLinkId_Type()
)
aix1AdminPVCLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1AdminPVCLinkId.setStatus("mandatory")


class _Aix1AdminPVCChannelNumber_Type(Integer32):
    """Custom type aix1AdminPVCChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Aix1AdminPVCChannelNumber_Type.__name__ = "Integer32"
_Aix1AdminPVCChannelNumber_Object = MibTableColumn
aix1AdminPVCChannelNumber = _Aix1AdminPVCChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 3, 1, 2),
    _Aix1AdminPVCChannelNumber_Type()
)
aix1AdminPVCChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aix1AdminPVCChannelNumber.setStatus("mandatory")


class _Aix1AdminPVCType_Type(Integer32):
    """Custom type aix1AdminPVCType based on Integer32"""
    defaultValue = 2

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
        *(("active", 2),
          ("connectOnActivity", 3),
          ("none", 1),
          ("passive", 4))
    )


_Aix1AdminPVCType_Type.__name__ = "Integer32"
_Aix1AdminPVCType_Object = MibTableColumn
aix1AdminPVCType = _Aix1AdminPVCType_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 3, 1, 3),
    _Aix1AdminPVCType_Type()
)
aix1AdminPVCType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1AdminPVCType.setStatus("mandatory")


class _Aix1AdminPVCTimer_Type(Integer32):
    """Custom type aix1AdminPVCTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_Aix1AdminPVCTimer_Type.__name__ = "Integer32"
_Aix1AdminPVCTimer_Object = MibTableColumn
aix1AdminPVCTimer = _Aix1AdminPVCTimer_Object(
    (1, 3, 6, 1, 4, 1, 539, 12, 6, 3, 1, 4),
    _Aix1AdminPVCTimer_Type()
)
aix1AdminPVCTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aix1AdminPVCTimer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIX1-MIB",
    **{"IfIndexType": IfIndexType,
       "aii": aii,
       "aiSystemOID": aiSystemOID,
       "ai192": ai192,
       "ai192Ver7": ai192Ver7,
       "ai192Ver70": ai192Ver70,
       "ai192Ver708": ai192Ver708,
       "ai192Ver709": ai192Ver709,
       "ai192Ver71": ai192Ver71,
       "ai192Ver710": ai192Ver710,
       "ai192Ver711": ai192Ver711,
       "ai192Ver72": ai192Ver72,
       "ai192Ver720": ai192Ver720,
       "ai192Ver721": ai192Ver721,
       "ai192Ver77": ai192Ver77,
       "ai196": ai196,
       "ai196Ver7": ai196Ver7,
       "ai196Ver70": ai196Ver70,
       "ai196Ver708": ai196Ver708,
       "ai196Ver709": ai196Ver709,
       "ai196Ver71": ai196Ver71,
       "ai196Ver710": ai196Ver710,
       "ai196Ver711": ai196Ver711,
       "ai196Ver72": ai196Ver72,
       "ai196Ver720": ai196Ver720,
       "ai196Ver721": ai196Ver721,
       "ai196Ver77": ai196Ver77,
       "aiX1": aiX1,
       "aiX1System": aiX1System,
       "aix1AdminGbufXoffThreshold": aix1AdminGbufXoffThreshold,
       "aix1AdminGbufRecovThreshold": aix1AdminGbufRecovThreshold,
       "aix1AdminRollover": aix1AdminRollover,
       "aix1Bx25AdminCallDown": aix1Bx25AdminCallDown,
       "aix1Bx25AdminDMlock": aix1Bx25AdminDMlock,
       "aix1Bx25AdminLinkUp": aix1Bx25AdminLinkUp,
       "aix1StatErrX25InData": aix1StatErrX25InData,
       "aix1StatErrX25OutData": aix1StatErrX25OutData,
       "aix1StatErrX25OutPkt": aix1StatErrX25OutPkt,
       "aix1StatErrX25OutChoked": aix1StatErrX25OutChoked,
       "aix1StatErrPlogCount": aix1StatErrPlogCount,
       "aix1StatErrGfctlXoffs": aix1StatErrGfctlXoffs,
       "aix1StatErrGfctlDiscards": aix1StatErrGfctlDiscards,
       "aix1StatErrUwteBadTrans": aix1StatErrUwteBadTrans,
       "aix1StatErrUwteBadFlds": aix1StatErrUwteBadFlds,
       "aix1StatErrUwteMissingFlds": aix1StatErrUwteMissingFlds,
       "aix1StatErrLogOutLost": aix1StatErrLogOutLost,
       "aix1StatErrVcMuxErrs": aix1StatErrVcMuxErrs,
       "aix1StatErrEmptyPktsRcv": aix1StatErrEmptyPktsRcv,
       "aix1StatInCharsPerSec80s": aix1StatInCharsPerSec80s,
       "aix1StatOutCharsPerSec80s": aix1StatOutCharsPerSec80s,
       "aiX1Appl": aiX1Appl,
       "aix1ApplAdminTable": aix1ApplAdminTable,
       "aix1ApplAdminEntry": aix1ApplAdminEntry,
       "aix1ApplAdminIndex": aix1ApplAdminIndex,
       "aix1ApplAdminLinkStart": aix1ApplAdminLinkStart,
       "aix1ApplAdminLinkMode": aix1ApplAdminLinkMode,
       "aix1ApplAdminResetErrs": aix1ApplAdminResetErrs,
       "aix1ApplAdminXONXOFFProto": aix1ApplAdminXONXOFFProto,
       "aix1ApplAdminNMAProto": aix1ApplAdminNMAProto,
       "aix1ApplAdminOPSINEProto": aix1ApplAdminOPSINEProto,
       "aix1ApplAdminTL1Proto": aix1ApplAdminTL1Proto,
       "aix1ApplAdminLinkDescription": aix1ApplAdminLinkDescription,
       "aix1ApplAdminLinkConnectionMode": aix1ApplAdminLinkConnectionMode,
       "aix1ApplOperTable": aix1ApplOperTable,
       "aix1ApplOperEntry": aix1ApplOperEntry,
       "aix1ApplOperIndex": aix1ApplOperIndex,
       "aix1ApplOperLinkMode": aix1ApplOperLinkMode,
       "aix1ApplOperXONXOFFProto": aix1ApplOperXONXOFFProto,
       "aix1ApplOperNMAProto": aix1ApplOperNMAProto,
       "aix1ApplOperOPSINEProto": aix1ApplOperOPSINEProto,
       "aix1ApplOperTL1Proto": aix1ApplOperTL1Proto,
       "aix1ApplOperLinkDescription": aix1ApplOperLinkDescription,
       "aix1ApplOperLinkConnectionMode": aix1ApplOperLinkConnectionMode,
       "aiX1Pkt": aiX1Pkt,
       "aix1PktAdminTable": aix1PktAdminTable,
       "aix1PktAdminEntry": aix1PktAdminEntry,
       "aix1PktAdminIndex": aix1PktAdminIndex,
       "aix1PktAdminConformanceMode": aix1PktAdminConformanceMode,
       "aix1PktAdminDBit": aix1PktAdminDBit,
       "aix1PktAdminQBitMBit": aix1PktAdminQBitMBit,
       "aix1PktAdminUseRejectPkts": aix1PktAdminUseRejectPkts,
       "aix1PktAdminSendInitialRestart": aix1PktAdminSendInitialRestart,
       "aix1PktAdminStdsBody": aix1PktAdminStdsBody,
       "aix1PktAdminFacilChecking": aix1PktAdminFacilChecking,
       "aix1PktAdminUndefinedFacils": aix1PktAdminUndefinedFacils,
       "aix1PktAdminDefMaxPktSize": aix1PktAdminDefMaxPktSize,
       "aix1PktAdminDefWindowSize": aix1PktAdminDefWindowSize,
       "aix1PktAdminNegMaxPktSize": aix1PktAdminNegMaxPktSize,
       "aix1PktAdminNegWindowSize": aix1PktAdminNegWindowSize,
       "aix1PktAdminPacketizingTimer": aix1PktAdminPacketizingTimer,
       "aix1PktAdminPVCOffset": aix1PktAdminPVCOffset,
       "aix1PktAdminSVCOffset": aix1PktAdminSVCOffset,
       "aix1PktOperTable": aix1PktOperTable,
       "aix1PktOperEntry": aix1PktOperEntry,
       "aix1PktOperIndex": aix1PktOperIndex,
       "aix1PktOperConformanceMode": aix1PktOperConformanceMode,
       "aix1PktOperDBit": aix1PktOperDBit,
       "aix1PktOperQBitMBit": aix1PktOperQBitMBit,
       "aix1PktOperUseRejectPkts": aix1PktOperUseRejectPkts,
       "aix1PktOperSendInitialRestart": aix1PktOperSendInitialRestart,
       "aix1PktOperStdsBody": aix1PktOperStdsBody,
       "aix1PktOperFacilChecking": aix1PktOperFacilChecking,
       "aix1PktOperUndefinedFacils": aix1PktOperUndefinedFacils,
       "aix1PktOperDefMaxPktSize": aix1PktOperDefMaxPktSize,
       "aix1PktOperDefWindowSize": aix1PktOperDefWindowSize,
       "aix1PktOperNegMaxPktSize": aix1PktOperNegMaxPktSize,
       "aix1PktOperNegWindowSize": aix1PktOperNegWindowSize,
       "aix1PktOperPacketizingTimer": aix1PktOperPacketizingTimer,
       "aix1PktOperPVCOffset": aix1PktOperPVCOffset,
       "aix1PktOperSVCOffset": aix1PktOperSVCOffset,
       "aix1PktStatTable": aix1PktStatTable,
       "aix1PktStatEntry": aix1PktStatEntry,
       "aix1PktStatIndex": aix1PktStatIndex,
       "aix1PktStatInCharsPerSec80s": aix1PktStatInCharsPerSec80s,
       "aix1PktStatOutCharsPerSec80s": aix1PktStatOutCharsPerSec80s,
       "aiX1Frm": aiX1Frm,
       "aix1FrmAdminTable": aix1FrmAdminTable,
       "aix1FrmAdminEntry": aix1FrmAdminEntry,
       "aix1FrmAdminIndex": aix1FrmAdminIndex,
       "aix1FrmAdminIdleRRs": aix1FrmAdminIdleRRs,
       "aix1FrmAdminRandomizeT1": aix1FrmAdminRandomizeT1,
       "aix1FrmOperTable": aix1FrmOperTable,
       "aix1FrmOperEntry": aix1FrmOperEntry,
       "aix1FrmOperIndex": aix1FrmOperIndex,
       "aix1FrmOperIdleRRs": aix1FrmOperIdleRRs,
       "aix1FrmOperRandomizeT1": aix1FrmOperRandomizeT1,
       "aiX1Phys": aiX1Phys,
       "aix1PhysAdminTable": aix1PhysAdminTable,
       "aix1PhysAdminEntry": aix1PhysAdminEntry,
       "aix1PhysAdminIndex": aix1PhysAdminIndex,
       "aix1PhysAdminInterFrameDelayStatus": aix1PhysAdminInterFrameDelayStatus,
       "aix1PhysAdminInterFrameDelayInterval": aix1PhysAdminInterFrameDelayInterval,
       "aix1PhysAdminT1LineBuildOut": aix1PhysAdminT1LineBuildOut,
       "aix1PhysOperTable": aix1PhysOperTable,
       "aix1PhysOperEntry": aix1PhysOperEntry,
       "aix1PhysOperIndex": aix1PhysOperIndex,
       "aix1PhysOperInterFrameDelayStatus": aix1PhysOperInterFrameDelayStatus,
       "aix1PhysOperInterFrameDelayInterval": aix1PhysOperInterFrameDelayInterval,
       "aix1PhysOperT1LineBuildOut": aix1PhysOperT1LineBuildOut,
       "aix1PhysStatTable": aix1PhysStatTable,
       "aix1PhysStatEntry": aix1PhysStatEntry,
       "aix1PhysStatIndex": aix1PhysStatIndex,
       "aix1PhysStatTxAborts": aix1PhysStatTxAborts,
       "aiX1VC": aiX1VC,
       "aix1CircuitTable": aix1CircuitTable,
       "aix1CircuitEntry": aix1CircuitEntry,
       "aix1CircuitLinkId": aix1CircuitLinkId,
       "aix1CircuitChannelNumber": aix1CircuitChannelNumber,
       "aix1CircuitState": aix1CircuitState,
       "aix1CircuitConType": aix1CircuitConType,
       "aix1CircuitBCNumber": aix1CircuitBCNumber,
       "aix1CircuitUserData": aix1CircuitUserData,
       "aix1CircuitRemoteBasePort": aix1CircuitRemoteBasePort,
       "aix1CircuitRemoteVCNumber": aix1CircuitRemoteVCNumber,
       "aix1CircuitPktsSent": aix1CircuitPktsSent,
       "aix1CircuitPktsRcvd": aix1CircuitPktsRcvd,
       "aix1CircuitOperPVCType": aix1CircuitOperPVCType,
       "aix1CircuitOperPVCTimer": aix1CircuitOperPVCTimer,
       "aix1VCTable": aix1VCTable,
       "aix1VCEntry": aix1VCEntry,
       "aix1VCVCNumber": aix1VCVCNumber,
       "aix1VCState": aix1VCState,
       "aix1VCConType": aix1VCConType,
       "aix1VCBCNumber": aix1VCBCNumber,
       "aix1VCUserData": aix1VCUserData,
       "aix1VCRemoteBasePort": aix1VCRemoteBasePort,
       "aix1VCRemoteVCNumber": aix1VCRemoteVCNumber,
       "aix1VCPktsSent": aix1VCPktsSent,
       "aix1VCPktsRcvd": aix1VCPktsRcvd,
       "aix1VCOperPVCType": aix1VCOperPVCType,
       "aix1VCOperPVCTimer": aix1VCOperPVCTimer,
       "aix1AdminPVCTable": aix1AdminPVCTable,
       "aix1AdminPVCEntry": aix1AdminPVCEntry,
       "aix1AdminPVCLinkId": aix1AdminPVCLinkId,
       "aix1AdminPVCChannelNumber": aix1AdminPVCChannelNumber,
       "aix1AdminPVCType": aix1AdminPVCType,
       "aix1AdminPVCTimer": aix1AdminPVCTimer}
)
