# SNMP MIB module (Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:04 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "DashedHexString",
    "HexString",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

(mscVr,
 mscVrIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-VirtualRouterMIB",
    "mscVr",
    "mscVrIndex")

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

_MscVrSres_ObjectIdentity = ObjectIdentity
mscVrSres = _MscVrSres_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13)
)
_MscVrSresRowStatusTable_Object = MibTable
mscVrSresRowStatusTable = _MscVrSresRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 1)
)
if mibBuilder.loadTexts:
    mscVrSresRowStatusTable.setStatus("mandatory")
_MscVrSresRowStatusEntry_Object = MibTableRow
mscVrSresRowStatusEntry = _MscVrSresRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 1, 1)
)
mscVrSresRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB", "mscVrSresIndex"),
)
if mibBuilder.loadTexts:
    mscVrSresRowStatusEntry.setStatus("mandatory")
_MscVrSresRowStatus_Type = RowStatus
_MscVrSresRowStatus_Object = MibTableColumn
mscVrSresRowStatus = _MscVrSresRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 1, 1, 1),
    _MscVrSresRowStatus_Type()
)
mscVrSresRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSresRowStatus.setStatus("mandatory")
_MscVrSresComponentName_Type = DisplayString
_MscVrSresComponentName_Object = MibTableColumn
mscVrSresComponentName = _MscVrSresComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 1, 1, 2),
    _MscVrSresComponentName_Type()
)
mscVrSresComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresComponentName.setStatus("mandatory")
_MscVrSresStorageType_Type = StorageType
_MscVrSresStorageType_Object = MibTableColumn
mscVrSresStorageType = _MscVrSresStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 1, 1, 4),
    _MscVrSresStorageType_Type()
)
mscVrSresStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresStorageType.setStatus("mandatory")
_MscVrSresIndex_Type = NonReplicated
_MscVrSresIndex_Object = MibTableColumn
mscVrSresIndex = _MscVrSresIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 1, 1, 10),
    _MscVrSresIndex_Type()
)
mscVrSresIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSresIndex.setStatus("mandatory")
_MscVrSresRe_ObjectIdentity = ObjectIdentity
mscVrSresRe = _MscVrSresRe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2)
)
_MscVrSresReRowStatusTable_Object = MibTable
mscVrSresReRowStatusTable = _MscVrSresReRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrSresReRowStatusTable.setStatus("mandatory")
_MscVrSresReRowStatusEntry_Object = MibTableRow
mscVrSresReRowStatusEntry = _MscVrSresReRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2, 1, 1)
)
mscVrSresReRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB", "mscVrSresIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB", "mscVrSresReDestMacAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB", "mscVrSresReProtocolPortNameIndex"),
)
if mibBuilder.loadTexts:
    mscVrSresReRowStatusEntry.setStatus("mandatory")
_MscVrSresReRowStatus_Type = RowStatus
_MscVrSresReRowStatus_Object = MibTableColumn
mscVrSresReRowStatus = _MscVrSresReRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2, 1, 1, 1),
    _MscVrSresReRowStatus_Type()
)
mscVrSresReRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresReRowStatus.setStatus("mandatory")
_MscVrSresReComponentName_Type = DisplayString
_MscVrSresReComponentName_Object = MibTableColumn
mscVrSresReComponentName = _MscVrSresReComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2, 1, 1, 2),
    _MscVrSresReComponentName_Type()
)
mscVrSresReComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresReComponentName.setStatus("mandatory")
_MscVrSresReStorageType_Type = StorageType
_MscVrSresReStorageType_Object = MibTableColumn
mscVrSresReStorageType = _MscVrSresReStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2, 1, 1, 4),
    _MscVrSresReStorageType_Type()
)
mscVrSresReStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresReStorageType.setStatus("mandatory")


class _MscVrSresReDestMacAddressIndex_Type(DashedHexString):
    """Custom type mscVrSresReDestMacAddressIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscVrSresReDestMacAddressIndex_Type.__name__ = "DashedHexString"
_MscVrSresReDestMacAddressIndex_Object = MibTableColumn
mscVrSresReDestMacAddressIndex = _MscVrSresReDestMacAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2, 1, 1, 10),
    _MscVrSresReDestMacAddressIndex_Type()
)
mscVrSresReDestMacAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSresReDestMacAddressIndex.setStatus("mandatory")


class _MscVrSresReProtocolPortNameIndex_Type(AsciiStringIndex):
    """Custom type mscVrSresReProtocolPortNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MscVrSresReProtocolPortNameIndex_Type.__name__ = "AsciiStringIndex"
