# SNMP MIB module (BIANCA-BRICK-MIBMODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-MIBMODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:33 2024
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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Mdm_ObjectIdentity = ObjectIdentity
mdm = _Mdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 18)
)
_MdmProfileTable_Object = MibTable
mdmProfileTable = _MdmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1)
)
if mibBuilder.loadTexts:
    mdmProfileTable.setStatus("mandatory")
_MdmProfileEntry_Object = MibTableRow
mdmProfileEntry = _MdmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1)
)
mdmProfileEntry.setIndexNames(
    (0, "BIANCA-BRICK-MIBMODEM-MIB", "mdmProfileName"),
)
if mibBuilder.loadTexts:
    mdmProfileEntry.setStatus("mandatory")


class _MdmProfileName_Type(Integer32):
    """Custom type mdmProfileName based on Integer32"""
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
        *(("profile-1", 1),
          ("profile-2", 2),
          ("profile-3", 3),
          ("profile-4", 4),
          ("profile-5", 5),
          ("profile-6", 6),
          ("profile-7", 7),
          ("profile-8", 8))
    )


_MdmProfileName_Type.__name__ = "Integer32"
_MdmProfileName_Object = MibTableColumn
mdmProfileName = _MdmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 1),
    _MdmProfileName_Type()
)
mdmProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmProfileName.setStatus("mandatory")
_MdmProfileDescr_Type = DisplayString
_MdmProfileDescr_Object = MibTableColumn
mdmProfileDescr = _MdmProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 2),
    _MdmProfileDescr_Type()
)
mdmProfileDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileDescr.setStatus("mandatory")


class _MdmProfileModulation_Type(Integer32):
    """Custom type mdmProfileModulation based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("bell103", 1),
          ("bell212", 2),
          ("k56flex", 10),
          ("v21", 3),
          ("v22", 4),
          ("v22bis", 5),
          ("v23", 6),
          ("v32", 7),
          ("v32bis", 8),
          ("v34", 9),
          ("v90", 12),
          ("vfc", 11))
    )


_MdmProfileModulation_Type.__name__ = "Integer32"
_MdmProfileModulation_Object = MibTableColumn
mdmProfileModulation = _MdmProfileModulation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 3),
    _MdmProfileModulation_Type()
)
mdmProfileModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileModulation.setStatus("mandatory")


class _MdmProfileMinBps_Type(Integer32):
    """Custom type mdmProfileMinBps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(75,
              300,
              1200,
              2400,
              4800,
              7200,
              9600,
              12000,
              14400,
              16800,
              19200,
              21600,
              24000,
              26400,
              28800,
              31200,
              32000,
              33600,
              34000,
              36000,
              38000,
              40000,
              42000,
              44000,
              46000,
              48000,
              50000,
              52000,
              54000,
              56000)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1200),
          ("b12000", 12000),
          ("b14400", 14400),
          ("b16800", 16800),
          ("b19200", 19200),
          ("b21600", 21600),
          ("b2400", 2400),
          ("b24000", 24000),
          ("b26400", 26400),
          ("b28800", 28800),
          ("b300", 300),
          ("b31200", 31200),
          ("b32000", 32000),
          ("b33600", 33600),
          ("b34000", 34000),
          ("b36000", 36000),
          ("b38000", 38000),
          ("b40000", 40000),
          ("b42000", 42000),
          ("b44000", 44000),
          ("b46000", 46000),
          ("b4800", 4800),
          ("b48000", 48000),
          ("b50000", 50000),
          ("b52000", 52000),
          ("b54000", 54000),
          ("b56000", 56000),
          ("b7200", 7200),
          ("b75", 75),
          ("b9600", 9600))
    )


_MdmProfileMinBps_Type.__name__ = "Integer32"
_MdmProfileMinBps_Object = MibTableColumn
mdmProfileMinBps = _MdmProfileMinBps_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 4),
    _MdmProfileMinBps_Type()
)
mdmProfileMinBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileMinBps.setStatus("mandatory")


