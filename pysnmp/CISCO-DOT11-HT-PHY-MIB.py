# SNMP MIB module (CISCO-DOT11-HT-PHY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-HT-PHY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:52 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDot11HtPhyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 607)
)
ciscoDot11HtPhyMIB.setRevisions(
        ("2006-12-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CD11HtPhyBeamformFeedback(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoDot11HtPhyMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDot11HtPhyMIBNotifs = _CiscoDot11HtPhyMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 0)
)
_CiscoDot11HtPhyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDot11HtPhyMIBObjects = _CiscoDot11HtPhyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1)
)
_CD11HtPhy_ObjectIdentity = ObjectIdentity
cD11HtPhy = _CD11HtPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1)
)
_CD11HtPhyAntennaTable_Object = MibTable
cD11HtPhyAntennaTable = _CD11HtPhyAntennaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cD11HtPhyAntennaTable.setStatus("current")
_CD11HtPhyAntennaEntry_Object = MibTableRow
cD11HtPhyAntennaEntry = _CD11HtPhyAntennaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1)
)
cD11HtPhyAntennaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cD11HtPhyAntennaEntry.setStatus("current")


class _CD11HtPhyAntennaSelectionImplemented_Type(TruthValue):
    """Custom type cD11HtPhyAntennaSelectionImplemented based on TruthValue"""


_CD11HtPhyAntennaSelectionImplemented_Object = MibTableColumn
cD11HtPhyAntennaSelectionImplemented = _CD11HtPhyAntennaSelectionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 1),
    _CD11HtPhyAntennaSelectionImplemented_Type()
)
cD11HtPhyAntennaSelectionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyAntennaSelectionImplemented.setStatus("current")


class _CD11HtPhyXmitExpCSIFdbkASImplemented_Type(TruthValue):
    """Custom type cD11HtPhyXmitExpCSIFdbkASImplemented based on TruthValue"""


_CD11HtPhyXmitExpCSIFdbkASImplemented_Object = MibTableColumn
cD11HtPhyXmitExpCSIFdbkASImplemented = _CD11HtPhyXmitExpCSIFdbkASImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 5),
    _CD11HtPhyXmitExpCSIFdbkASImplemented_Type()
)
cD11HtPhyXmitExpCSIFdbkASImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyXmitExpCSIFdbkASImplemented.setStatus("current")


class _CD11HtPhyXmitIndFdbkASImplemented_Type(TruthValue):
    """Custom type cD11HtPhyXmitIndFdbkASImplemented based on TruthValue"""


_CD11HtPhyXmitIndFdbkASImplemented_Object = MibTableColumn
cD11HtPhyXmitIndFdbkASImplemented = _CD11HtPhyXmitIndFdbkASImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 6),
    _CD11HtPhyXmitIndFdbkASImplemented_Type()
)
cD11HtPhyXmitIndFdbkASImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyXmitIndFdbkASImplemented.setStatus("current")


class _CD11HtPhyExplCSIFdbkASImplemented_Type(TruthValue):
    """Custom type cD11HtPhyExplCSIFdbkASImplemented based on TruthValue"""


_CD11HtPhyExplCSIFdbkASImplemented_Object = MibTableColumn
cD11HtPhyExplCSIFdbkASImplemented = _CD11HtPhyExplCSIFdbkASImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 7),
    _CD11HtPhyExplCSIFdbkASImplemented_Type()
)
cD11HtPhyExplCSIFdbkASImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyExplCSIFdbkASImplemented.setStatus("current")


class _CD11HtPhyXmitIndCompFdbkASImplemented_Type(TruthValue):
    """Custom type cD11HtPhyXmitIndCompFdbkASImplemented based on TruthValue"""


_CD11HtPhyXmitIndCompFdbkASImplemented_Object = MibTableColumn
cD11HtPhyXmitIndCompFdbkASImplemented = _CD11HtPhyXmitIndCompFdbkASImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 8),
    _CD11HtPhyXmitIndCompFdbkASImplemented_Type()
)
cD11HtPhyXmitIndCompFdbkASImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyXmitIndCompFdbkASImplemented.setStatus("current")


class _CD11HtPhyRcvAntennaSelImplemented_Type(TruthValue):
    """Custom type cD11HtPhyRcvAntennaSelImplemented based on TruthValue"""


_CD11HtPhyRcvAntennaSelImplemented_Object = MibTableColumn
cD11HtPhyRcvAntennaSelImplemented = _CD11HtPhyRcvAntennaSelImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 9),
    _CD11HtPhyRcvAntennaSelImplemented_Type()
)
cD11HtPhyRcvAntennaSelImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyRcvAntennaSelImplemented.setStatus("current")


class _CD11HtPhyXmitSoundPPDUImplemented_Type(TruthValue):
    """Custom type cD11HtPhyXmitSoundPPDUImplemented based on TruthValue"""


_CD11HtPhyXmitSoundPPDUImplemented_Object = MibTableColumn
cD11HtPhyXmitSoundPPDUImplemented = _CD11HtPhyXmitSoundPPDUImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 1, 1, 10),
    _CD11HtPhyXmitSoundPPDUImplemented_Type()
)
cD11HtPhyXmitSoundPPDUImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyXmitSoundPPDUImplemented.setStatus("current")
_CD11HtPhyTable_Object = MibTable
cD11HtPhyTable = _CD11HtPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cD11HtPhyTable.setStatus("current")
_CD11HtPhyEntry_Object = MibTableRow
cD11HtPhyEntry = _CD11HtPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1)
)
cD11HtPhyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cD11HtPhyEntry.setStatus("current")


