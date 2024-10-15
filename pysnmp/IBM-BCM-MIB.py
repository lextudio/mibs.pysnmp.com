# SNMP MIB module (IBM-BCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-BCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:25 2024
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

(busConfEntry,
 busConfIndex) = mibBuilder.importSymbols(
    "LAN-EMULATION-BUS-MIB",
    "busConfEntry",
    "busConfIndex")

(AtmLaneAddress,) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "AtmLaneAddress")

(mssServerLanE,) = mibBuilder.importSymbols(
    "NWAYSMSS-MIB",
    "mssServerLanE")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class BcmCacheAge(Integer32):
    """Custom type BcmCacheAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbmBcmMIB_ObjectIdentity = ObjectIdentity
ibmBcmMIB = _IbmBcmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3)
)
_BcmConfGroup_ObjectIdentity = ObjectIdentity
bcmConfGroup = _BcmConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1)
)
_BcmConfTable_Object = MibTable
bcmConfTable = _BcmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    bcmConfTable.setStatus("mandatory")
_BcmConfEntry_Object = MibTableRow
bcmConfEntry = _BcmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 1, 1)
)
bcmConfEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
)
if mibBuilder.loadTexts:
    bcmConfEntry.setStatus("mandatory")
_BcmRouteCacheEnabled_Type = TruthValue
_BcmRouteCacheEnabled_Object = MibTableColumn
bcmRouteCacheEnabled = _BcmRouteCacheEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 1, 1, 1),
    _BcmRouteCacheEnabled_Type()
)
bcmRouteCacheEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmRouteCacheEnabled.setStatus("mandatory")
_BcmStaticTargetsNextId_Type = Integer32
_BcmStaticTargetsNextId_Object = MibScalar
bcmStaticTargetsNextId = _BcmStaticTargetsNextId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 2),
    _BcmStaticTargetsNextId_Type()
)
bcmStaticTargetsNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmStaticTargetsNextId.setStatus("mandatory")
_BcmStaticTargetsTable_Object = MibTable
bcmStaticTargetsTable = _BcmStaticTargetsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    bcmStaticTargetsTable.setStatus("mandatory")
_BcmStaticTargetsEntry_Object = MibTableRow
bcmStaticTargetsEntry = _BcmStaticTargetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 3, 1)
)
bcmStaticTargetsEntry.setIndexNames(
    (0, "IBM-BCM-MIB", "bcmStaticTargetsIndex"),
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
)
if mibBuilder.loadTexts:
    bcmStaticTargetsEntry.setStatus("mandatory")
_BcmStaticTargetsIndex_Type = Integer32
_BcmStaticTargetsIndex_Object = MibTableColumn
bcmStaticTargetsIndex = _BcmStaticTargetsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 3, 1, 1),
    _BcmStaticTargetsIndex_Type()
)
bcmStaticTargetsIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmStaticTargetsIndex.setStatus("mandatory")
_BcmStaticTargetsAtmAddress_Type = AtmLaneAddress
_BcmStaticTargetsAtmAddress_Object = MibTableColumn
bcmStaticTargetsAtmAddress = _BcmStaticTargetsAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 3, 1, 2),
    _BcmStaticTargetsAtmAddress_Type()
)
bcmStaticTargetsAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmStaticTargetsAtmAddress.setStatus("mandatory")
_BcmStaticTargetsMacAddress_Type = MacAddress
_BcmStaticTargetsMacAddress_Object = MibTableColumn
bcmStaticTargetsMacAddress = _BcmStaticTargetsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 3, 1, 3),
    _BcmStaticTargetsMacAddress_Type()
)
bcmStaticTargetsMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmStaticTargetsMacAddress.setStatus("mandatory")


class _BcmStaticTargetsProtocol_Type(Integer32):
    """Custom type bcmStaticTargetsProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ipx", 4),
          ("noStaticProtocolDefined", 0))
    )


_BcmStaticTargetsProtocol_Type.__name__ = "Integer32"
_BcmStaticTargetsProtocol_Object = MibTableColumn
bcmStaticTargetsProtocol = _BcmStaticTargetsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 3, 1, 4),
    _BcmStaticTargetsProtocol_Type()
)
bcmStaticTargetsProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmStaticTargetsProtocol.setStatus("mandatory")
_BcmStaticTargetsRowStatus_Type = RowStatus
_BcmStaticTargetsRowStatus_Object = MibTableColumn
bcmStaticTargetsRowStatus = _BcmStaticTargetsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 3, 1, 5),
    _BcmStaticTargetsRowStatus_Type()
)
bcmStaticTargetsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmStaticTargetsRowStatus.setStatus("mandatory")
_BcmIpConfTable_Object = MibTable
bcmIpConfTable = _BcmIpConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    bcmIpConfTable.setStatus("mandatory")
_BcmIpConfEntry_Object = MibTableRow
bcmIpConfEntry = _BcmIpConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 4, 1)
)
bcmIpConfEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
)
if mibBuilder.loadTexts:
    bcmIpConfEntry.setStatus("mandatory")


