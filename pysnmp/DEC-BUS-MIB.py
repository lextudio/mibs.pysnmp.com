# SNMP MIB module (DEC-BUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEC-BUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:33 2024
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

(decMIBextension,) = mibBuilder.importSymbols(
    "DECATM-MIB",
    "decMIBextension")

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

_DecBusMIB_ObjectIdentity = ObjectIdentity
decBusMIB = _DecBusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29)
)
_DecBusMIBObjects_ObjectIdentity = ObjectIdentity
decBusMIBObjects = _DecBusMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1)
)
_DecBusConfigTable_Object = MibTable
decBusConfigTable = _DecBusConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1)
)
if mibBuilder.loadTexts:
    decBusConfigTable.setStatus("mandatory")
_DecBusConfigEntry_Object = MibTableRow
decBusConfigEntry = _DecBusConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1, 1)
)
decBusConfigEntry.setIndexNames(
    (0, "DEC-BUS-MIB", "decBusIndex"),
)
if mibBuilder.loadTexts:
    decBusConfigEntry.setStatus("mandatory")
_DecBusIndex_Type = Integer32
_DecBusIndex_Object = MibTableColumn
decBusIndex = _DecBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1, 1, 1),
    _DecBusIndex_Type()
)
decBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusIndex.setStatus("mandatory")


class _DecBusRowStatus_Type(Integer32):
    """Custom type decBusRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecBusRowStatus_Type.__name__ = "Integer32"
_DecBusRowStatus_Object = MibTableColumn
decBusRowStatus = _DecBusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1, 1, 2),
    _DecBusRowStatus_Type()
)
decBusRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusRowStatus.setStatus("mandatory")


class _DecBusAdminStatus_Type(Integer32):
    """Custom type decBusAdminStatus based on Integer32"""
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


_DecBusAdminStatus_Type.__name__ = "Integer32"
_DecBusAdminStatus_Object = MibTableColumn
decBusAdminStatus = _DecBusAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1, 1, 3),
    _DecBusAdminStatus_Type()
)
decBusAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusAdminStatus.setStatus("mandatory")


class _DecBusOperStatus_Type(Integer32):
    """Custom type decBusOperStatus based on Integer32"""
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
        *(("deleting", 4),
          ("disabling", 3),
          ("down", 2),
          ("up", 1))
    )


_DecBusOperStatus_Type.__name__ = "Integer32"
_DecBusOperStatus_Object = MibTableColumn
decBusOperStatus = _DecBusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1, 1, 4),
    _DecBusOperStatus_Type()
)
decBusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusOperStatus.setStatus("mandatory")
_DecBusLastChange_Type = TimeTicks
_DecBusLastChange_Object = MibTableColumn
decBusLastChange = _DecBusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1, 1, 5),
    _DecBusLastChange_Type()
)
decBusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusLastChange.setStatus("mandatory")


class _DecBusAtmAddress_Type(OctetString):
    """Custom type decBusAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecBusAtmAddress_Type.__name__ = "OctetString"
_DecBusAtmAddress_Object = MibTableColumn
decBusAtmAddress = _DecBusAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1, 1, 6),
    _DecBusAtmAddress_Type()
)
decBusAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusAtmAddress.setStatus("mandatory")


class _DecBusDescription_Type(OctetString):
    """Custom type decBusDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DecBusDescription_Type.__name__ = "OctetString"
_DecBusDescription_Object = MibTableColumn
decBusDescription = _DecBusDescription_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1, 1, 7),
    _DecBusDescription_Type()
)
decBusDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusDescription.setStatus("mandatory")


class _DecBusLanName_Type(OctetString):
    """Custom type decBusLanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DecBusLanName_Type.__name__ = "OctetString"
_DecBusLanName_Object = MibTableColumn
decBusLanName = _DecBusLanName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1, 1, 8),
    _DecBusLanName_Type()
)
decBusLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusLanName.setStatus("mandatory")


class _DecBusLanType_Type(Integer32):
    """Custom type decBusLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aflane8023", 2),
          ("aflane8025", 3))
    )


_DecBusLanType_Type.__name__ = "Integer32"
_DecBusLanType_Object = MibTableColumn
decBusLanType = _DecBusLanType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1, 1, 9),
    _DecBusLanType_Type()
)
decBusLanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusLanType.setStatus("mandatory")


class _DecBusMaxDataFrameSize_Type(Integer32):
    """Custom type decBusMaxDataFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("max1516", 2),
          ("max18190", 5),
          ("max4544", 3),
          ("max9234", 4))
    )


_DecBusMaxDataFrameSize_Type.__name__ = "Integer32"
_DecBusMaxDataFrameSize_Object = MibTableColumn
decBusMaxDataFrameSize = _DecBusMaxDataFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1, 1, 10),
    _DecBusMaxDataFrameSize_Type()
)
decBusMaxDataFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusMaxDataFrameSize.setStatus("mandatory")