_MscVrSresReProtocolPortNameIndex_Object = MibTableColumn
mscVrSresReProtocolPortNameIndex = _MscVrSresReProtocolPortNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2, 1, 1, 11),
    _MscVrSresReProtocolPortNameIndex_Type()
)
mscVrSresReProtocolPortNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrSresReProtocolPortNameIndex.setStatus("mandatory")
_MscVrSresReOperTable_Object = MibTable
mscVrSresReOperTable = _MscVrSresReOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrSresReOperTable.setStatus("mandatory")
_MscVrSresReOperEntry_Object = MibTableRow
mscVrSresReOperEntry = _MscVrSresReOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2, 10, 1)
)
mscVrSresReOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB", "mscVrSresIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB", "mscVrSresReDestMacAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB", "mscVrSresReProtocolPortNameIndex"),
)
if mibBuilder.loadTexts:
    mscVrSresReOperEntry.setStatus("mandatory")


class _MscVrSresReRouteControl_Type(HexString):
    """Custom type mscVrSresReRouteControl based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscVrSresReRouteControl_Type.__name__ = "HexString"
_MscVrSresReRouteControl_Object = MibTableColumn
mscVrSresReRouteControl = _MscVrSresReRouteControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2, 10, 1, 1),
    _MscVrSresReRouteControl_Type()
)
mscVrSresReRouteControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresReRouteControl.setStatus("mandatory")


class _MscVrSresReRifLength_Type(Unsigned32):
    """Custom type mscVrSresReRifLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_MscVrSresReRifLength_Type.__name__ = "Unsigned32"
_MscVrSresReRifLength_Object = MibTableColumn
mscVrSresReRifLength = _MscVrSresReRifLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2, 10, 1, 2),
    _MscVrSresReRifLength_Type()
)
mscVrSresReRifLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresReRifLength.setStatus("mandatory")


class _MscVrSresReRdDirection_Type(Integer32):
    """Custom type mscVrSresReRdDirection based on Integer32"""
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


_MscVrSresReRdDirection_Type.__name__ = "Integer32"
_MscVrSresReRdDirection_Object = MibTableColumn
mscVrSresReRdDirection = _MscVrSresReRdDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2, 10, 1, 3),
    _MscVrSresReRdDirection_Type()
)
mscVrSresReRdDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresReRdDirection.setStatus("mandatory")


class _MscVrSresReRouteDescr_Type(AsciiString):
    """Custom type mscVrSresReRouteDescr based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 90),
    )


_MscVrSresReRouteDescr_Type.__name__ = "AsciiString"
_MscVrSresReRouteDescr_Object = MibTableColumn
mscVrSresReRouteDescr = _MscVrSresReRouteDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 2, 10, 1, 4),
    _MscVrSresReRouteDescr_Type()
)
mscVrSresReRouteDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresReRouteDescr.setStatus("mandatory")
_MscVrSresAdminControlTable_Object = MibTable
mscVrSresAdminControlTable = _MscVrSresAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 10)
)
if mibBuilder.loadTexts:
    mscVrSresAdminControlTable.setStatus("mandatory")
_MscVrSresAdminControlEntry_Object = MibTableRow
mscVrSresAdminControlEntry = _MscVrSresAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 10, 1)
)
mscVrSresAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB", "mscVrSresIndex"),
)
if mibBuilder.loadTexts:
    mscVrSresAdminControlEntry.setStatus("mandatory")


class _MscVrSresSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrSresSnmpAdminStatus based on Integer32"""
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


_MscVrSresSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrSresSnmpAdminStatus_Object = MibTableColumn
mscVrSresSnmpAdminStatus = _MscVrSresSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 10, 1, 1),
    _MscVrSresSnmpAdminStatus_Type()
)
mscVrSresSnmpAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresSnmpAdminStatus.setStatus("mandatory")
_MscVrSresProvTable_Object = MibTable
mscVrSresProvTable = _MscVrSresProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 11)
)
if mibBuilder.loadTexts:
    mscVrSresProvTable.setStatus("mandatory")
