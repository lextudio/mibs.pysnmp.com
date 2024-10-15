# SNMP MIB module (REDLINE-AN80I-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDLINE-AN80I-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:28 2024
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

(redlineTransmission,) = mibBuilder.importSymbols(
    "REDLINE-MIB",
    "redlineTransmission")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

redlineAn80iIfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2)
)
redlineAn80iIfMib.setRevisions(
        ("2005-11-28 15:43",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RedlineAn80iIfTrapDefinitions_ObjectIdentity = ObjectIdentity
redlineAn80iIfTrapDefinitions = _RedlineAn80iIfTrapDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 0)
)
_RedlineAn80iIfPtpObjects_ObjectIdentity = ObjectIdentity
redlineAn80iIfPtpObjects = _RedlineAn80iIfPtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1)
)
_RedlineAn80iIfPtpLinkConfig_ObjectIdentity = ObjectIdentity
redlineAn80iIfPtpLinkConfig = _RedlineAn80iIfPtpLinkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 1)
)


class _An80iIfEncryptionControl_Type(Integer32):
    """Custom type an80iIfEncryptionControl based on Integer32"""
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
        *(("aes128", 3),
          ("aes192", 4),
          ("aes256", 5),
          ("off", 1),
          ("redline", 2))
    )


_An80iIfEncryptionControl_Type.__name__ = "Integer32"
_An80iIfEncryptionControl_Object = MibScalar
an80iIfEncryptionControl = _An80iIfEncryptionControl_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 1, 1),
    _An80iIfEncryptionControl_Type()
)
an80iIfEncryptionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iIfEncryptionControl.setStatus("current")


class _An80iIfModReduction_Type(Integer32):
    """Custom type an80iIfModReduction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_An80iIfModReduction_Type.__name__ = "Integer32"
_An80iIfModReduction_Object = MibScalar
an80iIfModReduction = _An80iIfModReduction_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 1, 2),
    _An80iIfModReduction_Type()
)
an80iIfModReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iIfModReduction.setStatus("current")


class _An80iIfAdaptiveMod_Type(Integer32):
    """Custom type an80iIfAdaptiveMod based on Integer32"""
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


_An80iIfAdaptiveMod_Type.__name__ = "Integer32"
_An80iIfAdaptiveMod_Object = MibScalar
an80iIfAdaptiveMod = _An80iIfAdaptiveMod_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 1, 3),
    _An80iIfAdaptiveMod_Type()
)
an80iIfAdaptiveMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iIfAdaptiveMod.setStatus("current")


class _An80iIfUncodedBurstRate_Type(Integer32):
    """Custom type an80iIfUncodedBurstRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_An80iIfUncodedBurstRate_Type.__name__ = "Integer32"
_An80iIfUncodedBurstRate_Object = MibScalar
an80iIfUncodedBurstRate = _An80iIfUncodedBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 1, 4),
    _An80iIfUncodedBurstRate_Type()
)
an80iIfUncodedBurstRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iIfUncodedBurstRate.setStatus("current")
_An80iIfEncryptionKey_Type = OctetString
_An80iIfEncryptionKey_Object = MibScalar
an80iIfEncryptionKey = _An80iIfEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 1, 5),
    _An80iIfEncryptionKey_Type()
)
an80iIfEncryptionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iIfEncryptionKey.setStatus("current")


class _An80iIfPacketRetransControl_Type(Integer32):
    """Custom type an80iIfPacketRetransControl based on Integer32"""
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


_An80iIfPacketRetransControl_Type.__name__ = "Integer32"
_An80iIfPacketRetransControl_Object = MibScalar
an80iIfPacketRetransControl = _An80iIfPacketRetransControl_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 1, 6),
    _An80iIfPacketRetransControl_Type()
)
an80iIfPacketRetransControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iIfPacketRetransControl.setStatus("current")


class _An80iIfLinkLenMode_Type(Integer32):
    """Custom type an80iIfLinkLenMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_An80iIfLinkLenMode_Type.__name__ = "Integer32"
_An80iIfLinkLenMode_Object = MibScalar
an80iIfLinkLenMode = _An80iIfLinkLenMode_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 1, 7),
    _An80iIfLinkLenMode_Type()
)
an80iIfLinkLenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iIfLinkLenMode.setStatus("current")
_An80iIfLinkLength_Type = Integer32
_An80iIfLinkLength_Object = MibScalar
an80iIfLinkLength = _An80iIfLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 1, 8),
    _An80iIfLinkLength_Type()
)
an80iIfLinkLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iIfLinkLength.setStatus("current")
if mibBuilder.loadTexts:
    an80iIfLinkLength.setUnits("Km")
_An80iIfCalcLinkDst_Type = Integer32
_An80iIfCalcLinkDst_Object = MibScalar
an80iIfCalcLinkDst = _An80iIfCalcLinkDst_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 1, 9),
    _An80iIfCalcLinkDst_Type()
)
an80iIfCalcLinkDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfCalcLinkDst.setStatus("current")
if mibBuilder.loadTexts:
    an80iIfCalcLinkDst.setUnits("Km")


class _An80iIfLinkName_Type(DisplayString):
    """Custom type an80iIfLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_An80iIfLinkName_Type.__name__ = "DisplayString"
_An80iIfLinkName_Object = MibScalar
an80iIfLinkName = _An80iIfLinkName_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 1, 10),
    _An80iIfLinkName_Type()
)
an80iIfLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iIfLinkName.setStatus("current")
_RedlineAn80iIfPtpLinkStats_ObjectIdentity = ObjectIdentity
redlineAn80iIfPtpLinkStats = _RedlineAn80iIfPtpLinkStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 2)
)
_An80iIfCurrUncodedBurstRate_Type = Unsigned32
_An80iIfCurrUncodedBurstRate_Object = MibScalar
an80iIfCurrUncodedBurstRate = _An80iIfCurrUncodedBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 2, 1),
    _An80iIfCurrUncodedBurstRate_Type()
)
an80iIfCurrUncodedBurstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfCurrUncodedBurstRate.setStatus("current")


class _An80iIfPtpLinkStatus_Type(Integer32):
    """Custom type an80iIfPtpLinkStatus based on Integer32"""
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


