# SNMP MIB module (MADGERSW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MADGERSW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:58 2024
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
 NotificationType,
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
    "NotificationType",
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class INTEGER48(OctetString):
    """Custom type INTEGER48 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class NSAP(OctetString):
    """Custom type NSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )





class TRNMacAddress(OctetString):
    """Custom type TRNMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class ETHMacAddress(OctetString):
    """Custom type ETHMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class RingswitchRowStatus(Integer32):
    """Custom type RingswitchRowStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )





class LCDText(OctetString):
    """Custom type LCDText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Madge_ObjectIdentity = ObjectIdentity
madge = _Madge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494)
)
_Ringswitch_ObjectIdentity = ObjectIdentity
ringswitch = _Ringswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4)
)
_RingswitchBase_ObjectIdentity = ObjectIdentity
ringswitchBase = _RingswitchBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 1)
)
_RingswitchBasePSFanSpeed_Type = Integer32
_RingswitchBasePSFanSpeed_Object = MibScalar
ringswitchBasePSFanSpeed = _RingswitchBasePSFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 1),
    _RingswitchBasePSFanSpeed_Type()
)
ringswitchBasePSFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchBasePSFanSpeed.setStatus("mandatory")
_RingswitchBaseExtFanSpeed_Type = Integer32
_RingswitchBaseExtFanSpeed_Object = MibScalar
ringswitchBaseExtFanSpeed = _RingswitchBaseExtFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 2),
    _RingswitchBaseExtFanSpeed_Type()
)
ringswitchBaseExtFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchBaseExtFanSpeed.setStatus("mandatory")


class _RingswitchBaseRipSapSuppression_Type(Integer32):
    """Custom type ringswitchBaseRipSapSuppression based on Integer32"""
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


_RingswitchBaseRipSapSuppression_Type.__name__ = "Integer32"
_RingswitchBaseRipSapSuppression_Object = MibScalar
ringswitchBaseRipSapSuppression = _RingswitchBaseRipSapSuppression_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 3),
    _RingswitchBaseRipSapSuppression_Type()
)
ringswitchBaseRipSapSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchBaseRipSapSuppression.setStatus("mandatory")


class _RingswitchBaseAREConversion_Type(Integer32):
    """Custom type ringswitchBaseAREConversion based on Integer32"""
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
        *(("disable", 5),
          ("enable-all", 2),
          ("enable-bcast-all", 4),
          ("enable-bcast-first", 3),
          ("enable-first", 1))
    )


_RingswitchBaseAREConversion_Type.__name__ = "Integer32"
_RingswitchBaseAREConversion_Object = MibScalar
ringswitchBaseAREConversion = _RingswitchBaseAREConversion_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 4),
    _RingswitchBaseAREConversion_Type()
)
ringswitchBaseAREConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchBaseAREConversion.setStatus("mandatory")


class _RingswitchBaseStpMode_Type(Integer32):
    """Custom type ringswitchBaseStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ibm-sr", 1),
          ("ieee8021d", 2))
    )


_RingswitchBaseStpMode_Type.__name__ = "Integer32"
_RingswitchBaseStpMode_Object = MibScalar
ringswitchBaseStpMode = _RingswitchBaseStpMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 5),
    _RingswitchBaseStpMode_Type()
)
ringswitchBaseStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchBaseStpMode.setStatus("mandatory")


class _RingswitchBaseRMONState_Type(Integer32):
    """Custom type ringswitchBaseRMONState based on Integer32"""
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


_RingswitchBaseRMONState_Type.__name__ = "Integer32"
_RingswitchBaseRMONState_Object = MibScalar
ringswitchBaseRMONState = _RingswitchBaseRMONState_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 6),
    _RingswitchBaseRMONState_Type()
)
ringswitchBaseRMONState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchBaseRMONState.setStatus("mandatory")


class _RingswitchBaseBackPlaneType_Type(Integer32):
    """Custom type ringswitchBaseBackPlaneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual-psu", 2),
          ("express", 3),
          ("original", 1))
    )


_RingswitchBaseBackPlaneType_Type.__name__ = "Integer32"
_RingswitchBaseBackPlaneType_Object = MibScalar
ringswitchBaseBackPlaneType = _RingswitchBaseBackPlaneType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 7),
    _RingswitchBaseBackPlaneType_Type()
)
ringswitchBaseBackPlaneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchBaseBackPlaneType.setStatus("mandatory")
_RingswitchBaseRMONMirrorPort_Type = Integer32
_RingswitchBaseRMONMirrorPort_Object = MibScalar
ringswitchBaseRMONMirrorPort = _RingswitchBaseRMONMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 8),
    _RingswitchBaseRMONMirrorPort_Type()
)
ringswitchBaseRMONMirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchBaseRMONMirrorPort.setStatus("mandatory")


class _RingswitchBaseTotalResetCounters_Type(Integer32):
    """Custom type ringswitchBaseTotalResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_RingswitchBaseTotalResetCounters_Type.__name__ = "Integer32"
_RingswitchBaseTotalResetCounters_Object = MibScalar
ringswitchBaseTotalResetCounters = _RingswitchBaseTotalResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 9),
    _RingswitchBaseTotalResetCounters_Type()
)
ringswitchBaseTotalResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchBaseTotalResetCounters.setStatus("mandatory")


class _RingswitchBaseDownloadMode_Type(Integer32):
    """Custom type ringswitchBaseDownloadMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("normal", 1))
    )


_RingswitchBaseDownloadMode_Type.__name__ = "Integer32"
_RingswitchBaseDownloadMode_Object = MibScalar
ringswitchBaseDownloadMode = _RingswitchBaseDownloadMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 1, 10),
    _RingswitchBaseDownloadMode_Type()
)
ringswitchBaseDownloadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchBaseDownloadMode.setStatus("mandatory")
_RingswitchPort_ObjectIdentity = ObjectIdentity
ringswitchPort = _RingswitchPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 2)
)
_RingswitchPortTable_Object = MibTable
ringswitchPortTable = _RingswitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ringswitchPortTable.setStatus("mandatory")
_RingswitchPortEntry_Object = MibTableRow
ringswitchPortEntry = _RingswitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1)
)
ringswitchPortEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchPortNum"),
)
if mibBuilder.loadTexts:
    ringswitchPortEntry.setStatus("mandatory")


class _RingswitchPortNum_Type(Integer32):
    """Custom type ringswitchPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchPortNum_Type.__name__ = "Integer32"
_RingswitchPortNum_Object = MibTableColumn
ringswitchPortNum = _RingswitchPortNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 1),
    _RingswitchPortNum_Type()
)
ringswitchPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortNum.setStatus("mandatory")


class _RingswitchPortRingStatus_Type(Integer32):
    """Custom type ringswitchPortRingStatus based on Integer32"""
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
        *(("beaconing", 3),
          ("dtr-wait", 5),
          ("normal", 1),
          ("normal-fdx", 4),
          ("single", 2))
    )


_RingswitchPortRingStatus_Type.__name__ = "Integer32"
_RingswitchPortRingStatus_Object = MibTableColumn
ringswitchPortRingStatus = _RingswitchPortRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 2),
    _RingswitchPortRingStatus_Type()
)
ringswitchPortRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortRingStatus.setStatus("mandatory")


class _RingswitchPortAdapterStatus_Type(Integer32):
    """Custom type ringswitchPortAdapterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1),
          ("opening", 3))
    )


_RingswitchPortAdapterStatus_Type.__name__ = "Integer32"
_RingswitchPortAdapterStatus_Object = MibTableColumn
ringswitchPortAdapterStatus = _RingswitchPortAdapterStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 3),
    _RingswitchPortAdapterStatus_Type()
)
ringswitchPortAdapterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortAdapterStatus.setStatus("mandatory")


class _RingswitchPortMediaType_Type(Integer32):
    """Custom type ringswitchPortMediaType based on Integer32"""
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
        *(("absent", 4),
          ("fddi-fiber", 3),
          ("tr-copper", 1),
          ("tr-fiber", 2))
    )


_RingswitchPortMediaType_Type.__name__ = "Integer32"
_RingswitchPortMediaType_Object = MibTableColumn
ringswitchPortMediaType = _RingswitchPortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 4),
    _RingswitchPortMediaType_Type()
)
ringswitchPortMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortMediaType.setStatus("mandatory")


class _RingswitchPortIfMode_Type(Integer32):
    """Custom type ringswitchPortIfMode based on Integer32"""
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
        *(("conc-classic", 6),
          ("conc-fdx", 4),
          ("concentrator", 2),
          ("node", 1),
          ("node-cau-rio", 7),
          ("node-classic", 5),
          ("node-fdx", 3))
    )


_RingswitchPortIfMode_Type.__name__ = "Integer32"
_RingswitchPortIfMode_Object = MibTableColumn
ringswitchPortIfMode = _RingswitchPortIfMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 5),
    _RingswitchPortIfMode_Type()
)
ringswitchPortIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortIfMode.setStatus("mandatory")


class _RingswitchPortRingSpeed_Type(Integer32):
    """Custom type ringswitchPortRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("four", 1),
          ("hundred", 3),
          ("sixteen", 2))
    )


_RingswitchPortRingSpeed_Type.__name__ = "Integer32"
_RingswitchPortRingSpeed_Object = MibTableColumn
ringswitchPortRingSpeed = _RingswitchPortRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 6),
    _RingswitchPortRingSpeed_Type()
)
ringswitchPortRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortRingSpeed.setStatus("mandatory")


class _RingswitchPortTestState_Type(Integer32):
    """Custom type ringswitchPortTestState based on Integer32"""
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
        *(("disabled", 1),
          ("failed", 3),
          ("ok", 4),
          ("running", 2),
          ("unknown", 5))
    )


_RingswitchPortTestState_Type.__name__ = "Integer32"
_RingswitchPortTestState_Object = MibTableColumn
ringswitchPortTestState = _RingswitchPortTestState_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 7),
    _RingswitchPortTestState_Type()
)
ringswitchPortTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortTestState.setStatus("mandatory")


class _RingswitchPortTestError_Type(Integer32):
    """Custom type ringswitchPortTestError based on Integer32"""
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
        *(("bad-rnum", 5),
          ("duplicate-ring", 3),
          ("fail-b", 6),
          ("fail-nb", 4),
          ("no-error", 1),
          ("same-ring", 2))
    )


_RingswitchPortTestError_Type.__name__ = "Integer32"
_RingswitchPortTestError_Object = MibTableColumn
ringswitchPortTestError = _RingswitchPortTestError_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 8),
    _RingswitchPortTestError_Type()
)
ringswitchPortTestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortTestError.setStatus("mandatory")


class _RingswitchPortTestPhase_Type(Integer32):
    """Custom type ringswitchPortTestPhase based on Integer32"""
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
        *(("broadcast", 4),
          ("not-running", 1),
          ("routed", 3),
          ("same-ring", 2),
          ("success", 5))
    )


_RingswitchPortTestPhase_Type.__name__ = "Integer32"
_RingswitchPortTestPhase_Object = MibTableColumn
ringswitchPortTestPhase = _RingswitchPortTestPhase_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 9),
    _RingswitchPortTestPhase_Type()
)
ringswitchPortTestPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortTestPhase.setStatus("mandatory")
_RingswitchPortSummary_Type = Integer32
_RingswitchPortSummary_Object = MibTableColumn
ringswitchPortSummary = _RingswitchPortSummary_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 10),
    _RingswitchPortSummary_Type()
)
ringswitchPortSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortSummary.setStatus("mandatory")
_RingswitchPortAddress_Type = TRNMacAddress
_RingswitchPortAddress_Object = MibTableColumn
ringswitchPortAddress = _RingswitchPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 11),
    _RingswitchPortAddress_Type()
)
ringswitchPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortAddress.setStatus("mandatory")
_RingswitchPortLAA_Type = TRNMacAddress
_RingswitchPortLAA_Object = MibTableColumn
ringswitchPortLAA = _RingswitchPortLAA_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 12),
    _RingswitchPortLAA_Type()
)
ringswitchPortLAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortLAA.setStatus("mandatory")


class _RingswitchPortStationType_Type(Integer32):
    """Custom type ringswitchPortStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anything", 1),
          ("workstations", 2))
    )


_RingswitchPortStationType_Type.__name__ = "Integer32"
_RingswitchPortStationType_Object = MibTableColumn
ringswitchPortStationType = _RingswitchPortStationType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 13),
    _RingswitchPortStationType_Type()
)
ringswitchPortStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortStationType.setStatus("mandatory")


class _RingswitchPortRPSEnable_Type(Integer32):
    """Custom type ringswitchPortRPSEnable based on Integer32"""
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


_RingswitchPortRPSEnable_Type.__name__ = "Integer32"
_RingswitchPortRPSEnable_Object = MibTableColumn
ringswitchPortRPSEnable = _RingswitchPortRPSEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 14),
    _RingswitchPortRPSEnable_Type()
)
ringswitchPortRPSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortRPSEnable.setStatus("mandatory")


class _RingswitchPortCutThruEnable_Type(Integer32):
    """Custom type ringswitchPortCutThruEnable based on Integer32"""
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


_RingswitchPortCutThruEnable_Type.__name__ = "Integer32"
_RingswitchPortCutThruEnable_Object = MibTableColumn
ringswitchPortCutThruEnable = _RingswitchPortCutThruEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 15),
    _RingswitchPortCutThruEnable_Type()
)
ringswitchPortCutThruEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortCutThruEnable.setStatus("mandatory")
_RingswitchPortInOctets_Type = INTEGER48
_RingswitchPortInOctets_Object = MibTableColumn
ringswitchPortInOctets = _RingswitchPortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 16),
    _RingswitchPortInOctets_Type()
)
ringswitchPortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortInOctets.setStatus("mandatory")
_RingswitchPortOutOctets_Type = INTEGER48
_RingswitchPortOutOctets_Object = MibTableColumn
ringswitchPortOutOctets = _RingswitchPortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 17),
    _RingswitchPortOutOctets_Type()
)
ringswitchPortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortOutOctets.setStatus("mandatory")
_RingswitchPortSpecInFrames_Type = INTEGER48
_RingswitchPortSpecInFrames_Object = MibTableColumn
ringswitchPortSpecInFrames = _RingswitchPortSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 18),
    _RingswitchPortSpecInFrames_Type()
)
ringswitchPortSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortSpecInFrames.setStatus("mandatory")
_RingswitchPortSpecOutFrames_Type = INTEGER48
_RingswitchPortSpecOutFrames_Object = MibTableColumn
ringswitchPortSpecOutFrames = _RingswitchPortSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 19),
    _RingswitchPortSpecOutFrames_Type()
)
ringswitchPortSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortSpecOutFrames.setStatus("mandatory")
_RingswitchPortApeInFrames_Type = INTEGER48
_RingswitchPortApeInFrames_Object = MibTableColumn
ringswitchPortApeInFrames = _RingswitchPortApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 20),
    _RingswitchPortApeInFrames_Type()
)
ringswitchPortApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortApeInFrames.setStatus("mandatory")
_RingswitchPortApeOutFrames_Type = INTEGER48
_RingswitchPortApeOutFrames_Object = MibTableColumn
ringswitchPortApeOutFrames = _RingswitchPortApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 21),
    _RingswitchPortApeOutFrames_Type()
)
ringswitchPortApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortApeOutFrames.setStatus("mandatory")
_RingswitchPortSteInFrames_Type = INTEGER48
_RingswitchPortSteInFrames_Object = MibTableColumn
ringswitchPortSteInFrames = _RingswitchPortSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 22),
    _RingswitchPortSteInFrames_Type()
)
ringswitchPortSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortSteInFrames.setStatus("mandatory")
_RingswitchPortSteOutFrames_Type = INTEGER48
_RingswitchPortSteOutFrames_Object = MibTableColumn
ringswitchPortSteOutFrames = _RingswitchPortSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 23),
    _RingswitchPortSteOutFrames_Type()
)
ringswitchPortSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortSteOutFrames.setStatus("mandatory")


class _RingswitchPortResetCounters_Type(Integer32):
    """Custom type ringswitchPortResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_RingswitchPortResetCounters_Type.__name__ = "Integer32"
_RingswitchPortResetCounters_Object = MibTableColumn
ringswitchPortResetCounters = _RingswitchPortResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 24),
    _RingswitchPortResetCounters_Type()
)
ringswitchPortResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortResetCounters.setStatus("mandatory")


class _RingswitchPortFixupMode_Type(Integer32):
    """Custom type ringswitchPortFixupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("fddi-all", 2))
    )


_RingswitchPortFixupMode_Type.__name__ = "Integer32"
_RingswitchPortFixupMode_Object = MibTableColumn
ringswitchPortFixupMode = _RingswitchPortFixupMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 25),
    _RingswitchPortFixupMode_Type()
)
ringswitchPortFixupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortFixupMode.setStatus("mandatory")


class _RingswitchPortForwardMode_Type(Integer32):
    """Custom type ringswitchPortForwardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sr-only", 1),
          ("sr-tb", 3),
          ("tb-only", 2))
    )


_RingswitchPortForwardMode_Type.__name__ = "Integer32"
_RingswitchPortForwardMode_Object = MibTableColumn
ringswitchPortForwardMode = _RingswitchPortForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 26),
    _RingswitchPortForwardMode_Type()
)
ringswitchPortForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortForwardMode.setStatus("mandatory")


class _RingswitchPortRMONCapabilities_Type(Integer32):
    """Custom type ringswitchPortRMONCapabilities based on Integer32"""
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
        *(("disabled", 1),
          ("economy", 2),
          ("snooping", 4),
          ("standard", 3))
    )


_RingswitchPortRMONCapabilities_Type.__name__ = "Integer32"
_RingswitchPortRMONCapabilities_Object = MibTableColumn
ringswitchPortRMONCapabilities = _RingswitchPortRMONCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 27),
    _RingswitchPortRMONCapabilities_Type()
)
ringswitchPortRMONCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortRMONCapabilities.setStatus("mandatory")


class _RingswitchPortRMONMode_Type(Integer32):
    """Custom type ringswitchPortRMONMode based on Integer32"""
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
        *(("disabled", 1),
          ("economy", 2),
          ("snooping", 4),
          ("standard", 3))
    )


_RingswitchPortRMONMode_Type.__name__ = "Integer32"
_RingswitchPortRMONMode_Object = MibTableColumn
ringswitchPortRMONMode = _RingswitchPortRMONMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 28),
    _RingswitchPortRMONMode_Type()
)
ringswitchPortRMONMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortRMONMode.setStatus("mandatory")
_RingswitchPortRMONSnoop_Type = TRNMacAddress
_RingswitchPortRMONSnoop_Object = MibTableColumn
ringswitchPortRMONSnoop = _RingswitchPortRMONSnoop_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 29),
    _RingswitchPortRMONSnoop_Type()
)
ringswitchPortRMONSnoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchPortRMONSnoop.setStatus("mandatory")
_RingswitchPortTransparentInFrames_Type = INTEGER48
_RingswitchPortTransparentInFrames_Object = MibTableColumn
ringswitchPortTransparentInFrames = _RingswitchPortTransparentInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 30),
    _RingswitchPortTransparentInFrames_Type()
)
ringswitchPortTransparentInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortTransparentInFrames.setStatus("mandatory")
_RingswitchPortTransparentOutFrames_Type = INTEGER48
_RingswitchPortTransparentOutFrames_Object = MibTableColumn
ringswitchPortTransparentOutFrames = _RingswitchPortTransparentOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 31),
    _RingswitchPortTransparentOutFrames_Type()
)
ringswitchPortTransparentOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortTransparentOutFrames.setStatus("mandatory")
_RingswitchPortTransparentDiscFrames_Type = INTEGER48
_RingswitchPortTransparentDiscFrames_Object = MibTableColumn
ringswitchPortTransparentDiscFrames = _RingswitchPortTransparentDiscFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 32),
    _RingswitchPortTransparentDiscFrames_Type()
)
ringswitchPortTransparentDiscFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortTransparentDiscFrames.setStatus("mandatory")
_RingswitchPortLEDs_Type = OctetString
_RingswitchPortLEDs_Object = MibTableColumn
ringswitchPortLEDs = _RingswitchPortLEDs_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 2, 1, 1, 33),
    _RingswitchPortLEDs_Type()
)
ringswitchPortLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPortLEDs.setStatus("mandatory")
_RingswitchFwd_ObjectIdentity = ObjectIdentity
ringswitchFwd = _RingswitchFwd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 3)
)


class _RingswitchFwdAdminState_Type(Integer32):
    """Custom type ringswitchFwdAdminState based on Integer32"""
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
        *(("disable", 2),
          ("sr-only", 1),
          ("srt", 4),
          ("srt-plus", 5),
          ("tb-only", 3))
    )


_RingswitchFwdAdminState_Type.__name__ = "Integer32"
_RingswitchFwdAdminState_Object = MibScalar
ringswitchFwdAdminState = _RingswitchFwdAdminState_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 1),
    _RingswitchFwdAdminState_Type()
)
ringswitchFwdAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFwdAdminState.setStatus("mandatory")


class _RingswitchFwdOperState_Type(Integer32):
    """Custom type ringswitchFwdOperState based on Integer32"""
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
        *(("inactive", 2),
          ("sr-only", 1),
          ("srt", 4),
          ("srt-plus", 5),
          ("tb-only", 3))
    )


_RingswitchFwdOperState_Type.__name__ = "Integer32"
_RingswitchFwdOperState_Object = MibScalar
ringswitchFwdOperState = _RingswitchFwdOperState_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 2),
    _RingswitchFwdOperState_Type()
)
ringswitchFwdOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdOperState.setStatus("mandatory")
_RingswitchFwdPortTable_Object = MibTable
ringswitchFwdPortTable = _RingswitchFwdPortTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3)
)
if mibBuilder.loadTexts:
    ringswitchFwdPortTable.setStatus("mandatory")
_RingswitchFwdPortEntry_Object = MibTableRow
ringswitchFwdPortEntry = _RingswitchFwdPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1)
)
ringswitchFwdPortEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchFwdPort"),
)
if mibBuilder.loadTexts:
    ringswitchFwdPortEntry.setStatus("mandatory")


class _RingswitchFwdPort_Type(Integer32):
    """Custom type ringswitchFwdPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchFwdPort_Type.__name__ = "Integer32"
_RingswitchFwdPort_Object = MibTableColumn
ringswitchFwdPort = _RingswitchFwdPort_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 1),
    _RingswitchFwdPort_Type()
)
ringswitchFwdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPort.setStatus("mandatory")


class _RingswitchFwdPortMode_Type(Integer32):
    """Custom type ringswitchFwdPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sr-only", 1),
          ("sr-tb", 3),
          ("tb-only", 2))
    )


_RingswitchFwdPortMode_Type.__name__ = "Integer32"
_RingswitchFwdPortMode_Object = MibTableColumn
ringswitchFwdPortMode = _RingswitchFwdPortMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 2),
    _RingswitchFwdPortMode_Type()
)
ringswitchFwdPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFwdPortMode.setStatus("mandatory")


class _RingswitchFwdPortStationType_Type(Integer32):
    """Custom type ringswitchFwdPortStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anything", 1),
          ("workstations", 2))
    )


_RingswitchFwdPortStationType_Type.__name__ = "Integer32"
_RingswitchFwdPortStationType_Object = MibTableColumn
ringswitchFwdPortStationType = _RingswitchFwdPortStationType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 3),
    _RingswitchFwdPortStationType_Type()
)
ringswitchFwdPortStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFwdPortStationType.setStatus("mandatory")


class _RingswitchFwdPortCutThruEnable_Type(Integer32):
    """Custom type ringswitchFwdPortCutThruEnable based on Integer32"""
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


_RingswitchFwdPortCutThruEnable_Type.__name__ = "Integer32"
_RingswitchFwdPortCutThruEnable_Object = MibTableColumn
ringswitchFwdPortCutThruEnable = _RingswitchFwdPortCutThruEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 4),
    _RingswitchFwdPortCutThruEnable_Type()
)
ringswitchFwdPortCutThruEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFwdPortCutThruEnable.setStatus("mandatory")
_RingswitchFwdPortSpecInFrames_Type = INTEGER48
_RingswitchFwdPortSpecInFrames_Object = MibTableColumn
ringswitchFwdPortSpecInFrames = _RingswitchFwdPortSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 5),
    _RingswitchFwdPortSpecInFrames_Type()
)
ringswitchFwdPortSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortSpecInFrames.setStatus("mandatory")
_RingswitchFwdPortSpecOutFrames_Type = INTEGER48
_RingswitchFwdPortSpecOutFrames_Object = MibTableColumn
ringswitchFwdPortSpecOutFrames = _RingswitchFwdPortSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 6),
    _RingswitchFwdPortSpecOutFrames_Type()
)
ringswitchFwdPortSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortSpecOutFrames.setStatus("mandatory")
_RingswitchFwdPortApeInFrames_Type = INTEGER48
_RingswitchFwdPortApeInFrames_Object = MibTableColumn
ringswitchFwdPortApeInFrames = _RingswitchFwdPortApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 7),
    _RingswitchFwdPortApeInFrames_Type()
)
ringswitchFwdPortApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortApeInFrames.setStatus("mandatory")
_RingswitchFwdPortApeOutFrames_Type = INTEGER48
_RingswitchFwdPortApeOutFrames_Object = MibTableColumn
ringswitchFwdPortApeOutFrames = _RingswitchFwdPortApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 8),
    _RingswitchFwdPortApeOutFrames_Type()
)
ringswitchFwdPortApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortApeOutFrames.setStatus("mandatory")
_RingswitchFwdPortSteInFrames_Type = INTEGER48
_RingswitchFwdPortSteInFrames_Object = MibTableColumn
ringswitchFwdPortSteInFrames = _RingswitchFwdPortSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 9),
    _RingswitchFwdPortSteInFrames_Type()
)
ringswitchFwdPortSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortSteInFrames.setStatus("mandatory")
_RingswitchFwdPortSteOutFrames_Type = INTEGER48
_RingswitchFwdPortSteOutFrames_Object = MibTableColumn
ringswitchFwdPortSteOutFrames = _RingswitchFwdPortSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 10),
    _RingswitchFwdPortSteOutFrames_Type()
)
ringswitchFwdPortSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortSteOutFrames.setStatus("mandatory")
_RingswitchFwdPortTransparentInFrames_Type = INTEGER48
_RingswitchFwdPortTransparentInFrames_Object = MibTableColumn
ringswitchFwdPortTransparentInFrames = _RingswitchFwdPortTransparentInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 11),
    _RingswitchFwdPortTransparentInFrames_Type()
)
ringswitchFwdPortTransparentInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTransparentInFrames.setStatus("mandatory")
_RingswitchFwdPortTransparentOutFrames_Type = INTEGER48
_RingswitchFwdPortTransparentOutFrames_Object = MibTableColumn
ringswitchFwdPortTransparentOutFrames = _RingswitchFwdPortTransparentOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 12),
    _RingswitchFwdPortTransparentOutFrames_Type()
)
ringswitchFwdPortTransparentOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTransparentOutFrames.setStatus("mandatory")
_RingswitchFwdPortTransparentDiscFrames_Type = INTEGER48
_RingswitchFwdPortTransparentDiscFrames_Object = MibTableColumn
ringswitchFwdPortTransparentDiscFrames = _RingswitchFwdPortTransparentDiscFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 13),
    _RingswitchFwdPortTransparentDiscFrames_Type()
)
ringswitchFwdPortTransparentDiscFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTransparentDiscFrames.setStatus("mandatory")


class _RingswitchFwdPortTestState_Type(Integer32):
    """Custom type ringswitchFwdPortTestState based on Integer32"""
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
        *(("disabled", 1),
          ("failed", 3),
          ("ok", 4),
          ("ok-use-spt", 6),
          ("running", 2),
          ("unknown", 5))
    )


_RingswitchFwdPortTestState_Type.__name__ = "Integer32"
_RingswitchFwdPortTestState_Object = MibTableColumn
ringswitchFwdPortTestState = _RingswitchFwdPortTestState_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 14),
    _RingswitchFwdPortTestState_Type()
)
ringswitchFwdPortTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTestState.setStatus("mandatory")


class _RingswitchFwdPortTestError_Type(Integer32):
    """Custom type ringswitchFwdPortTestError based on Integer32"""
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
        *(("bad-rnum", 5),
          ("duplicate-ring", 3),
          ("fail-b", 6),
          ("fail-nb", 4),
          ("no-error", 1),
          ("same-ring", 2))
    )


_RingswitchFwdPortTestError_Type.__name__ = "Integer32"
_RingswitchFwdPortTestError_Object = MibTableColumn
ringswitchFwdPortTestError = _RingswitchFwdPortTestError_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 15),
    _RingswitchFwdPortTestError_Type()
)
ringswitchFwdPortTestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTestError.setStatus("mandatory")


class _RingswitchFwdPortTestPhase_Type(Integer32):
    """Custom type ringswitchFwdPortTestPhase based on Integer32"""
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
        *(("broadcast", 4),
          ("not-running", 1),
          ("routed", 3),
          ("same-ring", 2),
          ("success", 5))
    )


_RingswitchFwdPortTestPhase_Type.__name__ = "Integer32"
_RingswitchFwdPortTestPhase_Object = MibTableColumn
ringswitchFwdPortTestPhase = _RingswitchFwdPortTestPhase_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 16),
    _RingswitchFwdPortTestPhase_Type()
)
ringswitchFwdPortTestPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTestPhase.setStatus("mandatory")


class _RingswitchFwdPortTbForce_Type(Integer32):
    """Custom type ringswitchFwdPortTbForce based on Integer32"""
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


_RingswitchFwdPortTbForce_Type.__name__ = "Integer32"
_RingswitchFwdPortTbForce_Object = MibTableColumn
ringswitchFwdPortTbForce = _RingswitchFwdPortTbForce_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 17),
    _RingswitchFwdPortTbForce_Type()
)
ringswitchFwdPortTbForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFwdPortTbForce.setStatus("mandatory")
_RingswitchFwdPortStpMaster_Type = Integer32
_RingswitchFwdPortStpMaster_Object = MibTableColumn
ringswitchFwdPortStpMaster = _RingswitchFwdPortStpMaster_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 18),
    _RingswitchFwdPortStpMaster_Type()
)
ringswitchFwdPortStpMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFwdPortStpMaster.setStatus("mandatory")


class _RingswitchFwdPortTbState_Type(Integer32):
    """Custom type ringswitchFwdPortTbState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_RingswitchFwdPortTbState_Type.__name__ = "Integer32"
_RingswitchFwdPortTbState_Object = MibTableColumn
ringswitchFwdPortTbState = _RingswitchFwdPortTbState_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 19),
    _RingswitchFwdPortTbState_Type()
)
ringswitchFwdPortTbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTbState.setStatus("mandatory")


class _RingswitchFwdPortSteState_Type(Integer32):
    """Custom type ringswitchFwdPortSteState based on Integer32"""
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


_RingswitchFwdPortSteState_Type.__name__ = "Integer32"
_RingswitchFwdPortSteState_Object = MibTableColumn
ringswitchFwdPortSteState = _RingswitchFwdPortSteState_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 20),
    _RingswitchFwdPortSteState_Type()
)
ringswitchFwdPortSteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortSteState.setStatus("mandatory")
_RingswitchFwdPortTbUnicastInFrames_Type = INTEGER48
_RingswitchFwdPortTbUnicastInFrames_Object = MibTableColumn
ringswitchFwdPortTbUnicastInFrames = _RingswitchFwdPortTbUnicastInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 21),
    _RingswitchFwdPortTbUnicastInFrames_Type()
)
ringswitchFwdPortTbUnicastInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTbUnicastInFrames.setStatus("mandatory")
_RingswitchFwdPortTbUnicastOutFrames_Type = INTEGER48
_RingswitchFwdPortTbUnicastOutFrames_Object = MibTableColumn
ringswitchFwdPortTbUnicastOutFrames = _RingswitchFwdPortTbUnicastOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 22),
    _RingswitchFwdPortTbUnicastOutFrames_Type()
)
ringswitchFwdPortTbUnicastOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTbUnicastOutFrames.setStatus("mandatory")
_RingswitchFwdPortTbBroadcastInFrames_Type = INTEGER48
_RingswitchFwdPortTbBroadcastInFrames_Object = MibTableColumn
ringswitchFwdPortTbBroadcastInFrames = _RingswitchFwdPortTbBroadcastInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 23),
    _RingswitchFwdPortTbBroadcastInFrames_Type()
)
ringswitchFwdPortTbBroadcastInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTbBroadcastInFrames.setStatus("mandatory")
_RingswitchFwdPortTbBroadcastOutFrames_Type = INTEGER48
_RingswitchFwdPortTbBroadcastOutFrames_Object = MibTableColumn
ringswitchFwdPortTbBroadcastOutFrames = _RingswitchFwdPortTbBroadcastOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 24),
    _RingswitchFwdPortTbBroadcastOutFrames_Type()
)
ringswitchFwdPortTbBroadcastOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTbBroadcastOutFrames.setStatus("mandatory")
_RingswitchFwdPortTbMulticastInFrames_Type = INTEGER48
_RingswitchFwdPortTbMulticastInFrames_Object = MibTableColumn
ringswitchFwdPortTbMulticastInFrames = _RingswitchFwdPortTbMulticastInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 25),
    _RingswitchFwdPortTbMulticastInFrames_Type()
)
ringswitchFwdPortTbMulticastInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTbMulticastInFrames.setStatus("mandatory")
_RingswitchFwdPortTbMulticastOutFrames_Type = INTEGER48
_RingswitchFwdPortTbMulticastOutFrames_Object = MibTableColumn
ringswitchFwdPortTbMulticastOutFrames = _RingswitchFwdPortTbMulticastOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 26),
    _RingswitchFwdPortTbMulticastOutFrames_Type()
)
ringswitchFwdPortTbMulticastOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTbMulticastOutFrames.setStatus("mandatory")
_RingswitchFwdPortTbMiscInFrames_Type = INTEGER48
_RingswitchFwdPortTbMiscInFrames_Object = MibTableColumn
ringswitchFwdPortTbMiscInFrames = _RingswitchFwdPortTbMiscInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 27),
    _RingswitchFwdPortTbMiscInFrames_Type()
)
ringswitchFwdPortTbMiscInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTbMiscInFrames.setStatus("mandatory")
_RingswitchFwdPortTbMiscOutFrames_Type = INTEGER48
_RingswitchFwdPortTbMiscOutFrames_Object = MibTableColumn
ringswitchFwdPortTbMiscOutFrames = _RingswitchFwdPortTbMiscOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 28),
    _RingswitchFwdPortTbMiscOutFrames_Type()
)
ringswitchFwdPortTbMiscOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortTbMiscOutFrames.setStatus("mandatory")
_RingswitchFwdPortMatrixSrSpecFrames_Type = OctetString
_RingswitchFwdPortMatrixSrSpecFrames_Object = MibTableColumn
ringswitchFwdPortMatrixSrSpecFrames = _RingswitchFwdPortMatrixSrSpecFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 29),
    _RingswitchFwdPortMatrixSrSpecFrames_Type()
)
ringswitchFwdPortMatrixSrSpecFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortMatrixSrSpecFrames.setStatus("mandatory")
_RingswitchFwdPortMatrixTbUniFrames_Type = OctetString
_RingswitchFwdPortMatrixTbUniFrames_Object = MibTableColumn
ringswitchFwdPortMatrixTbUniFrames = _RingswitchFwdPortMatrixTbUniFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 30),
    _RingswitchFwdPortMatrixTbUniFrames_Type()
)
ringswitchFwdPortMatrixTbUniFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdPortMatrixTbUniFrames.setStatus("mandatory")


class _RingswitchFwdPortEthernetSRBlk_Type(Integer32):
    """Custom type ringswitchFwdPortEthernetSRBlk based on Integer32"""
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


_RingswitchFwdPortEthernetSRBlk_Type.__name__ = "Integer32"
_RingswitchFwdPortEthernetSRBlk_Object = MibTableColumn
ringswitchFwdPortEthernetSRBlk = _RingswitchFwdPortEthernetSRBlk_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 31),
    _RingswitchFwdPortEthernetSRBlk_Type()
)
ringswitchFwdPortEthernetSRBlk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFwdPortEthernetSRBlk.setStatus("mandatory")


class _RingswitchFwdPortAutoPathCost_Type(Integer32):
    """Custom type ringswitchFwdPortAutoPathCost based on Integer32"""
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


_RingswitchFwdPortAutoPathCost_Type.__name__ = "Integer32"
_RingswitchFwdPortAutoPathCost_Object = MibTableColumn
ringswitchFwdPortAutoPathCost = _RingswitchFwdPortAutoPathCost_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 32),
    _RingswitchFwdPortAutoPathCost_Type()
)
ringswitchFwdPortAutoPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFwdPortAutoPathCost.setStatus("mandatory")


class _RingswitchFwdPortBroadcastReflect_Type(Integer32):
    """Custom type ringswitchFwdPortBroadcastReflect based on Integer32"""
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


_RingswitchFwdPortBroadcastReflect_Type.__name__ = "Integer32"
_RingswitchFwdPortBroadcastReflect_Object = MibTableColumn
ringswitchFwdPortBroadcastReflect = _RingswitchFwdPortBroadcastReflect_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 3, 1, 33),
    _RingswitchFwdPortBroadcastReflect_Type()
)
ringswitchFwdPortBroadcastReflect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFwdPortBroadcastReflect.setStatus("mandatory")
_RingswitchFwdTotalRxFrames_Type = INTEGER48
_RingswitchFwdTotalRxFrames_Object = MibScalar
ringswitchFwdTotalRxFrames = _RingswitchFwdTotalRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 4),
    _RingswitchFwdTotalRxFrames_Type()
)
ringswitchFwdTotalRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalRxFrames.setStatus("mandatory")
_RingswitchFwdTotalTxFrames_Type = INTEGER48
_RingswitchFwdTotalTxFrames_Object = MibScalar
ringswitchFwdTotalTxFrames = _RingswitchFwdTotalTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 5),
    _RingswitchFwdTotalTxFrames_Type()
)
ringswitchFwdTotalTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalTxFrames.setStatus("mandatory")


class _RingswitchFwdBridgeNum_Type(Integer32):
    """Custom type ringswitchFwdBridgeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RingswitchFwdBridgeNum_Type.__name__ = "Integer32"