class _DecBusMaxFrameAge_Type(Integer32):
    """Custom type decBusMaxFrameAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DecBusMaxFrameAge_Type.__name__ = "Integer32"
_DecBusMaxFrameAge_Object = MibTableColumn
decBusMaxFrameAge = _DecBusMaxFrameAge_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1, 1, 11),
    _DecBusMaxFrameAge_Type()
)
decBusMaxFrameAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusMaxFrameAge.setStatus("mandatory")


class _DecBusMaxForwardingRate_Type(Integer32):
    """Custom type decBusMaxForwardingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DecBusMaxForwardingRate_Type.__name__ = "Integer32"
_DecBusMaxForwardingRate_Object = MibTableColumn
decBusMaxForwardingRate = _DecBusMaxForwardingRate_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 1, 1, 12),
    _DecBusMaxForwardingRate_Type()
)
decBusMaxForwardingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusMaxForwardingRate.setStatus("mandatory")
_DecBusClientStatesTable_Object = MibTable
decBusClientStatesTable = _DecBusClientStatesTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 2)
)
if mibBuilder.loadTexts:
    decBusClientStatesTable.setStatus("mandatory")
_DecBusClientStatesEntry_Object = MibTableRow
decBusClientStatesEntry = _DecBusClientStatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 2, 1)
)
decBusClientStatesEntry.setIndexNames(
    (0, "DEC-BUS-MIB", "decBusIndex"),
)
if mibBuilder.loadTexts:
    decBusClientStatesEntry.setStatus("mandatory")
_DecBusActiveClients_Type = Integer32
_DecBusActiveClients_Object = MibTableColumn
decBusActiveClients = _DecBusActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 2, 1, 1),
    _DecBusActiveClients_Type()
)
decBusActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusActiveClients.setStatus("mandatory")
_DecBusMulticastFwdInProgress_Type = Integer32
_DecBusMulticastFwdInProgress_Object = MibTableColumn
decBusMulticastFwdInProgress = _DecBusMulticastFwdInProgress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 2, 1, 2),
    _DecBusMulticastFwdInProgress_Type()
)
decBusMulticastFwdInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMulticastFwdInProgress.setStatus("mandatory")
_DecBusTerminating_Type = Integer32
_DecBusTerminating_Object = MibTableColumn
decBusTerminating = _DecBusTerminating_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 2, 1, 3),
    _DecBusTerminating_Type()
)
decBusTerminating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusTerminating.setStatus("mandatory")
_DecBusTrafficTable_Object = MibTable
decBusTrafficTable = _DecBusTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 3)
)
if mibBuilder.loadTexts:
    decBusTrafficTable.setStatus("mandatory")
_DecBusTrafficEntry_Object = MibTableRow
decBusTrafficEntry = _DecBusTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 3, 1)
)
decBusTrafficEntry.setIndexNames(
    (0, "DEC-BUS-MIB", "decBusIndex"),
)
if mibBuilder.loadTexts:
    decBusTrafficEntry.setStatus("mandatory")
_DecBusFramesForwarded_Type = Counter32
_DecBusFramesForwarded_Object = MibTableColumn
decBusFramesForwarded = _DecBusFramesForwarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 3, 1, 1),
    _DecBusFramesForwarded_Type()
)
decBusFramesForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusFramesForwarded.setStatus("mandatory")
_DecBusInvalidFrames_Type = Counter32
_DecBusInvalidFrames_Object = MibTableColumn
decBusInvalidFrames = _DecBusInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 3, 1, 2),
    _DecBusInvalidFrames_Type()
)
decBusInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusInvalidFrames.setStatus("mandatory")
_DecBusFramesAgedOut_Type = Counter32
_DecBusFramesAgedOut_Object = MibTableColumn
decBusFramesAgedOut = _DecBusFramesAgedOut_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 3, 1, 3),
    _DecBusFramesAgedOut_Type()
)
decBusFramesAgedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusFramesAgedOut.setStatus("mandatory")
_DecBusFramesRateLimited_Type = Counter32
_DecBusFramesRateLimited_Object = MibTableColumn
decBusFramesRateLimited = _DecBusFramesRateLimited_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 3, 1, 4),
    _DecBusFramesRateLimited_Type()
)
decBusFramesRateLimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusFramesRateLimited.setStatus("mandatory")
_DecBusFramesDiscarded_Type = Counter32
_DecBusFramesDiscarded_Object = MibTableColumn
decBusFramesDiscarded = _DecBusFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 3, 1, 5),
    _DecBusFramesDiscarded_Type()
)
decBusFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusFramesDiscarded.setStatus("mandatory")
_DecBusClientTable_Object = MibTable
decBusClientTable = _DecBusClientTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 4)
)
if mibBuilder.loadTexts:
    decBusClientTable.setStatus("mandatory")
