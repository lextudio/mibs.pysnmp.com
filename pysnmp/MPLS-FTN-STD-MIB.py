# SNMP MIB module (MPLS-FTN-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-FTN-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:01 2024
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

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(InterfaceIndexOrZero,
 ifCounterDiscontinuityGroup,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifCounterDiscontinuityGroup",
    "ifGeneralInformationGroup")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(mplsStdMIB,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "mplsStdMIB")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

mplsFTNStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 8)
)
mplsFTNStdMIB.setRevisions(
        ("2004-06-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsFTNEntryIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class MplsFTNEntryIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_MplsFTNNotifications_ObjectIdentity = ObjectIdentity
mplsFTNNotifications = _MplsFTNNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 0)
)
_MplsFTNObjects_ObjectIdentity = ObjectIdentity
mplsFTNObjects = _MplsFTNObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1)
)
_MplsFTNIndexNext_Type = MplsFTNEntryIndexOrZero
_MplsFTNIndexNext_Object = MibScalar
mplsFTNIndexNext = _MplsFTNIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 1),
    _MplsFTNIndexNext_Type()
)
mplsFTNIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFTNIndexNext.setStatus("current")
_MplsFTNTableLastChanged_Type = TimeStamp
_MplsFTNTableLastChanged_Object = MibScalar
mplsFTNTableLastChanged = _MplsFTNTableLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 2),
    _MplsFTNTableLastChanged_Type()
)
mplsFTNTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFTNTableLastChanged.setStatus("current")
_MplsFTNTable_Object = MibTable
mplsFTNTable = _MplsFTNTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3)
)
if mibBuilder.loadTexts:
    mplsFTNTable.setStatus("current")
_MplsFTNEntry_Object = MibTableRow
mplsFTNEntry = _MplsFTNEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1)
)
mplsFTNEntry.setIndexNames(
    (0, "MPLS-FTN-STD-MIB", "mplsFTNIndex"),
)
if mibBuilder.loadTexts:
    mplsFTNEntry.setStatus("current")
_MplsFTNIndex_Type = MplsFTNEntryIndex
_MplsFTNIndex_Object = MibTableColumn
mplsFTNIndex = _MplsFTNIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 1),
    _MplsFTNIndex_Type()
)
mplsFTNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFTNIndex.setStatus("current")
_MplsFTNRowStatus_Type = RowStatus
_MplsFTNRowStatus_Object = MibTableColumn
mplsFTNRowStatus = _MplsFTNRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 2),
    _MplsFTNRowStatus_Type()
)
mplsFTNRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNRowStatus.setStatus("current")
_MplsFTNDescr_Type = SnmpAdminString
_MplsFTNDescr_Object = MibTableColumn
mplsFTNDescr = _MplsFTNDescr_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 3),
    _MplsFTNDescr_Type()
)
mplsFTNDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNDescr.setStatus("current")


class _MplsFTNMask_Type(Bits):
    """Custom type mplsFTNMask based on Bits"""
    namedValues = NamedValues(
        *(("destAddr", 1),
          ("destPort", 3),
          ("dscp", 5),
          ("protocol", 4),
          ("sourceAddr", 0),
          ("sourcePort", 2))
    )

_MplsFTNMask_Type.__name__ = "Bits"
_MplsFTNMask_Object = MibTableColumn
mplsFTNMask = _MplsFTNMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 4),
    _MplsFTNMask_Type()
)
mplsFTNMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNMask.setStatus("current")
_MplsFTNAddrType_Type = InetAddressType
_MplsFTNAddrType_Object = MibTableColumn
mplsFTNAddrType = _MplsFTNAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 5),
    _MplsFTNAddrType_Type()
)
mplsFTNAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNAddrType.setStatus("current")
_MplsFTNSourceAddrMin_Type = InetAddress
_MplsFTNSourceAddrMin_Object = MibTableColumn
mplsFTNSourceAddrMin = _MplsFTNSourceAddrMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 6),
    _MplsFTNSourceAddrMin_Type()
)
mplsFTNSourceAddrMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNSourceAddrMin.setStatus("current")
_MplsFTNSourceAddrMax_Type = InetAddress
_MplsFTNSourceAddrMax_Object = MibTableColumn
mplsFTNSourceAddrMax = _MplsFTNSourceAddrMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 7),
    _MplsFTNSourceAddrMax_Type()
)
mplsFTNSourceAddrMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNSourceAddrMax.setStatus("current")
_MplsFTNDestAddrMin_Type = InetAddress
_MplsFTNDestAddrMin_Object = MibTableColumn
mplsFTNDestAddrMin = _MplsFTNDestAddrMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 8),
    _MplsFTNDestAddrMin_Type()
)
mplsFTNDestAddrMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNDestAddrMin.setStatus("current")
_MplsFTNDestAddrMax_Type = InetAddress
_MplsFTNDestAddrMax_Object = MibTableColumn
mplsFTNDestAddrMax = _MplsFTNDestAddrMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 9),
    _MplsFTNDestAddrMax_Type()
)
mplsFTNDestAddrMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNDestAddrMax.setStatus("current")


