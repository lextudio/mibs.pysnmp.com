# SNMP MIB module (E5-111-AESCOMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/E5-111-AESCOMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:07 2024
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

(aesSeriesCommon,) = mibBuilder.importSymbols(
    "E5-111-MIB",
    "aesSeriesCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

_AesMaxNumOfProfiles_Type = Integer32
_AesMaxNumOfProfiles_Object = MibScalar
aesMaxNumOfProfiles = _AesMaxNumOfProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 1),
    _AesMaxNumOfProfiles_Type()
)
aesMaxNumOfProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesMaxNumOfProfiles.setStatus("current")
_AesLineConfTable_Object = MibTable
aesLineConfTable = _AesLineConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 2)
)
if mibBuilder.loadTexts:
    aesLineConfTable.setStatus("current")
_AesLineConfEntry_Object = MibTableRow
aesLineConfEntry = _AesLineConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 2, 1)
)
aesLineConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aesLineConfEntry.setStatus("current")


class _AesLineConfAdslMode_Type(Integer32):
    """Custom type aesLineConfAdslMode based on Integer32"""
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
        *(("adsl2", 6),
          ("adsl2Plus", 7),
          ("auto", 4),
          ("etsi", 5),
          ("gDotDmt", 2),
          ("gDotLite", 1),
          ("t1Dot413", 3))
    )


_AesLineConfAdslMode_Type.__name__ = "Integer32"
_AesLineConfAdslMode_Object = MibTableColumn
aesLineConfAdslMode = _AesLineConfAdslMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 2, 1, 1),
    _AesLineConfAdslMode_Type()
)
aesLineConfAdslMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfAdslMode.setStatus("current")


class _AesLineConfEncap_Type(Integer32):
    """Custom type aesLineConfEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_AesLineConfEncap_Type.__name__ = "Integer32"
_AesLineConfEncap_Object = MibTableColumn
aesLineConfEncap = _AesLineConfEncap_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 2, 1, 2),
    _AesLineConfEncap_Type()
)
aesLineConfEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfEncap.setStatus("current")
_AesLineConfVpi_Type = Integer32
_AesLineConfVpi_Object = MibTableColumn
aesLineConfVpi = _AesLineConfVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 2, 1, 3),
    _AesLineConfVpi_Type()
)
aesLineConfVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfVpi.setStatus("current")
_AesLineConfVci_Type = Integer32
_AesLineConfVci_Object = MibTableColumn
aesLineConfVci = _AesLineConfVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 2, 1, 4),
    _AesLineConfVci_Type()
)
aesLineConfVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfVci.setStatus("current")


class _AesLineConfAnnexL_Type(Integer32):
    """Custom type aesLineConfAnnexL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enableNarrowMode", 1),
          ("enableWideMode", 2))
    )


_AesLineConfAnnexL_Type.__name__ = "Integer32"
_AesLineConfAnnexL_Object = MibTableColumn
aesLineConfAnnexL = _AesLineConfAnnexL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 2, 1, 5),
    _AesLineConfAnnexL_Type()
)
aesLineConfAnnexL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfAnnexL.setStatus("current")


class _AesLineConfPmMode_Type(Integer32):
    """Custom type aesLineConfPmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enableL2Mode", 2))
    )


_AesLineConfPmMode_Type.__name__ = "Integer32"
_AesLineConfPmMode_Object = MibTableColumn
aesLineConfPmMode = _AesLineConfPmMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 2, 1, 6),
    _AesLineConfPmMode_Type()
)
aesLineConfPmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfPmMode.setStatus("current")


class _AesLineConfRateMode_Type(Integer32):
    """Custom type aesLineConfRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptAtRuntime", 3),
          ("adaptAtStartup", 2),
          ("fixed", 1))
    )


_AesLineConfRateMode_Type.__name__ = "Integer32"
_AesLineConfRateMode_Object = MibTableColumn
aesLineConfRateMode = _AesLineConfRateMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 2, 1, 7),
    _AesLineConfRateMode_Type()
)
aesLineConfRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfRateMode.setStatus("current")


class _AesLineConfAnnexM_Type(Integer32):
    """Custom type aesLineConfAnnexM based on Integer32"""
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