_RingswitchFwdBridgeNum_Object = MibScalar
ringswitchFwdBridgeNum = _RingswitchFwdBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 6),
    _RingswitchFwdBridgeNum_Type()
)
ringswitchFwdBridgeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdBridgeNum.setStatus("mandatory")
_RingswitchFwdTbForced_Type = OctetString
_RingswitchFwdTbForced_Object = MibScalar
ringswitchFwdTbForced = _RingswitchFwdTbForced_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 7),
    _RingswitchFwdTbForced_Type()
)
ringswitchFwdTbForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTbForced.setStatus("mandatory")
_RingswitchFwdStpMasters_Type = OctetString
_RingswitchFwdStpMasters_Object = MibScalar
ringswitchFwdStpMasters = _RingswitchFwdStpMasters_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 8),
    _RingswitchFwdStpMasters_Type()
)
ringswitchFwdStpMasters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdStpMasters.setStatus("mandatory")


class _RingswitchFwdGlobalHopLimit_Type(Integer32):
    """Custom type ringswitchFwdGlobalHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_RingswitchFwdGlobalHopLimit_Type.__name__ = "Integer32"
_RingswitchFwdGlobalHopLimit_Object = MibScalar
ringswitchFwdGlobalHopLimit = _RingswitchFwdGlobalHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 9),
    _RingswitchFwdGlobalHopLimit_Type()
)
ringswitchFwdGlobalHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdGlobalHopLimit.setStatus("mandatory")
_RingswitchFwdTotalBadFrames_Type = INTEGER48
_RingswitchFwdTotalBadFrames_Object = MibScalar
ringswitchFwdTotalBadFrames = _RingswitchFwdTotalBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 10),
    _RingswitchFwdTotalBadFrames_Type()
)
ringswitchFwdTotalBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalBadFrames.setStatus("mandatory")
_RingswitchFwdTotalSpecInFrames_Type = INTEGER48
_RingswitchFwdTotalSpecInFrames_Object = MibScalar
ringswitchFwdTotalSpecInFrames = _RingswitchFwdTotalSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 11),
    _RingswitchFwdTotalSpecInFrames_Type()
)
ringswitchFwdTotalSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalSpecInFrames.setStatus("mandatory")
_RingswitchFwdTotalSpecOutFrames_Type = INTEGER48
_RingswitchFwdTotalSpecOutFrames_Object = MibScalar
ringswitchFwdTotalSpecOutFrames = _RingswitchFwdTotalSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 12),
    _RingswitchFwdTotalSpecOutFrames_Type()
)
ringswitchFwdTotalSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalSpecOutFrames.setStatus("mandatory")
_RingswitchFwdTotalApeInFrames_Type = INTEGER48
_RingswitchFwdTotalApeInFrames_Object = MibScalar
ringswitchFwdTotalApeInFrames = _RingswitchFwdTotalApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 13),
    _RingswitchFwdTotalApeInFrames_Type()
)
ringswitchFwdTotalApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalApeInFrames.setStatus("mandatory")
_RingswitchFwdTotalApeOutFrames_Type = INTEGER48
_RingswitchFwdTotalApeOutFrames_Object = MibScalar
ringswitchFwdTotalApeOutFrames = _RingswitchFwdTotalApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 14),
    _RingswitchFwdTotalApeOutFrames_Type()
)
ringswitchFwdTotalApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalApeOutFrames.setStatus("mandatory")
_RingswitchFwdTotalSteInFrames_Type = INTEGER48
_RingswitchFwdTotalSteInFrames_Object = MibScalar
ringswitchFwdTotalSteInFrames = _RingswitchFwdTotalSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 15),
    _RingswitchFwdTotalSteInFrames_Type()
)
ringswitchFwdTotalSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalSteInFrames.setStatus("mandatory")
_RingswitchFwdTotalSteOutFrames_Type = INTEGER48
_RingswitchFwdTotalSteOutFrames_Object = MibScalar
ringswitchFwdTotalSteOutFrames = _RingswitchFwdTotalSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 16),
    _RingswitchFwdTotalSteOutFrames_Type()
)
ringswitchFwdTotalSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalSteOutFrames.setStatus("mandatory")
_RingswitchFwdTotalTransparentInFrames_Type = INTEGER48
_RingswitchFwdTotalTransparentInFrames_Object = MibScalar
ringswitchFwdTotalTransparentInFrames = _RingswitchFwdTotalTransparentInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 17),
    _RingswitchFwdTotalTransparentInFrames_Type()
)
ringswitchFwdTotalTransparentInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalTransparentInFrames.setStatus("mandatory")
_RingswitchFwdTotalTransparentOutFrames_Type = INTEGER48
_RingswitchFwdTotalTransparentOutFrames_Object = MibScalar
ringswitchFwdTotalTransparentOutFrames = _RingswitchFwdTotalTransparentOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 18),
    _RingswitchFwdTotalTransparentOutFrames_Type()
)
ringswitchFwdTotalTransparentOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalTransparentOutFrames.setStatus("mandatory")
_RingswitchFwdTotalTpUnicastInFrames_Type = INTEGER48
_RingswitchFwdTotalTpUnicastInFrames_Object = MibScalar
ringswitchFwdTotalTpUnicastInFrames = _RingswitchFwdTotalTpUnicastInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 19),
    _RingswitchFwdTotalTpUnicastInFrames_Type()
)
ringswitchFwdTotalTpUnicastInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalTpUnicastInFrames.setStatus("mandatory")
_RingswitchFwdTotalTpUnicastOutFrames_Type = INTEGER48
_RingswitchFwdTotalTpUnicastOutFrames_Object = MibScalar
ringswitchFwdTotalTpUnicastOutFrames = _RingswitchFwdTotalTpUnicastOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 20),
    _RingswitchFwdTotalTpUnicastOutFrames_Type()
)
ringswitchFwdTotalTpUnicastOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalTpUnicastOutFrames.setStatus("mandatory")
_RingswitchFwdTotalTpBroadcastInFrames_Type = INTEGER48
_RingswitchFwdTotalTpBroadcastInFrames_Object = MibScalar
ringswitchFwdTotalTpBroadcastInFrames = _RingswitchFwdTotalTpBroadcastInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 21),
    _RingswitchFwdTotalTpBroadcastInFrames_Type()
)
ringswitchFwdTotalTpBroadcastInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalTpBroadcastInFrames.setStatus("mandatory")
_RingswitchFwdTotalTpBroadcastOutFrames_Type = INTEGER48
_RingswitchFwdTotalTpBroadcastOutFrames_Object = MibScalar
ringswitchFwdTotalTpBroadcastOutFrames = _RingswitchFwdTotalTpBroadcastOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 22),
    _RingswitchFwdTotalTpBroadcastOutFrames_Type()
)
ringswitchFwdTotalTpBroadcastOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalTpBroadcastOutFrames.setStatus("mandatory")
_RingswitchFwdTotalTpMulticastInFrames_Type = INTEGER48
_RingswitchFwdTotalTpMulticastInFrames_Object = MibScalar
ringswitchFwdTotalTpMulticastInFrames = _RingswitchFwdTotalTpMulticastInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 23),
    _RingswitchFwdTotalTpMulticastInFrames_Type()
)
ringswitchFwdTotalTpMulticastInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalTpMulticastInFrames.setStatus("mandatory")
_RingswitchFwdTotalTpMulticastOutFrames_Type = INTEGER48
_RingswitchFwdTotalTpMulticastOutFrames_Object = MibScalar
ringswitchFwdTotalTpMulticastOutFrames = _RingswitchFwdTotalTpMulticastOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 24),
    _RingswitchFwdTotalTpMulticastOutFrames_Type()
)
ringswitchFwdTotalTpMulticastOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalTpMulticastOutFrames.setStatus("mandatory")
_RingswitchFwdTotalTpMiscInFrames_Type = INTEGER48
_RingswitchFwdTotalTpMiscInFrames_Object = MibScalar
ringswitchFwdTotalTpMiscInFrames = _RingswitchFwdTotalTpMiscInFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 25),
    _RingswitchFwdTotalTpMiscInFrames_Type()
)
ringswitchFwdTotalTpMiscInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalTpMiscInFrames.setStatus("mandatory")
_RingswitchFwdTotalTpMiscOutFrames_Type = INTEGER48
_RingswitchFwdTotalTpMiscOutFrames_Object = MibScalar
ringswitchFwdTotalTpMiscOutFrames = _RingswitchFwdTotalTpMiscOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 26),
    _RingswitchFwdTotalTpMiscOutFrames_Type()
)
ringswitchFwdTotalTpMiscOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFwdTotalTpMiscOutFrames.setStatus("mandatory")


class _RingswitchFwdMaxFrameSize_Type(Integer32):
    """Custom type ringswitchFwdMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("use18K-frames", 1),
          ("use4500-frames", 2))
    )


_RingswitchFwdMaxFrameSize_Type.__name__ = "Integer32"
_RingswitchFwdMaxFrameSize_Object = MibScalar
ringswitchFwdMaxFrameSize = _RingswitchFwdMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 3, 27),
    _RingswitchFwdMaxFrameSize_Type()
)
ringswitchFwdMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFwdMaxFrameSize.setStatus("mandatory")
_RingswitchLCD_ObjectIdentity = ObjectIdentity
ringswitchLCD = _RingswitchLCD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 4)
)


class _RingswitchLCDTotalDisplays_Type(Integer32):
    """Custom type ringswitchLCDTotalDisplays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchLCDTotalDisplays_Type.__name__ = "Integer32"
_RingswitchLCDTotalDisplays_Object = MibScalar
ringswitchLCDTotalDisplays = _RingswitchLCDTotalDisplays_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 1),
    _RingswitchLCDTotalDisplays_Type()
)
ringswitchLCDTotalDisplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLCDTotalDisplays.setStatus("mandatory")


class _RingswitchLCDCurrentDisplay_Type(Integer32):
    """Custom type ringswitchLCDCurrentDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchLCDCurrentDisplay_Type.__name__ = "Integer32"
_RingswitchLCDCurrentDisplay_Object = MibScalar
ringswitchLCDCurrentDisplay = _RingswitchLCDCurrentDisplay_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 2),
    _RingswitchLCDCurrentDisplay_Type()
)
ringswitchLCDCurrentDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchLCDCurrentDisplay.setStatus("mandatory")
_RingswitchLCDCurrentMsgText_Type = LCDText
_RingswitchLCDCurrentMsgText_Object = MibScalar
ringswitchLCDCurrentMsgText = _RingswitchLCDCurrentMsgText_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 3),
    _RingswitchLCDCurrentMsgText_Type()
)
ringswitchLCDCurrentMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLCDCurrentMsgText.setStatus("mandatory")
_RingswitchLCDTable_Object = MibTable
ringswitchLCDTable = _RingswitchLCDTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 4)
)
if mibBuilder.loadTexts:
    ringswitchLCDTable.setStatus("mandatory")
_RingswitchLCDTableEntry_Object = MibTableRow
ringswitchLCDTableEntry = _RingswitchLCDTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 4, 1)
)
ringswitchLCDTableEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchLCDNum"),
)
if mibBuilder.loadTexts:
    ringswitchLCDTableEntry.setStatus("mandatory")


class _RingswitchLCDNum_Type(Integer32):
    """Custom type ringswitchLCDNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchLCDNum_Type.__name__ = "Integer32"
_RingswitchLCDNum_Object = MibTableColumn
ringswitchLCDNum = _RingswitchLCDNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 4, 1, 1),
    _RingswitchLCDNum_Type()
)
ringswitchLCDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLCDNum.setStatus("mandatory")
_RingswitchLCDMsgText_Type = LCDText
_RingswitchLCDMsgText_Object = MibTableColumn
ringswitchLCDMsgText = _RingswitchLCDMsgText_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 4, 1, 2),
    _RingswitchLCDMsgText_Type()
)
ringswitchLCDMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLCDMsgText.setStatus("mandatory")


class _RingswitchLCDUp_Type(Integer32):
    """Custom type ringswitchLCDUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchLCDUp_Type.__name__ = "Integer32"
_RingswitchLCDUp_Object = MibTableColumn
ringswitchLCDUp = _RingswitchLCDUp_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 4, 1, 3),
    _RingswitchLCDUp_Type()
)
ringswitchLCDUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLCDUp.setStatus("mandatory")


class _RingswitchLCDDown_Type(Integer32):
    """Custom type ringswitchLCDDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchLCDDown_Type.__name__ = "Integer32"
_RingswitchLCDDown_Object = MibTableColumn
ringswitchLCDDown = _RingswitchLCDDown_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 4, 4, 1, 4),
    _RingswitchLCDDown_Type()
)
ringswitchLCDDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLCDDown.setStatus("mandatory")
_RingswitchLAN_ObjectIdentity = ObjectIdentity
ringswitchLAN = _RingswitchLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 5)
)
_RingswitchLANTable_Object = MibTable
ringswitchLANTable = _RingswitchLANTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 1)
)
if mibBuilder.loadTexts:
    ringswitchLANTable.setStatus("mandatory")
_RingswitchLANEntry_Object = MibTableRow
ringswitchLANEntry = _RingswitchLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 1, 1)
)
ringswitchLANEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchLANIndex"),
)
if mibBuilder.loadTexts:
    ringswitchLANEntry.setStatus("mandatory")


class _RingswitchLANIndex_Type(Integer32):
    """Custom type ringswitchLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchLANIndex_Type.__name__ = "Integer32"
_RingswitchLANIndex_Object = MibTableColumn
ringswitchLANIndex = _RingswitchLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 1, 1, 1),
    _RingswitchLANIndex_Type()
)
ringswitchLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLANIndex.setStatus("mandatory")
_RingswitchLANName_Type = DisplayString
_RingswitchLANName_Object = MibTableColumn
ringswitchLANName = _RingswitchLANName_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 1, 1, 2),
    _RingswitchLANName_Type()
)
ringswitchLANName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchLANName.setStatus("mandatory")


class _RingswitchLANPermeable_Type(Integer32):
    """Custom type ringswitchLANPermeable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("impermeable", 1),
          ("permeable", 2))
    )


_RingswitchLANPermeable_Type.__name__ = "Integer32"
_RingswitchLANPermeable_Object = MibTableColumn
ringswitchLANPermeable = _RingswitchLANPermeable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 1, 1, 3),
    _RingswitchLANPermeable_Type()
)
ringswitchLANPermeable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchLANPermeable.setStatus("mandatory")


class _RingswitchLANStatus_Type(Integer32):
    """Custom type ringswitchLANStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_RingswitchLANStatus_Type.__name__ = "Integer32"
_RingswitchLANStatus_Object = MibTableColumn
ringswitchLANStatus = _RingswitchLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 1, 1, 4),
    _RingswitchLANStatus_Type()
)
ringswitchLANStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchLANStatus.setStatus("mandatory")
_RingswitchLANRingTable_Object = MibTable
ringswitchLANRingTable = _RingswitchLANRingTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 2)
)
if mibBuilder.loadTexts:
    ringswitchLANRingTable.setStatus("mandatory")
_RingswitchLANRingEntry_Object = MibTableRow
ringswitchLANRingEntry = _RingswitchLANRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 2, 1)
)
ringswitchLANRingEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchLANRingGroup"),
    (0, "MADGERSW-MIB", "ringswitchLANRingIndex"),
)
if mibBuilder.loadTexts:
    ringswitchLANRingEntry.setStatus("mandatory")
_RingswitchLANRingGroup_Type = Integer32
_RingswitchLANRingGroup_Object = MibTableColumn
ringswitchLANRingGroup = _RingswitchLANRingGroup_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 2, 1, 1),
    _RingswitchLANRingGroup_Type()
)
ringswitchLANRingGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLANRingGroup.setStatus("mandatory")
_RingswitchLANRingIndex_Type = Integer32
_RingswitchLANRingIndex_Object = MibTableColumn
ringswitchLANRingIndex = _RingswitchLANRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 2, 1, 2),
    _RingswitchLANRingIndex_Type()
)
ringswitchLANRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchLANRingIndex.setStatus("mandatory")
_RingswitchLANRingNum_Type = Integer32
_RingswitchLANRingNum_Object = MibTableColumn
ringswitchLANRingNum = _RingswitchLANRingNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 2, 1, 3),
    _RingswitchLANRingNum_Type()
)
ringswitchLANRingNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchLANRingNum.setStatus("mandatory")


class _RingswitchLANRingStatus_Type(Integer32):
    """Custom type ringswitchLANRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_RingswitchLANRingStatus_Type.__name__ = "Integer32"
_RingswitchLANRingStatus_Object = MibTableColumn
ringswitchLANRingStatus = _RingswitchLANRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 5, 2, 1, 4),
    _RingswitchLANRingStatus_Type()
)
ringswitchLANRingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchLANRingStatus.setStatus("mandatory")
_RingswitchVirt_ObjectIdentity = ObjectIdentity
ringswitchVirt = _RingswitchVirt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 6)
)
_RingswitchVirtTB_ObjectIdentity = ObjectIdentity
ringswitchVirtTB = _RingswitchVirtTB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 6, 1)
)
_RingswitchVirtTBTable_Object = MibTable
ringswitchVirtTBTable = _RingswitchVirtTBTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 6, 1, 1)
)
if mibBuilder.loadTexts:
    ringswitchVirtTBTable.setStatus("mandatory")
_RingswitchVirtTBEntry_Object = MibTableRow
ringswitchVirtTBEntry = _RingswitchVirtTBEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 6, 1, 1, 1)
)
ringswitchVirtTBEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchVirtTBIndex"),
)
if mibBuilder.loadTexts:
    ringswitchVirtTBEntry.setStatus("mandatory")


class _RingswitchVirtTBIndex_Type(Integer32):
    """Custom type ringswitchVirtTBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_RingswitchVirtTBIndex_Type.__name__ = "Integer32"
_RingswitchVirtTBIndex_Object = MibTableColumn
ringswitchVirtTBIndex = _RingswitchVirtTBIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 6, 1, 1, 1, 1),
    _RingswitchVirtTBIndex_Type()
)
ringswitchVirtTBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchVirtTBIndex.setStatus("mandatory")
_RingswitchVirtTBStatus_Type = RingswitchRowStatus
_RingswitchVirtTBStatus_Object = MibTableColumn
ringswitchVirtTBStatus = _RingswitchVirtTBStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 6, 1, 1, 1, 2),
    _RingswitchVirtTBStatus_Type()
)
ringswitchVirtTBStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchVirtTBStatus.setStatus("mandatory")
_RingswitchVirtTBName_Type = DisplayString
_RingswitchVirtTBName_Object = MibTableColumn
ringswitchVirtTBName = _RingswitchVirtTBName_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 6, 1, 1, 1, 3),
    _RingswitchVirtTBName_Type()
)
ringswitchVirtTBName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchVirtTBName.setStatus("mandatory")


class _RingswitchVirtTBType_Type(Integer32):
    """Custom type ringswitchVirtTBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("port-only", 1)
    )


_RingswitchVirtTBType_Type.__name__ = "Integer32"
_RingswitchVirtTBType_Object = MibTableColumn
ringswitchVirtTBType = _RingswitchVirtTBType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 6, 1, 1, 1, 4),
    _RingswitchVirtTBType_Type()
)
ringswitchVirtTBType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchVirtTBType.setStatus("mandatory")
_RingswitchVirtTBNumArray_Type = OctetString
_RingswitchVirtTBNumArray_Object = MibTableColumn
ringswitchVirtTBNumArray = _RingswitchVirtTBNumArray_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 6, 1, 1, 1, 5),
    _RingswitchVirtTBNumArray_Type()
)
ringswitchVirtTBNumArray.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchVirtTBNumArray.setStatus("mandatory")
_RingswitchVirtTBNumSize_Type = Integer32
_RingswitchVirtTBNumSize_Object = MibTableColumn
ringswitchVirtTBNumSize = _RingswitchVirtTBNumSize_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 6, 1, 1, 1, 6),
    _RingswitchVirtTBNumSize_Type()
)
ringswitchVirtTBNumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchVirtTBNumSize.setStatus("mandatory")
_RingswitchSlot_ObjectIdentity = ObjectIdentity
ringswitchSlot = _RingswitchSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 7)
)
_RingswitchSlotNumSlots_Type = Integer32
_RingswitchSlotNumSlots_Object = MibScalar
ringswitchSlotNumSlots = _RingswitchSlotNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 1),
    _RingswitchSlotNumSlots_Type()
)
ringswitchSlotNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotNumSlots.setStatus("mandatory")
_RingswitchSlotTable_Object = MibTable
ringswitchSlotTable = _RingswitchSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2)
)
if mibBuilder.loadTexts:
    ringswitchSlotTable.setStatus("mandatory")
_RingswitchSlotEntry_Object = MibTableRow
ringswitchSlotEntry = _RingswitchSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1)
)
ringswitchSlotEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchSlotIndex"),
)
if mibBuilder.loadTexts:
    ringswitchSlotEntry.setStatus("mandatory")


class _RingswitchSlotIndex_Type(Integer32):
    """Custom type ringswitchSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchSlotIndex_Type.__name__ = "Integer32"
_RingswitchSlotIndex_Object = MibTableColumn
ringswitchSlotIndex = _RingswitchSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 1),
    _RingswitchSlotIndex_Type()
)
ringswitchSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotIndex.setStatus("mandatory")


class _RingswitchSlotStatus_Type(Integer32):
    """Custom type ringswitchSlotStatus based on Integer32"""
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
        *(("full-support", 2),
          ("invalid", 1),
          ("no-port-fwd", 4),
          ("no-port-open", 3))
    )


_RingswitchSlotStatus_Type.__name__ = "Integer32"
_RingswitchSlotStatus_Object = MibTableColumn
ringswitchSlotStatus = _RingswitchSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 2),
    _RingswitchSlotStatus_Type()
)
ringswitchSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotStatus.setStatus("mandatory")
_RingswitchSlotBasePort_Type = Integer32
_RingswitchSlotBasePort_Object = MibTableColumn
ringswitchSlotBasePort = _RingswitchSlotBasePort_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 3),
    _RingswitchSlotBasePort_Type()
)
ringswitchSlotBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotBasePort.setStatus("mandatory")


class _RingswitchSlotCardType_Type(Integer32):
    """Custom type ringswitchSlotCardType based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("absent", 4),
          ("atm-fiber", 7),
          ("ethernet", 18),
          ("fddi-fiber", 3),
          ("gigabit-ethernet", 19),
          ("group-switch", 9),
          ("three-layer-switch", 15),
          ("tr-copper-4", 1),
          ("tr-copper-8", 6),
          ("tr-copper-al-4", 10),
          ("tr-copper-hstr-2", 11),
          ("tr-copper-hstr-4", 12),
          ("tr-copper-hstr-8", 16),
          ("tr-fiber-4", 2),
          ("tr-fiber-8", 8),
          ("tr-fiber-hstr-2", 13),
          ("tr-fiber-hstr-4", 14),
          ("tr-fiber-hstr-8", 17),
          ("unknown", 5))
    )


_RingswitchSlotCardType_Type.__name__ = "Integer32"
_RingswitchSlotCardType_Object = MibTableColumn
ringswitchSlotCardType = _RingswitchSlotCardType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 4),
    _RingswitchSlotCardType_Type()
)
ringswitchSlotCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotCardType.setStatus("mandatory")


class _RingswitchSlotCardId_Type(Integer32):
    """Custom type ringswitchSlotCardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingswitchSlotCardId_Type.__name__ = "Integer32"
_RingswitchSlotCardId_Object = MibTableColumn
ringswitchSlotCardId = _RingswitchSlotCardId_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 5),
    _RingswitchSlotCardId_Type()
)
ringswitchSlotCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotCardId.setStatus("mandatory")


class _RingswitchSlotCardRevision_Type(Integer32):
    """Custom type ringswitchSlotCardRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingswitchSlotCardRevision_Type.__name__ = "Integer32"
_RingswitchSlotCardRevision_Object = MibTableColumn
ringswitchSlotCardRevision = _RingswitchSlotCardRevision_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 6),
    _RingswitchSlotCardRevision_Type()
)
ringswitchSlotCardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotCardRevision.setStatus("mandatory")


class _RingswitchSlotCardDescription_Type(DisplayString):
    """Custom type ringswitchSlotCardDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RingswitchSlotCardDescription_Type.__name__ = "DisplayString"
_RingswitchSlotCardDescription_Object = MibTableColumn
ringswitchSlotCardDescription = _RingswitchSlotCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 7),
    _RingswitchSlotCardDescription_Type()
)
ringswitchSlotCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotCardDescription.setStatus("mandatory")
_RingswitchSlotCardNumPorts_Type = Integer32
_RingswitchSlotCardNumPorts_Object = MibTableColumn
ringswitchSlotCardNumPorts = _RingswitchSlotCardNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 8),
    _RingswitchSlotCardNumPorts_Type()
)
ringswitchSlotCardNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotCardNumPorts.setStatus("mandatory")


class _RingswitchSlotCardLAN_Type(Integer32):
    """Custom type ringswitchSlotCardLAN based on Integer32"""
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
        *(("atm", 4),
          ("ethernet", 6),
          ("fddi", 3),
          ("gigabit", 7),
          ("none", 1),
          ("tls", 5),
          ("token-ring", 2))
    )


_RingswitchSlotCardLAN_Type.__name__ = "Integer32"
_RingswitchSlotCardLAN_Object = MibTableColumn
ringswitchSlotCardLAN = _RingswitchSlotCardLAN_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 9),
    _RingswitchSlotCardLAN_Type()
)
ringswitchSlotCardLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotCardLAN.setStatus("mandatory")
_RingswitchSlotCardLEDs_Type = OctetString
_RingswitchSlotCardLEDs_Object = MibTableColumn
ringswitchSlotCardLEDs = _RingswitchSlotCardLEDs_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 10),
    _RingswitchSlotCardLEDs_Type()
)
ringswitchSlotCardLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotCardLEDs.setStatus("mandatory")
_RingswitchSlotIfAdminStatus_Type = OctetString
_RingswitchSlotIfAdminStatus_Object = MibTableColumn
ringswitchSlotIfAdminStatus = _RingswitchSlotIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 11),
    _RingswitchSlotIfAdminStatus_Type()
)
ringswitchSlotIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotIfAdminStatus.setStatus("mandatory")
_RingswitchSlotAdapterStatus_Type = OctetString
_RingswitchSlotAdapterStatus_Object = MibTableColumn
ringswitchSlotAdapterStatus = _RingswitchSlotAdapterStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 12),
    _RingswitchSlotAdapterStatus_Type()
)
ringswitchSlotAdapterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotAdapterStatus.setStatus("mandatory")
_RingswitchSlotTestError_Type = OctetString
_RingswitchSlotTestError_Object = MibTableColumn
ringswitchSlotTestError = _RingswitchSlotTestError_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 13),
    _RingswitchSlotTestError_Type()
)
ringswitchSlotTestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotTestError.setStatus("mandatory")
_RingswitchSlotPortHealth_Type = OctetString
_RingswitchSlotPortHealth_Object = MibTableColumn
ringswitchSlotPortHealth = _RingswitchSlotPortHealth_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 14),
    _RingswitchSlotPortHealth_Type()
)
ringswitchSlotPortHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotPortHealth.setStatus("mandatory")


class _RingswitchSlotLastStatus_Type(Integer32):
    """Custom type ringswitchSlotLastStatus based on Integer32"""
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
        *(("atm-if-down", 1),
          ("atm-porta-down", 2),
          ("atm-portb-down", 3),
          ("fddi-if-down", 4),
          ("fddi-porta-iso", 5),
          ("fddi-portb-iso", 6))
    )


_RingswitchSlotLastStatus_Type.__name__ = "Integer32"
_RingswitchSlotLastStatus_Object = MibTableColumn
ringswitchSlotLastStatus = _RingswitchSlotLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 15),
    _RingswitchSlotLastStatus_Type()
)
ringswitchSlotLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotLastStatus.setStatus("mandatory")
_RingswitchSlotPortCreated_Type = OctetString
_RingswitchSlotPortCreated_Object = MibTableColumn
ringswitchSlotPortCreated = _RingswitchSlotPortCreated_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 16),
    _RingswitchSlotPortCreated_Type()
)
ringswitchSlotPortCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotPortCreated.setStatus("mandatory")


class _RingswitchSlotHealth_Type(Integer32):
    """Custom type ringswitchSlotHealth based on Integer32"""
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
        *(("critical", 4),
          ("degraded", 3),
          ("normal", 1),
          ("warning", 2))
    )


_RingswitchSlotHealth_Type.__name__ = "Integer32"
_RingswitchSlotHealth_Object = MibTableColumn
ringswitchSlotHealth = _RingswitchSlotHealth_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 17),
    _RingswitchSlotHealth_Type()
)
ringswitchSlotHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotHealth.setStatus("mandatory")
_RingswitchSlotVersion_Type = Integer32
_RingswitchSlotVersion_Object = MibTableColumn
ringswitchSlotVersion = _RingswitchSlotVersion_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 7, 2, 1, 18),
    _RingswitchSlotVersion_Type()
)
ringswitchSlotVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchSlotVersion.setStatus("mandatory")
_RingswitchGenPort_ObjectIdentity = ObjectIdentity
ringswitchGenPort = _RingswitchGenPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 8)
)
_RingswitchGenPortTable_Object = MibTable
ringswitchGenPortTable = _RingswitchGenPortTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1)
)
if mibBuilder.loadTexts:
    ringswitchGenPortTable.setStatus("mandatory")
_RingswitchGenPortEntry_Object = MibTableRow
ringswitchGenPortEntry = _RingswitchGenPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1)
)
ringswitchGenPortEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchGenPortNum"),
)
if mibBuilder.loadTexts:
    ringswitchGenPortEntry.setStatus("mandatory")