class _MplsFTNSourcePortMin_Type(InetPortNumber):
    """Custom type mplsFTNSourcePortMin based on InetPortNumber"""
    defaultValue = 0


_MplsFTNSourcePortMin_Object = MibTableColumn
mplsFTNSourcePortMin = _MplsFTNSourcePortMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 10),
    _MplsFTNSourcePortMin_Type()
)
mplsFTNSourcePortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNSourcePortMin.setStatus("current")


class _MplsFTNSourcePortMax_Type(InetPortNumber):
    """Custom type mplsFTNSourcePortMax based on InetPortNumber"""
    defaultValue = 65535


_MplsFTNSourcePortMax_Object = MibTableColumn
mplsFTNSourcePortMax = _MplsFTNSourcePortMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 11),
    _MplsFTNSourcePortMax_Type()
)
mplsFTNSourcePortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNSourcePortMax.setStatus("current")


class _MplsFTNDestPortMin_Type(InetPortNumber):
    """Custom type mplsFTNDestPortMin based on InetPortNumber"""
    defaultValue = 0


_MplsFTNDestPortMin_Object = MibTableColumn
mplsFTNDestPortMin = _MplsFTNDestPortMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 12),
    _MplsFTNDestPortMin_Type()
)
mplsFTNDestPortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNDestPortMin.setStatus("current")


class _MplsFTNDestPortMax_Type(InetPortNumber):
    """Custom type mplsFTNDestPortMax based on InetPortNumber"""
    defaultValue = 65535


_MplsFTNDestPortMax_Object = MibTableColumn
mplsFTNDestPortMax = _MplsFTNDestPortMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 13),
    _MplsFTNDestPortMax_Type()
)
mplsFTNDestPortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNDestPortMax.setStatus("current")


class _MplsFTNProtocol_Type(Integer32):
    """Custom type mplsFTNProtocol based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsFTNProtocol_Type.__name__ = "Integer32"
_MplsFTNProtocol_Object = MibTableColumn
mplsFTNProtocol = _MplsFTNProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 14),
    _MplsFTNProtocol_Type()
)
mplsFTNProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNProtocol.setStatus("current")
_MplsFTNDscp_Type = Dscp
_MplsFTNDscp_Object = MibTableColumn
mplsFTNDscp = _MplsFTNDscp_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 15),
    _MplsFTNDscp_Type()
)
mplsFTNDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNDscp.setStatus("current")


class _MplsFTNActionType_Type(Integer32):
    """Custom type mplsFTNActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redirectLsp", 1),
          ("redirectTunnel", 2))
    )


_MplsFTNActionType_Type.__name__ = "Integer32"
_MplsFTNActionType_Object = MibTableColumn
mplsFTNActionType = _MplsFTNActionType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 16),
    _MplsFTNActionType_Type()
)
mplsFTNActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNActionType.setStatus("current")
_MplsFTNActionPointer_Type = RowPointer
_MplsFTNActionPointer_Object = MibTableColumn
mplsFTNActionPointer = _MplsFTNActionPointer_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 17),
    _MplsFTNActionPointer_Type()
)
mplsFTNActionPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNActionPointer.setStatus("current")


class _MplsFTNStorageType_Type(StorageType):
    """Custom type mplsFTNStorageType based on StorageType"""