_AesLineConfAnnexM_Type.__name__ = "Integer32"
_AesLineConfAnnexM_Object = MibTableColumn
aesLineConfAnnexM = _AesLineConfAnnexM_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 2, 1, 8),
    _AesLineConfAnnexM_Type()
)
aesLineConfAnnexM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineConfAnnexM.setStatus("current")
_AesLineDiagnostic_ObjectIdentity = ObjectIdentity
aesLineDiagnostic = _AesLineDiagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3)
)
_AesAtucLineDiagLATN_Type = Integer32
_AesAtucLineDiagLATN_Object = MibScalar
aesAtucLineDiagLATN = _AesAtucLineDiagLATN_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3, 1),
    _AesAtucLineDiagLATN_Type()
)
aesAtucLineDiagLATN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAtucLineDiagLATN.setStatus("current")
if mibBuilder.loadTexts:
    aesAtucLineDiagLATN.setUnits("tenth dB")
_AesAtucLineDiagSATN_Type = Integer32
_AesAtucLineDiagSATN_Object = MibScalar
aesAtucLineDiagSATN = _AesAtucLineDiagSATN_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3, 2),
    _AesAtucLineDiagSATN_Type()
)
aesAtucLineDiagSATN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAtucLineDiagSATN.setStatus("current")
if mibBuilder.loadTexts:
    aesAtucLineDiagSATN.setUnits("tenth dB")
_AesAtucLineDiagSNRM_Type = Integer32
_AesAtucLineDiagSNRM_Object = MibScalar
aesAtucLineDiagSNRM = _AesAtucLineDiagSNRM_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3, 3),
    _AesAtucLineDiagSNRM_Type()
)
aesAtucLineDiagSNRM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAtucLineDiagSNRM.setStatus("current")
if mibBuilder.loadTexts:
    aesAtucLineDiagSNRM.setUnits("tenth dB")
_AesAtucLineDiagACTATP_Type = Integer32
_AesAtucLineDiagACTATP_Object = MibScalar
aesAtucLineDiagACTATP = _AesAtucLineDiagACTATP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3, 4),
    _AesAtucLineDiagACTATP_Type()
)
aesAtucLineDiagACTATP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAtucLineDiagACTATP.setStatus("current")
if mibBuilder.loadTexts:
    aesAtucLineDiagACTATP.setUnits("tenth dB")
_AesAtucLineDiagATTNDR_Type = Unsigned32
_AesAtucLineDiagATTNDR_Object = MibScalar
aesAtucLineDiagATTNDR = _AesAtucLineDiagATTNDR_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3, 5),
    _AesAtucLineDiagATTNDR_Type()
)
aesAtucLineDiagATTNDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAtucLineDiagATTNDR.setStatus("current")
_AesAturLineDiagLATN_Type = Integer32
_AesAturLineDiagLATN_Object = MibScalar
aesAturLineDiagLATN = _AesAturLineDiagLATN_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3, 6),
    _AesAturLineDiagLATN_Type()
)
aesAturLineDiagLATN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAturLineDiagLATN.setStatus("current")
if mibBuilder.loadTexts:
    aesAturLineDiagLATN.setUnits("tenth dB")
_AesAturLineDiagSATN_Type = Integer32
_AesAturLineDiagSATN_Object = MibScalar
aesAturLineDiagSATN = _AesAturLineDiagSATN_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3, 7),
    _AesAturLineDiagSATN_Type()
)
aesAturLineDiagSATN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAturLineDiagSATN.setStatus("current")
if mibBuilder.loadTexts:
    aesAturLineDiagSATN.setUnits("tenth dB")
_AesAturLineDiagSNRM_Type = Integer32
_AesAturLineDiagSNRM_Object = MibScalar
aesAturLineDiagSNRM = _AesAturLineDiagSNRM_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3, 8),
    _AesAturLineDiagSNRM_Type()
)
aesAturLineDiagSNRM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAturLineDiagSNRM.setStatus("current")
if mibBuilder.loadTexts:
    aesAturLineDiagSNRM.setUnits("tenth dB")
_AesAturLineDiagACTATP_Type = Integer32
_AesAturLineDiagACTATP_Object = MibScalar
aesAturLineDiagACTATP = _AesAturLineDiagACTATP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3, 9),
    _AesAturLineDiagACTATP_Type()
)
aesAturLineDiagACTATP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAturLineDiagACTATP.setStatus("current")
if mibBuilder.loadTexts:
    aesAturLineDiagACTATP.setUnits("tenth dB")