class _MdmProfileMaxRecvBps_Type(Integer32):
    """Custom type mdmProfileMaxRecvBps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              7200,
              9600,
              12000,
              14400,
              16800,
              19200,
              21600,
              24000,
              26400,
              28800,
              31200,
              32000,
              33600,
              34000,
              36000,
              38000,
              40000,
              42000,
              44000,
              46000,
              48000,
              50000,
              52000,
              54000,
              56000)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1200),
          ("b12000", 12000),
          ("b14400", 14400),
          ("b16800", 16800),
          ("b19200", 19200),
          ("b21600", 21600),
          ("b2400", 2400),
          ("b24000", 24000),
          ("b26400", 26400),
          ("b28800", 28800),
          ("b300", 300),
          ("b31200", 31200),
          ("b32000", 32000),
          ("b33600", 33600),
          ("b34000", 34000),
          ("b36000", 36000),
          ("b38000", 38000),
          ("b40000", 40000),
          ("b42000", 42000),
          ("b44000", 44000),
          ("b46000", 46000),
          ("b4800", 4800),
          ("b48000", 48000),
          ("b50000", 50000),
          ("b52000", 52000),
          ("b54000", 54000),
          ("b56000", 56000),
          ("b7200", 7200),
          ("b9600", 9600))
    )


_MdmProfileMaxRecvBps_Type.__name__ = "Integer32"
_MdmProfileMaxRecvBps_Object = MibTableColumn
mdmProfileMaxRecvBps = _MdmProfileMaxRecvBps_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 5),
    _MdmProfileMaxRecvBps_Type()
)
mdmProfileMaxRecvBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileMaxRecvBps.setStatus("mandatory")


class _MdmProfileMaxXmitBps_Type(Integer32):
    """Custom type mdmProfileMaxXmitBps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              7200,
              9600,
              12000,
              14400,
              16800,
              19200,
              21600,
              24000,
              26400,
              28800,
              31200,
              32000,
              33600,
              34000,
              36000,
              38000,
              40000,
              42000,
              44000,
              46000,
              48000,
              50000,
              52000,
              54000,
              56000)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1200),
          ("b12000", 12000),
          ("b14400", 14400),
          ("b16800", 16800),
          ("b19200", 19200),
          ("b21600", 21600),
          ("b2400", 2400),
          ("b24000", 24000),
          ("b26400", 26400),
          ("b28800", 28800),
          ("b300", 300),
          ("b31200", 31200),
          ("b32000", 32000),
          ("b33600", 33600),
          ("b34000", 34000),
          ("b36000", 36000),
          ("b38000", 38000),
          ("b40000", 40000),
          ("b42000", 42000),
          ("b44000", 44000),
          ("b46000", 46000),
          ("b4800", 4800),
          ("b48000", 48000),
          ("b50000", 50000),
          ("b52000", 52000),
          ("b54000", 54000),
          ("b56000", 56000),
          ("b7200", 7200),
          ("b9600", 9600))
    )


_MdmProfileMaxXmitBps_Type.__name__ = "Integer32"
_MdmProfileMaxXmitBps_Object = MibTableColumn
mdmProfileMaxXmitBps = _MdmProfileMaxXmitBps_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 6),
    _MdmProfileMaxXmitBps_Type()
)
mdmProfileMaxXmitBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileMaxXmitBps.setStatus("mandatory")


class _MdmProfileAutoMode_Type(Integer32):
    """Custom type mdmProfileAutoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MdmProfileAutoMode_Type.__name__ = "Integer32"
_MdmProfileAutoMode_Object = MibTableColumn
mdmProfileAutoMode = _MdmProfileAutoMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 7),
    _MdmProfileAutoMode_Type()
)
mdmProfileAutoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileAutoMode.setStatus("mandatory")


class _MdmProfileComprV42bis_Type(Integer32):
    """Custom type mdmProfileComprV42bis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("off", 1))
    )


_MdmProfileComprV42bis_Type.__name__ = "Integer32"
_MdmProfileComprV42bis_Object = MibTableColumn
mdmProfileComprV42bis = _MdmProfileComprV42bis_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 8),
    _MdmProfileComprV42bis_Type()
)
mdmProfileComprV42bis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileComprV42bis.setStatus("mandatory")


