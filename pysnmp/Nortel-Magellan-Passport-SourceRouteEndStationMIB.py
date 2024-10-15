# SNMP MIB module (Nortel-Magellan-Passport-SourceRouteEndStationMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-SourceRouteEndStationMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:23 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 DashedHexString,
 HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "DashedHexString",
    "HexString",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

(vr,
 vrIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VirtualRouterMIB",
    "vr",
    "vrIndex")

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

_VrSres_ObjectIdentity = ObjectIdentity
vrSres = _VrSres_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13)
)
_VrSresRowStatusTable_Object = MibTable
vrSresRowStatusTable = _VrSresRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 1)
)
if mibBuilder.loadTexts:
    vrSresRowStatusTable.setStatus("mandatory")
_VrSresRowStatusEntry_Object = MibTableRow
vrSresRowStatusEntry = _VrSresRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 1, 1)
)
vrSresRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SourceRouteEndStationMIB", "vrSresIndex"),
)
if mibBuilder.loadTexts:
    vrSresRowStatusEntry.setStatus("mandatory")
_VrSresRowStatus_Type = RowStatus
_VrSresRowStatus_Object = MibTableColumn
vrSresRowStatus = _VrSresRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 1, 1, 1),
    _VrSresRowStatus_Type()
)
vrSresRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSresRowStatus.setStatus("mandatory")
_VrSresComponentName_Type = DisplayString
_VrSresComponentName_Object = MibTableColumn
vrSresComponentName = _VrSresComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 1, 1, 2),
    _VrSresComponentName_Type()
)
vrSresComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresComponentName.setStatus("mandatory")
_VrSresStorageType_Type = StorageType
_VrSresStorageType_Object = MibTableColumn
vrSresStorageType = _VrSresStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 1, 1, 4),
    _VrSresStorageType_Type()
)
vrSresStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresStorageType.setStatus("mandatory")
_VrSresIndex_Type = NonReplicated
_VrSresIndex_Object = MibTableColumn
vrSresIndex = _VrSresIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 1, 1, 10),
    _VrSresIndex_Type()
)
vrSresIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSresIndex.setStatus("mandatory")
_VrSresRe_ObjectIdentity = ObjectIdentity
vrSresRe = _VrSresRe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2)
)
_VrSresReRowStatusTable_Object = MibTable
vrSresReRowStatusTable = _VrSresReRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2, 1)
)
if mibBuilder.loadTexts:
    vrSresReRowStatusTable.setStatus("mandatory")
_VrSresReRowStatusEntry_Object = MibTableRow
vrSresReRowStatusEntry = _VrSresReRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2, 1, 1)
)
vrSresReRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SourceRouteEndStationMIB", "vrSresIndex"),
    (0, "Nortel-Magellan-Passport-SourceRouteEndStationMIB", "vrSresReDestMacAddressIndex"),
    (0, "Nortel-Magellan-Passport-SourceRouteEndStationMIB", "vrSresReProtocolPortNameIndex"),
)
if mibBuilder.loadTexts:
    vrSresReRowStatusEntry.setStatus("mandatory")
_VrSresReRowStatus_Type = RowStatus
_VrSresReRowStatus_Object = MibTableColumn
vrSresReRowStatus = _VrSresReRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2, 1, 1, 1),
    _VrSresReRowStatus_Type()
)
vrSresReRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresReRowStatus.setStatus("mandatory")
_VrSresReComponentName_Type = DisplayString
_VrSresReComponentName_Object = MibTableColumn
vrSresReComponentName = _VrSresReComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2, 1, 1, 2),
    _VrSresReComponentName_Type()
)
vrSresReComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresReComponentName.setStatus("mandatory")
_VrSresReStorageType_Type = StorageType
_VrSresReStorageType_Object = MibTableColumn
vrSresReStorageType = _VrSresReStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2, 1, 1, 4),
    _VrSresReStorageType_Type()
)
vrSresReStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresReStorageType.setStatus("mandatory")


