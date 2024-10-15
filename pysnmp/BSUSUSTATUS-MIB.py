# SNMP MIB module (BSUSUSTATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BSUSUSTATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:49 2024
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

(aniBsuSuGroup,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "aniBsuSuGroup")

(aniBsuWirelessPort,) = mibBuilder.importSymbols(
    "BSUWIRELESSIF-MIB",
    "aniBsuWirelessPort")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

aniBsuSuStatus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniBsuSuUSLinkStatusTable_Object = MibTable
aniBsuSuUSLinkStatusTable = _AniBsuSuUSLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 1)
)
if mibBuilder.loadTexts:
    aniBsuSuUSLinkStatusTable.setStatus("current")
_AniBsuSuUSLinkStatusEntry_Object = MibTableRow
aniBsuSuUSLinkStatusEntry = _AniBsuSuUSLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 1, 1)
)
aniBsuSuUSLinkStatusEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
    (0, "BSUSUSTATUS-MIB", "aniBsuSuStatusMacAddr"),
)
if mibBuilder.loadTexts:
    aniBsuSuUSLinkStatusEntry.setStatus("current")
_AniBsuSuStatusMacAddr_Type = MacAddress
_AniBsuSuStatusMacAddr_Object = MibTableColumn
aniBsuSuStatusMacAddr = _AniBsuSuStatusMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 1, 1, 1),
    _AniBsuSuStatusMacAddr_Type()
)
aniBsuSuStatusMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusMacAddr.setStatus("current")
_AniBsuSuStatusIpAddr_Type = IpAddress
_AniBsuSuStatusIpAddr_Object = MibTableColumn
aniBsuSuStatusIpAddr = _AniBsuSuStatusIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 1, 1, 2),
    _AniBsuSuStatusIpAddr_Type()
)
aniBsuSuStatusIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusIpAddr.setStatus("current")


class _AniBsuSuStatusUSPolarization_Type(Integer32):
    """Custom type aniBsuSuStatusUSPolarization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("horizontal", 1),
          ("vertical", 2))
    )


_AniBsuSuStatusUSPolarization_Type.__name__ = "Integer32"
_AniBsuSuStatusUSPolarization_Object = MibTableColumn
aniBsuSuStatusUSPolarization = _AniBsuSuStatusUSPolarization_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 1, 1, 3),
    _AniBsuSuStatusUSPolarization_Type()
)
aniBsuSuStatusUSPolarization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusUSPolarization.setStatus("current")


class _AniBsuSuStatusUSModulation_Type(Integer32):
    """Custom type aniBsuSuStatusUSModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qam16", 2),
          ("qpsk", 1))
    )


_AniBsuSuStatusUSModulation_Type.__name__ = "Integer32"
_AniBsuSuStatusUSModulation_Object = MibTableColumn
aniBsuSuStatusUSModulation = _AniBsuSuStatusUSModulation_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 1, 1, 4),
    _AniBsuSuStatusUSModulation_Type()
)
aniBsuSuStatusUSModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusUSModulation.setStatus("current")


class _AniBsuSuStatusUSFec_Type(Integer32):
    """Custom type aniBsuSuStatusUSFec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_AniBsuSuStatusUSFec_Type.__name__ = "Integer32"
_AniBsuSuStatusUSFec_Object = MibTableColumn
aniBsuSuStatusUSFec = _AniBsuSuStatusUSFec_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 1, 1, 5),
    _AniBsuSuStatusUSFec_Type()
)
aniBsuSuStatusUSFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusUSFec.setStatus("current")


class _AniBsuSuStatusSuTxPowerAttn_Type(Integer32):
    """Custom type aniBsuSuStatusSuTxPowerAttn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 62),
    )