_AesAturLineDiagATTNDR_Type = Unsigned32
_AesAturLineDiagATTNDR_Object = MibScalar
aesAturLineDiagATTNDR = _AesAturLineDiagATTNDR_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3, 10),
    _AesAturLineDiagATTNDR_Type()
)
aesAturLineDiagATTNDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAturLineDiagATTNDR.setStatus("current")
_AesLineDiagTarget_Type = Integer32
_AesLineDiagTarget_Object = MibScalar
aesLineDiagTarget = _AesLineDiagTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3, 11),
    _AesLineDiagTarget_Type()
)
aesLineDiagTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineDiagTarget.setStatus("current")
_AesLineDiagOps_Type = Integer32
_AesLineDiagOps_Object = MibScalar
aesLineDiagOps = _AesLineDiagOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3, 12),
    _AesLineDiagOps_Type()
)
aesLineDiagOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesLineDiagOps.setStatus("current")
_AesLineDiagFailReason_Type = DisplayString
_AesLineDiagFailReason_Object = MibScalar
aesLineDiagFailReason = _AesLineDiagFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 3, 13),
    _AesLineDiagFailReason_Type()
)
aesLineDiagFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagFailReason.setStatus("current")
_AesLineDiagPs_ObjectIdentity = ObjectIdentity
aesLineDiagPs = _AesLineDiagPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 4)
)
_AesAtucNumOfSubcarriersPerPort_Type = Integer32
_AesAtucNumOfSubcarriersPerPort_Object = MibScalar
aesAtucNumOfSubcarriersPerPort = _AesAtucNumOfSubcarriersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 4, 1),
    _AesAtucNumOfSubcarriersPerPort_Type()
)
aesAtucNumOfSubcarriersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAtucNumOfSubcarriersPerPort.setStatus("current")
_AesAturNumOfSubcarriersPerPort_Type = Integer32
_AesAturNumOfSubcarriersPerPort_Object = MibScalar
aesAturNumOfSubcarriersPerPort = _AesAturNumOfSubcarriersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 4, 2),
    _AesAturNumOfSubcarriersPerPort_Type()
)
aesAturNumOfSubcarriersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesAturNumOfSubcarriersPerPort.setStatus("current")
_AesLineDiagPsCCFLirl1_Type = OctetString
_AesLineDiagPsCCFLirl1_Object = MibScalar
aesLineDiagPsCCFLirl1 = _AesLineDiagPsCCFLirl1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 4, 3),
    _AesLineDiagPsCCFLirl1_Type()
)
aesLineDiagPsCCFLirl1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsCCFLirl1.setStatus("current")
_AesLineDiagPsCCFLirl2_Type = OctetString
_AesLineDiagPsCCFLirl2_Object = MibScalar
aesLineDiagPsCCFLirl2 = _AesLineDiagPsCCFLirl2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 4, 4),
    _AesLineDiagPsCCFLirl2_Type()
)
aesLineDiagPsCCFLirl2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsCCFLirl2.setStatus("current")
_AesLineDiagPsCCFLiim1_Type = OctetString
_AesLineDiagPsCCFLiim1_Object = MibScalar
aesLineDiagPsCCFLiim1 = _AesLineDiagPsCCFLiim1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 4, 5),
    _AesLineDiagPsCCFLiim1_Type()
)
aesLineDiagPsCCFLiim1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsCCFLiim1.setStatus("current")
_AesLineDiagPsCCFLiim2_Type = OctetString
_AesLineDiagPsCCFLiim2_Object = MibScalar
aesLineDiagPsCCFLiim2 = _AesLineDiagPsCCFLiim2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 4, 6),
    _AesLineDiagPsCCFLiim2_Type()
)
aesLineDiagPsCCFLiim2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsCCFLiim2.setStatus("current")
_AesLineDiagPsCCFLog1_Type = OctetString
_AesLineDiagPsCCFLog1_Object = MibScalar
aesLineDiagPsCCFLog1 = _AesLineDiagPsCCFLog1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 4, 7),
    _AesLineDiagPsCCFLog1_Type()
)
aesLineDiagPsCCFLog1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsCCFLog1.setStatus("current")
_AesLineDiagPsCCFLog2_Type = OctetString
_AesLineDiagPsCCFLog2_Object = MibScalar
aesLineDiagPsCCFLog2 = _AesLineDiagPsCCFLog2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 4, 8),
    _AesLineDiagPsCCFLog2_Type()
)
aesLineDiagPsCCFLog2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsCCFLog2.setStatus("current")
_AesLineDiagPsQLN_Type = OctetString
_AesLineDiagPsQLN_Object = MibScalar
aesLineDiagPsQLN = _AesLineDiagPsQLN_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 4, 9),
    _AesLineDiagPsQLN_Type()
)
aesLineDiagPsQLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsQLN.setStatus("current")
if mibBuilder.loadTexts:
    aesLineDiagPsQLN.setUnits("tenth dB")