class _RingswitchGenPortNum_Type(Integer32):
    """Custom type ringswitchGenPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchGenPortNum_Type.__name__ = "Integer32"
_RingswitchGenPortNum_Object = MibTableColumn
ringswitchGenPortNum = _RingswitchGenPortNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 1),
    _RingswitchGenPortNum_Type()
)
ringswitchGenPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchGenPortNum.setStatus("mandatory")


class _RingswitchGenPortAdapterStatus_Type(Integer32):
    """Custom type ringswitchGenPortAdapterStatus based on Integer32"""
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
        *(("closed", 2),
          ("open", 1),
          ("opening", 3),
          ("ready", 4))
    )


_RingswitchGenPortAdapterStatus_Type.__name__ = "Integer32"
_RingswitchGenPortAdapterStatus_Object = MibTableColumn
ringswitchGenPortAdapterStatus = _RingswitchGenPortAdapterStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 2),
    _RingswitchGenPortAdapterStatus_Type()
)
ringswitchGenPortAdapterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchGenPortAdapterStatus.setStatus("mandatory")
_RingswitchGenPortAddress_Type = TRNMacAddress
_RingswitchGenPortAddress_Object = MibTableColumn
ringswitchGenPortAddress = _RingswitchGenPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 3),
    _RingswitchGenPortAddress_Type()
)
ringswitchGenPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchGenPortAddress.setStatus("mandatory")
_RingswitchGenPortLAA_Type = TRNMacAddress
_RingswitchGenPortLAA_Object = MibTableColumn
ringswitchGenPortLAA = _RingswitchGenPortLAA_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 4),
    _RingswitchGenPortLAA_Type()
)
ringswitchGenPortLAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchGenPortLAA.setStatus("mandatory")
_RingswitchGenPortInOctets_Type = INTEGER48
_RingswitchGenPortInOctets_Object = MibTableColumn
ringswitchGenPortInOctets = _RingswitchGenPortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 5),
    _RingswitchGenPortInOctets_Type()
)
ringswitchGenPortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchGenPortInOctets.setStatus("mandatory")
_RingswitchGenPortOutOctets_Type = INTEGER48
_RingswitchGenPortOutOctets_Object = MibTableColumn
ringswitchGenPortOutOctets = _RingswitchGenPortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 6),
    _RingswitchGenPortOutOctets_Type()
)
ringswitchGenPortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchGenPortOutOctets.setStatus("mandatory")


class _RingswitchGenPortResetCounters_Type(Integer32):
    """Custom type ringswitchGenPortResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_RingswitchGenPortResetCounters_Type.__name__ = "Integer32"
_RingswitchGenPortResetCounters_Object = MibTableColumn
ringswitchGenPortResetCounters = _RingswitchGenPortResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 7),
    _RingswitchGenPortResetCounters_Type()
)
ringswitchGenPortResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchGenPortResetCounters.setStatus("mandatory")


class _RingswitchGenPortRMONCapabilities_Type(Integer32):
    """Custom type ringswitchGenPortRMONCapabilities based on Integer32"""
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
        *(("disabled", 1),
          ("economy", 2),
          ("snooping", 4),
          ("standard", 3))
    )


_RingswitchGenPortRMONCapabilities_Type.__name__ = "Integer32"
_RingswitchGenPortRMONCapabilities_Object = MibTableColumn
ringswitchGenPortRMONCapabilities = _RingswitchGenPortRMONCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 8),
    _RingswitchGenPortRMONCapabilities_Type()
)
ringswitchGenPortRMONCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchGenPortRMONCapabilities.setStatus("mandatory")


class _RingswitchGenPortRMONMode_Type(Integer32):
    """Custom type ringswitchGenPortRMONMode based on Integer32"""
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
        *(("disabled", 1),
          ("economy", 2),
          ("snooping", 4),
          ("standard", 3))
    )


_RingswitchGenPortRMONMode_Type.__name__ = "Integer32"
_RingswitchGenPortRMONMode_Object = MibTableColumn
ringswitchGenPortRMONMode = _RingswitchGenPortRMONMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 9),
    _RingswitchGenPortRMONMode_Type()
)
ringswitchGenPortRMONMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchGenPortRMONMode.setStatus("mandatory")
_RingswitchGenPortRMONSnoop_Type = TRNMacAddress
_RingswitchGenPortRMONSnoop_Object = MibTableColumn
ringswitchGenPortRMONSnoop = _RingswitchGenPortRMONSnoop_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 10),
    _RingswitchGenPortRMONSnoop_Type()
)
ringswitchGenPortRMONSnoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchGenPortRMONSnoop.setStatus("mandatory")
_RingswitchGenPortIPXNet_Type = Integer32
_RingswitchGenPortIPXNet_Object = MibTableColumn
ringswitchGenPortIPXNet = _RingswitchGenPortIPXNet_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 11),
    _RingswitchGenPortIPXNet_Type()
)
ringswitchGenPortIPXNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchGenPortIPXNet.setStatus("mandatory")


class _RingswitchGenPortLastStatus_Type(Integer32):
    """Custom type ringswitchGenPortLastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fddi-bypass", 3),
          ("fddi-remove", 1),
          ("fddi-twisted", 2))
    )


_RingswitchGenPortLastStatus_Type.__name__ = "Integer32"
_RingswitchGenPortLastStatus_Object = MibTableColumn
ringswitchGenPortLastStatus = _RingswitchGenPortLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 12),
    _RingswitchGenPortLastStatus_Type()
)
ringswitchGenPortLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchGenPortLastStatus.setStatus("mandatory")


class _RingswitchGenPortCreate_Type(Integer32):
    """Custom type ringswitchGenPortCreate based on Integer32"""
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


_RingswitchGenPortCreate_Type.__name__ = "Integer32"
_RingswitchGenPortCreate_Object = MibTableColumn
ringswitchGenPortCreate = _RingswitchGenPortCreate_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 13),
    _RingswitchGenPortCreate_Type()
)
ringswitchGenPortCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchGenPortCreate.setStatus("mandatory")


class _RingswitchGenPortHealth_Type(Integer32):
    """Custom type ringswitchGenPortHealth based on Integer32"""
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
        *(("critical", 4),
          ("degraded", 3),
          ("normal", 1),
          ("warning", 2))
    )


_RingswitchGenPortHealth_Type.__name__ = "Integer32"
_RingswitchGenPortHealth_Object = MibTableColumn
ringswitchGenPortHealth = _RingswitchGenPortHealth_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 8, 1, 1, 14),
    _RingswitchGenPortHealth_Type()
)
ringswitchGenPortHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchGenPortHealth.setStatus("mandatory")
_RingswitchTR_ObjectIdentity = ObjectIdentity
ringswitchTR = _RingswitchTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 9)
)
_RingswitchTRIfTable_Object = MibTable
ringswitchTRIfTable = _RingswitchTRIfTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1)
)
if mibBuilder.loadTexts:
    ringswitchTRIfTable.setStatus("mandatory")
_RingswitchTRIfEntry_Object = MibTableRow
ringswitchTRIfEntry = _RingswitchTRIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1, 1)
)
ringswitchTRIfEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchTRIfIndex"),
)
if mibBuilder.loadTexts:
    ringswitchTRIfEntry.setStatus("mandatory")
_RingswitchTRIfIndex_Type = Integer32
_RingswitchTRIfIndex_Object = MibTableColumn
ringswitchTRIfIndex = _RingswitchTRIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1, 1, 1),
    _RingswitchTRIfIndex_Type()
)
ringswitchTRIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTRIfIndex.setStatus("mandatory")


class _RingswitchTRIfRingSpeed_Type(Integer32):
    """Custom type ringswitchTRIfRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("four", 1),
          ("hundred", 3),
          ("sixteen", 2))
    )


_RingswitchTRIfRingSpeed_Type.__name__ = "Integer32"
_RingswitchTRIfRingSpeed_Object = MibTableColumn
ringswitchTRIfRingSpeed = _RingswitchTRIfRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1, 1, 2),
    _RingswitchTRIfRingSpeed_Type()
)
ringswitchTRIfRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRIfRingSpeed.setStatus("mandatory")


class _RingswitchTRIfMode_Type(Integer32):
    """Custom type ringswitchTRIfMode based on Integer32"""
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
        *(("conc-classic", 6),
          ("conc-fdx", 4),
          ("concentrator", 2),
          ("node", 1),
          ("node-cau-rio", 7),
          ("node-classic", 5),
          ("node-fdx", 3))
    )


_RingswitchTRIfMode_Type.__name__ = "Integer32"
_RingswitchTRIfMode_Object = MibTableColumn
ringswitchTRIfMode = _RingswitchTRIfMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1, 1, 3),
    _RingswitchTRIfMode_Type()
)
ringswitchTRIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRIfMode.setStatus("mandatory")


class _RingswitchTRIfRPSEnable_Type(Integer32):
    """Custom type ringswitchTRIfRPSEnable based on Integer32"""
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


_RingswitchTRIfRPSEnable_Type.__name__ = "Integer32"
_RingswitchTRIfRPSEnable_Object = MibTableColumn
ringswitchTRIfRPSEnable = _RingswitchTRIfRPSEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1, 1, 4),
    _RingswitchTRIfRPSEnable_Type()
)
ringswitchTRIfRPSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRIfRPSEnable.setStatus("mandatory")


class _RingswitchTRIfRingStatus_Type(Integer32):
    """Custom type ringswitchTRIfRingStatus based on Integer32"""
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
        *(("beaconing", 3),
          ("dtr-wait", 5),
          ("normal", 1),
          ("normal-fdx", 4),
          ("single", 2))
    )


_RingswitchTRIfRingStatus_Type.__name__ = "Integer32"
_RingswitchTRIfRingStatus_Object = MibTableColumn
ringswitchTRIfRingStatus = _RingswitchTRIfRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1, 1, 5),
    _RingswitchTRIfRingStatus_Type()
)
ringswitchTRIfRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTRIfRingStatus.setStatus("mandatory")


class _RingswitchTRIfSoftErrTimer_Type(Integer32):
    """Custom type ringswitchTRIfSoftErrTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchTRIfSoftErrTimer_Type.__name__ = "Integer32"
_RingswitchTRIfSoftErrTimer_Object = MibTableColumn
ringswitchTRIfSoftErrTimer = _RingswitchTRIfSoftErrTimer_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1, 1, 6),
    _RingswitchTRIfSoftErrTimer_Type()
)
ringswitchTRIfSoftErrTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRIfSoftErrTimer.setStatus("mandatory")


class _RingswitchTRIfFrameStatusControl_Type(Integer32):
    """Custom type ringswitchTRIfFrameStatusControl based on Integer32"""
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


_RingswitchTRIfFrameStatusControl_Type.__name__ = "Integer32"
_RingswitchTRIfFrameStatusControl_Object = MibTableColumn
ringswitchTRIfFrameStatusControl = _RingswitchTRIfFrameStatusControl_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1, 1, 7),
    _RingswitchTRIfFrameStatusControl_Type()
)
ringswitchTRIfFrameStatusControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRIfFrameStatusControl.setStatus("mandatory")


class _RingswitchTRIfTokenPriorityControl_Type(Integer32):
    """Custom type ringswitchTRIfTokenPriorityControl based on Integer32"""
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


_RingswitchTRIfTokenPriorityControl_Type.__name__ = "Integer32"
_RingswitchTRIfTokenPriorityControl_Object = MibTableColumn
ringswitchTRIfTokenPriorityControl = _RingswitchTRIfTokenPriorityControl_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1, 1, 8),
    _RingswitchTRIfTokenPriorityControl_Type()
)
ringswitchTRIfTokenPriorityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRIfTokenPriorityControl.setStatus("mandatory")


class _RingswitchTRIfFastFailoverEnable_Type(Integer32):
    """Custom type ringswitchTRIfFastFailoverEnable based on Integer32"""
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


_RingswitchTRIfFastFailoverEnable_Type.__name__ = "Integer32"
_RingswitchTRIfFastFailoverEnable_Object = MibTableColumn
ringswitchTRIfFastFailoverEnable = _RingswitchTRIfFastFailoverEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1, 1, 9),
    _RingswitchTRIfFastFailoverEnable_Type()
)
ringswitchTRIfFastFailoverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRIfFastFailoverEnable.setStatus("mandatory")


class _RingswitchTRIfFastFailoverStandbyStatus_Type(Integer32):
    """Custom type ringswitchTRIfFastFailoverStandbyStatus based on Integer32"""
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
        *(("closed", 2),
          ("open", 1),
          ("open-fail", 5),
          ("opening", 3),
          ("ready", 4))
    )


_RingswitchTRIfFastFailoverStandbyStatus_Type.__name__ = "Integer32"
_RingswitchTRIfFastFailoverStandbyStatus_Object = MibTableColumn
ringswitchTRIfFastFailoverStandbyStatus = _RingswitchTRIfFastFailoverStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1, 1, 10),
    _RingswitchTRIfFastFailoverStandbyStatus_Type()
)
ringswitchTRIfFastFailoverStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTRIfFastFailoverStandbyStatus.setStatus("mandatory")


class _RingswitchTRIfFastFailoverPrimaryPort_Type(Integer32):
    """Custom type ringswitchTRIfFastFailoverPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("left", 1),
          ("right", 2),
          ("unknown", 0))
    )


_RingswitchTRIfFastFailoverPrimaryPort_Type.__name__ = "Integer32"
_RingswitchTRIfFastFailoverPrimaryPort_Object = MibTableColumn
ringswitchTRIfFastFailoverPrimaryPort = _RingswitchTRIfFastFailoverPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1, 1, 11),
    _RingswitchTRIfFastFailoverPrimaryPort_Type()
)
ringswitchTRIfFastFailoverPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRIfFastFailoverPrimaryPort.setStatus("mandatory")


class _RingswitchTRIfFastFailoverTrapInfoReason_Type(Integer32):
    """Custom type ringswitchTRIfFastFailoverTrapInfoReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("links-swapped", 3),
          ("primary-open-fail", 1),
          ("standby-open-fail", 2))
    )


_RingswitchTRIfFastFailoverTrapInfoReason_Type.__name__ = "Integer32"
_RingswitchTRIfFastFailoverTrapInfoReason_Object = MibTableColumn
ringswitchTRIfFastFailoverTrapInfoReason = _RingswitchTRIfFastFailoverTrapInfoReason_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 1, 1, 12),
    _RingswitchTRIfFastFailoverTrapInfoReason_Type()
)
ringswitchTRIfFastFailoverTrapInfoReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ringswitchTRIfFastFailoverTrapInfoReason.setStatus("mandatory")
_RingswitchTRGrpSwtchTable_Object = MibTable
ringswitchTRGrpSwtchTable = _RingswitchTRGrpSwtchTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 2)
)
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchTable.setStatus("mandatory")
_RingswitchTRGrpSwtchEntry_Object = MibTableRow
ringswitchTRGrpSwtchEntry = _RingswitchTRGrpSwtchEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 2, 1)
)
ringswitchTRGrpSwtchEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchTRGrpSwtchIfIndex"),
)
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchEntry.setStatus("mandatory")
_RingswitchTRGrpSwtchIfIndex_Type = Integer32
_RingswitchTRGrpSwtchIfIndex_Object = MibTableColumn
ringswitchTRGrpSwtchIfIndex = _RingswitchTRGrpSwtchIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 2, 1, 1),
    _RingswitchTRGrpSwtchIfIndex_Type()
)
ringswitchTRGrpSwtchIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchIfIndex.setStatus("mandatory")


class _RingswitchTRGrpSwtchRemoveThreshold_Type(Integer32):
    """Custom type ringswitchTRGrpSwtchRemoveThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RingswitchTRGrpSwtchRemoveThreshold_Type.__name__ = "Integer32"
_RingswitchTRGrpSwtchRemoveThreshold_Object = MibTableColumn
ringswitchTRGrpSwtchRemoveThreshold = _RingswitchTRGrpSwtchRemoveThreshold_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 2, 1, 2),
    _RingswitchTRGrpSwtchRemoveThreshold_Type()
)
ringswitchTRGrpSwtchRemoveThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchRemoveThreshold.setStatus("mandatory")


class _RingswitchTRGrpSwtchRingPollAction_Type(Integer32):
    """Custom type ringswitchTRGrpSwtchRingPollAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("inform", 2),
          ("remove", 3))
    )


_RingswitchTRGrpSwtchRingPollAction_Type.__name__ = "Integer32"
_RingswitchTRGrpSwtchRingPollAction_Object = MibTableColumn
ringswitchTRGrpSwtchRingPollAction = _RingswitchTRGrpSwtchRingPollAction_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 2, 1, 3),
    _RingswitchTRGrpSwtchRingPollAction_Type()
)
ringswitchTRGrpSwtchRingPollAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchRingPollAction.setStatus("mandatory")


class _RingswitchTRGrpSwtchBeaconThreshold_Type(Integer32):
    """Custom type ringswitchTRGrpSwtchBeaconThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RingswitchTRGrpSwtchBeaconThreshold_Type.__name__ = "Integer32"
_RingswitchTRGrpSwtchBeaconThreshold_Object = MibTableColumn
ringswitchTRGrpSwtchBeaconThreshold = _RingswitchTRGrpSwtchBeaconThreshold_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 2, 1, 4),
    _RingswitchTRGrpSwtchBeaconThreshold_Type()
)
ringswitchTRGrpSwtchBeaconThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchBeaconThreshold.setStatus("mandatory")


class _RingswitchTRGrpSwtchBeaconAction_Type(Integer32):
    """Custom type ringswitchTRGrpSwtchBeaconAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("inform", 2),
          ("remove", 3))
    )


_RingswitchTRGrpSwtchBeaconAction_Type.__name__ = "Integer32"
_RingswitchTRGrpSwtchBeaconAction_Object = MibTableColumn
ringswitchTRGrpSwtchBeaconAction = _RingswitchTRGrpSwtchBeaconAction_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 2, 1, 5),
    _RingswitchTRGrpSwtchBeaconAction_Type()
)
ringswitchTRGrpSwtchBeaconAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchBeaconAction.setStatus("mandatory")


class _RingswitchTRGrpSwtchPurgeThreshold_Type(Integer32):
    """Custom type ringswitchTRGrpSwtchPurgeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RingswitchTRGrpSwtchPurgeThreshold_Type.__name__ = "Integer32"
_RingswitchTRGrpSwtchPurgeThreshold_Object = MibTableColumn
ringswitchTRGrpSwtchPurgeThreshold = _RingswitchTRGrpSwtchPurgeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 2, 1, 6),
    _RingswitchTRGrpSwtchPurgeThreshold_Type()
)
ringswitchTRGrpSwtchPurgeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchPurgeThreshold.setStatus("mandatory")


class _RingswitchTRGrpSwtchPurgeAction_Type(Integer32):
    """Custom type ringswitchTRGrpSwtchPurgeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("inform", 2),
          ("remove", 3))
    )


_RingswitchTRGrpSwtchPurgeAction_Type.__name__ = "Integer32"
_RingswitchTRGrpSwtchPurgeAction_Object = MibTableColumn
ringswitchTRGrpSwtchPurgeAction = _RingswitchTRGrpSwtchPurgeAction_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 2, 1, 7),
    _RingswitchTRGrpSwtchPurgeAction_Type()
)
ringswitchTRGrpSwtchPurgeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchPurgeAction.setStatus("mandatory")


class _RingswitchTRGrpSwtchIsoErrThreshold_Type(Integer32):
    """Custom type ringswitchTRGrpSwtchIsoErrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RingswitchTRGrpSwtchIsoErrThreshold_Type.__name__ = "Integer32"
_RingswitchTRGrpSwtchIsoErrThreshold_Object = MibTableColumn
ringswitchTRGrpSwtchIsoErrThreshold = _RingswitchTRGrpSwtchIsoErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 2, 1, 8),
    _RingswitchTRGrpSwtchIsoErrThreshold_Type()
)
ringswitchTRGrpSwtchIsoErrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchIsoErrThreshold.setStatus("mandatory")


class _RingswitchTRGrpSwtchIsoErrAction_Type(Integer32):
    """Custom type ringswitchTRGrpSwtchIsoErrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("inform", 2),
          ("remove", 3))
    )


_RingswitchTRGrpSwtchIsoErrAction_Type.__name__ = "Integer32"
_RingswitchTRGrpSwtchIsoErrAction_Object = MibTableColumn
ringswitchTRGrpSwtchIsoErrAction = _RingswitchTRGrpSwtchIsoErrAction_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 2, 1, 9),
    _RingswitchTRGrpSwtchIsoErrAction_Type()
)
ringswitchTRGrpSwtchIsoErrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchIsoErrAction.setStatus("mandatory")


class _RingswitchTRGrpSwtchRingPollThreshold_Type(Integer32):
    """Custom type ringswitchTRGrpSwtchRingPollThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RingswitchTRGrpSwtchRingPollThreshold_Type.__name__ = "Integer32"
_RingswitchTRGrpSwtchRingPollThreshold_Object = MibTableColumn
ringswitchTRGrpSwtchRingPollThreshold = _RingswitchTRGrpSwtchRingPollThreshold_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 2, 1, 10),
    _RingswitchTRGrpSwtchRingPollThreshold_Type()
)
ringswitchTRGrpSwtchRingPollThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchRingPollThreshold.setStatus("mandatory")
_RingswitchTRGrpSwtchPortTable_Object = MibTable
ringswitchTRGrpSwtchPortTable = _RingswitchTRGrpSwtchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 3)
)
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchPortTable.setStatus("mandatory")
_RingswitchTRGrpSwtchPortEntry_Object = MibTableRow
ringswitchTRGrpSwtchPortEntry = _RingswitchTRGrpSwtchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 3, 1)
)
ringswitchTRGrpSwtchPortEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchTRGrpSwtchPortIfIndex"),
    (0, "MADGERSW-MIB", "ringswitchTRGrpSwtchPortIndex"),
)
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchPortEntry.setStatus("mandatory")
_RingswitchTRGrpSwtchPortIfIndex_Type = Integer32
_RingswitchTRGrpSwtchPortIfIndex_Object = MibTableColumn
ringswitchTRGrpSwtchPortIfIndex = _RingswitchTRGrpSwtchPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 3, 1, 1),
    _RingswitchTRGrpSwtchPortIfIndex_Type()
)
ringswitchTRGrpSwtchPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchPortIfIndex.setStatus("mandatory")


class _RingswitchTRGrpSwtchPortIndex_Type(Integer32):
    """Custom type ringswitchTRGrpSwtchPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RingswitchTRGrpSwtchPortIndex_Type.__name__ = "Integer32"
_RingswitchTRGrpSwtchPortIndex_Object = MibTableColumn
ringswitchTRGrpSwtchPortIndex = _RingswitchTRGrpSwtchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 3, 1, 2),
    _RingswitchTRGrpSwtchPortIndex_Type()
)
ringswitchTRGrpSwtchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchPortIndex.setStatus("mandatory")
_RingswitchTRGrpSwtchPortAddress_Type = TRNMacAddress
_RingswitchTRGrpSwtchPortAddress_Object = MibTableColumn
ringswitchTRGrpSwtchPortAddress = _RingswitchTRGrpSwtchPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 3, 1, 3),
    _RingswitchTRGrpSwtchPortAddress_Type()
)
ringswitchTRGrpSwtchPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchPortAddress.setStatus("mandatory")
_RingswitchTRGrpSwtchTrapInfo_ObjectIdentity = ObjectIdentity
ringswitchTRGrpSwtchTrapInfo = _RingswitchTRGrpSwtchTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 4)
)


class _RingswitchTRGrpSwtchTrapInfoReason_Type(Integer32):
    """Custom type ringswitchTRGrpSwtchTrapInfoReason based on Integer32"""
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
        *(("beaconing", 3),
          ("beaconing-fault", 7),
          ("isolating-errors", 5),
          ("reason-unknown", 1),
          ("removal-exceeded", 6),
          ("ring-poll-failure", 2),
          ("ring-purges", 4))
    )


_RingswitchTRGrpSwtchTrapInfoReason_Type.__name__ = "Integer32"
_RingswitchTRGrpSwtchTrapInfoReason_Object = MibScalar
ringswitchTRGrpSwtchTrapInfoReason = _RingswitchTRGrpSwtchTrapInfoReason_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 4, 1),
    _RingswitchTRGrpSwtchTrapInfoReason_Type()
)
ringswitchTRGrpSwtchTrapInfoReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchTrapInfoReason.setStatus("mandatory")
_RingswitchTRGrpSwtchSlotTable_Object = MibTable
ringswitchTRGrpSwtchSlotTable = _RingswitchTRGrpSwtchSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 5)
)
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchSlotTable.setStatus("mandatory")
_RingswitchTRGrpSwtchSlotEntry_Object = MibTableRow
ringswitchTRGrpSwtchSlotEntry = _RingswitchTRGrpSwtchSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 5, 1)
)
ringswitchTRGrpSwtchSlotEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchTRGrpSwtchSlotIndex"),
)
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchSlotEntry.setStatus("mandatory")


class _RingswitchTRGrpSwtchSlotIndex_Type(Integer32):
    """Custom type ringswitchTRGrpSwtchSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchTRGrpSwtchSlotIndex_Type.__name__ = "Integer32"
_RingswitchTRGrpSwtchSlotIndex_Object = MibTableColumn
ringswitchTRGrpSwtchSlotIndex = _RingswitchTRGrpSwtchSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 5, 1, 1),
    _RingswitchTRGrpSwtchSlotIndex_Type()
)
ringswitchTRGrpSwtchSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchSlotIndex.setStatus("mandatory")
_RingswitchTRGrpSwtchSlotAdminStatii_Type = OctetString
_RingswitchTRGrpSwtchSlotAdminStatii_Object = MibTableColumn
ringswitchTRGrpSwtchSlotAdminStatii = _RingswitchTRGrpSwtchSlotAdminStatii_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 5, 1, 2),
    _RingswitchTRGrpSwtchSlotAdminStatii_Type()
)
ringswitchTRGrpSwtchSlotAdminStatii.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchSlotAdminStatii.setStatus("mandatory")
_RingswitchTRGrpSwtchSlotAutoPartitions_Type = OctetString
_RingswitchTRGrpSwtchSlotAutoPartitions_Object = MibTableColumn
ringswitchTRGrpSwtchSlotAutoPartitions = _RingswitchTRGrpSwtchSlotAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 5, 1, 3),
    _RingswitchTRGrpSwtchSlotAutoPartitions_Type()
)
ringswitchTRGrpSwtchSlotAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchSlotAutoPartitions.setStatus("mandatory")
_RingswitchTRGrpSwtchSlotOperStatii_Type = OctetString
_RingswitchTRGrpSwtchSlotOperStatii_Object = MibTableColumn
ringswitchTRGrpSwtchSlotOperStatii = _RingswitchTRGrpSwtchSlotOperStatii_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 9, 5, 1, 4),
    _RingswitchTRGrpSwtchSlotOperStatii_Type()
)
ringswitchTRGrpSwtchSlotOperStatii.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTRGrpSwtchSlotOperStatii.setStatus("mandatory")
_RingswitchFDDI_ObjectIdentity = ObjectIdentity
ringswitchFDDI = _RingswitchFDDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 10)
)
_RingswitchFDDICardTable_Object = MibTable
ringswitchFDDICardTable = _RingswitchFDDICardTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 10, 1)
)
if mibBuilder.loadTexts:
    ringswitchFDDICardTable.setStatus("mandatory")
_RingswitchFDDICardEntry_Object = MibTableRow
ringswitchFDDICardEntry = _RingswitchFDDICardEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 10, 1, 1)
)
ringswitchFDDICardEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchFDDICardNum"),
)
if mibBuilder.loadTexts:
    ringswitchFDDICardEntry.setStatus("mandatory")


class _RingswitchFDDICardNum_Type(Integer32):
    """Custom type ringswitchFDDICardNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchFDDICardNum_Type.__name__ = "Integer32"
_RingswitchFDDICardNum_Object = MibTableColumn
ringswitchFDDICardNum = _RingswitchFDDICardNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 10, 1, 1, 1),
    _RingswitchFDDICardNum_Type()
)
ringswitchFDDICardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFDDICardNum.setStatus("mandatory")


class _RingswitchFDDICardSMTIndex_Type(Integer32):
    """Custom type ringswitchFDDICardSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchFDDICardSMTIndex_Type.__name__ = "Integer32"
_RingswitchFDDICardSMTIndex_Object = MibTableColumn
ringswitchFDDICardSMTIndex = _RingswitchFDDICardSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 10, 1, 1, 2),
    _RingswitchFDDICardSMTIndex_Type()
)
ringswitchFDDICardSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFDDICardSMTIndex.setStatus("mandatory")


class _RingswitchFDDICardFixupMode_Type(Integer32):
    """Custom type ringswitchFDDICardFixupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("fddi-all", 2))
    )


_RingswitchFDDICardFixupMode_Type.__name__ = "Integer32"
_RingswitchFDDICardFixupMode_Object = MibTableColumn
ringswitchFDDICardFixupMode = _RingswitchFDDICardFixupMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 10, 1, 1, 3),
    _RingswitchFDDICardFixupMode_Type()
)
ringswitchFDDICardFixupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFDDICardFixupMode.setStatus("mandatory")


class _RingswitchFDDICardVRStatus_Type(Integer32):
    """Custom type ringswitchFDDICardVRStatus based on Integer32"""
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


_RingswitchFDDICardVRStatus_Type.__name__ = "Integer32"
_RingswitchFDDICardVRStatus_Object = MibTableColumn
ringswitchFDDICardVRStatus = _RingswitchFDDICardVRStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 10, 1, 1, 4),
    _RingswitchFDDICardVRStatus_Type()
)
ringswitchFDDICardVRStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFDDICardVRStatus.setStatus("mandatory")
_RingswitchFDDICardVRRingNum_Type = Integer32
_RingswitchFDDICardVRRingNum_Object = MibTableColumn
ringswitchFDDICardVRRingNum = _RingswitchFDDICardVRRingNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 10, 1, 1, 5),
    _RingswitchFDDICardVRRingNum_Type()
)
ringswitchFDDICardVRRingNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFDDICardVRRingNum.setStatus("mandatory")
_RingswitchFDDICardVRBridgeNum_Type = Integer32
_RingswitchFDDICardVRBridgeNum_Object = MibTableColumn
ringswitchFDDICardVRBridgeNum = _RingswitchFDDICardVRBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 10, 1, 1, 6),
    _RingswitchFDDICardVRBridgeNum_Type()
)
ringswitchFDDICardVRBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFDDICardVRBridgeNum.setStatus("mandatory")
_RingswitchFDDICardStatus_Type = Integer32
_RingswitchFDDICardStatus_Object = MibTableColumn
ringswitchFDDICardStatus = _RingswitchFDDICardStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 10, 1, 1, 7),
    _RingswitchFDDICardStatus_Type()
)
ringswitchFDDICardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFDDICardStatus.setStatus("mandatory")
_RingswitchATM_ObjectIdentity = ObjectIdentity
ringswitchATM = _RingswitchATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 11)
)
_RingswitchATMCardTable_Object = MibTable
ringswitchATMCardTable = _RingswitchATMCardTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1)
)
if mibBuilder.loadTexts:
    ringswitchATMCardTable.setStatus("mandatory")
_RingswitchATMCardEntry_Object = MibTableRow
ringswitchATMCardEntry = _RingswitchATMCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1)
)
ringswitchATMCardEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchATMCardNum"),
)
if mibBuilder.loadTexts:
    ringswitchATMCardEntry.setStatus("mandatory")


class _RingswitchATMCardNum_Type(Integer32):
    """Custom type ringswitchATMCardNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchATMCardNum_Type.__name__ = "Integer32"
_RingswitchATMCardNum_Object = MibTableColumn
ringswitchATMCardNum = _RingswitchATMCardNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 1),
    _RingswitchATMCardNum_Type()
)
ringswitchATMCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMCardNum.setStatus("mandatory")


class _RingswitchATMCardAdminStatus_Type(Integer32):
    """Custom type ringswitchATMCardAdminStatus based on Integer32"""
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


_RingswitchATMCardAdminStatus_Type.__name__ = "Integer32"
_RingswitchATMCardAdminStatus_Object = MibTableColumn
ringswitchATMCardAdminStatus = _RingswitchATMCardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 2),
    _RingswitchATMCardAdminStatus_Type()
)
ringswitchATMCardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMCardAdminStatus.setStatus("mandatory")


class _RingswitchATMCardRemoteUNIVer_Type(Integer32):
    """Custom type ringswitchATMCardRemoteUNIVer based on Integer32"""
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
        *(("uni-30", 2),
          ("uni-31", 3),
          ("uni-40", 4),
          ("unknown", 1))
    )


_RingswitchATMCardRemoteUNIVer_Type.__name__ = "Integer32"
_RingswitchATMCardRemoteUNIVer_Object = MibTableColumn
ringswitchATMCardRemoteUNIVer = _RingswitchATMCardRemoteUNIVer_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 3),
    _RingswitchATMCardRemoteUNIVer_Type()
)
ringswitchATMCardRemoteUNIVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMCardRemoteUNIVer.setStatus("mandatory")
_RingswitchATMCardLECSAddress_Type = NSAP
_RingswitchATMCardLECSAddress_Object = MibTableColumn
ringswitchATMCardLECSAddress = _RingswitchATMCardLECSAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 4),
    _RingswitchATMCardLECSAddress_Type()
)
ringswitchATMCardLECSAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMCardLECSAddress.setStatus("mandatory")


class _RingswitchATMCardLECSIlmi_Type(Integer32):
    """Custom type ringswitchATMCardLECSIlmi based on Integer32"""
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


_RingswitchATMCardLECSIlmi_Type.__name__ = "Integer32"
_RingswitchATMCardLECSIlmi_Object = MibTableColumn
ringswitchATMCardLECSIlmi = _RingswitchATMCardLECSIlmi_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 5),
    _RingswitchATMCardLECSIlmi_Type()
)
ringswitchATMCardLECSIlmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMCardLECSIlmi.setStatus("mandatory")


class _RingswitchATMCardLECSWka_Type(Integer32):
    """Custom type ringswitchATMCardLECSWka based on Integer32"""
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


_RingswitchATMCardLECSWka_Type.__name__ = "Integer32"
_RingswitchATMCardLECSWka_Object = MibTableColumn
ringswitchATMCardLECSWka = _RingswitchATMCardLECSWka_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 6),
    _RingswitchATMCardLECSWka_Type()
)
ringswitchATMCardLECSWka.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMCardLECSWka.setStatus("mandatory")


class _RingswitchATMCardLECSPvc_Type(Integer32):
    """Custom type ringswitchATMCardLECSPvc based on Integer32"""
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


_RingswitchATMCardLECSPvc_Type.__name__ = "Integer32"
_RingswitchATMCardLECSPvc_Object = MibTableColumn
ringswitchATMCardLECSPvc = _RingswitchATMCardLECSPvc_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 7),
    _RingswitchATMCardLECSPvc_Type()
)
ringswitchATMCardLECSPvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMCardLECSPvc.setStatus("mandatory")