_DecBusClientEntry_Object = MibTableRow
decBusClientEntry = _DecBusClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 4, 1)
)
decBusClientEntry.setIndexNames(
    (0, "DEC-BUS-MIB", "decBusIndex"),
    (0, "DEC-BUS-MIB", "decBusClientIndex"),
)
if mibBuilder.loadTexts:
    decBusClientEntry.setStatus("mandatory")
_DecBusClientIndex_Type = Integer32
_DecBusClientIndex_Object = MibTableColumn
decBusClientIndex = _DecBusClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 4, 1, 1),
    _DecBusClientIndex_Type()
)
decBusClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusClientIndex.setStatus("mandatory")


class _DecBusClientAtmAddress_Type(OctetString):
    """Custom type decBusClientAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecBusClientAtmAddress_Type.__name__ = "OctetString"
_DecBusClientAtmAddress_Object = MibTableColumn
decBusClientAtmAddress = _DecBusClientAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 4, 1, 2),
    _DecBusClientAtmAddress_Type()
)
decBusClientAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusClientAtmAddress.setStatus("mandatory")


class _DecBusClientID_Type(Integer32):
    """Custom type decBusClientID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_DecBusClientID_Type.__name__ = "Integer32"
_DecBusClientID_Object = MibTableColumn
decBusClientID = _DecBusClientID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 4, 1, 3),
    _DecBusClientID_Type()
)
decBusClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusClientID.setStatus("mandatory")


class _DecBusClientUsedSeveralIDs_Type(Integer32):
    """Custom type decBusClientUsedSeveralIDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_DecBusClientUsedSeveralIDs_Type.__name__ = "Integer32"
_DecBusClientUsedSeveralIDs_Object = MibTableColumn
decBusClientUsedSeveralIDs = _DecBusClientUsedSeveralIDs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 4, 1, 4),
    _DecBusClientUsedSeveralIDs_Type()
)
decBusClientUsedSeveralIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusClientUsedSeveralIDs.setStatus("mandatory")


class _DecBusClientState_Type(Integer32):
    """Custom type decBusClientState based on Integer32"""
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
        *(("busConnect", 3),
          ("clientConnect", 4),
          ("deleting", 6),
          ("noBusConnect", 2),
          ("operational", 5),
          ("other", 1))
    )


_DecBusClientState_Type.__name__ = "Integer32"
_DecBusClientState_Object = MibTableColumn
decBusClientState = _DecBusClientState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 4, 1, 5),
    _DecBusClientState_Type()
)
decBusClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusClientState.setStatus("mandatory")


class _DecBusClientRowStatus_Type(Integer32):
    """Custom type decBusClientRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecBusClientRowStatus_Type.__name__ = "Integer32"
_DecBusClientRowStatus_Object = MibTableColumn
decBusClientRowStatus = _DecBusClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 4, 1, 6),
    _DecBusClientRowStatus_Type()
)
decBusClientRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusClientRowStatus.setStatus("mandatory")
_DecBusLecTable_Object = MibTable
decBusLecTable = _DecBusLecTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 5)
)
if mibBuilder.loadTexts:
    decBusLecTable.setStatus("mandatory")
_DecBusLecEntry_Object = MibTableRow
decBusLecEntry = _DecBusLecEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 5, 1)
)
decBusLecEntry.setIndexNames(
    (0, "DEC-BUS-MIB", "decBusIndex"),
    (0, "DEC-BUS-MIB", "decBusLecAtmAddress"),
)
if mibBuilder.loadTexts:
    decBusLecEntry.setStatus("mandatory")


class _DecBusLecAtmAddress_Type(OctetString):
    """Custom type decBusLecAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecBusLecAtmAddress_Type.__name__ = "OctetString"
_DecBusLecAtmAddress_Object = MibTableColumn
decBusLecAtmAddress = _DecBusLecAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 5, 1, 1),
    _DecBusLecAtmAddress_Type()
)
decBusLecAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusLecAtmAddress.setStatus("mandatory")
_DecBusLecIndex_Type = Integer32
_DecBusLecIndex_Object = MibTableColumn
decBusLecIndex = _DecBusLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 5, 1, 2),
    _DecBusLecIndex_Type()
)
decBusLecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusLecIndex.setStatus("mandatory")


class _DecBusLecID_Type(Integer32):
    """Custom type decBusLecID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_DecBusLecID_Type.__name__ = "Integer32"
_DecBusLecID_Object = MibTableColumn
decBusLecID = _DecBusLecID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 5, 1, 3),
    _DecBusLecID_Type()
)
decBusLecID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusLecID.setStatus("mandatory")