_MscVrSresProvEntry_Object = MibTableRow
mscVrSresProvEntry = _MscVrSresProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 11, 1)
)
mscVrSresProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB", "mscVrSresIndex"),
)
if mibBuilder.loadTexts:
    mscVrSresProvEntry.setStatus("mandatory")


class _MscVrSresRouteTableNumEntries_Type(Unsigned32):
    """Custom type mscVrSresRouteTableNumEntries based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrSresRouteTableNumEntries_Type.__name__ = "Unsigned32"
_MscVrSresRouteTableNumEntries_Object = MibTableColumn
mscVrSresRouteTableNumEntries = _MscVrSresRouteTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 11, 1, 1),
    _MscVrSresRouteTableNumEntries_Type()
)
mscVrSresRouteTableNumEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSresRouteTableNumEntries.setStatus("mandatory")


class _MscVrSresAgingTime_Type(Unsigned32):
    """Custom type mscVrSresAgingTime based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000000),
    )


_MscVrSresAgingTime_Type.__name__ = "Unsigned32"
_MscVrSresAgingTime_Object = MibTableColumn
mscVrSresAgingTime = _MscVrSresAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 11, 1, 2),
    _MscVrSresAgingTime_Type()
)
mscVrSresAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrSresAgingTime.setStatus("mandatory")


class _MscVrSresRouteDescriptorLength_Type(Unsigned32):
    """Custom type mscVrSresRouteDescriptorLength based on Unsigned32"""
    defaultValue = 14

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 14),
    )


_MscVrSresRouteDescriptorLength_Type.__name__ = "Unsigned32"
_MscVrSresRouteDescriptorLength_Object = MibTableColumn
mscVrSresRouteDescriptorLength = _MscVrSresRouteDescriptorLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 11, 1, 3),
    _MscVrSresRouteDescriptorLength_Type()
)
mscVrSresRouteDescriptorLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresRouteDescriptorLength.setStatus("mandatory")
_MscVrSresOperStatusTable_Object = MibTable
mscVrSresOperStatusTable = _MscVrSresOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 12)
)
if mibBuilder.loadTexts:
    mscVrSresOperStatusTable.setStatus("mandatory")
_MscVrSresOperStatusEntry_Object = MibTableRow
mscVrSresOperStatusEntry = _MscVrSresOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 12, 1)
)
mscVrSresOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB", "mscVrSresIndex"),
)
if mibBuilder.loadTexts:
    mscVrSresOperStatusEntry.setStatus("mandatory")


class _MscVrSresSnmpOperStatus_Type(Integer32):
    """Custom type mscVrSresSnmpOperStatus based on Integer32"""
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


_MscVrSresSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrSresSnmpOperStatus_Object = MibTableColumn
mscVrSresSnmpOperStatus = _MscVrSresSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 12, 1, 1),
    _MscVrSresSnmpOperStatus_Type()
)
mscVrSresSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresSnmpOperStatus.setStatus("mandatory")
_MscVrSresStateTable_Object = MibTable
mscVrSresStateTable = _MscVrSresStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 13)
)
if mibBuilder.loadTexts:
    mscVrSresStateTable.setStatus("mandatory")
_MscVrSresStateEntry_Object = MibTableRow
mscVrSresStateEntry = _MscVrSresStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 13, 1)
)
mscVrSresStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB", "mscVrSresIndex"),
)
if mibBuilder.loadTexts:
    mscVrSresStateEntry.setStatus("mandatory")


class _MscVrSresAdminState_Type(Integer32):
    """Custom type mscVrSresAdminState based on Integer32"""
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


_MscVrSresAdminState_Type.__name__ = "Integer32"
_MscVrSresAdminState_Object = MibTableColumn
mscVrSresAdminState = _MscVrSresAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 13, 1, 1),
    _MscVrSresAdminState_Type()
)
mscVrSresAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresAdminState.setStatus("mandatory")


class _MscVrSresOperationalState_Type(Integer32):
    """Custom type mscVrSresOperationalState based on Integer32"""
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