_AesLineDiagPsSNR_Type = OctetString
_AesLineDiagPsSNR_Object = MibScalar
aesLineDiagPsSNR = _AesLineDiagPsSNR_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 4, 10),
    _AesLineDiagPsSNR_Type()
)
aesLineDiagPsSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineDiagPsSNR.setStatus("current")
if mibBuilder.loadTexts:
    aesLineDiagPsSNR.setUnits("tenth dB")
_AesMaxNumOfAlarmProfiles_Type = Integer32
_AesMaxNumOfAlarmProfiles_Object = MibScalar
aesMaxNumOfAlarmProfiles = _AesMaxNumOfAlarmProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 5),
    _AesMaxNumOfAlarmProfiles_Type()
)
aesMaxNumOfAlarmProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesMaxNumOfAlarmProfiles.setStatus("current")
_AesBitLoadingTable_Object = MibTable
aesBitLoadingTable = _AesBitLoadingTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 6)
)
if mibBuilder.loadTexts:
    aesBitLoadingTable.setStatus("current")
_AesBitLoadingEntry_Object = MibTableRow
aesBitLoadingEntry = _AesBitLoadingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 6, 1)
)
aesBitLoadingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aesBitLoadingEntry.setStatus("current")
_AesBitLoadingBits_Type = OctetString
_AesBitLoadingBits_Object = MibTableColumn
aesBitLoadingBits = _AesBitLoadingBits_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 6, 1, 1),
    _AesBitLoadingBits_Type()
)
aesBitLoadingBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesBitLoadingBits.setStatus("current")
_AesBitLoadingAtucNumOfCarriers_Type = Integer32
_AesBitLoadingAtucNumOfCarriers_Object = MibTableColumn
aesBitLoadingAtucNumOfCarriers = _AesBitLoadingAtucNumOfCarriers_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 6, 1, 2),
    _AesBitLoadingAtucNumOfCarriers_Type()
)
aesBitLoadingAtucNumOfCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesBitLoadingAtucNumOfCarriers.setStatus("current")
_AesBitLoadingAturNumOfCarriers_Type = Integer32
_AesBitLoadingAturNumOfCarriers_Object = MibTableColumn
aesBitLoadingAturNumOfCarriers = _AesBitLoadingAturNumOfCarriers_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 6, 1, 3),
    _AesBitLoadingAturNumOfCarriers_Type()
)
aesBitLoadingAturNumOfCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesBitLoadingAturNumOfCarriers.setStatus("current")
_AesLineStatusTable_Object = MibTable
aesLineStatusTable = _AesLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 7)
)
if mibBuilder.loadTexts:
    aesLineStatusTable.setStatus("current")
_AesLineStatusEntry_Object = MibTableRow
aesLineStatusEntry = _AesLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 7, 1)
)
aesLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aesLineStatusEntry.setStatus("current")


class _AesLineStatusAdslMode_Type(Integer32):
    """Custom type aesLineStatusAdslMode based on Integer32"""
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
        *(("adsl2", 5),
          ("adsl2Plus", 6),
          ("etsi", 4),
          ("gDotDmt", 2),
          ("gDotLite", 1),
          ("t1Dot413", 3))
    )


_AesLineStatusAdslMode_Type.__name__ = "Integer32"
_AesLineStatusAdslMode_Object = MibTableColumn
aesLineStatusAdslMode = _AesLineStatusAdslMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 7, 1, 1),
    _AesLineStatusAdslMode_Type()
)
aesLineStatusAdslMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aesLineStatusAdslMode.setStatus("current")
_Selt_ObjectIdentity = ObjectIdentity
selt = _Selt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 8)
)
_SeltTarget_Type = Integer32
_SeltTarget_Object = MibScalar
seltTarget = _SeltTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 8, 1),
    _SeltTarget_Type()
)
seltTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltTarget.setStatus("current")
_SeltOps_Type = Integer32
_SeltOps_Object = MibScalar
seltOps = _SeltOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 8, 2),
    _SeltOps_Type()
)
seltOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    seltOps.setStatus("current")
_SeltStatus_Type = DisplayString
_SeltStatus_Object = MibScalar
seltStatus = _SeltStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 8, 3),
    _SeltStatus_Type()
)
seltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltStatus.setStatus("current")