class _BcmIpConfOperStatus_Type(Integer32):
    """Custom type bcmIpConfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_BcmIpConfOperStatus_Type.__name__ = "Integer32"
_BcmIpConfOperStatus_Object = MibTableColumn
bcmIpConfOperStatus = _BcmIpConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 4, 1, 1),
    _BcmIpConfOperStatus_Type()
)
bcmIpConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpConfOperStatus.setStatus("mandatory")


class _BcmIpConfAdminStatus_Type(Integer32):
    """Custom type bcmIpConfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("up", 2))
    )


_BcmIpConfAdminStatus_Type.__name__ = "Integer32"
_BcmIpConfAdminStatus_Object = MibTableColumn
bcmIpConfAdminStatus = _BcmIpConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 4, 1, 2),
    _BcmIpConfAdminStatus_Type()
)
bcmIpConfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmIpConfAdminStatus.setStatus("mandatory")
_BcmIpConfCacheAge_Type = BcmCacheAge
_BcmIpConfCacheAge_Object = MibTableColumn
bcmIpConfCacheAge = _BcmIpConfCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 4, 1, 3),
    _BcmIpConfCacheAge_Type()
)
bcmIpConfCacheAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmIpConfCacheAge.setStatus("mandatory")
_BcmIpxConfTable_Object = MibTable
bcmIpxConfTable = _BcmIpxConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    bcmIpxConfTable.setStatus("mandatory")
_BcmIpxConfEntry_Object = MibTableRow
bcmIpxConfEntry = _BcmIpxConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 5, 1)
)
bcmIpxConfEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
)
if mibBuilder.loadTexts:
    bcmIpxConfEntry.setStatus("mandatory")


class _BcmIpxConfOperStatus_Type(Integer32):
    """Custom type bcmIpxConfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_BcmIpxConfOperStatus_Type.__name__ = "Integer32"
_BcmIpxConfOperStatus_Object = MibTableColumn
bcmIpxConfOperStatus = _BcmIpxConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 5, 1, 1),
    _BcmIpxConfOperStatus_Type()
)
bcmIpxConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxConfOperStatus.setStatus("mandatory")


class _BcmIpxConfAdminStatus_Type(Integer32):
    """Custom type bcmIpxConfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("up", 2))
    )


_BcmIpxConfAdminStatus_Type.__name__ = "Integer32"
_BcmIpxConfAdminStatus_Object = MibTableColumn
bcmIpxConfAdminStatus = _BcmIpxConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 5, 1, 2),
    _BcmIpxConfAdminStatus_Type()
)
bcmIpxConfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmIpxConfAdminStatus.setStatus("mandatory")
_BcmIpxConfCacheAge_Type = BcmCacheAge
_BcmIpxConfCacheAge_Object = MibTableColumn
bcmIpxConfCacheAge = _BcmIpxConfCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 5, 1, 3),
    _BcmIpxConfCacheAge_Type()
)
bcmIpxConfCacheAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmIpxConfCacheAge.setStatus("mandatory")
_BcmNbConfTable_Object = MibTable
bcmNbConfTable = _BcmNbConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    bcmNbConfTable.setStatus("mandatory")
_BcmNbConfEntry_Object = MibTableRow
bcmNbConfEntry = _BcmNbConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 6, 1)
)
bcmNbConfEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
)
if mibBuilder.loadTexts:
    bcmNbConfEntry.setStatus("mandatory")


class _BcmNbConfOperStatus_Type(Integer32):
    """Custom type bcmNbConfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_BcmNbConfOperStatus_Type.__name__ = "Integer32"
_BcmNbConfOperStatus_Object = MibTableColumn
bcmNbConfOperStatus = _BcmNbConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 6, 1, 1),
    _BcmNbConfOperStatus_Type()
)
bcmNbConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbConfOperStatus.setStatus("mandatory")


class _BcmNbConfAdminStatus_Type(Integer32):
    """Custom type bcmNbConfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("up", 2))
    )


_BcmNbConfAdminStatus_Type.__name__ = "Integer32"
_BcmNbConfAdminStatus_Object = MibTableColumn
bcmNbConfAdminStatus = _BcmNbConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 6, 1, 2),
    _BcmNbConfAdminStatus_Type()
)
bcmNbConfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmNbConfAdminStatus.setStatus("mandatory")
_BcmNbConfCacheAge_Type = BcmCacheAge
_BcmNbConfCacheAge_Object = MibTableColumn
bcmNbConfCacheAge = _BcmNbConfCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 1, 6, 1, 3),
    _BcmNbConfCacheAge_Type()
)
bcmNbConfCacheAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmNbConfCacheAge.setStatus("mandatory")
_BcmStatGroup_ObjectIdentity = ObjectIdentity
bcmStatGroup = _BcmStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2)
)
_BcmStatTable_Object = MibTable
bcmStatTable = _BcmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    bcmStatTable.setStatus("mandatory")
_BcmStatEntry_Object = MibTableRow
bcmStatEntry = _BcmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1)
)
bcmStatEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
)
if mibBuilder.loadTexts:
    bcmStatEntry.setStatus("mandatory")