_An80iIfPtpLinkStatus_Type.__name__ = "Integer32"
_An80iIfPtpLinkStatus_Object = MibScalar
an80iIfPtpLinkStatus = _An80iIfPtpLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 2, 2),
    _An80iIfPtpLinkStatus_Type()
)
an80iIfPtpLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPtpLinkStatus.setStatus("current")
_An80iIfRxPackets_Type = Counter64
_An80iIfRxPackets_Object = MibScalar
an80iIfRxPackets = _An80iIfRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 2, 3),
    _An80iIfRxPackets_Type()
)
an80iIfRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfRxPackets.setStatus("current")
_An80iIfRxPacketsReTx_Type = Counter64
_An80iIfRxPacketsReTx_Object = MibScalar
an80iIfRxPacketsReTx = _An80iIfRxPacketsReTx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 2, 4),
    _An80iIfRxPacketsReTx_Type()
)
an80iIfRxPacketsReTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfRxPacketsReTx.setStatus("current")
_An80iIfRxPacketsDisc_Type = Counter64
_An80iIfRxPacketsDisc_Object = MibScalar
an80iIfRxPacketsDisc = _An80iIfRxPacketsDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 2, 5),
    _An80iIfRxPacketsDisc_Type()
)
an80iIfRxPacketsDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfRxPacketsDisc.setStatus("current")
_An80iIfTxPackets_Type = Counter64
_An80iIfTxPackets_Object = MibScalar
an80iIfTxPackets = _An80iIfTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 2, 6),
    _An80iIfTxPackets_Type()
)
an80iIfTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfTxPackets.setStatus("current")
_An80iIfTxPacketsReTx_Type = Counter64
_An80iIfTxPacketsReTx_Object = MibScalar
an80iIfTxPacketsReTx = _An80iIfTxPacketsReTx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 2, 7),
    _An80iIfTxPacketsReTx_Type()
)
an80iIfTxPacketsReTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfTxPacketsReTx.setStatus("current")
_An80iIfTxPacketsDisc_Type = Counter64
_An80iIfTxPacketsDisc_Object = MibScalar
an80iIfTxPacketsDisc = _An80iIfTxPacketsDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 2, 8),
    _An80iIfTxPacketsDisc_Type()
)
an80iIfTxPacketsDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfTxPacketsDisc.setStatus("current")
_An80iIfRssiMin_Type = Integer32
_An80iIfRssiMin_Object = MibScalar
an80iIfRssiMin = _An80iIfRssiMin_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 2, 9),
    _An80iIfRssiMin_Type()
)
an80iIfRssiMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfRssiMin.setStatus("current")
_An80iIfRssiMean_Type = Integer32
_An80iIfRssiMean_Object = MibScalar
an80iIfRssiMean = _An80iIfRssiMean_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 2, 10),
    _An80iIfRssiMean_Type()
)
an80iIfRssiMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfRssiMean.setStatus("current")
_An80iIfRssiMax_Type = Integer32
_An80iIfRssiMax_Object = MibScalar
an80iIfRssiMax = _An80iIfRssiMax_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 2, 11),
    _An80iIfRssiMax_Type()
)
an80iIfRssiMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfRssiMax.setStatus("current")
_An80iIfAvrSinAdr_Type = Integer32
_An80iIfAvrSinAdr_Object = MibScalar
an80iIfAvrSinAdr = _An80iIfAvrSinAdr_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 1, 2, 12),
    _An80iIfAvrSinAdr_Type()
)
an80iIfAvrSinAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfAvrSinAdr.setStatus("current")
_RedlineAn80iIfPmpObjects_ObjectIdentity = ObjectIdentity
redlineAn80iIfPmpObjects = _RedlineAn80iIfPmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2)
)
_RedlineAn80iIfPmpSsObjects_ObjectIdentity = ObjectIdentity
redlineAn80iIfPmpSsObjects = _RedlineAn80iIfPmpSsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 1)
)
_An80iIfLastMissedMacAddress_Type = MacAddress
_An80iIfLastMissedMacAddress_Object = MibScalar
an80iIfLastMissedMacAddress = _An80iIfLastMissedMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 1, 1),
    _An80iIfLastMissedMacAddress_Type()
)
an80iIfLastMissedMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfLastMissedMacAddress.setStatus("current")
_An80iIfLastRegistMacAddress_Type = MacAddress
_An80iIfLastRegistMacAddress_Object = MibScalar
an80iIfLastRegistMacAddress = _An80iIfLastRegistMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 1, 2),
    _An80iIfLastRegistMacAddress_Type()
)
an80iIfLastRegistMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfLastRegistMacAddress.setStatus("current")
_An80iIfDenyMacAddress_Type = MacAddress
_An80iIfDenyMacAddress_Object = MibScalar
an80iIfDenyMacAddress = _An80iIfDenyMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 1, 3),
    _An80iIfDenyMacAddress_Type()
)
an80iIfDenyMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an80iIfDenyMacAddress.setStatus("current")


class _An80iIfLastRegistLinkId_Type(Integer32):
    """Custom type an80iIfLastRegistLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_An80iIfLastRegistLinkId_Type.__name__ = "Integer32"
_An80iIfLastRegistLinkId_Object = MibScalar
an80iIfLastRegistLinkId = _An80iIfLastRegistLinkId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 1, 4),
    _An80iIfLastRegistLinkId_Type()
)
an80iIfLastRegistLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfLastRegistLinkId.setStatus("current")
_An80iIfPmpLinkConfigTable_Object = MibTable
an80iIfPmpLinkConfigTable = _An80iIfPmpLinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 2)
)
if mibBuilder.loadTexts:
    an80iIfPmpLinkConfigTable.setStatus("current")
_An80iIfPmpLinkConfigEntry_Object = MibTableRow
an80iIfPmpLinkConfigEntry = _An80iIfPmpLinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 2, 1)
)
an80iIfPmpLinkConfigEntry.setIndexNames(
    (0, "REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkId"),
)
if mibBuilder.loadTexts:
    an80iIfPmpLinkConfigEntry.setStatus("current")


class _An80iIfPmpLinkId_Type(Integer32):
    """Custom type an80iIfPmpLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1023),
    )


_An80iIfPmpLinkId_Type.__name__ = "Integer32"
_An80iIfPmpLinkId_Object = MibTableColumn
an80iIfPmpLinkId = _An80iIfPmpLinkId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 2, 1, 1),
    _An80iIfPmpLinkId_Type()
)
an80iIfPmpLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    an80iIfPmpLinkId.setStatus("current")


