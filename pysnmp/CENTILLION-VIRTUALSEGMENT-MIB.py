# SNMP MIB module (CENTILLION-VIRTUALSEGMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-VIRTUALSEGMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:06 2024
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

(BridgeGroupId,) = mibBuilder.importSymbols(
    "CENTILLION-BRIDGEGROUP-MIB",
    "BridgeGroupId")

(Boolean,
 StatusIndicator,
 sysConfig) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "Boolean",
    "StatusIndicator",
    "sysConfig")

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



class VirtualSegmentTypeId(Integer32):
    """Custom type VirtualSegmentTypeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 3),
          ("other", 1),
          ("token-ring", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VirtualSegmentGroup_ObjectIdentity = ObjectIdentity
virtualSegmentGroup = _VirtualSegmentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23)
)
_VirtualSegmentConfigNumber_Type = Integer32
_VirtualSegmentConfigNumber_Object = MibScalar
virtualSegmentConfigNumber = _VirtualSegmentConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 1),
    _VirtualSegmentConfigNumber_Type()
)
virtualSegmentConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualSegmentConfigNumber.setStatus("mandatory")
_VirtualSegmentActiveNumber_Type = Integer32
_VirtualSegmentActiveNumber_Object = MibScalar
virtualSegmentActiveNumber = _VirtualSegmentActiveNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 2),
    _VirtualSegmentActiveNumber_Type()
)
virtualSegmentActiveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualSegmentActiveNumber.setStatus("mandatory")
_VirtualSegmentTable_Object = MibTable
virtualSegmentTable = _VirtualSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3)
)
if mibBuilder.loadTexts:
    virtualSegmentTable.setStatus("mandatory")
_VirtualSegmentEntry_Object = MibTableRow
virtualSegmentEntry = _VirtualSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1)
)
virtualSegmentEntry.setIndexNames(
    (0, "CENTILLION-VIRTUALSEGMENT-MIB", "virtualSegmentType"),
    (0, "CENTILLION-VIRTUALSEGMENT-MIB", "virtualSegmentId"),
)
if mibBuilder.loadTexts:
    virtualSegmentEntry.setStatus("mandatory")
_VirtualSegmentType_Type = VirtualSegmentTypeId
_VirtualSegmentType_Object = MibTableColumn
virtualSegmentType = _VirtualSegmentType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 1),
    _VirtualSegmentType_Type()
)
virtualSegmentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualSegmentType.setStatus("mandatory")
_VirtualSegmentId_Type = Integer32
_VirtualSegmentId_Object = MibTableColumn
virtualSegmentId = _VirtualSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 2),
    _VirtualSegmentId_Type()
)
virtualSegmentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualSegmentId.setStatus("mandatory")
_VirtualSegmentStatus_Type = StatusIndicator
_VirtualSegmentStatus_Object = MibTableColumn
virtualSegmentStatus = _VirtualSegmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 3),
    _VirtualSegmentStatus_Type()
)
virtualSegmentStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualSegmentStatus.setStatus("mandatory")
_VirtualSegmentIfIndex_Type = Integer32
_VirtualSegmentIfIndex_Object = MibTableColumn
virtualSegmentIfIndex = _VirtualSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 4),
    _VirtualSegmentIfIndex_Type()
)
virtualSegmentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualSegmentIfIndex.setStatus("mandatory")
_VirtualSegmentConfiguredPortNumber_Type = Integer32
_VirtualSegmentConfiguredPortNumber_Object = MibTableColumn
virtualSegmentConfiguredPortNumber = _VirtualSegmentConfiguredPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 5),
    _VirtualSegmentConfiguredPortNumber_Type()
)
virtualSegmentConfiguredPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualSegmentConfiguredPortNumber.setStatus("mandatory")
_VirtualSegmentActivePortNumber_Type = Integer32
_VirtualSegmentActivePortNumber_Object = MibTableColumn
virtualSegmentActivePortNumber = _VirtualSegmentActivePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 6),
    _VirtualSegmentActivePortNumber_Type()
)
virtualSegmentActivePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualSegmentActivePortNumber.setStatus("mandatory")
_VirtualSegmentSpecific_Type = ObjectIdentifier
_VirtualSegmentSpecific_Object = MibTableColumn
virtualSegmentSpecific = _VirtualSegmentSpecific_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 7),
    _VirtualSegmentSpecific_Type()
)
virtualSegmentSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualSegmentSpecific.setStatus("mandatory")


class _VirtualSegmentAdminEncapsulation_Type(Integer32):
    """Custom type virtualSegmentAdminEncapsulation based on Integer32"""
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
        *(("ethernet-csmacd", 4),
          ("ethernet-iso88023", 3),
          ("iso88023-csmacd", 5),
          ("iso88025-tokenRing", 2),
          ("other", 1))
    )


_VirtualSegmentAdminEncapsulation_Type.__name__ = "Integer32"
_VirtualSegmentAdminEncapsulation_Object = MibTableColumn
virtualSegmentAdminEncapsulation = _VirtualSegmentAdminEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 8),
    _VirtualSegmentAdminEncapsulation_Type()
)
virtualSegmentAdminEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualSegmentAdminEncapsulation.setStatus("mandatory")
_VirtualSegmentBridgeGroupIdentifier_Type = BridgeGroupId
_VirtualSegmentBridgeGroupIdentifier_Object = MibTableColumn
virtualSegmentBridgeGroupIdentifier = _VirtualSegmentBridgeGroupIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 9),
    _VirtualSegmentBridgeGroupIdentifier_Type()
)
virtualSegmentBridgeGroupIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualSegmentBridgeGroupIdentifier.setStatus("mandatory")


class _VirtualSegmentGroupName_Type(DisplayString):
    """Custom type virtualSegmentGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VirtualSegmentGroupName_Type.__name__ = "DisplayString"