class _VrSresReDestMacAddressIndex_Type(DashedHexString):
    """Custom type vrSresReDestMacAddressIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_VrSresReDestMacAddressIndex_Type.__name__ = "DashedHexString"
_VrSresReDestMacAddressIndex_Object = MibTableColumn
vrSresReDestMacAddressIndex = _VrSresReDestMacAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2, 1, 1, 10),
    _VrSresReDestMacAddressIndex_Type()
)
vrSresReDestMacAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSresReDestMacAddressIndex.setStatus("mandatory")


class _VrSresReProtocolPortNameIndex_Type(AsciiStringIndex):
    """Custom type vrSresReProtocolPortNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_VrSresReProtocolPortNameIndex_Type.__name__ = "AsciiStringIndex"
_VrSresReProtocolPortNameIndex_Object = MibTableColumn
vrSresReProtocolPortNameIndex = _VrSresReProtocolPortNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2, 1, 1, 11),
    _VrSresReProtocolPortNameIndex_Type()
)
vrSresReProtocolPortNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrSresReProtocolPortNameIndex.setStatus("mandatory")
_VrSresReOperTable_Object = MibTable
vrSresReOperTable = _VrSresReOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2, 10)
)
if mibBuilder.loadTexts:
    vrSresReOperTable.setStatus("mandatory")
_VrSresReOperEntry_Object = MibTableRow
vrSresReOperEntry = _VrSresReOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2, 10, 1)
)
vrSresReOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SourceRouteEndStationMIB", "vrSresIndex"),
    (0, "Nortel-Magellan-Passport-SourceRouteEndStationMIB", "vrSresReDestMacAddressIndex"),
    (0, "Nortel-Magellan-Passport-SourceRouteEndStationMIB", "vrSresReProtocolPortNameIndex"),
)
if mibBuilder.loadTexts:
    vrSresReOperEntry.setStatus("mandatory")


class _VrSresReRouteControl_Type(HexString):
    """Custom type vrSresReRouteControl based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VrSresReRouteControl_Type.__name__ = "HexString"
_VrSresReRouteControl_Object = MibTableColumn
vrSresReRouteControl = _VrSresReRouteControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2, 10, 1, 1),
    _VrSresReRouteControl_Type()
)
vrSresReRouteControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresReRouteControl.setStatus("mandatory")


class _VrSresReRifLength_Type(Unsigned32):
    """Custom type vrSresReRifLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_VrSresReRifLength_Type.__name__ = "Unsigned32"
_VrSresReRifLength_Object = MibTableColumn
vrSresReRifLength = _VrSresReRifLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2, 10, 1, 2),
    _VrSresReRifLength_Type()
)
vrSresReRifLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresReRifLength.setStatus("mandatory")


class _VrSresReRdDirection_Type(Integer32):
    """Custom type vrSresReRdDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leftToRight", 0),
          ("noRif", 2),
          ("rightToLeft", 1))
    )


_VrSresReRdDirection_Type.__name__ = "Integer32"
_VrSresReRdDirection_Object = MibTableColumn
vrSresReRdDirection = _VrSresReRdDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2, 10, 1, 3),
    _VrSresReRdDirection_Type()
)
vrSresReRdDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresReRdDirection.setStatus("mandatory")


class _VrSresReRouteDescr_Type(AsciiString):
    """Custom type vrSresReRouteDescr based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 90),
    )


_VrSresReRouteDescr_Type.__name__ = "AsciiString"
_VrSresReRouteDescr_Object = MibTableColumn
vrSresReRouteDescr = _VrSresReRouteDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 2, 10, 1, 4),
    _VrSresReRouteDescr_Type()
)
vrSresReRouteDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresReRouteDescr.setStatus("mandatory")
_VrSresAdminControlTable_Object = MibTable
vrSresAdminControlTable = _VrSresAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 10)
)
if mibBuilder.loadTexts:
    vrSresAdminControlTable.setStatus("mandatory")
_VrSresAdminControlEntry_Object = MibTableRow
vrSresAdminControlEntry = _VrSresAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 10, 1)
)
vrSresAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SourceRouteEndStationMIB", "vrSresIndex"),
)
if mibBuilder.loadTexts:
    vrSresAdminControlEntry.setStatus("mandatory")