class _An80iIfPmpLinkName_Type(DisplayString):
    """Custom type an80iIfPmpLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_An80iIfPmpLinkName_Type.__name__ = "DisplayString"
_An80iIfPmpLinkName_Object = MibTableColumn
an80iIfPmpLinkName = _An80iIfPmpLinkName_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 2, 1, 2),
    _An80iIfPmpLinkName_Type()
)
an80iIfPmpLinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpLinkName.setStatus("current")
_An80iIfPmpLinkPeerMacAddress_Type = MacAddress
_An80iIfPmpLinkPeerMacAddress_Object = MibTableColumn
an80iIfPmpLinkPeerMacAddress = _An80iIfPmpLinkPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 2, 1, 3),
    _An80iIfPmpLinkPeerMacAddress_Type()
)
an80iIfPmpLinkPeerMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpLinkPeerMacAddress.setStatus("current")
_An80iIfPmpLinkULBurstRate_Type = Unsigned32
_An80iIfPmpLinkULBurstRate_Object = MibTableColumn
an80iIfPmpLinkULBurstRate = _An80iIfPmpLinkULBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 2, 1, 4),
    _An80iIfPmpLinkULBurstRate_Type()
)
an80iIfPmpLinkULBurstRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpLinkULBurstRate.setStatus("current")
_An80iIfPmpLinkDLBurstRate_Type = Unsigned32
_An80iIfPmpLinkDLBurstRate_Object = MibTableColumn
an80iIfPmpLinkDLBurstRate = _An80iIfPmpLinkDLBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 2, 1, 5),
    _An80iIfPmpLinkDLBurstRate_Type()
)
an80iIfPmpLinkDLBurstRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpLinkDLBurstRate.setStatus("current")
_An80iIfPmpLinkConfigStatus_Type = RowStatus
_An80iIfPmpLinkConfigStatus_Object = MibTableColumn
an80iIfPmpLinkConfigStatus = _An80iIfPmpLinkConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 2, 1, 6),
    _An80iIfPmpLinkConfigStatus_Type()
)
an80iIfPmpLinkConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpLinkConfigStatus.setStatus("current")
_An80iIfPmpLinkStatsTable_Object = MibTable
an80iIfPmpLinkStatsTable = _An80iIfPmpLinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3)
)
if mibBuilder.loadTexts:
    an80iIfPmpLinkStatsTable.setStatus("current")
_An80iIfPmpLinkStatsEntry_Object = MibTableRow
an80iIfPmpLinkStatsEntry = _An80iIfPmpLinkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1)
)
an80iIfPmpLinkStatsEntry.setIndexNames(
    (0, "REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkId"),
)
if mibBuilder.loadTexts:
    an80iIfPmpLinkStatsEntry.setStatus("current")


class _An80iIfPmpLinkStatus_Type(Integer32):
    """Custom type an80iIfPmpLinkStatus based on Integer32"""
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


_An80iIfPmpLinkStatus_Type.__name__ = "Integer32"
_An80iIfPmpLinkStatus_Object = MibTableColumn
an80iIfPmpLinkStatus = _An80iIfPmpLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 1),
    _An80iIfPmpLinkStatus_Type()
)
an80iIfPmpLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkStatus.setStatus("current")
_An80iIfPmpLinkStatusCode_Type = Integer32
_An80iIfPmpLinkStatusCode_Object = MibTableColumn
an80iIfPmpLinkStatusCode = _An80iIfPmpLinkStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 2),
    _An80iIfPmpLinkStatusCode_Type()
)
an80iIfPmpLinkStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkStatusCode.setStatus("current")
_An80iIfRegPmpLinkConns_Type = Integer32
_An80iIfRegPmpLinkConns_Object = MibTableColumn
an80iIfRegPmpLinkConns = _An80iIfRegPmpLinkConns_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 3),
    _An80iIfRegPmpLinkConns_Type()
)
an80iIfRegPmpLinkConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfRegPmpLinkConns.setStatus("current")
_An80iIfPmpLinkUpTime_Type = TimeTicks
_An80iIfPmpLinkUpTime_Object = MibTableColumn
an80iIfPmpLinkUpTime = _An80iIfPmpLinkUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 4),
    _An80iIfPmpLinkUpTime_Type()
)
an80iIfPmpLinkUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkUpTime.setStatus("current")
_An80iIfPmpLinkLostCount_Type = Counter32
_An80iIfPmpLinkLostCount_Object = MibTableColumn
an80iIfPmpLinkLostCount = _An80iIfPmpLinkLostCount_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 5),
    _An80iIfPmpLinkLostCount_Type()
)
an80iIfPmpLinkLostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkLostCount.setStatus("current")
_An80iIfPmpLinkCurrDLUncBurstRate_Type = Unsigned32
_An80iIfPmpLinkCurrDLUncBurstRate_Object = MibTableColumn
an80iIfPmpLinkCurrDLUncBurstRate = _An80iIfPmpLinkCurrDLUncBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 6),
    _An80iIfPmpLinkCurrDLUncBurstRate_Type()
)
an80iIfPmpLinkCurrDLUncBurstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkCurrDLUncBurstRate.setStatus("current")
_An80iIfPmpLinkDLRssi_Type = Integer32
_An80iIfPmpLinkDLRssi_Object = MibTableColumn
an80iIfPmpLinkDLRssi = _An80iIfPmpLinkDLRssi_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 7),
    _An80iIfPmpLinkDLRssi_Type()
)
an80iIfPmpLinkDLRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkDLRssi.setStatus("current")
_An80iIfPmpLinkDLSinAdr_Type = Integer32
_An80iIfPmpLinkDLSinAdr_Object = MibTableColumn
an80iIfPmpLinkDLSinAdr = _An80iIfPmpLinkDLSinAdr_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 8),
    _An80iIfPmpLinkDLSinAdr_Type()
)
an80iIfPmpLinkDLSinAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkDLSinAdr.setStatus("current")
_An80iIfPmpLinkDLLostFrm_Type = Counter64
_An80iIfPmpLinkDLLostFrm_Object = MibTableColumn
an80iIfPmpLinkDLLostFrm = _An80iIfPmpLinkDLLostFrm_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 9),
    _An80iIfPmpLinkDLLostFrm_Type()
)
an80iIfPmpLinkDLLostFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkDLLostFrm.setStatus("current")
_An80iIfPmpLinkDLBlksTot_Type = Counter64
_An80iIfPmpLinkDLBlksTot_Object = MibTableColumn
an80iIfPmpLinkDLBlksTot = _An80iIfPmpLinkDLBlksTot_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 10),
    _An80iIfPmpLinkDLBlksTot_Type()
)
an80iIfPmpLinkDLBlksTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkDLBlksTot.setStatus("current")
_An80iIfPmpLinkDLBlksRetr_Type = Counter64
_An80iIfPmpLinkDLBlksRetr_Object = MibTableColumn
an80iIfPmpLinkDLBlksRetr = _An80iIfPmpLinkDLBlksRetr_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 11),
    _An80iIfPmpLinkDLBlksRetr_Type()
)
an80iIfPmpLinkDLBlksRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkDLBlksRetr.setStatus("current")
_An80iIfPmpLinkDLBlksDisc_Type = Counter64
_An80iIfPmpLinkDLBlksDisc_Object = MibTableColumn
an80iIfPmpLinkDLBlksDisc = _An80iIfPmpLinkDLBlksDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 12),
    _An80iIfPmpLinkDLBlksDisc_Type()
)
an80iIfPmpLinkDLBlksDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkDLBlksDisc.setStatus("current")
_An80iIfPmpLinkCurrULUncBurstRate_Type = Unsigned32
_An80iIfPmpLinkCurrULUncBurstRate_Object = MibTableColumn
an80iIfPmpLinkCurrULUncBurstRate = _An80iIfPmpLinkCurrULUncBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 13),
    _An80iIfPmpLinkCurrULUncBurstRate_Type()
)
an80iIfPmpLinkCurrULUncBurstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkCurrULUncBurstRate.setStatus("current")
if mibBuilder.loadTexts:
    an80iIfPmpLinkCurrULUncBurstRate.setUnits("Mb/s")
_An80iIfPmpLinkULRssi_Type = Integer32
_An80iIfPmpLinkULRssi_Object = MibTableColumn
an80iIfPmpLinkULRssi = _An80iIfPmpLinkULRssi_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 14),
    _An80iIfPmpLinkULRssi_Type()
)
an80iIfPmpLinkULRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkULRssi.setStatus("current")
_An80iIfPmpLinkULSinAdr_Type = Integer32
_An80iIfPmpLinkULSinAdr_Object = MibTableColumn
an80iIfPmpLinkULSinAdr = _An80iIfPmpLinkULSinAdr_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 15),
    _An80iIfPmpLinkULSinAdr_Type()
)
an80iIfPmpLinkULSinAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkULSinAdr.setStatus("current")
_An80iIfPmpLinkULLostFrm_Type = Counter64
_An80iIfPmpLinkULLostFrm_Object = MibTableColumn
an80iIfPmpLinkULLostFrm = _An80iIfPmpLinkULLostFrm_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 16),
    _An80iIfPmpLinkULLostFrm_Type()
)
an80iIfPmpLinkULLostFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkULLostFrm.setStatus("current")
_An80iIfPmpLinkULBlksTot_Type = Counter64
_An80iIfPmpLinkULBlksTot_Object = MibTableColumn
an80iIfPmpLinkULBlksTot = _An80iIfPmpLinkULBlksTot_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 17),
    _An80iIfPmpLinkULBlksTot_Type()
)
an80iIfPmpLinkULBlksTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkULBlksTot.setStatus("current")
_An80iIfPmpLinkULBlksRetr_Type = Counter64
_An80iIfPmpLinkULBlksRetr_Object = MibTableColumn
an80iIfPmpLinkULBlksRetr = _An80iIfPmpLinkULBlksRetr_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 18),
    _An80iIfPmpLinkULBlksRetr_Type()
)
an80iIfPmpLinkULBlksRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkULBlksRetr.setStatus("current")
_An80iIfPmpLinkULBlksDisc_Type = Counter64
_An80iIfPmpLinkULBlksDisc_Object = MibTableColumn
an80iIfPmpLinkULBlksDisc = _An80iIfPmpLinkULBlksDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 19),
    _An80iIfPmpLinkULBlksDisc_Type()
)
an80iIfPmpLinkULBlksDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkULBlksDisc.setStatus("current")
_An80iIfPmpLinkStatsStatus_Type = RowStatus
_An80iIfPmpLinkStatsStatus_Object = MibTableColumn
an80iIfPmpLinkStatsStatus = _An80iIfPmpLinkStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 3, 1, 20),
    _An80iIfPmpLinkStatsStatus_Type()
)
an80iIfPmpLinkStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpLinkStatsStatus.setStatus("current")
_An80iIfPmpGroupConfigTable_Object = MibTable
an80iIfPmpGroupConfigTable = _An80iIfPmpGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 4)
)
if mibBuilder.loadTexts:
    an80iIfPmpGroupConfigTable.setStatus("current")
_An80iIfPmpGroupConfigEntry_Object = MibTableRow
an80iIfPmpGroupConfigEntry = _An80iIfPmpGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 4, 1)
)
an80iIfPmpGroupConfigEntry.setIndexNames(
    (0, "REDLINE-AN80I-IF-MIB", "an80iIfPmpGroupId"),
)
if mibBuilder.loadTexts:
    an80iIfPmpGroupConfigEntry.setStatus("current")


class _An80iIfPmpGroupId_Type(Integer32):
    """Custom type an80iIfPmpGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1023),
    )