_MplsFTNStorageType_Object = MibTableColumn
mplsFTNStorageType = _MplsFTNStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 18),
    _MplsFTNStorageType_Type()
)
mplsFTNStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNStorageType.setStatus("current")
_MplsFTNMapTableLastChanged_Type = TimeStamp
_MplsFTNMapTableLastChanged_Object = MibScalar
mplsFTNMapTableLastChanged = _MplsFTNMapTableLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 4),
    _MplsFTNMapTableLastChanged_Type()
)
mplsFTNMapTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFTNMapTableLastChanged.setStatus("current")
_MplsFTNMapTable_Object = MibTable
mplsFTNMapTable = _MplsFTNMapTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5)
)
if mibBuilder.loadTexts:
    mplsFTNMapTable.setStatus("current")
_MplsFTNMapEntry_Object = MibTableRow
mplsFTNMapEntry = _MplsFTNMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1)
)
mplsFTNMapEntry.setIndexNames(
    (0, "MPLS-FTN-STD-MIB", "mplsFTNMapIndex"),
    (0, "MPLS-FTN-STD-MIB", "mplsFTNMapPrevIndex"),
    (0, "MPLS-FTN-STD-MIB", "mplsFTNMapCurrIndex"),
)
if mibBuilder.loadTexts:
    mplsFTNMapEntry.setStatus("current")
_MplsFTNMapIndex_Type = InterfaceIndexOrZero
_MplsFTNMapIndex_Object = MibTableColumn
mplsFTNMapIndex = _MplsFTNMapIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 1),
    _MplsFTNMapIndex_Type()
)
mplsFTNMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFTNMapIndex.setStatus("current")
_MplsFTNMapPrevIndex_Type = MplsFTNEntryIndexOrZero
_MplsFTNMapPrevIndex_Object = MibTableColumn
mplsFTNMapPrevIndex = _MplsFTNMapPrevIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 2),
    _MplsFTNMapPrevIndex_Type()
)
mplsFTNMapPrevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFTNMapPrevIndex.setStatus("current")
_MplsFTNMapCurrIndex_Type = MplsFTNEntryIndex
_MplsFTNMapCurrIndex_Object = MibTableColumn
mplsFTNMapCurrIndex = _MplsFTNMapCurrIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 3),
    _MplsFTNMapCurrIndex_Type()
)
mplsFTNMapCurrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFTNMapCurrIndex.setStatus("current")