class _CD11HtPhyOperatingMode_Type(Integer32):
    """Custom type cD11HtPhyOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("greenField", 3),
          ("legacy", 1),
          ("mixed", 2))
    )


_CD11HtPhyOperatingMode_Type.__name__ = "Integer32"
_CD11HtPhyOperatingMode_Object = MibTableColumn
cD11HtPhyOperatingMode = _CD11HtPhyOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 1),
    _CD11HtPhyOperatingMode_Type()
)
cD11HtPhyOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyOperatingMode.setStatus("current")


class _CD11HtPhyOperModeFrequency_Type(Integer32):
    """Custom type cD11HtPhyOperModeFrequency based on Integer32"""
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
        *(("dupLegacyMode", 3),
          ("fortyMHzLowerMode", 5),
          ("fortyMHzUpperMode", 4),
          ("htMode", 2),
          ("legacyMode", 1))
    )


_CD11HtPhyOperModeFrequency_Type.__name__ = "Integer32"
_CD11HtPhyOperModeFrequency_Object = MibTableColumn
cD11HtPhyOperModeFrequency = _CD11HtPhyOperModeFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 2),
    _CD11HtPhyOperModeFrequency_Type()
)
cD11HtPhyOperModeFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyOperModeFrequency.setStatus("current")


class _CD11HtPhyOperBand_Type(Integer32):
    """Custom type cD11HtPhyOperBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("band24GHz", 1),
          ("band5GHz", 2))
    )


_CD11HtPhyOperBand_Type.__name__ = "Integer32"
_CD11HtPhyOperBand_Object = MibTableColumn
cD11HtPhyOperBand = _CD11HtPhyOperBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 3),
    _CD11HtPhyOperBand_Type()
)
cD11HtPhyOperBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyOperBand.setStatus("current")


class _CD11HtPhyFortyMHzOperationImplemented_Type(TruthValue):
    """Custom type cD11HtPhyFortyMHzOperationImplemented based on TruthValue"""


_CD11HtPhyFortyMHzOperationImplemented_Object = MibTableColumn
cD11HtPhyFortyMHzOperationImplemented = _CD11HtPhyFortyMHzOperationImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 4),
    _CD11HtPhyFortyMHzOperationImplemented_Type()
)
cD11HtPhyFortyMHzOperationImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyFortyMHzOperationImplemented.setStatus("current")


class _CD11HtPhyFortyMHzOperationEnabled_Type(TruthValue):
    """Custom type cD11HtPhyFortyMHzOperationEnabled based on TruthValue"""


_CD11HtPhyFortyMHzOperationEnabled_Object = MibTableColumn
cD11HtPhyFortyMHzOperationEnabled = _CD11HtPhyFortyMHzOperationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 5),
    _CD11HtPhyFortyMHzOperationEnabled_Type()
)
cD11HtPhyFortyMHzOperationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyFortyMHzOperationEnabled.setStatus("current")
_CD11HtPhyCurrentControlChannel_Type = Unsigned32
_CD11HtPhyCurrentControlChannel_Object = MibTableColumn
cD11HtPhyCurrentControlChannel = _CD11HtPhyCurrentControlChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 6),
    _CD11HtPhyCurrentControlChannel_Type()
)
cD11HtPhyCurrentControlChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyCurrentControlChannel.setStatus("current")


class _CD11HtPhyCurrentExtensionChannel_Type(Integer32):
    """Custom type cD11HtPhyCurrentExtensionChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("extensionAbove", 2),
          ("extensionBelow", 3),
          ("noExtension", 1))
    )


_CD11HtPhyCurrentExtensionChannel_Type.__name__ = "Integer32"
_CD11HtPhyCurrentExtensionChannel_Object = MibTableColumn
cD11HtPhyCurrentExtensionChannel = _CD11HtPhyCurrentExtensionChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 7),
    _CD11HtPhyCurrentExtensionChannel_Type()
)
cD11HtPhyCurrentExtensionChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtPhyCurrentExtensionChannel.setStatus("current")


class _CD11HtPhyExtChannelCCAImplemented_Type(TruthValue):
    """Custom type cD11HtPhyExtChannelCCAImplemented based on TruthValue"""


_CD11HtPhyExtChannelCCAImplemented_Object = MibTableColumn
cD11HtPhyExtChannelCCAImplemented = _CD11HtPhyExtChannelCCAImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 8),
    _CD11HtPhyExtChannelCCAImplemented_Type()
)
cD11HtPhyExtChannelCCAImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyExtChannelCCAImplemented.setStatus("current")


class _CD11HtPhyNumberOfSpatialStreamsImplemented_Type(Integer32):
    """Custom type cD11HtPhyNumberOfSpatialStreamsImplemented based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CD11HtPhyNumberOfSpatialStreamsImplemented_Type.__name__ = "Integer32"
_CD11HtPhyNumberOfSpatialStreamsImplemented_Object = MibTableColumn
cD11HtPhyNumberOfSpatialStreamsImplemented = _CD11HtPhyNumberOfSpatialStreamsImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 9),
    _CD11HtPhyNumberOfSpatialStreamsImplemented_Type()
)
cD11HtPhyNumberOfSpatialStreamsImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyNumberOfSpatialStreamsImplemented.setStatus("current")