_An80iIfPmpGroupId_Type.__name__ = "Integer32"
_An80iIfPmpGroupId_Object = MibTableColumn
an80iIfPmpGroupId = _An80iIfPmpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 4, 1, 1),
    _An80iIfPmpGroupId_Type()
)
an80iIfPmpGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    an80iIfPmpGroupId.setStatus("current")


class _An80iIfPmpGroupName_Type(DisplayString):
    """Custom type an80iIfPmpGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_An80iIfPmpGroupName_Type.__name__ = "DisplayString"
_An80iIfPmpGroupName_Object = MibTableColumn
an80iIfPmpGroupName = _An80iIfPmpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 4, 1, 2),
    _An80iIfPmpGroupName_Type()
)
an80iIfPmpGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpGroupName.setStatus("current")


class _An80iIfPmpGroupTaggingControl_Type(Integer32):
    """Custom type an80iIfPmpGroupTaggingControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passThrough", 1),
          ("tagged", 2))
    )


_An80iIfPmpGroupTaggingControl_Type.__name__ = "Integer32"
_An80iIfPmpGroupTaggingControl_Object = MibTableColumn
an80iIfPmpGroupTaggingControl = _An80iIfPmpGroupTaggingControl_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 4, 1, 3),
    _An80iIfPmpGroupTaggingControl_Type()
)
an80iIfPmpGroupTaggingControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpGroupTaggingControl.setStatus("current")


class _An80iIfPmpGroupVlanId_Type(Integer32):
    """Custom type an80iIfPmpGroupVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_An80iIfPmpGroupVlanId_Type.__name__ = "Integer32"
_An80iIfPmpGroupVlanId_Object = MibTableColumn
an80iIfPmpGroupVlanId = _An80iIfPmpGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 4, 1, 4),
    _An80iIfPmpGroupVlanId_Type()
)
an80iIfPmpGroupVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpGroupVlanId.setStatus("current")


class _An80iIfPmpGroupDefPriority_Type(Integer32):
    """Custom type an80iIfPmpGroupDefPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_An80iIfPmpGroupDefPriority_Type.__name__ = "Integer32"
_An80iIfPmpGroupDefPriority_Object = MibTableColumn
an80iIfPmpGroupDefPriority = _An80iIfPmpGroupDefPriority_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 4, 1, 5),
    _An80iIfPmpGroupDefPriority_Type()
)
an80iIfPmpGroupDefPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpGroupDefPriority.setStatus("current")


class _An80iIfPmpGroupSCEtherControl_Type(Integer32):
    """Custom type an80iIfPmpGroupSCEtherControl based on Integer32"""
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