class _VrSresSnmpAdminStatus_Type(Integer32):
    """Custom type vrSresSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_VrSresSnmpAdminStatus_Type.__name__ = "Integer32"
_VrSresSnmpAdminStatus_Object = MibTableColumn
vrSresSnmpAdminStatus = _VrSresSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 10, 1, 1),
    _VrSresSnmpAdminStatus_Type()
)
vrSresSnmpAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresSnmpAdminStatus.setStatus("mandatory")
_VrSresProvTable_Object = MibTable
vrSresProvTable = _VrSresProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 11)
)
if mibBuilder.loadTexts:
    vrSresProvTable.setStatus("mandatory")
_VrSresProvEntry_Object = MibTableRow
vrSresProvEntry = _VrSresProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 11, 1)
)
vrSresProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SourceRouteEndStationMIB", "vrSresIndex"),
)
if mibBuilder.loadTexts:
    vrSresProvEntry.setStatus("mandatory")


class _VrSresRouteTableNumEntries_Type(Unsigned32):
    """Custom type vrSresRouteTableNumEntries based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrSresRouteTableNumEntries_Type.__name__ = "Unsigned32"
_VrSresRouteTableNumEntries_Object = MibTableColumn
vrSresRouteTableNumEntries = _VrSresRouteTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 11, 1, 1),
    _VrSresRouteTableNumEntries_Type()
)
vrSresRouteTableNumEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSresRouteTableNumEntries.setStatus("mandatory")


class _VrSresAgingTime_Type(Unsigned32):
    """Custom type vrSresAgingTime based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000000),
    )


_VrSresAgingTime_Type.__name__ = "Unsigned32"
_VrSresAgingTime_Object = MibTableColumn
vrSresAgingTime = _VrSresAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 11, 1, 2),
    _VrSresAgingTime_Type()
)
vrSresAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrSresAgingTime.setStatus("mandatory")


class _VrSresRouteDescriptorLength_Type(Unsigned32):
    """Custom type vrSresRouteDescriptorLength based on Unsigned32"""
    defaultValue = 14

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 14),
    )


_VrSresRouteDescriptorLength_Type.__name__ = "Unsigned32"
_VrSresRouteDescriptorLength_Object = MibTableColumn
vrSresRouteDescriptorLength = _VrSresRouteDescriptorLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 11, 1, 3),
    _VrSresRouteDescriptorLength_Type()
)
vrSresRouteDescriptorLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresRouteDescriptorLength.setStatus("mandatory")
_VrSresOperStatusTable_Object = MibTable
vrSresOperStatusTable = _VrSresOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 12)
)
if mibBuilder.loadTexts:
    vrSresOperStatusTable.setStatus("mandatory")
_VrSresOperStatusEntry_Object = MibTableRow
vrSresOperStatusEntry = _VrSresOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 12, 1)
)
vrSresOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SourceRouteEndStationMIB", "vrSresIndex"),
)
if mibBuilder.loadTexts:
    vrSresOperStatusEntry.setStatus("mandatory")


class _VrSresSnmpOperStatus_Type(Integer32):
    """Custom type vrSresSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_VrSresSnmpOperStatus_Type.__name__ = "Integer32"
_VrSresSnmpOperStatus_Object = MibTableColumn
vrSresSnmpOperStatus = _VrSresSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 12, 1, 1),
    _VrSresSnmpOperStatus_Type()
)
vrSresSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresSnmpOperStatus.setStatus("mandatory")
_VrSresStateTable_Object = MibTable
vrSresStateTable = _VrSresStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 13)
)
if mibBuilder.loadTexts:
    vrSresStateTable.setStatus("mandatory")
_VrSresStateEntry_Object = MibTableRow
vrSresStateEntry = _VrSresStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 13, 1)
)
vrSresStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SourceRouteEndStationMIB", "vrSresIndex"),
)
if mibBuilder.loadTexts:
    vrSresStateEntry.setStatus("mandatory")


