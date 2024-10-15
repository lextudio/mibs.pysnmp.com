# SNMP MIB module (DECHUB900-ERPTR-MIB-V3-0) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DECHUB900-ERPTR-MIB-V3-0
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:40 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_DecMIBextension_ObjectIdentity = ObjectIdentity
decMIBextension = _DecMIBextension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_DecHub900_ObjectIdentity = ObjectIdentity
decHub900 = _DecHub900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11)
)
_Repeater_ObjectIdentity = ObjectIdentity
repeater = _Repeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5)
)
_RptrVersion1_ObjectIdentity = ObjectIdentity
rptrVersion1 = _RptrVersion1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1)
)
_RptrExtensions_ObjectIdentity = ObjectIdentity
rptrExtensions = _RptrExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1)
)
_ErptrBasicPackage_ObjectIdentity = ObjectIdentity
erptrBasicPackage = _ErptrBasicPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1)
)
_ErptrRptrInfo_ObjectIdentity = ObjectIdentity
erptrRptrInfo = _ErptrRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1)
)


class _ErptrAutoPartitionAlg_Type(Integer32):
    """Custom type erptrAutoPartitionAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enhanced", 2),
          ("standard", 1))
    )


_ErptrAutoPartitionAlg_Type.__name__ = "Integer32"
_ErptrAutoPartitionAlg_Object = MibScalar
erptrAutoPartitionAlg = _ErptrAutoPartitionAlg_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 1),
    _ErptrAutoPartitionAlg_Type()
)
erptrAutoPartitionAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrAutoPartitionAlg.setStatus("mandatory")


class _ErptrAutoPartitionReconnectAlg_Type(Integer32):
    """Custom type erptrAutoPartitionReconnectAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("txOnly", 2))
    )


_ErptrAutoPartitionReconnectAlg_Type.__name__ = "Integer32"
_ErptrAutoPartitionReconnectAlg_Object = MibScalar
erptrAutoPartitionReconnectAlg = _ErptrAutoPartitionReconnectAlg_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 2),
    _ErptrAutoPartitionReconnectAlg_Type()
)
erptrAutoPartitionReconnectAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrAutoPartitionReconnectAlg.setStatus("mandatory")


class _ErptrJamBits_Type(Integer32):
    """Custom type erptrJamBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jb128", 2),
          ("jb96", 1))
    )


_ErptrJamBits_Type.__name__ = "Integer32"
_ErptrJamBits_Object = MibScalar
erptrJamBits = _ErptrJamBits_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 3),
    _ErptrJamBits_Type()
)
erptrJamBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrJamBits.setStatus("mandatory")
_ErptrHealthTextChanges_Type = Counter32
_ErptrHealthTextChanges_Object = MibScalar
erptrHealthTextChanges = _ErptrHealthTextChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 4),
    _ErptrHealthTextChanges_Type()
)
erptrHealthTextChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrHealthTextChanges.setStatus("mandatory")
_ErptrTotalPortEvents_Type = Counter32
_ErptrTotalPortEvents_Object = MibScalar
erptrTotalPortEvents = _ErptrTotalPortEvents_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 5),
    _ErptrTotalPortEvents_Type()
)
erptrTotalPortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrTotalPortEvents.setStatus("mandatory")
_ErptrTotalRptrErrors_Type = Counter32
_ErptrTotalRptrErrors_Object = MibScalar
erptrTotalRptrErrors = _ErptrTotalRptrErrors_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 6),
    _ErptrTotalRptrErrors_Type()
)
erptrTotalRptrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrTotalRptrErrors.setStatus("mandatory")


class _ErptrJabberProtectionAdminStatus_Type(Integer32):
    """Custom type erptrJabberProtectionAdminStatus based on Integer32"""
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


_ErptrJabberProtectionAdminStatus_Type.__name__ = "Integer32"
_ErptrJabberProtectionAdminStatus_Object = MibScalar
erptrJabberProtectionAdminStatus = _ErptrJabberProtectionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 7),
    _ErptrJabberProtectionAdminStatus_Type()
)
erptrJabberProtectionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrJabberProtectionAdminStatus.setStatus("mandatory")
_ErptrTotalPorts_Type = Counter32
_ErptrTotalPorts_Object = MibScalar
erptrTotalPorts = _ErptrTotalPorts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 8),
    _ErptrTotalPorts_Type()
)
erptrTotalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrTotalPorts.setStatus("mandatory")


class _ErptrPMDCarrierCardType_Type(Integer32):
    """Custom type erptrPMDCarrierCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type10Base", 2),
          ("unknown", 1))
    )


_ErptrPMDCarrierCardType_Type.__name__ = "Integer32"
_ErptrPMDCarrierCardType_Object = MibScalar
erptrPMDCarrierCardType = _ErptrPMDCarrierCardType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 9),
    _ErptrPMDCarrierCardType_Type()
)
erptrPMDCarrierCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrPMDCarrierCardType.setStatus("mandatory")
_ErptrGroupInfo_ObjectIdentity = ObjectIdentity
erptrGroupInfo = _ErptrGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2)
)
_ErptrGroupTable_Object = MibTable
erptrGroupTable = _ErptrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    erptrGroupTable.setStatus("mandatory")
_ErptrGroupEntry_Object = MibTableRow
erptrGroupEntry = _ErptrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2, 1, 1)
)
erptrGroupEntry.setIndexNames(
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrGroupIndex"),
)
if mibBuilder.loadTexts:
    erptrGroupEntry.setStatus("mandatory")


class _ErptrGroupIndex_Type(Integer32):
    """Custom type erptrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrGroupIndex_Type.__name__ = "Integer32"
_ErptrGroupIndex_Object = MibTableColumn
erptrGroupIndex = _ErptrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2, 1, 1, 1),
    _ErptrGroupIndex_Type()
)
erptrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrGroupIndex.setStatus("mandatory")
_ErptrGroupTransmitCollisions_Type = Counter32
_ErptrGroupTransmitCollisions_Object = MibTableColumn
erptrGroupTransmitCollisions = _ErptrGroupTransmitCollisions_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2, 1, 1, 2),
    _ErptrGroupTransmitCollisions_Type()
)
erptrGroupTransmitCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrGroupTransmitCollisions.setStatus("mandatory")


class _ErptrGroupReset_Type(Integer32):
    """Custom type erptrGroupReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_ErptrGroupReset_Type.__name__ = "Integer32"
_ErptrGroupReset_Object = MibTableColumn
erptrGroupReset = _ErptrGroupReset_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2, 1, 1, 3),
    _ErptrGroupReset_Type()
)
erptrGroupReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrGroupReset.setStatus("mandatory")
_ErptrGroupLanTotalOctets_Type = Counter32
_ErptrGroupLanTotalOctets_Object = MibTableColumn
erptrGroupLanTotalOctets = _ErptrGroupLanTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2, 1, 1, 4),
    _ErptrGroupLanTotalOctets_Type()
)
erptrGroupLanTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrGroupLanTotalOctets.setStatus("mandatory")
_ErptrPortInfo_ObjectIdentity = ObjectIdentity
erptrPortInfo = _ErptrPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3)
)
_ErptrPortTable_Object = MibTable
erptrPortTable = _ErptrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    erptrPortTable.setStatus("mandatory")
_ErptrPortEntry_Object = MibTableRow
erptrPortEntry = _ErptrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1)
)
erptrPortEntry.setIndexNames(
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrPortGroupIndex"),
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrPortIndex"),
)
if mibBuilder.loadTexts:
    erptrPortEntry.setStatus("mandatory")