_AniBsuSuStatusSuTxPowerAttn_Type.__name__ = "Integer32"
_AniBsuSuStatusSuTxPowerAttn_Object = MibTableColumn
aniBsuSuStatusSuTxPowerAttn = _AniBsuSuStatusSuTxPowerAttn_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 1, 1, 6),
    _AniBsuSuStatusSuTxPowerAttn_Type()
)
aniBsuSuStatusSuTxPowerAttn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusSuTxPowerAttn.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuSuStatusSuTxPowerAttn.setUnits("dB")
_AniBsuSuStatusUSRxPower_Type = Integer32
_AniBsuSuStatusUSRxPower_Object = MibTableColumn
aniBsuSuStatusUSRxPower = _AniBsuSuStatusUSRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 1, 1, 7),
    _AniBsuSuStatusUSRxPower_Type()
)
aniBsuSuStatusUSRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusUSRxPower.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuSuStatusUSRxPower.setUnits("dBm")
_AniBsuSuStatusSuTxPower_Type = Integer32
_AniBsuSuStatusSuTxPower_Object = MibTableColumn
aniBsuSuStatusSuTxPower = _AniBsuSuStatusSuTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 1, 1, 8),
    _AniBsuSuStatusSuTxPower_Type()
)
aniBsuSuStatusSuTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusSuTxPower.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuSuStatusSuTxPower.setUnits("dBm")
_AniBsuSuDSLinkStatusTable_Object = MibTable
aniBsuSuDSLinkStatusTable = _AniBsuSuDSLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 2)
)
if mibBuilder.loadTexts:
    aniBsuSuDSLinkStatusTable.setStatus("current")
_AniBsuSuDSLinkStatusEntry_Object = MibTableRow
aniBsuSuDSLinkStatusEntry = _AniBsuSuDSLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 2, 1)
)
aniBsuSuDSLinkStatusEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
    (0, "BSUSUSTATUS-MIB", "aniBsuSuStatusMacAddr"),
)
if mibBuilder.loadTexts:
    aniBsuSuDSLinkStatusEntry.setStatus("current")


class _AniBsuSuStatusDSPolarization_Type(Integer32):
    """Custom type aniBsuSuStatusDSPolarization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("horizontal", 1),
          ("vertical", 2))
    )


_AniBsuSuStatusDSPolarization_Type.__name__ = "Integer32"
_AniBsuSuStatusDSPolarization_Object = MibTableColumn
aniBsuSuStatusDSPolarization = _AniBsuSuStatusDSPolarization_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 2, 1, 1),
    _AniBsuSuStatusDSPolarization_Type()
)
aniBsuSuStatusDSPolarization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusDSPolarization.setStatus("current")


class _AniBsuSuStatusDSModulation_Type(Integer32):
    """Custom type aniBsuSuStatusDSModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qam16", 2),
          ("qpsk", 1))
    )


_AniBsuSuStatusDSModulation_Type.__name__ = "Integer32"
_AniBsuSuStatusDSModulation_Object = MibTableColumn
aniBsuSuStatusDSModulation = _AniBsuSuStatusDSModulation_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 2, 1, 2),
    _AniBsuSuStatusDSModulation_Type()
)
aniBsuSuStatusDSModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusDSModulation.setStatus("current")