_BcmFramesReceived_Type = Counter32
_BcmFramesReceived_Object = MibTableColumn
bcmFramesReceived = _BcmFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 1),
    _BcmFramesReceived_Type()
)
bcmFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmFramesReceived.setStatus("mandatory")
_BcmOctetsReceived_Type = Counter32
_BcmOctetsReceived_Object = MibTableColumn
bcmOctetsReceived = _BcmOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 2),
    _BcmOctetsReceived_Type()
)
bcmOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmOctetsReceived.setStatus("mandatory")
_BcmFramesReturned_Type = Counter32
_BcmFramesReturned_Object = MibTableColumn
bcmFramesReturned = _BcmFramesReturned_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 3),
    _BcmFramesReturned_Type()
)
bcmFramesReturned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmFramesReturned.setStatus("mandatory")
_BcmOctetsReturned_Type = Counter32
_BcmOctetsReturned_Object = MibTableColumn
bcmOctetsReturned = _BcmOctetsReturned_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 4),
    _BcmOctetsReturned_Type()
)
bcmOctetsReturned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmOctetsReturned.setStatus("mandatory")
_BcmFramesDiscarded_Type = Counter32
_BcmFramesDiscarded_Object = MibTableColumn
bcmFramesDiscarded = _BcmFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 5),
    _BcmFramesDiscarded_Type()
)
bcmFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmFramesDiscarded.setStatus("mandatory")
_BcmOctetsDiscarded_Type = Counter32
_BcmOctetsDiscarded_Object = MibTableColumn
bcmOctetsDiscarded = _BcmOctetsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 6),
    _BcmOctetsDiscarded_Type()
)
bcmOctetsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmOctetsDiscarded.setStatus("mandatory")
_BcmFramesTransmitted_Type = Counter32
_BcmFramesTransmitted_Object = MibTableColumn
bcmFramesTransmitted = _BcmFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 7),
    _BcmFramesTransmitted_Type()
)
bcmFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmFramesTransmitted.setStatus("mandatory")
_BcmOctetsTransmitted_Type = Counter32
_BcmOctetsTransmitted_Object = MibTableColumn
bcmOctetsTransmitted = _BcmOctetsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 8),
    _BcmOctetsTransmitted_Type()
)
bcmOctetsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmOctetsTransmitted.setStatus("mandatory")
_BcmTransmitErrorFrames_Type = Counter32
_BcmTransmitErrorFrames_Object = MibTableColumn
bcmTransmitErrorFrames = _BcmTransmitErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 9),
    _BcmTransmitErrorFrames_Type()
)
bcmTransmitErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmTransmitErrorFrames.setStatus("mandatory")
_BcmTransmitErrorOctets_Type = Counter32
_BcmTransmitErrorOctets_Object = MibTableColumn
bcmTransmitErrorOctets = _BcmTransmitErrorOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 10),
    _BcmTransmitErrorOctets_Type()
)
bcmTransmitErrorOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmTransmitErrorOctets.setStatus("mandatory")
_BcmBroadcastFramesDirectedNoRif_Type = Counter32
_BcmBroadcastFramesDirectedNoRif_Object = MibTableColumn
bcmBroadcastFramesDirectedNoRif = _BcmBroadcastFramesDirectedNoRif_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 11),
    _BcmBroadcastFramesDirectedNoRif_Type()
)
bcmBroadcastFramesDirectedNoRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmBroadcastFramesDirectedNoRif.setStatus("mandatory")
_BcmBroadcastFramesDirectedAre_Type = Counter32
_BcmBroadcastFramesDirectedAre_Object = MibTableColumn
bcmBroadcastFramesDirectedAre = _BcmBroadcastFramesDirectedAre_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 12),
    _BcmBroadcastFramesDirectedAre_Type()
)
bcmBroadcastFramesDirectedAre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmBroadcastFramesDirectedAre.setStatus("mandatory")
_BcmBroadcastFramesDirectedSte_Type = Counter32
_BcmBroadcastFramesDirectedSte_Object = MibTableColumn
bcmBroadcastFramesDirectedSte = _BcmBroadcastFramesDirectedSte_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 13),
    _BcmBroadcastFramesDirectedSte_Type()
)
bcmBroadcastFramesDirectedSte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmBroadcastFramesDirectedSte.setStatus("mandatory")
_BcmBroadcastFramesDirectedSrf_Type = Counter32
_BcmBroadcastFramesDirectedSrf_Object = MibTableColumn
bcmBroadcastFramesDirectedSrf = _BcmBroadcastFramesDirectedSrf_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 1, 1, 14),
    _BcmBroadcastFramesDirectedSrf_Type()
)
bcmBroadcastFramesDirectedSrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmBroadcastFramesDirectedSrf.setStatus("mandatory")
_BcmIpStatTable_Object = MibTable
bcmIpStatTable = _BcmIpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    bcmIpStatTable.setStatus("mandatory")
_BcmIpStatEntry_Object = MibTableRow
bcmIpStatEntry = _BcmIpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1)
)
bcmIpStatEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
)
if mibBuilder.loadTexts:
    bcmIpStatEntry.setStatus("mandatory")