class _CD11HtPhyNumberOfSpatialStreamsEnabled_Type(Integer32):
    """Custom type cD11HtPhyNumberOfSpatialStreamsEnabled based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CD11HtPhyNumberOfSpatialStreamsEnabled_Type.__name__ = "Integer32"
_CD11HtPhyNumberOfSpatialStreamsEnabled_Object = MibTableColumn
cD11HtPhyNumberOfSpatialStreamsEnabled = _CD11HtPhyNumberOfSpatialStreamsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 10),
    _CD11HtPhyNumberOfSpatialStreamsEnabled_Type()
)
cD11HtPhyNumberOfSpatialStreamsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyNumberOfSpatialStreamsEnabled.setStatus("current")


class _CD11HtPhyGreenFieldImplemented_Type(TruthValue):
    """Custom type cD11HtPhyGreenFieldImplemented based on TruthValue"""


_CD11HtPhyGreenFieldImplemented_Object = MibTableColumn
cD11HtPhyGreenFieldImplemented = _CD11HtPhyGreenFieldImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 11),
    _CD11HtPhyGreenFieldImplemented_Type()
)
cD11HtPhyGreenFieldImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyGreenFieldImplemented.setStatus("current")


class _CD11HtPhyGreenFieldEnabled_Type(TruthValue):
    """Custom type cD11HtPhyGreenFieldEnabled based on TruthValue"""


_CD11HtPhyGreenFieldEnabled_Object = MibTableColumn
cD11HtPhyGreenFieldEnabled = _CD11HtPhyGreenFieldEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 12),
    _CD11HtPhyGreenFieldEnabled_Type()
)
cD11HtPhyGreenFieldEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtPhyGreenFieldEnabled.setStatus("current")


class _CD11HtPhyShortGIInTwentyImplemented_Type(TruthValue):
    """Custom type cD11HtPhyShortGIInTwentyImplemented based on TruthValue"""


_CD11HtPhyShortGIInTwentyImplemented_Object = MibTableColumn
cD11HtPhyShortGIInTwentyImplemented = _CD11HtPhyShortGIInTwentyImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 13),
    _CD11HtPhyShortGIInTwentyImplemented_Type()
)
cD11HtPhyShortGIInTwentyImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyShortGIInTwentyImplemented.setStatus("current")


class _CD11HtPhyShortGIInTwentyEnabled_Type(TruthValue):
    """Custom type cD11HtPhyShortGIInTwentyEnabled based on TruthValue"""


_CD11HtPhyShortGIInTwentyEnabled_Object = MibTableColumn
cD11HtPhyShortGIInTwentyEnabled = _CD11HtPhyShortGIInTwentyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 14),
    _CD11HtPhyShortGIInTwentyEnabled_Type()
)
cD11HtPhyShortGIInTwentyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtPhyShortGIInTwentyEnabled.setStatus("current")


class _CD11HtPhyShortGIInFortyImplemented_Type(TruthValue):
    """Custom type cD11HtPhyShortGIInFortyImplemented based on TruthValue"""


_CD11HtPhyShortGIInFortyImplemented_Object = MibTableColumn
cD11HtPhyShortGIInFortyImplemented = _CD11HtPhyShortGIInFortyImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 15),
    _CD11HtPhyShortGIInFortyImplemented_Type()
)
cD11HtPhyShortGIInFortyImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyShortGIInFortyImplemented.setStatus("current")


class _CD11HtPhyShortGIInFortyEnabled_Type(TruthValue):
    """Custom type cD11HtPhyShortGIInFortyEnabled based on TruthValue"""


_CD11HtPhyShortGIInFortyEnabled_Object = MibTableColumn
cD11HtPhyShortGIInFortyEnabled = _CD11HtPhyShortGIInFortyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 16),
    _CD11HtPhyShortGIInFortyEnabled_Type()
)
cD11HtPhyShortGIInFortyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtPhyShortGIInFortyEnabled.setStatus("current")


class _CD11HtPhyAdvancedCodingImplemented_Type(TruthValue):
    """Custom type cD11HtPhyAdvancedCodingImplemented based on TruthValue"""


_CD11HtPhyAdvancedCodingImplemented_Object = MibTableColumn
cD11HtPhyAdvancedCodingImplemented = _CD11HtPhyAdvancedCodingImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 17),
    _CD11HtPhyAdvancedCodingImplemented_Type()
)
cD11HtPhyAdvancedCodingImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyAdvancedCodingImplemented.setStatus("current")


class _CD11HtPhyAdvancedCodingEnabled_Type(TruthValue):
    """Custom type cD11HtPhyAdvancedCodingEnabled based on TruthValue"""


_CD11HtPhyAdvancedCodingEnabled_Object = MibTableColumn
cD11HtPhyAdvancedCodingEnabled = _CD11HtPhyAdvancedCodingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 18),
    _CD11HtPhyAdvancedCodingEnabled_Type()
)
cD11HtPhyAdvancedCodingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtPhyAdvancedCodingEnabled.setStatus("current")


class _CD11HtPhyTxSTBCImplemented_Type(TruthValue):
    """Custom type cD11HtPhyTxSTBCImplemented based on TruthValue"""


_CD11HtPhyTxSTBCImplemented_Object = MibTableColumn
cD11HtPhyTxSTBCImplemented = _CD11HtPhyTxSTBCImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 19),
    _CD11HtPhyTxSTBCImplemented_Type()
)
cD11HtPhyTxSTBCImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyTxSTBCImplemented.setStatus("current")


class _CD11HtPhyTxSTBCEnabled_Type(TruthValue):
    """Custom type cD11HtPhyTxSTBCEnabled based on TruthValue"""


_CD11HtPhyTxSTBCEnabled_Object = MibTableColumn
cD11HtPhyTxSTBCEnabled = _CD11HtPhyTxSTBCEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 20),
    _CD11HtPhyTxSTBCEnabled_Type()
)
cD11HtPhyTxSTBCEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtPhyTxSTBCEnabled.setStatus("current")


class _CD11HtPhyRxSTBCImplemented_Type(TruthValue):
    """Custom type cD11HtPhyRxSTBCImplemented based on TruthValue"""


_CD11HtPhyRxSTBCImplemented_Object = MibTableColumn
cD11HtPhyRxSTBCImplemented = _CD11HtPhyRxSTBCImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 21),
    _CD11HtPhyRxSTBCImplemented_Type()
)
cD11HtPhyRxSTBCImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyRxSTBCImplemented.setStatus("current")


class _CD11HtPhyRxSTBCEnabled_Type(TruthValue):
    """Custom type cD11HtPhyRxSTBCEnabled based on TruthValue"""


_CD11HtPhyRxSTBCEnabled_Object = MibTableColumn
cD11HtPhyRxSTBCEnabled = _CD11HtPhyRxSTBCEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 22),
    _CD11HtPhyRxSTBCEnabled_Type()
)
cD11HtPhyRxSTBCEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtPhyRxSTBCEnabled.setStatus("current")


class _CD11HtPhyBeamFormingImplemented_Type(TruthValue):
    """Custom type cD11HtPhyBeamFormingImplemented based on TruthValue"""


_CD11HtPhyBeamFormingImplemented_Object = MibTableColumn
cD11HtPhyBeamFormingImplemented = _CD11HtPhyBeamFormingImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 23),
    _CD11HtPhyBeamFormingImplemented_Type()
)
cD11HtPhyBeamFormingImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyBeamFormingImplemented.setStatus("current")


class _CD11HtPhyBeamFormingEnabled_Type(TruthValue):
    """Custom type cD11HtPhyBeamFormingEnabled based on TruthValue"""


_CD11HtPhyBeamFormingEnabled_Object = MibTableColumn
cD11HtPhyBeamFormingEnabled = _CD11HtPhyBeamFormingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 2, 1, 24),
    _CD11HtPhyBeamFormingEnabled_Type()
)
cD11HtPhyBeamFormingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cD11HtPhyBeamFormingEnabled.setStatus("current")
_CD11HtPhySupportedMCSTable_Object = MibTable
cD11HtPhySupportedMCSTable = _CD11HtPhySupportedMCSTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cD11HtPhySupportedMCSTable.setStatus("current")
_CD11HtPhySupportedMCSEntry_Object = MibTableRow
cD11HtPhySupportedMCSEntry = _CD11HtPhySupportedMCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 3, 1)
)
cD11HtPhySupportedMCSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cD11HtPhySupportedMCSEntry.setStatus("current")


class _CD11HtPhySupportedMCSTxValue_Type(OctetString):
    """Custom type cD11HtPhySupportedMCSTxValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_CD11HtPhySupportedMCSTxValue_Type.__name__ = "OctetString"