class _RingswitchATMCardActivePort_Type(Integer32):
    """Custom type ringswitchATMCardActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-a", 1),
          ("port-b", 2))
    )


_RingswitchATMCardActivePort_Type.__name__ = "Integer32"
_RingswitchATMCardActivePort_Object = MibTableColumn
ringswitchATMCardActivePort = _RingswitchATMCardActivePort_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 8),
    _RingswitchATMCardActivePort_Type()
)
ringswitchATMCardActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMCardActivePort.setStatus("mandatory")


class _RingswitchATMCardILMIStatus_Type(Integer32):
    """Custom type ringswitchATMCardILMIStatus based on Integer32"""
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


_RingswitchATMCardILMIStatus_Type.__name__ = "Integer32"
_RingswitchATMCardILMIStatus_Object = MibTableColumn
ringswitchATMCardILMIStatus = _RingswitchATMCardILMIStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 9),
    _RingswitchATMCardILMIStatus_Type()
)
ringswitchATMCardILMIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMCardILMIStatus.setStatus("mandatory")


class _RingswitchATMCardSignalStatus_Type(Integer32):
    """Custom type ringswitchATMCardSignalStatus based on Integer32"""
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


_RingswitchATMCardSignalStatus_Type.__name__ = "Integer32"
_RingswitchATMCardSignalStatus_Object = MibTableColumn
ringswitchATMCardSignalStatus = _RingswitchATMCardSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 10),
    _RingswitchATMCardSignalStatus_Type()
)
ringswitchATMCardSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMCardSignalStatus.setStatus("mandatory")
_RingswitchATMCardHardWiredESI_Type = ETHMacAddress
_RingswitchATMCardHardWiredESI_Object = MibTableColumn
ringswitchATMCardHardWiredESI = _RingswitchATMCardHardWiredESI_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 11),
    _RingswitchATMCardHardWiredESI_Type()
)
ringswitchATMCardHardWiredESI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMCardHardWiredESI.setStatus("mandatory")
_RingswitchATMCardLocalESI_Type = ETHMacAddress
_RingswitchATMCardLocalESI_Object = MibTableColumn
ringswitchATMCardLocalESI = _RingswitchATMCardLocalESI_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 12),
    _RingswitchATMCardLocalESI_Type()
)
ringswitchATMCardLocalESI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMCardLocalESI.setStatus("mandatory")


class _RingswitchATMCardPortB_Type(Integer32):
    """Custom type ringswitchATMCardPortB based on Integer32"""
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


_RingswitchATMCardPortB_Type.__name__ = "Integer32"
_RingswitchATMCardPortB_Object = MibTableColumn
ringswitchATMCardPortB = _RingswitchATMCardPortB_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 13),
    _RingswitchATMCardPortB_Type()
)
ringswitchATMCardPortB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMCardPortB.setStatus("mandatory")


class _RingswitchATMCardMode_Type(Integer32):
    """Custom type ringswitchATMCardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_RingswitchATMCardMode_Type.__name__ = "Integer32"
_RingswitchATMCardMode_Object = MibTableColumn
ringswitchATMCardMode = _RingswitchATMCardMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 14),
    _RingswitchATMCardMode_Type()
)
ringswitchATMCardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMCardMode.setStatus("mandatory")
_RingswitchATMCardSONETIfIndex_Type = Integer32
_RingswitchATMCardSONETIfIndex_Object = MibTableColumn
ringswitchATMCardSONETIfIndex = _RingswitchATMCardSONETIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 15),
    _RingswitchATMCardSONETIfIndex_Type()
)
ringswitchATMCardSONETIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMCardSONETIfIndex.setStatus("mandatory")
_RingswitchATMCardATMIfIndex_Type = Integer32
_RingswitchATMCardATMIfIndex_Object = MibTableColumn
ringswitchATMCardATMIfIndex = _RingswitchATMCardATMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 16),
    _RingswitchATMCardATMIfIndex_Type()
)
ringswitchATMCardATMIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMCardATMIfIndex.setStatus("mandatory")
_RingswitchATMCardAAL5IfIndex_Type = Integer32
_RingswitchATMCardAAL5IfIndex_Object = MibTableColumn
ringswitchATMCardAAL5IfIndex = _RingswitchATMCardAAL5IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 17),
    _RingswitchATMCardAAL5IfIndex_Type()
)
ringswitchATMCardAAL5IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMCardAAL5IfIndex.setStatus("mandatory")
_RingswitchATMCardRowStatuses_Type = OctetString
_RingswitchATMCardRowStatuses_Object = MibTableColumn
ringswitchATMCardRowStatuses = _RingswitchATMCardRowStatuses_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 18),
    _RingswitchATMCardRowStatuses_Type()
)
ringswitchATMCardRowStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMCardRowStatuses.setStatus("mandatory")


class _RingswitchATMCardMediaType_Type(Integer32):
    """Custom type ringswitchATMCardMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multi-mode-fiber", 1),
          ("single-mode-fiber", 2))
    )


_RingswitchATMCardMediaType_Type.__name__ = "Integer32"
_RingswitchATMCardMediaType_Object = MibTableColumn
ringswitchATMCardMediaType = _RingswitchATMCardMediaType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 19),
    _RingswitchATMCardMediaType_Type()
)
ringswitchATMCardMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMCardMediaType.setStatus("mandatory")


class _RingswitchATMCardConfigUNIVer_Type(Integer32):
    """Custom type ringswitchATMCardConfigUNIVer based on Integer32"""
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
        *(("autoConfig", 1),
          ("uni-30", 2),
          ("uni-31", 3),
          ("uni-40", 4))
    )


_RingswitchATMCardConfigUNIVer_Type.__name__ = "Integer32"
_RingswitchATMCardConfigUNIVer_Object = MibTableColumn
ringswitchATMCardConfigUNIVer = _RingswitchATMCardConfigUNIVer_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 20),
    _RingswitchATMCardConfigUNIVer_Type()
)
ringswitchATMCardConfigUNIVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMCardConfigUNIVer.setStatus("mandatory")


class _RingswitchATMCardActualUNIVer_Type(Integer32):
    """Custom type ringswitchATMCardActualUNIVer based on Integer32"""
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
        *(("uni-30", 2),
          ("uni-31", 3),
          ("uni-40", 4),
          ("unknown", 1))
    )


_RingswitchATMCardActualUNIVer_Type.__name__ = "Integer32"
_RingswitchATMCardActualUNIVer_Object = MibTableColumn
ringswitchATMCardActualUNIVer = _RingswitchATMCardActualUNIVer_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 21),
    _RingswitchATMCardActualUNIVer_Type()
)
ringswitchATMCardActualUNIVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMCardActualUNIVer.setStatus("mandatory")


class _RingswitchATMCardEthLecSupport_Type(Integer32):
    """Custom type ringswitchATMCardEthLecSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_RingswitchATMCardEthLecSupport_Type.__name__ = "Integer32"
_RingswitchATMCardEthLecSupport_Object = MibTableColumn
ringswitchATMCardEthLecSupport = _RingswitchATMCardEthLecSupport_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 1, 1, 22),
    _RingswitchATMCardEthLecSupport_Type()
)
ringswitchATMCardEthLecSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMCardEthLecSupport.setStatus("mandatory")
_RingswitchATMPortTable_Object = MibTable
ringswitchATMPortTable = _RingswitchATMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2)
)
if mibBuilder.loadTexts:
    ringswitchATMPortTable.setStatus("mandatory")
_RingswitchATMPortEntry_Object = MibTableRow
ringswitchATMPortEntry = _RingswitchATMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1)
)
ringswitchATMPortEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchATMPortNum"),
)
if mibBuilder.loadTexts:
    ringswitchATMPortEntry.setStatus("mandatory")


class _RingswitchATMPortNum_Type(Integer32):
    """Custom type ringswitchATMPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchATMPortNum_Type.__name__ = "Integer32"
_RingswitchATMPortNum_Object = MibTableColumn
ringswitchATMPortNum = _RingswitchATMPortNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 1),
    _RingswitchATMPortNum_Type()
)
ringswitchATMPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMPortNum.setStatus("mandatory")


class _RingswitchATMPortFailReason_Type(Integer32):
    """Custom type ringswitchATMPortFailReason based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("already-open", 15),
          ("bus-connect-fail", 8),
          ("bus-didnt-connect", 9),
          ("bus-not-found", 7),
          ("bus-vc-dropped", 12),
          ("config-failed", 4),
          ("duplicate-elan", 10),
          ("insufficient-memory", 14),
          ("invalid-port", 16),
          ("join-failed", 6),
          ("lecs-not-found", 3),
          ("les-connect-fail", 5),
          ("les-vc-dropped", 11),
          ("rejoin-wrong-elan", 13),
          ("sig-ilmi-fail", 2),
          ("success", 1),
          ("unknown", 17))
    )


_RingswitchATMPortFailReason_Type.__name__ = "Integer32"
_RingswitchATMPortFailReason_Object = MibTableColumn
ringswitchATMPortFailReason = _RingswitchATMPortFailReason_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 2),
    _RingswitchATMPortFailReason_Type()
)
ringswitchATMPortFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMPortFailReason.setStatus("mandatory")


class _RingswitchATMPortFailSecondary_Type(Integer32):
    """Custom type ringswitchATMPortFailSecondary based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("access-denied", 9),
          ("dup-atm-address", 7),
          ("dup-lan-destination", 6),
          ("insuff-information", 15),
          ("insuff-resources", 8),
          ("invalid-atm-address", 12),
          ("invalid-lan-destination", 11),
          ("invalid-request-params", 5),
          ("invalid-requester-id", 10),
          ("le-configure-error", 14),
          ("no-configuration", 13),
          ("none", 1),
          ("timeout", 2),
          ("undefined-error", 3),
          ("version-not-supported", 4))
    )


_RingswitchATMPortFailSecondary_Type.__name__ = "Integer32"
_RingswitchATMPortFailSecondary_Object = MibTableColumn
ringswitchATMPortFailSecondary = _RingswitchATMPortFailSecondary_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 3),
    _RingswitchATMPortFailSecondary_Type()
)
ringswitchATMPortFailSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMPortFailSecondary.setStatus("mandatory")
_RingswitchATMPortRxDiscards_Type = Integer32
_RingswitchATMPortRxDiscards_Object = MibTableColumn
ringswitchATMPortRxDiscards = _RingswitchATMPortRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 4),
    _RingswitchATMPortRxDiscards_Type()
)
ringswitchATMPortRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMPortRxDiscards.setStatus("mandatory")
_RingswitchATMPortTxDiscards_Type = Integer32
_RingswitchATMPortTxDiscards_Object = MibTableColumn
ringswitchATMPortTxDiscards = _RingswitchATMPortTxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 5),
    _RingswitchATMPortTxDiscards_Type()
)
ringswitchATMPortTxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMPortTxDiscards.setStatus("mandatory")
_RingswitchATMPortTxQuotaDiscards_Type = Integer32
_RingswitchATMPortTxQuotaDiscards_Object = MibTableColumn
ringswitchATMPortTxQuotaDiscards = _RingswitchATMPortTxQuotaDiscards_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 6),
    _RingswitchATMPortTxQuotaDiscards_Type()
)
ringswitchATMPortTxQuotaDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMPortTxQuotaDiscards.setStatus("mandatory")
_RingswitchATMPortTxBUSBroadcasts_Type = Integer32
_RingswitchATMPortTxBUSBroadcasts_Object = MibTableColumn
ringswitchATMPortTxBUSBroadcasts = _RingswitchATMPortTxBUSBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 7),
    _RingswitchATMPortTxBUSBroadcasts_Type()
)
ringswitchATMPortTxBUSBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMPortTxBUSBroadcasts.setStatus("mandatory")
_RingswitchATMPortTxBUSUnknowns_Type = Integer32
_RingswitchATMPortTxBUSUnknowns_Object = MibTableColumn
ringswitchATMPortTxBUSUnknowns = _RingswitchATMPortTxBUSUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 8),
    _RingswitchATMPortTxBUSUnknowns_Type()
)
ringswitchATMPortTxBUSUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMPortTxBUSUnknowns.setStatus("mandatory")
_RingswitchATMPortRxBUSFiltered_Type = Integer32
_RingswitchATMPortRxBUSFiltered_Object = MibTableColumn
ringswitchATMPortRxBUSFiltered = _RingswitchATMPortRxBUSFiltered_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 9),
    _RingswitchATMPortRxBUSFiltered_Type()
)
ringswitchATMPortRxBUSFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchATMPortRxBUSFiltered.setStatus("mandatory")


class _RingswitchATMPortIPXTypeETH_Type(Integer32):
    """Custom type ringswitchATMPortIPXTypeETH based on Integer32"""
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
        *(("auto", 1),
          ("dix", 5),
          ("ieee8022", 2),
          ("ieee8023", 4),
          ("snap", 3))
    )


_RingswitchATMPortIPXTypeETH_Type.__name__ = "Integer32"
_RingswitchATMPortIPXTypeETH_Object = MibTableColumn
ringswitchATMPortIPXTypeETH = _RingswitchATMPortIPXTypeETH_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 10),
    _RingswitchATMPortIPXTypeETH_Type()
)
ringswitchATMPortIPXTypeETH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMPortIPXTypeETH.setStatus("mandatory")


class _RingswitchATMPortIPXTypeTRN_Type(Integer32):
    """Custom type ringswitchATMPortIPXTypeTRN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("ieee8022", 2),
          ("snap", 3))
    )


_RingswitchATMPortIPXTypeTRN_Type.__name__ = "Integer32"
_RingswitchATMPortIPXTypeTRN_Object = MibTableColumn
ringswitchATMPortIPXTypeTRN = _RingswitchATMPortIPXTypeTRN_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 11),
    _RingswitchATMPortIPXTypeTRN_Type()
)
ringswitchATMPortIPXTypeTRN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMPortIPXTypeTRN.setStatus("mandatory")


class _RingswitchATMPortIPXEvenize_Type(Integer32):
    """Custom type ringswitchATMPortIPXEvenize based on Integer32"""
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


_RingswitchATMPortIPXEvenize_Type.__name__ = "Integer32"
_RingswitchATMPortIPXEvenize_Object = MibTableColumn
ringswitchATMPortIPXEvenize = _RingswitchATMPortIPXEvenize_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 12),
    _RingswitchATMPortIPXEvenize_Type()
)
ringswitchATMPortIPXEvenize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMPortIPXEvenize.setStatus("mandatory")


class _RingswitchATMPortIPXBufLimit_Type(Integer32):
    """Custom type ringswitchATMPortIPXBufLimit based on Integer32"""
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


_RingswitchATMPortIPXBufLimit_Type.__name__ = "Integer32"
_RingswitchATMPortIPXBufLimit_Object = MibTableColumn
ringswitchATMPortIPXBufLimit = _RingswitchATMPortIPXBufLimit_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 13),
    _RingswitchATMPortIPXBufLimit_Type()
)
ringswitchATMPortIPXBufLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMPortIPXBufLimit.setStatus("mandatory")


class _RingswitchATMPortIPXEnable_Type(Integer32):
    """Custom type ringswitchATMPortIPXEnable based on Integer32"""
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


_RingswitchATMPortIPXEnable_Type.__name__ = "Integer32"
_RingswitchATMPortIPXEnable_Object = MibTableColumn
ringswitchATMPortIPXEnable = _RingswitchATMPortIPXEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 14),
    _RingswitchATMPortIPXEnable_Type()
)
ringswitchATMPortIPXEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMPortIPXEnable.setStatus("mandatory")


class _RingswitchATMPortIPEnable_Type(Integer32):
    """Custom type ringswitchATMPortIPEnable based on Integer32"""
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


_RingswitchATMPortIPEnable_Type.__name__ = "Integer32"
_RingswitchATMPortIPEnable_Object = MibTableColumn
ringswitchATMPortIPEnable = _RingswitchATMPortIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 15),
    _RingswitchATMPortIPEnable_Type()
)
ringswitchATMPortIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMPortIPEnable.setStatus("mandatory")


class _RingswitchATMPortIPMulticastType_Type(Integer32):
    """Custom type ringswitchATMPortIPMulticastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("functional", 2),
          ("group", 3))
    )


_RingswitchATMPortIPMulticastType_Type.__name__ = "Integer32"
_RingswitchATMPortIPMulticastType_Object = MibTableColumn
ringswitchATMPortIPMulticastType = _RingswitchATMPortIPMulticastType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 11, 2, 1, 16),
    _RingswitchATMPortIPMulticastType_Type()
)
ringswitchATMPortIPMulticastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchATMPortIPMulticastType.setStatus("mandatory")
_RingswitchPSU_ObjectIdentity = ObjectIdentity
ringswitchPSU = _RingswitchPSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 12)
)
_RingswitchPSUNumUnits_Type = Integer32
_RingswitchPSUNumUnits_Object = MibScalar
ringswitchPSUNumUnits = _RingswitchPSUNumUnits_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 12, 1),
    _RingswitchPSUNumUnits_Type()
)
ringswitchPSUNumUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPSUNumUnits.setStatus("mandatory")
_RingswitchPSUTable_Object = MibTable
ringswitchPSUTable = _RingswitchPSUTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 12, 2)
)
if mibBuilder.loadTexts:
    ringswitchPSUTable.setStatus("mandatory")
_RingswitchPSUEntry_Object = MibTableRow
ringswitchPSUEntry = _RingswitchPSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 12, 2, 1)
)
ringswitchPSUEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchPSUIndex"),
)
if mibBuilder.loadTexts:
    ringswitchPSUEntry.setStatus("mandatory")


class _RingswitchPSUIndex_Type(Integer32):
    """Custom type ringswitchPSUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchPSUIndex_Type.__name__ = "Integer32"
_RingswitchPSUIndex_Object = MibTableColumn
ringswitchPSUIndex = _RingswitchPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 12, 2, 1, 1),
    _RingswitchPSUIndex_Type()
)
ringswitchPSUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPSUIndex.setStatus("mandatory")


class _RingswitchPSUDescription_Type(DisplayString):
    """Custom type ringswitchPSUDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RingswitchPSUDescription_Type.__name__ = "DisplayString"
_RingswitchPSUDescription_Object = MibTableColumn
ringswitchPSUDescription = _RingswitchPSUDescription_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 12, 2, 1, 2),
    _RingswitchPSUDescription_Type()
)
ringswitchPSUDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPSUDescription.setStatus("mandatory")


class _RingswitchPSUStatus_Type(Integer32):
    """Custom type ringswitchPSUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unit-absent", 1),
          ("unit-broken", 2),
          ("unit-normal", 3))
    )


_RingswitchPSUStatus_Type.__name__ = "Integer32"
_RingswitchPSUStatus_Object = MibTableColumn
ringswitchPSUStatus = _RingswitchPSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 12, 2, 1, 3),
    _RingswitchPSUStatus_Type()
)
ringswitchPSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchPSUStatus.setStatus("mandatory")
_RingswitchFan_ObjectIdentity = ObjectIdentity
ringswitchFan = _RingswitchFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 13)
)
_RingswitchFanNumUnits_Type = Integer32
_RingswitchFanNumUnits_Object = MibScalar
ringswitchFanNumUnits = _RingswitchFanNumUnits_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 13, 1),
    _RingswitchFanNumUnits_Type()
)
ringswitchFanNumUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFanNumUnits.setStatus("mandatory")
_RingswitchFanTable_Object = MibTable
ringswitchFanTable = _RingswitchFanTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 13, 2)
)
if mibBuilder.loadTexts:
    ringswitchFanTable.setStatus("mandatory")
_RingswitchFanEntry_Object = MibTableRow
ringswitchFanEntry = _RingswitchFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 13, 2, 1)
)
ringswitchFanEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchFanIndex"),
)
if mibBuilder.loadTexts:
    ringswitchFanEntry.setStatus("mandatory")


class _RingswitchFanIndex_Type(Integer32):
    """Custom type ringswitchFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchFanIndex_Type.__name__ = "Integer32"
_RingswitchFanIndex_Object = MibTableColumn
ringswitchFanIndex = _RingswitchFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 13, 2, 1, 1),
    _RingswitchFanIndex_Type()
)
ringswitchFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFanIndex.setStatus("mandatory")


class _RingswitchFanDescription_Type(DisplayString):
    """Custom type ringswitchFanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RingswitchFanDescription_Type.__name__ = "DisplayString"
_RingswitchFanDescription_Object = MibTableColumn
ringswitchFanDescription = _RingswitchFanDescription_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 13, 2, 1, 2),
    _RingswitchFanDescription_Type()
)
ringswitchFanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFanDescription.setStatus("mandatory")


class _RingswitchFanSpeed_Type(Integer32):
    """Custom type ringswitchFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RingswitchFanSpeed_Type.__name__ = "Integer32"
_RingswitchFanSpeed_Object = MibTableColumn
ringswitchFanSpeed = _RingswitchFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 13, 2, 1, 3),
    _RingswitchFanSpeed_Type()
)
ringswitchFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFanSpeed.setStatus("mandatory")
_RingswitchTrap_ObjectIdentity = ObjectIdentity
ringswitchTrap = _RingswitchTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 14)
)


class _RingswitchRouteDescrSegmentID_Type(Integer32):
    """Custom type ringswitchRouteDescrSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RingswitchRouteDescrSegmentID_Type.__name__ = "Integer32"
_RingswitchRouteDescrSegmentID_Object = MibScalar
ringswitchRouteDescrSegmentID = _RingswitchRouteDescrSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 14, 1),
    _RingswitchRouteDescrSegmentID_Type()
)
ringswitchRouteDescrSegmentID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ringswitchRouteDescrSegmentID.setStatus("mandatory")


class _RingswitchRouteDescrBridgeNumber_Type(Integer32):
    """Custom type ringswitchRouteDescrBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RingswitchRouteDescrBridgeNumber_Type.__name__ = "Integer32"
_RingswitchRouteDescrBridgeNumber_Object = MibScalar
ringswitchRouteDescrBridgeNumber = _RingswitchRouteDescrBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 14, 2),
    _RingswitchRouteDescrBridgeNumber_Type()
)
ringswitchRouteDescrBridgeNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ringswitchRouteDescrBridgeNumber.setStatus("mandatory")


class _RingswitchVersionMismatch_Type(Integer32):
    """Custom type ringswitchVersionMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("boot-eprom-and-boot-flash", 1)
    )


_RingswitchVersionMismatch_Type.__name__ = "Integer32"
_RingswitchVersionMismatch_Object = MibScalar
ringswitchVersionMismatch = _RingswitchVersionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 14, 3),
    _RingswitchVersionMismatch_Type()
)
ringswitchVersionMismatch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ringswitchVersionMismatch.setStatus("mandatory")


class _RingswitchDownloadFailed_Type(Integer32):
    """Custom type ringswitchDownloadFailed based on Integer32"""
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
        *(("atm-code", 4),
          ("boot-code", 2),
          ("fddi-code", 3),
          ("microcode", 1))
    )


_RingswitchDownloadFailed_Type.__name__ = "Integer32"
_RingswitchDownloadFailed_Object = MibScalar
ringswitchDownloadFailed = _RingswitchDownloadFailed_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 14, 4),
    _RingswitchDownloadFailed_Type()
)
ringswitchDownloadFailed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ringswitchDownloadFailed.setStatus("mandatory")
_RingswitchFilter_ObjectIdentity = ObjectIdentity
ringswitchFilter = _RingswitchFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 15)
)
_RingswitchFilterTable_Object = MibTable
ringswitchFilterTable = _RingswitchFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 1)
)
if mibBuilder.loadTexts:
    ringswitchFilterTable.setStatus("mandatory")
_RingswitchFilterEntry_Object = MibTableRow
ringswitchFilterEntry = _RingswitchFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 1, 1)
)
ringswitchFilterEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchFilterIndex"),
)
if mibBuilder.loadTexts:
    ringswitchFilterEntry.setStatus("mandatory")
_RingswitchFilterIndex_Type = Integer32
_RingswitchFilterIndex_Object = MibTableColumn
ringswitchFilterIndex = _RingswitchFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 1, 1, 1),
    _RingswitchFilterIndex_Type()
)
ringswitchFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFilterIndex.setStatus("mandatory")
_RingswitchFilterStatus_Type = RingswitchRowStatus
_RingswitchFilterStatus_Object = MibTableColumn
ringswitchFilterStatus = _RingswitchFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 1, 1, 2),
    _RingswitchFilterStatus_Type()
)
ringswitchFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFilterStatus.setStatus("mandatory")
_RingswitchFilterName_Type = DisplayString
_RingswitchFilterName_Object = MibTableColumn
ringswitchFilterName = _RingswitchFilterName_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 1, 1, 3),
    _RingswitchFilterName_Type()
)
ringswitchFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFilterName.setStatus("mandatory")


class _RingswitchFilterData_Type(OctetString):
    """Custom type ringswitchFilterData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RingswitchFilterData_Type.__name__ = "OctetString"
_RingswitchFilterData_Object = MibTableColumn
ringswitchFilterData = _RingswitchFilterData_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 1, 1, 4),
    _RingswitchFilterData_Type()
)
ringswitchFilterData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFilterData.setStatus("mandatory")


class _RingswitchFilterExceptionType_Type(Integer32):
    """Custom type ringswitchFilterExceptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exception", 2),
          ("normal", 1))
    )


_RingswitchFilterExceptionType_Type.__name__ = "Integer32"
_RingswitchFilterExceptionType_Object = MibTableColumn
ringswitchFilterExceptionType = _RingswitchFilterExceptionType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 1, 1, 5),
    _RingswitchFilterExceptionType_Type()
)
ringswitchFilterExceptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFilterExceptionType.setStatus("mandatory")


class _RingswitchFilterType_Type(Integer32):
    """Custom type ringswitchFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("match-all", 2),
          ("normal", 1))
    )


_RingswitchFilterType_Type.__name__ = "Integer32"
_RingswitchFilterType_Object = MibTableColumn
ringswitchFilterType = _RingswitchFilterType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 1, 1, 6),
    _RingswitchFilterType_Type()
)
ringswitchFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFilterType.setStatus("mandatory")


class _RingswitchFilterForwardType_Type(Integer32):
    """Custom type ringswitchFilterForwardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sr-only", 1),
          ("sr-tb", 3),
          ("tb-only", 2))
    )


_RingswitchFilterForwardType_Type.__name__ = "Integer32"
_RingswitchFilterForwardType_Object = MibTableColumn
ringswitchFilterForwardType = _RingswitchFilterForwardType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 1, 1, 7),
    _RingswitchFilterForwardType_Type()
)
ringswitchFilterForwardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFilterForwardType.setStatus("mandatory")
_RingswitchFilterMatrixTable_Object = MibTable
ringswitchFilterMatrixTable = _RingswitchFilterMatrixTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 2)
)
if mibBuilder.loadTexts:
    ringswitchFilterMatrixTable.setStatus("mandatory")
_RingswitchFilterMatrixEntry_Object = MibTableRow
ringswitchFilterMatrixEntry = _RingswitchFilterMatrixEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 2, 1)
)
ringswitchFilterMatrixEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchFilterMatrixIndex"),
    (0, "MADGERSW-MIB", "ringswitchFilterMatrixRowIndex"),
)
if mibBuilder.loadTexts:
    ringswitchFilterMatrixEntry.setStatus("mandatory")
_RingswitchFilterMatrixIndex_Type = Integer32
_RingswitchFilterMatrixIndex_Object = MibTableColumn
ringswitchFilterMatrixIndex = _RingswitchFilterMatrixIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 2, 1, 1),
    _RingswitchFilterMatrixIndex_Type()
)
ringswitchFilterMatrixIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFilterMatrixIndex.setStatus("mandatory")
_RingswitchFilterMatrixRowIndex_Type = Integer32
_RingswitchFilterMatrixRowIndex_Object = MibTableColumn
ringswitchFilterMatrixRowIndex = _RingswitchFilterMatrixRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 2, 1, 2),
    _RingswitchFilterMatrixRowIndex_Type()
)
ringswitchFilterMatrixRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchFilterMatrixRowIndex.setStatus("mandatory")
_RingswitchFilterMatrixData_Type = OctetString
_RingswitchFilterMatrixData_Object = MibTableColumn
ringswitchFilterMatrixData = _RingswitchFilterMatrixData_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 15, 2, 1, 3),
    _RingswitchFilterMatrixData_Type()
)
ringswitchFilterMatrixData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchFilterMatrixData.setStatus("mandatory")
_RingswitchTLS_ObjectIdentity = ObjectIdentity
ringswitchTLS = _RingswitchTLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 16)
)
_RingswitchTLSCardTable_Object = MibTable
ringswitchTLSCardTable = _RingswitchTLSCardTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1)
)
if mibBuilder.loadTexts:
    ringswitchTLSCardTable.setStatus("mandatory")
_RingswitchTLSCardEntry_Object = MibTableRow
ringswitchTLSCardEntry = _RingswitchTLSCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1)
)
ringswitchTLSCardEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchTLSCardNum"),
)
if mibBuilder.loadTexts:
    ringswitchTLSCardEntry.setStatus("mandatory")


class _RingswitchTLSCardNum_Type(Integer32):
    """Custom type ringswitchTLSCardNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchTLSCardNum_Type.__name__ = "Integer32"
_RingswitchTLSCardNum_Object = MibTableColumn
ringswitchTLSCardNum = _RingswitchTLSCardNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 1),
    _RingswitchTLSCardNum_Type()
)
ringswitchTLSCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSCardNum.setStatus("mandatory")
_RingswitchTLSCardRowStatuses_Type = OctetString
_RingswitchTLSCardRowStatuses_Object = MibTableColumn
ringswitchTLSCardRowStatuses = _RingswitchTLSCardRowStatuses_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 2),
    _RingswitchTLSCardRowStatuses_Type()
)
ringswitchTLSCardRowStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSCardRowStatuses.setStatus("mandatory")


class _RingswitchTLSCardRIPTTL_Type(Integer32):
    """Custom type ringswitchTLSCardRIPTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RingswitchTLSCardRIPTTL_Type.__name__ = "Integer32"
_RingswitchTLSCardRIPTTL_Object = MibTableColumn
ringswitchTLSCardRIPTTL = _RingswitchTLSCardRIPTTL_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 3),
    _RingswitchTLSCardRIPTTL_Type()
)
ringswitchTLSCardRIPTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSCardRIPTTL.setStatus("mandatory")


class _RingswitchTLSCardRIPInterval_Type(Integer32):
    """Custom type ringswitchTLSCardRIPInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchTLSCardRIPInterval_Type.__name__ = "Integer32"
_RingswitchTLSCardRIPInterval_Object = MibTableColumn
ringswitchTLSCardRIPInterval = _RingswitchTLSCardRIPInterval_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 4),
    _RingswitchTLSCardRIPInterval_Type()
)
ringswitchTLSCardRIPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSCardRIPInterval.setStatus("mandatory")


class _RingswitchTLSCardRIPAging_Type(Integer32):
    """Custom type ringswitchTLSCardRIPAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchTLSCardRIPAging_Type.__name__ = "Integer32"
_RingswitchTLSCardRIPAging_Object = MibTableColumn
ringswitchTLSCardRIPAging = _RingswitchTLSCardRIPAging_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 5),
    _RingswitchTLSCardRIPAging_Type()
)
ringswitchTLSCardRIPAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSCardRIPAging.setStatus("mandatory")
_RingswitchTLSCardDefRoute_Type = IpAddress
_RingswitchTLSCardDefRoute_Object = MibTableColumn
ringswitchTLSCardDefRoute = _RingswitchTLSCardDefRoute_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 6),
    _RingswitchTLSCardDefRoute_Type()
)
ringswitchTLSCardDefRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSCardDefRoute.setStatus("mandatory")


class _RingswitchTLSCardDefRouteMetric_Type(Integer32):
    """Custom type ringswitchTLSCardDefRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RingswitchTLSCardDefRouteMetric_Type.__name__ = "Integer32"
_RingswitchTLSCardDefRouteMetric_Object = MibTableColumn
ringswitchTLSCardDefRouteMetric = _RingswitchTLSCardDefRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 7),
    _RingswitchTLSCardDefRouteMetric_Type()
)
ringswitchTLSCardDefRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSCardDefRouteMetric.setStatus("mandatory")


class _RingswitchTLSCardRIPFlags_Type(Integer32):
    """Custom type ringswitchTLSCardRIPFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RingswitchTLSCardRIPFlags_Type.__name__ = "Integer32"
_RingswitchTLSCardRIPFlags_Object = MibTableColumn
ringswitchTLSCardRIPFlags = _RingswitchTLSCardRIPFlags_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 8),
    _RingswitchTLSCardRIPFlags_Type()
)
ringswitchTLSCardRIPFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSCardRIPFlags.setStatus("mandatory")
_RingswitchTLSCardOSPFRouterId_Type = IpAddress
_RingswitchTLSCardOSPFRouterId_Object = MibTableColumn
ringswitchTLSCardOSPFRouterId = _RingswitchTLSCardOSPFRouterId_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 9),
    _RingswitchTLSCardOSPFRouterId_Type()
)
ringswitchTLSCardOSPFRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSCardOSPFRouterId.setStatus("mandatory")


class _RingswitchTLSCardOSPFFlags_Type(Integer32):
    """Custom type ringswitchTLSCardOSPFFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RingswitchTLSCardOSPFFlags_Type.__name__ = "Integer32"
_RingswitchTLSCardOSPFFlags_Object = MibTableColumn
ringswitchTLSCardOSPFFlags = _RingswitchTLSCardOSPFFlags_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 10),
    _RingswitchTLSCardOSPFFlags_Type()
)
ringswitchTLSCardOSPFFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSCardOSPFFlags.setStatus("mandatory")


class _RingswitchTLSCardStatsCpuUsage_Type(Integer32):
    """Custom type ringswitchTLSCardStatsCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RingswitchTLSCardStatsCpuUsage_Type.__name__ = "Integer32"
_RingswitchTLSCardStatsCpuUsage_Object = MibTableColumn
ringswitchTLSCardStatsCpuUsage = _RingswitchTLSCardStatsCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 11),
    _RingswitchTLSCardStatsCpuUsage_Type()
)
ringswitchTLSCardStatsCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSCardStatsCpuUsage.setStatus("mandatory")
_RingswitchTLSCardStatsFreeMem_Type = Integer32
_RingswitchTLSCardStatsFreeMem_Object = MibTableColumn
ringswitchTLSCardStatsFreeMem = _RingswitchTLSCardStatsFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 12),
    _RingswitchTLSCardStatsFreeMem_Type()
)
ringswitchTLSCardStatsFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSCardStatsFreeMem.setStatus("mandatory")
_RingswitchTLSCardStatsFramesFwd_Type = Integer32
_RingswitchTLSCardStatsFramesFwd_Object = MibTableColumn
ringswitchTLSCardStatsFramesFwd = _RingswitchTLSCardStatsFramesFwd_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 13),
    _RingswitchTLSCardStatsFramesFwd_Type()
)
ringswitchTLSCardStatsFramesFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSCardStatsFramesFwd.setStatus("mandatory")