class _ErptrPortGroupIndex_Type(Integer32):
    """Custom type erptrPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrPortGroupIndex_Type.__name__ = "Integer32"
_ErptrPortGroupIndex_Object = MibTableColumn
erptrPortGroupIndex = _ErptrPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 1),
    _ErptrPortGroupIndex_Type()
)
erptrPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrPortGroupIndex.setStatus("mandatory")


class _ErptrPortIndex_Type(Integer32):
    """Custom type erptrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrPortIndex_Type.__name__ = "Integer32"
_ErptrPortIndex_Object = MibTableColumn
erptrPortIndex = _ErptrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 2),
    _ErptrPortIndex_Type()
)
erptrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrPortIndex.setStatus("mandatory")


class _ErptrPortName_Type(DisplayString):
    """Custom type erptrPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ErptrPortName_Type.__name__ = "DisplayString"
_ErptrPortName_Object = MibTableColumn
erptrPortName = _ErptrPortName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 3),
    _ErptrPortName_Type()
)
erptrPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrPortName.setStatus("mandatory")
_ErptrPortPartitions_Type = Counter32
_ErptrPortPartitions_Object = MibTableColumn
erptrPortPartitions = _ErptrPortPartitions_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 4),
    _ErptrPortPartitions_Type()
)
erptrPortPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrPortPartitions.setStatus("mandatory")


class _ErptrPortPartitionReason_Type(Integer32):
    """Custom type erptrPortPartitionReason based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("consecutiveCollisions", 6),
          ("consecutiveCollisionsAndMgmtPart", 7),
          ("excessiveCollision", 4),
          ("excessiveCollisionAndMgmtPart", 5),
          ("forcedReconnection", 14),
          ("jabber", 8),
          ("jabberAndMgmtPart", 9),
          ("managementPartitioned", 3),
          ("noCarrierLoopback", 10),
          ("noCarrierLoopbackandMgmtPart", 11),
          ("notPartitioned", 2),
          ("transmitCarrierDropout", 12),
          ("transmitCarrierDropoutAndMgmtPart", 13),
          ("unknown", 1))
    )


_ErptrPortPartitionReason_Type.__name__ = "Integer32"
_ErptrPortPartitionReason_Object = MibTableColumn
erptrPortPartitionReason = _ErptrPortPartitionReason_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 5),
    _ErptrPortPartitionReason_Type()
)
erptrPortPartitionReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrPortPartitionReason.setStatus("mandatory")


class _ErptrPortMAUType_Type(Integer32):
    """Custom type erptrPortMAUType based on Integer32"""
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
        *(("type10Base2", 5),
          ("type10Base5", 3),
          ("type10BaseFB", 8),
          ("type10BaseFL", 9),
          ("type10BaseFP", 7),
          ("type10BaseT", 6),
          ("typeAUI", 2),
          ("typeBackplaneThinwire", 11),
          ("typeFoirl", 4),
          ("typeRAUI", 12),
          ("typeTelco10BaseT", 10),
          ("unknown", 1))
    )


_ErptrPortMAUType_Type.__name__ = "Integer32"
_ErptrPortMAUType_Object = MibTableColumn
erptrPortMAUType = _ErptrPortMAUType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 6),
    _ErptrPortMAUType_Type()
)
erptrPortMAUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrPortMAUType.setStatus("mandatory")


class _ErptrPortSQETestError_Type(Integer32):
    """Custom type erptrPortSQETestError based on Integer32"""
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
        *(("sqeTestDetected", 2),
          ("sqeTestMasked", 4),
          ("sqeTestNotDetected", 3),
          ("unknown", 1))
    )


_ErptrPortSQETestError_Type.__name__ = "Integer32"
_ErptrPortSQETestError_Object = MibTableColumn
erptrPortSQETestError = _ErptrPortSQETestError_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 7),
    _ErptrPortSQETestError_Type()
)
erptrPortSQETestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrPortSQETestError.setStatus("mandatory")
_ErptrAddrDBPackage_ObjectIdentity = ObjectIdentity
erptrAddrDBPackage = _ErptrAddrDBPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2)
)
_ErptrAddrDBRptrInfo_ObjectIdentity = ObjectIdentity
erptrAddrDBRptrInfo = _ErptrAddrDBRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 1)
)


class _ErptrAddrDBTableCapacity_Type(Integer32):
    """Custom type erptrAddrDBTableCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ErptrAddrDBTableCapacity_Type.__name__ = "Integer32"
_ErptrAddrDBTableCapacity_Object = MibScalar
erptrAddrDBTableCapacity = _ErptrAddrDBTableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 1, 1),
    _ErptrAddrDBTableCapacity_Type()
)
erptrAddrDBTableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrAddrDBTableCapacity.setStatus("mandatory")
_ErptrAddrDBGroupInfo_ObjectIdentity = ObjectIdentity
erptrAddrDBGroupInfo = _ErptrAddrDBGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 2)
)
_ErptrAddrDBPortInfo_ObjectIdentity = ObjectIdentity
erptrAddrDBPortInfo = _ErptrAddrDBPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 3)
)
_ErptrAddrDBPortAddrTable_Object = MibTable
erptrAddrDBPortAddrTable = _ErptrAddrDBPortAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    erptrAddrDBPortAddrTable.setStatus("mandatory")
_ErptrAddrDBPortAddrEntry_Object = MibTableRow
erptrAddrDBPortAddrEntry = _ErptrAddrDBPortAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 3, 1, 1)
)
erptrAddrDBPortAddrEntry.setIndexNames(
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrAddrDBPortPhyAddr"),
)
if mibBuilder.loadTexts:
    erptrAddrDBPortAddrEntry.setStatus("mandatory")
_ErptrAddrDBPortPhyAddr_Type = PhysAddress
_ErptrAddrDBPortPhyAddr_Object = MibTableColumn
erptrAddrDBPortPhyAddr = _ErptrAddrDBPortPhyAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 3, 1, 1, 1),
    _ErptrAddrDBPortPhyAddr_Type()
)
erptrAddrDBPortPhyAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrAddrDBPortPhyAddr.setStatus("mandatory")


class _ErptrAddrDBPortGroupIndex_Type(Integer32):
    """Custom type erptrAddrDBPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrAddrDBPortGroupIndex_Type.__name__ = "Integer32"
_ErptrAddrDBPortGroupIndex_Object = MibTableColumn
erptrAddrDBPortGroupIndex = _ErptrAddrDBPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 3, 1, 1, 2),
    _ErptrAddrDBPortGroupIndex_Type()
)
erptrAddrDBPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrAddrDBPortGroupIndex.setStatus("mandatory")