_CD11HtPhySupportedMCSTxValue_Object = MibTableColumn
cD11HtPhySupportedMCSTxValue = _CD11HtPhySupportedMCSTxValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 3, 1, 1),
    _CD11HtPhySupportedMCSTxValue_Type()
)
cD11HtPhySupportedMCSTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhySupportedMCSTxValue.setStatus("current")


class _CD11HtPhySupportedMCSRxValue_Type(OctetString):
    """Custom type cD11HtPhySupportedMCSRxValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_CD11HtPhySupportedMCSRxValue_Type.__name__ = "OctetString"
_CD11HtPhySupportedMCSRxValue_Object = MibTableColumn
cD11HtPhySupportedMCSRxValue = _CD11HtPhySupportedMCSRxValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 3, 1, 2),
    _CD11HtPhySupportedMCSRxValue_Type()
)
cD11HtPhySupportedMCSRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhySupportedMCSRxValue.setStatus("current")
_CD11HtPhyTxBFConfigTable_Object = MibTable
cD11HtPhyTxBFConfigTable = _CD11HtPhyTxBFConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cD11HtPhyTxBFConfigTable.setStatus("current")
_CD11HtPhyTxBFConfigEntry_Object = MibTableRow
cD11HtPhyTxBFConfigEntry = _CD11HtPhyTxBFConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1)
)
cD11HtPhyTxBFConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cD11HtPhyTxBFConfigEntry.setStatus("current")


class _CD11HtPhyRxStaggerSoundImplemented_Type(TruthValue):
    """Custom type cD11HtPhyRxStaggerSoundImplemented based on TruthValue"""


_CD11HtPhyRxStaggerSoundImplemented_Object = MibTableColumn
cD11HtPhyRxStaggerSoundImplemented = _CD11HtPhyRxStaggerSoundImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 1),
    _CD11HtPhyRxStaggerSoundImplemented_Type()
)
cD11HtPhyRxStaggerSoundImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyRxStaggerSoundImplemented.setStatus("current")


class _CD11HtPhyTxStaggerSoundImplemented_Type(TruthValue):
    """Custom type cD11HtPhyTxStaggerSoundImplemented based on TruthValue"""


_CD11HtPhyTxStaggerSoundImplemented_Object = MibTableColumn
cD11HtPhyTxStaggerSoundImplemented = _CD11HtPhyTxStaggerSoundImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 2),
    _CD11HtPhyTxStaggerSoundImplemented_Type()
)
cD11HtPhyTxStaggerSoundImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyTxStaggerSoundImplemented.setStatus("current")


class _CD11HtPhyRxZLFImplemented_Type(TruthValue):
    """Custom type cD11HtPhyRxZLFImplemented based on TruthValue"""


_CD11HtPhyRxZLFImplemented_Object = MibTableColumn
cD11HtPhyRxZLFImplemented = _CD11HtPhyRxZLFImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 3),
    _CD11HtPhyRxZLFImplemented_Type()
)
cD11HtPhyRxZLFImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyRxZLFImplemented.setStatus("current")


class _CD11HtPhyTxZLFImplemented_Type(TruthValue):
    """Custom type cD11HtPhyTxZLFImplemented based on TruthValue"""


_CD11HtPhyTxZLFImplemented_Object = MibTableColumn
cD11HtPhyTxZLFImplemented = _CD11HtPhyTxZLFImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 4),
    _CD11HtPhyTxZLFImplemented_Type()
)
cD11HtPhyTxZLFImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyTxZLFImplemented.setStatus("current")


class _CD11HtPhyImplicitTxBFImplemented_Type(TruthValue):
    """Custom type cD11HtPhyImplicitTxBFImplemented based on TruthValue"""


_CD11HtPhyImplicitTxBFImplemented_Object = MibTableColumn
cD11HtPhyImplicitTxBFImplemented = _CD11HtPhyImplicitTxBFImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 5),
    _CD11HtPhyImplicitTxBFImplemented_Type()
)
cD11HtPhyImplicitTxBFImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyImplicitTxBFImplemented.setStatus("current")


class _CD11HtPhyCalibrationImplemented_Type(Integer32):
    """Custom type cD11HtPhyCalibrationImplemented based on Integer32"""
    defaultValue = 1

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
        *(("ableToInitiate", 3),
          ("fullyCapable", 4),
          ("inCapable", 1),
          ("unableToInitiate", 2))
    )


_CD11HtPhyCalibrationImplemented_Type.__name__ = "Integer32"
_CD11HtPhyCalibrationImplemented_Object = MibTableColumn
cD11HtPhyCalibrationImplemented = _CD11HtPhyCalibrationImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 6),
    _CD11HtPhyCalibrationImplemented_Type()
)
cD11HtPhyCalibrationImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyCalibrationImplemented.setStatus("current")


class _CD11HtPhyExplCSITxBFImplemented_Type(TruthValue):
    """Custom type cD11HtPhyExplCSITxBFImplemented based on TruthValue"""


_CD11HtPhyExplCSITxBFImplemented_Object = MibTableColumn
cD11HtPhyExplCSITxBFImplemented = _CD11HtPhyExplCSITxBFImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 7),
    _CD11HtPhyExplCSITxBFImplemented_Type()
)
cD11HtPhyExplCSITxBFImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyExplCSITxBFImplemented.setStatus("current")


class _CD11HtPhyExplUncompSteerMatrixImplemented_Type(TruthValue):
    """Custom type cD11HtPhyExplUncompSteerMatrixImplemented based on TruthValue"""


_CD11HtPhyExplUncompSteerMatrixImplemented_Object = MibTableColumn
cD11HtPhyExplUncompSteerMatrixImplemented = _CD11HtPhyExplUncompSteerMatrixImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 8),
    _CD11HtPhyExplUncompSteerMatrixImplemented_Type()
)
cD11HtPhyExplUncompSteerMatrixImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyExplUncompSteerMatrixImplemented.setStatus("current")
_CD11HtPhyExplBFCSIFdbkImplemented_Type = CD11HtPhyBeamformFeedback
_CD11HtPhyExplBFCSIFdbkImplemented_Object = MibTableColumn
cD11HtPhyExplBFCSIFdbkImplemented = _CD11HtPhyExplBFCSIFdbkImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 9),
    _CD11HtPhyExplBFCSIFdbkImplemented_Type()
)
cD11HtPhyExplBFCSIFdbkImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyExplBFCSIFdbkImplemented.setStatus("current")
_CD11HtPhyExplUncompSteerMatrixFdbkImplemented_Type = CD11HtPhyBeamformFeedback
_CD11HtPhyExplUncompSteerMatrixFdbkImplemented_Object = MibTableColumn
cD11HtPhyExplUncompSteerMatrixFdbkImplemented = _CD11HtPhyExplUncompSteerMatrixFdbkImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 10),
    _CD11HtPhyExplUncompSteerMatrixFdbkImplemented_Type()
)
cD11HtPhyExplUncompSteerMatrixFdbkImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyExplUncompSteerMatrixFdbkImplemented.setStatus("current")
_CD11HtPhyExplCompSteerMatrixFdbkImplemented_Type = CD11HtPhyBeamformFeedback
_CD11HtPhyExplCompSteerMatrixFdbkImplemented_Object = MibTableColumn
cD11HtPhyExplCompSteerMatrixFdbkImplemented = _CD11HtPhyExplCompSteerMatrixFdbkImplemented_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 11),
    _CD11HtPhyExplCompSteerMatrixFdbkImplemented_Type()
)
cD11HtPhyExplCompSteerMatrixFdbkImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyExplCompSteerMatrixFdbkImplemented.setStatus("current")


class _CD11HtPhyNumberBeamFormingCSISupportAntenna_Type(Integer32):
    """Custom type cD11HtPhyNumberBeamFormingCSISupportAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CD11HtPhyNumberBeamFormingCSISupportAntenna_Type.__name__ = "Integer32"
