# SNMP MIB module (CISCO-DMN-DSG-DR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-DR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:22 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGDR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43)
)
ciscoDSGDR.setRevisions(
        ("2014-08-30 08:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DrGlobalCfg_ObjectIdentity = ObjectIdentity
drGlobalCfg = _DrGlobalCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 1)
)


class _Enable_Type(Integer32):
    """Custom type enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Enable_Type.__name__ = "Integer32"
_Enable_Object = MibScalar
enable = _Enable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 1, 1),
    _Enable_Type()
)
enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable.setStatus("current")


class _SigLockTime_Type(Integer32):
    """Custom type sigLockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_SigLockTime_Type.__name__ = "Integer32"
_SigLockTime_Object = MibScalar
sigLockTime = _SigLockTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 1, 2),
    _SigLockTime_Type()
)
sigLockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigLockTime.setStatus("current")


class _SigLossTime_Type(Integer32):
    """Custom type sigLossTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2160000),
    )


_SigLossTime_Type.__name__ = "Integer32"
_SigLossTime_Object = MibScalar
sigLossTime = _SigLossTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 1, 3),
    _SigLossTime_Type()
)
sigLossTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigLossTime.setStatus("current")


class _VerifyTimer_Type(Integer32):
    """Custom type verifyTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_VerifyTimer_Type.__name__ = "Integer32"
_VerifyTimer_Object = MibScalar
verifyTimer = _VerifyTimer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 1, 4),
    _VerifyTimer_Type()
)
verifyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    verifyTimer.setStatus("current")


class _Profile_Type(Integer32):
    """Custom type profile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("uplink", 2))
    )


_Profile_Type.__name__ = "Integer32"
_Profile_Object = MibScalar
profile = _Profile_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 1, 5),
    _Profile_Type()
)
profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profile.setStatus("current")
_BackupTransportTable_Object = MibTable
backupTransportTable = _BackupTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2)
)
if mibBuilder.loadTexts:
    backupTransportTable.setStatus("current")
_BackupTransportEntry_Object = MibTableRow
backupTransportEntry = _BackupTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1)
)
backupTransportEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-DR-MIB", "backupTransportIndex"),
)
if mibBuilder.loadTexts:
    backupTransportEntry.setStatus("current")


class _BackupTransportIndex_Type(Integer32):
    """Custom type backupTransportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BackupTransportIndex_Type.__name__ = "Integer32"
_BackupTransportIndex_Object = MibTableColumn
backupTransportIndex = _BackupTransportIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 1),
    _BackupTransportIndex_Type()
)
backupTransportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupTransportIndex.setStatus("current")


class _BackupTransportSetIdx_Type(Integer32):
    """Custom type backupTransportSetIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BackupTransportSetIdx_Type.__name__ = "Integer32"
_BackupTransportSetIdx_Object = MibTableColumn
backupTransportSetIdx = _BackupTransportSetIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 2),
    _BackupTransportSetIdx_Type()
)
backupTransportSetIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupTransportSetIdx.setStatus("current")


class _BackupTransportDvbsFec_Type(Integer32):
    """Custom type backupTransportDvbsFec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              6,
              7,
              10)
        )
    )
    namedValues = NamedValues(
        *(("auto", 10),
          ("fiveSixths", 6),
          ("oneHalf", 1),
          ("sevenEigths", 7),
          ("threeQuarters", 4),
          ("twoThirds", 3))
    )


_BackupTransportDvbsFec_Type.__name__ = "Integer32"
_BackupTransportDvbsFec_Object = MibTableColumn
backupTransportDvbsFec = _BackupTransportDvbsFec_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 3),
    _BackupTransportDvbsFec_Type()
)
backupTransportDvbsFec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupTransportDvbsFec.setStatus("current")


class _BackupTransportEwFlag_Type(Integer32):
    """Custom type backupTransportEwFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 1),
          ("notApplicable", 3),
          ("west", 2))
    )


_BackupTransportEwFlag_Type.__name__ = "Integer32"
_BackupTransportEwFlag_Object = MibTableColumn
backupTransportEwFlag = _BackupTransportEwFlag_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 4),
    _BackupTransportEwFlag_Type()
)
backupTransportEwFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupTransportEwFlag.setStatus("current")


class _BackupTransportFrequency_Type(Integer32):
    """Custom type backupTransportFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000000),
    )