class _RingswitchTLSCardStatsMaxCpuUsage_Type(Integer32):
    """Custom type ringswitchTLSCardStatsMaxCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RingswitchTLSCardStatsMaxCpuUsage_Type.__name__ = "Integer32"
_RingswitchTLSCardStatsMaxCpuUsage_Object = MibTableColumn
ringswitchTLSCardStatsMaxCpuUsage = _RingswitchTLSCardStatsMaxCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 14),
    _RingswitchTLSCardStatsMaxCpuUsage_Type()
)
ringswitchTLSCardStatsMaxCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSCardStatsMaxCpuUsage.setStatus("mandatory")
_RingswitchTLSCardStatsMinFreeMem_Type = Integer32
_RingswitchTLSCardStatsMinFreeMem_Object = MibTableColumn
ringswitchTLSCardStatsMinFreeMem = _RingswitchTLSCardStatsMinFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 15),
    _RingswitchTLSCardStatsMinFreeMem_Type()
)
ringswitchTLSCardStatsMinFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSCardStatsMinFreeMem.setStatus("mandatory")
_RingswitchTLSCardStatsMaxFramesFwd_Type = Integer32
_RingswitchTLSCardStatsMaxFramesFwd_Object = MibTableColumn
ringswitchTLSCardStatsMaxFramesFwd = _RingswitchTLSCardStatsMaxFramesFwd_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 16),
    _RingswitchTLSCardStatsMaxFramesFwd_Type()
)
ringswitchTLSCardStatsMaxFramesFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSCardStatsMaxFramesFwd.setStatus("mandatory")
_RingswitchTLSCardStatsResetState_Type = Integer32
_RingswitchTLSCardStatsResetState_Object = MibTableColumn
ringswitchTLSCardStatsResetState = _RingswitchTLSCardStatsResetState_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 17),
    _RingswitchTLSCardStatsResetState_Type()
)
ringswitchTLSCardStatsResetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSCardStatsResetState.setStatus("mandatory")
_RingswitchTLSCardARPFlush_Type = Integer32
_RingswitchTLSCardARPFlush_Object = MibTableColumn
ringswitchTLSCardARPFlush = _RingswitchTLSCardARPFlush_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 18),
    _RingswitchTLSCardARPFlush_Type()
)
ringswitchTLSCardARPFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSCardARPFlush.setStatus("mandatory")
_RingswitchTLSCardBootPRASecondsThreshold_Type = Integer32
_RingswitchTLSCardBootPRASecondsThreshold_Object = MibTableColumn
ringswitchTLSCardBootPRASecondsThreshold = _RingswitchTLSCardBootPRASecondsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 19),
    _RingswitchTLSCardBootPRASecondsThreshold_Type()
)
ringswitchTLSCardBootPRASecondsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSCardBootPRASecondsThreshold.setStatus("mandatory")


class _RingswitchTLSCardBootPRAHopsThreshold_Type(Integer32):
    """Custom type ringswitchTLSCardBootPRAHopsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RingswitchTLSCardBootPRAHopsThreshold_Type.__name__ = "Integer32"
_RingswitchTLSCardBootPRAHopsThreshold_Object = MibTableColumn
ringswitchTLSCardBootPRAHopsThreshold = _RingswitchTLSCardBootPRAHopsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 1, 1, 20),
    _RingswitchTLSCardBootPRAHopsThreshold_Type()
)
ringswitchTLSCardBootPRAHopsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSCardBootPRAHopsThreshold.setStatus("mandatory")
_RingswitchTLSPortTable_Object = MibTable
ringswitchTLSPortTable = _RingswitchTLSPortTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2)
)
if mibBuilder.loadTexts:
    ringswitchTLSPortTable.setStatus("mandatory")
_RingswitchTLSPortEntry_Object = MibTableRow
ringswitchTLSPortEntry = _RingswitchTLSPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1)
)
ringswitchTLSPortEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchTLSPortNum"),
)
if mibBuilder.loadTexts:
    ringswitchTLSPortEntry.setStatus("mandatory")


class _RingswitchTLSPortNum_Type(Integer32):
    """Custom type ringswitchTLSPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchTLSPortNum_Type.__name__ = "Integer32"
_RingswitchTLSPortNum_Object = MibTableColumn
ringswitchTLSPortNum = _RingswitchTLSPortNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 1),
    _RingswitchTLSPortNum_Type()
)
ringswitchTLSPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSPortNum.setStatus("mandatory")
_RingswitchTLSPortName_Type = DisplayString
_RingswitchTLSPortName_Object = MibTableColumn
ringswitchTLSPortName = _RingswitchTLSPortName_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 2),
    _RingswitchTLSPortName_Type()
)
ringswitchTLSPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortName.setStatus("mandatory")


class _RingswitchTLSPortMTU_Type(Integer32):
    """Custom type ringswitchTLSPortMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 18432),
    )


_RingswitchTLSPortMTU_Type.__name__ = "Integer32"
_RingswitchTLSPortMTU_Object = MibTableColumn
ringswitchTLSPortMTU = _RingswitchTLSPortMTU_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 3),
    _RingswitchTLSPortMTU_Type()
)
ringswitchTLSPortMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortMTU.setStatus("mandatory")


class _RingswitchTLSPortEnable_Type(Integer32):
    """Custom type ringswitchTLSPortEnable based on Integer32"""
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


_RingswitchTLSPortEnable_Type.__name__ = "Integer32"
_RingswitchTLSPortEnable_Object = MibTableColumn
ringswitchTLSPortEnable = _RingswitchTLSPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 4),
    _RingswitchTLSPortEnable_Type()
)
ringswitchTLSPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortEnable.setStatus("mandatory")
_RingswitchTLSPortIpAddress_Type = IpAddress
_RingswitchTLSPortIpAddress_Object = MibTableColumn
ringswitchTLSPortIpAddress = _RingswitchTLSPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 5),
    _RingswitchTLSPortIpAddress_Type()
)
ringswitchTLSPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortIpAddress.setStatus("mandatory")
_RingswitchTLSPortIpSubnetMask_Type = IpAddress
_RingswitchTLSPortIpSubnetMask_Object = MibTableColumn
ringswitchTLSPortIpSubnetMask = _RingswitchTLSPortIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 6),
    _RingswitchTLSPortIpSubnetMask_Type()
)
ringswitchTLSPortIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortIpSubnetMask.setStatus("mandatory")


class _RingswitchTLSPortRIPRxType_Type(Integer32):
    """Custom type ringswitchTLSPortRIPRxType based on Integer32"""
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
        *(("doNotReceive", 4),
          ("rip1", 1),
          ("rip1OrRip2", 3),
          ("rip2", 2))
    )


_RingswitchTLSPortRIPRxType_Type.__name__ = "Integer32"
_RingswitchTLSPortRIPRxType_Object = MibTableColumn
ringswitchTLSPortRIPRxType = _RingswitchTLSPortRIPRxType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 7),
    _RingswitchTLSPortRIPRxType_Type()
)
ringswitchTLSPortRIPRxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortRIPRxType.setStatus("mandatory")


class _RingswitchTLSPortRIPTxType_Type(Integer32):
    """Custom type ringswitchTLSPortRIPTxType based on Integer32"""
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
        *(("doNotSend", 1),
          ("rip1Compatible", 3),
          ("ripVersion1", 2),
          ("ripVersion2", 4))
    )


_RingswitchTLSPortRIPTxType_Type.__name__ = "Integer32"
_RingswitchTLSPortRIPTxType_Object = MibTableColumn
ringswitchTLSPortRIPTxType = _RingswitchTLSPortRIPTxType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 8),
    _RingswitchTLSPortRIPTxType_Type()
)
ringswitchTLSPortRIPTxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortRIPTxType.setStatus("mandatory")


class _RingswitchTLSPortRIPFlags_Type(Integer32):
    """Custom type ringswitchTLSPortRIPFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RingswitchTLSPortRIPFlags_Type.__name__ = "Integer32"
_RingswitchTLSPortRIPFlags_Object = MibTableColumn
ringswitchTLSPortRIPFlags = _RingswitchTLSPortRIPFlags_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 9),
    _RingswitchTLSPortRIPFlags_Type()
)
ringswitchTLSPortRIPFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortRIPFlags.setStatus("mandatory")
_RingswitchTLSPortIfArray_Type = OctetString
_RingswitchTLSPortIfArray_Object = MibTableColumn
ringswitchTLSPortIfArray = _RingswitchTLSPortIfArray_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 10),
    _RingswitchTLSPortIfArray_Type()
)
ringswitchTLSPortIfArray.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortIfArray.setStatus("mandatory")


class _RingswitchTLSPortRIP2AuthType_Type(Integer32):
    """Custom type ringswitchTLSPortRIP2AuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("noAuthentication", 1),
          ("simplePassword", 2))
    )


_RingswitchTLSPortRIP2AuthType_Type.__name__ = "Integer32"
_RingswitchTLSPortRIP2AuthType_Object = MibTableColumn
ringswitchTLSPortRIP2AuthType = _RingswitchTLSPortRIP2AuthType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 11),
    _RingswitchTLSPortRIP2AuthType_Type()
)
ringswitchTLSPortRIP2AuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortRIP2AuthType.setStatus("mandatory")


class _RingswitchTLSPortRIP2AuthKey_Type(OctetString):
    """Custom type ringswitchTLSPortRIP2AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RingswitchTLSPortRIP2AuthKey_Type.__name__ = "OctetString"
_RingswitchTLSPortRIP2AuthKey_Object = MibTableColumn
ringswitchTLSPortRIP2AuthKey = _RingswitchTLSPortRIP2AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 12),
    _RingswitchTLSPortRIP2AuthKey_Type()
)
ringswitchTLSPortRIP2AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortRIP2AuthKey.setStatus("mandatory")


class _RingswitchTLSPortOSPFEnable_Type(Integer32):
    """Custom type ringswitchTLSPortOSPFEnable based on Integer32"""
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


_RingswitchTLSPortOSPFEnable_Type.__name__ = "Integer32"
_RingswitchTLSPortOSPFEnable_Object = MibTableColumn
ringswitchTLSPortOSPFEnable = _RingswitchTLSPortOSPFEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 13),
    _RingswitchTLSPortOSPFEnable_Type()
)
ringswitchTLSPortOSPFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortOSPFEnable.setStatus("mandatory")
_RingswitchTLSPortOSPFAreaId_Type = IpAddress
_RingswitchTLSPortOSPFAreaId_Object = MibTableColumn
ringswitchTLSPortOSPFAreaId = _RingswitchTLSPortOSPFAreaId_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 14),
    _RingswitchTLSPortOSPFAreaId_Type()
)
ringswitchTLSPortOSPFAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortOSPFAreaId.setStatus("mandatory")


class _RingswitchTLSPortLegFlags_Type(Integer32):
    """Custom type ringswitchTLSPortLegFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RingswitchTLSPortLegFlags_Type.__name__ = "Integer32"
_RingswitchTLSPortLegFlags_Object = MibTableColumn
ringswitchTLSPortLegFlags = _RingswitchTLSPortLegFlags_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 15),
    _RingswitchTLSPortLegFlags_Type()
)
ringswitchTLSPortLegFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortLegFlags.setStatus("mandatory")


class _RingswitchTLSPortOSPFAuthType_Type(Integer32):
    """Custom type ringswitchTLSPortOSPFAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("noAuthentication", 1),
          ("simplePassword", 2))
    )


_RingswitchTLSPortOSPFAuthType_Type.__name__ = "Integer32"
_RingswitchTLSPortOSPFAuthType_Object = MibTableColumn
ringswitchTLSPortOSPFAuthType = _RingswitchTLSPortOSPFAuthType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 16),
    _RingswitchTLSPortOSPFAuthType_Type()
)
ringswitchTLSPortOSPFAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortOSPFAuthType.setStatus("mandatory")


class _RingswitchTLSPortOSPFAuthMD5KeyId_Type(Integer32):
    """Custom type ringswitchTLSPortOSPFAuthMD5KeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingswitchTLSPortOSPFAuthMD5KeyId_Type.__name__ = "Integer32"
_RingswitchTLSPortOSPFAuthMD5KeyId_Object = MibTableColumn
ringswitchTLSPortOSPFAuthMD5KeyId = _RingswitchTLSPortOSPFAuthMD5KeyId_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 17),
    _RingswitchTLSPortOSPFAuthMD5KeyId_Type()
)
ringswitchTLSPortOSPFAuthMD5KeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortOSPFAuthMD5KeyId.setStatus("mandatory")


class _RingswitchTLSPortOSPFAuthKey_Type(OctetString):
    """Custom type ringswitchTLSPortOSPFAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RingswitchTLSPortOSPFAuthKey_Type.__name__ = "OctetString"
_RingswitchTLSPortOSPFAuthKey_Object = MibTableColumn
ringswitchTLSPortOSPFAuthKey = _RingswitchTLSPortOSPFAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 18),
    _RingswitchTLSPortOSPFAuthKey_Type()
)
ringswitchTLSPortOSPFAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortOSPFAuthKey.setStatus("mandatory")


class _RingswitchTLSPortOSPFCost_Type(Integer32):
    """Custom type ringswitchTLSPortOSPFCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchTLSPortOSPFCost_Type.__name__ = "Integer32"
_RingswitchTLSPortOSPFCost_Object = MibTableColumn
ringswitchTLSPortOSPFCost = _RingswitchTLSPortOSPFCost_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 19),
    _RingswitchTLSPortOSPFCost_Type()
)
ringswitchTLSPortOSPFCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortOSPFCost.setStatus("mandatory")


class _RingswitchTLSPortOSPFPriority_Type(Integer32):
    """Custom type ringswitchTLSPortOSPFPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RingswitchTLSPortOSPFPriority_Type.__name__ = "Integer32"
_RingswitchTLSPortOSPFPriority_Object = MibTableColumn
ringswitchTLSPortOSPFPriority = _RingswitchTLSPortOSPFPriority_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 20),
    _RingswitchTLSPortOSPFPriority_Type()
)
ringswitchTLSPortOSPFPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortOSPFPriority.setStatus("mandatory")
_RingswitchTLSPortOSPFHelloInterval_Type = Integer32
_RingswitchTLSPortOSPFHelloInterval_Object = MibTableColumn
ringswitchTLSPortOSPFHelloInterval = _RingswitchTLSPortOSPFHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 21),
    _RingswitchTLSPortOSPFHelloInterval_Type()
)
ringswitchTLSPortOSPFHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortOSPFHelloInterval.setStatus("mandatory")
_RingswitchTLSPortOSPFDeadInterval_Type = Integer32
_RingswitchTLSPortOSPFDeadInterval_Object = MibTableColumn
ringswitchTLSPortOSPFDeadInterval = _RingswitchTLSPortOSPFDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 22),
    _RingswitchTLSPortOSPFDeadInterval_Type()
)
ringswitchTLSPortOSPFDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortOSPFDeadInterval.setStatus("mandatory")


class _RingswitchTLSPortBootPFlags_Type(Integer32):
    """Custom type ringswitchTLSPortBootPFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("relay-agent-disable", 0),
          ("relay-agent-enable", 1))
    )


_RingswitchTLSPortBootPFlags_Type.__name__ = "Integer32"
_RingswitchTLSPortBootPFlags_Object = MibTableColumn
ringswitchTLSPortBootPFlags = _RingswitchTLSPortBootPFlags_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 2, 1, 23),
    _RingswitchTLSPortBootPFlags_Type()
)
ringswitchTLSPortBootPFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSPortBootPFlags.setStatus("mandatory")
_RingswitchTLSStaticRouteTable_Object = MibTable
ringswitchTLSStaticRouteTable = _RingswitchTLSStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 3)
)
if mibBuilder.loadTexts:
    ringswitchTLSStaticRouteTable.setStatus("mandatory")
_RingswitchTLSStaticRouteEntry_Object = MibTableRow
ringswitchTLSStaticRouteEntry = _RingswitchTLSStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 3, 1)
)
ringswitchTLSStaticRouteEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchTLSStaticRouteCardNum"),
    (0, "MADGERSW-MIB", "ringswitchTLSStaticRouteIpAddress"),
)
if mibBuilder.loadTexts:
    ringswitchTLSStaticRouteEntry.setStatus("mandatory")
_RingswitchTLSStaticRouteCardNum_Type = Integer32
_RingswitchTLSStaticRouteCardNum_Object = MibTableColumn
ringswitchTLSStaticRouteCardNum = _RingswitchTLSStaticRouteCardNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 3, 1, 1),
    _RingswitchTLSStaticRouteCardNum_Type()
)
ringswitchTLSStaticRouteCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSStaticRouteCardNum.setStatus("mandatory")
_RingswitchTLSStaticRouteIpAddress_Type = IpAddress
_RingswitchTLSStaticRouteIpAddress_Object = MibTableColumn
ringswitchTLSStaticRouteIpAddress = _RingswitchTLSStaticRouteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 3, 1, 2),
    _RingswitchTLSStaticRouteIpAddress_Type()
)
ringswitchTLSStaticRouteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSStaticRouteIpAddress.setStatus("mandatory")
_RingswitchTLSStaticRouteMask_Type = IpAddress
_RingswitchTLSStaticRouteMask_Object = MibTableColumn
ringswitchTLSStaticRouteMask = _RingswitchTLSStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 3, 1, 3),
    _RingswitchTLSStaticRouteMask_Type()
)
ringswitchTLSStaticRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSStaticRouteMask.setStatus("mandatory")
_RingswitchTLSStaticRouteGateway_Type = IpAddress
_RingswitchTLSStaticRouteGateway_Object = MibTableColumn
ringswitchTLSStaticRouteGateway = _RingswitchTLSStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 3, 1, 4),
    _RingswitchTLSStaticRouteGateway_Type()
)
ringswitchTLSStaticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSStaticRouteGateway.setStatus("mandatory")


class _RingswitchTLSStaticRouteMetric_Type(Integer32):
    """Custom type ringswitchTLSStaticRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RingswitchTLSStaticRouteMetric_Type.__name__ = "Integer32"
_RingswitchTLSStaticRouteMetric_Object = MibTableColumn
ringswitchTLSStaticRouteMetric = _RingswitchTLSStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 3, 1, 5),
    _RingswitchTLSStaticRouteMetric_Type()
)
ringswitchTLSStaticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSStaticRouteMetric.setStatus("mandatory")
_RingswitchTLSRIPNeighbourTable_Object = MibTable
ringswitchTLSRIPNeighbourTable = _RingswitchTLSRIPNeighbourTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 4)
)
if mibBuilder.loadTexts:
    ringswitchTLSRIPNeighbourTable.setStatus("mandatory")
_RingswitchTLSRIPNeighbourEntry_Object = MibTableRow
ringswitchTLSRIPNeighbourEntry = _RingswitchTLSRIPNeighbourEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 4, 1)
)
ringswitchTLSRIPNeighbourEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchTLSRIPNeighbourCardNum"),
    (0, "MADGERSW-MIB", "ringswitchTLSRIPNeighbourIpAddress"),
)
if mibBuilder.loadTexts:
    ringswitchTLSRIPNeighbourEntry.setStatus("mandatory")
_RingswitchTLSRIPNeighbourCardNum_Type = Integer32
_RingswitchTLSRIPNeighbourCardNum_Object = MibTableColumn
ringswitchTLSRIPNeighbourCardNum = _RingswitchTLSRIPNeighbourCardNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 4, 1, 1),
    _RingswitchTLSRIPNeighbourCardNum_Type()
)
ringswitchTLSRIPNeighbourCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSRIPNeighbourCardNum.setStatus("mandatory")
_RingswitchTLSRIPNeighbourIpAddress_Type = IpAddress
_RingswitchTLSRIPNeighbourIpAddress_Object = MibTableColumn
ringswitchTLSRIPNeighbourIpAddress = _RingswitchTLSRIPNeighbourIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 4, 1, 2),
    _RingswitchTLSRIPNeighbourIpAddress_Type()
)
ringswitchTLSRIPNeighbourIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSRIPNeighbourIpAddress.setStatus("mandatory")


class _RingswitchTLSRIPNeighbourEnable_Type(Integer32):
    """Custom type ringswitchTLSRIPNeighbourEnable based on Integer32"""
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


_RingswitchTLSRIPNeighbourEnable_Type.__name__ = "Integer32"
_RingswitchTLSRIPNeighbourEnable_Object = MibTableColumn
ringswitchTLSRIPNeighbourEnable = _RingswitchTLSRIPNeighbourEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 4, 1, 3),
    _RingswitchTLSRIPNeighbourEnable_Type()
)
ringswitchTLSRIPNeighbourEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSRIPNeighbourEnable.setStatus("mandatory")
_RingswitchTLSRIPAdvertTable_Object = MibTable
ringswitchTLSRIPAdvertTable = _RingswitchTLSRIPAdvertTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 5)
)
if mibBuilder.loadTexts:
    ringswitchTLSRIPAdvertTable.setStatus("mandatory")
_RingswitchTLSRIPAdvertEntry_Object = MibTableRow
ringswitchTLSRIPAdvertEntry = _RingswitchTLSRIPAdvertEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 5, 1)
)
ringswitchTLSRIPAdvertEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchTLSRIPAdvertPortNum"),
    (0, "MADGERSW-MIB", "ringswitchTLSRIPAdvertIpAddress"),
)
if mibBuilder.loadTexts:
    ringswitchTLSRIPAdvertEntry.setStatus("mandatory")
_RingswitchTLSRIPAdvertPortNum_Type = Integer32
_RingswitchTLSRIPAdvertPortNum_Object = MibTableColumn
ringswitchTLSRIPAdvertPortNum = _RingswitchTLSRIPAdvertPortNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 5, 1, 1),
    _RingswitchTLSRIPAdvertPortNum_Type()
)
ringswitchTLSRIPAdvertPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSRIPAdvertPortNum.setStatus("mandatory")
_RingswitchTLSRIPAdvertIpAddress_Type = IpAddress
_RingswitchTLSRIPAdvertIpAddress_Object = MibTableColumn
ringswitchTLSRIPAdvertIpAddress = _RingswitchTLSRIPAdvertIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 5, 1, 2),
    _RingswitchTLSRIPAdvertIpAddress_Type()
)
ringswitchTLSRIPAdvertIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSRIPAdvertIpAddress.setStatus("mandatory")


class _RingswitchTLSRIPAdvertEnable_Type(Integer32):
    """Custom type ringswitchTLSRIPAdvertEnable based on Integer32"""
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


_RingswitchTLSRIPAdvertEnable_Type.__name__ = "Integer32"
_RingswitchTLSRIPAdvertEnable_Object = MibTableColumn
ringswitchTLSRIPAdvertEnable = _RingswitchTLSRIPAdvertEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 5, 1, 3),
    _RingswitchTLSRIPAdvertEnable_Type()
)
ringswitchTLSRIPAdvertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSRIPAdvertEnable.setStatus("mandatory")
_RingswitchTLSRIPRejectTable_Object = MibTable
ringswitchTLSRIPRejectTable = _RingswitchTLSRIPRejectTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 6)
)
if mibBuilder.loadTexts:
    ringswitchTLSRIPRejectTable.setStatus("mandatory")
_RingswitchTLSRIPRejectEntry_Object = MibTableRow
ringswitchTLSRIPRejectEntry = _RingswitchTLSRIPRejectEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 6, 1)
)
ringswitchTLSRIPRejectEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchTLSRIPRejectPortNum"),
    (0, "MADGERSW-MIB", "ringswitchTLSRIPRejectIpAddress"),
)
if mibBuilder.loadTexts:
    ringswitchTLSRIPRejectEntry.setStatus("mandatory")
_RingswitchTLSRIPRejectPortNum_Type = Integer32
_RingswitchTLSRIPRejectPortNum_Object = MibTableColumn
ringswitchTLSRIPRejectPortNum = _RingswitchTLSRIPRejectPortNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 6, 1, 1),
    _RingswitchTLSRIPRejectPortNum_Type()
)
ringswitchTLSRIPRejectPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSRIPRejectPortNum.setStatus("mandatory")
_RingswitchTLSRIPRejectIpAddress_Type = IpAddress
_RingswitchTLSRIPRejectIpAddress_Object = MibTableColumn
ringswitchTLSRIPRejectIpAddress = _RingswitchTLSRIPRejectIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 6, 1, 2),
    _RingswitchTLSRIPRejectIpAddress_Type()
)
ringswitchTLSRIPRejectIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSRIPRejectIpAddress.setStatus("mandatory")


class _RingswitchTLSRIPRejectEnable_Type(Integer32):
    """Custom type ringswitchTLSRIPRejectEnable based on Integer32"""
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


_RingswitchTLSRIPRejectEnable_Type.__name__ = "Integer32"
_RingswitchTLSRIPRejectEnable_Object = MibTableColumn
ringswitchTLSRIPRejectEnable = _RingswitchTLSRIPRejectEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 6, 1, 3),
    _RingswitchTLSRIPRejectEnable_Type()
)
ringswitchTLSRIPRejectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSRIPRejectEnable.setStatus("mandatory")
_RingswitchTLSOSPFAreaTable_Object = MibTable
ringswitchTLSOSPFAreaTable = _RingswitchTLSOSPFAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 7)
)
if mibBuilder.loadTexts:
    ringswitchTLSOSPFAreaTable.setStatus("mandatory")
_RingswitchTLSOSPFAreaEntry_Object = MibTableRow
ringswitchTLSOSPFAreaEntry = _RingswitchTLSOSPFAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 7, 1)
)
ringswitchTLSOSPFAreaEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchTLSOSPFAreaId"),
)
if mibBuilder.loadTexts:
    ringswitchTLSOSPFAreaEntry.setStatus("mandatory")
_RingswitchTLSOSPFAreaCardNum_Type = Integer32
_RingswitchTLSOSPFAreaCardNum_Object = MibTableColumn
ringswitchTLSOSPFAreaCardNum = _RingswitchTLSOSPFAreaCardNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 7, 1, 1),
    _RingswitchTLSOSPFAreaCardNum_Type()
)
ringswitchTLSOSPFAreaCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSOSPFAreaCardNum.setStatus("mandatory")
_RingswitchTLSOSPFAreaId_Type = IpAddress
_RingswitchTLSOSPFAreaId_Object = MibTableColumn
ringswitchTLSOSPFAreaId = _RingswitchTLSOSPFAreaId_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 7, 1, 2),
    _RingswitchTLSOSPFAreaId_Type()
)
ringswitchTLSOSPFAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSOSPFAreaId.setStatus("mandatory")
_RingswitchTLSOSPFAreaAddress_Type = IpAddress
_RingswitchTLSOSPFAreaAddress_Object = MibTableColumn
ringswitchTLSOSPFAreaAddress = _RingswitchTLSOSPFAreaAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 7, 1, 3),
    _RingswitchTLSOSPFAreaAddress_Type()
)
ringswitchTLSOSPFAreaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSOSPFAreaAddress.setStatus("mandatory")
_RingswitchTLSOSPFAreaAddressMask_Type = IpAddress
_RingswitchTLSOSPFAreaAddressMask_Object = MibTableColumn
ringswitchTLSOSPFAreaAddressMask = _RingswitchTLSOSPFAreaAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 7, 1, 4),
    _RingswitchTLSOSPFAreaAddressMask_Type()
)
ringswitchTLSOSPFAreaAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSOSPFAreaAddressMask.setStatus("mandatory")


class _RingswitchTLSOSPFAreaFlags_Type(Integer32):
    """Custom type ringswitchTLSOSPFAreaFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_RingswitchTLSOSPFAreaFlags_Type.__name__ = "Integer32"
_RingswitchTLSOSPFAreaFlags_Object = MibTableColumn
ringswitchTLSOSPFAreaFlags = _RingswitchTLSOSPFAreaFlags_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 7, 1, 5),
    _RingswitchTLSOSPFAreaFlags_Type()
)
ringswitchTLSOSPFAreaFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSOSPFAreaFlags.setStatus("mandatory")
_RingswitchTLSBootPRAServerTable_Object = MibTable
ringswitchTLSBootPRAServerTable = _RingswitchTLSBootPRAServerTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 8)
)
if mibBuilder.loadTexts:
    ringswitchTLSBootPRAServerTable.setStatus("mandatory")
_RingswitchTLSBootPRAServerEntry_Object = MibTableRow
ringswitchTLSBootPRAServerEntry = _RingswitchTLSBootPRAServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 8, 1)
)
ringswitchTLSBootPRAServerEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchTLSBootPRAServerCardNum"),
    (0, "MADGERSW-MIB", "ringswitchTLSBootPRAServerIpAddress"),
)
if mibBuilder.loadTexts:
    ringswitchTLSBootPRAServerEntry.setStatus("mandatory")
_RingswitchTLSBootPRAServerCardNum_Type = Integer32
_RingswitchTLSBootPRAServerCardNum_Object = MibTableColumn
ringswitchTLSBootPRAServerCardNum = _RingswitchTLSBootPRAServerCardNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 8, 1, 1),
    _RingswitchTLSBootPRAServerCardNum_Type()
)
ringswitchTLSBootPRAServerCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSBootPRAServerCardNum.setStatus("mandatory")
_RingswitchTLSBootPRAServerIpAddress_Type = IpAddress
_RingswitchTLSBootPRAServerIpAddress_Object = MibTableColumn
ringswitchTLSBootPRAServerIpAddress = _RingswitchTLSBootPRAServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 8, 1, 2),
    _RingswitchTLSBootPRAServerIpAddress_Type()
)
ringswitchTLSBootPRAServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSBootPRAServerIpAddress.setStatus("mandatory")


class _RingswitchTLSBootPRAServerName_Type(OctetString):
    """Custom type ringswitchTLSBootPRAServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_RingswitchTLSBootPRAServerName_Type.__name__ = "OctetString"
_RingswitchTLSBootPRAServerName_Object = MibTableColumn
ringswitchTLSBootPRAServerName = _RingswitchTLSBootPRAServerName_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 8, 1, 3),
    _RingswitchTLSBootPRAServerName_Type()
)
ringswitchTLSBootPRAServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSBootPRAServerName.setStatus("mandatory")


class _RingswitchTLSBootPRAServerEnable_Type(Integer32):
    """Custom type ringswitchTLSBootPRAServerEnable based on Integer32"""
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


_RingswitchTLSBootPRAServerEnable_Type.__name__ = "Integer32"
_RingswitchTLSBootPRAServerEnable_Object = MibTableColumn
ringswitchTLSBootPRAServerEnable = _RingswitchTLSBootPRAServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 8, 1, 4),
    _RingswitchTLSBootPRAServerEnable_Type()
)
ringswitchTLSBootPRAServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSBootPRAServerEnable.setStatus("mandatory")
_RingswitchTLSVRRPVRTRTable_Object = MibTable
ringswitchTLSVRRPVRTRTable = _RingswitchTLSVRRPVRTRTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 9)
)
if mibBuilder.loadTexts:
    ringswitchTLSVRRPVRTRTable.setStatus("mandatory")
_RingswitchTLSVRRPVRTREntry_Object = MibTableRow
ringswitchTLSVRRPVRTREntry = _RingswitchTLSVRRPVRTREntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 9, 1)
)
ringswitchTLSVRRPVRTREntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchTLSVRRPVRTRPortNum"),
    (0, "MADGERSW-MIB", "ringswitchTLSVRRPVRTRIpAddress"),
)
if mibBuilder.loadTexts:
    ringswitchTLSVRRPVRTREntry.setStatus("mandatory")
_RingswitchTLSVRRPVRTRPortNum_Type = Integer32
_RingswitchTLSVRRPVRTRPortNum_Object = MibTableColumn
ringswitchTLSVRRPVRTRPortNum = _RingswitchTLSVRRPVRTRPortNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 9, 1, 1),
    _RingswitchTLSVRRPVRTRPortNum_Type()
)
ringswitchTLSVRRPVRTRPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSVRRPVRTRPortNum.setStatus("mandatory")
_RingswitchTLSVRRPVRTRIpAddress_Type = IpAddress
_RingswitchTLSVRRPVRTRIpAddress_Object = MibTableColumn
ringswitchTLSVRRPVRTRIpAddress = _RingswitchTLSVRRPVRTRIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 9, 1, 2),
    _RingswitchTLSVRRPVRTRIpAddress_Type()
)
ringswitchTLSVRRPVRTRIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchTLSVRRPVRTRIpAddress.setStatus("mandatory")


class _RingswitchTLSVRRPVRTRVRID_Type(Integer32):
    """Custom type ringswitchTLSVRRPVRTRVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RingswitchTLSVRRPVRTRVRID_Type.__name__ = "Integer32"
_RingswitchTLSVRRPVRTRVRID_Object = MibTableColumn
ringswitchTLSVRRPVRTRVRID = _RingswitchTLSVRRPVRTRVRID_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 9, 1, 3),
    _RingswitchTLSVRRPVRTRVRID_Type()
)
ringswitchTLSVRRPVRTRVRID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSVRRPVRTRVRID.setStatus("mandatory")
_RingswitchTLSVRRPVRTRMacAddress_Type = TRNMacAddress
_RingswitchTLSVRRPVRTRMacAddress_Object = MibTableColumn
ringswitchTLSVRRPVRTRMacAddress = _RingswitchTLSVRRPVRTRMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 9, 1, 4),
    _RingswitchTLSVRRPVRTRMacAddress_Type()
)
ringswitchTLSVRRPVRTRMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSVRRPVRTRMacAddress.setStatus("mandatory")


class _RingswitchTLSVRRPVRTREnable_Type(Integer32):
    """Custom type ringswitchTLSVRRPVRTREnable based on Integer32"""
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


_RingswitchTLSVRRPVRTREnable_Type.__name__ = "Integer32"
_RingswitchTLSVRRPVRTREnable_Object = MibTableColumn
ringswitchTLSVRRPVRTREnable = _RingswitchTLSVRRPVRTREnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 9, 1, 5),
    _RingswitchTLSVRRPVRTREnable_Type()
)
ringswitchTLSVRRPVRTREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSVRRPVRTREnable.setStatus("mandatory")
_RingswitchTLSVRRPVRTRAdvertInterval_Type = Integer32
_RingswitchTLSVRRPVRTRAdvertInterval_Object = MibTableColumn
ringswitchTLSVRRPVRTRAdvertInterval = _RingswitchTLSVRRPVRTRAdvertInterval_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 9, 1, 6),
    _RingswitchTLSVRRPVRTRAdvertInterval_Type()
)
ringswitchTLSVRRPVRTRAdvertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSVRRPVRTRAdvertInterval.setStatus("mandatory")