class _ErptrAddrDBPortIndex_Type(Integer32):
    """Custom type erptrAddrDBPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrAddrDBPortIndex_Type.__name__ = "Integer32"
_ErptrAddrDBPortIndex_Object = MibTableColumn
erptrAddrDBPortIndex = _ErptrAddrDBPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 3, 1, 1, 3),
    _ErptrAddrDBPortIndex_Type()
)
erptrAddrDBPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrAddrDBPortIndex.setStatus("mandatory")
_ErptrDprPackage_ObjectIdentity = ObjectIdentity
erptrDprPackage = _ErptrDprPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3)
)
_ErptrDprRptrInfo_ObjectIdentity = ObjectIdentity
erptrDprRptrInfo = _ErptrDprRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 1)
)
_ErptrDprTotalStateChanges_Type = Counter32
_ErptrDprTotalStateChanges_Object = MibScalar
erptrDprTotalStateChanges = _ErptrDprTotalStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 1, 1),
    _ErptrDprTotalStateChanges_Type()
)
erptrDprTotalStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrDprTotalStateChanges.setStatus("mandatory")
_ErptrDprGroupInfo_ObjectIdentity = ObjectIdentity
erptrDprGroupInfo = _ErptrDprGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 2)
)
_ErptrDprPortInfo_ObjectIdentity = ObjectIdentity
erptrDprPortInfo = _ErptrDprPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3)
)
_ErptrDprLinkTable_Object = MibTable
erptrDprLinkTable = _ErptrDprLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    erptrDprLinkTable.setStatus("mandatory")
_ErptrDprLinkEntry_Object = MibTableRow
erptrDprLinkEntry = _ErptrDprLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1)
)
erptrDprLinkEntry.setIndexNames(
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrDprLinkGroupIndex"),
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrDprLinkPortIndex"),
)
if mibBuilder.loadTexts:
    erptrDprLinkEntry.setStatus("mandatory")


class _ErptrDprLinkGroupIndex_Type(Integer32):
    """Custom type erptrDprLinkGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrDprLinkGroupIndex_Type.__name__ = "Integer32"
_ErptrDprLinkGroupIndex_Object = MibTableColumn
erptrDprLinkGroupIndex = _ErptrDprLinkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 1),
    _ErptrDprLinkGroupIndex_Type()
)
erptrDprLinkGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrDprLinkGroupIndex.setStatus("mandatory")


class _ErptrDprLinkPortIndex_Type(Integer32):
    """Custom type erptrDprLinkPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrDprLinkPortIndex_Type.__name__ = "Integer32"
_ErptrDprLinkPortIndex_Object = MibTableColumn
erptrDprLinkPortIndex = _ErptrDprLinkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 2),
    _ErptrDprLinkPortIndex_Type()
)
erptrDprLinkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrDprLinkPortIndex.setStatus("mandatory")


class _ErptrDprLinkType_Type(Integer32):
    """Custom type erptrDprLinkType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redundantMaster", 1),
          ("redundantResponder", 2))
    )


_ErptrDprLinkType_Type.__name__ = "Integer32"
_ErptrDprLinkType_Object = MibTableColumn
erptrDprLinkType = _ErptrDprLinkType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 3),
    _ErptrDprLinkType_Type()
)
erptrDprLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrDprLinkType.setStatus("mandatory")


class _ErptrDprLinkToggle_Type(Integer32):
    """Custom type erptrDprLinkToggle based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noToggle", 1),
          ("toggle", 2))
    )


_ErptrDprLinkToggle_Type.__name__ = "Integer32"
_ErptrDprLinkToggle_Object = MibTableColumn
erptrDprLinkToggle = _ErptrDprLinkToggle_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 4),
    _ErptrDprLinkToggle_Type()
)
erptrDprLinkToggle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrDprLinkToggle.setStatus("mandatory")


class _ErptrDprLinkOperStatus_Type(Integer32):
    """Custom type erptrDprLinkOperStatus based on Integer32"""
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
        *(("masterPrimaryActive", 2),
          ("masterPrimaryLinkFailure", 4),
          ("masterPrimaryStandby", 3),
          ("redundancyNotOperational", 1),
          ("responderLinkFailure", 6),
          ("responderOk", 5))
    )


_ErptrDprLinkOperStatus_Type.__name__ = "Integer32"
_ErptrDprLinkOperStatus_Object = MibTableColumn
erptrDprLinkOperStatus = _ErptrDprLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 5),
    _ErptrDprLinkOperStatus_Type()
)
erptrDprLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrDprLinkOperStatus.setStatus("mandatory")


class _ErptrDprSecondaryGroupIndex_Type(Integer32):
    """Custom type erptrDprSecondaryGroupIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ErptrDprSecondaryGroupIndex_Type.__name__ = "Integer32"
_ErptrDprSecondaryGroupIndex_Object = MibTableColumn
erptrDprSecondaryGroupIndex = _ErptrDprSecondaryGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 6),
    _ErptrDprSecondaryGroupIndex_Type()
)
erptrDprSecondaryGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrDprSecondaryGroupIndex.setStatus("mandatory")


class _ErptrDprSecondaryPortIndex_Type(Integer32):
    """Custom type erptrDprSecondaryPortIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ErptrDprSecondaryPortIndex_Type.__name__ = "Integer32"
_ErptrDprSecondaryPortIndex_Object = MibTableColumn
erptrDprSecondaryPortIndex = _ErptrDprSecondaryPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 7),
    _ErptrDprSecondaryPortIndex_Type()
)
erptrDprSecondaryPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrDprSecondaryPortIndex.setStatus("mandatory")


class _ErptrDprSecondaryOperStatus_Type(Integer32):
    """Custom type erptrDprSecondaryOperStatus based on Integer32"""
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
        *(("masterSecondaryActive", 2),
          ("masterSecondaryLinkFailure", 4),
          ("masterSecondaryStandby", 3),
          ("redundancyNotOperational", 1))
    )


_ErptrDprSecondaryOperStatus_Type.__name__ = "Integer32"
_ErptrDprSecondaryOperStatus_Object = MibTableColumn
erptrDprSecondaryOperStatus = _ErptrDprSecondaryOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 8),
    _ErptrDprSecondaryOperStatus_Type()
)
erptrDprSecondaryOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrDprSecondaryOperStatus.setStatus("mandatory")


class _ErptrDprLinkName_Type(DisplayString):
    """Custom type erptrDprLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ErptrDprLinkName_Type.__name__ = "DisplayString"
_ErptrDprLinkName_Object = MibTableColumn
erptrDprLinkName = _ErptrDprLinkName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 9),
    _ErptrDprLinkName_Type()
)
erptrDprLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrDprLinkName.setStatus("mandatory")
_ErptrDprLinkStateChanges_Type = Counter32
_ErptrDprLinkStateChanges_Object = MibTableColumn
erptrDprLinkStateChanges = _ErptrDprLinkStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 10),
    _ErptrDprLinkStateChanges_Type()
)
erptrDprLinkStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrDprLinkStateChanges.setStatus("mandatory")


class _ErptrDprLinkEntryStatus_Type(Integer32):
    """Custom type erptrDprLinkEntryStatus based on Integer32"""
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


_ErptrDprLinkEntryStatus_Type.__name__ = "Integer32"
_ErptrDprLinkEntryStatus_Object = MibTableColumn
erptrDprLinkEntryStatus = _ErptrDprLinkEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 11),
    _ErptrDprLinkEntryStatus_Type()
)
erptrDprLinkEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrDprLinkEntryStatus.setStatus("mandatory")
_ErptrSecurityPackage_ObjectIdentity = ObjectIdentity
erptrSecurityPackage = _ErptrSecurityPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4)
)
_ErptrSecurityRptrInfo_ObjectIdentity = ObjectIdentity
erptrSecurityRptrInfo = _ErptrSecurityRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1)
)
_ErptrSecurityRptrSecurityViolations_Type = Counter32
_ErptrSecurityRptrSecurityViolations_Object = MibScalar
erptrSecurityRptrSecurityViolations = _ErptrSecurityRptrSecurityViolations_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 1),
    _ErptrSecurityRptrSecurityViolations_Type()
)
erptrSecurityRptrSecurityViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrSecurityRptrSecurityViolations.setStatus("mandatory")
_ErptrSecurityRptrLogTable_Object = MibTable
erptrSecurityRptrLogTable = _ErptrSecurityRptrLogTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    erptrSecurityRptrLogTable.setStatus("mandatory")
_ErptrSecurityRptrLogEntry_Object = MibTableRow
erptrSecurityRptrLogEntry = _ErptrSecurityRptrLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2, 1)
)
erptrSecurityRptrLogEntry.setIndexNames(
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrSecurityRptrLogIndex"),
)
if mibBuilder.loadTexts:
    erptrSecurityRptrLogEntry.setStatus("mandatory")