class _MdmProfileComprMNP5_Type(Integer32):
    """Custom type mdmProfileComprMNP5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("off", 1))
    )


_MdmProfileComprMNP5_Type.__name__ = "Integer32"
_MdmProfileComprMNP5_Object = MibTableColumn
mdmProfileComprMNP5 = _MdmProfileComprMNP5_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 9),
    _MdmProfileComprMNP5_Type()
)
mdmProfileComprMNP5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileComprMNP5.setStatus("mandatory")


class _MdmProfileErrorCorr_Type(Integer32):
    """Custom type mdmProfileErrorCorr based on Integer32"""
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
        *(("auto", 3),
          ("lapm", 4),
          ("mnp", 5),
          ("none", 1),
          ("required", 2))
    )


_MdmProfileErrorCorr_Type.__name__ = "Integer32"
_MdmProfileErrorCorr_Object = MibTableColumn
mdmProfileErrorCorr = _MdmProfileErrorCorr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 10),
    _MdmProfileErrorCorr_Type()
)
mdmProfileErrorCorr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileErrorCorr.setStatus("mandatory")


class _MdmProfileXmitLevel_Type(Integer32):
    """Custom type mdmProfileXmitLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 0),
    )


_MdmProfileXmitLevel_Type.__name__ = "Integer32"
_MdmProfileXmitLevel_Object = MibTableColumn
mdmProfileXmitLevel = _MdmProfileXmitLevel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 11),
    _MdmProfileXmitLevel_Type()
)
mdmProfileXmitLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileXmitLevel.setStatus("mandatory")


class _MdmProfileCDWaitTime_Type(Integer32):
    """Custom type mdmProfileCDWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 255000),
    )


_MdmProfileCDWaitTime_Type.__name__ = "Integer32"
_MdmProfileCDWaitTime_Object = MibTableColumn
mdmProfileCDWaitTime = _MdmProfileCDWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 12),
    _MdmProfileCDWaitTime_Type()
)
mdmProfileCDWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileCDWaitTime.setStatus("mandatory")


class _MdmProfileCDRespTime_Type(Integer32):
    """Custom type mdmProfileCDRespTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 25500),
    )


_MdmProfileCDRespTime_Type.__name__ = "Integer32"
_MdmProfileCDRespTime_Object = MibTableColumn
mdmProfileCDRespTime = _MdmProfileCDRespTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 13),
    _MdmProfileCDRespTime_Type()
)
mdmProfileCDRespTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileCDRespTime.setStatus("mandatory")


class _MdmProfileCDDiscTime_Type(Integer32):
    """Custom type mdmProfileCDDiscTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 25500),
    )


_MdmProfileCDDiscTime_Type.__name__ = "Integer32"
_MdmProfileCDDiscTime_Object = MibTableColumn
mdmProfileCDDiscTime = _MdmProfileCDDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 14),
    _MdmProfileCDDiscTime_Type()
)
mdmProfileCDDiscTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileCDDiscTime.setStatus("mandatory")


class _MdmProfileRetrain_Type(Integer32):
    """Custom type mdmProfileRetrain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallbf", 3),
          ("off", 1),
          ("retrain", 2))
    )


_MdmProfileRetrain_Type.__name__ = "Integer32"
_MdmProfileRetrain_Object = MibTableColumn
mdmProfileRetrain = _MdmProfileRetrain_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 15),
    _MdmProfileRetrain_Type()
)
mdmProfileRetrain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileRetrain.setStatus("mandatory")


class _MdmProfileIdleTimerMode_Type(Integer32):
    """Custom type mdmProfileIdleTimerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MdmProfileIdleTimerMode_Type.__name__ = "Integer32"
_MdmProfileIdleTimerMode_Object = MibTableColumn
mdmProfileIdleTimerMode = _MdmProfileIdleTimerMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 16),
    _MdmProfileIdleTimerMode_Type()
)
mdmProfileIdleTimerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileIdleTimerMode.setStatus("mandatory")


class _MdmProfileIdleTimerFixedDelay_Type(Integer32):
    """Custom type mdmProfileIdleTimerFixedDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_MdmProfileIdleTimerFixedDelay_Type.__name__ = "Integer32"