class _RingswitchTLSVRRPVRTRPriority_Type(Integer32):
    """Custom type ringswitchTLSVRRPVRTRPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingswitchTLSVRRPVRTRPriority_Type.__name__ = "Integer32"
_RingswitchTLSVRRPVRTRPriority_Object = MibTableColumn
ringswitchTLSVRRPVRTRPriority = _RingswitchTLSVRRPVRTRPriority_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 9, 1, 7),
    _RingswitchTLSVRRPVRTRPriority_Type()
)
ringswitchTLSVRRPVRTRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSVRRPVRTRPriority.setStatus("mandatory")


class _RingswitchTLSVRRPVRTRAuthType_Type(Integer32):
    """Custom type ringswitchTLSVRRPVRTRAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("simple", 2))
    )


_RingswitchTLSVRRPVRTRAuthType_Type.__name__ = "Integer32"
_RingswitchTLSVRRPVRTRAuthType_Object = MibTableColumn
ringswitchTLSVRRPVRTRAuthType = _RingswitchTLSVRRPVRTRAuthType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 9, 1, 8),
    _RingswitchTLSVRRPVRTRAuthType_Type()
)
ringswitchTLSVRRPVRTRAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSVRRPVRTRAuthType.setStatus("mandatory")


class _RingswitchTLSVRRPVRTRAuthKey_Type(OctetString):
    """Custom type ringswitchTLSVRRPVRTRAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RingswitchTLSVRRPVRTRAuthKey_Type.__name__ = "OctetString"
_RingswitchTLSVRRPVRTRAuthKey_Object = MibTableColumn
ringswitchTLSVRRPVRTRAuthKey = _RingswitchTLSVRRPVRTRAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 9, 1, 9),
    _RingswitchTLSVRRPVRTRAuthKey_Type()
)
ringswitchTLSVRRPVRTRAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSVRRPVRTRAuthKey.setStatus("mandatory")
_RingswitchTLSVRRPVRTRAdvertDeadInterval_Type = Integer32
_RingswitchTLSVRRPVRTRAdvertDeadInterval_Object = MibTableColumn
ringswitchTLSVRRPVRTRAdvertDeadInterval = _RingswitchTLSVRRPVRTRAdvertDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 16, 9, 1, 10),
    _RingswitchTLSVRRPVRTRAdvertDeadInterval_Type()
)
ringswitchTLSVRRPVRTRAdvertDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchTLSVRRPVRTRAdvertDeadInterval.setStatus("mandatory")
_RingswitchEthernet_ObjectIdentity = ObjectIdentity
ringswitchEthernet = _RingswitchEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 4, 21)
)
_RingswitchEthernetIfTable_Object = MibTable
ringswitchEthernetIfTable = _RingswitchEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1)
)
if mibBuilder.loadTexts:
    ringswitchEthernetIfTable.setStatus("mandatory")
_RingswitchEthernetIfEntry_Object = MibTableRow
ringswitchEthernetIfEntry = _RingswitchEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1)
)
ringswitchEthernetIfEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchEthernetIfIndex"),
)
if mibBuilder.loadTexts:
    ringswitchEthernetIfEntry.setStatus("mandatory")


class _RingswitchEthernetIfIndex_Type(Integer32):
    """Custom type ringswitchEthernetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RingswitchEthernetIfIndex_Type.__name__ = "Integer32"
_RingswitchEthernetIfIndex_Object = MibTableColumn
ringswitchEthernetIfIndex = _RingswitchEthernetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 1),
    _RingswitchEthernetIfIndex_Type()
)
ringswitchEthernetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetIfIndex.setStatus("mandatory")


class _RingswitchEthernetIfIPXEthType_Type(Integer32):
    """Custom type ringswitchEthernetIfIPXEthType based on Integer32"""
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
        *(("auto", 1),
          ("dix", 5),
          ("ieee8022", 2),
          ("ieee8023", 4),
          ("snap", 3))
    )


_RingswitchEthernetIfIPXEthType_Type.__name__ = "Integer32"
_RingswitchEthernetIfIPXEthType_Object = MibTableColumn
ringswitchEthernetIfIPXEthType = _RingswitchEthernetIfIPXEthType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 2),
    _RingswitchEthernetIfIPXEthType_Type()
)
ringswitchEthernetIfIPXEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfIPXEthType.setStatus("mandatory")


class _RingswitchEthernetIfOperIPXEthType_Type(Integer32):
    """Custom type ringswitchEthernetIfOperIPXEthType based on Integer32"""
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
        *(("dix", 5),
          ("ieee8022", 2),
          ("ieee8023", 4),
          ("snap", 3),
          ("unknown", 1))
    )


_RingswitchEthernetIfOperIPXEthType_Type.__name__ = "Integer32"
_RingswitchEthernetIfOperIPXEthType_Object = MibTableColumn
ringswitchEthernetIfOperIPXEthType = _RingswitchEthernetIfOperIPXEthType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 3),
    _RingswitchEthernetIfOperIPXEthType_Type()
)
ringswitchEthernetIfOperIPXEthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetIfOperIPXEthType.setStatus("mandatory")


class _RingswitchEthernetIfIPXTRType_Type(Integer32):
    """Custom type ringswitchEthernetIfIPXTRType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("ieee8022", 2),
          ("snap", 3))
    )


_RingswitchEthernetIfIPXTRType_Type.__name__ = "Integer32"
_RingswitchEthernetIfIPXTRType_Object = MibTableColumn
ringswitchEthernetIfIPXTRType = _RingswitchEthernetIfIPXTRType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 4),
    _RingswitchEthernetIfIPXTRType_Type()
)
ringswitchEthernetIfIPXTRType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfIPXTRType.setStatus("mandatory")


class _RingswitchEthernetIfOperIPXTRType_Type(Integer32):
    """Custom type ringswitchEthernetIfOperIPXTRType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8022", 2),
          ("snap", 3),
          ("unknown", 1))
    )


_RingswitchEthernetIfOperIPXTRType_Type.__name__ = "Integer32"
_RingswitchEthernetIfOperIPXTRType_Object = MibTableColumn
ringswitchEthernetIfOperIPXTRType = _RingswitchEthernetIfOperIPXTRType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 5),
    _RingswitchEthernetIfOperIPXTRType_Type()
)
ringswitchEthernetIfOperIPXTRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetIfOperIPXTRType.setStatus("mandatory")


class _RingswitchEthernetIfIPXEnable_Type(Integer32):
    """Custom type ringswitchEthernetIfIPXEnable based on Integer32"""
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


_RingswitchEthernetIfIPXEnable_Type.__name__ = "Integer32"
_RingswitchEthernetIfIPXEnable_Object = MibTableColumn
ringswitchEthernetIfIPXEnable = _RingswitchEthernetIfIPXEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 6),
    _RingswitchEthernetIfIPXEnable_Type()
)
ringswitchEthernetIfIPXEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfIPXEnable.setStatus("mandatory")


class _RingswitchEthernetIfIPEnable_Type(Integer32):
    """Custom type ringswitchEthernetIfIPEnable based on Integer32"""
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


_RingswitchEthernetIfIPEnable_Type.__name__ = "Integer32"
_RingswitchEthernetIfIPEnable_Object = MibTableColumn
ringswitchEthernetIfIPEnable = _RingswitchEthernetIfIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 7),
    _RingswitchEthernetIfIPEnable_Type()
)
ringswitchEthernetIfIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfIPEnable.setStatus("mandatory")


class _RingswitchEthernetIfAdminSpeed_Type(Integer32):
    """Custom type ringswitchEthernetIfAdminSpeed based on Integer32"""
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
        *(("auto", 1),
          ("speed1000Mbps", 4),
          ("speed100Mbps", 3),
          ("speed10Mbps", 2))
    )


_RingswitchEthernetIfAdminSpeed_Type.__name__ = "Integer32"
_RingswitchEthernetIfAdminSpeed_Object = MibTableColumn
ringswitchEthernetIfAdminSpeed = _RingswitchEthernetIfAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 8),
    _RingswitchEthernetIfAdminSpeed_Type()
)
ringswitchEthernetIfAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfAdminSpeed.setStatus("mandatory")


class _RingswitchEthernetIfOperSpeed_Type(Integer32):
    """Custom type ringswitchEthernetIfOperSpeed based on Integer32"""
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
        *(("hundred", 3),
          ("ten", 2),
          ("thousand", 4),
          ("unknown", 1))
    )


_RingswitchEthernetIfOperSpeed_Type.__name__ = "Integer32"
_RingswitchEthernetIfOperSpeed_Object = MibTableColumn
ringswitchEthernetIfOperSpeed = _RingswitchEthernetIfOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 9),
    _RingswitchEthernetIfOperSpeed_Type()
)
ringswitchEthernetIfOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetIfOperSpeed.setStatus("mandatory")


class _RingswitchEthernetIfAdminDuplexMode_Type(Integer32):
    """Custom type ringswitchEthernetIfAdminDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("full", 3),
          ("half", 2))
    )


_RingswitchEthernetIfAdminDuplexMode_Type.__name__ = "Integer32"
_RingswitchEthernetIfAdminDuplexMode_Object = MibTableColumn
ringswitchEthernetIfAdminDuplexMode = _RingswitchEthernetIfAdminDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 10),
    _RingswitchEthernetIfAdminDuplexMode_Type()
)
ringswitchEthernetIfAdminDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfAdminDuplexMode.setStatus("mandatory")


class _RingswitchEthernetIfOperDuplexMode_Type(Integer32):
    """Custom type ringswitchEthernetIfOperDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 3),
          ("half-duplex", 2),
          ("unknown", 1))
    )


_RingswitchEthernetIfOperDuplexMode_Type.__name__ = "Integer32"
_RingswitchEthernetIfOperDuplexMode_Object = MibTableColumn
ringswitchEthernetIfOperDuplexMode = _RingswitchEthernetIfOperDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 11),
    _RingswitchEthernetIfOperDuplexMode_Type()
)
ringswitchEthernetIfOperDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetIfOperDuplexMode.setStatus("mandatory")


class _RingswitchEthernetIfIPMulticastType_Type(Integer32):
    """Custom type ringswitchEthernetIfIPMulticastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("functional", 2),
          ("group", 3))
    )


_RingswitchEthernetIfIPMulticastType_Type.__name__ = "Integer32"
_RingswitchEthernetIfIPMulticastType_Object = MibTableColumn
ringswitchEthernetIfIPMulticastType = _RingswitchEthernetIfIPMulticastType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 12),
    _RingswitchEthernetIfIPMulticastType_Type()
)
ringswitchEthernetIfIPMulticastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfIPMulticastType.setStatus("mandatory")


class _RingswitchEthernetIfCacheClear_Type(Integer32):
    """Custom type ringswitchEthernetIfCacheClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_RingswitchEthernetIfCacheClear_Type.__name__ = "Integer32"
_RingswitchEthernetIfCacheClear_Object = MibTableColumn
ringswitchEthernetIfCacheClear = _RingswitchEthernetIfCacheClear_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 13),
    _RingswitchEthernetIfCacheClear_Type()
)
ringswitchEthernetIfCacheClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ringswitchEthernetIfCacheClear.setStatus("mandatory")


class _RingswitchEthernetIfSPTEncaps_Type(Integer32):
    """Custom type ringswitchEthernetIfSPTEncaps based on Integer32"""
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


_RingswitchEthernetIfSPTEncaps_Type.__name__ = "Integer32"
_RingswitchEthernetIfSPTEncaps_Object = MibTableColumn
ringswitchEthernetIfSPTEncaps = _RingswitchEthernetIfSPTEncaps_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 14),
    _RingswitchEthernetIfSPTEncaps_Type()
)
ringswitchEthernetIfSPTEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfSPTEncaps.setStatus("mandatory")


class _RingswitchEthernetIfPriorityTagging_Type(Integer32):
    """Custom type ringswitchEthernetIfPriorityTagging based on Integer32"""
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


_RingswitchEthernetIfPriorityTagging_Type.__name__ = "Integer32"
_RingswitchEthernetIfPriorityTagging_Object = MibTableColumn
ringswitchEthernetIfPriorityTagging = _RingswitchEthernetIfPriorityTagging_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 15),
    _RingswitchEthernetIfPriorityTagging_Type()
)
ringswitchEthernetIfPriorityTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfPriorityTagging.setStatus("mandatory")


class _RingswitchEthernetIfPriorityTaggingVLANId_Type(Integer32):
    """Custom type ringswitchEthernetIfPriorityTaggingVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RingswitchEthernetIfPriorityTaggingVLANId_Type.__name__ = "Integer32"
_RingswitchEthernetIfPriorityTaggingVLANId_Object = MibTableColumn
ringswitchEthernetIfPriorityTaggingVLANId = _RingswitchEthernetIfPriorityTaggingVLANId_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 16),
    _RingswitchEthernetIfPriorityTaggingVLANId_Type()
)
ringswitchEthernetIfPriorityTaggingVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfPriorityTaggingVLANId.setStatus("mandatory")
_RingswitchEthernetIfAdminIPXNetwork_Type = Integer32
_RingswitchEthernetIfAdminIPXNetwork_Object = MibTableColumn
ringswitchEthernetIfAdminIPXNetwork = _RingswitchEthernetIfAdminIPXNetwork_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 17),
    _RingswitchEthernetIfAdminIPXNetwork_Type()
)
ringswitchEthernetIfAdminIPXNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfAdminIPXNetwork.setStatus("mandatory")
_RingswitchEthernetIfOperIPXNetwork_Type = Integer32
_RingswitchEthernetIfOperIPXNetwork_Object = MibTableColumn
ringswitchEthernetIfOperIPXNetwork = _RingswitchEthernetIfOperIPXNetwork_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 18),
    _RingswitchEthernetIfOperIPXNetwork_Type()
)
ringswitchEthernetIfOperIPXNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetIfOperIPXNetwork.setStatus("mandatory")


class _RingswitchEthernetIfSTPBlockingTrapInfo_Type(Integer32):
    """Custom type ringswitchEthernetIfSTPBlockingTrapInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("unblocked", 2))
    )


_RingswitchEthernetIfSTPBlockingTrapInfo_Type.__name__ = "Integer32"
_RingswitchEthernetIfSTPBlockingTrapInfo_Object = MibTableColumn
ringswitchEthernetIfSTPBlockingTrapInfo = _RingswitchEthernetIfSTPBlockingTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 19),
    _RingswitchEthernetIfSTPBlockingTrapInfo_Type()
)
ringswitchEthernetIfSTPBlockingTrapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetIfSTPBlockingTrapInfo.setStatus("mandatory")


class _RingswitchEthernetIfAdminFlowCtrl_Type(Integer32):
    """Custom type ringswitchEthernetIfAdminFlowCtrl based on Integer32"""
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
        *(("no-pause", 2),
          ("not-applicable", 1),
          ("rx-pause", 4),
          ("tx-pause", 3),
          ("tx-rx-pause", 5))
    )


_RingswitchEthernetIfAdminFlowCtrl_Type.__name__ = "Integer32"
_RingswitchEthernetIfAdminFlowCtrl_Object = MibTableColumn
ringswitchEthernetIfAdminFlowCtrl = _RingswitchEthernetIfAdminFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 20),
    _RingswitchEthernetIfAdminFlowCtrl_Type()
)
ringswitchEthernetIfAdminFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfAdminFlowCtrl.setStatus("mandatory")


class _RingswitchEthernetIfOperFlowCtrl_Type(Integer32):
    """Custom type ringswitchEthernetIfOperFlowCtrl based on Integer32"""
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
        *(("no-pause", 2),
          ("rx-pause", 4),
          ("tx-pause", 3),
          ("tx-rx-pause", 5),
          ("unknown", 1))
    )


_RingswitchEthernetIfOperFlowCtrl_Type.__name__ = "Integer32"
_RingswitchEthernetIfOperFlowCtrl_Object = MibTableColumn
ringswitchEthernetIfOperFlowCtrl = _RingswitchEthernetIfOperFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 21),
    _RingswitchEthernetIfOperFlowCtrl_Type()
)
ringswitchEthernetIfOperFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetIfOperFlowCtrl.setStatus("mandatory")


class _RingswitchEthernetIfAutoNegotiate_Type(Integer32):
    """Custom type ringswitchEthernetIfAutoNegotiate based on Integer32"""
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
          ("enabled", 1),
          ("not-applicable", 3))
    )


_RingswitchEthernetIfAutoNegotiate_Type.__name__ = "Integer32"
_RingswitchEthernetIfAutoNegotiate_Object = MibTableColumn
ringswitchEthernetIfAutoNegotiate = _RingswitchEthernetIfAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 22),
    _RingswitchEthernetIfAutoNegotiate_Type()
)
ringswitchEthernetIfAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfAutoNegotiate.setStatus("mandatory")


class _RingswitchEthernetIfMediaType_Type(Integer32):
    """Custom type ringswitchEthernetIfMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fibre-lx", 3),
          ("fibre-sx", 2))
    )


_RingswitchEthernetIfMediaType_Type.__name__ = "Integer32"
_RingswitchEthernetIfMediaType_Object = MibTableColumn
ringswitchEthernetIfMediaType = _RingswitchEthernetIfMediaType_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 23),
    _RingswitchEthernetIfMediaType_Type()
)
ringswitchEthernetIfMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetIfMediaType.setStatus("mandatory")
_RingswitchEthernetIfAdminMaxFrameSize_Type = Integer32
_RingswitchEthernetIfAdminMaxFrameSize_Object = MibTableColumn
ringswitchEthernetIfAdminMaxFrameSize = _RingswitchEthernetIfAdminMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 24),
    _RingswitchEthernetIfAdminMaxFrameSize_Type()
)
ringswitchEthernetIfAdminMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfAdminMaxFrameSize.setStatus("mandatory")
_RingswitchEthernetIfOperMaxFrameSize_Type = Integer32
_RingswitchEthernetIfOperMaxFrameSize_Object = MibTableColumn
ringswitchEthernetIfOperMaxFrameSize = _RingswitchEthernetIfOperMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 1, 1, 25),
    _RingswitchEthernetIfOperMaxFrameSize_Type()
)
ringswitchEthernetIfOperMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetIfOperMaxFrameSize.setStatus("mandatory")
_RingswitchEthernetXBDupAddrTable_Object = MibTable
ringswitchEthernetXBDupAddrTable = _RingswitchEthernetXBDupAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 2)
)
if mibBuilder.loadTexts:
    ringswitchEthernetXBDupAddrTable.setStatus("mandatory")
_RingswitchEthernetXBDupAddrEntry_Object = MibTableRow
ringswitchEthernetXBDupAddrEntry = _RingswitchEthernetXBDupAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 2, 1)
)
ringswitchEthernetXBDupAddrEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchEthernetXBDupAddrIfIndex"),
    (0, "MADGERSW-MIB", "ringswitchEthernetXBDupAddrIndex"),
)
if mibBuilder.loadTexts:
    ringswitchEthernetXBDupAddrEntry.setStatus("mandatory")
_RingswitchEthernetXBDupAddrIfIndex_Type = Integer32
_RingswitchEthernetXBDupAddrIfIndex_Object = MibTableColumn
ringswitchEthernetXBDupAddrIfIndex = _RingswitchEthernetXBDupAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 2, 1, 1),
    _RingswitchEthernetXBDupAddrIfIndex_Type()
)
ringswitchEthernetXBDupAddrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBDupAddrIfIndex.setStatus("mandatory")


class _RingswitchEthernetXBDupAddrIndex_Type(Integer32):
    """Custom type ringswitchEthernetXBDupAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RingswitchEthernetXBDupAddrIndex_Type.__name__ = "Integer32"
_RingswitchEthernetXBDupAddrIndex_Object = MibTableColumn
ringswitchEthernetXBDupAddrIndex = _RingswitchEthernetXBDupAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 2, 1, 2),
    _RingswitchEthernetXBDupAddrIndex_Type()
)
ringswitchEthernetXBDupAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBDupAddrIndex.setStatus("mandatory")
_RingswitchEthernetXBDupAddrMacAddress_Type = TRNMacAddress
_RingswitchEthernetXBDupAddrMacAddress_Object = MibTableColumn
ringswitchEthernetXBDupAddrMacAddress = _RingswitchEthernetXBDupAddrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 2, 1, 3),
    _RingswitchEthernetXBDupAddrMacAddress_Type()
)
ringswitchEthernetXBDupAddrMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringswitchEthernetXBDupAddrMacAddress.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsTable_Object = MibTable
ringswitchEthernetXBToTRNStatsTable = _RingswitchEthernetXBToTRNStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3)
)
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsTable.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsEntry_Object = MibTableRow
ringswitchEthernetXBToTRNStatsEntry = _RingswitchEthernetXBToTRNStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1)
)
ringswitchEthernetXBToTRNStatsEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchEthernetXBToTRNStatsIfIndex"),
)
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsEntry.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsIfIndex_Type = Integer32
_RingswitchEthernetXBToTRNStatsIfIndex_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsIfIndex = _RingswitchEthernetXBToTRNStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 1),
    _RingswitchEthernetXBToTRNStatsIfIndex_Type()
)
ringswitchEthernetXBToTRNStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsIfIndex.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscSptEncapsBlock_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscSptEncapsBlock_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscSptEncapsBlock = _RingswitchEthernetXBToTRNStatsDiscSptEncapsBlock_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 2),
    _RingswitchEthernetXBToTRNStatsDiscSptEncapsBlock_Type()
)
ringswitchEthernetXBToTRNStatsDiscSptEncapsBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscSptEncapsBlock.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscFilter_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscFilter_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscFilter = _RingswitchEthernetXBToTRNStatsDiscFilter_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 3),
    _RingswitchEthernetXBToTRNStatsDiscFilter_Type()
)
ringswitchEthernetXBToTRNStatsDiscFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscFilter.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscBPDU_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscBPDU_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscBPDU = _RingswitchEthernetXBToTRNStatsDiscBPDU_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 4),
    _RingswitchEthernetXBToTRNStatsDiscBPDU_Type()
)
ringswitchEthernetXBToTRNStatsDiscBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscBPDU.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscBPDUEncaps_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscBPDUEncaps_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscBPDUEncaps = _RingswitchEthernetXBToTRNStatsDiscBPDUEncaps_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 5),
    _RingswitchEthernetXBToTRNStatsDiscBPDUEncaps_Type()
)
ringswitchEthernetXBToTRNStatsDiscBPDUEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscBPDUEncaps.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscTag8021qCfi_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscTag8021qCfi_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscTag8021qCfi = _RingswitchEthernetXBToTRNStatsDiscTag8021qCfi_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 6),
    _RingswitchEthernetXBToTRNStatsDiscTag8021qCfi_Type()
)
ringswitchEthernetXBToTRNStatsDiscTag8021qCfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscTag8021qCfi.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscTag8021qVlan_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscTag8021qVlan_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscTag8021qVlan = _RingswitchEthernetXBToTRNStatsDiscTag8021qVlan_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 7),
    _RingswitchEthernetXBToTRNStatsDiscTag8021qVlan_Type()
)
ringswitchEthernetXBToTRNStatsDiscTag8021qVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscTag8021qVlan.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscBadRif_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscBadRif_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscBadRif = _RingswitchEthernetXBToTRNStatsDiscBadRif_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 8),
    _RingswitchEthernetXBToTRNStatsDiscBadRif_Type()
)
ringswitchEthernetXBToTRNStatsDiscBadRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscBadRif.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscHopLimit_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscHopLimit_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscHopLimit = _RingswitchEthernetXBToTRNStatsDiscHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 9),
    _RingswitchEthernetXBToTRNStatsDiscHopLimit_Type()
)
ringswitchEthernetXBToTRNStatsDiscHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscHopLimit.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscDuplicateRin_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscDuplicateRin_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscDuplicateRin = _RingswitchEthernetXBToTRNStatsDiscDuplicateRin_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 10),
    _RingswitchEthernetXBToTRNStatsDiscDuplicateRin_Type()
)
ringswitchEthernetXBToTRNStatsDiscDuplicateRin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscDuplicateRin.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscIPDisabled_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscIPDisabled_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscIPDisabled = _RingswitchEthernetXBToTRNStatsDiscIPDisabled_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 11),
    _RingswitchEthernetXBToTRNStatsDiscIPDisabled_Type()
)
ringswitchEthernetXBToTRNStatsDiscIPDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscIPDisabled.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscARPDisabled_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscARPDisabled_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscARPDisabled = _RingswitchEthernetXBToTRNStatsDiscARPDisabled_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 12),
    _RingswitchEthernetXBToTRNStatsDiscARPDisabled_Type()
)
ringswitchEthernetXBToTRNStatsDiscARPDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscARPDisabled.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscNCPCache_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscNCPCache_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscNCPCache = _RingswitchEthernetXBToTRNStatsDiscNCPCache_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 13),
    _RingswitchEthernetXBToTRNStatsDiscNCPCache_Type()
)
ringswitchEthernetXBToTRNStatsDiscNCPCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscNCPCache.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscIPXDisabled_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscIPXDisabled_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscIPXDisabled = _RingswitchEthernetXBToTRNStatsDiscIPXDisabled_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 14),
    _RingswitchEthernetXBToTRNStatsDiscIPXDisabled_Type()
)
ringswitchEthernetXBToTRNStatsDiscIPXDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscIPXDisabled.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscIPXTypeSnap_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscIPXTypeSnap_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscIPXTypeSnap = _RingswitchEthernetXBToTRNStatsDiscIPXTypeSnap_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 15),
    _RingswitchEthernetXBToTRNStatsDiscIPXTypeSnap_Type()
)
ringswitchEthernetXBToTRNStatsDiscIPXTypeSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscIPXTypeSnap.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscIPXType8022_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscIPXType8022_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscIPXType8022 = _RingswitchEthernetXBToTRNStatsDiscIPXType8022_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 16),
    _RingswitchEthernetXBToTRNStatsDiscIPXType8022_Type()
)
ringswitchEthernetXBToTRNStatsDiscIPXType8022.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscIPXType8022.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscIPXType8023_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscIPXType8023_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscIPXType8023 = _RingswitchEthernetXBToTRNStatsDiscIPXType8023_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 17),
    _RingswitchEthernetXBToTRNStatsDiscIPXType8023_Type()
)
ringswitchEthernetXBToTRNStatsDiscIPXType8023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscIPXType8023.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsDiscIPXTypeDix_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsDiscIPXTypeDix_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsDiscIPXTypeDix = _RingswitchEthernetXBToTRNStatsDiscIPXTypeDix_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 18),
    _RingswitchEthernetXBToTRNStatsDiscIPXTypeDix_Type()
)
ringswitchEthernetXBToTRNStatsDiscIPXTypeDix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsDiscIPXTypeDix.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsNoFakeBuffer_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsNoFakeBuffer_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsNoFakeBuffer = _RingswitchEthernetXBToTRNStatsNoFakeBuffer_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 19),
    _RingswitchEthernetXBToTRNStatsNoFakeBuffer_Type()
)
ringswitchEthernetXBToTRNStatsNoFakeBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsNoFakeBuffer.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsCacheFull_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsCacheFull_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsCacheFull = _RingswitchEthernetXBToTRNStatsCacheFull_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 20),
    _RingswitchEthernetXBToTRNStatsCacheFull_Type()
)
ringswitchEthernetXBToTRNStatsCacheFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsCacheFull.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsFwdIPFrames_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsFwdIPFrames_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsFwdIPFrames = _RingswitchEthernetXBToTRNStatsFwdIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 21),
    _RingswitchEthernetXBToTRNStatsFwdIPFrames_Type()
)
ringswitchEthernetXBToTRNStatsFwdIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsFwdIPFrames.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsFwdIPMulticast_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsFwdIPMulticast_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsFwdIPMulticast = _RingswitchEthernetXBToTRNStatsFwdIPMulticast_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 22),
    _RingswitchEthernetXBToTRNStatsFwdIPMulticast_Type()
)
ringswitchEthernetXBToTRNStatsFwdIPMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsFwdIPMulticast.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsFwdARPFrames_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsFwdARPFrames_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsFwdARPFrames = _RingswitchEthernetXBToTRNStatsFwdARPFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 23),
    _RingswitchEthernetXBToTRNStatsFwdARPFrames_Type()
)
ringswitchEthernetXBToTRNStatsFwdARPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsFwdARPFrames.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsFwdIPXFrames_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsFwdIPXFrames_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsFwdIPXFrames = _RingswitchEthernetXBToTRNStatsFwdIPXFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 24),
    _RingswitchEthernetXBToTRNStatsFwdIPXFrames_Type()
)
ringswitchEthernetXBToTRNStatsFwdIPXFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsFwdIPXFrames.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsFwdAARPPh1Frames_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsFwdAARPPh1Frames_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsFwdAARPPh1Frames = _RingswitchEthernetXBToTRNStatsFwdAARPPh1Frames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 25),
    _RingswitchEthernetXBToTRNStatsFwdAARPPh1Frames_Type()
)
ringswitchEthernetXBToTRNStatsFwdAARPPh1Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsFwdAARPPh1Frames.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsFwdAARPPh2Frames_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsFwdAARPPh2Frames_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsFwdAARPPh2Frames = _RingswitchEthernetXBToTRNStatsFwdAARPPh2Frames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 26),
    _RingswitchEthernetXBToTRNStatsFwdAARPPh2Frames_Type()
)
ringswitchEthernetXBToTRNStatsFwdAARPPh2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsFwdAARPPh2Frames.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsFwdOtherEthFrames_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsFwdOtherEthFrames_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsFwdOtherEthFrames = _RingswitchEthernetXBToTRNStatsFwdOtherEthFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 27),
    _RingswitchEthernetXBToTRNStatsFwdOtherEthFrames_Type()
)
ringswitchEthernetXBToTRNStatsFwdOtherEthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsFwdOtherEthFrames.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsFwdZeroOUIFrames_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsFwdZeroOUIFrames_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsFwdZeroOUIFrames = _RingswitchEthernetXBToTRNStatsFwdZeroOUIFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 28),
    _RingswitchEthernetXBToTRNStatsFwdZeroOUIFrames_Type()
)
ringswitchEthernetXBToTRNStatsFwdZeroOUIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsFwdZeroOUIFrames.setStatus("deprecated")
_RingswitchEthernetXBToTRNStatsFwdOtherDLCFrames_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsFwdOtherDLCFrames_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsFwdOtherDLCFrames = _RingswitchEthernetXBToTRNStatsFwdOtherDLCFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 29),
    _RingswitchEthernetXBToTRNStatsFwdOtherDLCFrames_Type()
)
ringswitchEthernetXBToTRNStatsFwdOtherDLCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsFwdOtherDLCFrames.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsFwdBPDUEncaps_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsFwdBPDUEncaps_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsFwdBPDUEncaps = _RingswitchEthernetXBToTRNStatsFwdBPDUEncaps_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 30),
    _RingswitchEthernetXBToTRNStatsFwdBPDUEncaps_Type()
)
ringswitchEthernetXBToTRNStatsFwdBPDUEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsFwdBPDUEncaps.setStatus("mandatory")
_RingswitchEthernetXBToTRNStatsFwdBPDUDecaps_Type = INTEGER48
_RingswitchEthernetXBToTRNStatsFwdBPDUDecaps_Object = MibTableColumn
ringswitchEthernetXBToTRNStatsFwdBPDUDecaps = _RingswitchEthernetXBToTRNStatsFwdBPDUDecaps_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 3, 1, 31),
    _RingswitchEthernetXBToTRNStatsFwdBPDUDecaps_Type()
)
ringswitchEthernetXBToTRNStatsFwdBPDUDecaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBToTRNStatsFwdBPDUDecaps.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsTable_Object = MibTable
ringswitchEthernetXBFromTRNStatsTable = _RingswitchEthernetXBFromTRNStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4)
)
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsTable.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsEntry_Object = MibTableRow
ringswitchEthernetXBFromTRNStatsEntry = _RingswitchEthernetXBFromTRNStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1)
)
ringswitchEthernetXBFromTRNStatsEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchEthernetXBFromTRNStatsIfIndex"),
)
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsEntry.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsIfIndex_Type = Integer32
_RingswitchEthernetXBFromTRNStatsIfIndex_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsIfIndex = _RingswitchEthernetXBFromTRNStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 1),
    _RingswitchEthernetXBFromTRNStatsIfIndex_Type()
)
ringswitchEthernetXBFromTRNStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsIfIndex.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscTooBig_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscTooBig_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscTooBig = _RingswitchEthernetXBFromTRNStatsDiscTooBig_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 2),
    _RingswitchEthernetXBFromTRNStatsDiscTooBig_Type()
)
ringswitchEthernetXBFromTRNStatsDiscTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscTooBig.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscSptEncapsBlock_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscSptEncapsBlock_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscSptEncapsBlock = _RingswitchEthernetXBFromTRNStatsDiscSptEncapsBlock_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 3),
    _RingswitchEthernetXBFromTRNStatsDiscSptEncapsBlock_Type()
)
ringswitchEthernetXBFromTRNStatsDiscSptEncapsBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscSptEncapsBlock.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscFilter_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscFilter_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscFilter = _RingswitchEthernetXBFromTRNStatsDiscFilter_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 4),
    _RingswitchEthernetXBFromTRNStatsDiscFilter_Type()
)
ringswitchEthernetXBFromTRNStatsDiscFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscFilter.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscBPDU_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscBPDU_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscBPDU = _RingswitchEthernetXBFromTRNStatsDiscBPDU_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 5),
    _RingswitchEthernetXBFromTRNStatsDiscBPDU_Type()
)
ringswitchEthernetXBFromTRNStatsDiscBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscBPDU.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscBPDUEncaps_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscBPDUEncaps_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscBPDUEncaps = _RingswitchEthernetXBFromTRNStatsDiscBPDUEncaps_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 6),
    _RingswitchEthernetXBFromTRNStatsDiscBPDUEncaps_Type()
)
ringswitchEthernetXBFromTRNStatsDiscBPDUEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscBPDUEncaps.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscTag8021qCfi_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscTag8021qCfi_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscTag8021qCfi = _RingswitchEthernetXBFromTRNStatsDiscTag8021qCfi_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 7),
    _RingswitchEthernetXBFromTRNStatsDiscTag8021qCfi_Type()
)
ringswitchEthernetXBFromTRNStatsDiscTag8021qCfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscTag8021qCfi.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscTag8021qVlan_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscTag8021qVlan_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscTag8021qVlan = _RingswitchEthernetXBFromTRNStatsDiscTag8021qVlan_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 8),
    _RingswitchEthernetXBFromTRNStatsDiscTag8021qVlan_Type()
)
ringswitchEthernetXBFromTRNStatsDiscTag8021qVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscTag8021qVlan.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscBadRIF_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscBadRIF_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscBadRIF = _RingswitchEthernetXBFromTRNStatsDiscBadRIF_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 9),
    _RingswitchEthernetXBFromTRNStatsDiscBadRIF_Type()
)
ringswitchEthernetXBFromTRNStatsDiscBadRIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscBadRIF.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscZeroRingNum_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscZeroRingNum_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscZeroRingNum = _RingswitchEthernetXBFromTRNStatsDiscZeroRingNum_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 10),
    _RingswitchEthernetXBFromTRNStatsDiscZeroRingNum_Type()
)
ringswitchEthernetXBFromTRNStatsDiscZeroRingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscZeroRingNum.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscNonTermRIF_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscNonTermRIF_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscNonTermRIF = _RingswitchEthernetXBFromTRNStatsDiscNonTermRIF_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 11),
    _RingswitchEthernetXBFromTRNStatsDiscNonTermRIF_Type()
)
ringswitchEthernetXBFromTRNStatsDiscNonTermRIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscNonTermRIF.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscIPDisabled_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscIPDisabled_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscIPDisabled = _RingswitchEthernetXBFromTRNStatsDiscIPDisabled_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 12),
    _RingswitchEthernetXBFromTRNStatsDiscIPDisabled_Type()
)
ringswitchEthernetXBFromTRNStatsDiscIPDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscIPDisabled.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscARPDisabled_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscARPDisabled_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscARPDisabled = _RingswitchEthernetXBFromTRNStatsDiscARPDisabled_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 13),
    _RingswitchEthernetXBFromTRNStatsDiscARPDisabled_Type()
)
ringswitchEthernetXBFromTRNStatsDiscARPDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscARPDisabled.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscIPCantFrag_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscIPCantFrag_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscIPCantFrag = _RingswitchEthernetXBFromTRNStatsDiscIPCantFrag_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 14),
    _RingswitchEthernetXBFromTRNStatsDiscIPCantFrag_Type()
)
ringswitchEthernetXBFromTRNStatsDiscIPCantFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscIPCantFrag.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscNCPCache_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscNCPCache_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscNCPCache = _RingswitchEthernetXBFromTRNStatsDiscNCPCache_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 15),
    _RingswitchEthernetXBFromTRNStatsDiscNCPCache_Type()
)
ringswitchEthernetXBFromTRNStatsDiscNCPCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscNCPCache.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscIPXDisabled_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscIPXDisabled_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscIPXDisabled = _RingswitchEthernetXBFromTRNStatsDiscIPXDisabled_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 16),
    _RingswitchEthernetXBFromTRNStatsDiscIPXDisabled_Type()
)
ringswitchEthernetXBFromTRNStatsDiscIPXDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscIPXDisabled.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscIPXTypeSnap_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscIPXTypeSnap_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscIPXTypeSnap = _RingswitchEthernetXBFromTRNStatsDiscIPXTypeSnap_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 17),
    _RingswitchEthernetXBFromTRNStatsDiscIPXTypeSnap_Type()
)
ringswitchEthernetXBFromTRNStatsDiscIPXTypeSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscIPXTypeSnap.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsDiscIPXType8022_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsDiscIPXType8022_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsDiscIPXType8022 = _RingswitchEthernetXBFromTRNStatsDiscIPXType8022_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 18),
    _RingswitchEthernetXBFromTRNStatsDiscIPXType8022_Type()
)
ringswitchEthernetXBFromTRNStatsDiscIPXType8022.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsDiscIPXType8022.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsCacheFull_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsCacheFull_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsCacheFull = _RingswitchEthernetXBFromTRNStatsCacheFull_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 19),
    _RingswitchEthernetXBFromTRNStatsCacheFull_Type()
)
ringswitchEthernetXBFromTRNStatsCacheFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsCacheFull.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsRIFCacheFull_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsRIFCacheFull_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsRIFCacheFull = _RingswitchEthernetXBFromTRNStatsRIFCacheFull_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 20),
    _RingswitchEthernetXBFromTRNStatsRIFCacheFull_Type()
)
ringswitchEthernetXBFromTRNStatsRIFCacheFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsRIFCacheFull.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsFwdIPFrames_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsFwdIPFrames_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsFwdIPFrames = _RingswitchEthernetXBFromTRNStatsFwdIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 21),
    _RingswitchEthernetXBFromTRNStatsFwdIPFrames_Type()
)
ringswitchEthernetXBFromTRNStatsFwdIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsFwdIPFrames.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsFwdIPFragmented_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsFwdIPFragmented_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsFwdIPFragmented = _RingswitchEthernetXBFromTRNStatsFwdIPFragmented_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 22),
    _RingswitchEthernetXBFromTRNStatsFwdIPFragmented_Type()
)
ringswitchEthernetXBFromTRNStatsFwdIPFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsFwdIPFragmented.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsFwdIPMulticast_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsFwdIPMulticast_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsFwdIPMulticast = _RingswitchEthernetXBFromTRNStatsFwdIPMulticast_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 23),
    _RingswitchEthernetXBFromTRNStatsFwdIPMulticast_Type()
)
ringswitchEthernetXBFromTRNStatsFwdIPMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsFwdIPMulticast.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsFwdARPFrames_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsFwdARPFrames_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsFwdARPFrames = _RingswitchEthernetXBFromTRNStatsFwdARPFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 24),
    _RingswitchEthernetXBFromTRNStatsFwdARPFrames_Type()
)
ringswitchEthernetXBFromTRNStatsFwdARPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsFwdARPFrames.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsFwdIPXFrames_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsFwdIPXFrames_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsFwdIPXFrames = _RingswitchEthernetXBFromTRNStatsFwdIPXFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 25),
    _RingswitchEthernetXBFromTRNStatsFwdIPXFrames_Type()
)
ringswitchEthernetXBFromTRNStatsFwdIPXFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsFwdIPXFrames.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsFwdAARPPh1Frames_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsFwdAARPPh1Frames_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsFwdAARPPh1Frames = _RingswitchEthernetXBFromTRNStatsFwdAARPPh1Frames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 26),
    _RingswitchEthernetXBFromTRNStatsFwdAARPPh1Frames_Type()
)
ringswitchEthernetXBFromTRNStatsFwdAARPPh1Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsFwdAARPPh1Frames.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsFwdAARPPh2Frames_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsFwdAARPPh2Frames_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsFwdAARPPh2Frames = _RingswitchEthernetXBFromTRNStatsFwdAARPPh2Frames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 27),
    _RingswitchEthernetXBFromTRNStatsFwdAARPPh2Frames_Type()
)
ringswitchEthernetXBFromTRNStatsFwdAARPPh2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsFwdAARPPh2Frames.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsFwdTunnel8021hFrames_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsFwdTunnel8021hFrames_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsFwdTunnel8021hFrames = _RingswitchEthernetXBFromTRNStatsFwdTunnel8021hFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 28),
    _RingswitchEthernetXBFromTRNStatsFwdTunnel8021hFrames_Type()
)
ringswitchEthernetXBFromTRNStatsFwdTunnel8021hFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsFwdTunnel8021hFrames.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsFwdZeroOUISnapFrames_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsFwdZeroOUISnapFrames_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsFwdZeroOUISnapFrames = _RingswitchEthernetXBFromTRNStatsFwdZeroOUISnapFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 29),
    _RingswitchEthernetXBFromTRNStatsFwdZeroOUISnapFrames_Type()
)
ringswitchEthernetXBFromTRNStatsFwdZeroOUISnapFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsFwdZeroOUISnapFrames.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsFwdOtherDLCFrames_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsFwdOtherDLCFrames_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsFwdOtherDLCFrames = _RingswitchEthernetXBFromTRNStatsFwdOtherDLCFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 30),
    _RingswitchEthernetXBFromTRNStatsFwdOtherDLCFrames_Type()
)
ringswitchEthernetXBFromTRNStatsFwdOtherDLCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsFwdOtherDLCFrames.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsFwdBPDUDecaps_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsFwdBPDUDecaps_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsFwdBPDUDecaps = _RingswitchEthernetXBFromTRNStatsFwdBPDUDecaps_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 31),
    _RingswitchEthernetXBFromTRNStatsFwdBPDUDecaps_Type()
)
ringswitchEthernetXBFromTRNStatsFwdBPDUDecaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsFwdBPDUDecaps.setStatus("mandatory")
_RingswitchEthernetXBFromTRNStatsFwdBPDUEncaps_Type = INTEGER48
_RingswitchEthernetXBFromTRNStatsFwdBPDUEncaps_Object = MibTableColumn
ringswitchEthernetXBFromTRNStatsFwdBPDUEncaps = _RingswitchEthernetXBFromTRNStatsFwdBPDUEncaps_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 4, 1, 32),
    _RingswitchEthernetXBFromTRNStatsFwdBPDUEncaps_Type()
)
ringswitchEthernetXBFromTRNStatsFwdBPDUEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetXBFromTRNStatsFwdBPDUEncaps.setStatus("mandatory")
_RingswitchEthernetExtPhysStatsTable_Object = MibTable
ringswitchEthernetExtPhysStatsTable = _RingswitchEthernetExtPhysStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 5)
)
if mibBuilder.loadTexts:
    ringswitchEthernetExtPhysStatsTable.setStatus("mandatory")