class _ErptrSecurityRptrLogIndex_Type(Integer32):
    """Custom type erptrSecurityRptrLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ErptrSecurityRptrLogIndex_Type.__name__ = "Integer32"
_ErptrSecurityRptrLogIndex_Object = MibTableColumn
erptrSecurityRptrLogIndex = _ErptrSecurityRptrLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2, 1, 1),
    _ErptrSecurityRptrLogIndex_Type()
)
erptrSecurityRptrLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrSecurityRptrLogIndex.setStatus("mandatory")


class _ErptrSecurityRptrLogGroupIndex_Type(Integer32):
    """Custom type erptrSecurityRptrLogGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrSecurityRptrLogGroupIndex_Type.__name__ = "Integer32"
_ErptrSecurityRptrLogGroupIndex_Object = MibTableColumn
erptrSecurityRptrLogGroupIndex = _ErptrSecurityRptrLogGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2, 1, 2),
    _ErptrSecurityRptrLogGroupIndex_Type()
)
erptrSecurityRptrLogGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrSecurityRptrLogGroupIndex.setStatus("mandatory")


class _ErptrSecurityRptrLogPortIndex_Type(Integer32):
    """Custom type erptrSecurityRptrLogPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrSecurityRptrLogPortIndex_Type.__name__ = "Integer32"
_ErptrSecurityRptrLogPortIndex_Object = MibTableColumn
erptrSecurityRptrLogPortIndex = _ErptrSecurityRptrLogPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2, 1, 3),
    _ErptrSecurityRptrLogPortIndex_Type()
)
erptrSecurityRptrLogPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrSecurityRptrLogPortIndex.setStatus("mandatory")
_ErptrSecurityRptrLogTime_Type = TimeTicks
_ErptrSecurityRptrLogTime_Object = MibTableColumn
erptrSecurityRptrLogTime = _ErptrSecurityRptrLogTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2, 1, 4),
    _ErptrSecurityRptrLogTime_Type()
)
erptrSecurityRptrLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrSecurityRptrLogTime.setStatus("mandatory")
_ErptrSecurityRptrLogPhysAddress_Type = PhysAddress
_ErptrSecurityRptrLogPhysAddress_Object = MibTableColumn
erptrSecurityRptrLogPhysAddress = _ErptrSecurityRptrLogPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2, 1, 5),
    _ErptrSecurityRptrLogPhysAddress_Type()
)
erptrSecurityRptrLogPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrSecurityRptrLogPhysAddress.setStatus("mandatory")


class _ErptrSecurityRptrLogCapacity_Type(Integer32):
    """Custom type erptrSecurityRptrLogCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ErptrSecurityRptrLogCapacity_Type.__name__ = "Integer32"
_ErptrSecurityRptrLogCapacity_Object = MibScalar
erptrSecurityRptrLogCapacity = _ErptrSecurityRptrLogCapacity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 3),
    _ErptrSecurityRptrLogCapacity_Type()
)
erptrSecurityRptrLogCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrSecurityRptrLogCapacity.setStatus("mandatory")
_ErptrSecurityGroupInfo_ObjectIdentity = ObjectIdentity
erptrSecurityGroupInfo = _ErptrSecurityGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 2)
)
_ErptrSecurityPortInfo_ObjectIdentity = ObjectIdentity
erptrSecurityPortInfo = _ErptrSecurityPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3)
)
_ErptrSecurityPortCtrlTable_Object = MibTable
erptrSecurityPortCtrlTable = _ErptrSecurityPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    erptrSecurityPortCtrlTable.setStatus("mandatory")
_ErptrSecurityPortCtrlEntry_Object = MibTableRow
erptrSecurityPortCtrlEntry = _ErptrSecurityPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1)
)
erptrSecurityPortCtrlEntry.setIndexNames(
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrSecurityPortCtrlGroupIndex"),
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrSecurityPortCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    erptrSecurityPortCtrlEntry.setStatus("mandatory")


class _ErptrSecurityPortCtrlGroupIndex_Type(Integer32):
    """Custom type erptrSecurityPortCtrlGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrSecurityPortCtrlGroupIndex_Type.__name__ = "Integer32"
_ErptrSecurityPortCtrlGroupIndex_Object = MibTableColumn
erptrSecurityPortCtrlGroupIndex = _ErptrSecurityPortCtrlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1, 1),
    _ErptrSecurityPortCtrlGroupIndex_Type()
)
erptrSecurityPortCtrlGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrSecurityPortCtrlGroupIndex.setStatus("mandatory")


class _ErptrSecurityPortCtrlPortIndex_Type(Integer32):
    """Custom type erptrSecurityPortCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrSecurityPortCtrlPortIndex_Type.__name__ = "Integer32"
_ErptrSecurityPortCtrlPortIndex_Object = MibTableColumn
erptrSecurityPortCtrlPortIndex = _ErptrSecurityPortCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1, 2),
    _ErptrSecurityPortCtrlPortIndex_Type()
)
erptrSecurityPortCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrSecurityPortCtrlPortIndex.setStatus("mandatory")


class _ErptrSecurityPortCtrlEavesdropMode_Type(Integer32):
    """Custom type erptrSecurityPortCtrlEavesdropMode based on Integer32"""
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


_ErptrSecurityPortCtrlEavesdropMode_Type.__name__ = "Integer32"
_ErptrSecurityPortCtrlEavesdropMode_Object = MibTableColumn
erptrSecurityPortCtrlEavesdropMode = _ErptrSecurityPortCtrlEavesdropMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1, 3),
    _ErptrSecurityPortCtrlEavesdropMode_Type()
)
erptrSecurityPortCtrlEavesdropMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrSecurityPortCtrlEavesdropMode.setStatus("mandatory")


class _ErptrSecurityPortCtrlIntrusionMode_Type(Integer32):
    """Custom type erptrSecurityPortCtrlIntrusionMode based on Integer32"""
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
        *(("disablePort", 4),
          ("disabled", 1),
          ("jamUnauthPackets", 3),
          ("notifyOnly", 2))
    )


_ErptrSecurityPortCtrlIntrusionMode_Type.__name__ = "Integer32"
_ErptrSecurityPortCtrlIntrusionMode_Object = MibTableColumn
erptrSecurityPortCtrlIntrusionMode = _ErptrSecurityPortCtrlIntrusionMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1, 4),
    _ErptrSecurityPortCtrlIntrusionMode_Type()
)
erptrSecurityPortCtrlIntrusionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrSecurityPortCtrlIntrusionMode.setStatus("mandatory")