_MscVrSresOperationalState_Type.__name__ = "Integer32"
_MscVrSresOperationalState_Object = MibTableColumn
mscVrSresOperationalState = _MscVrSresOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 13, 1, 2),
    _MscVrSresOperationalState_Type()
)
mscVrSresOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresOperationalState.setStatus("mandatory")


class _MscVrSresUsageState_Type(Integer32):
    """Custom type mscVrSresUsageState based on Integer32"""
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


_MscVrSresUsageState_Type.__name__ = "Integer32"
_MscVrSresUsageState_Object = MibTableColumn
mscVrSresUsageState = _MscVrSresUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 13, 1, 3),
    _MscVrSresUsageState_Type()
)
mscVrSresUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresUsageState.setStatus("mandatory")
_MscVrSresOperTable_Object = MibTable
mscVrSresOperTable = _MscVrSresOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 14)
)
if mibBuilder.loadTexts:
    mscVrSresOperTable.setStatus("mandatory")
_MscVrSresOperEntry_Object = MibTableRow
mscVrSresOperEntry = _MscVrSresOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 14, 1)
)
mscVrSresOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB", "mscVrSresIndex"),
)
if mibBuilder.loadTexts:
    mscVrSresOperEntry.setStatus("mandatory")


class _MscVrSresRtEntriesUsed_Type(Gauge32):
    """Custom type mscVrSresRtEntriesUsed based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrSresRtEntriesUsed_Type.__name__ = "Gauge32"
_MscVrSresRtEntriesUsed_Object = MibTableColumn
mscVrSresRtEntriesUsed = _MscVrSresRtEntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 14, 1, 1),
    _MscVrSresRtEntriesUsed_Type()
)
mscVrSresRtEntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresRtEntriesUsed.setStatus("mandatory")


class _MscVrSresRtEntriesFree_Type(Gauge32):
    """Custom type mscVrSresRtEntriesFree based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrSresRtEntriesFree_Type.__name__ = "Gauge32"