class _SeltCableType_Type(Integer32):
    """Custom type seltCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("awg24", 1),
          ("awg26", 2))
    )


_SeltCableType_Type.__name__ = "Integer32"
_SeltCableType_Object = MibScalar
seltCableType = _SeltCableType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 8, 4),
    _SeltCableType_Type()
)
seltCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltCableType.setStatus("current")
_SeltLoopEstimateLengthFt_Type = Integer32
_SeltLoopEstimateLengthFt_Object = MibScalar
seltLoopEstimateLengthFt = _SeltLoopEstimateLengthFt_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 8, 5),
    _SeltLoopEstimateLengthFt_Type()
)
seltLoopEstimateLengthFt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthFt.setStatus("current")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthFt.setUnits("feet")
_SeltLoopEstimateLengthMeter_Type = Integer32
_SeltLoopEstimateLengthMeter_Object = MibScalar
seltLoopEstimateLengthMeter = _SeltLoopEstimateLengthMeter_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 97, 8, 6),
    _SeltLoopEstimateLengthMeter_Type()
)
seltLoopEstimateLengthMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setStatus("current")
if mibBuilder.loadTexts:
    seltLoopEstimateLengthMeter.setUnits("meter")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "E5-111-AESCOMMON-MIB",
    **{"aesMaxNumOfProfiles": aesMaxNumOfProfiles,
       "aesLineConfTable": aesLineConfTable,
       "aesLineConfEntry": aesLineConfEntry,
       "aesLineConfAdslMode": aesLineConfAdslMode,
       "aesLineConfEncap": aesLineConfEncap,
       "aesLineConfVpi": aesLineConfVpi,
       "aesLineConfVci": aesLineConfVci,
       "aesLineConfAnnexL": aesLineConfAnnexL,
       "aesLineConfPmMode": aesLineConfPmMode,
       "aesLineConfRateMode": aesLineConfRateMode,
       "aesLineConfAnnexM": aesLineConfAnnexM,
       "aesLineDiagnostic": aesLineDiagnostic,
       "aesAtucLineDiagLATN": aesAtucLineDiagLATN,
       "aesAtucLineDiagSATN": aesAtucLineDiagSATN,
       "aesAtucLineDiagSNRM": aesAtucLineDiagSNRM,
       "aesAtucLineDiagACTATP": aesAtucLineDiagACTATP,
       "aesAtucLineDiagATTNDR": aesAtucLineDiagATTNDR,
       "aesAturLineDiagLATN": aesAturLineDiagLATN,
       "aesAturLineDiagSATN": aesAturLineDiagSATN,
       "aesAturLineDiagSNRM": aesAturLineDiagSNRM,
       "aesAturLineDiagACTATP": aesAturLineDiagACTATP,
       "aesAturLineDiagATTNDR": aesAturLineDiagATTNDR,
       "aesLineDiagTarget": aesLineDiagTarget,
       "aesLineDiagOps": aesLineDiagOps,
       "aesLineDiagFailReason": aesLineDiagFailReason,
       "aesLineDiagPs": aesLineDiagPs,
       "aesAtucNumOfSubcarriersPerPort": aesAtucNumOfSubcarriersPerPort,
       "aesAturNumOfSubcarriersPerPort": aesAturNumOfSubcarriersPerPort,
       "aesLineDiagPsCCFLirl1": aesLineDiagPsCCFLirl1,
       "aesLineDiagPsCCFLirl2": aesLineDiagPsCCFLirl2,
       "aesLineDiagPsCCFLiim1": aesLineDiagPsCCFLiim1,
       "aesLineDiagPsCCFLiim2": aesLineDiagPsCCFLiim2,
       "aesLineDiagPsCCFLog1": aesLineDiagPsCCFLog1,
       "aesLineDiagPsCCFLog2": aesLineDiagPsCCFLog2,
       "aesLineDiagPsQLN": aesLineDiagPsQLN,
       "aesLineDiagPsSNR": aesLineDiagPsSNR,
       "aesMaxNumOfAlarmProfiles": aesMaxNumOfAlarmProfiles,
       "aesBitLoadingTable": aesBitLoadingTable,
       "aesBitLoadingEntry": aesBitLoadingEntry,
       "aesBitLoadingBits": aesBitLoadingBits,
       "aesBitLoadingAtucNumOfCarriers": aesBitLoadingAtucNumOfCarriers,
       "aesBitLoadingAturNumOfCarriers": aesBitLoadingAturNumOfCarriers,
       "aesLineStatusTable": aesLineStatusTable,
       "aesLineStatusEntry": aesLineStatusEntry,
       "aesLineStatusAdslMode": aesLineStatusAdslMode,
       "selt": selt,
       "seltTarget": seltTarget,
       "seltOps": seltOps,
       "seltStatus": seltStatus,
       "seltCableType": seltCableType,
       "seltLoopEstimateLengthFt": seltLoopEstimateLengthFt,
       "seltLoopEstimateLengthMeter": seltLoopEstimateLengthMeter}
)