_RingswitchEthernetExtPhysStatsEntry_Object = MibTableRow
ringswitchEthernetExtPhysStatsEntry = _RingswitchEthernetExtPhysStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 5, 1)
)
ringswitchEthernetExtPhysStatsEntry.setIndexNames(
    (0, "MADGERSW-MIB", "ringswitchEthernetExtPhysStatsIfIndex"),
)
if mibBuilder.loadTexts:
    ringswitchEthernetExtPhysStatsEntry.setStatus("mandatory")
_RingswitchEthernetExtPhysStatsIfIndex_Type = Integer32
_RingswitchEthernetExtPhysStatsIfIndex_Object = MibTableColumn
ringswitchEthernetExtPhysStatsIfIndex = _RingswitchEthernetExtPhysStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 5, 1, 1),
    _RingswitchEthernetExtPhysStatsIfIndex_Type()
)
ringswitchEthernetExtPhysStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetExtPhysStatsIfIndex.setStatus("mandatory")
_RingswitchEthernetExtPhysStatsRxDataErrors_Type = Integer32
_RingswitchEthernetExtPhysStatsRxDataErrors_Object = MibTableColumn
ringswitchEthernetExtPhysStatsRxDataErrors = _RingswitchEthernetExtPhysStatsRxDataErrors_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 5, 1, 2),
    _RingswitchEthernetExtPhysStatsRxDataErrors_Type()
)
ringswitchEthernetExtPhysStatsRxDataErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetExtPhysStatsRxDataErrors.setStatus("mandatory")
_RingswitchEthernetExtPhysStatsRxSequenceErrors_Type = Integer32
_RingswitchEthernetExtPhysStatsRxSequenceErrors_Object = MibTableColumn
ringswitchEthernetExtPhysStatsRxSequenceErrors = _RingswitchEthernetExtPhysStatsRxSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 5, 1, 3),
    _RingswitchEthernetExtPhysStatsRxSequenceErrors_Type()
)
ringswitchEthernetExtPhysStatsRxSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetExtPhysStatsRxSequenceErrors.setStatus("mandatory")
_RingswitchEthernetExtPhysStatsRxCarrierExtErrors_Type = Integer32
_RingswitchEthernetExtPhysStatsRxCarrierExtErrors_Object = MibTableColumn
ringswitchEthernetExtPhysStatsRxCarrierExtErrors = _RingswitchEthernetExtPhysStatsRxCarrierExtErrors_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 5, 1, 4),
    _RingswitchEthernetExtPhysStatsRxCarrierExtErrors_Type()
)
ringswitchEthernetExtPhysStatsRxCarrierExtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetExtPhysStatsRxCarrierExtErrors.setStatus("mandatory")
_RingswitchEthernetExtPhysStatsXonRxFrames_Type = Integer32
_RingswitchEthernetExtPhysStatsXonRxFrames_Object = MibTableColumn
ringswitchEthernetExtPhysStatsXonRxFrames = _RingswitchEthernetExtPhysStatsXonRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 5, 1, 5),
    _RingswitchEthernetExtPhysStatsXonRxFrames_Type()
)
ringswitchEthernetExtPhysStatsXonRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetExtPhysStatsXonRxFrames.setStatus("mandatory")
_RingswitchEthernetExtPhysStatsXonTxFrames_Type = Integer32
_RingswitchEthernetExtPhysStatsXonTxFrames_Object = MibTableColumn
ringswitchEthernetExtPhysStatsXonTxFrames = _RingswitchEthernetExtPhysStatsXonTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 5, 1, 6),
    _RingswitchEthernetExtPhysStatsXonTxFrames_Type()
)
ringswitchEthernetExtPhysStatsXonTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetExtPhysStatsXonTxFrames.setStatus("mandatory")
_RingswitchEthernetExtPhysStatsXoffRxFrames_Type = Integer32
_RingswitchEthernetExtPhysStatsXoffRxFrames_Object = MibTableColumn
ringswitchEthernetExtPhysStatsXoffRxFrames = _RingswitchEthernetExtPhysStatsXoffRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 5, 1, 7),
    _RingswitchEthernetExtPhysStatsXoffRxFrames_Type()
)
ringswitchEthernetExtPhysStatsXoffRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetExtPhysStatsXoffRxFrames.setStatus("mandatory")
_RingswitchEthernetExtPhysStatsXoffTxFrames_Type = Integer32
_RingswitchEthernetExtPhysStatsXoffTxFrames_Object = MibTableColumn
ringswitchEthernetExtPhysStatsXoffTxFrames = _RingswitchEthernetExtPhysStatsXoffTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 494, 4, 21, 5, 1, 8),
    _RingswitchEthernetExtPhysStatsXoffTxFrames_Type()
)
ringswitchEthernetExtPhysStatsXoffTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringswitchEthernetExtPhysStatsXoffTxFrames.setStatus("mandatory")

# Managed Objects groups


# Notification objects

fanPSSpeedFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 1)
)
fanPSSpeedFailed.setObjects(
    ("MADGERSW-MIB", "ringswitchBasePSFanSpeed")
)
if mibBuilder.loadTexts:
    fanPSSpeedFailed.setStatus(
        ""
    )

fanExtSpeedFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 2)
)
fanExtSpeedFailed.setObjects(
    ("MADGERSW-MIB", "ringswitchBaseExtFanSpeed")
)
if mibBuilder.loadTexts:
    fanExtSpeedFailed.setStatus(
        ""
    )

portFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 3)
)
portFailed.setObjects(
    ("MADGERSW-MIB", "ringswitchPortAdapterStatus")
)
if mibBuilder.loadTexts:
    portFailed.setStatus(
        ""
    )

brTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 4)
)
brTestFailed.setObjects(
    ("MADGERSW-MIB", "ringswitchPortTestError")
)
if mibBuilder.loadTexts:
    brTestFailed.setStatus(
        ""
    )

elanRingnumFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 5)
)
elanRingnumFailed.setObjects(
    ("MADGERSW-MIB", "ringswitchGenPortNum")
)
if mibBuilder.loadTexts:
    elanRingnumFailed.setStatus(
        ""
    )

routeDescriptorFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 6)
)
routeDescriptorFailed.setObjects(
      *(("MADGERSW-MIB", "ringswitchGenPortNum"),
        ("MADGERSW-MIB", "ringswitchRouteDescrSegmentID"),
        ("MADGERSW-MIB", "ringswitchRouteDescrBridgeNumber"))
)
if mibBuilder.loadTexts:
    routeDescriptorFailed.setStatus(
        ""
    )

fanSpeedFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 7)
)
fanSpeedFailed.setObjects(
    ("MADGERSW-MIB", "ringswitchFanSpeed")
)
if mibBuilder.loadTexts:
    fanSpeedFailed.setStatus(
        ""
    )

psuFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 8)
)
psuFailed.setObjects(
    ("MADGERSW-MIB", "ringswitchPSUStatus")
)
if mibBuilder.loadTexts:
    psuFailed.setStatus(
        ""
    )

versionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 9)
)
versionMismatch.setObjects(
    ("MADGERSW-MIB", "ringswitchVersionMismatch")
)
if mibBuilder.loadTexts:
    versionMismatch.setStatus(
        ""
    )

genPortStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 10)
)
genPortStatus.setObjects(
    ("MADGERSW-MIB", "ringswitchGenPortLastStatus")
)
if mibBuilder.loadTexts:
    genPortStatus.setStatus(
        ""
    )

slotStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 11)
)
slotStatus.setObjects(
    ("MADGERSW-MIB", "ringswitchSlotLastStatus")
)
if mibBuilder.loadTexts:
    slotStatus.setStatus(
        ""
    )

oneNodePerPortViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 12)
)
oneNodePerPortViolation.setObjects(
    ("MADGERSW-MIB", "ringswitchTRGrpSwtchIfIndex")
)
if mibBuilder.loadTexts:
    oneNodePerPortViolation.setStatus(
        ""
    )

grpSwitchPortDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 13)
)
grpSwitchPortDisabled.setObjects(
      *(("MADGERSW-MIB", "ringswitchTRGrpSwtchIfIndex"),
        ("MADGERSW-MIB", "ringswitchTRGrpSwtchPortIndex"),
        ("MADGERSW-MIB", "ringswitchTRGrpSwtchTrapInfoReason"))
)
if mibBuilder.loadTexts:
    grpSwitchPortDisabled.setStatus(
        ""
    )

grpSwitchPortKilled = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 14)
)
grpSwitchPortKilled.setObjects(
      *(("MADGERSW-MIB", "ringswitchTRGrpSwtchIfIndex"),
        ("MADGERSW-MIB", "ringswitchTRGrpSwtchPortIndex"),
        ("MADGERSW-MIB", "ringswitchTRGrpSwtchTrapInfoReason"))
)
if mibBuilder.loadTexts:
    grpSwitchPortKilled.setStatus(
        ""
    )

downloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 15)
)
downloadFailed.setObjects(
    ("MADGERSW-MIB", "ringswitchDownloadFailed")
)
if mibBuilder.loadTexts:
    downloadFailed.setStatus(
        ""
    )

grpSwitchPortFaultDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 16)
)
grpSwitchPortFaultDetected.setObjects(
      *(("MADGERSW-MIB", "ringswitchTRGrpSwtchIfIndex"),
        ("MADGERSW-MIB", "ringswitchTRGrpSwtchPortIndex"),
        ("MADGERSW-MIB", "ringswitchTRGrpSwtchTrapInfoReason"))
)
if mibBuilder.loadTexts:
    grpSwitchPortFaultDetected.setStatus(
        ""
    )

fastFailoverWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 17)
)
fastFailoverWarning.setObjects(
      *(("MADGERSW-MIB", "ringswitchTRIfFastFailoverPrimaryPort"),
        ("MADGERSW-MIB", "ringswitchTRIfFastFailoverTrapInfoReason"))
)
if mibBuilder.loadTexts:
    fastFailoverWarning.setStatus(
        ""
    )

ethernetSTPBlockingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 494, 4, 0, 18)
)
ethernetSTPBlockingTrap.setObjects(
      *(("MADGERSW-MIB", "ringswitchEthernetIfIndex"),
        ("MADGERSW-MIB", "ringswitchEthernetIfSTPBlockingTrapInfo"))
)
if mibBuilder.loadTexts:
    ethernetSTPBlockingTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MADGERSW-MIB",
    **{"DisplayString": DisplayString,
       "INTEGER48": INTEGER48,
       "NSAP": NSAP,
       "TRNMacAddress": TRNMacAddress,
       "ETHMacAddress": ETHMacAddress,
       "RingswitchRowStatus": RingswitchRowStatus,
       "LCDText": LCDText,
       "madge": madge,
       "ringswitch": ringswitch,
       "fanPSSpeedFailed": fanPSSpeedFailed,
       "fanExtSpeedFailed": fanExtSpeedFailed,
       "portFailed": portFailed,
       "brTestFailed": brTestFailed,
       "elanRingnumFailed": elanRingnumFailed,
       "routeDescriptorFailed": routeDescriptorFailed,
       "fanSpeedFailed": fanSpeedFailed,
       "psuFailed": psuFailed,
       "versionMismatch": versionMismatch,
       "genPortStatus": genPortStatus,
       "slotStatus": slotStatus,
       "oneNodePerPortViolation": oneNodePerPortViolation,
       "grpSwitchPortDisabled": grpSwitchPortDisabled,
       "grpSwitchPortKilled": grpSwitchPortKilled,
       "downloadFailed": downloadFailed,
       "grpSwitchPortFaultDetected": grpSwitchPortFaultDetected,
       "fastFailoverWarning": fastFailoverWarning,
       "ethernetSTPBlockingTrap": ethernetSTPBlockingTrap,
       "ringswitchBase": ringswitchBase,
       "ringswitchBasePSFanSpeed": ringswitchBasePSFanSpeed,
       "ringswitchBaseExtFanSpeed": ringswitchBaseExtFanSpeed,
       "ringswitchBaseRipSapSuppression": ringswitchBaseRipSapSuppression,
       "ringswitchBaseAREConversion": ringswitchBaseAREConversion,
       "ringswitchBaseStpMode": ringswitchBaseStpMode,
       "ringswitchBaseRMONState": ringswitchBaseRMONState,
       "ringswitchBaseBackPlaneType": ringswitchBaseBackPlaneType,
       "ringswitchBaseRMONMirrorPort": ringswitchBaseRMONMirrorPort,
       "ringswitchBaseTotalResetCounters": ringswitchBaseTotalResetCounters,
       "ringswitchBaseDownloadMode": ringswitchBaseDownloadMode,
       "ringswitchPort": ringswitchPort,
       "ringswitchPortTable": ringswitchPortTable,
       "ringswitchPortEntry": ringswitchPortEntry,
       "ringswitchPortNum": ringswitchPortNum,
       "ringswitchPortRingStatus": ringswitchPortRingStatus,
       "ringswitchPortAdapterStatus": ringswitchPortAdapterStatus,
       "ringswitchPortMediaType": ringswitchPortMediaType,
       "ringswitchPortIfMode": ringswitchPortIfMode,
       "ringswitchPortRingSpeed": ringswitchPortRingSpeed,
       "ringswitchPortTestState": ringswitchPortTestState,
       "ringswitchPortTestError": ringswitchPortTestError,
       "ringswitchPortTestPhase": ringswitchPortTestPhase,
       "ringswitchPortSummary": ringswitchPortSummary,
       "ringswitchPortAddress": ringswitchPortAddress,
       "ringswitchPortLAA": ringswitchPortLAA,
       "ringswitchPortStationType": ringswitchPortStationType,
       "ringswitchPortRPSEnable": ringswitchPortRPSEnable,
       "ringswitchPortCutThruEnable": ringswitchPortCutThruEnable,
       "ringswitchPortInOctets": ringswitchPortInOctets,
       "ringswitchPortOutOctets": ringswitchPortOutOctets,
       "ringswitchPortSpecInFrames": ringswitchPortSpecInFrames,
       "ringswitchPortSpecOutFrames": ringswitchPortSpecOutFrames,
       "ringswitchPortApeInFrames": ringswitchPortApeInFrames,
       "ringswitchPortApeOutFrames": ringswitchPortApeOutFrames,
       "ringswitchPortSteInFrames": ringswitchPortSteInFrames,
       "ringswitchPortSteOutFrames": ringswitchPortSteOutFrames,
       "ringswitchPortResetCounters": ringswitchPortResetCounters,
       "ringswitchPortFixupMode": ringswitchPortFixupMode,
       "ringswitchPortForwardMode": ringswitchPortForwardMode,
       "ringswitchPortRMONCapabilities": ringswitchPortRMONCapabilities,
       "ringswitchPortRMONMode": ringswitchPortRMONMode,
       "ringswitchPortRMONSnoop": ringswitchPortRMONSnoop,
       "ringswitchPortTransparentInFrames": ringswitchPortTransparentInFrames,
       "ringswitchPortTransparentOutFrames": ringswitchPortTransparentOutFrames,
       "ringswitchPortTransparentDiscFrames": ringswitchPortTransparentDiscFrames,
       "ringswitchPortLEDs": ringswitchPortLEDs,
       "ringswitchFwd": ringswitchFwd,
       "ringswitchFwdAdminState": ringswitchFwdAdminState,
       "ringswitchFwdOperState": ringswitchFwdOperState,
       "ringswitchFwdPortTable": ringswitchFwdPortTable,
       "ringswitchFwdPortEntry": ringswitchFwdPortEntry,
       "ringswitchFwdPort": ringswitchFwdPort,
       "ringswitchFwdPortMode": ringswitchFwdPortMode,
       "ringswitchFwdPortStationType": ringswitchFwdPortStationType,
       "ringswitchFwdPortCutThruEnable": ringswitchFwdPortCutThruEnable,
       "ringswitchFwdPortSpecInFrames": ringswitchFwdPortSpecInFrames,
       "ringswitchFwdPortSpecOutFrames": ringswitchFwdPortSpecOutFrames,
       "ringswitchFwdPortApeInFrames": ringswitchFwdPortApeInFrames,
       "ringswitchFwdPortApeOutFrames": ringswitchFwdPortApeOutFrames,
       "ringswitchFwdPortSteInFrames": ringswitchFwdPortSteInFrames,
       "ringswitchFwdPortSteOutFrames": ringswitchFwdPortSteOutFrames,
       "ringswitchFwdPortTransparentInFrames": ringswitchFwdPortTransparentInFrames,
       "ringswitchFwdPortTransparentOutFrames": ringswitchFwdPortTransparentOutFrames,
       "ringswitchFwdPortTransparentDiscFrames": ringswitchFwdPortTransparentDiscFrames,
       "ringswitchFwdPortTestState": ringswitchFwdPortTestState,
       "ringswitchFwdPortTestError": ringswitchFwdPortTestError,
       "ringswitchFwdPortTestPhase": ringswitchFwdPortTestPhase,
       "ringswitchFwdPortTbForce": ringswitchFwdPortTbForce,
       "ringswitchFwdPortStpMaster": ringswitchFwdPortStpMaster,
       "ringswitchFwdPortTbState": ringswitchFwdPortTbState,
       "ringswitchFwdPortSteState": ringswitchFwdPortSteState,
       "ringswitchFwdPortTbUnicastInFrames": ringswitchFwdPortTbUnicastInFrames,
       "ringswitchFwdPortTbUnicastOutFrames": ringswitchFwdPortTbUnicastOutFrames,
       "ringswitchFwdPortTbBroadcastInFrames": ringswitchFwdPortTbBroadcastInFrames,
       "ringswitchFwdPortTbBroadcastOutFrames": ringswitchFwdPortTbBroadcastOutFrames,
       "ringswitchFwdPortTbMulticastInFrames": ringswitchFwdPortTbMulticastInFrames,
       "ringswitchFwdPortTbMulticastOutFrames": ringswitchFwdPortTbMulticastOutFrames,
       "ringswitchFwdPortTbMiscInFrames": ringswitchFwdPortTbMiscInFrames,
       "ringswitchFwdPortTbMiscOutFrames": ringswitchFwdPortTbMiscOutFrames,
       "ringswitchFwdPortMatrixSrSpecFrames": ringswitchFwdPortMatrixSrSpecFrames,
       "ringswitchFwdPortMatrixTbUniFrames": ringswitchFwdPortMatrixTbUniFrames,
       "ringswitchFwdPortEthernetSRBlk": ringswitchFwdPortEthernetSRBlk,
       "ringswitchFwdPortAutoPathCost": ringswitchFwdPortAutoPathCost,
       "ringswitchFwdPortBroadcastReflect": ringswitchFwdPortBroadcastReflect,
       "ringswitchFwdTotalRxFrames": ringswitchFwdTotalRxFrames,
       "ringswitchFwdTotalTxFrames": ringswitchFwdTotalTxFrames,
       "ringswitchFwdBridgeNum": ringswitchFwdBridgeNum,
       "ringswitchFwdTbForced": ringswitchFwdTbForced,
       "ringswitchFwdStpMasters": ringswitchFwdStpMasters,
       "ringswitchFwdGlobalHopLimit": ringswitchFwdGlobalHopLimit,
       "ringswitchFwdTotalBadFrames": ringswitchFwdTotalBadFrames,
       "ringswitchFwdTotalSpecInFrames": ringswitchFwdTotalSpecInFrames,
       "ringswitchFwdTotalSpecOutFrames": ringswitchFwdTotalSpecOutFrames,
       "ringswitchFwdTotalApeInFrames": ringswitchFwdTotalApeInFrames,
       "ringswitchFwdTotalApeOutFrames": ringswitchFwdTotalApeOutFrames,
       "ringswitchFwdTotalSteInFrames": ringswitchFwdTotalSteInFrames,
       "ringswitchFwdTotalSteOutFrames": ringswitchFwdTotalSteOutFrames,
       "ringswitchFwdTotalTransparentInFrames": ringswitchFwdTotalTransparentInFrames,
       "ringswitchFwdTotalTransparentOutFrames": ringswitchFwdTotalTransparentOutFrames,
       "ringswitchFwdTotalTpUnicastInFrames": ringswitchFwdTotalTpUnicastInFrames,
       "ringswitchFwdTotalTpUnicastOutFrames": ringswitchFwdTotalTpUnicastOutFrames,
       "ringswitchFwdTotalTpBroadcastInFrames": ringswitchFwdTotalTpBroadcastInFrames,
       "ringswitchFwdTotalTpBroadcastOutFrames": ringswitchFwdTotalTpBroadcastOutFrames,
       "ringswitchFwdTotalTpMulticastInFrames": ringswitchFwdTotalTpMulticastInFrames,
       "ringswitchFwdTotalTpMulticastOutFrames": ringswitchFwdTotalTpMulticastOutFrames,
       "ringswitchFwdTotalTpMiscInFrames": ringswitchFwdTotalTpMiscInFrames,
       "ringswitchFwdTotalTpMiscOutFrames": ringswitchFwdTotalTpMiscOutFrames,
       "ringswitchFwdMaxFrameSize": ringswitchFwdMaxFrameSize,
       "ringswitchLCD": ringswitchLCD,
       "ringswitchLCDTotalDisplays": ringswitchLCDTotalDisplays,
       "ringswitchLCDCurrentDisplay": ringswitchLCDCurrentDisplay,
       "ringswitchLCDCurrentMsgText": ringswitchLCDCurrentMsgText,
       "ringswitchLCDTable": ringswitchLCDTable,
       "ringswitchLCDTableEntry": ringswitchLCDTableEntry,
       "ringswitchLCDNum": ringswitchLCDNum,
       "ringswitchLCDMsgText": ringswitchLCDMsgText,
       "ringswitchLCDUp": ringswitchLCDUp,
       "ringswitchLCDDown": ringswitchLCDDown,
       "ringswitchLAN": ringswitchLAN,
       "ringswitchLANTable": ringswitchLANTable,
       "ringswitchLANEntry": ringswitchLANEntry,
       "ringswitchLANIndex": ringswitchLANIndex,
       "ringswitchLANName": ringswitchLANName,
       "ringswitchLANPermeable": ringswitchLANPermeable,
       "ringswitchLANStatus": ringswitchLANStatus,
       "ringswitchLANRingTable": ringswitchLANRingTable,
       "ringswitchLANRingEntry": ringswitchLANRingEntry,
       "ringswitchLANRingGroup": ringswitchLANRingGroup,
       "ringswitchLANRingIndex": ringswitchLANRingIndex,
       "ringswitchLANRingNum": ringswitchLANRingNum,
       "ringswitchLANRingStatus": ringswitchLANRingStatus,
       "ringswitchVirt": ringswitchVirt,
       "ringswitchVirtTB": ringswitchVirtTB,
       "ringswitchVirtTBTable": ringswitchVirtTBTable,
       "ringswitchVirtTBEntry": ringswitchVirtTBEntry,
       "ringswitchVirtTBIndex": ringswitchVirtTBIndex,
       "ringswitchVirtTBStatus": ringswitchVirtTBStatus,
       "ringswitchVirtTBName": ringswitchVirtTBName,
       "ringswitchVirtTBType": ringswitchVirtTBType,
       "ringswitchVirtTBNumArray": ringswitchVirtTBNumArray,
       "ringswitchVirtTBNumSize": ringswitchVirtTBNumSize,
       "ringswitchSlot": ringswitchSlot,
       "ringswitchSlotNumSlots": ringswitchSlotNumSlots,
       "ringswitchSlotTable": ringswitchSlotTable,
       "ringswitchSlotEntry": ringswitchSlotEntry,
       "ringswitchSlotIndex": ringswitchSlotIndex,
       "ringswitchSlotStatus": ringswitchSlotStatus,
       "ringswitchSlotBasePort": ringswitchSlotBasePort,
       "ringswitchSlotCardType": ringswitchSlotCardType,
       "ringswitchSlotCardId": ringswitchSlotCardId,
       "ringswitchSlotCardRevision": ringswitchSlotCardRevision,
       "ringswitchSlotCardDescription": ringswitchSlotCardDescription,
       "ringswitchSlotCardNumPorts": ringswitchSlotCardNumPorts,
       "ringswitchSlotCardLAN": ringswitchSlotCardLAN,
       "ringswitchSlotCardLEDs": ringswitchSlotCardLEDs,
       "ringswitchSlotIfAdminStatus": ringswitchSlotIfAdminStatus,
       "ringswitchSlotAdapterStatus": ringswitchSlotAdapterStatus,
       "ringswitchSlotTestError": ringswitchSlotTestError,
       "ringswitchSlotPortHealth": ringswitchSlotPortHealth,
       "ringswitchSlotLastStatus": ringswitchSlotLastStatus,
       "ringswitchSlotPortCreated": ringswitchSlotPortCreated,
       "ringswitchSlotHealth": ringswitchSlotHealth,
       "ringswitchSlotVersion": ringswitchSlotVersion,
       "ringswitchGenPort": ringswitchGenPort,
       "ringswitchGenPortTable": ringswitchGenPortTable,
       "ringswitchGenPortEntry": ringswitchGenPortEntry,
       "ringswitchGenPortNum": ringswitchGenPortNum,
       "ringswitchGenPortAdapterStatus": ringswitchGenPortAdapterStatus,
       "ringswitchGenPortAddress": ringswitchGenPortAddress,
       "ringswitchGenPortLAA": ringswitchGenPortLAA,
       "ringswitchGenPortInOctets": ringswitchGenPortInOctets,
       "ringswitchGenPortOutOctets": ringswitchGenPortOutOctets,
       "ringswitchGenPortResetCounters": ringswitchGenPortResetCounters,
       "ringswitchGenPortRMONCapabilities": ringswitchGenPortRMONCapabilities,
       "ringswitchGenPortRMONMode": ringswitchGenPortRMONMode,
       "ringswitchGenPortRMONSnoop": ringswitchGenPortRMONSnoop,
       "ringswitchGenPortIPXNet": ringswitchGenPortIPXNet,
       "ringswitchGenPortLastStatus": ringswitchGenPortLastStatus,
       "ringswitchGenPortCreate": ringswitchGenPortCreate,
       "ringswitchGenPortHealth": ringswitchGenPortHealth,
       "ringswitchTR": ringswitchTR,
       "ringswitchTRIfTable": ringswitchTRIfTable,
       "ringswitchTRIfEntry": ringswitchTRIfEntry,
       "ringswitchTRIfIndex": ringswitchTRIfIndex,
       "ringswitchTRIfRingSpeed": ringswitchTRIfRingSpeed,
       "ringswitchTRIfMode": ringswitchTRIfMode,
       "ringswitchTRIfRPSEnable": ringswitchTRIfRPSEnable,
       "ringswitchTRIfRingStatus": ringswitchTRIfRingStatus,
       "ringswitchTRIfSoftErrTimer": ringswitchTRIfSoftErrTimer,
       "ringswitchTRIfFrameStatusControl": ringswitchTRIfFrameStatusControl,
       "ringswitchTRIfTokenPriorityControl": ringswitchTRIfTokenPriorityControl,
       "ringswitchTRIfFastFailoverEnable": ringswitchTRIfFastFailoverEnable,
       "ringswitchTRIfFastFailoverStandbyStatus": ringswitchTRIfFastFailoverStandbyStatus,
       "ringswitchTRIfFastFailoverPrimaryPort": ringswitchTRIfFastFailoverPrimaryPort,
       "ringswitchTRIfFastFailoverTrapInfoReason": ringswitchTRIfFastFailoverTrapInfoReason,
       "ringswitchTRGrpSwtchTable": ringswitchTRGrpSwtchTable,
       "ringswitchTRGrpSwtchEntry": ringswitchTRGrpSwtchEntry,
       "ringswitchTRGrpSwtchIfIndex": ringswitchTRGrpSwtchIfIndex,
       "ringswitchTRGrpSwtchRemoveThreshold": ringswitchTRGrpSwtchRemoveThreshold,
       "ringswitchTRGrpSwtchRingPollAction": ringswitchTRGrpSwtchRingPollAction,
       "ringswitchTRGrpSwtchBeaconThreshold": ringswitchTRGrpSwtchBeaconThreshold,
       "ringswitchTRGrpSwtchBeaconAction": ringswitchTRGrpSwtchBeaconAction,
       "ringswitchTRGrpSwtchPurgeThreshold": ringswitchTRGrpSwtchPurgeThreshold,
       "ringswitchTRGrpSwtchPurgeAction": ringswitchTRGrpSwtchPurgeAction,
       "ringswitchTRGrpSwtchIsoErrThreshold": ringswitchTRGrpSwtchIsoErrThreshold,
       "ringswitchTRGrpSwtchIsoErrAction": ringswitchTRGrpSwtchIsoErrAction,
       "ringswitchTRGrpSwtchRingPollThreshold": ringswitchTRGrpSwtchRingPollThreshold,
       "ringswitchTRGrpSwtchPortTable": ringswitchTRGrpSwtchPortTable,
       "ringswitchTRGrpSwtchPortEntry": ringswitchTRGrpSwtchPortEntry,
       "ringswitchTRGrpSwtchPortIfIndex": ringswitchTRGrpSwtchPortIfIndex,
       "ringswitchTRGrpSwtchPortIndex": ringswitchTRGrpSwtchPortIndex,
       "ringswitchTRGrpSwtchPortAddress": ringswitchTRGrpSwtchPortAddress,
       "ringswitchTRGrpSwtchTrapInfo": ringswitchTRGrpSwtchTrapInfo,
       "ringswitchTRGrpSwtchTrapInfoReason": ringswitchTRGrpSwtchTrapInfoReason,
       "ringswitchTRGrpSwtchSlotTable": ringswitchTRGrpSwtchSlotTable,
       "ringswitchTRGrpSwtchSlotEntry": ringswitchTRGrpSwtchSlotEntry,
       "ringswitchTRGrpSwtchSlotIndex": ringswitchTRGrpSwtchSlotIndex,
       "ringswitchTRGrpSwtchSlotAdminStatii": ringswitchTRGrpSwtchSlotAdminStatii,
       "ringswitchTRGrpSwtchSlotAutoPartitions": ringswitchTRGrpSwtchSlotAutoPartitions,
       "ringswitchTRGrpSwtchSlotOperStatii": ringswitchTRGrpSwtchSlotOperStatii,
       "ringswitchFDDI": ringswitchFDDI,
       "ringswitchFDDICardTable": ringswitchFDDICardTable,
       "ringswitchFDDICardEntry": ringswitchFDDICardEntry,
       "ringswitchFDDICardNum": ringswitchFDDICardNum,
       "ringswitchFDDICardSMTIndex": ringswitchFDDICardSMTIndex,
       "ringswitchFDDICardFixupMode": ringswitchFDDICardFixupMode,
       "ringswitchFDDICardVRStatus": ringswitchFDDICardVRStatus,
       "ringswitchFDDICardVRRingNum": ringswitchFDDICardVRRingNum,
       "ringswitchFDDICardVRBridgeNum": ringswitchFDDICardVRBridgeNum,
       "ringswitchFDDICardStatus": ringswitchFDDICardStatus,
       "ringswitchATM": ringswitchATM,
       "ringswitchATMCardTable": ringswitchATMCardTable,
       "ringswitchATMCardEntry": ringswitchATMCardEntry,
       "ringswitchATMCardNum": ringswitchATMCardNum,
       "ringswitchATMCardAdminStatus": ringswitchATMCardAdminStatus,
       "ringswitchATMCardRemoteUNIVer": ringswitchATMCardRemoteUNIVer,
       "ringswitchATMCardLECSAddress": ringswitchATMCardLECSAddress,
       "ringswitchATMCardLECSIlmi": ringswitchATMCardLECSIlmi,
       "ringswitchATMCardLECSWka": ringswitchATMCardLECSWka,
       "ringswitchATMCardLECSPvc": ringswitchATMCardLECSPvc,
       "ringswitchATMCardActivePort": ringswitchATMCardActivePort,
       "ringswitchATMCardILMIStatus": ringswitchATMCardILMIStatus,
       "ringswitchATMCardSignalStatus": ringswitchATMCardSignalStatus,
       "ringswitchATMCardHardWiredESI": ringswitchATMCardHardWiredESI,
       "ringswitchATMCardLocalESI": ringswitchATMCardLocalESI,
       "ringswitchATMCardPortB": ringswitchATMCardPortB,
       "ringswitchATMCardMode": ringswitchATMCardMode,
       "ringswitchATMCardSONETIfIndex": ringswitchATMCardSONETIfIndex,
       "ringswitchATMCardATMIfIndex": ringswitchATMCardATMIfIndex,
       "ringswitchATMCardAAL5IfIndex": ringswitchATMCardAAL5IfIndex,
       "ringswitchATMCardRowStatuses": ringswitchATMCardRowStatuses,
       "ringswitchATMCardMediaType": ringswitchATMCardMediaType,
       "ringswitchATMCardConfigUNIVer": ringswitchATMCardConfigUNIVer,
       "ringswitchATMCardActualUNIVer": ringswitchATMCardActualUNIVer,
       "ringswitchATMCardEthLecSupport": ringswitchATMCardEthLecSupport,
       "ringswitchATMPortTable": ringswitchATMPortTable,
       "ringswitchATMPortEntry": ringswitchATMPortEntry,
       "ringswitchATMPortNum": ringswitchATMPortNum,
       "ringswitchATMPortFailReason": ringswitchATMPortFailReason,
       "ringswitchATMPortFailSecondary": ringswitchATMPortFailSecondary,
       "ringswitchATMPortRxDiscards": ringswitchATMPortRxDiscards,
       "ringswitchATMPortTxDiscards": ringswitchATMPortTxDiscards,
       "ringswitchATMPortTxQuotaDiscards": ringswitchATMPortTxQuotaDiscards,
       "ringswitchATMPortTxBUSBroadcasts": ringswitchATMPortTxBUSBroadcasts,
       "ringswitchATMPortTxBUSUnknowns": ringswitchATMPortTxBUSUnknowns,
       "ringswitchATMPortRxBUSFiltered": ringswitchATMPortRxBUSFiltered,
       "ringswitchATMPortIPXTypeETH": ringswitchATMPortIPXTypeETH,
       "ringswitchATMPortIPXTypeTRN": ringswitchATMPortIPXTypeTRN,
       "ringswitchATMPortIPXEvenize": ringswitchATMPortIPXEvenize,
       "ringswitchATMPortIPXBufLimit": ringswitchATMPortIPXBufLimit,
       "ringswitchATMPortIPXEnable": ringswitchATMPortIPXEnable,
       "ringswitchATMPortIPEnable": ringswitchATMPortIPEnable,
       "ringswitchATMPortIPMulticastType": ringswitchATMPortIPMulticastType,
       "ringswitchPSU": ringswitchPSU,
       "ringswitchPSUNumUnits": ringswitchPSUNumUnits,
       "ringswitchPSUTable": ringswitchPSUTable,
       "ringswitchPSUEntry": ringswitchPSUEntry,
       "ringswitchPSUIndex": ringswitchPSUIndex,
       "ringswitchPSUDescription": ringswitchPSUDescription,
       "ringswitchPSUStatus": ringswitchPSUStatus,
       "ringswitchFan": ringswitchFan,
       "ringswitchFanNumUnits": ringswitchFanNumUnits,
       "ringswitchFanTable": ringswitchFanTable,
       "ringswitchFanEntry": ringswitchFanEntry,
       "ringswitchFanIndex": ringswitchFanIndex,
       "ringswitchFanDescription": ringswitchFanDescription,
       "ringswitchFanSpeed": ringswitchFanSpeed,
       "ringswitchTrap": ringswitchTrap,
       "ringswitchRouteDescrSegmentID": ringswitchRouteDescrSegmentID,
       "ringswitchRouteDescrBridgeNumber": ringswitchRouteDescrBridgeNumber,
       "ringswitchVersionMismatch": ringswitchVersionMismatch,
       "ringswitchDownloadFailed": ringswitchDownloadFailed,
       "ringswitchFilter": ringswitchFilter,
       "ringswitchFilterTable": ringswitchFilterTable,
       "ringswitchFilterEntry": ringswitchFilterEntry,
       "ringswitchFilterIndex": ringswitchFilterIndex,
       "ringswitchFilterStatus": ringswitchFilterStatus,
       "ringswitchFilterName": ringswitchFilterName,
       "ringswitchFilterData": ringswitchFilterData,
       "ringswitchFilterExceptionType": ringswitchFilterExceptionType,
       "ringswitchFilterType": ringswitchFilterType,
       "ringswitchFilterForwardType": ringswitchFilterForwardType,
       "ringswitchFilterMatrixTable": ringswitchFilterMatrixTable,
       "ringswitchFilterMatrixEntry": ringswitchFilterMatrixEntry,
       "ringswitchFilterMatrixIndex": ringswitchFilterMatrixIndex,
       "ringswitchFilterMatrixRowIndex": ringswitchFilterMatrixRowIndex,
       "ringswitchFilterMatrixData": ringswitchFilterMatrixData,
       "ringswitchTLS": ringswitchTLS,
       "ringswitchTLSCardTable": ringswitchTLSCardTable,
       "ringswitchTLSCardEntry": ringswitchTLSCardEntry,
       "ringswitchTLSCardNum": ringswitchTLSCardNum,
       "ringswitchTLSCardRowStatuses": ringswitchTLSCardRowStatuses,
       "ringswitchTLSCardRIPTTL": ringswitchTLSCardRIPTTL,
       "ringswitchTLSCardRIPInterval": ringswitchTLSCardRIPInterval,
       "ringswitchTLSCardRIPAging": ringswitchTLSCardRIPAging,
       "ringswitchTLSCardDefRoute": ringswitchTLSCardDefRoute,
       "ringswitchTLSCardDefRouteMetric": ringswitchTLSCardDefRouteMetric,
       "ringswitchTLSCardRIPFlags": ringswitchTLSCardRIPFlags,
       "ringswitchTLSCardOSPFRouterId": ringswitchTLSCardOSPFRouterId,
       "ringswitchTLSCardOSPFFlags": ringswitchTLSCardOSPFFlags,
       "ringswitchTLSCardStatsCpuUsage": ringswitchTLSCardStatsCpuUsage,
       "ringswitchTLSCardStatsFreeMem": ringswitchTLSCardStatsFreeMem,
       "ringswitchTLSCardStatsFramesFwd": ringswitchTLSCardStatsFramesFwd,
       "ringswitchTLSCardStatsMaxCpuUsage": ringswitchTLSCardStatsMaxCpuUsage,
       "ringswitchTLSCardStatsMinFreeMem": ringswitchTLSCardStatsMinFreeMem,
       "ringswitchTLSCardStatsMaxFramesFwd": ringswitchTLSCardStatsMaxFramesFwd,
       "ringswitchTLSCardStatsResetState": ringswitchTLSCardStatsResetState,
       "ringswitchTLSCardARPFlush": ringswitchTLSCardARPFlush,
       "ringswitchTLSCardBootPRASecondsThreshold": ringswitchTLSCardBootPRASecondsThreshold,
       "ringswitchTLSCardBootPRAHopsThreshold": ringswitchTLSCardBootPRAHopsThreshold,
       "ringswitchTLSPortTable": ringswitchTLSPortTable,
       "ringswitchTLSPortEntry": ringswitchTLSPortEntry,
       "ringswitchTLSPortNum": ringswitchTLSPortNum,
       "ringswitchTLSPortName": ringswitchTLSPortName,
       "ringswitchTLSPortMTU": ringswitchTLSPortMTU,
       "ringswitchTLSPortEnable": ringswitchTLSPortEnable,
       "ringswitchTLSPortIpAddress": ringswitchTLSPortIpAddress,
       "ringswitchTLSPortIpSubnetMask": ringswitchTLSPortIpSubnetMask,
       "ringswitchTLSPortRIPRxType": ringswitchTLSPortRIPRxType,
       "ringswitchTLSPortRIPTxType": ringswitchTLSPortRIPTxType,
       "ringswitchTLSPortRIPFlags": ringswitchTLSPortRIPFlags,
       "ringswitchTLSPortIfArray": ringswitchTLSPortIfArray,
       "ringswitchTLSPortRIP2AuthType": ringswitchTLSPortRIP2AuthType,
       "ringswitchTLSPortRIP2AuthKey": ringswitchTLSPortRIP2AuthKey,
       "ringswitchTLSPortOSPFEnable": ringswitchTLSPortOSPFEnable,
       "ringswitchTLSPortOSPFAreaId": ringswitchTLSPortOSPFAreaId,
       "ringswitchTLSPortLegFlags": ringswitchTLSPortLegFlags,
       "ringswitchTLSPortOSPFAuthType": ringswitchTLSPortOSPFAuthType,
       "ringswitchTLSPortOSPFAuthMD5KeyId": ringswitchTLSPortOSPFAuthMD5KeyId,
       "ringswitchTLSPortOSPFAuthKey": ringswitchTLSPortOSPFAuthKey,
       "ringswitchTLSPortOSPFCost": ringswitchTLSPortOSPFCost,
       "ringswitchTLSPortOSPFPriority": ringswitchTLSPortOSPFPriority,
       "ringswitchTLSPortOSPFHelloInterval": ringswitchTLSPortOSPFHelloInterval,
       "ringswitchTLSPortOSPFDeadInterval": ringswitchTLSPortOSPFDeadInterval,
       "ringswitchTLSPortBootPFlags": ringswitchTLSPortBootPFlags,
       "ringswitchTLSStaticRouteTable": ringswitchTLSStaticRouteTable,
       "ringswitchTLSStaticRouteEntry": ringswitchTLSStaticRouteEntry,
       "ringswitchTLSStaticRouteCardNum": ringswitchTLSStaticRouteCardNum,
       "ringswitchTLSStaticRouteIpAddress": ringswitchTLSStaticRouteIpAddress,
       "ringswitchTLSStaticRouteMask": ringswitchTLSStaticRouteMask,
       "ringswitchTLSStaticRouteGateway": ringswitchTLSStaticRouteGateway,
       "ringswitchTLSStaticRouteMetric": ringswitchTLSStaticRouteMetric,
       "ringswitchTLSRIPNeighbourTable": ringswitchTLSRIPNeighbourTable,
       "ringswitchTLSRIPNeighbourEntry": ringswitchTLSRIPNeighbourEntry,
       "ringswitchTLSRIPNeighbourCardNum": ringswitchTLSRIPNeighbourCardNum,
       "ringswitchTLSRIPNeighbourIpAddress": ringswitchTLSRIPNeighbourIpAddress,
       "ringswitchTLSRIPNeighbourEnable": ringswitchTLSRIPNeighbourEnable,
       "ringswitchTLSRIPAdvertTable": ringswitchTLSRIPAdvertTable,
       "ringswitchTLSRIPAdvertEntry": ringswitchTLSRIPAdvertEntry,
       "ringswitchTLSRIPAdvertPortNum": ringswitchTLSRIPAdvertPortNum,
       "ringswitchTLSRIPAdvertIpAddress": ringswitchTLSRIPAdvertIpAddress,
       "ringswitchTLSRIPAdvertEnable": ringswitchTLSRIPAdvertEnable,
       "ringswitchTLSRIPRejectTable": ringswitchTLSRIPRejectTable,
       "ringswitchTLSRIPRejectEntry": ringswitchTLSRIPRejectEntry,
       "ringswitchTLSRIPRejectPortNum": ringswitchTLSRIPRejectPortNum,
       "ringswitchTLSRIPRejectIpAddress": ringswitchTLSRIPRejectIpAddress,
       "ringswitchTLSRIPRejectEnable": ringswitchTLSRIPRejectEnable,
       "ringswitchTLSOSPFAreaTable": ringswitchTLSOSPFAreaTable,
       "ringswitchTLSOSPFAreaEntry": ringswitchTLSOSPFAreaEntry,
       "ringswitchTLSOSPFAreaCardNum": ringswitchTLSOSPFAreaCardNum,
       "ringswitchTLSOSPFAreaId": ringswitchTLSOSPFAreaId,
       "ringswitchTLSOSPFAreaAddress": ringswitchTLSOSPFAreaAddress,
       "ringswitchTLSOSPFAreaAddressMask": ringswitchTLSOSPFAreaAddressMask,
       "ringswitchTLSOSPFAreaFlags": ringswitchTLSOSPFAreaFlags,
       "ringswitchTLSBootPRAServerTable": ringswitchTLSBootPRAServerTable,
       "ringswitchTLSBootPRAServerEntry": ringswitchTLSBootPRAServerEntry,
       "ringswitchTLSBootPRAServerCardNum": ringswitchTLSBootPRAServerCardNum,
       "ringswitchTLSBootPRAServerIpAddress": ringswitchTLSBootPRAServerIpAddress,
       "ringswitchTLSBootPRAServerName": ringswitchTLSBootPRAServerName,
       "ringswitchTLSBootPRAServerEnable": ringswitchTLSBootPRAServerEnable,
       "ringswitchTLSVRRPVRTRTable": ringswitchTLSVRRPVRTRTable,
       "ringswitchTLSVRRPVRTREntry": ringswitchTLSVRRPVRTREntry,
       "ringswitchTLSVRRPVRTRPortNum": ringswitchTLSVRRPVRTRPortNum,
       "ringswitchTLSVRRPVRTRIpAddress": ringswitchTLSVRRPVRTRIpAddress,
       "ringswitchTLSVRRPVRTRVRID": ringswitchTLSVRRPVRTRVRID,
       "ringswitchTLSVRRPVRTRMacAddress": ringswitchTLSVRRPVRTRMacAddress,
       "ringswitchTLSVRRPVRTREnable": ringswitchTLSVRRPVRTREnable,
       "ringswitchTLSVRRPVRTRAdvertInterval": ringswitchTLSVRRPVRTRAdvertInterval,
       "ringswitchTLSVRRPVRTRPriority": ringswitchTLSVRRPVRTRPriority,
       "ringswitchTLSVRRPVRTRAuthType": ringswitchTLSVRRPVRTRAuthType,
       "ringswitchTLSVRRPVRTRAuthKey": ringswitchTLSVRRPVRTRAuthKey,
       "ringswitchTLSVRRPVRTRAdvertDeadInterval": ringswitchTLSVRRPVRTRAdvertDeadInterval,
       "ringswitchEthernet": ringswitchEthernet,
       "ringswitchEthernetIfTable": ringswitchEthernetIfTable,
       "ringswitchEthernetIfEntry": ringswitchEthernetIfEntry,
       "ringswitchEthernetIfIndex": ringswitchEthernetIfIndex,
       "ringswitchEthernetIfIPXEthType": ringswitchEthernetIfIPXEthType,
       "ringswitchEthernetIfOperIPXEthType": ringswitchEthernetIfOperIPXEthType,
       "ringswitchEthernetIfIPXTRType": ringswitchEthernetIfIPXTRType,
       "ringswitchEthernetIfOperIPXTRType": ringswitchEthernetIfOperIPXTRType,
       "ringswitchEthernetIfIPXEnable": ringswitchEthernetIfIPXEnable,
       "ringswitchEthernetIfIPEnable": ringswitchEthernetIfIPEnable,
       "ringswitchEthernetIfAdminSpeed": ringswitchEthernetIfAdminSpeed,
       "ringswitchEthernetIfOperSpeed": ringswitchEthernetIfOperSpeed,
       "ringswitchEthernetIfAdminDuplexMode": ringswitchEthernetIfAdminDuplexMode,
       "ringswitchEthernetIfOperDuplexMode": ringswitchEthernetIfOperDuplexMode,
       "ringswitchEthernetIfIPMulticastType": ringswitchEthernetIfIPMulticastType,
       "ringswitchEthernetIfCacheClear": ringswitchEthernetIfCacheClear,
       "ringswitchEthernetIfSPTEncaps": ringswitchEthernetIfSPTEncaps,
       "ringswitchEthernetIfPriorityTagging": ringswitchEthernetIfPriorityTagging,
       "ringswitchEthernetIfPriorityTaggingVLANId": ringswitchEthernetIfPriorityTaggingVLANId,
       "ringswitchEthernetIfAdminIPXNetwork": ringswitchEthernetIfAdminIPXNetwork,
       "ringswitchEthernetIfOperIPXNetwork": ringswitchEthernetIfOperIPXNetwork,
       "ringswitchEthernetIfSTPBlockingTrapInfo": ringswitchEthernetIfSTPBlockingTrapInfo,
       "ringswitchEthernetIfAdminFlowCtrl": ringswitchEthernetIfAdminFlowCtrl,
       "ringswitchEthernetIfOperFlowCtrl": ringswitchEthernetIfOperFlowCtrl,
       "ringswitchEthernetIfAutoNegotiate": ringswitchEthernetIfAutoNegotiate,
       "ringswitchEthernetIfMediaType": ringswitchEthernetIfMediaType,
       "ringswitchEthernetIfAdminMaxFrameSize": ringswitchEthernetIfAdminMaxFrameSize,
       "ringswitchEthernetIfOperMaxFrameSize": ringswitchEthernetIfOperMaxFrameSize,
       "ringswitchEthernetXBDupAddrTable": ringswitchEthernetXBDupAddrTable,
       "ringswitchEthernetXBDupAddrEntry": ringswitchEthernetXBDupAddrEntry,
       "ringswitchEthernetXBDupAddrIfIndex": ringswitchEthernetXBDupAddrIfIndex,
       "ringswitchEthernetXBDupAddrIndex": ringswitchEthernetXBDupAddrIndex,
       "ringswitchEthernetXBDupAddrMacAddress": ringswitchEthernetXBDupAddrMacAddress,
       "ringswitchEthernetXBToTRNStatsTable": ringswitchEthernetXBToTRNStatsTable,
       "ringswitchEthernetXBToTRNStatsEntry": ringswitchEthernetXBToTRNStatsEntry,
       "ringswitchEthernetXBToTRNStatsIfIndex": ringswitchEthernetXBToTRNStatsIfIndex,
       "ringswitchEthernetXBToTRNStatsDiscSptEncapsBlock": ringswitchEthernetXBToTRNStatsDiscSptEncapsBlock,
       "ringswitchEthernetXBToTRNStatsDiscFilter": ringswitchEthernetXBToTRNStatsDiscFilter,
       "ringswitchEthernetXBToTRNStatsDiscBPDU": ringswitchEthernetXBToTRNStatsDiscBPDU,
       "ringswitchEthernetXBToTRNStatsDiscBPDUEncaps": ringswitchEthernetXBToTRNStatsDiscBPDUEncaps,
       "ringswitchEthernetXBToTRNStatsDiscTag8021qCfi": ringswitchEthernetXBToTRNStatsDiscTag8021qCfi,
       "ringswitchEthernetXBToTRNStatsDiscTag8021qVlan": ringswitchEthernetXBToTRNStatsDiscTag8021qVlan,
       "ringswitchEthernetXBToTRNStatsDiscBadRif": ringswitchEthernetXBToTRNStatsDiscBadRif,
       "ringswitchEthernetXBToTRNStatsDiscHopLimit": ringswitchEthernetXBToTRNStatsDiscHopLimit,
       "ringswitchEthernetXBToTRNStatsDiscDuplicateRin": ringswitchEthernetXBToTRNStatsDiscDuplicateRin,
       "ringswitchEthernetXBToTRNStatsDiscIPDisabled": ringswitchEthernetXBToTRNStatsDiscIPDisabled,
       "ringswitchEthernetXBToTRNStatsDiscARPDisabled": ringswitchEthernetXBToTRNStatsDiscARPDisabled,
       "ringswitchEthernetXBToTRNStatsDiscNCPCache": ringswitchEthernetXBToTRNStatsDiscNCPCache,
       "ringswitchEthernetXBToTRNStatsDiscIPXDisabled": ringswitchEthernetXBToTRNStatsDiscIPXDisabled,
       "ringswitchEthernetXBToTRNStatsDiscIPXTypeSnap": ringswitchEthernetXBToTRNStatsDiscIPXTypeSnap,
       "ringswitchEthernetXBToTRNStatsDiscIPXType8022": ringswitchEthernetXBToTRNStatsDiscIPXType8022,
       "ringswitchEthernetXBToTRNStatsDiscIPXType8023": ringswitchEthernetXBToTRNStatsDiscIPXType8023,
       "ringswitchEthernetXBToTRNStatsDiscIPXTypeDix": ringswitchEthernetXBToTRNStatsDiscIPXTypeDix,
       "ringswitchEthernetXBToTRNStatsNoFakeBuffer": ringswitchEthernetXBToTRNStatsNoFakeBuffer,
       "ringswitchEthernetXBToTRNStatsCacheFull": ringswitchEthernetXBToTRNStatsCacheFull,
       "ringswitchEthernetXBToTRNStatsFwdIPFrames": ringswitchEthernetXBToTRNStatsFwdIPFrames,
       "ringswitchEthernetXBToTRNStatsFwdIPMulticast": ringswitchEthernetXBToTRNStatsFwdIPMulticast,
       "ringswitchEthernetXBToTRNStatsFwdARPFrames": ringswitchEthernetXBToTRNStatsFwdARPFrames,
       "ringswitchEthernetXBToTRNStatsFwdIPXFrames": ringswitchEthernetXBToTRNStatsFwdIPXFrames,
       "ringswitchEthernetXBToTRNStatsFwdAARPPh1Frames": ringswitchEthernetXBToTRNStatsFwdAARPPh1Frames,
       "ringswitchEthernetXBToTRNStatsFwdAARPPh2Frames": ringswitchEthernetXBToTRNStatsFwdAARPPh2Frames,
       "ringswitchEthernetXBToTRNStatsFwdOtherEthFrames": ringswitchEthernetXBToTRNStatsFwdOtherEthFrames,
       "ringswitchEthernetXBToTRNStatsFwdZeroOUIFrames": ringswitchEthernetXBToTRNStatsFwdZeroOUIFrames,
       "ringswitchEthernetXBToTRNStatsFwdOtherDLCFrames": ringswitchEthernetXBToTRNStatsFwdOtherDLCFrames,
       "ringswitchEthernetXBToTRNStatsFwdBPDUEncaps": ringswitchEthernetXBToTRNStatsFwdBPDUEncaps,
       "ringswitchEthernetXBToTRNStatsFwdBPDUDecaps": ringswitchEthernetXBToTRNStatsFwdBPDUDecaps,
       "ringswitchEthernetXBFromTRNStatsTable": ringswitchEthernetXBFromTRNStatsTable,
       "ringswitchEthernetXBFromTRNStatsEntry": ringswitchEthernetXBFromTRNStatsEntry,
       "ringswitchEthernetXBFromTRNStatsIfIndex": ringswitchEthernetXBFromTRNStatsIfIndex,
       "ringswitchEthernetXBFromTRNStatsDiscTooBig": ringswitchEthernetXBFromTRNStatsDiscTooBig,
       "ringswitchEthernetXBFromTRNStatsDiscSptEncapsBlock": ringswitchEthernetXBFromTRNStatsDiscSptEncapsBlock,
       "ringswitchEthernetXBFromTRNStatsDiscFilter": ringswitchEthernetXBFromTRNStatsDiscFilter,
       "ringswitchEthernetXBFromTRNStatsDiscBPDU": ringswitchEthernetXBFromTRNStatsDiscBPDU,
       "ringswitchEthernetXBFromTRNStatsDiscBPDUEncaps": ringswitchEthernetXBFromTRNStatsDiscBPDUEncaps,
       "ringswitchEthernetXBFromTRNStatsDiscTag8021qCfi": ringswitchEthernetXBFromTRNStatsDiscTag8021qCfi,
       "ringswitchEthernetXBFromTRNStatsDiscTag8021qVlan": ringswitchEthernetXBFromTRNStatsDiscTag8021qVlan,
       "ringswitchEthernetXBFromTRNStatsDiscBadRIF": ringswitchEthernetXBFromTRNStatsDiscBadRIF,
       "ringswitchEthernetXBFromTRNStatsDiscZeroRingNum": ringswitchEthernetXBFromTRNStatsDiscZeroRingNum,
       "ringswitchEthernetXBFromTRNStatsDiscNonTermRIF": ringswitchEthernetXBFromTRNStatsDiscNonTermRIF,
       "ringswitchEthernetXBFromTRNStatsDiscIPDisabled": ringswitchEthernetXBFromTRNStatsDiscIPDisabled,
       "ringswitchEthernetXBFromTRNStatsDiscARPDisabled": ringswitchEthernetXBFromTRNStatsDiscARPDisabled,
       "ringswitchEthernetXBFromTRNStatsDiscIPCantFrag": ringswitchEthernetXBFromTRNStatsDiscIPCantFrag,
       "ringswitchEthernetXBFromTRNStatsDiscNCPCache": ringswitchEthernetXBFromTRNStatsDiscNCPCache,
       "ringswitchEthernetXBFromTRNStatsDiscIPXDisabled": ringswitchEthernetXBFromTRNStatsDiscIPXDisabled,
       "ringswitchEthernetXBFromTRNStatsDiscIPXTypeSnap": ringswitchEthernetXBFromTRNStatsDiscIPXTypeSnap,
       "ringswitchEthernetXBFromTRNStatsDiscIPXType8022": ringswitchEthernetXBFromTRNStatsDiscIPXType8022,
       "ringswitchEthernetXBFromTRNStatsCacheFull": ringswitchEthernetXBFromTRNStatsCacheFull,
       "ringswitchEthernetXBFromTRNStatsRIFCacheFull": ringswitchEthernetXBFromTRNStatsRIFCacheFull,
       "ringswitchEthernetXBFromTRNStatsFwdIPFrames": ringswitchEthernetXBFromTRNStatsFwdIPFrames,
       "ringswitchEthernetXBFromTRNStatsFwdIPFragmented": ringswitchEthernetXBFromTRNStatsFwdIPFragmented,
       "ringswitchEthernetXBFromTRNStatsFwdIPMulticast": ringswitchEthernetXBFromTRNStatsFwdIPMulticast,
       "ringswitchEthernetXBFromTRNStatsFwdARPFrames": ringswitchEthernetXBFromTRNStatsFwdARPFrames,
       "ringswitchEthernetXBFromTRNStatsFwdIPXFrames": ringswitchEthernetXBFromTRNStatsFwdIPXFrames,
       "ringswitchEthernetXBFromTRNStatsFwdAARPPh1Frames": ringswitchEthernetXBFromTRNStatsFwdAARPPh1Frames,
       "ringswitchEthernetXBFromTRNStatsFwdAARPPh2Frames": ringswitchEthernetXBFromTRNStatsFwdAARPPh2Frames,
       "ringswitchEthernetXBFromTRNStatsFwdTunnel8021hFrames": ringswitchEthernetXBFromTRNStatsFwdTunnel8021hFrames,
       "ringswitchEthernetXBFromTRNStatsFwdZeroOUISnapFrames": ringswitchEthernetXBFromTRNStatsFwdZeroOUISnapFrames,
       "ringswitchEthernetXBFromTRNStatsFwdOtherDLCFrames": ringswitchEthernetXBFromTRNStatsFwdOtherDLCFrames,
       "ringswitchEthernetXBFromTRNStatsFwdBPDUDecaps": ringswitchEthernetXBFromTRNStatsFwdBPDUDecaps,
       "ringswitchEthernetXBFromTRNStatsFwdBPDUEncaps": ringswitchEthernetXBFromTRNStatsFwdBPDUEncaps,
       "ringswitchEthernetExtPhysStatsTable": ringswitchEthernetExtPhysStatsTable,
       "ringswitchEthernetExtPhysStatsEntry": ringswitchEthernetExtPhysStatsEntry,
       "ringswitchEthernetExtPhysStatsIfIndex": ringswitchEthernetExtPhysStatsIfIndex,
       "ringswitchEthernetExtPhysStatsRxDataErrors": ringswitchEthernetExtPhysStatsRxDataErrors,
       "ringswitchEthernetExtPhysStatsRxSequenceErrors": ringswitchEthernetExtPhysStatsRxSequenceErrors,
       "ringswitchEthernetExtPhysStatsRxCarrierExtErrors": ringswitchEthernetExtPhysStatsRxCarrierExtErrors,
       "ringswitchEthernetExtPhysStatsXonRxFrames": ringswitchEthernetExtPhysStatsXonRxFrames,
       "ringswitchEthernetExtPhysStatsXonTxFrames": ringswitchEthernetExtPhysStatsXonTxFrames,
       "ringswitchEthernetExtPhysStatsXoffRxFrames": ringswitchEthernetExtPhysStatsXoffRxFrames,
       "ringswitchEthernetExtPhysStatsXoffTxFrames": ringswitchEthernetExtPhysStatsXoffTxFrames}
)