_BcmIpFramesReceived_Type = Counter32
_BcmIpFramesReceived_Object = MibTableColumn
bcmIpFramesReceived = _BcmIpFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 1),
    _BcmIpFramesReceived_Type()
)
bcmIpFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpFramesReceived.setStatus("mandatory")
_BcmIpOctetsReceived_Type = Counter32
_BcmIpOctetsReceived_Object = MibTableColumn
bcmIpOctetsReceived = _BcmIpOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 2),
    _BcmIpOctetsReceived_Type()
)
bcmIpOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpOctetsReceived.setStatus("mandatory")
_BcmIpFramesReturned_Type = Counter32
_BcmIpFramesReturned_Object = MibTableColumn
bcmIpFramesReturned = _BcmIpFramesReturned_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 3),
    _BcmIpFramesReturned_Type()
)
bcmIpFramesReturned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpFramesReturned.setStatus("mandatory")
_BcmIpOctetsReturned_Type = Counter32
_BcmIpOctetsReturned_Object = MibTableColumn
bcmIpOctetsReturned = _BcmIpOctetsReturned_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 4),
    _BcmIpOctetsReturned_Type()
)
bcmIpOctetsReturned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpOctetsReturned.setStatus("mandatory")
_BcmIpFramesDiscarded_Type = Counter32
_BcmIpFramesDiscarded_Object = MibTableColumn
bcmIpFramesDiscarded = _BcmIpFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 5),
    _BcmIpFramesDiscarded_Type()
)
bcmIpFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpFramesDiscarded.setStatus("mandatory")
_BcmIpOctetsDiscarded_Type = Counter32
_BcmIpOctetsDiscarded_Object = MibTableColumn
bcmIpOctetsDiscarded = _BcmIpOctetsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 6),
    _BcmIpOctetsDiscarded_Type()
)
bcmIpOctetsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpOctetsDiscarded.setStatus("mandatory")
_BcmIpFramesTransmitted_Type = Counter32
_BcmIpFramesTransmitted_Object = MibTableColumn
bcmIpFramesTransmitted = _BcmIpFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 7),
    _BcmIpFramesTransmitted_Type()
)
bcmIpFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpFramesTransmitted.setStatus("mandatory")
_BcmIpOctetsTransmitted_Type = Counter32
_BcmIpOctetsTransmitted_Object = MibTableColumn
bcmIpOctetsTransmitted = _BcmIpOctetsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 8),
    _BcmIpOctetsTransmitted_Type()
)
bcmIpOctetsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpOctetsTransmitted.setStatus("mandatory")
_BcmIpTransmitErrorFrames_Type = Counter32
_BcmIpTransmitErrorFrames_Object = MibTableColumn
bcmIpTransmitErrorFrames = _BcmIpTransmitErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 9),
    _BcmIpTransmitErrorFrames_Type()
)
bcmIpTransmitErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpTransmitErrorFrames.setStatus("mandatory")
_BcmIpTransmitErrorOctets_Type = Counter32
_BcmIpTransmitErrorOctets_Object = MibTableColumn
bcmIpTransmitErrorOctets = _BcmIpTransmitErrorOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 10),
    _BcmIpTransmitErrorOctets_Type()
)
bcmIpTransmitErrorOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpTransmitErrorOctets.setStatus("mandatory")
_BcmIpBroadcastFramesDirectedNoRif_Type = Counter32
_BcmIpBroadcastFramesDirectedNoRif_Object = MibTableColumn
bcmIpBroadcastFramesDirectedNoRif = _BcmIpBroadcastFramesDirectedNoRif_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 11),
    _BcmIpBroadcastFramesDirectedNoRif_Type()
)
bcmIpBroadcastFramesDirectedNoRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpBroadcastFramesDirectedNoRif.setStatus("mandatory")
_BcmIpBroadcastFramesDirectedAre_Type = Counter32
_BcmIpBroadcastFramesDirectedAre_Object = MibTableColumn
bcmIpBroadcastFramesDirectedAre = _BcmIpBroadcastFramesDirectedAre_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 12),
    _BcmIpBroadcastFramesDirectedAre_Type()
)
bcmIpBroadcastFramesDirectedAre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpBroadcastFramesDirectedAre.setStatus("mandatory")
_BcmIpBroadcastFramesDirectedSte_Type = Counter32
_BcmIpBroadcastFramesDirectedSte_Object = MibTableColumn
bcmIpBroadcastFramesDirectedSte = _BcmIpBroadcastFramesDirectedSte_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 13),
    _BcmIpBroadcastFramesDirectedSte_Type()
)
bcmIpBroadcastFramesDirectedSte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpBroadcastFramesDirectedSte.setStatus("mandatory")
_BcmIpBroadcastFramesDirectedSrf_Type = Counter32
_BcmIpBroadcastFramesDirectedSrf_Object = MibTableColumn
bcmIpBroadcastFramesDirectedSrf = _BcmIpBroadcastFramesDirectedSrf_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 2, 1, 14),
    _BcmIpBroadcastFramesDirectedSrf_Type()
)
bcmIpBroadcastFramesDirectedSrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpBroadcastFramesDirectedSrf.setStatus("mandatory")
_BcmIpxStatTable_Object = MibTable
bcmIpxStatTable = _BcmIpxStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    bcmIpxStatTable.setStatus("mandatory")
_BcmIpxStatEntry_Object = MibTableRow
bcmIpxStatEntry = _BcmIpxStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1)
)
bcmIpxStatEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
)
if mibBuilder.loadTexts:
    bcmIpxStatEntry.setStatus("mandatory")