class _ErptrSecurityPortCtrlOperStatus_Type(Integer32):
    """Custom type erptrSecurityPortCtrlOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("securityNotOperational", 2),
          ("securityOperational", 1),
          ("violationPortDisabled", 3))
    )


_ErptrSecurityPortCtrlOperStatus_Type.__name__ = "Integer32"
_ErptrSecurityPortCtrlOperStatus_Object = MibTableColumn
erptrSecurityPortCtrlOperStatus = _ErptrSecurityPortCtrlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1, 5),
    _ErptrSecurityPortCtrlOperStatus_Type()
)
erptrSecurityPortCtrlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrSecurityPortCtrlOperStatus.setStatus("mandatory")
_ErptrSecurityPortCtrlViolations_Type = Counter32
_ErptrSecurityPortCtrlViolations_Object = MibTableColumn
erptrSecurityPortCtrlViolations = _ErptrSecurityPortCtrlViolations_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1, 6),
    _ErptrSecurityPortCtrlViolations_Type()
)
erptrSecurityPortCtrlViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrSecurityPortCtrlViolations.setStatus("mandatory")
_ErptrSecurityPortAddrTable_Object = MibTable
erptrSecurityPortAddrTable = _ErptrSecurityPortAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    erptrSecurityPortAddrTable.setStatus("mandatory")
_ErptrSecurityPortAddrEntry_Object = MibTableRow
erptrSecurityPortAddrEntry = _ErptrSecurityPortAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 2, 1)
)
erptrSecurityPortAddrEntry.setIndexNames(
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrSecurityPortAddrGroupIndex"),
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrSecurityPortAddrPortIndex"),
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrSecurityPortAddrPhysAddress"),
)
if mibBuilder.loadTexts:
    erptrSecurityPortAddrEntry.setStatus("mandatory")


class _ErptrSecurityPortAddrGroupIndex_Type(Integer32):
    """Custom type erptrSecurityPortAddrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrSecurityPortAddrGroupIndex_Type.__name__ = "Integer32"
_ErptrSecurityPortAddrGroupIndex_Object = MibTableColumn
erptrSecurityPortAddrGroupIndex = _ErptrSecurityPortAddrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 2, 1, 1),
    _ErptrSecurityPortAddrGroupIndex_Type()
)
erptrSecurityPortAddrGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrSecurityPortAddrGroupIndex.setStatus("mandatory")


class _ErptrSecurityPortAddrPortIndex_Type(Integer32):
    """Custom type erptrSecurityPortAddrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrSecurityPortAddrPortIndex_Type.__name__ = "Integer32"
_ErptrSecurityPortAddrPortIndex_Object = MibTableColumn
erptrSecurityPortAddrPortIndex = _ErptrSecurityPortAddrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 2, 1, 2),
    _ErptrSecurityPortAddrPortIndex_Type()
)
erptrSecurityPortAddrPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrSecurityPortAddrPortIndex.setStatus("mandatory")
_ErptrSecurityPortAddrPhysAddress_Type = PhysAddress
_ErptrSecurityPortAddrPhysAddress_Object = MibTableColumn
erptrSecurityPortAddrPhysAddress = _ErptrSecurityPortAddrPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 2, 1, 3),
    _ErptrSecurityPortAddrPhysAddress_Type()
)
erptrSecurityPortAddrPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrSecurityPortAddrPhysAddress.setStatus("mandatory")


class _ErptrSecurityPortAddrStatus_Type(Integer32):
    """Custom type erptrSecurityPortAddrStatus based on Integer32"""
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


_ErptrSecurityPortAddrStatus_Type.__name__ = "Integer32"
_ErptrSecurityPortAddrStatus_Object = MibTableColumn
erptrSecurityPortAddrStatus = _ErptrSecurityPortAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 2, 1, 4),
    _ErptrSecurityPortAddrStatus_Type()
)
erptrSecurityPortAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrSecurityPortAddrStatus.setStatus("mandatory")
_ErptrMauPackage_ObjectIdentity = ObjectIdentity
erptrMauPackage = _ErptrMauPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5)
)
_ErptrMauRptrInfo_ObjectIdentity = ObjectIdentity
erptrMauRptrInfo = _ErptrMauRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 1)
)
_ErptrMauTotalMediaUnavailable_Type = Gauge32
_ErptrMauTotalMediaUnavailable_Object = MibScalar
erptrMauTotalMediaUnavailable = _ErptrMauTotalMediaUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 1, 1),
    _ErptrMauTotalMediaUnavailable_Type()
)
erptrMauTotalMediaUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrMauTotalMediaUnavailable.setStatus("mandatory")
_ErptrMauGroupInfo_ObjectIdentity = ObjectIdentity
erptrMauGroupInfo = _ErptrMauGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 2)
)
_ErptrMauPortInfo_ObjectIdentity = ObjectIdentity
erptrMauPortInfo = _ErptrMauPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3)
)
_ErptrMauTable_Object = MibTable
erptrMauTable = _ErptrMauTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    erptrMauTable.setStatus("mandatory")
_ErptrMauEntry_Object = MibTableRow
erptrMauEntry = _ErptrMauEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1)
)
erptrMauEntry.setIndexNames(
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrMauGroupIndex"),
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrMauPortIndex"),
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrMauIndex"),
)
if mibBuilder.loadTexts:
    erptrMauEntry.setStatus("mandatory")


class _ErptrMauGroupIndex_Type(Integer32):
    """Custom type erptrMauGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrMauGroupIndex_Type.__name__ = "Integer32"
_ErptrMauGroupIndex_Object = MibTableColumn
erptrMauGroupIndex = _ErptrMauGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 1),
    _ErptrMauGroupIndex_Type()
)
erptrMauGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrMauGroupIndex.setStatus("mandatory")


class _ErptrMauPortIndex_Type(Integer32):
    """Custom type erptrMauPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrMauPortIndex_Type.__name__ = "Integer32"
_ErptrMauPortIndex_Object = MibTableColumn
erptrMauPortIndex = _ErptrMauPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 2),
    _ErptrMauPortIndex_Type()
)
erptrMauPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrMauPortIndex.setStatus("mandatory")


class _ErptrMauIndex_Type(Integer32):
    """Custom type erptrMauIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrMauIndex_Type.__name__ = "Integer32"
_ErptrMauIndex_Object = MibTableColumn
erptrMauIndex = _ErptrMauIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 3),
    _ErptrMauIndex_Type()
)
erptrMauIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrMauIndex.setStatus("mandatory")


class _ErptrMauLinkTestAdminStatus_Type(Integer32):
    """Custom type erptrMauLinkTestAdminStatus based on Integer32"""
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


_ErptrMauLinkTestAdminStatus_Type.__name__ = "Integer32"
_ErptrMauLinkTestAdminStatus_Object = MibTableColumn
erptrMauLinkTestAdminStatus = _ErptrMauLinkTestAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 4),
    _ErptrMauLinkTestAdminStatus_Type()
)
erptrMauLinkTestAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrMauLinkTestAdminStatus.setStatus("mandatory")


class _ErptrMauMediaPolarityStatus_Type(Integer32):
    """Custom type erptrMauMediaPolarityStatus based on Integer32"""
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
        *(("polarityCorrected", 3),
          ("polarityNotReversed", 1),
          ("polarityReversed", 2),
          ("unknown", 4))
    )


_ErptrMauMediaPolarityStatus_Type.__name__ = "Integer32"
_ErptrMauMediaPolarityStatus_Object = MibTableColumn
erptrMauMediaPolarityStatus = _ErptrMauMediaPolarityStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 5),
    _ErptrMauMediaPolarityStatus_Type()
)
erptrMauMediaPolarityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrMauMediaPolarityStatus.setStatus("mandatory")