_BackupTransportFrequency_Type.__name__ = "Integer32"
_BackupTransportFrequency_Object = MibTableColumn
backupTransportFrequency = _BackupTransportFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 5),
    _BackupTransportFrequency_Type()
)
backupTransportFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupTransportFrequency.setStatus("current")


class _BackupTransportRFInput_Type(Integer32):
    """Custom type backupTransportRFInput based on Integer32"""
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
        *(("rf1", 1),
          ("rf2", 2),
          ("rf3", 3),
          ("rf4", 4))
    )


_BackupTransportRFInput_Type.__name__ = "Integer32"
_BackupTransportRFInput_Object = MibTableColumn
backupTransportRFInput = _BackupTransportRFInput_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 6),
    _BackupTransportRFInput_Type()
)
backupTransportRFInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupTransportRFInput.setStatus("current")


class _BackupTransportModSys_Type(Integer32):
    """Custom type backupTransportModSys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qpsk_dvb-S2", 2),
          ("qpsk_dvb-s", 1))
    )


_BackupTransportModSys_Type.__name__ = "Integer32"
_BackupTransportModSys_Object = MibTableColumn
backupTransportModSys = _BackupTransportModSys_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 7),
    _BackupTransportModSys_Type()
)
backupTransportModSys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupTransportModSys.setStatus("current")


class _BackupTransportNetId_Type(Integer32):
    """Custom type backupTransportNetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BackupTransportNetId_Type.__name__ = "Integer32"
_BackupTransportNetId_Object = MibTableColumn
backupTransportNetId = _BackupTransportNetId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 8),
    _BackupTransportNetId_Type()
)
backupTransportNetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupTransportNetId.setStatus("current")


class _BackupTransportOrbitalPos_Type(Integer32):
    """Custom type backupTransportOrbitalPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_BackupTransportOrbitalPos_Type.__name__ = "Integer32"
_BackupTransportOrbitalPos_Object = MibTableColumn
backupTransportOrbitalPos = _BackupTransportOrbitalPos_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 9),
    _BackupTransportOrbitalPos_Type()
)
backupTransportOrbitalPos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupTransportOrbitalPos.setStatus("current")


class _BackupTransportOrbpolarization_Type(Integer32):
    """Custom type backupTransportOrbpolarization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_BackupTransportOrbpolarization_Type.__name__ = "Integer32"
_BackupTransportOrbpolarization_Object = MibTableColumn
backupTransportOrbpolarization = _BackupTransportOrbpolarization_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 10),
    _BackupTransportOrbpolarization_Type()
)
backupTransportOrbpolarization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupTransportOrbpolarization.setStatus("current")


class _BackupTransportSymbRate_Type(Integer32):
    """Custom type backupTransportSymbRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 450000),
    )


_BackupTransportSymbRate_Type.__name__ = "Integer32"
_BackupTransportSymbRate_Object = MibTableColumn
backupTransportSymbRate = _BackupTransportSymbRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 11),
    _BackupTransportSymbRate_Type()
)
backupTransportSymbRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupTransportSymbRate.setStatus("current")


class _BackupTransportRollOffFactor_Type(Integer32):
    """Custom type backupTransportRollOffFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              25)
        )
    )
    namedValues = NamedValues(
        *(("f20", 3),
          ("f25", 25),
          ("f35", 1))
    )


_BackupTransportRollOffFactor_Type.__name__ = "Integer32"
_BackupTransportRollOffFactor_Object = MibTableColumn
backupTransportRollOffFactor = _BackupTransportRollOffFactor_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 12),
    _BackupTransportRollOffFactor_Type()
)
backupTransportRollOffFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupTransportRollOffFactor.setStatus("current")


class _BackupTransportRowstatus_Type(Integer32):
    """Custom type backupTransportRowstatus based on Integer32"""
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
          ("add", 4),
          ("delete", 3),
          ("inactive", 2))
    )


_BackupTransportRowstatus_Type.__name__ = "Integer32"
_BackupTransportRowstatus_Object = MibTableColumn
backupTransportRowstatus = _BackupTransportRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 13),
    _BackupTransportRowstatus_Type()
)
backupTransportRowstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupTransportRowstatus.setStatus("current")
_BackupSetTable_Object = MibTable
backupSetTable = _BackupSetTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3)
)
if mibBuilder.loadTexts:
    backupSetTable.setStatus("current")