_BcmIpxFramesReceived_Type = Counter32
_BcmIpxFramesReceived_Object = MibTableColumn
bcmIpxFramesReceived = _BcmIpxFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 1),
    _BcmIpxFramesReceived_Type()
)
bcmIpxFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxFramesReceived.setStatus("mandatory")
_BcmIpxOctetsReceived_Type = Counter32
_BcmIpxOctetsReceived_Object = MibTableColumn
bcmIpxOctetsReceived = _BcmIpxOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 2),
    _BcmIpxOctetsReceived_Type()
)
bcmIpxOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxOctetsReceived.setStatus("mandatory")
_BcmIpxFramesReturned_Type = Counter32
_BcmIpxFramesReturned_Object = MibTableColumn
bcmIpxFramesReturned = _BcmIpxFramesReturned_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 3),
    _BcmIpxFramesReturned_Type()
)
bcmIpxFramesReturned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxFramesReturned.setStatus("mandatory")
_BcmIpxOctetsReturned_Type = Counter32
_BcmIpxOctetsReturned_Object = MibTableColumn
bcmIpxOctetsReturned = _BcmIpxOctetsReturned_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 4),
    _BcmIpxOctetsReturned_Type()
)
bcmIpxOctetsReturned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxOctetsReturned.setStatus("mandatory")
_BcmIpxFramesDiscarded_Type = Counter32
_BcmIpxFramesDiscarded_Object = MibTableColumn
bcmIpxFramesDiscarded = _BcmIpxFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 5),
    _BcmIpxFramesDiscarded_Type()
)
bcmIpxFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxFramesDiscarded.setStatus("mandatory")
_BcmIpxOctetsDiscarded_Type = Counter32
_BcmIpxOctetsDiscarded_Object = MibTableColumn
bcmIpxOctetsDiscarded = _BcmIpxOctetsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 6),
    _BcmIpxOctetsDiscarded_Type()
)
bcmIpxOctetsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxOctetsDiscarded.setStatus("mandatory")
_BcmIpxFramesTransmitted_Type = Counter32
_BcmIpxFramesTransmitted_Object = MibTableColumn
bcmIpxFramesTransmitted = _BcmIpxFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 7),
    _BcmIpxFramesTransmitted_Type()
)
bcmIpxFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxFramesTransmitted.setStatus("mandatory")
_BcmIpxOctetsTransmitted_Type = Counter32
_BcmIpxOctetsTransmitted_Object = MibTableColumn
bcmIpxOctetsTransmitted = _BcmIpxOctetsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 8),
    _BcmIpxOctetsTransmitted_Type()
)
bcmIpxOctetsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxOctetsTransmitted.setStatus("mandatory")
_BcmIpxTransmitErrorFrames_Type = Counter32
_BcmIpxTransmitErrorFrames_Object = MibTableColumn
bcmIpxTransmitErrorFrames = _BcmIpxTransmitErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 9),
    _BcmIpxTransmitErrorFrames_Type()
)
bcmIpxTransmitErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxTransmitErrorFrames.setStatus("mandatory")
_BcmIpxTransmitErrorOctets_Type = Counter32
_BcmIpxTransmitErrorOctets_Object = MibTableColumn
bcmIpxTransmitErrorOctets = _BcmIpxTransmitErrorOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 10),
    _BcmIpxTransmitErrorOctets_Type()
)
bcmIpxTransmitErrorOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxTransmitErrorOctets.setStatus("mandatory")
_BcmIpxBroadcastFramesDirectedNoRif_Type = Counter32
_BcmIpxBroadcastFramesDirectedNoRif_Object = MibTableColumn
bcmIpxBroadcastFramesDirectedNoRif = _BcmIpxBroadcastFramesDirectedNoRif_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 11),
    _BcmIpxBroadcastFramesDirectedNoRif_Type()
)
bcmIpxBroadcastFramesDirectedNoRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxBroadcastFramesDirectedNoRif.setStatus("mandatory")
_BcmIpxBroadcastFramesDirectedAre_Type = Counter32
_BcmIpxBroadcastFramesDirectedAre_Object = MibTableColumn
bcmIpxBroadcastFramesDirectedAre = _BcmIpxBroadcastFramesDirectedAre_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 12),
    _BcmIpxBroadcastFramesDirectedAre_Type()
)
bcmIpxBroadcastFramesDirectedAre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxBroadcastFramesDirectedAre.setStatus("mandatory")
_BcmIpxBroadcastFramesDirectedSte_Type = Counter32
_BcmIpxBroadcastFramesDirectedSte_Object = MibTableColumn
bcmIpxBroadcastFramesDirectedSte = _BcmIpxBroadcastFramesDirectedSte_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 13),
    _BcmIpxBroadcastFramesDirectedSte_Type()
)
bcmIpxBroadcastFramesDirectedSte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxBroadcastFramesDirectedSte.setStatus("mandatory")
_BcmIpxBroadcastFramesDirectedSrf_Type = Counter32
_BcmIpxBroadcastFramesDirectedSrf_Object = MibTableColumn
bcmIpxBroadcastFramesDirectedSrf = _BcmIpxBroadcastFramesDirectedSrf_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 3, 1, 14),
    _BcmIpxBroadcastFramesDirectedSrf_Type()
)
bcmIpxBroadcastFramesDirectedSrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmIpxBroadcastFramesDirectedSrf.setStatus("mandatory")
_BcmNbStatTable_Object = MibTable
bcmNbStatTable = _BcmNbStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    bcmNbStatTable.setStatus("mandatory")
_BcmNbStatEntry_Object = MibTableRow
bcmNbStatEntry = _BcmNbStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1)
)
bcmNbStatEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
)
if mibBuilder.loadTexts:
    bcmNbStatEntry.setStatus("mandatory")