class _MplsFTNMapRowStatus_Type(RowStatus):
    """Custom type mplsFTNMapRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_MplsFTNMapRowStatus_Type.__name__ = "RowStatus"
_MplsFTNMapRowStatus_Object = MibTableColumn
mplsFTNMapRowStatus = _MplsFTNMapRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 4),
    _MplsFTNMapRowStatus_Type()
)
mplsFTNMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNMapRowStatus.setStatus("current")


class _MplsFTNMapStorageType_Type(StorageType):
    """Custom type mplsFTNMapStorageType based on StorageType"""


_MplsFTNMapStorageType_Object = MibTableColumn
mplsFTNMapStorageType = _MplsFTNMapStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 5),
    _MplsFTNMapStorageType_Type()
)
mplsFTNMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFTNMapStorageType.setStatus("current")
_MplsFTNPerfTable_Object = MibTable
mplsFTNPerfTable = _MplsFTNPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6)
)
if mibBuilder.loadTexts:
    mplsFTNPerfTable.setStatus("current")
_MplsFTNPerfEntry_Object = MibTableRow
mplsFTNPerfEntry = _MplsFTNPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1)
)
mplsFTNPerfEntry.setIndexNames(
    (0, "MPLS-FTN-STD-MIB", "mplsFTNPerfIndex"),
    (0, "MPLS-FTN-STD-MIB", "mplsFTNPerfCurrIndex"),
)
if mibBuilder.loadTexts:
    mplsFTNPerfEntry.setStatus("current")
_MplsFTNPerfIndex_Type = InterfaceIndexOrZero
_MplsFTNPerfIndex_Object = MibTableColumn
mplsFTNPerfIndex = _MplsFTNPerfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 1),
    _MplsFTNPerfIndex_Type()
)
mplsFTNPerfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFTNPerfIndex.setStatus("current")
_MplsFTNPerfCurrIndex_Type = MplsFTNEntryIndex
_MplsFTNPerfCurrIndex_Object = MibTableColumn
mplsFTNPerfCurrIndex = _MplsFTNPerfCurrIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 2),
    _MplsFTNPerfCurrIndex_Type()
)
mplsFTNPerfCurrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFTNPerfCurrIndex.setStatus("current")
_MplsFTNPerfMatchedPackets_Type = Counter64
_MplsFTNPerfMatchedPackets_Object = MibTableColumn
mplsFTNPerfMatchedPackets = _MplsFTNPerfMatchedPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 3),
    _MplsFTNPerfMatchedPackets_Type()
)
mplsFTNPerfMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFTNPerfMatchedPackets.setStatus("current")
_MplsFTNPerfMatchedOctets_Type = Counter64
_MplsFTNPerfMatchedOctets_Object = MibTableColumn
mplsFTNPerfMatchedOctets = _MplsFTNPerfMatchedOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 4),
    _MplsFTNPerfMatchedOctets_Type()
)
mplsFTNPerfMatchedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFTNPerfMatchedOctets.setStatus("current")
_MplsFTNPerfDiscontinuityTime_Type = TimeStamp
_MplsFTNPerfDiscontinuityTime_Object = MibTableColumn
mplsFTNPerfDiscontinuityTime = _MplsFTNPerfDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 5),
    _MplsFTNPerfDiscontinuityTime_Type()
)
mplsFTNPerfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFTNPerfDiscontinuityTime.setStatus("current")
_MplsFTNConformance_ObjectIdentity = ObjectIdentity
mplsFTNConformance = _MplsFTNConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 2)
)
_MplsFTNGroups_ObjectIdentity = ObjectIdentity
mplsFTNGroups = _MplsFTNGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 1)
)
_MplsFTNCompliances_ObjectIdentity = ObjectIdentity
mplsFTNCompliances = _MplsFTNCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 2)
)

# Managed Objects groups

mplsFTNRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 1, 1)
)
mplsFTNRuleGroup.setObjects(
      *(("MPLS-FTN-STD-MIB", "mplsFTNIndexNext"),
        ("MPLS-FTN-STD-MIB", "mplsFTNTableLastChanged"),
        ("MPLS-FTN-STD-MIB", "mplsFTNRowStatus"),
        ("MPLS-FTN-STD-MIB", "mplsFTNDescr"),
        ("MPLS-FTN-STD-MIB", "mplsFTNMask"),
        ("MPLS-FTN-STD-MIB", "mplsFTNAddrType"),
        ("MPLS-FTN-STD-MIB", "mplsFTNSourceAddrMin"),
        ("MPLS-FTN-STD-MIB", "mplsFTNSourceAddrMax"),
        ("MPLS-FTN-STD-MIB", "mplsFTNDestAddrMin"),
        ("MPLS-FTN-STD-MIB", "mplsFTNDestAddrMax"),
        ("MPLS-FTN-STD-MIB", "mplsFTNSourcePortMin"),
        ("MPLS-FTN-STD-MIB", "mplsFTNSourcePortMax"),
        ("MPLS-FTN-STD-MIB", "mplsFTNDestPortMin"),
        ("MPLS-FTN-STD-MIB", "mplsFTNDestPortMax"),
        ("MPLS-FTN-STD-MIB", "mplsFTNProtocol"),
        ("MPLS-FTN-STD-MIB", "mplsFTNActionType"),
        ("MPLS-FTN-STD-MIB", "mplsFTNActionPointer"),
        ("MPLS-FTN-STD-MIB", "mplsFTNDscp"),
        ("MPLS-FTN-STD-MIB", "mplsFTNStorageType"))
)
if mibBuilder.loadTexts:
    mplsFTNRuleGroup.setStatus("current")

mplsFTNMapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 1, 2)
)
mplsFTNMapGroup.setObjects(
      *(("MPLS-FTN-STD-MIB", "mplsFTNMapTableLastChanged"),
        ("MPLS-FTN-STD-MIB", "mplsFTNMapRowStatus"),
        ("MPLS-FTN-STD-MIB", "mplsFTNMapStorageType"))
)
if mibBuilder.loadTexts:
    mplsFTNMapGroup.setStatus("current")

mplsFTNPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 1, 3)
)
mplsFTNPerfGroup.setObjects(
      *(("MPLS-FTN-STD-MIB", "mplsFTNPerfMatchedPackets"),
        ("MPLS-FTN-STD-MIB", "mplsFTNPerfMatchedOctets"),
        ("MPLS-FTN-STD-MIB", "mplsFTNPerfDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    mplsFTNPerfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mplsFTNModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mplsFTNModuleFullCompliance.setStatus(
        "current"
    )

mplsFTNModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mplsFTNModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-FTN-STD-MIB",
    **{"MplsFTNEntryIndex": MplsFTNEntryIndex,
       "MplsFTNEntryIndexOrZero": MplsFTNEntryIndexOrZero,
       "mplsFTNStdMIB": mplsFTNStdMIB,
       "mplsFTNNotifications": mplsFTNNotifications,
       "mplsFTNObjects": mplsFTNObjects,
       "mplsFTNIndexNext": mplsFTNIndexNext,
       "mplsFTNTableLastChanged": mplsFTNTableLastChanged,
       "mplsFTNTable": mplsFTNTable,
       "mplsFTNEntry": mplsFTNEntry,
       "mplsFTNIndex": mplsFTNIndex,
       "mplsFTNRowStatus": mplsFTNRowStatus,
       "mplsFTNDescr": mplsFTNDescr,
       "mplsFTNMask": mplsFTNMask,
       "mplsFTNAddrType": mplsFTNAddrType,
       "mplsFTNSourceAddrMin": mplsFTNSourceAddrMin,
       "mplsFTNSourceAddrMax": mplsFTNSourceAddrMax,
       "mplsFTNDestAddrMin": mplsFTNDestAddrMin,
       "mplsFTNDestAddrMax": mplsFTNDestAddrMax,
       "mplsFTNSourcePortMin": mplsFTNSourcePortMin,
       "mplsFTNSourcePortMax": mplsFTNSourcePortMax,
       "mplsFTNDestPortMin": mplsFTNDestPortMin,
       "mplsFTNDestPortMax": mplsFTNDestPortMax,
       "mplsFTNProtocol": mplsFTNProtocol,
       "mplsFTNDscp": mplsFTNDscp,
       "mplsFTNActionType": mplsFTNActionType,
       "mplsFTNActionPointer": mplsFTNActionPointer,
       "mplsFTNStorageType": mplsFTNStorageType,
       "mplsFTNMapTableLastChanged": mplsFTNMapTableLastChanged,
       "mplsFTNMapTable": mplsFTNMapTable,
       "mplsFTNMapEntry": mplsFTNMapEntry,
       "mplsFTNMapIndex": mplsFTNMapIndex,
       "mplsFTNMapPrevIndex": mplsFTNMapPrevIndex,
       "mplsFTNMapCurrIndex": mplsFTNMapCurrIndex,
       "mplsFTNMapRowStatus": mplsFTNMapRowStatus,
       "mplsFTNMapStorageType": mplsFTNMapStorageType,
       "mplsFTNPerfTable": mplsFTNPerfTable,
       "mplsFTNPerfEntry": mplsFTNPerfEntry,
       "mplsFTNPerfIndex": mplsFTNPerfIndex,
       "mplsFTNPerfCurrIndex": mplsFTNPerfCurrIndex,
       "mplsFTNPerfMatchedPackets": mplsFTNPerfMatchedPackets,
       "mplsFTNPerfMatchedOctets": mplsFTNPerfMatchedOctets,
       "mplsFTNPerfDiscontinuityTime": mplsFTNPerfDiscontinuityTime,
       "mplsFTNConformance": mplsFTNConformance,
       "mplsFTNGroups": mplsFTNGroups,
       "mplsFTNRuleGroup": mplsFTNRuleGroup,
       "mplsFTNMapGroup": mplsFTNMapGroup,
       "mplsFTNPerfGroup": mplsFTNPerfGroup,
       "mplsFTNCompliances": mplsFTNCompliances,
       "mplsFTNModuleFullCompliance": mplsFTNModuleFullCompliance,
       "mplsFTNModuleReadOnlyCompliance": mplsFTNModuleReadOnlyCompliance}
)