_BackupSetEntry_Object = MibTableRow
backupSetEntry = _BackupSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1)
)
backupSetEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-DR-MIB", "backupSetPeid"),
    (0, "CISCO-DMN-DSG-DR-MIB", "backupSetRecid"),
)
if mibBuilder.loadTexts:
    backupSetEntry.setStatus("current")


class _BackupSetPeid_Type(Integer32):
    """Custom type backupSetPeid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BackupSetPeid_Type.__name__ = "Integer32"
_BackupSetPeid_Object = MibTableColumn
backupSetPeid = _BackupSetPeid_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1, 1),
    _BackupSetPeid_Type()
)
backupSetPeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupSetPeid.setStatus("current")


class _BackupSetRecid_Type(Integer32):
    """Custom type backupSetRecid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BackupSetRecid_Type.__name__ = "Integer32"
_BackupSetRecid_Object = MibTableColumn
backupSetRecid = _BackupSetRecid_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1, 2),
    _BackupSetRecid_Type()
)
backupSetRecid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupSetRecid.setStatus("current")


class _BackupSetCsiidx_Type(Integer32):
    """Custom type backupSetCsiidx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BackupSetCsiidx_Type.__name__ = "Integer32"
_BackupSetCsiidx_Object = MibTableColumn
backupSetCsiidx = _BackupSetCsiidx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1, 3),
    _BackupSetCsiidx_Type()
)
backupSetCsiidx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupSetCsiidx.setStatus("current")


class _BackupSetBkpch_Type(Integer32):
    """Custom type backupSetBkpch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BackupSetBkpch_Type.__name__ = "Integer32"
_BackupSetBkpch_Object = MibTableColumn
backupSetBkpch = _BackupSetBkpch_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1, 4),
    _BackupSetBkpch_Type()
)
backupSetBkpch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupSetBkpch.setStatus("current")


class _BackupSetBkpchDispText_Type(DisplayString):
    """Custom type backupSetBkpchDispText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_BackupSetBkpchDispText_Type.__name__ = "DisplayString"
_BackupSetBkpchDispText_Object = MibTableColumn
backupSetBkpchDispText = _BackupSetBkpchDispText_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1, 5),
    _BackupSetBkpchDispText_Type()
)
backupSetBkpchDispText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupSetBkpchDispText.setStatus("current")


class _BackupSetRowStatus_Type(Integer32):
    """Custom type backupSetRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_BackupSetRowStatus_Type.__name__ = "Integer32"
_BackupSetRowStatus_Object = MibTableColumn
backupSetRowStatus = _BackupSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1, 6),
    _BackupSetRowStatus_Type()
)
backupSetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupSetRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-DR-MIB",
    **{"ciscoDSGDR": ciscoDSGDR,
       "drGlobalCfg": drGlobalCfg,
       "enable": enable,
       "sigLockTime": sigLockTime,
       "sigLossTime": sigLossTime,
       "verifyTimer": verifyTimer,
       "profile": profile,
       "backupTransportTable": backupTransportTable,
       "backupTransportEntry": backupTransportEntry,
       "backupTransportIndex": backupTransportIndex,
       "backupTransportSetIdx": backupTransportSetIdx,
       "backupTransportDvbsFec": backupTransportDvbsFec,
       "backupTransportEwFlag": backupTransportEwFlag,
       "backupTransportFrequency": backupTransportFrequency,
       "backupTransportRFInput": backupTransportRFInput,
       "backupTransportModSys": backupTransportModSys,
       "backupTransportNetId": backupTransportNetId,
       "backupTransportOrbitalPos": backupTransportOrbitalPos,
       "backupTransportOrbpolarization": backupTransportOrbpolarization,
       "backupTransportSymbRate": backupTransportSymbRate,
       "backupTransportRollOffFactor": backupTransportRollOffFactor,
       "backupTransportRowstatus": backupTransportRowstatus,
       "backupSetTable": backupSetTable,
       "backupSetEntry": backupSetEntry,
       "backupSetPeid": backupSetPeid,
       "backupSetRecid": backupSetRecid,
       "backupSetCsiidx": backupSetCsiidx,
       "backupSetBkpch": backupSetBkpch,
       "backupSetBkpchDispText": backupSetBkpchDispText,
       "backupSetRowStatus": backupSetRowStatus}
)