_An80iIfPmpGroupSCEtherControl_Type.__name__ = "Integer32"
_An80iIfPmpGroupSCEtherControl_Object = MibTableColumn
an80iIfPmpGroupSCEtherControl = _An80iIfPmpGroupSCEtherControl_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 4, 1, 6),
    _An80iIfPmpGroupSCEtherControl_Type()
)
an80iIfPmpGroupSCEtherControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpGroupSCEtherControl.setStatus("current")


class _An80iIfPmpGroupQosLevel_Type(Integer32):
    """Custom type an80iIfPmpGroupQosLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 53),
    )


_An80iIfPmpGroupQosLevel_Type.__name__ = "Integer32"
_An80iIfPmpGroupQosLevel_Object = MibTableColumn
an80iIfPmpGroupQosLevel = _An80iIfPmpGroupQosLevel_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 4, 1, 7),
    _An80iIfPmpGroupQosLevel_Type()
)
an80iIfPmpGroupQosLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpGroupQosLevel.setStatus("current")
_An80iIfPmpGroupConfigStatus_Type = RowStatus
_An80iIfPmpGroupConfigStatus_Object = MibTableColumn
an80iIfPmpGroupConfigStatus = _An80iIfPmpGroupConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 4, 1, 8),
    _An80iIfPmpGroupConfigStatus_Type()
)
an80iIfPmpGroupConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpGroupConfigStatus.setStatus("current")


class _An80iIfPmpGroupRate_Type(Integer32):
    """Custom type an80iIfPmpGroupRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_An80iIfPmpGroupRate_Type.__name__ = "Integer32"
_An80iIfPmpGroupRate_Object = MibTableColumn
an80iIfPmpGroupRate = _An80iIfPmpGroupRate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 4, 1, 9),
    _An80iIfPmpGroupRate_Type()
)
an80iIfPmpGroupRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpGroupRate.setStatus("current")


class _An80iIfPmpGroupSStoSSMulticast_Type(Integer32):
    """Custom type an80iIfPmpGroupSStoSSMulticast based on Integer32"""
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


_An80iIfPmpGroupSStoSSMulticast_Type.__name__ = "Integer32"
_An80iIfPmpGroupSStoSSMulticast_Object = MibTableColumn
an80iIfPmpGroupSStoSSMulticast = _An80iIfPmpGroupSStoSSMulticast_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 4, 1, 10),
    _An80iIfPmpGroupSStoSSMulticast_Type()
)
an80iIfPmpGroupSStoSSMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpGroupSStoSSMulticast.setStatus("current")
_An80iIfPmpGroupStatsTable_Object = MibTable
an80iIfPmpGroupStatsTable = _An80iIfPmpGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 5)
)
if mibBuilder.loadTexts:
    an80iIfPmpGroupStatsTable.setStatus("current")
_An80iIfPmpGroupStatsEntry_Object = MibTableRow
an80iIfPmpGroupStatsEntry = _An80iIfPmpGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 5, 1)
)
an80iIfPmpGroupStatsEntry.setIndexNames(
    (0, "REDLINE-AN80I-IF-MIB", "an80iIfPmpGroupId"),
)
if mibBuilder.loadTexts:
    an80iIfPmpGroupStatsEntry.setStatus("current")
_An80iIfPmpGroupPacketsTx_Type = Counter64
_An80iIfPmpGroupPacketsTx_Object = MibTableColumn
an80iIfPmpGroupPacketsTx = _An80iIfPmpGroupPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 5, 1, 1),
    _An80iIfPmpGroupPacketsTx_Type()
)
an80iIfPmpGroupPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpGroupPacketsTx.setStatus("current")
_An80iIfPmpGroupPacketDisc_Type = Counter64
_An80iIfPmpGroupPacketDisc_Object = MibTableColumn
an80iIfPmpGroupPacketDisc = _An80iIfPmpGroupPacketDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 5, 1, 2),
    _An80iIfPmpGroupPacketDisc_Type()
)
an80iIfPmpGroupPacketDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpGroupPacketDisc.setStatus("current")
_An80iIfPmpGroupStatsStatus_Type = RowStatus
_An80iIfPmpGroupStatsStatus_Object = MibTableColumn
an80iIfPmpGroupStatsStatus = _An80iIfPmpGroupStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 5, 1, 3),
    _An80iIfPmpGroupStatsStatus_Type()
)
an80iIfPmpGroupStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpGroupStatsStatus.setStatus("current")
_An80iIfPmpConnConfigTable_Object = MibTable
an80iIfPmpConnConfigTable = _An80iIfPmpConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 6)
)
if mibBuilder.loadTexts:
    an80iIfPmpConnConfigTable.setStatus("current")
_An80iIfPmpConnConfigEntry_Object = MibTableRow
an80iIfPmpConnConfigEntry = _An80iIfPmpConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 6, 1)
)
an80iIfPmpConnConfigEntry.setIndexNames(
    (0, "REDLINE-AN80I-IF-MIB", "an80iIfPmpConnId"),
)
if mibBuilder.loadTexts:
    an80iIfPmpConnConfigEntry.setStatus("current")


class _An80iIfPmpConnId_Type(Integer32):
    """Custom type an80iIfPmpConnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1023),
    )


_An80iIfPmpConnId_Type.__name__ = "Integer32"
_An80iIfPmpConnId_Object = MibTableColumn
an80iIfPmpConnId = _An80iIfPmpConnId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 6, 1, 1),
    _An80iIfPmpConnId_Type()
)
an80iIfPmpConnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    an80iIfPmpConnId.setStatus("current")


class _An80iIfPmpConnName_Type(DisplayString):
    """Custom type an80iIfPmpConnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_An80iIfPmpConnName_Type.__name__ = "DisplayString"
_An80iIfPmpConnName_Object = MibTableColumn
an80iIfPmpConnName = _An80iIfPmpConnName_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 6, 1, 2),
    _An80iIfPmpConnName_Type()
)
an80iIfPmpConnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpConnName.setStatus("current")


class _An80iIfPmpConnTaggingControl_Type(Integer32):
    """Custom type an80iIfPmpConnTaggingControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passThrough", 1),
          ("tagged", 2))
    )


_An80iIfPmpConnTaggingControl_Type.__name__ = "Integer32"
_An80iIfPmpConnTaggingControl_Object = MibTableColumn
an80iIfPmpConnTaggingControl = _An80iIfPmpConnTaggingControl_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 6, 1, 3),
    _An80iIfPmpConnTaggingControl_Type()
)
an80iIfPmpConnTaggingControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpConnTaggingControl.setStatus("current")


class _An80iIfPmpConnVlanId_Type(Integer32):
    """Custom type an80iIfPmpConnVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_An80iIfPmpConnVlanId_Type.__name__ = "Integer32"
_An80iIfPmpConnVlanId_Object = MibTableColumn
an80iIfPmpConnVlanId = _An80iIfPmpConnVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 6, 1, 4),
    _An80iIfPmpConnVlanId_Type()
)
an80iIfPmpConnVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpConnVlanId.setStatus("current")