class _DecBusLecUsedSeveralIDs_Type(Integer32):
    """Custom type decBusLecUsedSeveralIDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_DecBusLecUsedSeveralIDs_Type.__name__ = "Integer32"
_DecBusLecUsedSeveralIDs_Object = MibTableColumn
decBusLecUsedSeveralIDs = _DecBusLecUsedSeveralIDs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 5, 1, 4),
    _DecBusLecUsedSeveralIDs_Type()
)
decBusLecUsedSeveralIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusLecUsedSeveralIDs.setStatus("mandatory")


class _DecBusLecState_Type(Integer32):
    """Custom type decBusLecState based on Integer32"""
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
        *(("busConnect", 3),
          ("clientConnect", 4),
          ("deleting", 6),
          ("noBusConnect", 2),
          ("operational", 5),
          ("other", 1))
    )


_DecBusLecState_Type.__name__ = "Integer32"
_DecBusLecState_Object = MibTableColumn
decBusLecState = _DecBusLecState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 5, 1, 5),
    _DecBusLecState_Type()
)
decBusLecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusLecState.setStatus("mandatory")


class _DecBusLecRowStatus_Type(Integer32):
    """Custom type decBusLecRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecBusLecRowStatus_Type.__name__ = "Integer32"
_DecBusLecRowStatus_Object = MibTableColumn
decBusLecRowStatus = _DecBusLecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 5, 1, 6),
    _DecBusLecRowStatus_Type()
)
decBusLecRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusLecRowStatus.setStatus("mandatory")
_DecBusMulticastSendTable_Object = MibTable
decBusMulticastSendTable = _DecBusMulticastSendTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 6)
)
if mibBuilder.loadTexts:
    decBusMulticastSendTable.setStatus("mandatory")
_DecBusMulticastSendEntry_Object = MibTableRow
decBusMulticastSendEntry = _DecBusMulticastSendEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 6, 1)
)
decBusMulticastSendEntry.setIndexNames(
    (0, "DEC-BUS-MIB", "decBusIndex"),
    (0, "DEC-BUS-MIB", "decBusLecAtmAddress"),
)
if mibBuilder.loadTexts:
    decBusMulticastSendEntry.setStatus("mandatory")


class _DecBusMulticastSendInterface_Type(Integer32):
    """Custom type decBusMulticastSendInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DecBusMulticastSendInterface_Type.__name__ = "Integer32"
_DecBusMulticastSendInterface_Object = MibTableColumn
decBusMulticastSendInterface = _DecBusMulticastSendInterface_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 6, 1, 1),
    _DecBusMulticastSendInterface_Type()
)
decBusMulticastSendInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusMulticastSendInterface.setStatus("mandatory")


class _DecBusMulticastSendVpi_Type(Integer32):
    """Custom type decBusMulticastSendVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DecBusMulticastSendVpi_Type.__name__ = "Integer32"
_DecBusMulticastSendVpi_Object = MibTableColumn
decBusMulticastSendVpi = _DecBusMulticastSendVpi_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 6, 1, 2),
    _DecBusMulticastSendVpi_Type()
)
decBusMulticastSendVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusMulticastSendVpi.setStatus("mandatory")


class _DecBusMulticastSendVci_Type(Integer32):
    """Custom type decBusMulticastSendVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DecBusMulticastSendVci_Type.__name__ = "Integer32"
_DecBusMulticastSendVci_Object = MibTableColumn
decBusMulticastSendVci = _DecBusMulticastSendVci_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 6, 1, 3),
    _DecBusMulticastSendVci_Type()
)
decBusMulticastSendVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusMulticastSendVci.setStatus("mandatory")


class _DecBusMulticastSendRowStatus_Type(Integer32):
    """Custom type decBusMulticastSendRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecBusMulticastSendRowStatus_Type.__name__ = "Integer32"
_DecBusMulticastSendRowStatus_Object = MibTableColumn
decBusMulticastSendRowStatus = _DecBusMulticastSendRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 6, 1, 4),
    _DecBusMulticastSendRowStatus_Type()
)
decBusMulticastSendRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusMulticastSendRowStatus.setStatus("mandatory")
_DecBusMulticastFwdTable_Object = MibTable
decBusMulticastFwdTable = _DecBusMulticastFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 7)
)
if mibBuilder.loadTexts:
    decBusMulticastFwdTable.setStatus("mandatory")
_DecBusMulticastFwdEntry_Object = MibTableRow
decBusMulticastFwdEntry = _DecBusMulticastFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 7, 1)
)
decBusMulticastFwdEntry.setIndexNames(
    (0, "DEC-BUS-MIB", "decBusIndex"),
    (0, "DEC-BUS-MIB", "decBusMulticastFwdInterface"),
    (0, "DEC-BUS-MIB", "decBusMulticastFwdVpi"),
    (0, "DEC-BUS-MIB", "decBusMulticastFwdVci"),
)
if mibBuilder.loadTexts:
    decBusMulticastFwdEntry.setStatus("mandatory")