class _ErptrMauMediaAvailable_Type(Integer32):
    """Custom type erptrMauMediaAvailable based on Integer32"""
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
        *(("available", 3),
          ("invalidSignal", 6),
          ("notAvailable", 4),
          ("other", 1),
          ("remoteFault", 5),
          ("unknown", 2))
    )


_ErptrMauMediaAvailable_Type.__name__ = "Integer32"
_ErptrMauMediaAvailable_Object = MibTableColumn
erptrMauMediaAvailable = _ErptrMauMediaAvailable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 6),
    _ErptrMauMediaAvailable_Type()
)
erptrMauMediaAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrMauMediaAvailable.setStatus("mandatory")
_ErptrMauMediaAvailableChanges_Type = Counter32
_ErptrMauMediaAvailableChanges_Object = MibTableColumn
erptrMauMediaAvailableChanges = _ErptrMauMediaAvailableChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 7),
    _ErptrMauMediaAvailableChanges_Type()
)
erptrMauMediaAvailableChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrMauMediaAvailableChanges.setStatus("mandatory")


class _ErptrMauMaxLinkLength_Type(Integer32):
    """Custom type erptrMauMaxLinkLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("standard", 1))
    )


_ErptrMauMaxLinkLength_Type.__name__ = "Integer32"
_ErptrMauMaxLinkLength_Object = MibTableColumn
erptrMauMaxLinkLength = _ErptrMauMaxLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 8),
    _ErptrMauMaxLinkLength_Type()
)
erptrMauMaxLinkLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrMauMaxLinkLength.setStatus("mandatory")
_ErptrAddrLearnPackage_ObjectIdentity = ObjectIdentity
erptrAddrLearnPackage = _ErptrAddrLearnPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6)
)
_ErptrAddrLearnRptrInfo_ObjectIdentity = ObjectIdentity
erptrAddrLearnRptrInfo = _ErptrAddrLearnRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 1)
)
_ErptrAddrLearnGroupInfo_ObjectIdentity = ObjectIdentity
erptrAddrLearnGroupInfo = _ErptrAddrLearnGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 2)
)
_ErptrAddrLearnPortInfo_ObjectIdentity = ObjectIdentity
erptrAddrLearnPortInfo = _ErptrAddrLearnPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3)
)
_ErptrAddrLearnPortCtrlTable_Object = MibTable
erptrAddrLearnPortCtrlTable = _ErptrAddrLearnPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    erptrAddrLearnPortCtrlTable.setStatus("mandatory")
_ErptrAddrLearnPortCtrlEntry_Object = MibTableRow
erptrAddrLearnPortCtrlEntry = _ErptrAddrLearnPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1, 1)
)
erptrAddrLearnPortCtrlEntry.setIndexNames(
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrAddrLearnPortCtrlGroupIndex"),
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrAddrLearnPortCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    erptrAddrLearnPortCtrlEntry.setStatus("mandatory")


class _ErptrAddrLearnPortCtrlGroupIndex_Type(Integer32):
    """Custom type erptrAddrLearnPortCtrlGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrAddrLearnPortCtrlGroupIndex_Type.__name__ = "Integer32"
_ErptrAddrLearnPortCtrlGroupIndex_Object = MibTableColumn
erptrAddrLearnPortCtrlGroupIndex = _ErptrAddrLearnPortCtrlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1, 1, 1),
    _ErptrAddrLearnPortCtrlGroupIndex_Type()
)
erptrAddrLearnPortCtrlGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrAddrLearnPortCtrlGroupIndex.setStatus("mandatory")


class _ErptrAddrLearnPortCtrlPortIndex_Type(Integer32):
    """Custom type erptrAddrLearnPortCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrAddrLearnPortCtrlPortIndex_Type.__name__ = "Integer32"
_ErptrAddrLearnPortCtrlPortIndex_Object = MibTableColumn
erptrAddrLearnPortCtrlPortIndex = _ErptrAddrLearnPortCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1, 1, 2),
    _ErptrAddrLearnPortCtrlPortIndex_Type()
)
erptrAddrLearnPortCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrAddrLearnPortCtrlPortIndex.setStatus("mandatory")


class _ErptrAddrLearnPortCtrlCapacity_Type(Integer32):
    """Custom type erptrAddrLearnPortCtrlCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ErptrAddrLearnPortCtrlCapacity_Type.__name__ = "Integer32"
_ErptrAddrLearnPortCtrlCapacity_Object = MibTableColumn
erptrAddrLearnPortCtrlCapacity = _ErptrAddrLearnPortCtrlCapacity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1, 1, 3),
    _ErptrAddrLearnPortCtrlCapacity_Type()
)
erptrAddrLearnPortCtrlCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrAddrLearnPortCtrlCapacity.setStatus("mandatory")


class _ErptrAddrLearnPortCtrlAdminStatus_Type(Integer32):
    """Custom type erptrAddrLearnPortCtrlAdminStatus based on Integer32"""
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
        *(("clearLearnedAddresses", 4),
          ("disableLearning", 3),
          ("enableLearning", 2),
          ("other", 1))
    )


_ErptrAddrLearnPortCtrlAdminStatus_Type.__name__ = "Integer32"
_ErptrAddrLearnPortCtrlAdminStatus_Object = MibTableColumn
erptrAddrLearnPortCtrlAdminStatus = _ErptrAddrLearnPortCtrlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1, 1, 4),
    _ErptrAddrLearnPortCtrlAdminStatus_Type()
)
erptrAddrLearnPortCtrlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erptrAddrLearnPortCtrlAdminStatus.setStatus("mandatory")


class _ErptrAddrLearnPortCtrlOperStatus_Type(Integer32):
    """Custom type erptrAddrLearnPortCtrlOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("learningDisabled", 3),
          ("learningEnabledAndActive", 1),
          ("learningEnabledAndStopped", 2))
    )


_ErptrAddrLearnPortCtrlOperStatus_Type.__name__ = "Integer32"
_ErptrAddrLearnPortCtrlOperStatus_Object = MibTableColumn
erptrAddrLearnPortCtrlOperStatus = _ErptrAddrLearnPortCtrlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1, 1, 5),
    _ErptrAddrLearnPortCtrlOperStatus_Type()
)
erptrAddrLearnPortCtrlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrAddrLearnPortCtrlOperStatus.setStatus("mandatory")
_ErptrAddrLearnPortAddressTable_Object = MibTable
erptrAddrLearnPortAddressTable = _ErptrAddrLearnPortAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    erptrAddrLearnPortAddressTable.setStatus("mandatory")
_ErptrAddrLearnPortAddressEntry_Object = MibTableRow
erptrAddrLearnPortAddressEntry = _ErptrAddrLearnPortAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 2, 1)
)
erptrAddrLearnPortAddressEntry.setIndexNames(
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrAddrLearnPortAddressGroupIndex"),
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrAddrLearnPortAddressPortIndex"),
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrAddrLearnPortAddressIndex"),
)
if mibBuilder.loadTexts:
    erptrAddrLearnPortAddressEntry.setStatus("mandatory")


class _ErptrAddrLearnPortAddressGroupIndex_Type(Integer32):
    """Custom type erptrAddrLearnPortAddressGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrAddrLearnPortAddressGroupIndex_Type.__name__ = "Integer32"