_MscVrSresRtEntriesFree_Object = MibTableColumn
mscVrSresRtEntriesFree = _MscVrSresRtEntriesFree_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 14, 1, 2),
    _MscVrSresRtEntriesFree_Type()
)
mscVrSresRtEntriesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresRtEntriesFree.setStatus("mandatory")
_MscVrSresRtEntriesDenied_Type = Counter32
_MscVrSresRtEntriesDenied_Object = MibTableColumn
mscVrSresRtEntriesDenied = _MscVrSresRtEntriesDenied_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 13, 14, 1, 3),
    _MscVrSresRtEntriesDenied_Type()
)
mscVrSresRtEntriesDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrSresRtEntriesDenied.setStatus("mandatory")
_SourceRouteEndStationMIB_ObjectIdentity = ObjectIdentity
sourceRouteEndStationMIB = _SourceRouteEndStationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 54)
)
_SourceRouteEndStationGroup_ObjectIdentity = ObjectIdentity
sourceRouteEndStationGroup = _SourceRouteEndStationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 54, 1)
)
_SourceRouteEndStationGroupCA_ObjectIdentity = ObjectIdentity
sourceRouteEndStationGroupCA = _SourceRouteEndStationGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 54, 1, 1)
)
_SourceRouteEndStationGroupCA02_ObjectIdentity = ObjectIdentity
sourceRouteEndStationGroupCA02 = _SourceRouteEndStationGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 54, 1, 1, 3)
)
_SourceRouteEndStationGroupCA02A_ObjectIdentity = ObjectIdentity
sourceRouteEndStationGroupCA02A = _SourceRouteEndStationGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 54, 1, 1, 3, 2)
)
_SourceRouteEndStationCapabilities_ObjectIdentity = ObjectIdentity
sourceRouteEndStationCapabilities = _SourceRouteEndStationCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 54, 3)
)
_SourceRouteEndStationCapabilitiesCA_ObjectIdentity = ObjectIdentity
sourceRouteEndStationCapabilitiesCA = _SourceRouteEndStationCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 54, 3, 1)
)
_SourceRouteEndStationCapabilitiesCA02_ObjectIdentity = ObjectIdentity
sourceRouteEndStationCapabilitiesCA02 = _SourceRouteEndStationCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 54, 3, 1, 3)
)
_SourceRouteEndStationCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
sourceRouteEndStationCapabilitiesCA02A = _SourceRouteEndStationCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 54, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-SourceRouteEndStationMIB",
    **{"mscVrSres": mscVrSres,
       "mscVrSresRowStatusTable": mscVrSresRowStatusTable,
       "mscVrSresRowStatusEntry": mscVrSresRowStatusEntry,
       "mscVrSresRowStatus": mscVrSresRowStatus,
       "mscVrSresComponentName": mscVrSresComponentName,
       "mscVrSresStorageType": mscVrSresStorageType,
       "mscVrSresIndex": mscVrSresIndex,
       "mscVrSresRe": mscVrSresRe,
       "mscVrSresReRowStatusTable": mscVrSresReRowStatusTable,
       "mscVrSresReRowStatusEntry": mscVrSresReRowStatusEntry,
       "mscVrSresReRowStatus": mscVrSresReRowStatus,
       "mscVrSresReComponentName": mscVrSresReComponentName,
       "mscVrSresReStorageType": mscVrSresReStorageType,
       "mscVrSresReDestMacAddressIndex": mscVrSresReDestMacAddressIndex,
       "mscVrSresReProtocolPortNameIndex": mscVrSresReProtocolPortNameIndex,
       "mscVrSresReOperTable": mscVrSresReOperTable,
       "mscVrSresReOperEntry": mscVrSresReOperEntry,
       "mscVrSresReRouteControl": mscVrSresReRouteControl,
       "mscVrSresReRifLength": mscVrSresReRifLength,
       "mscVrSresReRdDirection": mscVrSresReRdDirection,
       "mscVrSresReRouteDescr": mscVrSresReRouteDescr,
       "mscVrSresAdminControlTable": mscVrSresAdminControlTable,
       "mscVrSresAdminControlEntry": mscVrSresAdminControlEntry,
       "mscVrSresSnmpAdminStatus": mscVrSresSnmpAdminStatus,
       "mscVrSresProvTable": mscVrSresProvTable,
       "mscVrSresProvEntry": mscVrSresProvEntry,
       "mscVrSresRouteTableNumEntries": mscVrSresRouteTableNumEntries,
       "mscVrSresAgingTime": mscVrSresAgingTime,
       "mscVrSresRouteDescriptorLength": mscVrSresRouteDescriptorLength,
       "mscVrSresOperStatusTable": mscVrSresOperStatusTable,
       "mscVrSresOperStatusEntry": mscVrSresOperStatusEntry,
       "mscVrSresSnmpOperStatus": mscVrSresSnmpOperStatus,
       "mscVrSresStateTable": mscVrSresStateTable,
       "mscVrSresStateEntry": mscVrSresStateEntry,
       "mscVrSresAdminState": mscVrSresAdminState,
       "mscVrSresOperationalState": mscVrSresOperationalState,
       "mscVrSresUsageState": mscVrSresUsageState,
       "mscVrSresOperTable": mscVrSresOperTable,
       "mscVrSresOperEntry": mscVrSresOperEntry,
       "mscVrSresRtEntriesUsed": mscVrSresRtEntriesUsed,
       "mscVrSresRtEntriesFree": mscVrSresRtEntriesFree,
       "mscVrSresRtEntriesDenied": mscVrSresRtEntriesDenied,
       "sourceRouteEndStationMIB": sourceRouteEndStationMIB,
       "sourceRouteEndStationGroup": sourceRouteEndStationGroup,
       "sourceRouteEndStationGroupCA": sourceRouteEndStationGroupCA,
       "sourceRouteEndStationGroupCA02": sourceRouteEndStationGroupCA02,
       "sourceRouteEndStationGroupCA02A": sourceRouteEndStationGroupCA02A,
       "sourceRouteEndStationCapabilities": sourceRouteEndStationCapabilities,
       "sourceRouteEndStationCapabilitiesCA": sourceRouteEndStationCapabilitiesCA,
       "sourceRouteEndStationCapabilitiesCA02": sourceRouteEndStationCapabilitiesCA02,
       "sourceRouteEndStationCapabilitiesCA02A": sourceRouteEndStationCapabilitiesCA02A}
)