class _DecBusMulticastFwdInterface_Type(Integer32):
    """Custom type decBusMulticastFwdInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DecBusMulticastFwdInterface_Type.__name__ = "Integer32"
_DecBusMulticastFwdInterface_Object = MibTableColumn
decBusMulticastFwdInterface = _DecBusMulticastFwdInterface_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 7, 1, 1),
    _DecBusMulticastFwdInterface_Type()
)
decBusMulticastFwdInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMulticastFwdInterface.setStatus("mandatory")


class _DecBusMulticastFwdVpi_Type(Integer32):
    """Custom type decBusMulticastFwdVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DecBusMulticastFwdVpi_Type.__name__ = "Integer32"
_DecBusMulticastFwdVpi_Object = MibTableColumn
decBusMulticastFwdVpi = _DecBusMulticastFwdVpi_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 7, 1, 2),
    _DecBusMulticastFwdVpi_Type()
)
decBusMulticastFwdVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMulticastFwdVpi.setStatus("mandatory")


class _DecBusMulticastFwdVci_Type(Integer32):
    """Custom type decBusMulticastFwdVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DecBusMulticastFwdVci_Type.__name__ = "Integer32"
_DecBusMulticastFwdVci_Object = MibTableColumn
decBusMulticastFwdVci = _DecBusMulticastFwdVci_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 7, 1, 3),
    _DecBusMulticastFwdVci_Type()
)
decBusMulticastFwdVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMulticastFwdVci.setStatus("mandatory")


class _DecBusMulticastFwdRowStatus_Type(Integer32):
    """Custom type decBusMulticastFwdRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DecBusMulticastFwdRowStatus_Type.__name__ = "Integer32"
_DecBusMulticastFwdRowStatus_Object = MibTableColumn
decBusMulticastFwdRowStatus = _DecBusMulticastFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 7, 1, 4),
    _DecBusMulticastFwdRowStatus_Type()
)
decBusMulticastFwdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusMulticastFwdRowStatus.setStatus("mandatory")
_DecBusCallStatsTable_Object = MibTable
decBusCallStatsTable = _DecBusCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 8)
)
if mibBuilder.loadTexts:
    decBusCallStatsTable.setStatus("mandatory")
_DecBusCallStatsEntry_Object = MibTableRow
decBusCallStatsEntry = _DecBusCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 8, 1)
)
decBusCallStatsEntry.setIndexNames(
    (0, "DEC-BUS-MIB", "decBusIndex"),
)
if mibBuilder.loadTexts:
    decBusCallStatsEntry.setStatus("mandatory")
_DecBusMulticastSendCalls_Type = Counter32
_DecBusMulticastSendCalls_Object = MibTableColumn
decBusMulticastSendCalls = _DecBusMulticastSendCalls_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 8, 1, 1),
    _DecBusMulticastSendCalls_Type()
)
decBusMulticastSendCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMulticastSendCalls.setStatus("mandatory")
_DecBusMulticastSendFailures_Type = Counter32
_DecBusMulticastSendFailures_Object = MibTableColumn
decBusMulticastSendFailures = _DecBusMulticastSendFailures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 8, 1, 2),
    _DecBusMulticastSendFailures_Type()
)
decBusMulticastSendFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMulticastSendFailures.setStatus("mandatory")
_DecBusMsOutOfResourcesFailures_Type = Counter32
_DecBusMsOutOfResourcesFailures_Object = MibTableColumn
decBusMsOutOfResourcesFailures = _DecBusMsOutOfResourcesFailures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 8, 1, 3),
    _DecBusMsOutOfResourcesFailures_Type()
)
decBusMsOutOfResourcesFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMsOutOfResourcesFailures.setStatus("mandatory")
_DecBusMsInvalidInfoElements_Type = Counter32
_DecBusMsInvalidInfoElements_Object = MibTableColumn
decBusMsInvalidInfoElements = _DecBusMsInvalidInfoElements_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 8, 1, 4),
    _DecBusMsInvalidInfoElements_Type()
)
decBusMsInvalidInfoElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMsInvalidInfoElements.setStatus("mandatory")
_DecBusMsWrongLanTypes_Type = Counter32
_DecBusMsWrongLanTypes_Object = MibTableColumn
decBusMsWrongLanTypes = _DecBusMsWrongLanTypes_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 8, 1, 5),
    _DecBusMsWrongLanTypes_Type()
)
decBusMsWrongLanTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMsWrongLanTypes.setStatus("mandatory")
_DecBusMsWrongMaxFrameSizes_Type = Counter32
_DecBusMsWrongMaxFrameSizes_Object = MibTableColumn
decBusMsWrongMaxFrameSizes = _DecBusMsWrongMaxFrameSizes_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 8, 1, 6),
    _DecBusMsWrongMaxFrameSizes_Type()
)
decBusMsWrongMaxFrameSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMsWrongMaxFrameSizes.setStatus("mandatory")
_DecBusMulticastForwardCalls_Type = Counter32
_DecBusMulticastForwardCalls_Object = MibTableColumn
decBusMulticastForwardCalls = _DecBusMulticastForwardCalls_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 8, 1, 7),
    _DecBusMulticastForwardCalls_Type()
)
decBusMulticastForwardCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMulticastForwardCalls.setStatus("mandatory")
_DecBusMulticastForwardFailures_Type = Counter32
_DecBusMulticastForwardFailures_Object = MibTableColumn
decBusMulticastForwardFailures = _DecBusMulticastForwardFailures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 8, 1, 8),
    _DecBusMulticastForwardFailures_Type()
)
decBusMulticastForwardFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMulticastForwardFailures.setStatus("mandatory")
_DecBusMfOutOfResourcesFailures_Type = Counter32
_DecBusMfOutOfResourcesFailures_Object = MibTableColumn
decBusMfOutOfResourcesFailures = _DecBusMfOutOfResourcesFailures_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 8, 1, 9),
    _DecBusMfOutOfResourcesFailures_Type()
)
decBusMfOutOfResourcesFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMfOutOfResourcesFailures.setStatus("mandatory")
_DecBusMfClientRejects_Type = Counter32
_DecBusMfClientRejects_Object = MibTableColumn
decBusMfClientRejects = _DecBusMfClientRejects_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 8, 1, 10),
    _DecBusMfClientRejects_Type()
)
decBusMfClientRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusMfClientRejects.setStatus("mandatory")
_DecBusEventLogMaximumSize_Type = Integer32
_DecBusEventLogMaximumSize_Object = MibScalar
decBusEventLogMaximumSize = _DecBusEventLogMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 9),
    _DecBusEventLogMaximumSize_Type()
)
decBusEventLogMaximumSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decBusEventLogMaximumSize.setStatus("mandatory")
_DecBusEventLogTable_Object = MibTable
decBusEventLogTable = _DecBusEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 10)
)
if mibBuilder.loadTexts:
    decBusEventLogTable.setStatus("mandatory")