_VirtualSegmentGroupName_Object = MibTableColumn
virtualSegmentGroupName = _VirtualSegmentGroupName_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 10),
    _VirtualSegmentGroupName_Type()
)
virtualSegmentGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualSegmentGroupName.setStatus("mandatory")


class _VirtualSegmentGroupServer_Type(Boolean):
    """Custom type virtualSegmentGroupServer based on Boolean"""


_VirtualSegmentGroupServer_Object = MibTableColumn
virtualSegmentGroupServer = _VirtualSegmentGroupServer_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 11),
    _VirtualSegmentGroupServer_Type()
)
virtualSegmentGroupServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualSegmentGroupServer.setStatus("mandatory")
_VirtualSegmentPortTable_Object = MibTable
virtualSegmentPortTable = _VirtualSegmentPortTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4)
)
if mibBuilder.loadTexts:
    virtualSegmentPortTable.setStatus("mandatory")
_VirtualSegmentPortEntry_Object = MibTableRow
virtualSegmentPortEntry = _VirtualSegmentPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1)
)
virtualSegmentPortEntry.setIndexNames(
    (0, "CENTILLION-VIRTUALSEGMENT-MIB", "virtualSegmentPortType"),
    (0, "CENTILLION-VIRTUALSEGMENT-MIB", "virtualSegmentPortId"),
    (0, "CENTILLION-VIRTUALSEGMENT-MIB", "virtualSegmentPortCardNumber"),
    (0, "CENTILLION-VIRTUALSEGMENT-MIB", "virtualSegmentPortPortNumber"),
)
if mibBuilder.loadTexts:
    virtualSegmentPortEntry.setStatus("mandatory")
_VirtualSegmentPortType_Type = VirtualSegmentTypeId
_VirtualSegmentPortType_Object = MibTableColumn
virtualSegmentPortType = _VirtualSegmentPortType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1, 1),
    _VirtualSegmentPortType_Type()
)
virtualSegmentPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualSegmentPortType.setStatus("mandatory")
_VirtualSegmentPortId_Type = Integer32
_VirtualSegmentPortId_Object = MibTableColumn
virtualSegmentPortId = _VirtualSegmentPortId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1, 2),
    _VirtualSegmentPortId_Type()
)
virtualSegmentPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualSegmentPortId.setStatus("mandatory")
_VirtualSegmentPortCardNumber_Type = Integer32
_VirtualSegmentPortCardNumber_Object = MibTableColumn
virtualSegmentPortCardNumber = _VirtualSegmentPortCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1, 3),
    _VirtualSegmentPortCardNumber_Type()
)
virtualSegmentPortCardNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualSegmentPortCardNumber.setStatus("mandatory")
_VirtualSegmentPortPortNumber_Type = Integer32
_VirtualSegmentPortPortNumber_Object = MibTableColumn
virtualSegmentPortPortNumber = _VirtualSegmentPortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1, 4),
    _VirtualSegmentPortPortNumber_Type()
)
virtualSegmentPortPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualSegmentPortPortNumber.setStatus("mandatory")
_VirtualSegmentPortStatus_Type = StatusIndicator
_VirtualSegmentPortStatus_Object = MibTableColumn
virtualSegmentPortStatus = _VirtualSegmentPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1, 5),
    _VirtualSegmentPortStatus_Type()
)
virtualSegmentPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualSegmentPortStatus.setStatus("mandatory")
_VirtualSegmentPortIfIndex_Type = Integer32
_VirtualSegmentPortIfIndex_Object = MibTableColumn
virtualSegmentPortIfIndex = _VirtualSegmentPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1, 6),
    _VirtualSegmentPortIfIndex_Type()
)
virtualSegmentPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualSegmentPortIfIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-VIRTUALSEGMENT-MIB",
    **{"VirtualSegmentTypeId": VirtualSegmentTypeId,
       "virtualSegmentGroup": virtualSegmentGroup,
       "virtualSegmentConfigNumber": virtualSegmentConfigNumber,
       "virtualSegmentActiveNumber": virtualSegmentActiveNumber,
       "virtualSegmentTable": virtualSegmentTable,
       "virtualSegmentEntry": virtualSegmentEntry,
       "virtualSegmentType": virtualSegmentType,
       "virtualSegmentId": virtualSegmentId,
       "virtualSegmentStatus": virtualSegmentStatus,
       "virtualSegmentIfIndex": virtualSegmentIfIndex,
       "virtualSegmentConfiguredPortNumber": virtualSegmentConfiguredPortNumber,
       "virtualSegmentActivePortNumber": virtualSegmentActivePortNumber,
       "virtualSegmentSpecific": virtualSegmentSpecific,
       "virtualSegmentAdminEncapsulation": virtualSegmentAdminEncapsulation,
       "virtualSegmentBridgeGroupIdentifier": virtualSegmentBridgeGroupIdentifier,
       "virtualSegmentGroupName": virtualSegmentGroupName,
       "virtualSegmentGroupServer": virtualSegmentGroupServer,
       "virtualSegmentPortTable": virtualSegmentPortTable,
       "virtualSegmentPortEntry": virtualSegmentPortEntry,
       "virtualSegmentPortType": virtualSegmentPortType,
       "virtualSegmentPortId": virtualSegmentPortId,
       "virtualSegmentPortCardNumber": virtualSegmentPortCardNumber,
       "virtualSegmentPortPortNumber": virtualSegmentPortPortNumber,
       "virtualSegmentPortStatus": virtualSegmentPortStatus,
       "virtualSegmentPortIfIndex": virtualSegmentPortIfIndex}
)