_CD11HtPhyNumberBeamFormingCSISupportAntenna_Object = MibTableColumn
cD11HtPhyNumberBeamFormingCSISupportAntenna = _CD11HtPhyNumberBeamFormingCSISupportAntenna_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 12),
    _CD11HtPhyNumberBeamFormingCSISupportAntenna_Type()
)
cD11HtPhyNumberBeamFormingCSISupportAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyNumberBeamFormingCSISupportAntenna.setStatus("current")


class _CD11HtPhyNumberUncompSteerMatrixSupportAntenna_Type(Integer32):
    """Custom type cD11HtPhyNumberUncompSteerMatrixSupportAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CD11HtPhyNumberUncompSteerMatrixSupportAntenna_Type.__name__ = "Integer32"
_CD11HtPhyNumberUncompSteerMatrixSupportAntenna_Object = MibTableColumn
cD11HtPhyNumberUncompSteerMatrixSupportAntenna = _CD11HtPhyNumberUncompSteerMatrixSupportAntenna_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 13),
    _CD11HtPhyNumberUncompSteerMatrixSupportAntenna_Type()
)
cD11HtPhyNumberUncompSteerMatrixSupportAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyNumberUncompSteerMatrixSupportAntenna.setStatus("current")


class _CD11HtPhyNumberCompSteerMatrixSupportAntenna_Type(Integer32):
    """Custom type cD11HtPhyNumberCompSteerMatrixSupportAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CD11HtPhyNumberCompSteerMatrixSupportAntenna_Type.__name__ = "Integer32"