_DecBusEventLogEntry_Object = MibTableRow
decBusEventLogEntry = _DecBusEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 10, 1)
)
decBusEventLogEntry.setIndexNames(
    (0, "DEC-BUS-MIB", "decBusEventIndex"),
)
if mibBuilder.loadTexts:
    decBusEventLogEntry.setStatus("mandatory")
_DecBusEventIndex_Type = Integer32
_DecBusEventIndex_Object = MibTableColumn
decBusEventIndex = _DecBusEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 10, 1, 1),
    _DecBusEventIndex_Type()
)
decBusEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusEventIndex.setStatus("mandatory")


class _DecBusEventType_Type(Integer32):
    """Custom type decBusEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("joinFailed", 1)
    )


_DecBusEventType_Type.__name__ = "Integer32"
_DecBusEventType_Object = MibTableColumn
decBusEventType = _DecBusEventType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 10, 1, 2),
    _DecBusEventType_Type()
)
decBusEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusEventType.setStatus("mandatory")


class _DecBusEventReason_Type(Integer32):
    """Custom type decBusEventReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
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
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              90,
              91,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 7),
          ("busConnectTimeout", 58),
          ("clientNotConnectedToLes", 59),
          ("controlDistributeFailure", 54),
          ("duplicateAtmAddress", 5),
          ("duplicateLanDestination", 4),
          ("insecureAtmAddress", 100),
          ("insufficientResources", 6),
          ("invalidAalMode", 90),
          ("invalidAalParameters", 81),
          ("invalidAalSccs", 91),
          ("invalidAtmAddress", 10),
          ("invalidAtmTrafficDescriptor", 82),
          ("invalidBlli", 84),
          ("invalidBroadbandBearerCapability", 83),
          ("invalidCalledPartyNumber", 86),
          ("invalidCallingPartyNumber", 85),
          ("invalidConnectionIdentifier", 87),
          ("invalidInformationElement", 80),
          ("invalidLanDestination", 9),
          ("invalidQosParameter", 88),
          ("invalidRequestParameters", 2),
          ("invalidRequestorId", 8),
          ("joinNotCompleted", 56),
          ("joinTimeout", 57),
          ("missingInformationElement", 70),
          ("multicastForwardFailure", 55),
          ("noAalParameters", 71),
          ("noAtmTrafficDescriptor", 72),
          ("noBlli", 74),
          ("noBroadbandBearerCapability", 73),
          ("noCalledPartyNumber", 76),
          ("noCallingPartyNumber", 75),
          ("noConnectionIdentifier", 77),
          ("noQosParameter", 78),
          ("nonDuplicateRequest", 53),
          ("unverifiedAtmAddress", 101),
          ("versionNotSupported", 1),
          ("wrongJoinMaxFrameSize", 52),
          ("wrongLanType", 50),
          ("wrongMaxFrameSize", 51))
    )