_ErptrAddrLearnPortAddressGroupIndex_Object = MibTableColumn
erptrAddrLearnPortAddressGroupIndex = _ErptrAddrLearnPortAddressGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 2, 1, 1),
    _ErptrAddrLearnPortAddressGroupIndex_Type()
)
erptrAddrLearnPortAddressGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrAddrLearnPortAddressGroupIndex.setStatus("mandatory")


class _ErptrAddrLearnPortAddressPortIndex_Type(Integer32):
    """Custom type erptrAddrLearnPortAddressPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrAddrLearnPortAddressPortIndex_Type.__name__ = "Integer32"
_ErptrAddrLearnPortAddressPortIndex_Object = MibTableColumn
erptrAddrLearnPortAddressPortIndex = _ErptrAddrLearnPortAddressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 2, 1, 2),
    _ErptrAddrLearnPortAddressPortIndex_Type()
)
erptrAddrLearnPortAddressPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrAddrLearnPortAddressPortIndex.setStatus("mandatory")


class _ErptrAddrLearnPortAddressIndex_Type(Integer32):
    """Custom type erptrAddrLearnPortAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ErptrAddrLearnPortAddressIndex_Type.__name__ = "Integer32"
_ErptrAddrLearnPortAddressIndex_Object = MibTableColumn
erptrAddrLearnPortAddressIndex = _ErptrAddrLearnPortAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 2, 1, 3),
    _ErptrAddrLearnPortAddressIndex_Type()
)
erptrAddrLearnPortAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrAddrLearnPortAddressIndex.setStatus("mandatory")
_ErptrAddrLearnPortAddress_Type = PhysAddress
_ErptrAddrLearnPortAddress_Object = MibTableColumn
erptrAddrLearnPortAddress = _ErptrAddrLearnPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 2, 1, 4),
    _ErptrAddrLearnPortAddress_Type()
)
erptrAddrLearnPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrAddrLearnPortAddress.setStatus("mandatory")
_ErptrMonitorPackage_ObjectIdentity = ObjectIdentity
erptrMonitorPackage = _ErptrMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7)
)
_ErptrMonitorRptrInfo_ObjectIdentity = ObjectIdentity
erptrMonitorRptrInfo = _ErptrMonitorRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 1)
)
_ErptrMonitorGroupInfo_ObjectIdentity = ObjectIdentity
erptrMonitorGroupInfo = _ErptrMonitorGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 2)
)
_ErptrMonitorPortInfo_ObjectIdentity = ObjectIdentity
erptrMonitorPortInfo = _ErptrMonitorPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3)
)
_ErptrMonitorPortTable_Object = MibTable
erptrMonitorPortTable = _ErptrMonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    erptrMonitorPortTable.setStatus("mandatory")
_ErptrMonitorPortEntry_Object = MibTableRow
erptrMonitorPortEntry = _ErptrMonitorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3, 1, 1)
)
erptrMonitorPortEntry.setIndexNames(
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrMonitorPortGroupIndex"),
    (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrMonitorPortIndex"),
)
if mibBuilder.loadTexts:
    erptrMonitorPortEntry.setStatus("mandatory")


class _ErptrMonitorPortGroupIndex_Type(Integer32):
    """Custom type erptrMonitorPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrMonitorPortGroupIndex_Type.__name__ = "Integer32"
_ErptrMonitorPortGroupIndex_Object = MibTableColumn
erptrMonitorPortGroupIndex = _ErptrMonitorPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3, 1, 1, 1),
    _ErptrMonitorPortGroupIndex_Type()
)
erptrMonitorPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrMonitorPortGroupIndex.setStatus("mandatory")


class _ErptrMonitorPortIndex_Type(Integer32):
    """Custom type erptrMonitorPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErptrMonitorPortIndex_Type.__name__ = "Integer32"
_ErptrMonitorPortIndex_Object = MibTableColumn
erptrMonitorPortIndex = _ErptrMonitorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3, 1, 1, 2),
    _ErptrMonitorPortIndex_Type()
)
erptrMonitorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrMonitorPortIndex.setStatus("mandatory")
_ErptrMonitorPortMulticastFrames_Type = Counter32
_ErptrMonitorPortMulticastFrames_Object = MibTableColumn
erptrMonitorPortMulticastFrames = _ErptrMonitorPortMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3, 1, 1, 3),
    _ErptrMonitorPortMulticastFrames_Type()
)
erptrMonitorPortMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrMonitorPortMulticastFrames.setStatus("mandatory")
_ErptrMonitorPortBroadcastFrames_Type = Counter32
_ErptrMonitorPortBroadcastFrames_Object = MibTableColumn
erptrMonitorPortBroadcastFrames = _ErptrMonitorPortBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3, 1, 1, 4),
    _ErptrMonitorPortBroadcastFrames_Type()
)
erptrMonitorPortBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erptrMonitorPortBroadcastFrames.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DECHUB900-ERPTR-MIB-V3-0",
    **{"dec": dec,
       "ema": ema,
       "decMIBextension": decMIBextension,
       "decHub900": decHub900,
       "repeater": repeater,
       "rptrVersion1": rptrVersion1,
       "rptrExtensions": rptrExtensions,
       "erptrBasicPackage": erptrBasicPackage,
       "erptrRptrInfo": erptrRptrInfo,
       "erptrAutoPartitionAlg": erptrAutoPartitionAlg,
       "erptrAutoPartitionReconnectAlg": erptrAutoPartitionReconnectAlg,
       "erptrJamBits": erptrJamBits,
       "erptrHealthTextChanges": erptrHealthTextChanges,
       "erptrTotalPortEvents": erptrTotalPortEvents,
       "erptrTotalRptrErrors": erptrTotalRptrErrors,
       "erptrJabberProtectionAdminStatus": erptrJabberProtectionAdminStatus,
       "erptrTotalPorts": erptrTotalPorts,
       "erptrPMDCarrierCardType": erptrPMDCarrierCardType,
       "erptrGroupInfo": erptrGroupInfo,
       "erptrGroupTable": erptrGroupTable,
       "erptrGroupEntry": erptrGroupEntry,
       "erptrGroupIndex": erptrGroupIndex,
       "erptrGroupTransmitCollisions": erptrGroupTransmitCollisions,
       "erptrGroupReset": erptrGroupReset,
       "erptrGroupLanTotalOctets": erptrGroupLanTotalOctets,
       "erptrPortInfo": erptrPortInfo,
       "erptrPortTable": erptrPortTable,
       "erptrPortEntry": erptrPortEntry,
       "erptrPortGroupIndex": erptrPortGroupIndex,
       "erptrPortIndex": erptrPortIndex,
       "erptrPortName": erptrPortName,
       "erptrPortPartitions": erptrPortPartitions,
       "erptrPortPartitionReason": erptrPortPartitionReason,
       "erptrPortMAUType": erptrPortMAUType,
       "erptrPortSQETestError": erptrPortSQETestError,
       "erptrAddrDBPackage": erptrAddrDBPackage,
       "erptrAddrDBRptrInfo": erptrAddrDBRptrInfo,
       "erptrAddrDBTableCapacity": erptrAddrDBTableCapacity,
       "erptrAddrDBGroupInfo": erptrAddrDBGroupInfo,
       "erptrAddrDBPortInfo": erptrAddrDBPortInfo,
       "erptrAddrDBPortAddrTable": erptrAddrDBPortAddrTable,
       "erptrAddrDBPortAddrEntry": erptrAddrDBPortAddrEntry,
       "erptrAddrDBPortPhyAddr": erptrAddrDBPortPhyAddr,
       "erptrAddrDBPortGroupIndex": erptrAddrDBPortGroupIndex,
       "erptrAddrDBPortIndex": erptrAddrDBPortIndex,
       "erptrDprPackage": erptrDprPackage,
       "erptrDprRptrInfo": erptrDprRptrInfo,
       "erptrDprTotalStateChanges": erptrDprTotalStateChanges,
       "erptrDprGroupInfo": erptrDprGroupInfo,
       "erptrDprPortInfo": erptrDprPortInfo,
       "erptrDprLinkTable": erptrDprLinkTable,
       "erptrDprLinkEntry": erptrDprLinkEntry,
       "erptrDprLinkGroupIndex": erptrDprLinkGroupIndex,
       "erptrDprLinkPortIndex": erptrDprLinkPortIndex,
       "erptrDprLinkType": erptrDprLinkType,
       "erptrDprLinkToggle": erptrDprLinkToggle,
       "erptrDprLinkOperStatus": erptrDprLinkOperStatus,
       "erptrDprSecondaryGroupIndex": erptrDprSecondaryGroupIndex,
       "erptrDprSecondaryPortIndex": erptrDprSecondaryPortIndex,
       "erptrDprSecondaryOperStatus": erptrDprSecondaryOperStatus,
       "erptrDprLinkName": erptrDprLinkName,
       "erptrDprLinkStateChanges": erptrDprLinkStateChanges,
       "erptrDprLinkEntryStatus": erptrDprLinkEntryStatus,
       "erptrSecurityPackage": erptrSecurityPackage,
       "erptrSecurityRptrInfo": erptrSecurityRptrInfo,
       "erptrSecurityRptrSecurityViolations": erptrSecurityRptrSecurityViolations,
       "erptrSecurityRptrLogTable": erptrSecurityRptrLogTable,
       "erptrSecurityRptrLogEntry": erptrSecurityRptrLogEntry,
       "erptrSecurityRptrLogIndex": erptrSecurityRptrLogIndex,
       "erptrSecurityRptrLogGroupIndex": erptrSecurityRptrLogGroupIndex,
       "erptrSecurityRptrLogPortIndex": erptrSecurityRptrLogPortIndex,
       "erptrSecurityRptrLogTime": erptrSecurityRptrLogTime,
       "erptrSecurityRptrLogPhysAddress": erptrSecurityRptrLogPhysAddress,
       "erptrSecurityRptrLogCapacity": erptrSecurityRptrLogCapacity,
       "erptrSecurityGroupInfo": erptrSecurityGroupInfo,
       "erptrSecurityPortInfo": erptrSecurityPortInfo,
       "erptrSecurityPortCtrlTable": erptrSecurityPortCtrlTable,
       "erptrSecurityPortCtrlEntry": erptrSecurityPortCtrlEntry,
       "erptrSecurityPortCtrlGroupIndex": erptrSecurityPortCtrlGroupIndex,
       "erptrSecurityPortCtrlPortIndex": erptrSecurityPortCtrlPortIndex,
       "erptrSecurityPortCtrlEavesdropMode": erptrSecurityPortCtrlEavesdropMode,
       "erptrSecurityPortCtrlIntrusionMode": erptrSecurityPortCtrlIntrusionMode,
       "erptrSecurityPortCtrlOperStatus": erptrSecurityPortCtrlOperStatus,
       "erptrSecurityPortCtrlViolations": erptrSecurityPortCtrlViolations,
       "erptrSecurityPortAddrTable": erptrSecurityPortAddrTable,
       "erptrSecurityPortAddrEntry": erptrSecurityPortAddrEntry,
       "erptrSecurityPortAddrGroupIndex": erptrSecurityPortAddrGroupIndex,
       "erptrSecurityPortAddrPortIndex": erptrSecurityPortAddrPortIndex,
       "erptrSecurityPortAddrPhysAddress": erptrSecurityPortAddrPhysAddress,
       "erptrSecurityPortAddrStatus": erptrSecurityPortAddrStatus,
       "erptrMauPackage": erptrMauPackage,
       "erptrMauRptrInfo": erptrMauRptrInfo,
       "erptrMauTotalMediaUnavailable": erptrMauTotalMediaUnavailable,
       "erptrMauGroupInfo": erptrMauGroupInfo,
       "erptrMauPortInfo": erptrMauPortInfo,
       "erptrMauTable": erptrMauTable,
       "erptrMauEntry": erptrMauEntry,
       "erptrMauGroupIndex": erptrMauGroupIndex,
       "erptrMauPortIndex": erptrMauPortIndex,
       "erptrMauIndex": erptrMauIndex,
       "erptrMauLinkTestAdminStatus": erptrMauLinkTestAdminStatus,
       "erptrMauMediaPolarityStatus": erptrMauMediaPolarityStatus,
       "erptrMauMediaAvailable": erptrMauMediaAvailable,
       "erptrMauMediaAvailableChanges": erptrMauMediaAvailableChanges,
       "erptrMauMaxLinkLength": erptrMauMaxLinkLength,
       "erptrAddrLearnPackage": erptrAddrLearnPackage,
       "erptrAddrLearnRptrInfo": erptrAddrLearnRptrInfo,
       "erptrAddrLearnGroupInfo": erptrAddrLearnGroupInfo,
       "erptrAddrLearnPortInfo": erptrAddrLearnPortInfo,
       "erptrAddrLearnPortCtrlTable": erptrAddrLearnPortCtrlTable,
       "erptrAddrLearnPortCtrlEntry": erptrAddrLearnPortCtrlEntry,
       "erptrAddrLearnPortCtrlGroupIndex": erptrAddrLearnPortCtrlGroupIndex,
       "erptrAddrLearnPortCtrlPortIndex": erptrAddrLearnPortCtrlPortIndex,
       "erptrAddrLearnPortCtrlCapacity": erptrAddrLearnPortCtrlCapacity,
       "erptrAddrLearnPortCtrlAdminStatus": erptrAddrLearnPortCtrlAdminStatus,
       "erptrAddrLearnPortCtrlOperStatus": erptrAddrLearnPortCtrlOperStatus,
       "erptrAddrLearnPortAddressTable": erptrAddrLearnPortAddressTable,
       "erptrAddrLearnPortAddressEntry": erptrAddrLearnPortAddressEntry,
       "erptrAddrLearnPortAddressGroupIndex": erptrAddrLearnPortAddressGroupIndex,
       "erptrAddrLearnPortAddressPortIndex": erptrAddrLearnPortAddressPortIndex,
       "erptrAddrLearnPortAddressIndex": erptrAddrLearnPortAddressIndex,
       "erptrAddrLearnPortAddress": erptrAddrLearnPortAddress,
       "erptrMonitorPackage": erptrMonitorPackage,
       "erptrMonitorRptrInfo": erptrMonitorRptrInfo,
       "erptrMonitorGroupInfo": erptrMonitorGroupInfo,
       "erptrMonitorPortInfo": erptrMonitorPortInfo,
       "erptrMonitorPortTable": erptrMonitorPortTable,
       "erptrMonitorPortEntry": erptrMonitorPortEntry,
       "erptrMonitorPortGroupIndex": erptrMonitorPortGroupIndex,
       "erptrMonitorPortIndex": erptrMonitorPortIndex,
       "erptrMonitorPortMulticastFrames": erptrMonitorPortMulticastFrames,
       "erptrMonitorPortBroadcastFrames": erptrMonitorPortBroadcastFrames}
)