_MdmProfileIdleTimerFixedDelay_Object = MibTableColumn
mdmProfileIdleTimerFixedDelay = _MdmProfileIdleTimerFixedDelay_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 17),
    _MdmProfileIdleTimerFixedDelay_Type()
)
mdmProfileIdleTimerFixedDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileIdleTimerFixedDelay.setStatus("mandatory")


class _MdmProfileIdleTimerCharDelay_Type(Integer32):
    """Custom type mdmProfileIdleTimerCharDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MdmProfileIdleTimerCharDelay_Type.__name__ = "Integer32"
_MdmProfileIdleTimerCharDelay_Object = MibTableColumn
mdmProfileIdleTimerCharDelay = _MdmProfileIdleTimerCharDelay_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 1, 1, 18),
    _MdmProfileIdleTimerCharDelay_Type()
)
mdmProfileIdleTimerCharDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmProfileIdleTimerCharDelay.setStatus("mandatory")
_MdmTable_Object = MibTable
mdmTable = _MdmTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2)
)
if mibBuilder.loadTexts:
    mdmTable.setStatus("mandatory")
_MdmEntry_Object = MibTableRow
mdmEntry = _MdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2, 1)
)
mdmEntry.setIndexNames(
    (0, "BIANCA-BRICK-MIBMODEM-MIB", "mdmIndex"),
)
if mibBuilder.loadTexts:
    mdmEntry.setStatus("mandatory")
_MdmIndex_Type = Integer32
_MdmIndex_Object = MibTableColumn
mdmIndex = _MdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2, 1, 1),
    _MdmIndex_Type()
)
mdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIndex.setStatus("mandatory")


class _MdmAction_Type(Integer32):
    """Custom type mdmAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("reboot", 1))
    )


_MdmAction_Type.__name__ = "Integer32"
_MdmAction_Object = MibTableColumn
mdmAction = _MdmAction_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2, 1, 2),
    _MdmAction_Type()
)
mdmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmAction.setStatus("mandatory")


class _MdmType_Type(Integer32):
    """Custom type mdmType based on Integer32"""
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
        *(("csm336", 2),
          ("csm56K", 1),
          ("mdm144", 3),
          ("mdm336", 4),
          ("telindus", 5))
    )


_MdmType_Type.__name__ = "Integer32"
_MdmType_Object = MibTableColumn
mdmType = _MdmType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2, 1, 3),
    _MdmType_Type()
)
mdmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmType.setStatus("mandatory")


class _MdmState_Type(Integer32):
    """Custom type mdmState based on Integer32"""
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
        *(("booting", 1),
          ("called", 4),
          ("calling", 3),
          ("connected", 5),
          ("hangup", 6),
          ("idle", 2),
          ("stopped", 7))
    )


_MdmState_Type.__name__ = "Integer32"
_MdmState_Object = MibTableColumn
mdmState = _MdmState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2, 1, 4),
    _MdmState_Type()
)
mdmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmState.setStatus("mandatory")


class _MdmMode_Type(Integer32):
    """Custom type mdmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 4),
          ("fax", 3),
          ("modem", 1),
          ("none", 7),
          ("ppp", 2))
    )


_MdmMode_Type.__name__ = "Integer32"
_MdmMode_Object = MibTableColumn
mdmMode = _MdmMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2, 1, 5),
    _MdmMode_Type()
)
mdmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmMode.setStatus("mandatory")


class _MdmModulation_Type(Integer32):
    """Custom type mdmModulation based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("bell103", 1),
          ("bell212", 2),
          ("k56flex", 10),
          ("unknown", 31),
          ("v21", 3),
          ("v22", 4),
          ("v22bis", 5),
          ("v23", 6),
          ("v32", 7),
          ("v32bis", 8),
          ("v34", 9),
          ("v90", 12),
          ("vfc", 11))
    )


_MdmModulation_Type.__name__ = "Integer32"
_MdmModulation_Object = MibTableColumn
mdmModulation = _MdmModulation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2, 1, 6),
    _MdmModulation_Type()
)
mdmModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModulation.setStatus("mandatory")