_DecBusEventReason_Type.__name__ = "Integer32"
_DecBusEventReason_Object = MibTableColumn
decBusEventReason = _DecBusEventReason_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 10, 1, 3),
    _DecBusEventReason_Type()
)
decBusEventReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusEventReason.setStatus("mandatory")
_DecBusEventServer_Type = Integer32
_DecBusEventServer_Object = MibTableColumn
decBusEventServer = _DecBusEventServer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 10, 1, 4),
    _DecBusEventServer_Type()
)
decBusEventServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusEventServer.setStatus("mandatory")


class _DecBusEventServerAtmAddress_Type(OctetString):
    """Custom type decBusEventServerAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecBusEventServerAtmAddress_Type.__name__ = "OctetString"
_DecBusEventServerAtmAddress_Object = MibTableColumn
decBusEventServerAtmAddress = _DecBusEventServerAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 10, 1, 5),
    _DecBusEventServerAtmAddress_Type()
)
decBusEventServerAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusEventServerAtmAddress.setStatus("mandatory")


class _DecBusEventClientAtmAddress_Type(OctetString):
    """Custom type decBusEventClientAtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DecBusEventClientAtmAddress_Type.__name__ = "OctetString"
_DecBusEventClientAtmAddress_Object = MibTableColumn
decBusEventClientAtmAddress = _DecBusEventClientAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 10, 1, 6),
    _DecBusEventClientAtmAddress_Type()
)
decBusEventClientAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusEventClientAtmAddress.setStatus("mandatory")
_DecBusEventTimestamp_Type = TimeTicks
_DecBusEventTimestamp_Object = MibTableColumn
decBusEventTimestamp = _DecBusEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 1, 10, 1, 7),
    _DecBusEventTimestamp_Type()
)
decBusEventTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decBusEventTimestamp.setStatus("mandatory")
_DecBusMIBConformance_ObjectIdentity = ObjectIdentity
decBusMIBConformance = _DecBusMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 2)
)
_DecBusMIBGroups_ObjectIdentity = ObjectIdentity
decBusMIBGroups = _DecBusMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 2, 1)
)
_DecBusConfigGroup_ObjectIdentity = ObjectIdentity
decBusConfigGroup = _DecBusConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 2, 1, 1)
)
_DecBusClientStatesGroup_ObjectIdentity = ObjectIdentity
decBusClientStatesGroup = _DecBusClientStatesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 2, 1, 2)
)
_DecBusTrafficGroup_ObjectIdentity = ObjectIdentity
decBusTrafficGroup = _DecBusTrafficGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 2, 1, 3)
)
_DecBusClientGroup_ObjectIdentity = ObjectIdentity
decBusClientGroup = _DecBusClientGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 2, 1, 4)
)
_DecBusLecGroup_ObjectIdentity = ObjectIdentity
decBusLecGroup = _DecBusLecGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 2, 1, 5)
)
_DecBusCircuitGroup_ObjectIdentity = ObjectIdentity
decBusCircuitGroup = _DecBusCircuitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 2, 1, 6)
)
_DecBusCallStatsGroup_ObjectIdentity = ObjectIdentity
decBusCallStatsGroup = _DecBusCallStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 2, 1, 7)
)
_DecBusEventLogGroup_ObjectIdentity = ObjectIdentity
decBusEventLogGroup = _DecBusEventLogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 2, 1, 8)
)
_DecBusMIBCompliances_ObjectIdentity = ObjectIdentity
decBusMIBCompliances = _DecBusMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 2, 2)
)
_DecBusMIBCompliance_ObjectIdentity = ObjectIdentity
decBusMIBCompliance = _DecBusMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 29, 2, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEC-BUS-MIB",
    **{"decBusMIB": decBusMIB,
       "decBusMIBObjects": decBusMIBObjects,
       "decBusConfigTable": decBusConfigTable,
       "decBusConfigEntry": decBusConfigEntry,
       "decBusIndex": decBusIndex,
       "decBusRowStatus": decBusRowStatus,
       "decBusAdminStatus": decBusAdminStatus,
       "decBusOperStatus": decBusOperStatus,
       "decBusLastChange": decBusLastChange,
       "decBusAtmAddress": decBusAtmAddress,
       "decBusDescription": decBusDescription,
       "decBusLanName": decBusLanName,
       "decBusLanType": decBusLanType,
       "decBusMaxDataFrameSize": decBusMaxDataFrameSize,
       "decBusMaxFrameAge": decBusMaxFrameAge,
       "decBusMaxForwardingRate": decBusMaxForwardingRate,
       "decBusClientStatesTable": decBusClientStatesTable,
       "decBusClientStatesEntry": decBusClientStatesEntry,
       "decBusActiveClients": decBusActiveClients,
       "decBusMulticastFwdInProgress": decBusMulticastFwdInProgress,
       "decBusTerminating": decBusTerminating,
       "decBusTrafficTable": decBusTrafficTable,
       "decBusTrafficEntry": decBusTrafficEntry,
       "decBusFramesForwarded": decBusFramesForwarded,
       "decBusInvalidFrames": decBusInvalidFrames,
       "decBusFramesAgedOut": decBusFramesAgedOut,
       "decBusFramesRateLimited": decBusFramesRateLimited,
       "decBusFramesDiscarded": decBusFramesDiscarded,
       "decBusClientTable": decBusClientTable,
       "decBusClientEntry": decBusClientEntry,
       "decBusClientIndex": decBusClientIndex,
       "decBusClientAtmAddress": decBusClientAtmAddress,
       "decBusClientID": decBusClientID,
       "decBusClientUsedSeveralIDs": decBusClientUsedSeveralIDs,
       "decBusClientState": decBusClientState,
       "decBusClientRowStatus": decBusClientRowStatus,
       "decBusLecTable": decBusLecTable,
       "decBusLecEntry": decBusLecEntry,
       "decBusLecAtmAddress": decBusLecAtmAddress,
       "decBusLecIndex": decBusLecIndex,
       "decBusLecID": decBusLecID,
       "decBusLecUsedSeveralIDs": decBusLecUsedSeveralIDs,
       "decBusLecState": decBusLecState,
       "decBusLecRowStatus": decBusLecRowStatus,
       "decBusMulticastSendTable": decBusMulticastSendTable,
       "decBusMulticastSendEntry": decBusMulticastSendEntry,
       "decBusMulticastSendInterface": decBusMulticastSendInterface,
       "decBusMulticastSendVpi": decBusMulticastSendVpi,
       "decBusMulticastSendVci": decBusMulticastSendVci,
       "decBusMulticastSendRowStatus": decBusMulticastSendRowStatus,
       "decBusMulticastFwdTable": decBusMulticastFwdTable,
       "decBusMulticastFwdEntry": decBusMulticastFwdEntry,
       "decBusMulticastFwdInterface": decBusMulticastFwdInterface,
       "decBusMulticastFwdVpi": decBusMulticastFwdVpi,
       "decBusMulticastFwdVci": decBusMulticastFwdVci,
       "decBusMulticastFwdRowStatus": decBusMulticastFwdRowStatus,
       "decBusCallStatsTable": decBusCallStatsTable,
       "decBusCallStatsEntry": decBusCallStatsEntry,
       "decBusMulticastSendCalls": decBusMulticastSendCalls,
       "decBusMulticastSendFailures": decBusMulticastSendFailures,
       "decBusMsOutOfResourcesFailures": decBusMsOutOfResourcesFailures,
       "decBusMsInvalidInfoElements": decBusMsInvalidInfoElements,
       "decBusMsWrongLanTypes": decBusMsWrongLanTypes,
       "decBusMsWrongMaxFrameSizes": decBusMsWrongMaxFrameSizes,
       "decBusMulticastForwardCalls": decBusMulticastForwardCalls,
       "decBusMulticastForwardFailures": decBusMulticastForwardFailures,
       "decBusMfOutOfResourcesFailures": decBusMfOutOfResourcesFailures,
       "decBusMfClientRejects": decBusMfClientRejects,
       "decBusEventLogMaximumSize": decBusEventLogMaximumSize,
       "decBusEventLogTable": decBusEventLogTable,
       "decBusEventLogEntry": decBusEventLogEntry,
       "decBusEventIndex": decBusEventIndex,
       "decBusEventType": decBusEventType,
       "decBusEventReason": decBusEventReason,
       "decBusEventServer": decBusEventServer,
       "decBusEventServerAtmAddress": decBusEventServerAtmAddress,
       "decBusEventClientAtmAddress": decBusEventClientAtmAddress,
       "decBusEventTimestamp": decBusEventTimestamp,
       "decBusMIBConformance": decBusMIBConformance,
       "decBusMIBGroups": decBusMIBGroups,
       "decBusConfigGroup": decBusConfigGroup,
       "decBusClientStatesGroup": decBusClientStatesGroup,
       "decBusTrafficGroup": decBusTrafficGroup,
       "decBusClientGroup": decBusClientGroup,
       "decBusLecGroup": decBusLecGroup,
       "decBusCircuitGroup": decBusCircuitGroup,
       "decBusCallStatsGroup": decBusCallStatsGroup,
       "decBusEventLogGroup": decBusEventLogGroup,
       "decBusMIBCompliances": decBusMIBCompliances,
       "decBusMIBCompliance": decBusMIBCompliance}
)