class _VrSresAdminState_Type(Integer32):
    """Custom type vrSresAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_VrSresAdminState_Type.__name__ = "Integer32"
_VrSresAdminState_Object = MibTableColumn
vrSresAdminState = _VrSresAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 13, 1, 1),
    _VrSresAdminState_Type()
)
vrSresAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresAdminState.setStatus("mandatory")


class _VrSresOperationalState_Type(Integer32):
    """Custom type vrSresOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VrSresOperationalState_Type.__name__ = "Integer32"
_VrSresOperationalState_Object = MibTableColumn
vrSresOperationalState = _VrSresOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 13, 1, 2),
    _VrSresOperationalState_Type()
)
vrSresOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresOperationalState.setStatus("mandatory")


class _VrSresUsageState_Type(Integer32):
    """Custom type vrSresUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_VrSresUsageState_Type.__name__ = "Integer32"
_VrSresUsageState_Object = MibTableColumn
vrSresUsageState = _VrSresUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 13, 1, 3),
    _VrSresUsageState_Type()
)
vrSresUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresUsageState.setStatus("mandatory")
_VrSresOperTable_Object = MibTable
vrSresOperTable = _VrSresOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 14)
)
if mibBuilder.loadTexts:
    vrSresOperTable.setStatus("mandatory")
_VrSresOperEntry_Object = MibTableRow
vrSresOperEntry = _VrSresOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 14, 1)
)
vrSresOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-SourceRouteEndStationMIB", "vrSresIndex"),
)
if mibBuilder.loadTexts:
    vrSresOperEntry.setStatus("mandatory")


class _VrSresRtEntriesUsed_Type(Gauge32):
    """Custom type vrSresRtEntriesUsed based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrSresRtEntriesUsed_Type.__name__ = "Gauge32"
_VrSresRtEntriesUsed_Object = MibTableColumn
vrSresRtEntriesUsed = _VrSresRtEntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 14, 1, 1),
    _VrSresRtEntriesUsed_Type()
)
vrSresRtEntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresRtEntriesUsed.setStatus("mandatory")