class _An80iIfPmpConnDefPriority_Type(Integer32):
    """Custom type an80iIfPmpConnDefPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_An80iIfPmpConnDefPriority_Type.__name__ = "Integer32"
_An80iIfPmpConnDefPriority_Object = MibTableColumn
an80iIfPmpConnDefPriority = _An80iIfPmpConnDefPriority_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 6, 1, 5),
    _An80iIfPmpConnDefPriority_Type()
)
an80iIfPmpConnDefPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpConnDefPriority.setStatus("current")


class _An80iIfPmpConnDefParentLink_Type(Integer32):
    """Custom type an80iIfPmpConnDefParentLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1023),
    )


_An80iIfPmpConnDefParentLink_Type.__name__ = "Integer32"
_An80iIfPmpConnDefParentLink_Object = MibTableColumn
an80iIfPmpConnDefParentLink = _An80iIfPmpConnDefParentLink_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 6, 1, 6),
    _An80iIfPmpConnDefParentLink_Type()
)
an80iIfPmpConnDefParentLink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpConnDefParentLink.setStatus("current")


class _An80iIfPmpConnDefParenGroup_Type(Integer32):
    """Custom type an80iIfPmpConnDefParenGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1023),
    )


_An80iIfPmpConnDefParenGroup_Type.__name__ = "Integer32"
_An80iIfPmpConnDefParenGroup_Object = MibTableColumn
an80iIfPmpConnDefParenGroup = _An80iIfPmpConnDefParenGroup_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 6, 1, 7),
    _An80iIfPmpConnDefParenGroup_Type()
)
an80iIfPmpConnDefParenGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpConnDefParenGroup.setStatus("current")


class _An80iIfPmpConnDLQos_Type(Integer32):
    """Custom type an80iIfPmpConnDLQos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 53),
    )


_An80iIfPmpConnDLQos_Type.__name__ = "Integer32"
_An80iIfPmpConnDLQos_Object = MibTableColumn
an80iIfPmpConnDLQos = _An80iIfPmpConnDLQos_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 6, 1, 8),
    _An80iIfPmpConnDLQos_Type()
)
an80iIfPmpConnDLQos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpConnDLQos.setStatus("current")