_CD11HtPhyNumberCompSteerMatrixSupportAntenna_Object = MibTableColumn
cD11HtPhyNumberCompSteerMatrixSupportAntenna = _CD11HtPhyNumberCompSteerMatrixSupportAntenna_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 4, 1, 14),
    _CD11HtPhyNumberCompSteerMatrixSupportAntenna_Type()
)
cD11HtPhyNumberCompSteerMatrixSupportAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyNumberCompSteerMatrixSupportAntenna.setStatus("current")
_CD11HtPhyEnhPowerTable_Object = MibTable
cD11HtPhyEnhPowerTable = _CD11HtPhyEnhPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cD11HtPhyEnhPowerTable.setStatus("current")
_CD11HtPhyEnhPowerEntry_Object = MibTableRow
cD11HtPhyEnhPowerEntry = _CD11HtPhyEnhPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 5, 1)
)
cD11HtPhyEnhPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cD11HtPhyEnhPowerEntry.setStatus("current")


class _CD11HtPhyEnhPowerLevel20MHz_Type(Unsigned32):
    """Custom type cD11HtPhyEnhPowerLevel20MHz based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CD11HtPhyEnhPowerLevel20MHz_Type.__name__ = "Unsigned32"
_CD11HtPhyEnhPowerLevel20MHz_Object = MibTableColumn
cD11HtPhyEnhPowerLevel20MHz = _CD11HtPhyEnhPowerLevel20MHz_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 5, 1, 1),
    _CD11HtPhyEnhPowerLevel20MHz_Type()
)
cD11HtPhyEnhPowerLevel20MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyEnhPowerLevel20MHz.setStatus("current")


class _CD11HtPhyEnhPowerLevel40MHz_Type(Unsigned32):
    """Custom type cD11HtPhyEnhPowerLevel40MHz based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CD11HtPhyEnhPowerLevel40MHz_Type.__name__ = "Unsigned32"
_CD11HtPhyEnhPowerLevel40MHz_Object = MibTableColumn
cD11HtPhyEnhPowerLevel40MHz = _CD11HtPhyEnhPowerLevel40MHz_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 1, 1, 5, 1, 2),
    _CD11HtPhyEnhPowerLevel40MHz_Type()
)
cD11HtPhyEnhPowerLevel40MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cD11HtPhyEnhPowerLevel40MHz.setStatus("current")
_CiscoDot11HtPhyMIBConform_ObjectIdentity = ObjectIdentity
ciscoDot11HtPhyMIBConform = _CiscoDot11HtPhyMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 2)
)
_CiscoDot11HtPhyMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDot11HtPhyMIBCompliances = _CiscoDot11HtPhyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 1)
)
_CiscoDot11HtPhyMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDot11HtPhyMIBGroups = _CiscoDot11HtPhyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 2)
)

# Managed Objects groups

ciscoDot11HtPhyAntennaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 2, 1)
)
ciscoDot11HtPhyAntennaGroup.setObjects(
      *(("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyAntennaSelectionImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyXmitExpCSIFdbkASImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyXmitIndFdbkASImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExplCSIFdbkASImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyXmitIndCompFdbkASImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyRcvAntennaSelImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyXmitSoundPPDUImplemented"))
)
if mibBuilder.loadTexts:
    ciscoDot11HtPhyAntennaGroup.setStatus("current")