class _VrSresRtEntriesFree_Type(Gauge32):
    """Custom type vrSresRtEntriesFree based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrSresRtEntriesFree_Type.__name__ = "Gauge32"
_VrSresRtEntriesFree_Object = MibTableColumn
vrSresRtEntriesFree = _VrSresRtEntriesFree_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 14, 1, 2),
    _VrSresRtEntriesFree_Type()
)
vrSresRtEntriesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresRtEntriesFree.setStatus("mandatory")
_VrSresRtEntriesDenied_Type = Counter32
_VrSresRtEntriesDenied_Object = MibTableColumn
vrSresRtEntriesDenied = _VrSresRtEntriesDenied_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 13, 14, 1, 3),
    _VrSresRtEntriesDenied_Type()
)
vrSresRtEntriesDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrSresRtEntriesDenied.setStatus("mandatory")
_SourceRouteEndStationMIB_ObjectIdentity = ObjectIdentity
sourceRouteEndStationMIB = _SourceRouteEndStationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 54)
)
_SourceRouteEndStationGroup_ObjectIdentity = ObjectIdentity
sourceRouteEndStationGroup = _SourceRouteEndStationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 54, 1)
)
_SourceRouteEndStationGroupBD_ObjectIdentity = ObjectIdentity
sourceRouteEndStationGroupBD = _SourceRouteEndStationGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 54, 1, 4)
)
_SourceRouteEndStationGroupBD01_ObjectIdentity = ObjectIdentity
sourceRouteEndStationGroupBD01 = _SourceRouteEndStationGroupBD01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 54, 1, 4, 2)
)
_SourceRouteEndStationGroupBD01A_ObjectIdentity = ObjectIdentity
sourceRouteEndStationGroupBD01A = _SourceRouteEndStationGroupBD01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 54, 1, 4, 2, 2)
)
_SourceRouteEndStationCapabilities_ObjectIdentity = ObjectIdentity
sourceRouteEndStationCapabilities = _SourceRouteEndStationCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 54, 3)
)
_SourceRouteEndStationCapabilitiesBD_ObjectIdentity = ObjectIdentity
sourceRouteEndStationCapabilitiesBD = _SourceRouteEndStationCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 54, 3, 4)
)
_SourceRouteEndStationCapabilitiesBD01_ObjectIdentity = ObjectIdentity
sourceRouteEndStationCapabilitiesBD01 = _SourceRouteEndStationCapabilitiesBD01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 54, 3, 4, 2)
)
_SourceRouteEndStationCapabilitiesBD01A_ObjectIdentity = ObjectIdentity
sourceRouteEndStationCapabilitiesBD01A = _SourceRouteEndStationCapabilitiesBD01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 54, 3, 4, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-SourceRouteEndStationMIB",
    **{"vrSres": vrSres,
       "vrSresRowStatusTable": vrSresRowStatusTable,
       "vrSresRowStatusEntry": vrSresRowStatusEntry,
       "vrSresRowStatus": vrSresRowStatus,
       "vrSresComponentName": vrSresComponentName,
       "vrSresStorageType": vrSresStorageType,
       "vrSresIndex": vrSresIndex,
       "vrSresRe": vrSresRe,
       "vrSresReRowStatusTable": vrSresReRowStatusTable,
       "vrSresReRowStatusEntry": vrSresReRowStatusEntry,
       "vrSresReRowStatus": vrSresReRowStatus,
       "vrSresReComponentName": vrSresReComponentName,
       "vrSresReStorageType": vrSresReStorageType,
       "vrSresReDestMacAddressIndex": vrSresReDestMacAddressIndex,
       "vrSresReProtocolPortNameIndex": vrSresReProtocolPortNameIndex,
       "vrSresReOperTable": vrSresReOperTable,
       "vrSresReOperEntry": vrSresReOperEntry,
       "vrSresReRouteControl": vrSresReRouteControl,
       "vrSresReRifLength": vrSresReRifLength,
       "vrSresReRdDirection": vrSresReRdDirection,
       "vrSresReRouteDescr": vrSresReRouteDescr,
       "vrSresAdminControlTable": vrSresAdminControlTable,
       "vrSresAdminControlEntry": vrSresAdminControlEntry,
       "vrSresSnmpAdminStatus": vrSresSnmpAdminStatus,
       "vrSresProvTable": vrSresProvTable,
       "vrSresProvEntry": vrSresProvEntry,
       "vrSresRouteTableNumEntries": vrSresRouteTableNumEntries,
       "vrSresAgingTime": vrSresAgingTime,
       "vrSresRouteDescriptorLength": vrSresRouteDescriptorLength,
       "vrSresOperStatusTable": vrSresOperStatusTable,
       "vrSresOperStatusEntry": vrSresOperStatusEntry,
       "vrSresSnmpOperStatus": vrSresSnmpOperStatus,
       "vrSresStateTable": vrSresStateTable,
       "vrSresStateEntry": vrSresStateEntry,
       "vrSresAdminState": vrSresAdminState,
       "vrSresOperationalState": vrSresOperationalState,
       "vrSresUsageState": vrSresUsageState,
       "vrSresOperTable": vrSresOperTable,
       "vrSresOperEntry": vrSresOperEntry,
       "vrSresRtEntriesUsed": vrSresRtEntriesUsed,
       "vrSresRtEntriesFree": vrSresRtEntriesFree,
       "vrSresRtEntriesDenied": vrSresRtEntriesDenied,
       "sourceRouteEndStationMIB": sourceRouteEndStationMIB,
       "sourceRouteEndStationGroup": sourceRouteEndStationGroup,
       "sourceRouteEndStationGroupBD": sourceRouteEndStationGroupBD,
       "sourceRouteEndStationGroupBD01": sourceRouteEndStationGroupBD01,
       "sourceRouteEndStationGroupBD01A": sourceRouteEndStationGroupBD01A,
       "sourceRouteEndStationCapabilities": sourceRouteEndStationCapabilities,
       "sourceRouteEndStationCapabilitiesBD": sourceRouteEndStationCapabilitiesBD,
       "sourceRouteEndStationCapabilitiesBD01": sourceRouteEndStationCapabilitiesBD01,
       "sourceRouteEndStationCapabilitiesBD01A": sourceRouteEndStationCapabilitiesBD01A}
)