class _An80iIfPmpConnULQos_Type(Integer32):
    """Custom type an80iIfPmpConnULQos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 53),
    )


_An80iIfPmpConnULQos_Type.__name__ = "Integer32"
_An80iIfPmpConnULQos_Object = MibTableColumn
an80iIfPmpConnULQos = _An80iIfPmpConnULQos_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 6, 1, 9),
    _An80iIfPmpConnULQos_Type()
)
an80iIfPmpConnULQos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpConnULQos.setStatus("current")
_An80iIfPmpConnConfigStatus_Type = RowStatus
_An80iIfPmpConnConfigStatus_Object = MibTableColumn
an80iIfPmpConnConfigStatus = _An80iIfPmpConnConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 6, 1, 10),
    _An80iIfPmpConnConfigStatus_Type()
)
an80iIfPmpConnConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    an80iIfPmpConnConfigStatus.setStatus("current")
_An80iIfPmpConnStatsTable_Object = MibTable
an80iIfPmpConnStatsTable = _An80iIfPmpConnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 7)
)
if mibBuilder.loadTexts:
    an80iIfPmpConnStatsTable.setStatus("current")
_An80iIfPmpConnStatsEntry_Object = MibTableRow
an80iIfPmpConnStatsEntry = _An80iIfPmpConnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 7, 1)
)
an80iIfPmpConnStatsEntry.setIndexNames(
    (0, "REDLINE-AN80I-IF-MIB", "an80iIfPmpConnId"),
)
if mibBuilder.loadTexts:
    an80iIfPmpConnStatsEntry.setStatus("current")
_An80iIfPmpConnDLPacketsTx_Type = Counter64
_An80iIfPmpConnDLPacketsTx_Object = MibTableColumn
an80iIfPmpConnDLPacketsTx = _An80iIfPmpConnDLPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 7, 1, 1),
    _An80iIfPmpConnDLPacketsTx_Type()
)
an80iIfPmpConnDLPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpConnDLPacketsTx.setStatus("current")
_An80iIfPmpConnDLPacketsRx_Type = Counter64
_An80iIfPmpConnDLPacketsRx_Object = MibTableColumn
an80iIfPmpConnDLPacketsRx = _An80iIfPmpConnDLPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 7, 1, 2),
    _An80iIfPmpConnDLPacketsRx_Type()
)
an80iIfPmpConnDLPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpConnDLPacketsRx.setStatus("current")
_An80iIfPmpConnDLPacketsDisc_Type = Counter64
_An80iIfPmpConnDLPacketsDisc_Object = MibTableColumn
an80iIfPmpConnDLPacketsDisc = _An80iIfPmpConnDLPacketsDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 7, 1, 3),
    _An80iIfPmpConnDLPacketsDisc_Type()
)
an80iIfPmpConnDLPacketsDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpConnDLPacketsDisc.setStatus("current")
_An80iIfPmpConnULPacketsTx_Type = Counter64
_An80iIfPmpConnULPacketsTx_Object = MibTableColumn
an80iIfPmpConnULPacketsTx = _An80iIfPmpConnULPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 7, 1, 4),
    _An80iIfPmpConnULPacketsTx_Type()
)
an80iIfPmpConnULPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpConnULPacketsTx.setStatus("current")
_An80iIfPmpConnULPacketsRx_Type = Counter64
_An80iIfPmpConnULPacketsRx_Object = MibTableColumn
an80iIfPmpConnULPacketsRx = _An80iIfPmpConnULPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 7, 1, 5),
    _An80iIfPmpConnULPacketsRx_Type()
)
an80iIfPmpConnULPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpConnULPacketsRx.setStatus("current")
_An80iIfPmpConnULPacketsDisc_Type = Counter64
_An80iIfPmpConnULPacketsDisc_Object = MibTableColumn
an80iIfPmpConnULPacketsDisc = _An80iIfPmpConnULPacketsDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 7, 1, 6),
    _An80iIfPmpConnULPacketsDisc_Type()
)
an80iIfPmpConnULPacketsDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpConnULPacketsDisc.setStatus("current")
_An80iIfPmpConnStatsStatus_Type = RowStatus
_An80iIfPmpConnStatsStatus_Object = MibTableColumn
an80iIfPmpConnStatsStatus = _An80iIfPmpConnStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 2, 7, 1, 7),
    _An80iIfPmpConnStatsStatus_Type()
)
an80iIfPmpConnStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an80iIfPmpConnStatsStatus.setStatus("current")
_RedlineAn80iIfConformance_ObjectIdentity = ObjectIdentity
redlineAn80iIfConformance = _RedlineAn80iIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 4)
)
_RedlineAn80iIfGroups_ObjectIdentity = ObjectIdentity
redlineAn80iIfGroups = _RedlineAn80iIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 4, 1)
)
_RedlineAn80iIfCompls_ObjectIdentity = ObjectIdentity
redlineAn80iIfCompls = _RedlineAn80iIfCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 4, 2)
)

# Managed Objects groups

redlineAn80iIfPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 4, 1, 1)
)
redlineAn80iIfPtpGroup.setObjects(
      *(("REDLINE-AN80I-IF-MIB", "an80iIfEncryptionControl"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfModReduction"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfAdaptiveMod"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfUncodedBurstRate"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfEncryptionKey"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPacketRetransControl"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfLinkLenMode"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfLinkLength"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfCurrUncodedBurstRate"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPtpLinkStatus"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfRxPackets"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfRxPacketsReTx"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfRxPacketsDisc"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfTxPackets"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfTxPacketsReTx"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfTxPacketsDisc"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfRssiMin"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfRssiMean"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfRssiMax"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfAvrSinAdr"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfCalcLinkDst"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfLinkName"))
)
if mibBuilder.loadTexts:
    redlineAn80iIfPtpGroup.setStatus("current")

redlineAn80iIfPmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 4, 1, 2)
)
redlineAn80iIfPmpGroup.setObjects(
      *(("REDLINE-AN80I-IF-MIB", "an80iIfLastMissedMacAddress"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfLastRegistMacAddress"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfDenyMacAddress"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfLastRegistLinkId"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkName"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkPeerMacAddress"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkULBurstRate"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkDLBurstRate"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkStatus"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkStatusCode"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfRegPmpLinkConns"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkLostCount"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkUpTime"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkLostCount"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkCurrDLUncBurstRate"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkLostCount"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkDLSinAdr"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkDLLostFrm"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkDLBlksTot"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkDLBlksRetr"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkDLBlksDisc"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkCurrULUncBurstRate"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkULRssi"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkULSinAdr"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkULLostFrm"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkULBlksTot"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkULBlksRetr"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpLinkULBlksDisc"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpGroupName"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpGroupTaggingControl"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpGroupVlanId"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpGroupDefPriority"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpGroupSCEtherControl"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpGroupQosLevel"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpGroupPacketsTx"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpGroupPacketDisc"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnName"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnTaggingControl"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnVlanId"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnDefPriority"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnDefParentLink"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnDefParenGroup"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnDLQos"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnULQos"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnDLPacketsTx"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnDLPacketsRx"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnDLPacketsDisc"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnULPacketsTx"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnULPacketsRx"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfPmpConnULPacketsDisc"))
)
if mibBuilder.loadTexts:
    redlineAn80iIfPmpGroup.setStatus("current")


# Notification objects

an80iIfRegistrationFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 0, 1)
)
an80iIfRegistrationFailedTrap.setObjects(
    ("REDLINE-AN80I-IF-MIB", "an80iIfLastMissedMacAddress")
)
if mibBuilder.loadTexts:
    an80iIfRegistrationFailedTrap.setStatus(
        "current"
    )

an80iIfRegistrationOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 0, 2)
)
an80iIfRegistrationOKTrap.setObjects(
    ("REDLINE-AN80I-IF-MIB", "an80iIfLastRegistMacAddress")
)
if mibBuilder.loadTexts:
    an80iIfRegistrationOKTrap.setStatus(
        "current"
    )


# Notifications groups

redlineAn80iIfNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 4, 1, 3)
)
redlineAn80iIfNotificationGroup.setObjects(
      *(("REDLINE-AN80I-IF-MIB", "an80iIfRegistrationFailedTrap"),
        ("REDLINE-AN80I-IF-MIB", "an80iIfRegistrationOKTrap"))
)
if mibBuilder.loadTexts:
    redlineAn80iIfNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

redlineAn80iIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    redlineAn80iIfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDLINE-AN80I-IF-MIB",
    **{"redlineAn80iIfMib": redlineAn80iIfMib,
       "redlineAn80iIfTrapDefinitions": redlineAn80iIfTrapDefinitions,
       "an80iIfRegistrationFailedTrap": an80iIfRegistrationFailedTrap,
       "an80iIfRegistrationOKTrap": an80iIfRegistrationOKTrap,
       "redlineAn80iIfPtpObjects": redlineAn80iIfPtpObjects,
       "redlineAn80iIfPtpLinkConfig": redlineAn80iIfPtpLinkConfig,
       "an80iIfEncryptionControl": an80iIfEncryptionControl,
       "an80iIfModReduction": an80iIfModReduction,
       "an80iIfAdaptiveMod": an80iIfAdaptiveMod,
       "an80iIfUncodedBurstRate": an80iIfUncodedBurstRate,
       "an80iIfEncryptionKey": an80iIfEncryptionKey,
       "an80iIfPacketRetransControl": an80iIfPacketRetransControl,
       "an80iIfLinkLenMode": an80iIfLinkLenMode,
       "an80iIfLinkLength": an80iIfLinkLength,
       "an80iIfCalcLinkDst": an80iIfCalcLinkDst,
       "an80iIfLinkName": an80iIfLinkName,
       "redlineAn80iIfPtpLinkStats": redlineAn80iIfPtpLinkStats,
       "an80iIfCurrUncodedBurstRate": an80iIfCurrUncodedBurstRate,
       "an80iIfPtpLinkStatus": an80iIfPtpLinkStatus,
       "an80iIfRxPackets": an80iIfRxPackets,
       "an80iIfRxPacketsReTx": an80iIfRxPacketsReTx,
       "an80iIfRxPacketsDisc": an80iIfRxPacketsDisc,
       "an80iIfTxPackets": an80iIfTxPackets,
       "an80iIfTxPacketsReTx": an80iIfTxPacketsReTx,
       "an80iIfTxPacketsDisc": an80iIfTxPacketsDisc,
       "an80iIfRssiMin": an80iIfRssiMin,
       "an80iIfRssiMean": an80iIfRssiMean,
       "an80iIfRssiMax": an80iIfRssiMax,
       "an80iIfAvrSinAdr": an80iIfAvrSinAdr,
       "redlineAn80iIfPmpObjects": redlineAn80iIfPmpObjects,
       "redlineAn80iIfPmpSsObjects": redlineAn80iIfPmpSsObjects,
       "an80iIfLastMissedMacAddress": an80iIfLastMissedMacAddress,
       "an80iIfLastRegistMacAddress": an80iIfLastRegistMacAddress,
       "an80iIfDenyMacAddress": an80iIfDenyMacAddress,
       "an80iIfLastRegistLinkId": an80iIfLastRegistLinkId,
       "an80iIfPmpLinkConfigTable": an80iIfPmpLinkConfigTable,
       "an80iIfPmpLinkConfigEntry": an80iIfPmpLinkConfigEntry,
       "an80iIfPmpLinkId": an80iIfPmpLinkId,
       "an80iIfPmpLinkName": an80iIfPmpLinkName,
       "an80iIfPmpLinkPeerMacAddress": an80iIfPmpLinkPeerMacAddress,
       "an80iIfPmpLinkULBurstRate": an80iIfPmpLinkULBurstRate,
       "an80iIfPmpLinkDLBurstRate": an80iIfPmpLinkDLBurstRate,
       "an80iIfPmpLinkConfigStatus": an80iIfPmpLinkConfigStatus,
       "an80iIfPmpLinkStatsTable": an80iIfPmpLinkStatsTable,
       "an80iIfPmpLinkStatsEntry": an80iIfPmpLinkStatsEntry,
       "an80iIfPmpLinkStatus": an80iIfPmpLinkStatus,
       "an80iIfPmpLinkStatusCode": an80iIfPmpLinkStatusCode,
       "an80iIfRegPmpLinkConns": an80iIfRegPmpLinkConns,
       "an80iIfPmpLinkUpTime": an80iIfPmpLinkUpTime,
       "an80iIfPmpLinkLostCount": an80iIfPmpLinkLostCount,
       "an80iIfPmpLinkCurrDLUncBurstRate": an80iIfPmpLinkCurrDLUncBurstRate,
       "an80iIfPmpLinkDLRssi": an80iIfPmpLinkDLRssi,
       "an80iIfPmpLinkDLSinAdr": an80iIfPmpLinkDLSinAdr,
       "an80iIfPmpLinkDLLostFrm": an80iIfPmpLinkDLLostFrm,
       "an80iIfPmpLinkDLBlksTot": an80iIfPmpLinkDLBlksTot,
       "an80iIfPmpLinkDLBlksRetr": an80iIfPmpLinkDLBlksRetr,
       "an80iIfPmpLinkDLBlksDisc": an80iIfPmpLinkDLBlksDisc,
       "an80iIfPmpLinkCurrULUncBurstRate": an80iIfPmpLinkCurrULUncBurstRate,
       "an80iIfPmpLinkULRssi": an80iIfPmpLinkULRssi,
       "an80iIfPmpLinkULSinAdr": an80iIfPmpLinkULSinAdr,
       "an80iIfPmpLinkULLostFrm": an80iIfPmpLinkULLostFrm,
       "an80iIfPmpLinkULBlksTot": an80iIfPmpLinkULBlksTot,
       "an80iIfPmpLinkULBlksRetr": an80iIfPmpLinkULBlksRetr,
       "an80iIfPmpLinkULBlksDisc": an80iIfPmpLinkULBlksDisc,
       "an80iIfPmpLinkStatsStatus": an80iIfPmpLinkStatsStatus,
       "an80iIfPmpGroupConfigTable": an80iIfPmpGroupConfigTable,
       "an80iIfPmpGroupConfigEntry": an80iIfPmpGroupConfigEntry,
       "an80iIfPmpGroupId": an80iIfPmpGroupId,
       "an80iIfPmpGroupName": an80iIfPmpGroupName,
       "an80iIfPmpGroupTaggingControl": an80iIfPmpGroupTaggingControl,
       "an80iIfPmpGroupVlanId": an80iIfPmpGroupVlanId,
       "an80iIfPmpGroupDefPriority": an80iIfPmpGroupDefPriority,
       "an80iIfPmpGroupSCEtherControl": an80iIfPmpGroupSCEtherControl,
       "an80iIfPmpGroupQosLevel": an80iIfPmpGroupQosLevel,
       "an80iIfPmpGroupConfigStatus": an80iIfPmpGroupConfigStatus,
       "an80iIfPmpGroupRate": an80iIfPmpGroupRate,
       "an80iIfPmpGroupSStoSSMulticast": an80iIfPmpGroupSStoSSMulticast,
       "an80iIfPmpGroupStatsTable": an80iIfPmpGroupStatsTable,
       "an80iIfPmpGroupStatsEntry": an80iIfPmpGroupStatsEntry,
       "an80iIfPmpGroupPacketsTx": an80iIfPmpGroupPacketsTx,
       "an80iIfPmpGroupPacketDisc": an80iIfPmpGroupPacketDisc,
       "an80iIfPmpGroupStatsStatus": an80iIfPmpGroupStatsStatus,
       "an80iIfPmpConnConfigTable": an80iIfPmpConnConfigTable,
       "an80iIfPmpConnConfigEntry": an80iIfPmpConnConfigEntry,
       "an80iIfPmpConnId": an80iIfPmpConnId,
       "an80iIfPmpConnName": an80iIfPmpConnName,
       "an80iIfPmpConnTaggingControl": an80iIfPmpConnTaggingControl,
       "an80iIfPmpConnVlanId": an80iIfPmpConnVlanId,
       "an80iIfPmpConnDefPriority": an80iIfPmpConnDefPriority,
       "an80iIfPmpConnDefParentLink": an80iIfPmpConnDefParentLink,
       "an80iIfPmpConnDefParenGroup": an80iIfPmpConnDefParenGroup,
       "an80iIfPmpConnDLQos": an80iIfPmpConnDLQos,
       "an80iIfPmpConnULQos": an80iIfPmpConnULQos,
       "an80iIfPmpConnConfigStatus": an80iIfPmpConnConfigStatus,
       "an80iIfPmpConnStatsTable": an80iIfPmpConnStatsTable,
       "an80iIfPmpConnStatsEntry": an80iIfPmpConnStatsEntry,
       "an80iIfPmpConnDLPacketsTx": an80iIfPmpConnDLPacketsTx,
       "an80iIfPmpConnDLPacketsRx": an80iIfPmpConnDLPacketsRx,
       "an80iIfPmpConnDLPacketsDisc": an80iIfPmpConnDLPacketsDisc,
       "an80iIfPmpConnULPacketsTx": an80iIfPmpConnULPacketsTx,
       "an80iIfPmpConnULPacketsRx": an80iIfPmpConnULPacketsRx,
       "an80iIfPmpConnULPacketsDisc": an80iIfPmpConnULPacketsDisc,
       "an80iIfPmpConnStatsStatus": an80iIfPmpConnStatsStatus,
       "redlineAn80iIfConformance": redlineAn80iIfConformance,
       "redlineAn80iIfGroups": redlineAn80iIfGroups,
       "redlineAn80iIfPtpGroup": redlineAn80iIfPtpGroup,
       "redlineAn80iIfPmpGroup": redlineAn80iIfPmpGroup,
       "redlineAn80iIfNotificationGroup": redlineAn80iIfNotificationGroup,
       "redlineAn80iIfCompls": redlineAn80iIfCompls,
       "redlineAn80iIfCompliance": redlineAn80iIfCompliance}
)