ciscoDot11HtPhyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 2, 2)
)
ciscoDot11HtPhyConfigGroup.setObjects(
      *(("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyOperatingMode"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyOperModeFrequency"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyOperBand"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyFortyMHzOperationImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyFortyMHzOperationEnabled"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyCurrentControlChannel"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyCurrentExtensionChannel"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExtChannelCCAImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyNumberOfSpatialStreamsImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyNumberOfSpatialStreamsEnabled"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyGreenFieldImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyGreenFieldEnabled"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyShortGIInTwentyImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyShortGIInTwentyEnabled"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyShortGIInFortyImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyShortGIInFortyEnabled"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyAdvancedCodingImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyAdvancedCodingEnabled"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyTxSTBCImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyTxSTBCEnabled"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyRxSTBCImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyRxSTBCEnabled"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyBeamFormingImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyBeamFormingEnabled"))
)
if mibBuilder.loadTexts:
    ciscoDot11HtPhyConfigGroup.setStatus("current")

ciscoDot11HtPhyMcsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 2, 3)
)
ciscoDot11HtPhyMcsGroup.setObjects(
      *(("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhySupportedMCSTxValue"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhySupportedMCSRxValue"))
)
if mibBuilder.loadTexts:
    ciscoDot11HtPhyMcsGroup.setStatus("current")

ciscoDot11HtPhyTxBfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 2, 4)
)
ciscoDot11HtPhyTxBfGroup.setObjects(
      *(("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyRxStaggerSoundImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyTxStaggerSoundImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyRxZLFImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyTxZLFImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyImplicitTxBFImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyCalibrationImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExplCSITxBFImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExplUncompSteerMatrixImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExplBFCSIFdbkImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExplUncompSteerMatrixFdbkImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyExplCompSteerMatrixFdbkImplemented"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyNumberBeamFormingCSISupportAntenna"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyNumberUncompSteerMatrixSupportAntenna"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyNumberCompSteerMatrixSupportAntenna"))
)
if mibBuilder.loadTexts:
    ciscoDot11HtPhyTxBfGroup.setStatus("current")

ciscoDot11HtPhyEnhPowerLevelsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 2, 5)
)
ciscoDot11HtPhyEnhPowerLevelsGroup.setObjects(
      *(("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyEnhPowerLevel20MHz"),
        ("CISCO-DOT11-HT-PHY-MIB", "cD11HtPhyEnhPowerLevel40MHz"))
)
if mibBuilder.loadTexts:
    ciscoDot11HtPhyEnhPowerLevelsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDot11HtMacCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 607, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDot11HtMacCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-HT-PHY-MIB",
    **{"CD11HtPhyBeamformFeedback": CD11HtPhyBeamformFeedback,
       "ciscoDot11HtPhyMIB": ciscoDot11HtPhyMIB,
       "ciscoDot11HtPhyMIBNotifs": ciscoDot11HtPhyMIBNotifs,
       "ciscoDot11HtPhyMIBObjects": ciscoDot11HtPhyMIBObjects,
       "cD11HtPhy": cD11HtPhy,
       "cD11HtPhyAntennaTable": cD11HtPhyAntennaTable,
       "cD11HtPhyAntennaEntry": cD11HtPhyAntennaEntry,
       "cD11HtPhyAntennaSelectionImplemented": cD11HtPhyAntennaSelectionImplemented,
       "cD11HtPhyXmitExpCSIFdbkASImplemented": cD11HtPhyXmitExpCSIFdbkASImplemented,
       "cD11HtPhyXmitIndFdbkASImplemented": cD11HtPhyXmitIndFdbkASImplemented,
       "cD11HtPhyExplCSIFdbkASImplemented": cD11HtPhyExplCSIFdbkASImplemented,
       "cD11HtPhyXmitIndCompFdbkASImplemented": cD11HtPhyXmitIndCompFdbkASImplemented,
       "cD11HtPhyRcvAntennaSelImplemented": cD11HtPhyRcvAntennaSelImplemented,
       "cD11HtPhyXmitSoundPPDUImplemented": cD11HtPhyXmitSoundPPDUImplemented,
       "cD11HtPhyTable": cD11HtPhyTable,
       "cD11HtPhyEntry": cD11HtPhyEntry,
       "cD11HtPhyOperatingMode": cD11HtPhyOperatingMode,
       "cD11HtPhyOperModeFrequency": cD11HtPhyOperModeFrequency,
       "cD11HtPhyOperBand": cD11HtPhyOperBand,
       "cD11HtPhyFortyMHzOperationImplemented": cD11HtPhyFortyMHzOperationImplemented,
       "cD11HtPhyFortyMHzOperationEnabled": cD11HtPhyFortyMHzOperationEnabled,
       "cD11HtPhyCurrentControlChannel": cD11HtPhyCurrentControlChannel,
       "cD11HtPhyCurrentExtensionChannel": cD11HtPhyCurrentExtensionChannel,
       "cD11HtPhyExtChannelCCAImplemented": cD11HtPhyExtChannelCCAImplemented,
       "cD11HtPhyNumberOfSpatialStreamsImplemented": cD11HtPhyNumberOfSpatialStreamsImplemented,
       "cD11HtPhyNumberOfSpatialStreamsEnabled": cD11HtPhyNumberOfSpatialStreamsEnabled,
       "cD11HtPhyGreenFieldImplemented": cD11HtPhyGreenFieldImplemented,
       "cD11HtPhyGreenFieldEnabled": cD11HtPhyGreenFieldEnabled,
       "cD11HtPhyShortGIInTwentyImplemented": cD11HtPhyShortGIInTwentyImplemented,
       "cD11HtPhyShortGIInTwentyEnabled": cD11HtPhyShortGIInTwentyEnabled,
       "cD11HtPhyShortGIInFortyImplemented": cD11HtPhyShortGIInFortyImplemented,
       "cD11HtPhyShortGIInFortyEnabled": cD11HtPhyShortGIInFortyEnabled,
       "cD11HtPhyAdvancedCodingImplemented": cD11HtPhyAdvancedCodingImplemented,
       "cD11HtPhyAdvancedCodingEnabled": cD11HtPhyAdvancedCodingEnabled,
       "cD11HtPhyTxSTBCImplemented": cD11HtPhyTxSTBCImplemented,
       "cD11HtPhyTxSTBCEnabled": cD11HtPhyTxSTBCEnabled,
       "cD11HtPhyRxSTBCImplemented": cD11HtPhyRxSTBCImplemented,
       "cD11HtPhyRxSTBCEnabled": cD11HtPhyRxSTBCEnabled,
       "cD11HtPhyBeamFormingImplemented": cD11HtPhyBeamFormingImplemented,
       "cD11HtPhyBeamFormingEnabled": cD11HtPhyBeamFormingEnabled,
       "cD11HtPhySupportedMCSTable": cD11HtPhySupportedMCSTable,
       "cD11HtPhySupportedMCSEntry": cD11HtPhySupportedMCSEntry,
       "cD11HtPhySupportedMCSTxValue": cD11HtPhySupportedMCSTxValue,
       "cD11HtPhySupportedMCSRxValue": cD11HtPhySupportedMCSRxValue,
       "cD11HtPhyTxBFConfigTable": cD11HtPhyTxBFConfigTable,
       "cD11HtPhyTxBFConfigEntry": cD11HtPhyTxBFConfigEntry,
       "cD11HtPhyRxStaggerSoundImplemented": cD11HtPhyRxStaggerSoundImplemented,
       "cD11HtPhyTxStaggerSoundImplemented": cD11HtPhyTxStaggerSoundImplemented,
       "cD11HtPhyRxZLFImplemented": cD11HtPhyRxZLFImplemented,
       "cD11HtPhyTxZLFImplemented": cD11HtPhyTxZLFImplemented,
       "cD11HtPhyImplicitTxBFImplemented": cD11HtPhyImplicitTxBFImplemented,
       "cD11HtPhyCalibrationImplemented": cD11HtPhyCalibrationImplemented,
       "cD11HtPhyExplCSITxBFImplemented": cD11HtPhyExplCSITxBFImplemented,
       "cD11HtPhyExplUncompSteerMatrixImplemented": cD11HtPhyExplUncompSteerMatrixImplemented,
       "cD11HtPhyExplBFCSIFdbkImplemented": cD11HtPhyExplBFCSIFdbkImplemented,
       "cD11HtPhyExplUncompSteerMatrixFdbkImplemented": cD11HtPhyExplUncompSteerMatrixFdbkImplemented,
       "cD11HtPhyExplCompSteerMatrixFdbkImplemented": cD11HtPhyExplCompSteerMatrixFdbkImplemented,
       "cD11HtPhyNumberBeamFormingCSISupportAntenna": cD11HtPhyNumberBeamFormingCSISupportAntenna,
       "cD11HtPhyNumberUncompSteerMatrixSupportAntenna": cD11HtPhyNumberUncompSteerMatrixSupportAntenna,
       "cD11HtPhyNumberCompSteerMatrixSupportAntenna": cD11HtPhyNumberCompSteerMatrixSupportAntenna,
       "cD11HtPhyEnhPowerTable": cD11HtPhyEnhPowerTable,
       "cD11HtPhyEnhPowerEntry": cD11HtPhyEnhPowerEntry,
       "cD11HtPhyEnhPowerLevel20MHz": cD11HtPhyEnhPowerLevel20MHz,
       "cD11HtPhyEnhPowerLevel40MHz": cD11HtPhyEnhPowerLevel40MHz,
       "ciscoDot11HtPhyMIBConform": ciscoDot11HtPhyMIBConform,
       "ciscoDot11HtPhyMIBCompliances": ciscoDot11HtPhyMIBCompliances,
       "ciscoDot11HtMacCompliance": ciscoDot11HtMacCompliance,
       "ciscoDot11HtPhyMIBGroups": ciscoDot11HtPhyMIBGroups,
       "ciscoDot11HtPhyAntennaGroup": ciscoDot11HtPhyAntennaGroup,
       "ciscoDot11HtPhyConfigGroup": ciscoDot11HtPhyConfigGroup,
       "ciscoDot11HtPhyMcsGroup": ciscoDot11HtPhyMcsGroup,
       "ciscoDot11HtPhyTxBfGroup": ciscoDot11HtPhyTxBfGroup,
       "ciscoDot11HtPhyEnhPowerLevelsGroup": ciscoDot11HtPhyEnhPowerLevelsGroup}
)