class _MdmErrorCorr_Type(Integer32):
    """Custom type mdmErrorCorr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alt", 2),
          ("lapm", 3),
          ("none", 1))
    )


_MdmErrorCorr_Type.__name__ = "Integer32"
_MdmErrorCorr_Object = MibTableColumn
mdmErrorCorr = _MdmErrorCorr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2, 1, 7),
    _MdmErrorCorr_Type()
)
mdmErrorCorr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmErrorCorr.setStatus("mandatory")


class _MdmCompression_Type(Integer32):
    """Custom type mdmCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("class5", 2),
          ("none", 1),
          ("v42bis", 3))
    )


_MdmCompression_Type.__name__ = "Integer32"
_MdmCompression_Object = MibTableColumn
mdmCompression = _MdmCompression_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2, 1, 8),
    _MdmCompression_Type()
)
mdmCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCompression.setStatus("mandatory")
_MdmXmitSpeed_Type = Integer32
_MdmXmitSpeed_Object = MibTableColumn
mdmXmitSpeed = _MdmXmitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2, 1, 9),
    _MdmXmitSpeed_Type()
)
mdmXmitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmXmitSpeed.setStatus("mandatory")
_MdmRcvSpeed_Type = Integer32
_MdmRcvSpeed_Object = MibTableColumn
mdmRcvSpeed = _MdmRcvSpeed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2, 1, 10),
    _MdmRcvSpeed_Type()
)
mdmRcvSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRcvSpeed.setStatus("mandatory")
_MdmIfIndex_Type = Integer32
_MdmIfIndex_Object = MibTableColumn
mdmIfIndex = _MdmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2, 1, 11),
    _MdmIfIndex_Type()
)
mdmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIfIndex.setStatus("mandatory")


class _MdmIfBchannel_Type(Integer32):
    """Custom type mdmIfBchannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MdmIfBchannel_Type.__name__ = "Integer32"
_MdmIfBchannel_Object = MibTableColumn
mdmIfBchannel = _MdmIfBchannel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 18, 2, 1, 12),
    _MdmIfBchannel_Type()
)
mdmIfBchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIfBchannel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-MIBMODEM-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "mdm": mdm,
       "mdmProfileTable": mdmProfileTable,
       "mdmProfileEntry": mdmProfileEntry,
       "mdmProfileName": mdmProfileName,
       "mdmProfileDescr": mdmProfileDescr,
       "mdmProfileModulation": mdmProfileModulation,
       "mdmProfileMinBps": mdmProfileMinBps,
       "mdmProfileMaxRecvBps": mdmProfileMaxRecvBps,
       "mdmProfileMaxXmitBps": mdmProfileMaxXmitBps,
       "mdmProfileAutoMode": mdmProfileAutoMode,
       "mdmProfileComprV42bis": mdmProfileComprV42bis,
       "mdmProfileComprMNP5": mdmProfileComprMNP5,
       "mdmProfileErrorCorr": mdmProfileErrorCorr,
       "mdmProfileXmitLevel": mdmProfileXmitLevel,
       "mdmProfileCDWaitTime": mdmProfileCDWaitTime,
       "mdmProfileCDRespTime": mdmProfileCDRespTime,
       "mdmProfileCDDiscTime": mdmProfileCDDiscTime,
       "mdmProfileRetrain": mdmProfileRetrain,
       "mdmProfileIdleTimerMode": mdmProfileIdleTimerMode,
       "mdmProfileIdleTimerFixedDelay": mdmProfileIdleTimerFixedDelay,
       "mdmProfileIdleTimerCharDelay": mdmProfileIdleTimerCharDelay,
       "mdmTable": mdmTable,
       "mdmEntry": mdmEntry,
       "mdmIndex": mdmIndex,
       "mdmAction": mdmAction,
       "mdmType": mdmType,
       "mdmState": mdmState,
       "mdmMode": mdmMode,
       "mdmModulation": mdmModulation,
       "mdmErrorCorr": mdmErrorCorr,
       "mdmCompression": mdmCompression,
       "mdmXmitSpeed": mdmXmitSpeed,
       "mdmRcvSpeed": mdmRcvSpeed,
       "mdmIfIndex": mdmIfIndex,
       "mdmIfBchannel": mdmIfBchannel}
)