_BcmNbFramesReceived_Type = Counter32
_BcmNbFramesReceived_Object = MibTableColumn
bcmNbFramesReceived = _BcmNbFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 1),
    _BcmNbFramesReceived_Type()
)
bcmNbFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbFramesReceived.setStatus("mandatory")
_BcmNbOctetsReceived_Type = Counter32
_BcmNbOctetsReceived_Object = MibTableColumn
bcmNbOctetsReceived = _BcmNbOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 2),
    _BcmNbOctetsReceived_Type()
)
bcmNbOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbOctetsReceived.setStatus("mandatory")
_BcmNbFramesReturned_Type = Counter32
_BcmNbFramesReturned_Object = MibTableColumn
bcmNbFramesReturned = _BcmNbFramesReturned_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 3),
    _BcmNbFramesReturned_Type()
)
bcmNbFramesReturned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbFramesReturned.setStatus("mandatory")
_BcmNbOctetsReturned_Type = Counter32
_BcmNbOctetsReturned_Object = MibTableColumn
bcmNbOctetsReturned = _BcmNbOctetsReturned_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 4),
    _BcmNbOctetsReturned_Type()
)
bcmNbOctetsReturned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbOctetsReturned.setStatus("mandatory")
_BcmNbFramesDiscarded_Type = Counter32
_BcmNbFramesDiscarded_Object = MibTableColumn
bcmNbFramesDiscarded = _BcmNbFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 5),
    _BcmNbFramesDiscarded_Type()
)
bcmNbFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbFramesDiscarded.setStatus("mandatory")
_BcmNbOctetsDiscarded_Type = Counter32
_BcmNbOctetsDiscarded_Object = MibTableColumn
bcmNbOctetsDiscarded = _BcmNbOctetsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 6),
    _BcmNbOctetsDiscarded_Type()
)
bcmNbOctetsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbOctetsDiscarded.setStatus("mandatory")
_BcmNbFramesTransmitted_Type = Counter32
_BcmNbFramesTransmitted_Object = MibTableColumn
bcmNbFramesTransmitted = _BcmNbFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 7),
    _BcmNbFramesTransmitted_Type()
)
bcmNbFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbFramesTransmitted.setStatus("mandatory")
_BcmNbOctetsTransmitted_Type = Counter32
_BcmNbOctetsTransmitted_Object = MibTableColumn
bcmNbOctetsTransmitted = _BcmNbOctetsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 8),
    _BcmNbOctetsTransmitted_Type()
)
bcmNbOctetsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbOctetsTransmitted.setStatus("mandatory")
_BcmNbTransmitErrorFrames_Type = Counter32
_BcmNbTransmitErrorFrames_Object = MibTableColumn
bcmNbTransmitErrorFrames = _BcmNbTransmitErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 9),
    _BcmNbTransmitErrorFrames_Type()
)
bcmNbTransmitErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbTransmitErrorFrames.setStatus("mandatory")
_BcmNbTransmitErrorOctets_Type = Counter32
_BcmNbTransmitErrorOctets_Object = MibTableColumn
bcmNbTransmitErrorOctets = _BcmNbTransmitErrorOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 10),
    _BcmNbTransmitErrorOctets_Type()
)
bcmNbTransmitErrorOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbTransmitErrorOctets.setStatus("mandatory")
_BcmNbBroadcastFramesDirectedNoRif_Type = Counter32
_BcmNbBroadcastFramesDirectedNoRif_Object = MibTableColumn
bcmNbBroadcastFramesDirectedNoRif = _BcmNbBroadcastFramesDirectedNoRif_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 11),
    _BcmNbBroadcastFramesDirectedNoRif_Type()
)
bcmNbBroadcastFramesDirectedNoRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbBroadcastFramesDirectedNoRif.setStatus("mandatory")
_BcmNbBroadcastFramesDirectedAre_Type = Counter32
_BcmNbBroadcastFramesDirectedAre_Object = MibTableColumn
bcmNbBroadcastFramesDirectedAre = _BcmNbBroadcastFramesDirectedAre_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 12),
    _BcmNbBroadcastFramesDirectedAre_Type()
)
bcmNbBroadcastFramesDirectedAre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbBroadcastFramesDirectedAre.setStatus("mandatory")
_BcmNbBroadcastFramesDirectedSte_Type = Counter32
_BcmNbBroadcastFramesDirectedSte_Object = MibTableColumn
bcmNbBroadcastFramesDirectedSte = _BcmNbBroadcastFramesDirectedSte_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 13),
    _BcmNbBroadcastFramesDirectedSte_Type()
)
bcmNbBroadcastFramesDirectedSte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbBroadcastFramesDirectedSte.setStatus("mandatory")
_BcmNbBroadcastFramesDirectedSrf_Type = Counter32
_BcmNbBroadcastFramesDirectedSrf_Object = MibTableColumn
bcmNbBroadcastFramesDirectedSrf = _BcmNbBroadcastFramesDirectedSrf_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 2, 4, 1, 14),
    _BcmNbBroadcastFramesDirectedSrf_Type()
)
bcmNbBroadcastFramesDirectedSrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbBroadcastFramesDirectedSrf.setStatus("mandatory")
_BcmMIBConformance_ObjectIdentity = ObjectIdentity
bcmMIBConformance = _BcmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 3)
)
_BcmMIBGroups_ObjectIdentity = ObjectIdentity
bcmMIBGroups = _BcmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 3, 1)
)
_BcmCConfGroup_ObjectIdentity = ObjectIdentity
bcmCConfGroup = _BcmCConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 3, 1, 1)
)
_BcmCStaticTargetsConfigGroup_ObjectIdentity = ObjectIdentity
bcmCStaticTargetsConfigGroup = _BcmCStaticTargetsConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 3, 1, 2)
)
_BcmCIpConfigGroup_ObjectIdentity = ObjectIdentity
bcmCIpConfigGroup = _BcmCIpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 3, 1, 3)
)
_BcmCIpxConfigGroup_ObjectIdentity = ObjectIdentity
bcmCIpxConfigGroup = _BcmCIpxConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 3, 1, 4)
)
_BcmCNbConfigGroup_ObjectIdentity = ObjectIdentity
bcmCNbConfigGroup = _BcmCNbConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 3, 1, 5)
)
_BcmCStatGroup_ObjectIdentity = ObjectIdentity
bcmCStatGroup = _BcmCStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 3, 1, 6)
)
_BcmCIpStatGroup_ObjectIdentity = ObjectIdentity
bcmCIpStatGroup = _BcmCIpStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 3, 1, 7)
)
_BcmCIpxStatGroup_ObjectIdentity = ObjectIdentity
bcmCIpxStatGroup = _BcmCIpxStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 3, 1, 8)
)
_BcmCNbStatGroup_ObjectIdentity = ObjectIdentity
bcmCNbStatGroup = _BcmCNbStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 3, 1, 9)
)
_BcmMIBCompliances_ObjectIdentity = ObjectIdentity
bcmMIBCompliances = _BcmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 3, 2)
)
_BcmMIBCompliance_ObjectIdentity = ObjectIdentity
bcmMIBCompliance = _BcmMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 3, 3, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-BCM-MIB",
    **{"BcmCacheAge": BcmCacheAge,
       "ibmBcmMIB": ibmBcmMIB,
       "bcmConfGroup": bcmConfGroup,
       "bcmConfTable": bcmConfTable,
       "bcmConfEntry": bcmConfEntry,
       "bcmRouteCacheEnabled": bcmRouteCacheEnabled,
       "bcmStaticTargetsNextId": bcmStaticTargetsNextId,
       "bcmStaticTargetsTable": bcmStaticTargetsTable,
       "bcmStaticTargetsEntry": bcmStaticTargetsEntry,
       "bcmStaticTargetsIndex": bcmStaticTargetsIndex,
       "bcmStaticTargetsAtmAddress": bcmStaticTargetsAtmAddress,
       "bcmStaticTargetsMacAddress": bcmStaticTargetsMacAddress,
       "bcmStaticTargetsProtocol": bcmStaticTargetsProtocol,
       "bcmStaticTargetsRowStatus": bcmStaticTargetsRowStatus,
       "bcmIpConfTable": bcmIpConfTable,
       "bcmIpConfEntry": bcmIpConfEntry,
       "bcmIpConfOperStatus": bcmIpConfOperStatus,
       "bcmIpConfAdminStatus": bcmIpConfAdminStatus,
       "bcmIpConfCacheAge": bcmIpConfCacheAge,
       "bcmIpxConfTable": bcmIpxConfTable,
       "bcmIpxConfEntry": bcmIpxConfEntry,
       "bcmIpxConfOperStatus": bcmIpxConfOperStatus,
       "bcmIpxConfAdminStatus": bcmIpxConfAdminStatus,
       "bcmIpxConfCacheAge": bcmIpxConfCacheAge,
       "bcmNbConfTable": bcmNbConfTable,
       "bcmNbConfEntry": bcmNbConfEntry,
       "bcmNbConfOperStatus": bcmNbConfOperStatus,
       "bcmNbConfAdminStatus": bcmNbConfAdminStatus,
       "bcmNbConfCacheAge": bcmNbConfCacheAge,
       "bcmStatGroup": bcmStatGroup,
       "bcmStatTable": bcmStatTable,
       "bcmStatEntry": bcmStatEntry,
       "bcmFramesReceived": bcmFramesReceived,
       "bcmOctetsReceived": bcmOctetsReceived,
       "bcmFramesReturned": bcmFramesReturned,
       "bcmOctetsReturned": bcmOctetsReturned,
       "bcmFramesDiscarded": bcmFramesDiscarded,
       "bcmOctetsDiscarded": bcmOctetsDiscarded,
       "bcmFramesTransmitted": bcmFramesTransmitted,
       "bcmOctetsTransmitted": bcmOctetsTransmitted,
       "bcmTransmitErrorFrames": bcmTransmitErrorFrames,
       "bcmTransmitErrorOctets": bcmTransmitErrorOctets,
       "bcmBroadcastFramesDirectedNoRif": bcmBroadcastFramesDirectedNoRif,
       "bcmBroadcastFramesDirectedAre": bcmBroadcastFramesDirectedAre,
       "bcmBroadcastFramesDirectedSte": bcmBroadcastFramesDirectedSte,
       "bcmBroadcastFramesDirectedSrf": bcmBroadcastFramesDirectedSrf,
       "bcmIpStatTable": bcmIpStatTable,
       "bcmIpStatEntry": bcmIpStatEntry,
       "bcmIpFramesReceived": bcmIpFramesReceived,
       "bcmIpOctetsReceived": bcmIpOctetsReceived,
       "bcmIpFramesReturned": bcmIpFramesReturned,
       "bcmIpOctetsReturned": bcmIpOctetsReturned,
       "bcmIpFramesDiscarded": bcmIpFramesDiscarded,
       "bcmIpOctetsDiscarded": bcmIpOctetsDiscarded,
       "bcmIpFramesTransmitted": bcmIpFramesTransmitted,
       "bcmIpOctetsTransmitted": bcmIpOctetsTransmitted,
       "bcmIpTransmitErrorFrames": bcmIpTransmitErrorFrames,
       "bcmIpTransmitErrorOctets": bcmIpTransmitErrorOctets,
       "bcmIpBroadcastFramesDirectedNoRif": bcmIpBroadcastFramesDirectedNoRif,
       "bcmIpBroadcastFramesDirectedAre": bcmIpBroadcastFramesDirectedAre,
       "bcmIpBroadcastFramesDirectedSte": bcmIpBroadcastFramesDirectedSte,
       "bcmIpBroadcastFramesDirectedSrf": bcmIpBroadcastFramesDirectedSrf,
       "bcmIpxStatTable": bcmIpxStatTable,
       "bcmIpxStatEntry": bcmIpxStatEntry,
       "bcmIpxFramesReceived": bcmIpxFramesReceived,
       "bcmIpxOctetsReceived": bcmIpxOctetsReceived,
       "bcmIpxFramesReturned": bcmIpxFramesReturned,
       "bcmIpxOctetsReturned": bcmIpxOctetsReturned,
       "bcmIpxFramesDiscarded": bcmIpxFramesDiscarded,
       "bcmIpxOctetsDiscarded": bcmIpxOctetsDiscarded,
       "bcmIpxFramesTransmitted": bcmIpxFramesTransmitted,
       "bcmIpxOctetsTransmitted": bcmIpxOctetsTransmitted,
       "bcmIpxTransmitErrorFrames": bcmIpxTransmitErrorFrames,
       "bcmIpxTransmitErrorOctets": bcmIpxTransmitErrorOctets,
       "bcmIpxBroadcastFramesDirectedNoRif": bcmIpxBroadcastFramesDirectedNoRif,
       "bcmIpxBroadcastFramesDirectedAre": bcmIpxBroadcastFramesDirectedAre,
       "bcmIpxBroadcastFramesDirectedSte": bcmIpxBroadcastFramesDirectedSte,
       "bcmIpxBroadcastFramesDirectedSrf": bcmIpxBroadcastFramesDirectedSrf,
       "bcmNbStatTable": bcmNbStatTable,
       "bcmNbStatEntry": bcmNbStatEntry,
       "bcmNbFramesReceived": bcmNbFramesReceived,
       "bcmNbOctetsReceived": bcmNbOctetsReceived,
       "bcmNbFramesReturned": bcmNbFramesReturned,
       "bcmNbOctetsReturned": bcmNbOctetsReturned,
       "bcmNbFramesDiscarded": bcmNbFramesDiscarded,
       "bcmNbOctetsDiscarded": bcmNbOctetsDiscarded,
       "bcmNbFramesTransmitted": bcmNbFramesTransmitted,
       "bcmNbOctetsTransmitted": bcmNbOctetsTransmitted,
       "bcmNbTransmitErrorFrames": bcmNbTransmitErrorFrames,
       "bcmNbTransmitErrorOctets": bcmNbTransmitErrorOctets,
       "bcmNbBroadcastFramesDirectedNoRif": bcmNbBroadcastFramesDirectedNoRif,
       "bcmNbBroadcastFramesDirectedAre": bcmNbBroadcastFramesDirectedAre,
       "bcmNbBroadcastFramesDirectedSte": bcmNbBroadcastFramesDirectedSte,
       "bcmNbBroadcastFramesDirectedSrf": bcmNbBroadcastFramesDirectedSrf,
       "bcmMIBConformance": bcmMIBConformance,
       "bcmMIBGroups": bcmMIBGroups,
       "bcmCConfGroup": bcmCConfGroup,
       "bcmCStaticTargetsConfigGroup": bcmCStaticTargetsConfigGroup,
       "bcmCIpConfigGroup": bcmCIpConfigGroup,
       "bcmCIpxConfigGroup": bcmCIpxConfigGroup,
       "bcmCNbConfigGroup": bcmCNbConfigGroup,
       "bcmCStatGroup": bcmCStatGroup,
       "bcmCIpStatGroup": bcmCIpStatGroup,
       "bcmCIpxStatGroup": bcmCIpxStatGroup,
       "bcmCNbStatGroup": bcmCNbStatGroup,
       "bcmMIBCompliances": bcmMIBCompliances,
       "bcmMIBCompliance": bcmMIBCompliance}
)