class _AniBsuSuStatusDSFec_Type(Integer32):
    """Custom type aniBsuSuStatusDSFec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_AniBsuSuStatusDSFec_Type.__name__ = "Integer32"
_AniBsuSuStatusDSFec_Object = MibTableColumn
aniBsuSuStatusDSFec = _AniBsuSuStatusDSFec_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 2, 1, 3),
    _AniBsuSuStatusDSFec_Type()
)
aniBsuSuStatusDSFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusDSFec.setStatus("current")
_AniBsuSuStatusDSRxPower_Type = DisplayString
_AniBsuSuStatusDSRxPower_Object = MibTableColumn
aniBsuSuStatusDSRxPower = _AniBsuSuStatusDSRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 2, 1, 5),
    _AniBsuSuStatusDSRxPower_Type()
)
aniBsuSuStatusDSRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusDSRxPower.setStatus("current")
_AniBsuSuStatusBsuTxPower_Type = Integer32
_AniBsuSuStatusBsuTxPower_Object = MibTableColumn
aniBsuSuStatusBsuTxPower = _AniBsuSuStatusBsuTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 2, 1, 6),
    _AniBsuSuStatusBsuTxPower_Type()
)
aniBsuSuStatusBsuTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusBsuTxPower.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuSuStatusBsuTxPower.setUnits("dBm")
_AniBsuSuLinkStatusTable_Object = MibTable
aniBsuSuLinkStatusTable = _AniBsuSuLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 3)
)
if mibBuilder.loadTexts:
    aniBsuSuLinkStatusTable.setStatus("current")
_AniBsuSuLinkStatusEntry_Object = MibTableRow
aniBsuSuLinkStatusEntry = _AniBsuSuLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 3, 1)
)
aniBsuSuLinkStatusEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
    (0, "BSUSUSTATUS-MIB", "aniBsuSuStatusMacAddr"),
)
if mibBuilder.loadTexts:
    aniBsuSuLinkStatusEntry.setStatus("current")
_AniBsuSuStatusIpAddress_Type = IpAddress
_AniBsuSuStatusIpAddress_Object = MibTableColumn
aniBsuSuStatusIpAddress = _AniBsuSuStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 3, 1, 1),
    _AniBsuSuStatusIpAddress_Type()
)
aniBsuSuStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusIpAddress.setStatus("current")
_AniBsuSuStatusPropagationDelay_Type = Integer32
_AniBsuSuStatusPropagationDelay_Object = MibTableColumn
aniBsuSuStatusPropagationDelay = _AniBsuSuStatusPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 3, 1, 2),
    _AniBsuSuStatusPropagationDelay_Type()
)
aniBsuSuStatusPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusPropagationDelay.setStatus("current")
_AniBsuSuStatusDistance_Type = DisplayString
_AniBsuSuStatusDistance_Object = MibTableColumn
aniBsuSuStatusDistance = _AniBsuSuStatusDistance_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 3, 1, 3),
    _AniBsuSuStatusDistance_Type()
)
aniBsuSuStatusDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusDistance.setStatus("current")
_AniBsuSuStatusLinkType_Type = DisplayString
_AniBsuSuStatusLinkType_Object = MibTableColumn
aniBsuSuStatusLinkType = _AniBsuSuStatusLinkType_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 3, 1, 4),
    _AniBsuSuStatusLinkType_Type()
)
aniBsuSuStatusLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusLinkType.setStatus("current")
_AniBsuSuStatusPathLossExponent_Type = DisplayString
_AniBsuSuStatusPathLossExponent_Object = MibTableColumn
aniBsuSuStatusPathLossExponent = _AniBsuSuStatusPathLossExponent_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 3, 3, 1, 5),
    _AniBsuSuStatusPathLossExponent_Type()
)
aniBsuSuStatusPathLossExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuStatusPathLossExponent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BSUSUSTATUS-MIB",
    **{"aniBsuSuStatus": aniBsuSuStatus,
       "aniBsuSuUSLinkStatusTable": aniBsuSuUSLinkStatusTable,
       "aniBsuSuUSLinkStatusEntry": aniBsuSuUSLinkStatusEntry,
       "aniBsuSuStatusMacAddr": aniBsuSuStatusMacAddr,
       "aniBsuSuStatusIpAddr": aniBsuSuStatusIpAddr,
       "aniBsuSuStatusUSPolarization": aniBsuSuStatusUSPolarization,
       "aniBsuSuStatusUSModulation": aniBsuSuStatusUSModulation,
       "aniBsuSuStatusUSFec": aniBsuSuStatusUSFec,
       "aniBsuSuStatusSuTxPowerAttn": aniBsuSuStatusSuTxPowerAttn,
       "aniBsuSuStatusUSRxPower": aniBsuSuStatusUSRxPower,
       "aniBsuSuStatusSuTxPower": aniBsuSuStatusSuTxPower,
       "aniBsuSuDSLinkStatusTable": aniBsuSuDSLinkStatusTable,
       "aniBsuSuDSLinkStatusEntry": aniBsuSuDSLinkStatusEntry,
       "aniBsuSuStatusDSPolarization": aniBsuSuStatusDSPolarization,
       "aniBsuSuStatusDSModulation": aniBsuSuStatusDSModulation,
       "aniBsuSuStatusDSFec": aniBsuSuStatusDSFec,
       "aniBsuSuStatusDSRxPower": aniBsuSuStatusDSRxPower,
       "aniBsuSuStatusBsuTxPower": aniBsuSuStatusBsuTxPower,
       "aniBsuSuLinkStatusTable": aniBsuSuLinkStatusTable,
       "aniBsuSuLinkStatusEntry": aniBsuSuLinkStatusEntry,
       "aniBsuSuStatusIpAddress": aniBsuSuStatusIpAddress,
       "aniBsuSuStatusPropagationDelay": aniBsuSuStatusPropagationDelay,
       "aniBsuSuStatusDistance": aniBsuSuStatusDistance,
       "aniBsuSuStatusLinkType": aniBsuSuStatusLinkType,
       "aniBsuSuStatusPathLossExponent": aniBsuSuStatusPathLossExponent}
)
