# SNMP MIB module (EQLAPPLIANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLAPPLIANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:00 2024
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

(UTFString,
 eqlGroupId) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "UTFString",
    "eqlGroupId")

(eqlMemberIndex,) = mibBuilder.importSymbols(
    "EQLMEMBER-MIB",
    "eqlMemberIndex")

(eqliscsiVolumeEntry,
 eqliscsiVolumeTargetIscsiName) = mibBuilder.importSymbols(
    "EQLVOLUME-MIB",
    "eqliscsiVolumeEntry",
    "eqliscsiVolumeTargetIscsiName")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eqlApplianceModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 17)
)
eqlApplianceModule.setRevisions(
        ("2013-02-21 08:00",
         "2012-03-05 10:00",
         "2009-07-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EqlApplianceObjects_ObjectIdentity = ObjectIdentity
eqlApplianceObjects = _EqlApplianceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1)
)
_EqlApplianceTable_Object = MibTable
eqlApplianceTable = _EqlApplianceTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1)
)
if mibBuilder.loadTexts:
    eqlApplianceTable.setStatus("current")
_EqlApplianceEntry_Object = MibTableRow
eqlApplianceEntry = _EqlApplianceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1)
)
eqlApplianceEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceEntry.setStatus("current")
_EqlApplianceIndex_Type = Unsigned32
_EqlApplianceIndex_Object = MibTableColumn
eqlApplianceIndex = _EqlApplianceIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 1),
    _EqlApplianceIndex_Type()
)
eqlApplianceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceIndex.setStatus("current")
_EqlApplianceRowStatus_Type = RowStatus
_EqlApplianceRowStatus_Object = MibTableColumn
eqlApplianceRowStatus = _EqlApplianceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 2),
    _EqlApplianceRowStatus_Type()
)
eqlApplianceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceRowStatus.setStatus("current")


class _EqlApplianceName_Type(OctetString):
    """Custom type eqlApplianceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceName_Type.__name__ = "OctetString"
_EqlApplianceName_Object = MibTableColumn
eqlApplianceName = _EqlApplianceName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 3),
    _EqlApplianceName_Type()
)
eqlApplianceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceName.setStatus("current")


class _EqlApplianceType_Type(Integer32):
    """Custom type eqlApplianceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blade-chassis", 2),
          ("nas", 1))
    )


_EqlApplianceType_Type.__name__ = "Integer32"
_EqlApplianceType_Object = MibTableColumn
eqlApplianceType = _EqlApplianceType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 4),
    _EqlApplianceType_Type()
)
eqlApplianceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceType.setStatus("current")


class _EqlApplianceState_Type(Integer32):
    """Custom type eqlApplianceState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1000,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
              1009,
              1010,
              1011,
              1012,
              1013,
              1014,
              1015,
              1016,
              1017,
              1018)
        )
    )
    namedValues = NamedValues(
        *(("client-network", 1003),
          ("cluster-name", 1015),
          ("configure-gateway", 1004),
          ("configured", 1014),
          ("create-volume-acls", 1009),
          ("format-in-progress", 1011),
          ("internal-network", 1001),
          ("make-cluster", 1007),
          ("nas-appliance-create-in-progress", 1017),
          ("node-setup", 1000),
          ("nodes-validation-inprogress", 1006),
          ("san-network", 1002),
          ("send-eql-group-ip", 1008),
          ("start-format", 1010),
          ("start-nas-appliance-create", 1016),
          ("start-nodes-validation", 1005),
          ("start-system", 1012),
          ("start-system-in-progress", 1013),
          ("start-volume-discovery", 1018),
          ("unconfigured", 0))
    )


_EqlApplianceState_Type.__name__ = "Integer32"
_EqlApplianceState_Object = MibTableColumn
eqlApplianceState = _EqlApplianceState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 5),
    _EqlApplianceState_Type()
)
eqlApplianceState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceState.setStatus("current")
_EqlApplianceDescription_Type = DisplayString
_EqlApplianceDescription_Object = MibTableColumn
eqlApplianceDescription = _EqlApplianceDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 6),
    _EqlApplianceDescription_Type()
)
eqlApplianceDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceDescription.setStatus("current")
_EqlApplianceMgmtAddressType_Type = InetAddressType
_EqlApplianceMgmtAddressType_Object = MibTableColumn
eqlApplianceMgmtAddressType = _EqlApplianceMgmtAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 7),
    _EqlApplianceMgmtAddressType_Type()
)
eqlApplianceMgmtAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMgmtAddressType.setStatus("current")
_EqlApplianceMgmtAddress_Type = InetAddress
_EqlApplianceMgmtAddress_Object = MibTableColumn
eqlApplianceMgmtAddress = _EqlApplianceMgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 8),
    _EqlApplianceMgmtAddress_Type()
)
eqlApplianceMgmtAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMgmtAddress.setStatus("current")


class _EqlApplianceMgmtPort_Type(Unsigned32):
    """Custom type eqlApplianceMgmtPort based on Unsigned32"""
    defaultValue = 3004


_EqlApplianceMgmtPort_Object = MibTableColumn
eqlApplianceMgmtPort = _EqlApplianceMgmtPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 9),
    _EqlApplianceMgmtPort_Type()
)
eqlApplianceMgmtPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMgmtPort.setStatus("current")
_EqlApplianceMajorVersion_Type = Unsigned32
_EqlApplianceMajorVersion_Object = MibTableColumn
eqlApplianceMajorVersion = _EqlApplianceMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 10),
    _EqlApplianceMajorVersion_Type()
)
eqlApplianceMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceMajorVersion.setStatus("current")
_EqlApplianceMinorVersion_Type = Unsigned32
_EqlApplianceMinorVersion_Object = MibTableColumn
eqlApplianceMinorVersion = _EqlApplianceMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 11),
    _EqlApplianceMinorVersion_Type()
)
eqlApplianceMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceMinorVersion.setStatus("current")
_EqlApplianceMaintVersion_Type = Unsigned32
_EqlApplianceMaintVersion_Object = MibTableColumn
eqlApplianceMaintVersion = _EqlApplianceMaintVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 12),
    _EqlApplianceMaintVersion_Type()
)
eqlApplianceMaintVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceMaintVersion.setStatus("current")


class _EqlApplianceVendorId_Type(OctetString):
    """Custom type eqlApplianceVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlApplianceVendorId_Type.__name__ = "OctetString"
_EqlApplianceVendorId_Object = MibTableColumn
eqlApplianceVendorId = _EqlApplianceVendorId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 13),
    _EqlApplianceVendorId_Type()
)
eqlApplianceVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceVendorId.setStatus("current")


class _EqlApplianceSharedSecret_Type(OctetString):
    """Custom type eqlApplianceSharedSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlApplianceSharedSecret_Type.__name__ = "OctetString"
_EqlApplianceSharedSecret_Object = MibTableColumn
eqlApplianceSharedSecret = _EqlApplianceSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 14),
    _EqlApplianceSharedSecret_Type()
)
eqlApplianceSharedSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceSharedSecret.setStatus("current")


class _EqlApplianceUserName_Type(UTFString):
    """Custom type eqlApplianceUserName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlApplianceUserName_Type.__name__ = "UTFString"
_EqlApplianceUserName_Object = MibTableColumn
eqlApplianceUserName = _EqlApplianceUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 15),
    _EqlApplianceUserName_Type()
)
eqlApplianceUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUserName.setStatus("current")
_EqlApplianceNumberOfNodes_Type = Unsigned32
_EqlApplianceNumberOfNodes_Object = MibTableColumn
eqlApplianceNumberOfNodes = _EqlApplianceNumberOfNodes_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 16),
    _EqlApplianceNumberOfNodes_Type()
)
eqlApplianceNumberOfNodes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNumberOfNodes.setStatus("current")
_EqlApplianceUniqueID_Type = Unsigned32
_EqlApplianceUniqueID_Object = MibTableColumn
eqlApplianceUniqueID = _EqlApplianceUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 17),
    _EqlApplianceUniqueID_Type()
)
eqlApplianceUniqueID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUniqueID.setStatus("current")
_EqlApplianceConfigStatus_Type = Unsigned32
_EqlApplianceConfigStatus_Object = MibTableColumn
eqlApplianceConfigStatus = _EqlApplianceConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 18),
    _EqlApplianceConfigStatus_Type()
)
eqlApplianceConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceConfigStatus.setStatus("current")


class _EqlApplianceAction_Type(Integer32):
    """Custom type eqlApplianceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("abort", 3),
          ("continue", 4),
          ("none", 0),
          ("retry", 2),
          ("start", 1))
    )


_EqlApplianceAction_Type.__name__ = "Integer32"
_EqlApplianceAction_Object = MibTableColumn
eqlApplianceAction = _EqlApplianceAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 19),
    _EqlApplianceAction_Type()
)
eqlApplianceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAction.setStatus("current")


class _EqlApplianceAdminStatus_Type(Integer32):
    """Custom type eqlApplianceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("down", 0),
          ("maintenance", 2),
          ("up", 1))
    )


_EqlApplianceAdminStatus_Type.__name__ = "Integer32"
_EqlApplianceAdminStatus_Object = MibTableColumn
eqlApplianceAdminStatus = _EqlApplianceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 20),
    _EqlApplianceAdminStatus_Type()
)
eqlApplianceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAdminStatus.setStatus("current")
_EqlApplianceGatewayAddrType_Type = InetAddressType
_EqlApplianceGatewayAddrType_Object = MibTableColumn
eqlApplianceGatewayAddrType = _EqlApplianceGatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 21),
    _EqlApplianceGatewayAddrType_Type()
)
eqlApplianceGatewayAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceGatewayAddrType.setStatus("current")
_EqlApplianceGatewayAddr_Type = InetAddress
_EqlApplianceGatewayAddr_Object = MibTableColumn
eqlApplianceGatewayAddr = _EqlApplianceGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 22),
    _EqlApplianceGatewayAddr_Type()
)
eqlApplianceGatewayAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceGatewayAddr.setStatus("current")


class _EqlApplianceLastScheduleIndex_Type(Unsigned32):
    """Custom type eqlApplianceLastScheduleIndex based on Unsigned32"""
    defaultValue = 0


_EqlApplianceLastScheduleIndex_Object = MibTableColumn
eqlApplianceLastScheduleIndex = _EqlApplianceLastScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 23),
    _EqlApplianceLastScheduleIndex_Type()
)
eqlApplianceLastScheduleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLastScheduleIndex.setStatus("current")


class _EqlApplianceMPV_Type(Unsigned32):
    """Custom type eqlApplianceMPV based on Unsigned32"""
    defaultValue = 0


_EqlApplianceMPV_Object = MibTableColumn
eqlApplianceMPV = _EqlApplianceMPV_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 24),
    _EqlApplianceMPV_Type()
)
eqlApplianceMPV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMPV.setStatus("current")


class _EqlApplianceEnableFTP_Type(Integer32):
    """Custom type eqlApplianceEnableFTP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_EqlApplianceEnableFTP_Type.__name__ = "Integer32"
_EqlApplianceEnableFTP_Object = MibTableColumn
eqlApplianceEnableFTP = _EqlApplianceEnableFTP_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 25),
    _EqlApplianceEnableFTP_Type()
)
eqlApplianceEnableFTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlApplianceEnableFTP.setStatus("current")


class _EqlApplianceDesiredServiceMode_Type(Integer32):
    """Custom type eqlApplianceDesiredServiceMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("maintenance", 1),
          ("normal", 0))
    )


_EqlApplianceDesiredServiceMode_Type.__name__ = "Integer32"
_EqlApplianceDesiredServiceMode_Object = MibTableColumn
eqlApplianceDesiredServiceMode = _EqlApplianceDesiredServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 26),
    _EqlApplianceDesiredServiceMode_Type()
)
eqlApplianceDesiredServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlApplianceDesiredServiceMode.setStatus("current")


class _EqlApplianceServiceModeStatus_Type(Integer32):
    """Custom type eqlApplianceServiceModeStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("maintenance", 1),
          ("normal", 0),
          ("transition-to-maint", 2),
          ("transition-to-normal", 3))
    )


_EqlApplianceServiceModeStatus_Type.__name__ = "Integer32"
_EqlApplianceServiceModeStatus_Object = MibTableColumn
eqlApplianceServiceModeStatus = _EqlApplianceServiceModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 27),
    _EqlApplianceServiceModeStatus_Type()
)
eqlApplianceServiceModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceServiceModeStatus.setStatus("current")
_EqlApplianceRequestId_Type = Counter64
_EqlApplianceRequestId_Object = MibTableColumn
eqlApplianceRequestId = _EqlApplianceRequestId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 1, 1, 28),
    _EqlApplianceRequestId_Type()
)
eqlApplianceRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceRequestId.setStatus("current")
_EqlApplianceUniqueIDTable_Object = MibTable
eqlApplianceUniqueIDTable = _EqlApplianceUniqueIDTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 2)
)
if mibBuilder.loadTexts:
    eqlApplianceUniqueIDTable.setStatus("current")
_EqlApplianceUniqueIDEntry_Object = MibTableRow
eqlApplianceUniqueIDEntry = _EqlApplianceUniqueIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 2, 1)
)
eqlApplianceUniqueIDEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceUniqueIDType"),
)
if mibBuilder.loadTexts:
    eqlApplianceUniqueIDEntry.setStatus("current")


class _EqlApplianceUniqueIDType_Type(Integer32):
    """Custom type eqlApplianceUniqueIDType based on Integer32"""
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
        *(("fsid", 1),
          ("nfsexportname", 3),
          ("partnershipid", 4),
          ("replicationid", 5),
          ("userid", 2))
    )


_EqlApplianceUniqueIDType_Type.__name__ = "Integer32"
_EqlApplianceUniqueIDType_Object = MibTableColumn
eqlApplianceUniqueIDType = _EqlApplianceUniqueIDType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 2, 1, 1),
    _EqlApplianceUniqueIDType_Type()
)
eqlApplianceUniqueIDType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceUniqueIDType.setStatus("current")
_EqlApplianceUniqueIDValueLen_Type = Unsigned32
_EqlApplianceUniqueIDValueLen_Object = MibTableColumn
eqlApplianceUniqueIDValueLen = _EqlApplianceUniqueIDValueLen_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 2, 1, 2),
    _EqlApplianceUniqueIDValueLen_Type()
)
eqlApplianceUniqueIDValueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUniqueIDValueLen.setStatus("current")


class _EqlApplianceUniqueIDValue_Type(OctetString):
    """Custom type eqlApplianceUniqueIDValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_EqlApplianceUniqueIDValue_Type.__name__ = "OctetString"
_EqlApplianceUniqueIDValue_Object = MibTableColumn
eqlApplianceUniqueIDValue = _EqlApplianceUniqueIDValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 2, 1, 3),
    _EqlApplianceUniqueIDValue_Type()
)
eqlApplianceUniqueIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUniqueIDValue.setStatus("current")
_EqlApplianceUnInitNodesTable_Object = MibTable
eqlApplianceUnInitNodesTable = _EqlApplianceUnInitNodesTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3)
)
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodesTable.setStatus("current")
_EqlApplianceUnInitNodesEntry_Object = MibTableRow
eqlApplianceUnInitNodesEntry = _EqlApplianceUnInitNodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1)
)
eqlApplianceUnInitNodesEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceUnInitNodeProductType"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceUnInitNodeServiceTag"),
)
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodesEntry.setStatus("current")


class _EqlApplianceUnInitNodeProductType_Type(Integer32):
    """Custom type eqlApplianceUnInitNodeProductType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("nas", 1)
    )


_EqlApplianceUnInitNodeProductType_Type.__name__ = "Integer32"
_EqlApplianceUnInitNodeProductType_Object = MibTableColumn
eqlApplianceUnInitNodeProductType = _EqlApplianceUnInitNodeProductType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1, 1),
    _EqlApplianceUnInitNodeProductType_Type()
)
eqlApplianceUnInitNodeProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodeProductType.setStatus("current")


class _EqlApplianceUnInitNodeServiceTag_Type(OctetString):
    """Custom type eqlApplianceUnInitNodeServiceTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EqlApplianceUnInitNodeServiceTag_Type.__name__ = "OctetString"
_EqlApplianceUnInitNodeServiceTag_Object = MibTableColumn
eqlApplianceUnInitNodeServiceTag = _EqlApplianceUnInitNodeServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1, 2),
    _EqlApplianceUnInitNodeServiceTag_Type()
)
eqlApplianceUnInitNodeServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodeServiceTag.setStatus("current")


class _EqlApplianceUnInitNodeState_Type(Integer32):
    """Custom type eqlApplianceUnInitNodeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discover", 1),
          ("found", 2))
    )


_EqlApplianceUnInitNodeState_Type.__name__ = "Integer32"
_EqlApplianceUnInitNodeState_Object = MibTableColumn
eqlApplianceUnInitNodeState = _EqlApplianceUnInitNodeState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1, 3),
    _EqlApplianceUnInitNodeState_Type()
)
eqlApplianceUnInitNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodeState.setStatus("current")


class _EqlApplianceUnInitNodeModel_Type(OctetString):
    """Custom type eqlApplianceUnInitNodeModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceUnInitNodeModel_Type.__name__ = "OctetString"
_EqlApplianceUnInitNodeModel_Object = MibTableColumn
eqlApplianceUnInitNodeModel = _EqlApplianceUnInitNodeModel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1, 4),
    _EqlApplianceUnInitNodeModel_Type()
)
eqlApplianceUnInitNodeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodeModel.setStatus("current")


class _EqlApplianceUnInitNodeVendor_Type(OctetString):
    """Custom type eqlApplianceUnInitNodeVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceUnInitNodeVendor_Type.__name__ = "OctetString"
_EqlApplianceUnInitNodeVendor_Object = MibTableColumn
eqlApplianceUnInitNodeVendor = _EqlApplianceUnInitNodeVendor_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1, 5),
    _EqlApplianceUnInitNodeVendor_Type()
)
eqlApplianceUnInitNodeVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodeVendor.setStatus("current")
_EqlApplianceUnInitNodeLinkLocalIPType_Type = InetAddressType
_EqlApplianceUnInitNodeLinkLocalIPType_Object = MibTableColumn
eqlApplianceUnInitNodeLinkLocalIPType = _EqlApplianceUnInitNodeLinkLocalIPType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1, 6),
    _EqlApplianceUnInitNodeLinkLocalIPType_Type()
)
eqlApplianceUnInitNodeLinkLocalIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodeLinkLocalIPType.setStatus("current")
_EqlApplianceUnInitNodeLinkLocalIP_Type = InetAddress
_EqlApplianceUnInitNodeLinkLocalIP_Object = MibTableColumn
eqlApplianceUnInitNodeLinkLocalIP = _EqlApplianceUnInitNodeLinkLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1, 7),
    _EqlApplianceUnInitNodeLinkLocalIP_Type()
)
eqlApplianceUnInitNodeLinkLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodeLinkLocalIP.setStatus("current")
_EqlApplianceUnInitNodeMajorVersion_Type = Unsigned32
_EqlApplianceUnInitNodeMajorVersion_Object = MibTableColumn
eqlApplianceUnInitNodeMajorVersion = _EqlApplianceUnInitNodeMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1, 8),
    _EqlApplianceUnInitNodeMajorVersion_Type()
)
eqlApplianceUnInitNodeMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodeMajorVersion.setStatus("current")
_EqlApplianceUnInitNodeMinorVersion_Type = Unsigned32
_EqlApplianceUnInitNodeMinorVersion_Object = MibTableColumn
eqlApplianceUnInitNodeMinorVersion = _EqlApplianceUnInitNodeMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1, 9),
    _EqlApplianceUnInitNodeMinorVersion_Type()
)
eqlApplianceUnInitNodeMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodeMinorVersion.setStatus("current")
_EqlApplianceUnInitNodeMaintVersion_Type = Unsigned32
_EqlApplianceUnInitNodeMaintVersion_Object = MibTableColumn
eqlApplianceUnInitNodeMaintVersion = _EqlApplianceUnInitNodeMaintVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1, 10),
    _EqlApplianceUnInitNodeMaintVersion_Type()
)
eqlApplianceUnInitNodeMaintVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodeMaintVersion.setStatus("current")
_EqlApplianceUnInitNodeRowStatus_Type = RowStatus
_EqlApplianceUnInitNodeRowStatus_Object = MibTableColumn
eqlApplianceUnInitNodeRowStatus = _EqlApplianceUnInitNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1, 11),
    _EqlApplianceUnInitNodeRowStatus_Type()
)
eqlApplianceUnInitNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodeRowStatus.setStatus("current")
_EqlApplianceUnInitNodeClusterMPV_Type = Unsigned32
_EqlApplianceUnInitNodeClusterMPV_Object = MibTableColumn
eqlApplianceUnInitNodeClusterMPV = _EqlApplianceUnInitNodeClusterMPV_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1, 12),
    _EqlApplianceUnInitNodeClusterMPV_Type()
)
eqlApplianceUnInitNodeClusterMPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodeClusterMPV.setStatus("current")


class _EqlApplianceUnInitNodeChassisTag_Type(OctetString):
    """Custom type eqlApplianceUnInitNodeChassisTag based on OctetString"""
    defaultValue = OctetString("-")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EqlApplianceUnInitNodeChassisTag_Type.__name__ = "OctetString"
_EqlApplianceUnInitNodeChassisTag_Object = MibTableColumn
eqlApplianceUnInitNodeChassisTag = _EqlApplianceUnInitNodeChassisTag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 3, 1, 13),
    _EqlApplianceUnInitNodeChassisTag_Type()
)
eqlApplianceUnInitNodeChassisTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceUnInitNodeChassisTag.setStatus("current")
_EqlApplianceNodeTable_Object = MibTable
eqlApplianceNodeTable = _EqlApplianceNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4)
)
if mibBuilder.loadTexts:
    eqlApplianceNodeTable.setStatus("current")
_EqlApplianceNodeEntry_Object = MibTableRow
eqlApplianceNodeEntry = _EqlApplianceNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1)
)
eqlApplianceNodeEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNodeIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceNodeEntry.setStatus("current")
_EqlApplianceNodeIndex_Type = Unsigned32
_EqlApplianceNodeIndex_Object = MibTableColumn
eqlApplianceNodeIndex = _EqlApplianceNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 1),
    _EqlApplianceNodeIndex_Type()
)
eqlApplianceNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceNodeIndex.setStatus("current")
_EqlApplianceNodeRowStatus_Type = RowStatus
_EqlApplianceNodeRowStatus_Object = MibTableColumn
eqlApplianceNodeRowStatus = _EqlApplianceNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 2),
    _EqlApplianceNodeRowStatus_Type()
)
eqlApplianceNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNodeRowStatus.setStatus("current")


class _EqlApplianceNodeProductType_Type(Integer32):
    """Custom type eqlApplianceNodeProductType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fs7500", 1),
          ("fs7600", 2),
          ("fs7610", 3))
    )


_EqlApplianceNodeProductType_Type.__name__ = "Integer32"
_EqlApplianceNodeProductType_Object = MibTableColumn
eqlApplianceNodeProductType = _EqlApplianceNodeProductType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 3),
    _EqlApplianceNodeProductType_Type()
)
eqlApplianceNodeProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeProductType.setStatus("current")


class _EqlApplianceNodeServiceTag_Type(OctetString):
    """Custom type eqlApplianceNodeServiceTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EqlApplianceNodeServiceTag_Type.__name__ = "OctetString"
_EqlApplianceNodeServiceTag_Object = MibTableColumn
eqlApplianceNodeServiceTag = _EqlApplianceNodeServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 4),
    _EqlApplianceNodeServiceTag_Type()
)
eqlApplianceNodeServiceTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNodeServiceTag.setStatus("current")


class _EqlApplianceNodeModel_Type(OctetString):
    """Custom type eqlApplianceNodeModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceNodeModel_Type.__name__ = "OctetString"
_EqlApplianceNodeModel_Object = MibTableColumn
eqlApplianceNodeModel = _EqlApplianceNodeModel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 5),
    _EqlApplianceNodeModel_Type()
)
eqlApplianceNodeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeModel.setStatus("current")


class _EqlApplianceNodeVendor_Type(OctetString):
    """Custom type eqlApplianceNodeVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceNodeVendor_Type.__name__ = "OctetString"
_EqlApplianceNodeVendor_Object = MibTableColumn
eqlApplianceNodeVendor = _EqlApplianceNodeVendor_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 6),
    _EqlApplianceNodeVendor_Type()
)
eqlApplianceNodeVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeVendor.setStatus("current")
_EqlApplianceNodeLinkLocalIPType_Type = InetAddressType
_EqlApplianceNodeLinkLocalIPType_Object = MibTableColumn
eqlApplianceNodeLinkLocalIPType = _EqlApplianceNodeLinkLocalIPType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 7),
    _EqlApplianceNodeLinkLocalIPType_Type()
)
eqlApplianceNodeLinkLocalIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeLinkLocalIPType.setStatus("current")
_EqlApplianceNodeLinkLocalIP_Type = InetAddress
_EqlApplianceNodeLinkLocalIP_Object = MibTableColumn
eqlApplianceNodeLinkLocalIP = _EqlApplianceNodeLinkLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 8),
    _EqlApplianceNodeLinkLocalIP_Type()
)
eqlApplianceNodeLinkLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeLinkLocalIP.setStatus("current")
_EqlApplianceNodeMajorVersion_Type = Unsigned32
_EqlApplianceNodeMajorVersion_Object = MibTableColumn
eqlApplianceNodeMajorVersion = _EqlApplianceNodeMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 9),
    _EqlApplianceNodeMajorVersion_Type()
)
eqlApplianceNodeMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeMajorVersion.setStatus("current")
_EqlApplianceNodeMinorVersion_Type = Unsigned32
_EqlApplianceNodeMinorVersion_Object = MibTableColumn
eqlApplianceNodeMinorVersion = _EqlApplianceNodeMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 10),
    _EqlApplianceNodeMinorVersion_Type()
)
eqlApplianceNodeMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeMinorVersion.setStatus("current")
_EqlApplianceNodeMaintVersion_Type = Unsigned32
_EqlApplianceNodeMaintVersion_Object = MibTableColumn
eqlApplianceNodeMaintVersion = _EqlApplianceNodeMaintVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 11),
    _EqlApplianceNodeMaintVersion_Type()
)
eqlApplianceNodeMaintVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeMaintVersion.setStatus("current")


class _EqlApplianceNodeName_Type(DisplayString):
    """Custom type eqlApplianceNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceNodeName_Type.__name__ = "DisplayString"
_EqlApplianceNodeName_Object = MibTableColumn
eqlApplianceNodeName = _EqlApplianceNodeName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 12),
    _EqlApplianceNodeName_Type()
)
eqlApplianceNodeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNodeName.setStatus("current")
_EqlApplianceNodePeerIndex_Type = Unsigned32
_EqlApplianceNodePeerIndex_Object = MibTableColumn
eqlApplianceNodePeerIndex = _EqlApplianceNodePeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 13),
    _EqlApplianceNodePeerIndex_Type()
)
eqlApplianceNodePeerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNodePeerIndex.setStatus("current")


class _EqlApplianceNodeConfigState_Type(Integer32):
    """Custom type eqlApplianceNodeConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007)
        )
    )
    namedValues = NamedValues(
        *(("client-network-complete", 1004),
          ("configured", 1006),
          ("detached", 1007),
          ("gateway-config-complete", 1005),
          ("internal-network-complete", 1002),
          ("node-setup-complete", 1001),
          ("san-network-complete", 1003),
          ("unconfigured", 0))
    )


_EqlApplianceNodeConfigState_Type.__name__ = "Integer32"
_EqlApplianceNodeConfigState_Object = MibTableColumn
eqlApplianceNodeConfigState = _EqlApplianceNodeConfigState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 14),
    _EqlApplianceNodeConfigState_Type()
)
eqlApplianceNodeConfigState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNodeConfigState.setStatus("current")
_EqlApplianceNodeConfigStatus_Type = Unsigned32
_EqlApplianceNodeConfigStatus_Object = MibTableColumn
eqlApplianceNodeConfigStatus = _EqlApplianceNodeConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 15),
    _EqlApplianceNodeConfigStatus_Type()
)
eqlApplianceNodeConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNodeConfigStatus.setStatus("current")
_EqlApplianceNodeGatewayAddrType_Type = InetAddressType
_EqlApplianceNodeGatewayAddrType_Object = MibTableColumn
eqlApplianceNodeGatewayAddrType = _EqlApplianceNodeGatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 16),
    _EqlApplianceNodeGatewayAddrType_Type()
)
eqlApplianceNodeGatewayAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNodeGatewayAddrType.setStatus("current")
_EqlApplianceNodeGatewayAddr_Type = InetAddress
_EqlApplianceNodeGatewayAddr_Object = MibTableColumn
eqlApplianceNodeGatewayAddr = _EqlApplianceNodeGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 17),
    _EqlApplianceNodeGatewayAddr_Type()
)
eqlApplianceNodeGatewayAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNodeGatewayAddr.setStatus("current")


class _EqlApplianceNodeInitiatorName_Type(OctetString):
    """Custom type eqlApplianceNodeInitiatorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqlApplianceNodeInitiatorName_Type.__name__ = "OctetString"
_EqlApplianceNodeInitiatorName_Object = MibTableColumn
eqlApplianceNodeInitiatorName = _EqlApplianceNodeInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 18),
    _EqlApplianceNodeInitiatorName_Type()
)
eqlApplianceNodeInitiatorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNodeInitiatorName.setStatus("current")


class _EqlApplianceNodeAdminStatus_Type(Integer32):
    """Custom type eqlApplianceNodeAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("attach", 2),
          ("detach", 1),
          ("on", 0),
          ("reset", 3))
    )


_EqlApplianceNodeAdminStatus_Type.__name__ = "Integer32"
_EqlApplianceNodeAdminStatus_Object = MibTableColumn
eqlApplianceNodeAdminStatus = _EqlApplianceNodeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 19),
    _EqlApplianceNodeAdminStatus_Type()
)
eqlApplianceNodeAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNodeAdminStatus.setStatus("current")


class _EqlApplianceNodeChassisTag_Type(OctetString):
    """Custom type eqlApplianceNodeChassisTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EqlApplianceNodeChassisTag_Type.__name__ = "OctetString"
_EqlApplianceNodeChassisTag_Object = MibTableColumn
eqlApplianceNodeChassisTag = _EqlApplianceNodeChassisTag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 20),
    _EqlApplianceNodeChassisTag_Type()
)
eqlApplianceNodeChassisTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNodeChassisTag.setStatus("current")


class _EqlApplianceNodeChassisName_Type(OctetString):
    """Custom type eqlApplianceNodeChassisName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EqlApplianceNodeChassisName_Type.__name__ = "OctetString"
_EqlApplianceNodeChassisName_Object = MibTableColumn
eqlApplianceNodeChassisName = _EqlApplianceNodeChassisName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 21),
    _EqlApplianceNodeChassisName_Type()
)
eqlApplianceNodeChassisName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNodeChassisName.setStatus("current")
_EqlApplianceNodeOpsRequestId_Type = Counter64
_EqlApplianceNodeOpsRequestId_Object = MibTableColumn
eqlApplianceNodeOpsRequestId = _EqlApplianceNodeOpsRequestId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 4, 1, 22),
    _EqlApplianceNodeOpsRequestId_Type()
)
eqlApplianceNodeOpsRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeOpsRequestId.setStatus("current")
_EqlApplianceNetworksTable_Object = MibTable
eqlApplianceNetworksTable = _EqlApplianceNetworksTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5)
)
if mibBuilder.loadTexts:
    eqlApplianceNetworksTable.setStatus("current")
_EqlApplianceNetworksEntry_Object = MibTableRow
eqlApplianceNetworksEntry = _EqlApplianceNetworksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5, 1)
)
eqlApplianceNetworksEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNetworkType"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNetworkID"),
)
if mibBuilder.loadTexts:
    eqlApplianceNetworksEntry.setStatus("current")
_EqlApplianceNetworkRowStatus_Type = RowStatus
_EqlApplianceNetworkRowStatus_Object = MibTableColumn
eqlApplianceNetworkRowStatus = _EqlApplianceNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5, 1, 1),
    _EqlApplianceNetworkRowStatus_Type()
)
eqlApplianceNetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNetworkRowStatus.setStatus("current")


class _EqlApplianceNetworkType_Type(Integer32):
    """Custom type eqlApplianceNetworkType based on Integer32"""
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
        *(("backplane", 4),
          ("client", 3),
          ("internal", 1),
          ("san", 2))
    )


_EqlApplianceNetworkType_Type.__name__ = "Integer32"
_EqlApplianceNetworkType_Object = MibTableColumn
eqlApplianceNetworkType = _EqlApplianceNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5, 1, 2),
    _EqlApplianceNetworkType_Type()
)
eqlApplianceNetworkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceNetworkType.setStatus("current")
_EqlApplianceNetworkID_Type = Unsigned32
_EqlApplianceNetworkID_Object = MibTableColumn
eqlApplianceNetworkID = _EqlApplianceNetworkID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5, 1, 3),
    _EqlApplianceNetworkID_Type()
)
eqlApplianceNetworkID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceNetworkID.setStatus("current")


class _EqlApplianceNetworkName_Type(OctetString):
    """Custom type eqlApplianceNetworkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceNetworkName_Type.__name__ = "OctetString"
_EqlApplianceNetworkName_Object = MibTableColumn
eqlApplianceNetworkName = _EqlApplianceNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5, 1, 4),
    _EqlApplianceNetworkName_Type()
)
eqlApplianceNetworkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNetworkName.setStatus("current")
_EqlApplianceNetworkBlockIPAddressType_Type = InetAddressType
_EqlApplianceNetworkBlockIPAddressType_Object = MibTableColumn
eqlApplianceNetworkBlockIPAddressType = _EqlApplianceNetworkBlockIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5, 1, 5),
    _EqlApplianceNetworkBlockIPAddressType_Type()
)
eqlApplianceNetworkBlockIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNetworkBlockIPAddressType.setStatus("current")
_EqlApplianceNetworkBlockIPAddress_Type = InetAddress
_EqlApplianceNetworkBlockIPAddress_Object = MibTableColumn
eqlApplianceNetworkBlockIPAddress = _EqlApplianceNetworkBlockIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5, 1, 6),
    _EqlApplianceNetworkBlockIPAddress_Type()
)
eqlApplianceNetworkBlockIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNetworkBlockIPAddress.setStatus("current")
_EqlApplianceNetworkBlockNetmaskAddrType_Type = InetAddressType
_EqlApplianceNetworkBlockNetmaskAddrType_Object = MibTableColumn
eqlApplianceNetworkBlockNetmaskAddrType = _EqlApplianceNetworkBlockNetmaskAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5, 1, 7),
    _EqlApplianceNetworkBlockNetmaskAddrType_Type()
)
eqlApplianceNetworkBlockNetmaskAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNetworkBlockNetmaskAddrType.setStatus("current")
_EqlApplianceNetworkBlockNetmaskAddr_Type = InetAddress
_EqlApplianceNetworkBlockNetmaskAddr_Object = MibTableColumn
eqlApplianceNetworkBlockNetmaskAddr = _EqlApplianceNetworkBlockNetmaskAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5, 1, 8),
    _EqlApplianceNetworkBlockNetmaskAddr_Type()
)
eqlApplianceNetworkBlockNetmaskAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNetworkBlockNetmaskAddr.setStatus("current")


class _EqlApplianceNetworkVLANTag_Type(Unsigned32):
    """Custom type eqlApplianceNetworkVLANTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_EqlApplianceNetworkVLANTag_Type.__name__ = "Unsigned32"
_EqlApplianceNetworkVLANTag_Object = MibTableColumn
eqlApplianceNetworkVLANTag = _EqlApplianceNetworkVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5, 1, 9),
    _EqlApplianceNetworkVLANTag_Type()
)
eqlApplianceNetworkVLANTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNetworkVLANTag.setStatus("current")


class _EqlApplianceNetworkAdminState_Type(Integer32):
    """Custom type eqlApplianceNetworkAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("creating", 1),
          ("done", 3),
          ("modifying", 2))
    )


_EqlApplianceNetworkAdminState_Type.__name__ = "Integer32"
_EqlApplianceNetworkAdminState_Object = MibTableColumn
eqlApplianceNetworkAdminState = _EqlApplianceNetworkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5, 1, 10),
    _EqlApplianceNetworkAdminState_Type()
)
eqlApplianceNetworkAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNetworkAdminState.setStatus("current")
_EqlApplianceNetworkMTUSize_Type = Unsigned32
_EqlApplianceNetworkMTUSize_Object = MibTableColumn
eqlApplianceNetworkMTUSize = _EqlApplianceNetworkMTUSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5, 1, 11),
    _EqlApplianceNetworkMTUSize_Type()
)
eqlApplianceNetworkMTUSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNetworkMTUSize.setStatus("current")


class _EqlApplianceNetworkBondingMode_Type(Integer32):
    """Custom type eqlApplianceNetworkBondingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alb", 0),
          ("lacp", 1))
    )


_EqlApplianceNetworkBondingMode_Type.__name__ = "Integer32"
_EqlApplianceNetworkBondingMode_Object = MibTableColumn
eqlApplianceNetworkBondingMode = _EqlApplianceNetworkBondingMode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 5, 1, 12),
    _EqlApplianceNetworkBondingMode_Type()
)
eqlApplianceNetworkBondingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNetworkBondingMode.setStatus("current")
_EqlApplianceIPTable_Object = MibTable
eqlApplianceIPTable = _EqlApplianceIPTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 6)
)
if mibBuilder.loadTexts:
    eqlApplianceIPTable.setStatus("current")
_EqlApplianceIPEntry_Object = MibTableRow
eqlApplianceIPEntry = _EqlApplianceIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 6, 1)
)
eqlApplianceIPEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNetworkType"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNetworkID"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIPAddressType"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIPAddress"),
)
if mibBuilder.loadTexts:
    eqlApplianceIPEntry.setStatus("current")
_EqlApplianceIPRowStatus_Type = RowStatus
_EqlApplianceIPRowStatus_Object = MibTableColumn
eqlApplianceIPRowStatus = _EqlApplianceIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 6, 1, 1),
    _EqlApplianceIPRowStatus_Type()
)
eqlApplianceIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceIPRowStatus.setStatus("current")
_EqlApplianceIPAddressType_Type = InetAddressType
_EqlApplianceIPAddressType_Object = MibTableColumn
eqlApplianceIPAddressType = _EqlApplianceIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 6, 1, 2),
    _EqlApplianceIPAddressType_Type()
)
eqlApplianceIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceIPAddressType.setStatus("current")
_EqlApplianceIPAddress_Type = InetAddress
_EqlApplianceIPAddress_Object = MibTableColumn
eqlApplianceIPAddress = _EqlApplianceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 6, 1, 3),
    _EqlApplianceIPAddress_Type()
)
eqlApplianceIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceIPAddress.setStatus("current")
_EqlApplianceNodeIPTable_Object = MibTable
eqlApplianceNodeIPTable = _EqlApplianceNodeIPTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 7)
)
if mibBuilder.loadTexts:
    eqlApplianceNodeIPTable.setStatus("current")
_EqlApplianceNodeIPEntry_Object = MibTableRow
eqlApplianceNodeIPEntry = _EqlApplianceNodeIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 7, 1)
)
eqlApplianceNodeIPEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNetworkType"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNetworkID"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNodeIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNodeIPAddressType"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNodeIPAddress"),
)
if mibBuilder.loadTexts:
    eqlApplianceNodeIPEntry.setStatus("current")
_EqlApplianceNodeIPRowStatus_Type = RowStatus
_EqlApplianceNodeIPRowStatus_Object = MibTableColumn
eqlApplianceNodeIPRowStatus = _EqlApplianceNodeIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 7, 1, 1),
    _EqlApplianceNodeIPRowStatus_Type()
)
eqlApplianceNodeIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNodeIPRowStatus.setStatus("current")
_EqlApplianceNodeIPAddressType_Type = InetAddressType
_EqlApplianceNodeIPAddressType_Object = MibTableColumn
eqlApplianceNodeIPAddressType = _EqlApplianceNodeIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 7, 1, 2),
    _EqlApplianceNodeIPAddressType_Type()
)
eqlApplianceNodeIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceNodeIPAddressType.setStatus("current")
_EqlApplianceNodeIPAddress_Type = InetAddress
_EqlApplianceNodeIPAddress_Object = MibTableColumn
eqlApplianceNodeIPAddress = _EqlApplianceNodeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 7, 1, 3),
    _EqlApplianceNodeIPAddress_Type()
)
eqlApplianceNodeIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceNodeIPAddress.setStatus("current")
_EqlApplianceOpsTable_Object = MibTable
eqlApplianceOpsTable = _EqlApplianceOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 8)
)
if mibBuilder.loadTexts:
    eqlApplianceOpsTable.setStatus("current")
_EqlApplianceOpsEntry_Object = MibTableRow
eqlApplianceOpsEntry = _EqlApplianceOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 8, 1)
)
eqlApplianceOpsEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceOpsType"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceOpsIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceOpsEntry.setStatus("current")
_EqlApplianceOpsIndex_Type = Unsigned32
_EqlApplianceOpsIndex_Object = MibTableColumn
eqlApplianceOpsIndex = _EqlApplianceOpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 8, 1, 1),
    _EqlApplianceOpsIndex_Type()
)
eqlApplianceOpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceOpsIndex.setStatus("current")
_EqlApplianceOpsRowStatus_Type = RowStatus
_EqlApplianceOpsRowStatus_Object = MibTableColumn
eqlApplianceOpsRowStatus = _EqlApplianceOpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 8, 1, 2),
    _EqlApplianceOpsRowStatus_Type()
)
eqlApplianceOpsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceOpsRowStatus.setStatus("current")


class _EqlApplianceOpsType_Type(Integer32):
    """Custom type eqlApplianceOpsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("add-nas-appliance", 13),
          ("add-pair", 9),
          ("attach", 5),
          ("container-cfg-modify", 19),
          ("create-nas-appliance", 11),
          ("delete", 10),
          ("detach", 8),
          ("diagnostics", 15),
          ("discover", 12),
          ("expand", 6),
          ("format", 2),
          ("incrementalformat", 7),
          ("join-nas-appliance", 14),
          ("nas-cluster-update", 16),
          ("none", 0),
          ("restore-config", 17),
          ("service-mode-change", 18),
          ("start", 3),
          ("stop", 4),
          ("validation", 1))
    )


_EqlApplianceOpsType_Type.__name__ = "Integer32"
_EqlApplianceOpsType_Object = MibTableColumn
eqlApplianceOpsType = _EqlApplianceOpsType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 8, 1, 3),
    _EqlApplianceOpsType_Type()
)
eqlApplianceOpsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceOpsType.setStatus("current")
_EqlApplianceOpsStatus_Type = Unsigned32
_EqlApplianceOpsStatus_Object = MibTableColumn
eqlApplianceOpsStatus = _EqlApplianceOpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 8, 1, 4),
    _EqlApplianceOpsStatus_Type()
)
eqlApplianceOpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceOpsStatus.setStatus("current")


class _EqlApplianceOpsPercentage_Type(Unsigned32):
    """Custom type eqlApplianceOpsPercentage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqlApplianceOpsPercentage_Type.__name__ = "Unsigned32"
_EqlApplianceOpsPercentage_Object = MibTableColumn
eqlApplianceOpsPercentage = _EqlApplianceOpsPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 8, 1, 5),
    _EqlApplianceOpsPercentage_Type()
)
eqlApplianceOpsPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceOpsPercentage.setStatus("current")
_EqlApplianceOpsRequestId_Type = Counter64
_EqlApplianceOpsRequestId_Object = MibTableColumn
eqlApplianceOpsRequestId = _EqlApplianceOpsRequestId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 8, 1, 6),
    _EqlApplianceOpsRequestId_Type()
)
eqlApplianceOpsRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceOpsRequestId.setStatus("current")
_EqlVolumeApplianceTable_Object = MibTable
eqlVolumeApplianceTable = _EqlVolumeApplianceTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 9)
)
if mibBuilder.loadTexts:
    eqlVolumeApplianceTable.setStatus("current")
_EqlVolumeApplianceEntry_Object = MibTableRow
eqlVolumeApplianceEntry = _EqlVolumeApplianceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 9, 1)
)
if mibBuilder.loadTexts:
    eqlVolumeApplianceEntry.setStatus("current")
_EqlVolumeApplianceRowStatus_Type = RowStatus
_EqlVolumeApplianceRowStatus_Object = MibTableColumn
eqlVolumeApplianceRowStatus = _EqlVolumeApplianceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 9, 1, 1),
    _EqlVolumeApplianceRowStatus_Type()
)
eqlVolumeApplianceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolumeApplianceRowStatus.setStatus("current")
_EqlVolumeApplianceIndex_Type = Unsigned32
_EqlVolumeApplianceIndex_Object = MibTableColumn
eqlVolumeApplianceIndex = _EqlVolumeApplianceIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 9, 1, 2),
    _EqlVolumeApplianceIndex_Type()
)
eqlVolumeApplianceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolumeApplianceIndex.setStatus("current")
_EqlVolumeApplianceNodeIndex_Type = Unsigned32
_EqlVolumeApplianceNodeIndex_Object = MibTableColumn
eqlVolumeApplianceNodeIndex = _EqlVolumeApplianceNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 9, 1, 3),
    _EqlVolumeApplianceNodeIndex_Type()
)
eqlVolumeApplianceNodeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolumeApplianceNodeIndex.setStatus("current")


class _EqlVolumeApplianceState_Type(Integer32):
    """Custom type eqlVolumeApplianceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("expansionpending", 2),
          ("formatpending", 0),
          ("formatted", 1))
    )


_EqlVolumeApplianceState_Type.__name__ = "Integer32"
_EqlVolumeApplianceState_Object = MibTableColumn
eqlVolumeApplianceState = _EqlVolumeApplianceState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 9, 1, 4),
    _EqlVolumeApplianceState_Type()
)
eqlVolumeApplianceState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolumeApplianceState.setStatus("current")
_EqlApplianceOpsFailureTable_Object = MibTable
eqlApplianceOpsFailureTable = _EqlApplianceOpsFailureTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 10)
)
if mibBuilder.loadTexts:
    eqlApplianceOpsFailureTable.setStatus("current")
_EqlApplianceOpsFailureEntry_Object = MibTableRow
eqlApplianceOpsFailureEntry = _EqlApplianceOpsFailureEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 10, 1)
)
eqlApplianceOpsFailureEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceOpsType"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceOpsIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceOpsFailureIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceOpsFailureEntry.setStatus("current")
_EqlApplianceOpsFailureIndex_Type = Unsigned32
_EqlApplianceOpsFailureIndex_Object = MibTableColumn
eqlApplianceOpsFailureIndex = _EqlApplianceOpsFailureIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 10, 1, 1),
    _EqlApplianceOpsFailureIndex_Type()
)
eqlApplianceOpsFailureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceOpsFailureIndex.setStatus("current")


class _EqlApplianceOpsFailureType_Type(Integer32):
    """Custom type eqlApplianceOpsFailureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_EqlApplianceOpsFailureType_Type.__name__ = "Integer32"
_EqlApplianceOpsFailureType_Object = MibTableColumn
eqlApplianceOpsFailureType = _EqlApplianceOpsFailureType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 10, 1, 2),
    _EqlApplianceOpsFailureType_Type()
)
eqlApplianceOpsFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceOpsFailureType.setStatus("current")
_EqlApplianceOpsFailureScope_Type = Unsigned32
_EqlApplianceOpsFailureScope_Object = MibTableColumn
eqlApplianceOpsFailureScope = _EqlApplianceOpsFailureScope_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 10, 1, 3),
    _EqlApplianceOpsFailureScope_Type()
)
eqlApplianceOpsFailureScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceOpsFailureScope.setStatus("current")
_EqlApplianceOpsFailureCode_Type = Unsigned32
_EqlApplianceOpsFailureCode_Object = MibTableColumn
eqlApplianceOpsFailureCode = _EqlApplianceOpsFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 10, 1, 4),
    _EqlApplianceOpsFailureCode_Type()
)
eqlApplianceOpsFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceOpsFailureCode.setStatus("current")


class _EqlApplianceOpsFailureComponent_Type(Integer32):
    """Custom type eqlApplianceOpsFailureComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("connectivity", 12),
          ("cpus", 3),
          ("fans", 1),
          ("fc", 4),
          ("ipmi", 7),
          ("memory", 11),
          ("monitor", 5),
          ("network", 13),
          ("nics", 6),
          ("psus", 2),
          ("raid", 10),
          ("temperatures", 9),
          ("unknown", 0),
          ("ups", 8))
    )


_EqlApplianceOpsFailureComponent_Type.__name__ = "Integer32"
_EqlApplianceOpsFailureComponent_Object = MibTableColumn
eqlApplianceOpsFailureComponent = _EqlApplianceOpsFailureComponent_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 10, 1, 5),
    _EqlApplianceOpsFailureComponent_Type()
)
eqlApplianceOpsFailureComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceOpsFailureComponent.setStatus("current")


class _EqlApplianceOpsFailureSubComponent_Type(OctetString):
    """Custom type eqlApplianceOpsFailureSubComponent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlApplianceOpsFailureSubComponent_Type.__name__ = "OctetString"
_EqlApplianceOpsFailureSubComponent_Object = MibTableColumn
eqlApplianceOpsFailureSubComponent = _EqlApplianceOpsFailureSubComponent_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 10, 1, 6),
    _EqlApplianceOpsFailureSubComponent_Type()
)
eqlApplianceOpsFailureSubComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceOpsFailureSubComponent.setStatus("current")


class _EqlApplianceOpsFailureMessage_Type(OctetString):
    """Custom type eqlApplianceOpsFailureMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EqlApplianceOpsFailureMessage_Type.__name__ = "OctetString"
_EqlApplianceOpsFailureMessage_Object = MibTableColumn
eqlApplianceOpsFailureMessage = _EqlApplianceOpsFailureMessage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 10, 1, 7),
    _EqlApplianceOpsFailureMessage_Type()
)
eqlApplianceOpsFailureMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceOpsFailureMessage.setStatus("current")
_EqlApplianceNodeHealthFailureTable_Object = MibTable
eqlApplianceNodeHealthFailureTable = _EqlApplianceNodeHealthFailureTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 11)
)
if mibBuilder.loadTexts:
    eqlApplianceNodeHealthFailureTable.setStatus("current")
_EqlApplianceNodeHealthFailureEntry_Object = MibTableRow
eqlApplianceNodeHealthFailureEntry = _EqlApplianceNodeHealthFailureEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 11, 1)
)
eqlApplianceNodeHealthFailureEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNodeIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNodeHealthFailureIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceNodeHealthFailureEntry.setStatus("current")
_EqlApplianceNodeHealthFailureIndex_Type = Unsigned32
_EqlApplianceNodeHealthFailureIndex_Object = MibTableColumn
eqlApplianceNodeHealthFailureIndex = _EqlApplianceNodeHealthFailureIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 11, 1, 1),
    _EqlApplianceNodeHealthFailureIndex_Type()
)
eqlApplianceNodeHealthFailureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceNodeHealthFailureIndex.setStatus("current")


class _EqlApplianceNodeHealthFailureType_Type(Integer32):
    """Custom type eqlApplianceNodeHealthFailureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_EqlApplianceNodeHealthFailureType_Type.__name__ = "Integer32"
_EqlApplianceNodeHealthFailureType_Object = MibTableColumn
eqlApplianceNodeHealthFailureType = _EqlApplianceNodeHealthFailureType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 11, 1, 2),
    _EqlApplianceNodeHealthFailureType_Type()
)
eqlApplianceNodeHealthFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeHealthFailureType.setStatus("current")
_EqlApplianceNodeHealthFailureCode_Type = Unsigned32
_EqlApplianceNodeHealthFailureCode_Object = MibTableColumn
eqlApplianceNodeHealthFailureCode = _EqlApplianceNodeHealthFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 11, 1, 3),
    _EqlApplianceNodeHealthFailureCode_Type()
)
eqlApplianceNodeHealthFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeHealthFailureCode.setStatus("current")


class _EqlApplianceNodeHealthFailureComponent_Type(Integer32):
    """Custom type eqlApplianceNodeHealthFailureComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internalhw", 3),
          ("network", 2),
          ("power", 1),
          ("unknown", 0))
    )


_EqlApplianceNodeHealthFailureComponent_Type.__name__ = "Integer32"
_EqlApplianceNodeHealthFailureComponent_Object = MibTableColumn
eqlApplianceNodeHealthFailureComponent = _EqlApplianceNodeHealthFailureComponent_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 11, 1, 4),
    _EqlApplianceNodeHealthFailureComponent_Type()
)
eqlApplianceNodeHealthFailureComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeHealthFailureComponent.setStatus("current")


class _EqlApplianceNodeHealthFailureSubComponent_Type(OctetString):
    """Custom type eqlApplianceNodeHealthFailureSubComponent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlApplianceNodeHealthFailureSubComponent_Type.__name__ = "OctetString"
_EqlApplianceNodeHealthFailureSubComponent_Object = MibTableColumn
eqlApplianceNodeHealthFailureSubComponent = _EqlApplianceNodeHealthFailureSubComponent_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 11, 1, 5),
    _EqlApplianceNodeHealthFailureSubComponent_Type()
)
eqlApplianceNodeHealthFailureSubComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeHealthFailureSubComponent.setStatus("current")


class _EqlApplianceNodeHealthFailureMessage_Type(OctetString):
    """Custom type eqlApplianceNodeHealthFailureMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EqlApplianceNodeHealthFailureMessage_Type.__name__ = "OctetString"
_EqlApplianceNodeHealthFailureMessage_Object = MibTableColumn
eqlApplianceNodeHealthFailureMessage = _EqlApplianceNodeHealthFailureMessage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 11, 1, 6),
    _EqlApplianceNodeHealthFailureMessage_Type()
)
eqlApplianceNodeHealthFailureMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeHealthFailureMessage.setStatus("current")
_EqlApplianceServiceStatusTable_Object = MibTable
eqlApplianceServiceStatusTable = _EqlApplianceServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 12)
)
if mibBuilder.loadTexts:
    eqlApplianceServiceStatusTable.setStatus("current")
_EqlApplianceServiceStatusEntry_Object = MibTableRow
eqlApplianceServiceStatusEntry = _EqlApplianceServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 12, 1)
)
eqlApplianceServiceStatusEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceServiceStatusEntry.setStatus("current")


class _EqlApplianceOverallState_Type(Integer32):
    """Custom type eqlApplianceOverallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("stopping", 3),
          ("unknown", 0))
    )


_EqlApplianceOverallState_Type.__name__ = "Integer32"
_EqlApplianceOverallState_Object = MibTableColumn
eqlApplianceOverallState = _EqlApplianceOverallState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 12, 1, 1),
    _EqlApplianceOverallState_Type()
)
eqlApplianceOverallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceOverallState.setStatus("current")


class _EqlApplianceServiceStatus_Type(Integer32):
    """Custom type eqlApplianceServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("normal", 3),
          ("unknown", 0),
          ("warning", 2))
    )


_EqlApplianceServiceStatus_Type.__name__ = "Integer32"
_EqlApplianceServiceStatus_Object = MibTableColumn
eqlApplianceServiceStatus = _EqlApplianceServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 12, 1, 2),
    _EqlApplianceServiceStatus_Type()
)
eqlApplianceServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceServiceStatus.setStatus("current")


class _EqlApplianceServiceCriticalConditions_Type(Bits):
    """Custom type eqlApplianceServiceCriticalConditions based on Bits"""
    namedValues = NamedValues(
        *(("eqlNASChassisBackplaneNetworkCritical", 6),
          ("eqlNASChassisClientNetworkCritical", 5),
          ("eqlNASChassisFanCritical", 9),
          ("eqlNASChassisInternalNetworkCritical", 7),
          ("eqlNASChassisSanNetworkCritical", 8),
          ("eqlNASControllerAmbientTempCritical", 10),
          ("eqlNASControllerBPSCritical", 11),
          ("eqlNASControllerCPUCritical", 12),
          ("eqlNASControllerFanCritical", 13),
          ("eqlNASControllerLocalDiskCritical", 14),
          ("eqlNASControllerMemoryCritical", 16),
          ("eqlNASControllerRaidControllerCritical", 15),
          ("eqlNASControllerVirtualDiskCritical", 17),
          ("exaStoreServersFault", 3),
          ("exaStoreServiceFaultCacheLoss", 0),
          ("exaStoreServiceFaultServers", 1),
          ("exaStoreServiceNoService", 2),
          ("exaStoreStorageSubsysFault", 4))
    )

_EqlApplianceServiceCriticalConditions_Type.__name__ = "Bits"
_EqlApplianceServiceCriticalConditions_Object = MibTableColumn
eqlApplianceServiceCriticalConditions = _EqlApplianceServiceCriticalConditions_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 12, 1, 3),
    _EqlApplianceServiceCriticalConditions_Type()
)
eqlApplianceServiceCriticalConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceServiceCriticalConditions.setStatus("current")


class _EqlApplianceServiceWarningConditions_Type(Bits):
    """Custom type eqlApplianceServiceWarningConditions based on Bits"""
    namedValues = NamedValues(
        *(("eqlNASChassisBackplaneNetworkNotOptimal", 7),
          ("eqlNASChassisClientNetworkNotOptimal", 6),
          ("eqlNASChassisFanNotOptimal", 10),
          ("eqlNASChassisInternalNetworkNotOptimal", 8),
          ("eqlNASChassisPowerSupplyPartial", 11),
          ("eqlNASChassisSanNetworkNotOptimal", 9),
          ("eqlNASControllerAmbientTempNotOptimal", 12),
          ("eqlNASControllerBPSNotOptimal", 13),
          ("eqlNASControllerCPUNotOptimal", 14),
          ("eqlNASControllerFanNotOptimal", 15),
          ("eqlNASControllerLocalDiskNotOptimal", 16),
          ("eqlNASControllerMemoryNotOptimal", 18),
          ("eqlNASControllerPowerSupplyPartial", 20),
          ("eqlNASControllerRaidControllerNotOptimal", 17),
          ("eqlNASControllerVirtualDiskNotOptimal", 19),
          ("exaStoreServersNotOptimal", 4),
          ("exaStoreServersSomeDetached", 3),
          ("exaStoreServersSomeDown", 2),
          ("exaStoreServiceFSCheckerFailed", 0),
          ("exaStoreServicejournal", 1),
          ("exaStoreStorageSubsysNotOptimal", 5))
    )

_EqlApplianceServiceWarningConditions_Type.__name__ = "Bits"
_EqlApplianceServiceWarningConditions_Object = MibTableColumn
eqlApplianceServiceWarningConditions = _EqlApplianceServiceWarningConditions_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 12, 1, 4),
    _EqlApplianceServiceWarningConditions_Type()
)
eqlApplianceServiceWarningConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceServiceWarningConditions.setStatus("current")


class _EqlApplianceServiceAction_Type(Integer32):
    """Custom type eqlApplianceServiceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("massFailback", 1),
          ("massRebalance", 2))
    )


_EqlApplianceServiceAction_Type.__name__ = "Integer32"
_EqlApplianceServiceAction_Object = MibTableColumn
eqlApplianceServiceAction = _EqlApplianceServiceAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 12, 1, 5),
    _EqlApplianceServiceAction_Type()
)
eqlApplianceServiceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlApplianceServiceAction.setStatus("current")
_EqlApplianceStatsTable_Object = MibTable
eqlApplianceStatsTable = _EqlApplianceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 13)
)
if mibBuilder.loadTexts:
    eqlApplianceStatsTable.setStatus("current")
_EqlApplianceStatsEntry_Object = MibTableRow
eqlApplianceStatsEntry = _EqlApplianceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 13, 1)
)
eqlApplianceStatsEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceStatsEntry.setStatus("current")
_EqlApplianceStatsTotalCapacity_Type = Counter64
_EqlApplianceStatsTotalCapacity_Object = MibTableColumn
eqlApplianceStatsTotalCapacity = _EqlApplianceStatsTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 13, 1, 1),
    _EqlApplianceStatsTotalCapacity_Type()
)
eqlApplianceStatsTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceStatsTotalCapacity.setStatus("current")
_EqlApplianceStatsTotalAllocated_Type = Counter64
_EqlApplianceStatsTotalAllocated_Object = MibTableColumn
eqlApplianceStatsTotalAllocated = _EqlApplianceStatsTotalAllocated_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 13, 1, 2),
    _EqlApplianceStatsTotalAllocated_Type()
)
eqlApplianceStatsTotalAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceStatsTotalAllocated.setStatus("current")
_EqlApplianceStatsTotalUsed_Type = Counter64
_EqlApplianceStatsTotalUsed_Object = MibTableColumn
eqlApplianceStatsTotalUsed = _EqlApplianceStatsTotalUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 13, 1, 3),
    _EqlApplianceStatsTotalUsed_Type()
)
eqlApplianceStatsTotalUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceStatsTotalUsed.setStatus("current")
_EqlApplianceStatsTotalFree_Type = Counter64
_EqlApplianceStatsTotalFree_Object = MibTableColumn
eqlApplianceStatsTotalFree = _EqlApplianceStatsTotalFree_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 13, 1, 4),
    _EqlApplianceStatsTotalFree_Type()
)
eqlApplianceStatsTotalFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceStatsTotalFree.setStatus("current")
_EqlApplianceStatsTotalSnapshots_Type = Counter64
_EqlApplianceStatsTotalSnapshots_Object = MibTableColumn
eqlApplianceStatsTotalSnapshots = _EqlApplianceStatsTotalSnapshots_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 13, 1, 5),
    _EqlApplianceStatsTotalSnapshots_Type()
)
eqlApplianceStatsTotalSnapshots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceStatsTotalSnapshots.setStatus("current")
_EqlApplianceStatsNumberOfContainers_Type = Counter64
_EqlApplianceStatsNumberOfContainers_Object = MibTableColumn
eqlApplianceStatsNumberOfContainers = _EqlApplianceStatsNumberOfContainers_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 13, 1, 6),
    _EqlApplianceStatsNumberOfContainers_Type()
)
eqlApplianceStatsNumberOfContainers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceStatsNumberOfContainers.setStatus("current")
_EqlApplianceStatsNumberOfNfsExports_Type = Counter64
_EqlApplianceStatsNumberOfNfsExports_Object = MibTableColumn
eqlApplianceStatsNumberOfNfsExports = _EqlApplianceStatsNumberOfNfsExports_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 13, 1, 7),
    _EqlApplianceStatsNumberOfNfsExports_Type()
)
eqlApplianceStatsNumberOfNfsExports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceStatsNumberOfNfsExports.setStatus("current")
_EqlApplianceStatsNumberOfCifsShares_Type = Counter64
_EqlApplianceStatsNumberOfCifsShares_Object = MibTableColumn
eqlApplianceStatsNumberOfCifsShares = _EqlApplianceStatsNumberOfCifsShares_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 13, 1, 8),
    _EqlApplianceStatsNumberOfCifsShares_Type()
)
eqlApplianceStatsNumberOfCifsShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceStatsNumberOfCifsShares.setStatus("current")
_EqlApplianceStatsNumberOfSnapshots_Type = Counter64
_EqlApplianceStatsNumberOfSnapshots_Object = MibTableColumn
eqlApplianceStatsNumberOfSnapshots = _EqlApplianceStatsNumberOfSnapshots_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 13, 1, 9),
    _EqlApplianceStatsNumberOfSnapshots_Type()
)
eqlApplianceStatsNumberOfSnapshots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceStatsNumberOfSnapshots.setStatus("current")
_EqlApplianceStatsTotalOptimizationSpaceSavings_Type = Counter64
_EqlApplianceStatsTotalOptimizationSpaceSavings_Object = MibTableColumn
eqlApplianceStatsTotalOptimizationSpaceSavings = _EqlApplianceStatsTotalOptimizationSpaceSavings_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 13, 1, 10),
    _EqlApplianceStatsTotalOptimizationSpaceSavings_Type()
)
eqlApplianceStatsTotalOptimizationSpaceSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceStatsTotalOptimizationSpaceSavings.setStatus("current")
_EqlApplianceNodeStatusTable_Object = MibTable
eqlApplianceNodeStatusTable = _EqlApplianceNodeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 14)
)
if mibBuilder.loadTexts:
    eqlApplianceNodeStatusTable.setStatus("current")
_EqlApplianceNodeStatusEntry_Object = MibTableRow
eqlApplianceNodeStatusEntry = _EqlApplianceNodeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 14, 1)
)
eqlApplianceNodeStatusEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNodeIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceNodeStatusEntry.setStatus("current")


class _EqlApplianceNodeStatusNodeState_Type(Integer32):
    """Custom type eqlApplianceNodeStatusNodeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("detached", 3),
          ("off", 2),
          ("on", 1),
          ("unknown", 0))
    )


_EqlApplianceNodeStatusNodeState_Type.__name__ = "Integer32"
_EqlApplianceNodeStatusNodeState_Object = MibTableColumn
eqlApplianceNodeStatusNodeState = _EqlApplianceNodeStatusNodeState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 14, 1, 1),
    _EqlApplianceNodeStatusNodeState_Type()
)
eqlApplianceNodeStatusNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceNodeStatusNodeState.setStatus("current")
_EqlApplianceMultiStateOpsTable_Object = MibTable
eqlApplianceMultiStateOpsTable = _EqlApplianceMultiStateOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15)
)
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsTable.setStatus("current")
_EqlApplianceMultiStateOpsEntry_Object = MibTableRow
eqlApplianceMultiStateOpsEntry = _EqlApplianceMultiStateOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1)
)
eqlApplianceMultiStateOpsEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceMultiStateOpsType"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceMultiStateOpsIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsEntry.setStatus("current")
_EqlApplianceMultiStateOpsIndex_Type = Unsigned32
_EqlApplianceMultiStateOpsIndex_Object = MibTableColumn
eqlApplianceMultiStateOpsIndex = _EqlApplianceMultiStateOpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 1),
    _EqlApplianceMultiStateOpsIndex_Type()
)
eqlApplianceMultiStateOpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsIndex.setStatus("current")
_EqlApplianceMultiStateOpsRowStatus_Type = RowStatus
_EqlApplianceMultiStateOpsRowStatus_Object = MibTableColumn
eqlApplianceMultiStateOpsRowStatus = _EqlApplianceMultiStateOpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 2),
    _EqlApplianceMultiStateOpsRowStatus_Type()
)
eqlApplianceMultiStateOpsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsRowStatus.setStatus("current")


class _EqlApplianceMultiStateOpsType_Type(Integer32):
    """Custom type eqlApplianceMultiStateOpsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("add-pair", 2),
          ("attach-node", 1),
          ("container-cfg-modify", 13),
          ("delete", 7),
          ("detach", 4),
          ("diagnostics", 9),
          ("long-running-blocking-config", 8),
          ("nas-cluster-update", 10),
          ("resize", 3),
          ("restore", 11),
          ("service-mode-change", 12),
          ("start", 5),
          ("stop", 6),
          ("unknown", 0))
    )


_EqlApplianceMultiStateOpsType_Type.__name__ = "Integer32"
_EqlApplianceMultiStateOpsType_Object = MibTableColumn
eqlApplianceMultiStateOpsType = _EqlApplianceMultiStateOpsType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 3),
    _EqlApplianceMultiStateOpsType_Type()
)
eqlApplianceMultiStateOpsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsType.setStatus("current")
_EqlApplianceMultiStateOpsStatus_Type = Unsigned32
_EqlApplianceMultiStateOpsStatus_Object = MibTableColumn
eqlApplianceMultiStateOpsStatus = _EqlApplianceMultiStateOpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 4),
    _EqlApplianceMultiStateOpsStatus_Type()
)
eqlApplianceMultiStateOpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsStatus.setStatus("current")


class _EqlApplianceMultiStateOpsServiceTag_Type(OctetString):
    """Custom type eqlApplianceMultiStateOpsServiceTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EqlApplianceMultiStateOpsServiceTag_Type.__name__ = "OctetString"
_EqlApplianceMultiStateOpsServiceTag_Object = MibTableColumn
eqlApplianceMultiStateOpsServiceTag = _EqlApplianceMultiStateOpsServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 5),
    _EqlApplianceMultiStateOpsServiceTag_Type()
)
eqlApplianceMultiStateOpsServiceTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsServiceTag.setStatus("current")


class _EqlApplianceMultiStateOpsServiceTag2_Type(OctetString):
    """Custom type eqlApplianceMultiStateOpsServiceTag2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EqlApplianceMultiStateOpsServiceTag2_Type.__name__ = "OctetString"
_EqlApplianceMultiStateOpsServiceTag2_Object = MibTableColumn
eqlApplianceMultiStateOpsServiceTag2 = _EqlApplianceMultiStateOpsServiceTag2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 6),
    _EqlApplianceMultiStateOpsServiceTag2_Type()
)
eqlApplianceMultiStateOpsServiceTag2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsServiceTag2.setStatus("current")
_EqlApplianceMultiStateOpsNodeIndex_Type = Unsigned32
_EqlApplianceMultiStateOpsNodeIndex_Object = MibTableColumn
eqlApplianceMultiStateOpsNodeIndex = _EqlApplianceMultiStateOpsNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 7),
    _EqlApplianceMultiStateOpsNodeIndex_Type()
)
eqlApplianceMultiStateOpsNodeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsNodeIndex.setStatus("current")
_EqlApplianceMultiStateOpsNodeIndex2_Type = Unsigned32
_EqlApplianceMultiStateOpsNodeIndex2_Object = MibTableColumn
eqlApplianceMultiStateOpsNodeIndex2 = _EqlApplianceMultiStateOpsNodeIndex2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 8),
    _EqlApplianceMultiStateOpsNodeIndex2_Type()
)
eqlApplianceMultiStateOpsNodeIndex2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsNodeIndex2.setStatus("current")


class _EqlApplianceMultiStateOpsState_Type(Integer32):
    """Custom type eqlApplianceMultiStateOpsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
              1009,
              1010,
              1101,
              1102,
              1103,
              1104,
              1105,
              1106,
              1107,
              1201,
              1301,
              1401,
              1501,
              1502,
              1503,
              1504,
              1505,
              1506,
              1507,
              1508,
              1509,
              1510,
              1511,
              1512,
              1513,
              1514,
              1515,
              1516,
              1517,
              1518,
              1519,
              1520,
              1521,
              1522,
              1523,
              1524,
              1601,
              1602,
              1701,
              1702,
              1703,
              1704,
              1705,
              1706,
              1707,
              1708,
              1709,
              1710,
              1711,
              1712,
              1713,
              1714,
              1801,
              1802,
              1803,
              1804,
              1805,
              1806,
              1807,
              1808,
              1809,
              1901,
              2001,
              2002,
              2003,
              2004,
              2005,
              2006,
              2007,
              2008,
              2009,
              2010,
              2011,
              2012,
              2013,
              2014,
              2015,
              2016,
              2101,
              2200)
        )
    )
    namedValues = NamedValues(
        *(("add-pair-action-inprogress", 1518),
          ("add-pair-attach-inprogress", 1516),
          ("add-pair-cluster-client-network", 1508),
          ("add-pair-cluster-internal-network", 1503),
          ("add-pair-cluster-san-network", 1506),
          ("add-pair-completed", 1519),
          ("add-pair-configure-gateway", 1510),
          ("add-pair-create-volume-acls", 1514),
          ("add-pair-nas-appliance-add-inprogress", 1521),
          ("add-pair-nas-appliance-join-inprogress", 1524),
          ("add-pair-node-count", 1502),
          ("add-pair-node-setup", 1501),
          ("add-pair-nodes-client-network", 1509),
          ("add-pair-nodes-internal-network", 1505),
          ("add-pair-nodes-san-network", 1507),
          ("add-pair-nodes-validation-inprogress", 1512),
          ("add-pair-prepare", 1513),
          ("add-pair-reset-node-count", 1504),
          ("add-pair-start-action", 1517),
          ("add-pair-start-attach", 1515),
          ("add-pair-start-nas-appliance-add", 1520),
          ("add-pair-start-nas-appliance-join", 1523),
          ("add-pair-start-nodes-validation", 1511),
          ("add-pair-start-volume-discovery", 1522),
          ("attach-action", 1008),
          ("attach-action-inprogress", 1009),
          ("attach-client-network", 1004),
          ("attach-completed", 1010),
          ("attach-configure-gateway", 1005),
          ("attach-internal-network", 1002),
          ("attach-node-setup", 1001),
          ("attach-nodes-validation-inprogress", 1007),
          ("attach-san-network", 1003),
          ("attach-start-nodes-validation", 1006),
          ("cifs-operation", 1713),
          ("configure-active-directory", 1708),
          ("configure-credential-ldap", 1705),
          ("configure-credential-nis", 1706),
          ("configure-credential-no-external", 1704),
          ("configure-credential-unknown", 1707),
          ("container-cfg-modify-inprogress", 2200),
          ("delete-container-host-access", 1711),
          ("delete-inprogress", 1601),
          ("detach-inprogress", 1201),
          ("grp-inet-addr-set", 1710),
          ("local-delete-inprogress", 1602),
          ("max-keep-set", 1709),
          ("modify-client-network", 1703),
          ("modify-internal-network", 1701),
          ("modify-san-network", 1702),
          ("nas-cluster-update-inprogress", 1901),
          ("nas-cluster-update-start", 1714),
          ("nas-diags-check-file-finished", 1807),
          ("nas-diags-check-file-started", 1806),
          ("nas-diags-check-general-finished", 1804),
          ("nas-diags-check-general-started", 1803),
          ("nas-diags-done", 1809),
          ("nas-diags-finalize", 1808),
          ("nas-diags-init", 1801),
          ("nas-diags-start-file", 1805),
          ("nas-diags-start-general", 1802),
          ("rename-cluster", 1712),
          ("resize-completed", 1105),
          ("resize-discover-volumes", 1107),
          ("resize-expand", 1101),
          ("resize-expand-inprogress", 1102),
          ("resize-format", 1103),
          ("resize-format-inprogress", 1104),
          ("resize-nas-volumes", 1106),
          ("restore-cluster-name", 2005),
          ("restore-config-restore-in-progress", 2015),
          ("restore-create-volume-acls", 2010),
          ("restore-done", 2016),
          ("restore-format-in-progress", 2013),
          ("restore-internal-network", 2004),
          ("restore-nas-appliance-create-in-progress", 2007),
          ("restore-san-network", 2008),
          ("restore-send-eql-group-ip", 2009),
          ("restore-service-mode-to-maintenance", 2002),
          ("restore-start", 2001),
          ("restore-start-config-restore", 2014),
          ("restore-start-format", 2012),
          ("restore-start-nas-appliance-create", 2006),
          ("restore-start-volume-discovery", 2011),
          ("restore-transitioning-to-maintenance", 2003),
          ("service-mode-change-inprogress", 2101),
          ("start-inprogress", 1301),
          ("stop-inprogress", 1401),
          ("unknown", 0))
    )


_EqlApplianceMultiStateOpsState_Type.__name__ = "Integer32"
_EqlApplianceMultiStateOpsState_Object = MibTableColumn
eqlApplianceMultiStateOpsState = _EqlApplianceMultiStateOpsState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 9),
    _EqlApplianceMultiStateOpsState_Type()
)
eqlApplianceMultiStateOpsState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsState.setStatus("current")


class _EqlApplianceMultiStateOpsPercentage_Type(Unsigned32):
    """Custom type eqlApplianceMultiStateOpsPercentage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqlApplianceMultiStateOpsPercentage_Type.__name__ = "Unsigned32"
_EqlApplianceMultiStateOpsPercentage_Object = MibTableColumn
eqlApplianceMultiStateOpsPercentage = _EqlApplianceMultiStateOpsPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 10),
    _EqlApplianceMultiStateOpsPercentage_Type()
)
eqlApplianceMultiStateOpsPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsPercentage.setStatus("current")


class _EqlApplianceMultiStateOpsAction_Type(Integer32):
    """Custom type eqlApplianceMultiStateOpsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("continue", 2),
          ("delete", 3),
          ("none", 0),
          ("retry", 1),
          ("start", 4))
    )


_EqlApplianceMultiStateOpsAction_Type.__name__ = "Integer32"
_EqlApplianceMultiStateOpsAction_Object = MibTableColumn
eqlApplianceMultiStateOpsAction = _EqlApplianceMultiStateOpsAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 11),
    _EqlApplianceMultiStateOpsAction_Type()
)
eqlApplianceMultiStateOpsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsAction.setStatus("current")
_EqlApplianceMultiStateOpsCurNodeIndex_Type = Unsigned32
_EqlApplianceMultiStateOpsCurNodeIndex_Object = MibTableColumn
eqlApplianceMultiStateOpsCurNodeIndex = _EqlApplianceMultiStateOpsCurNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 12),
    _EqlApplianceMultiStateOpsCurNodeIndex_Type()
)
eqlApplianceMultiStateOpsCurNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsCurNodeIndex.setStatus("current")


class _EqlApplianceMultiStateOpsLongRunningOp_Type(TruthValue):
    """Custom type eqlApplianceMultiStateOpsLongRunningOp based on TruthValue"""


_EqlApplianceMultiStateOpsLongRunningOp_Object = MibTableColumn
eqlApplianceMultiStateOpsLongRunningOp = _EqlApplianceMultiStateOpsLongRunningOp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 13),
    _EqlApplianceMultiStateOpsLongRunningOp_Type()
)
eqlApplianceMultiStateOpsLongRunningOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsLongRunningOp.setStatus("current")
_EqlApplianceMultiStateOpsRequestId_Type = Counter64
_EqlApplianceMultiStateOpsRequestId_Object = MibTableColumn
eqlApplianceMultiStateOpsRequestId = _EqlApplianceMultiStateOpsRequestId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 15, 1, 14),
    _EqlApplianceMultiStateOpsRequestId_Type()
)
eqlApplianceMultiStateOpsRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceMultiStateOpsRequestId.setStatus("current")
_EqlApplianceNdmpTable_Object = MibTable
eqlApplianceNdmpTable = _EqlApplianceNdmpTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 16)
)
if mibBuilder.loadTexts:
    eqlApplianceNdmpTable.setStatus("current")
_EqlApplianceNdmpEntry_Object = MibTableRow
eqlApplianceNdmpEntry = _EqlApplianceNdmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 16, 1)
)
eqlApplianceNdmpEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceNdmpEntry.setStatus("current")
_EqlApplianceNdmpRowStatus_Type = RowStatus
_EqlApplianceNdmpRowStatus_Object = MibTableColumn
eqlApplianceNdmpRowStatus = _EqlApplianceNdmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 16, 1, 1),
    _EqlApplianceNdmpRowStatus_Type()
)
eqlApplianceNdmpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNdmpRowStatus.setStatus("current")


class _EqlApplianceNdmpUserName_Type(DisplayString):
    """Custom type eqlApplianceNdmpUserName based on DisplayString"""
    defaultValue = OctetString("backup_user")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlApplianceNdmpUserName_Type.__name__ = "DisplayString"
_EqlApplianceNdmpUserName_Object = MibTableColumn
eqlApplianceNdmpUserName = _EqlApplianceNdmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 16, 1, 2),
    _EqlApplianceNdmpUserName_Type()
)
eqlApplianceNdmpUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNdmpUserName.setStatus("current")


class _EqlApplianceNdmpPasswd_Type(DisplayString):
    """Custom type eqlApplianceNdmpPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EqlApplianceNdmpPasswd_Type.__name__ = "DisplayString"
_EqlApplianceNdmpPasswd_Object = MibTableColumn
eqlApplianceNdmpPasswd = _EqlApplianceNdmpPasswd_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 16, 1, 3),
    _EqlApplianceNdmpPasswd_Type()
)
eqlApplianceNdmpPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNdmpPasswd.setStatus("current")


class _EqlApplianceNdmpDesiredState_Type(Integer32):
    """Custom type eqlApplianceNdmpDesiredState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 0))
    )


_EqlApplianceNdmpDesiredState_Type.__name__ = "Integer32"
_EqlApplianceNdmpDesiredState_Object = MibTableColumn
eqlApplianceNdmpDesiredState = _EqlApplianceNdmpDesiredState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 16, 1, 4),
    _EqlApplianceNdmpDesiredState_Type()
)
eqlApplianceNdmpDesiredState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNdmpDesiredState.setStatus("current")


class _EqlApplianceNdmpClientPort_Type(Integer32):
    """Custom type eqlApplianceNdmpClientPort based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EqlApplianceNdmpClientPort_Type.__name__ = "Integer32"
_EqlApplianceNdmpClientPort_Object = MibTableColumn
eqlApplianceNdmpClientPort = _EqlApplianceNdmpClientPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 16, 1, 5),
    _EqlApplianceNdmpClientPort_Type()
)
eqlApplianceNdmpClientPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNdmpClientPort.setStatus("current")
_EqlApplianceNdmpDmaServerTable_Object = MibTable
eqlApplianceNdmpDmaServerTable = _EqlApplianceNdmpDmaServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 17)
)
if mibBuilder.loadTexts:
    eqlApplianceNdmpDmaServerTable.setStatus("current")
_EqlApplianceNdmpDmaServerEntry_Object = MibTableRow
eqlApplianceNdmpDmaServerEntry = _EqlApplianceNdmpDmaServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 17, 1)
)
eqlApplianceNdmpDmaServerEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNdmpDmaServerIPAddressType"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNdmpDmaServerIPAddress"),
)
if mibBuilder.loadTexts:
    eqlApplianceNdmpDmaServerEntry.setStatus("current")
_EqlApplianceNdmpDmaServerRowStatus_Type = RowStatus
_EqlApplianceNdmpDmaServerRowStatus_Object = MibTableColumn
eqlApplianceNdmpDmaServerRowStatus = _EqlApplianceNdmpDmaServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 17, 1, 1),
    _EqlApplianceNdmpDmaServerRowStatus_Type()
)
eqlApplianceNdmpDmaServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNdmpDmaServerRowStatus.setStatus("current")
_EqlApplianceNdmpDmaServerIPAddressType_Type = InetAddressType
_EqlApplianceNdmpDmaServerIPAddressType_Object = MibTableColumn
eqlApplianceNdmpDmaServerIPAddressType = _EqlApplianceNdmpDmaServerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 17, 1, 2),
    _EqlApplianceNdmpDmaServerIPAddressType_Type()
)
eqlApplianceNdmpDmaServerIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNdmpDmaServerIPAddressType.setStatus("current")
_EqlApplianceNdmpDmaServerIPAddress_Type = InetAddress
_EqlApplianceNdmpDmaServerIPAddress_Object = MibTableColumn
eqlApplianceNdmpDmaServerIPAddress = _EqlApplianceNdmpDmaServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 17, 1, 3),
    _EqlApplianceNdmpDmaServerIPAddress_Type()
)
eqlApplianceNdmpDmaServerIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNdmpDmaServerIPAddress.setStatus("current")


class _EqlApplianceNdmpDmaServerTransactionState_Type(Integer32):
    """Custom type eqlApplianceNdmpDmaServerTransactionState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("configCommit", 3),
          ("configInProgress", 2),
          ("configNone", 0),
          ("configStart", 1),
          ("configStartCommit", 4))
    )


_EqlApplianceNdmpDmaServerTransactionState_Type.__name__ = "Integer32"
_EqlApplianceNdmpDmaServerTransactionState_Object = MibTableColumn
eqlApplianceNdmpDmaServerTransactionState = _EqlApplianceNdmpDmaServerTransactionState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 17, 1, 4),
    _EqlApplianceNdmpDmaServerTransactionState_Type()
)
eqlApplianceNdmpDmaServerTransactionState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceNdmpDmaServerTransactionState.setStatus("current")
_EqlApplianceLocalUserAccessTable_Object = MibTable
eqlApplianceLocalUserAccessTable = _EqlApplianceLocalUserAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 18)
)
if mibBuilder.loadTexts:
    eqlApplianceLocalUserAccessTable.setStatus("current")
_EqlApplianceLocalUserAccessEntry_Object = MibTableRow
eqlApplianceLocalUserAccessEntry = _EqlApplianceLocalUserAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 18, 1)
)
eqlApplianceLocalUserAccessEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceLocalUserName"),
)
if mibBuilder.loadTexts:
    eqlApplianceLocalUserAccessEntry.setStatus("current")
_EqlApplianceLocalUserAccessRowStatus_Type = RowStatus
_EqlApplianceLocalUserAccessRowStatus_Object = MibTableColumn
eqlApplianceLocalUserAccessRowStatus = _EqlApplianceLocalUserAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 18, 1, 1),
    _EqlApplianceLocalUserAccessRowStatus_Type()
)
eqlApplianceLocalUserAccessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLocalUserAccessRowStatus.setStatus("current")


class _EqlApplianceLocalUserName_Type(OctetString):
    """Custom type eqlApplianceLocalUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceLocalUserName_Type.__name__ = "OctetString"
_EqlApplianceLocalUserName_Object = MibTableColumn
eqlApplianceLocalUserName = _EqlApplianceLocalUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 18, 1, 2),
    _EqlApplianceLocalUserName_Type()
)
eqlApplianceLocalUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLocalUserName.setStatus("current")


class _EqlApplianceLocalUserPassword_Type(OctetString):
    """Custom type eqlApplianceLocalUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 240),
    )


_EqlApplianceLocalUserPassword_Type.__name__ = "OctetString"
_EqlApplianceLocalUserPassword_Object = MibTableColumn
eqlApplianceLocalUserPassword = _EqlApplianceLocalUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 18, 1, 3),
    _EqlApplianceLocalUserPassword_Type()
)
eqlApplianceLocalUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLocalUserPassword.setStatus("current")
_EqlApplianceLocalUserUid_Type = Unsigned32
_EqlApplianceLocalUserUid_Object = MibTableColumn
eqlApplianceLocalUserUid = _EqlApplianceLocalUserUid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 18, 1, 4),
    _EqlApplianceLocalUserUid_Type()
)
eqlApplianceLocalUserUid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLocalUserUid.setStatus("current")


class _EqlApplianceLocalUserPrimaryGroup_Type(OctetString):
    """Custom type eqlApplianceLocalUserPrimaryGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlApplianceLocalUserPrimaryGroup_Type.__name__ = "OctetString"
_EqlApplianceLocalUserPrimaryGroup_Object = MibTableColumn
eqlApplianceLocalUserPrimaryGroup = _EqlApplianceLocalUserPrimaryGroup_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 18, 1, 5),
    _EqlApplianceLocalUserPrimaryGroup_Type()
)
eqlApplianceLocalUserPrimaryGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLocalUserPrimaryGroup.setStatus("current")


class _EqlApplianceLocalUserRealName_Type(OctetString):
    """Custom type eqlApplianceLocalUserRealName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlApplianceLocalUserRealName_Type.__name__ = "OctetString"
_EqlApplianceLocalUserRealName_Object = MibTableColumn
eqlApplianceLocalUserRealName = _EqlApplianceLocalUserRealName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 18, 1, 6),
    _EqlApplianceLocalUserRealName_Type()
)
eqlApplianceLocalUserRealName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLocalUserRealName.setStatus("current")


class _EqlApplianceLocalUserSid_Type(OctetString):
    """Custom type eqlApplianceLocalUserSid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceLocalUserSid_Type.__name__ = "OctetString"
_EqlApplianceLocalUserSid_Object = MibTableColumn
eqlApplianceLocalUserSid = _EqlApplianceLocalUserSid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 18, 1, 7),
    _EqlApplianceLocalUserSid_Type()
)
eqlApplianceLocalUserSid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLocalUserSid.setStatus("deprecated")


class _EqlApplianceLocalUserRemarks_Type(OctetString):
    """Custom type eqlApplianceLocalUserRemarks based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceLocalUserRemarks_Type.__name__ = "OctetString"
_EqlApplianceLocalUserRemarks_Object = MibTableColumn
eqlApplianceLocalUserRemarks = _EqlApplianceLocalUserRemarks_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 18, 1, 8),
    _EqlApplianceLocalUserRemarks_Type()
)
eqlApplianceLocalUserRemarks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLocalUserRemarks.setStatus("current")


class _EqlApplianceLocalUserAdditionalGroups_Type(OctetString):
    """Custom type eqlApplianceLocalUserAdditionalGroups based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1023),
    )


_EqlApplianceLocalUserAdditionalGroups_Type.__name__ = "OctetString"
_EqlApplianceLocalUserAdditionalGroups_Object = MibTableColumn
eqlApplianceLocalUserAdditionalGroups = _EqlApplianceLocalUserAdditionalGroups_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 18, 1, 9),
    _EqlApplianceLocalUserAdditionalGroups_Type()
)
eqlApplianceLocalUserAdditionalGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLocalUserAdditionalGroups.setStatus("current")


class _EqlApplianceLocalUserAccess_Type(Integer32):
    """Custom type eqlApplianceLocalUserAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_EqlApplianceLocalUserAccess_Type.__name__ = "Integer32"
_EqlApplianceLocalUserAccess_Object = MibTableColumn
eqlApplianceLocalUserAccess = _EqlApplianceLocalUserAccess_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 18, 1, 10),
    _EqlApplianceLocalUserAccess_Type()
)
eqlApplianceLocalUserAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlApplianceLocalUserAccess.setStatus("current")
_EqlApplianceLocalGroupAccessTable_Object = MibTable
eqlApplianceLocalGroupAccessTable = _EqlApplianceLocalGroupAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 19)
)
if mibBuilder.loadTexts:
    eqlApplianceLocalGroupAccessTable.setStatus("current")
_EqlApplianceLocalGroupAccessEntry_Object = MibTableRow
eqlApplianceLocalGroupAccessEntry = _EqlApplianceLocalGroupAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 19, 1)
)
eqlApplianceLocalGroupAccessEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceLocalGroupName"),
)
if mibBuilder.loadTexts:
    eqlApplianceLocalGroupAccessEntry.setStatus("current")
_EqlApplianceLocalGroupAccessRowStatus_Type = RowStatus
_EqlApplianceLocalGroupAccessRowStatus_Object = MibTableColumn
eqlApplianceLocalGroupAccessRowStatus = _EqlApplianceLocalGroupAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 19, 1, 1),
    _EqlApplianceLocalGroupAccessRowStatus_Type()
)
eqlApplianceLocalGroupAccessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLocalGroupAccessRowStatus.setStatus("current")


class _EqlApplianceLocalGroupName_Type(OctetString):
    """Custom type eqlApplianceLocalGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceLocalGroupName_Type.__name__ = "OctetString"
_EqlApplianceLocalGroupName_Object = MibTableColumn
eqlApplianceLocalGroupName = _EqlApplianceLocalGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 19, 1, 2),
    _EqlApplianceLocalGroupName_Type()
)
eqlApplianceLocalGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLocalGroupName.setStatus("current")
_EqlApplianceLocalGroupGid_Type = Unsigned32
_EqlApplianceLocalGroupGid_Object = MibTableColumn
eqlApplianceLocalGroupGid = _EqlApplianceLocalGroupGid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 19, 1, 3),
    _EqlApplianceLocalGroupGid_Type()
)
eqlApplianceLocalGroupGid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLocalGroupGid.setStatus("current")


class _EqlApplianceLocalGroupGsid_Type(OctetString):
    """Custom type eqlApplianceLocalGroupGsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceLocalGroupGsid_Type.__name__ = "OctetString"
_EqlApplianceLocalGroupGsid_Object = MibTableColumn
eqlApplianceLocalGroupGsid = _EqlApplianceLocalGroupGsid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 19, 1, 4),
    _EqlApplianceLocalGroupGsid_Type()
)
eqlApplianceLocalGroupGsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLocalGroupGsid.setStatus("current")
_EqlApplianceCredentialsDatabaseTable_Object = MibTable
eqlApplianceCredentialsDatabaseTable = _EqlApplianceCredentialsDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 20)
)
if mibBuilder.loadTexts:
    eqlApplianceCredentialsDatabaseTable.setStatus("current")
_EqlApplianceCredentialsDatabaseEntry_Object = MibTableRow
eqlApplianceCredentialsDatabaseEntry = _EqlApplianceCredentialsDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 20, 1)
)
eqlApplianceCredentialsDatabaseEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceCredentialsDatabaseEntry.setStatus("current")
_EqlApplianceCredentialsDatabaseRowStatus_Type = RowStatus
_EqlApplianceCredentialsDatabaseRowStatus_Object = MibTableColumn
eqlApplianceCredentialsDatabaseRowStatus = _EqlApplianceCredentialsDatabaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 20, 1, 1),
    _EqlApplianceCredentialsDatabaseRowStatus_Type()
)
eqlApplianceCredentialsDatabaseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceCredentialsDatabaseRowStatus.setStatus("current")


class _EqlApplianceCredentialsDatabaseType_Type(Integer32):
    """Custom type eqlApplianceCredentialsDatabaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ldap", 1),
          ("nis", 2),
          ("noexternal", 0),
          ("unknown", 3))
    )


_EqlApplianceCredentialsDatabaseType_Type.__name__ = "Integer32"
_EqlApplianceCredentialsDatabaseType_Object = MibTableColumn
eqlApplianceCredentialsDatabaseType = _EqlApplianceCredentialsDatabaseType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 20, 1, 2),
    _EqlApplianceCredentialsDatabaseType_Type()
)
eqlApplianceCredentialsDatabaseType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceCredentialsDatabaseType.setStatus("current")


class _EqlApplianceCredentialsDatabaseLdapBaseDn_Type(OctetString):
    """Custom type eqlApplianceCredentialsDatabaseLdapBaseDn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EqlApplianceCredentialsDatabaseLdapBaseDn_Type.__name__ = "OctetString"
_EqlApplianceCredentialsDatabaseLdapBaseDn_Object = MibTableColumn
eqlApplianceCredentialsDatabaseLdapBaseDn = _EqlApplianceCredentialsDatabaseLdapBaseDn_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 20, 1, 3),
    _EqlApplianceCredentialsDatabaseLdapBaseDn_Type()
)
eqlApplianceCredentialsDatabaseLdapBaseDn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceCredentialsDatabaseLdapBaseDn.setStatus("current")


class _EqlApplianceCredentialsDatabaseLdapServerAddress_Type(OctetString):
    """Custom type eqlApplianceCredentialsDatabaseLdapServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceCredentialsDatabaseLdapServerAddress_Type.__name__ = "OctetString"
_EqlApplianceCredentialsDatabaseLdapServerAddress_Object = MibTableColumn
eqlApplianceCredentialsDatabaseLdapServerAddress = _EqlApplianceCredentialsDatabaseLdapServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 20, 1, 4),
    _EqlApplianceCredentialsDatabaseLdapServerAddress_Type()
)
eqlApplianceCredentialsDatabaseLdapServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceCredentialsDatabaseLdapServerAddress.setStatus("current")


class _EqlApplianceCredentialsDatabaseNisDomain_Type(OctetString):
    """Custom type eqlApplianceCredentialsDatabaseNisDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceCredentialsDatabaseNisDomain_Type.__name__ = "OctetString"
_EqlApplianceCredentialsDatabaseNisDomain_Object = MibTableColumn
eqlApplianceCredentialsDatabaseNisDomain = _EqlApplianceCredentialsDatabaseNisDomain_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 20, 1, 5),
    _EqlApplianceCredentialsDatabaseNisDomain_Type()
)
eqlApplianceCredentialsDatabaseNisDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceCredentialsDatabaseNisDomain.setStatus("current")


class _EqlApplianceCredentialsDatabaseNisServerAddress_Type(OctetString):
    """Custom type eqlApplianceCredentialsDatabaseNisServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_EqlApplianceCredentialsDatabaseNisServerAddress_Type.__name__ = "OctetString"
_EqlApplianceCredentialsDatabaseNisServerAddress_Object = MibTableColumn
eqlApplianceCredentialsDatabaseNisServerAddress = _EqlApplianceCredentialsDatabaseNisServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 20, 1, 6),
    _EqlApplianceCredentialsDatabaseNisServerAddress_Type()
)
eqlApplianceCredentialsDatabaseNisServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceCredentialsDatabaseNisServerAddress.setStatus("current")
_EqlApplianceActiveDirectoryAccessTable_Object = MibTable
eqlApplianceActiveDirectoryAccessTable = _EqlApplianceActiveDirectoryAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21)
)
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryAccessTable.setStatus("current")
_EqlApplianceActiveDirectoryAccessEntry_Object = MibTableRow
eqlApplianceActiveDirectoryAccessEntry = _EqlApplianceActiveDirectoryAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1)
)
eqlApplianceActiveDirectoryAccessEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryAccessEntry.setStatus("current")
_EqlApplianceActiveDirectoryRowStatus_Type = RowStatus
_EqlApplianceActiveDirectoryRowStatus_Object = MibTableColumn
eqlApplianceActiveDirectoryRowStatus = _EqlApplianceActiveDirectoryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 1),
    _EqlApplianceActiveDirectoryRowStatus_Type()
)
eqlApplianceActiveDirectoryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryRowStatus.setStatus("current")


class _EqlApplianceActiveDirectoryAdvancedSettings_Type(Integer32):
    """Custom type eqlApplianceActiveDirectoryAdvancedSettings based on Integer32"""
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
        *(("no", 1),
          ("unused", 0),
          ("yes", 2))
    )


_EqlApplianceActiveDirectoryAdvancedSettings_Type.__name__ = "Integer32"
_EqlApplianceActiveDirectoryAdvancedSettings_Object = MibTableColumn
eqlApplianceActiveDirectoryAdvancedSettings = _EqlApplianceActiveDirectoryAdvancedSettings_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 2),
    _EqlApplianceActiveDirectoryAdvancedSettings_Type()
)
eqlApplianceActiveDirectoryAdvancedSettings.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryAdvancedSettings.setStatus("current")


class _EqlApplianceActiveDirectoryNetBiosName_Type(OctetString):
    """Custom type eqlApplianceActiveDirectoryNetBiosName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceActiveDirectoryNetBiosName_Type.__name__ = "OctetString"
_EqlApplianceActiveDirectoryNetBiosName_Object = MibTableColumn
eqlApplianceActiveDirectoryNetBiosName = _EqlApplianceActiveDirectoryNetBiosName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 3),
    _EqlApplianceActiveDirectoryNetBiosName_Type()
)
eqlApplianceActiveDirectoryNetBiosName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryNetBiosName.setStatus("current")


class _EqlApplianceActiveDirectoryDomain_Type(OctetString):
    """Custom type eqlApplianceActiveDirectoryDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceActiveDirectoryDomain_Type.__name__ = "OctetString"
_EqlApplianceActiveDirectoryDomain_Object = MibTableColumn
eqlApplianceActiveDirectoryDomain = _EqlApplianceActiveDirectoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 4),
    _EqlApplianceActiveDirectoryDomain_Type()
)
eqlApplianceActiveDirectoryDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryDomain.setStatus("current")


class _EqlApplianceActiveDirectoryUserName_Type(OctetString):
    """Custom type eqlApplianceActiveDirectoryUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceActiveDirectoryUserName_Type.__name__ = "OctetString"
_EqlApplianceActiveDirectoryUserName_Object = MibTableColumn
eqlApplianceActiveDirectoryUserName = _EqlApplianceActiveDirectoryUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 5),
    _EqlApplianceActiveDirectoryUserName_Type()
)
eqlApplianceActiveDirectoryUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryUserName.setStatus("current")


class _EqlApplianceActiveDirectoryPassword_Type(OctetString):
    """Custom type eqlApplianceActiveDirectoryPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceActiveDirectoryPassword_Type.__name__ = "OctetString"
_EqlApplianceActiveDirectoryPassword_Object = MibTableColumn
eqlApplianceActiveDirectoryPassword = _EqlApplianceActiveDirectoryPassword_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 6),
    _EqlApplianceActiveDirectoryPassword_Type()
)
eqlApplianceActiveDirectoryPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryPassword.setStatus("current")


class _EqlApplianceActiveDirectoryDescription_Type(OctetString):
    """Custom type eqlApplianceActiveDirectoryDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1023),
    )


_EqlApplianceActiveDirectoryDescription_Type.__name__ = "OctetString"
_EqlApplianceActiveDirectoryDescription_Object = MibTableColumn
eqlApplianceActiveDirectoryDescription = _EqlApplianceActiveDirectoryDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 7),
    _EqlApplianceActiveDirectoryDescription_Type()
)
eqlApplianceActiveDirectoryDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryDescription.setStatus("current")


class _EqlApplianceActiveDirectoryFunctionalLevel_Type(OctetString):
    """Custom type eqlApplianceActiveDirectoryFunctionalLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_EqlApplianceActiveDirectoryFunctionalLevel_Type.__name__ = "OctetString"
_EqlApplianceActiveDirectoryFunctionalLevel_Object = MibTableColumn
eqlApplianceActiveDirectoryFunctionalLevel = _EqlApplianceActiveDirectoryFunctionalLevel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 8),
    _EqlApplianceActiveDirectoryFunctionalLevel_Type()
)
eqlApplianceActiveDirectoryFunctionalLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryFunctionalLevel.setStatus("current")


class _EqlApplianceActiveDirectoryWinsServer_Type(OctetString):
    """Custom type eqlApplianceActiveDirectoryWinsServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceActiveDirectoryWinsServer_Type.__name__ = "OctetString"
_EqlApplianceActiveDirectoryWinsServer_Object = MibTableColumn
eqlApplianceActiveDirectoryWinsServer = _EqlApplianceActiveDirectoryWinsServer_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 9),
    _EqlApplianceActiveDirectoryWinsServer_Type()
)
eqlApplianceActiveDirectoryWinsServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryWinsServer.setStatus("current")


class _EqlApplianceActiveDirectoryWorkGroup_Type(OctetString):
    """Custom type eqlApplianceActiveDirectoryWorkGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceActiveDirectoryWorkGroup_Type.__name__ = "OctetString"
_EqlApplianceActiveDirectoryWorkGroup_Object = MibTableColumn
eqlApplianceActiveDirectoryWorkGroup = _EqlApplianceActiveDirectoryWorkGroup_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 10),
    _EqlApplianceActiveDirectoryWorkGroup_Type()
)
eqlApplianceActiveDirectoryWorkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryWorkGroup.setStatus("current")


class _EqlApplianceActiveDirectoryDomainControllers_Type(OctetString):
    """Custom type eqlApplianceActiveDirectoryDomainControllers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlApplianceActiveDirectoryDomainControllers_Type.__name__ = "OctetString"
_EqlApplianceActiveDirectoryDomainControllers_Object = MibTableColumn
eqlApplianceActiveDirectoryDomainControllers = _EqlApplianceActiveDirectoryDomainControllers_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 11),
    _EqlApplianceActiveDirectoryDomainControllers_Type()
)
eqlApplianceActiveDirectoryDomainControllers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryDomainControllers.setStatus("current")


class _EqlApplianceActiveDirectoryMemberOfDomain_Type(OctetString):
    """Custom type eqlApplianceActiveDirectoryMemberOfDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_EqlApplianceActiveDirectoryMemberOfDomain_Type.__name__ = "OctetString"
_EqlApplianceActiveDirectoryMemberOfDomain_Object = MibTableColumn
eqlApplianceActiveDirectoryMemberOfDomain = _EqlApplianceActiveDirectoryMemberOfDomain_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 12),
    _EqlApplianceActiveDirectoryMemberOfDomain_Type()
)
eqlApplianceActiveDirectoryMemberOfDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryMemberOfDomain.setStatus("current")


class _EqlApplianceActiveDirectoryStatus_Type(Integer32):
    """Custom type eqlApplianceActiveDirectoryStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("unused", 0))
    )


_EqlApplianceActiveDirectoryStatus_Type.__name__ = "Integer32"
_EqlApplianceActiveDirectoryStatus_Object = MibTableColumn
eqlApplianceActiveDirectoryStatus = _EqlApplianceActiveDirectoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 13),
    _EqlApplianceActiveDirectoryStatus_Type()
)
eqlApplianceActiveDirectoryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryStatus.setStatus("current")


class _EqlApplianceActiveDirectoryAccessibleControllers_Type(OctetString):
    """Custom type eqlApplianceActiveDirectoryAccessibleControllers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlApplianceActiveDirectoryAccessibleControllers_Type.__name__ = "OctetString"
_EqlApplianceActiveDirectoryAccessibleControllers_Object = MibTableColumn
eqlApplianceActiveDirectoryAccessibleControllers = _EqlApplianceActiveDirectoryAccessibleControllers_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 14),
    _EqlApplianceActiveDirectoryAccessibleControllers_Type()
)
eqlApplianceActiveDirectoryAccessibleControllers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryAccessibleControllers.setStatus("current")


class _EqlApplianceActiveDirectoryPreferredControllers_Type(OctetString):
    """Custom type eqlApplianceActiveDirectoryPreferredControllers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlApplianceActiveDirectoryPreferredControllers_Type.__name__ = "OctetString"
_EqlApplianceActiveDirectoryPreferredControllers_Object = MibTableColumn
eqlApplianceActiveDirectoryPreferredControllers = _EqlApplianceActiveDirectoryPreferredControllers_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 21, 1, 15),
    _EqlApplianceActiveDirectoryPreferredControllers_Type()
)
eqlApplianceActiveDirectoryPreferredControllers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceActiveDirectoryPreferredControllers.setStatus("current")
_EqlApplianceManualMappingTable_Object = MibTable
eqlApplianceManualMappingTable = _EqlApplianceManualMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 22)
)
if mibBuilder.loadTexts:
    eqlApplianceManualMappingTable.setStatus("current")
_EqlApplianceManualMappingEntry_Object = MibTableRow
eqlApplianceManualMappingEntry = _EqlApplianceManualMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 22, 1)
)
eqlApplianceManualMappingEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceManualMappingUserName"),
)
if mibBuilder.loadTexts:
    eqlApplianceManualMappingEntry.setStatus("current")
_EqlApplianceManualMappingRowStatus_Type = RowStatus
_EqlApplianceManualMappingRowStatus_Object = MibTableColumn
eqlApplianceManualMappingRowStatus = _EqlApplianceManualMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 22, 1, 1),
    _EqlApplianceManualMappingRowStatus_Type()
)
eqlApplianceManualMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceManualMappingRowStatus.setStatus("current")


class _EqlApplianceManualMappingUserName_Type(OctetString):
    """Custom type eqlApplianceManualMappingUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlApplianceManualMappingUserName_Type.__name__ = "OctetString"
_EqlApplianceManualMappingUserName_Object = MibTableColumn
eqlApplianceManualMappingUserName = _EqlApplianceManualMappingUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 22, 1, 2),
    _EqlApplianceManualMappingUserName_Type()
)
eqlApplianceManualMappingUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceManualMappingUserName.setStatus("current")


class _EqlApplianceManualMappingMappedToUserName_Type(OctetString):
    """Custom type eqlApplianceManualMappingMappedToUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlApplianceManualMappingMappedToUserName_Type.__name__ = "OctetString"
_EqlApplianceManualMappingMappedToUserName_Object = MibTableColumn
eqlApplianceManualMappingMappedToUserName = _EqlApplianceManualMappingMappedToUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 22, 1, 3),
    _EqlApplianceManualMappingMappedToUserName_Type()
)
eqlApplianceManualMappingMappedToUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceManualMappingMappedToUserName.setStatus("current")


class _EqlApplianceManualMappingDirection_Type(Integer32):
    """Custom type eqlApplianceManualMappingDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unixtowindows", 2),
          ("unused", 0),
          ("windowstounix", 3))
    )


_EqlApplianceManualMappingDirection_Type.__name__ = "Integer32"
_EqlApplianceManualMappingDirection_Object = MibTableColumn
eqlApplianceManualMappingDirection = _EqlApplianceManualMappingDirection_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 22, 1, 4),
    _EqlApplianceManualMappingDirection_Type()
)
eqlApplianceManualMappingDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceManualMappingDirection.setStatus("current")
_EqlApplianceMappingPolicyTable_Object = MibTable
eqlApplianceMappingPolicyTable = _EqlApplianceMappingPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 23)
)
if mibBuilder.loadTexts:
    eqlApplianceMappingPolicyTable.setStatus("current")
_EqlApplianceMappingPolicyEntry_Object = MibTableRow
eqlApplianceMappingPolicyEntry = _EqlApplianceMappingPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 23, 1)
)
eqlApplianceMappingPolicyEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceMappingPolicyEntry.setStatus("current")
_EqlApplianceMappingPolicyRowStatus_Type = RowStatus
_EqlApplianceMappingPolicyRowStatus_Object = MibTableColumn
eqlApplianceMappingPolicyRowStatus = _EqlApplianceMappingPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 23, 1, 1),
    _EqlApplianceMappingPolicyRowStatus_Type()
)
eqlApplianceMappingPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMappingPolicyRowStatus.setStatus("current")


class _EqlApplianceMappingPolicyAcquireMapping_Type(Integer32):
    """Custom type eqlApplianceMappingPolicyAcquireMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("unused", 0))
    )


_EqlApplianceMappingPolicyAcquireMapping_Type.__name__ = "Integer32"
_EqlApplianceMappingPolicyAcquireMapping_Object = MibTableColumn
eqlApplianceMappingPolicyAcquireMapping = _EqlApplianceMappingPolicyAcquireMapping_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 23, 1, 2),
    _EqlApplianceMappingPolicyAcquireMapping_Type()
)
eqlApplianceMappingPolicyAcquireMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMappingPolicyAcquireMapping.setStatus("current")


class _EqlApplianceMappingPolicyAllowNotMapped_Type(Integer32):
    """Custom type eqlApplianceMappingPolicyAllowNotMapped based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("unused", 0))
    )


_EqlApplianceMappingPolicyAllowNotMapped_Type.__name__ = "Integer32"
_EqlApplianceMappingPolicyAllowNotMapped_Object = MibTableColumn
eqlApplianceMappingPolicyAllowNotMapped = _EqlApplianceMappingPolicyAllowNotMapped_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 23, 1, 3),
    _EqlApplianceMappingPolicyAllowNotMapped_Type()
)
eqlApplianceMappingPolicyAllowNotMapped.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceMappingPolicyAllowNotMapped.setStatus("deprecated")
_EqlApplianceAllGroupsTable_Object = MibTable
eqlApplianceAllGroupsTable = _EqlApplianceAllGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 24)
)
if mibBuilder.loadTexts:
    eqlApplianceAllGroupsTable.setStatus("current")
_EqlApplianceAllGroupsEntry_Object = MibTableRow
eqlApplianceAllGroupsEntry = _EqlApplianceAllGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 24, 1)
)
eqlApplianceAllGroupsEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceAllGroupsName"),
)
if mibBuilder.loadTexts:
    eqlApplianceAllGroupsEntry.setStatus("current")
_EqlApplianceAllGroupsRowStatus_Type = RowStatus
_EqlApplianceAllGroupsRowStatus_Object = MibTableColumn
eqlApplianceAllGroupsRowStatus = _EqlApplianceAllGroupsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 24, 1, 1),
    _EqlApplianceAllGroupsRowStatus_Type()
)
eqlApplianceAllGroupsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAllGroupsRowStatus.setStatus("current")


class _EqlApplianceAllGroupsName_Type(OctetString):
    """Custom type eqlApplianceAllGroupsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlApplianceAllGroupsName_Type.__name__ = "OctetString"
_EqlApplianceAllGroupsName_Object = MibTableColumn
eqlApplianceAllGroupsName = _EqlApplianceAllGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 24, 1, 2),
    _EqlApplianceAllGroupsName_Type()
)
eqlApplianceAllGroupsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAllGroupsName.setStatus("current")


class _EqlApplianceAllGroupsId_Type(OctetString):
    """Custom type eqlApplianceAllGroupsId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceAllGroupsId_Type.__name__ = "OctetString"
_EqlApplianceAllGroupsId_Object = MibTableColumn
eqlApplianceAllGroupsId = _EqlApplianceAllGroupsId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 24, 1, 3),
    _EqlApplianceAllGroupsId_Type()
)
eqlApplianceAllGroupsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAllGroupsId.setStatus("current")


class _EqlApplianceAllGroupsType_Type(Integer32):
    """Custom type eqlApplianceAllGroupsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ad", 1),
          ("unix", 2),
          ("unused", 0))
    )


_EqlApplianceAllGroupsType_Type.__name__ = "Integer32"
_EqlApplianceAllGroupsType_Object = MibTableColumn
eqlApplianceAllGroupsType = _EqlApplianceAllGroupsType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 24, 1, 4),
    _EqlApplianceAllGroupsType_Type()
)
eqlApplianceAllGroupsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAllGroupsType.setStatus("current")


class _EqlApplianceAllGroupsSource_Type(Integer32):
    """Custom type eqlApplianceAllGroupsSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("local", 1),
          ("unused", 0))
    )


_EqlApplianceAllGroupsSource_Type.__name__ = "Integer32"
_EqlApplianceAllGroupsSource_Object = MibTableColumn
eqlApplianceAllGroupsSource = _EqlApplianceAllGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 24, 1, 5),
    _EqlApplianceAllGroupsSource_Type()
)
eqlApplianceAllGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAllGroupsSource.setStatus("current")
_EqlApplianceAllUsersTable_Object = MibTable
eqlApplianceAllUsersTable = _EqlApplianceAllUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 25)
)
if mibBuilder.loadTexts:
    eqlApplianceAllUsersTable.setStatus("current")
_EqlApplianceAllUsersEntry_Object = MibTableRow
eqlApplianceAllUsersEntry = _EqlApplianceAllUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 25, 1)
)
eqlApplianceAllUsersEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceAllUsersName"),
)
if mibBuilder.loadTexts:
    eqlApplianceAllUsersEntry.setStatus("current")
_EqlApplianceAllUsersRowStatus_Type = RowStatus
_EqlApplianceAllUsersRowStatus_Object = MibTableColumn
eqlApplianceAllUsersRowStatus = _EqlApplianceAllUsersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 25, 1, 1),
    _EqlApplianceAllUsersRowStatus_Type()
)
eqlApplianceAllUsersRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAllUsersRowStatus.setStatus("current")


class _EqlApplianceAllUsersName_Type(OctetString):
    """Custom type eqlApplianceAllUsersName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlApplianceAllUsersName_Type.__name__ = "OctetString"
_EqlApplianceAllUsersName_Object = MibTableColumn
eqlApplianceAllUsersName = _EqlApplianceAllUsersName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 25, 1, 2),
    _EqlApplianceAllUsersName_Type()
)
eqlApplianceAllUsersName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAllUsersName.setStatus("current")


class _EqlApplianceAllUsersId_Type(OctetString):
    """Custom type eqlApplianceAllUsersId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceAllUsersId_Type.__name__ = "OctetString"
_EqlApplianceAllUsersId_Object = MibTableColumn
eqlApplianceAllUsersId = _EqlApplianceAllUsersId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 25, 1, 3),
    _EqlApplianceAllUsersId_Type()
)
eqlApplianceAllUsersId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAllUsersId.setStatus("current")


class _EqlApplianceAllUsersType_Type(Integer32):
    """Custom type eqlApplianceAllUsersType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ad", 1),
          ("unix", 2),
          ("unused", 0))
    )


_EqlApplianceAllUsersType_Type.__name__ = "Integer32"
_EqlApplianceAllUsersType_Object = MibTableColumn
eqlApplianceAllUsersType = _EqlApplianceAllUsersType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 25, 1, 4),
    _EqlApplianceAllUsersType_Type()
)
eqlApplianceAllUsersType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAllUsersType.setStatus("current")


class _EqlApplianceAllUsersSource_Type(Integer32):
    """Custom type eqlApplianceAllUsersSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("local", 1),
          ("unused", 0))
    )


_EqlApplianceAllUsersSource_Type.__name__ = "Integer32"
_EqlApplianceAllUsersSource_Object = MibTableColumn
eqlApplianceAllUsersSource = _EqlApplianceAllUsersSource_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 25, 1, 5),
    _EqlApplianceAllUsersSource_Type()
)
eqlApplianceAllUsersSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAllUsersSource.setStatus("current")
_EqlApplianceEQLMemberMPVTable_Object = MibTable
eqlApplianceEQLMemberMPVTable = _EqlApplianceEQLMemberMPVTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 26)
)
if mibBuilder.loadTexts:
    eqlApplianceEQLMemberMPVTable.setStatus("deprecated")
_EqlApplianceEQLMemberMPVEntry_Object = MibTableRow
eqlApplianceEQLMemberMPVEntry = _EqlApplianceEQLMemberMPVEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 26, 1)
)
eqlApplianceEQLMemberMPVEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceEQLMemberMPVEntry.setStatus("deprecated")
_EqlApplianceEQLMemberMPV_Type = Unsigned32
_EqlApplianceEQLMemberMPV_Object = MibTableColumn
eqlApplianceEQLMemberMPV = _EqlApplianceEQLMemberMPV_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 26, 1, 1),
    _EqlApplianceEQLMemberMPV_Type()
)
eqlApplianceEQLMemberMPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceEQLMemberMPV.setStatus("deprecated")
_EqlApplianceMPVTable_Object = MibTable
eqlApplianceMPVTable = _EqlApplianceMPVTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 27)
)
if mibBuilder.loadTexts:
    eqlApplianceMPVTable.setStatus("current")
_EqlApplianceMPVEntry_Object = MibTableRow
eqlApplianceMPVEntry = _EqlApplianceMPVEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 27, 1)
)
eqlApplianceMPVEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceMPVEntry.setStatus("current")
_EqlApplianceEQLGroupMPV_Type = Unsigned32
_EqlApplianceEQLGroupMPV_Object = MibTableColumn
eqlApplianceEQLGroupMPV = _EqlApplianceEQLGroupMPV_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 27, 1, 1),
    _EqlApplianceEQLGroupMPV_Type()
)
eqlApplianceEQLGroupMPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceEQLGroupMPV.setStatus("current")
_EqlApplianceClusterMPV_Type = Unsigned32
_EqlApplianceClusterMPV_Object = MibTableColumn
eqlApplianceClusterMPV = _EqlApplianceClusterMPV_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 27, 1, 2),
    _EqlApplianceClusterMPV_Type()
)
eqlApplianceClusterMPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceClusterMPV.setStatus("current")
_EqlApplianceClusterMajorVersion_Type = Unsigned32
_EqlApplianceClusterMajorVersion_Object = MibTableColumn
eqlApplianceClusterMajorVersion = _EqlApplianceClusterMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 27, 1, 3),
    _EqlApplianceClusterMajorVersion_Type()
)
eqlApplianceClusterMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceClusterMajorVersion.setStatus("current")
_EqlApplianceClusterMinorVersion_Type = Unsigned32
_EqlApplianceClusterMinorVersion_Object = MibTableColumn
eqlApplianceClusterMinorVersion = _EqlApplianceClusterMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 27, 1, 4),
    _EqlApplianceClusterMinorVersion_Type()
)
eqlApplianceClusterMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceClusterMinorVersion.setStatus("current")
_EqlApplianceClusterMaintVersion_Type = Unsigned32
_EqlApplianceClusterMaintVersion_Object = MibTableColumn
eqlApplianceClusterMaintVersion = _EqlApplianceClusterMaintVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 27, 1, 5),
    _EqlApplianceClusterMaintVersion_Type()
)
eqlApplianceClusterMaintVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceClusterMaintVersion.setStatus("current")
_EqlApplianceSyncedDataTable_Object = MibTable
eqlApplianceSyncedDataTable = _EqlApplianceSyncedDataTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 28)
)
if mibBuilder.loadTexts:
    eqlApplianceSyncedDataTable.setStatus("current")
_EqlApplianceSyncedDataEntry_Object = MibTableRow
eqlApplianceSyncedDataEntry = _EqlApplianceSyncedDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 28, 1)
)
eqlApplianceSyncedDataEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceSyncedDataType"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceSyncedDataIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceSyncedDataEntry.setStatus("current")
_EqlApplianceSyncedDataRowStatus_Type = RowStatus
_EqlApplianceSyncedDataRowStatus_Object = MibTableColumn
eqlApplianceSyncedDataRowStatus = _EqlApplianceSyncedDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 28, 1, 1),
    _EqlApplianceSyncedDataRowStatus_Type()
)
eqlApplianceSyncedDataRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceSyncedDataRowStatus.setStatus("current")


class _EqlApplianceSyncedDataType_Type(Integer32):
    """Custom type eqlApplianceSyncedDataType based on Integer32"""
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
        *(("cluster-san-vip", 6),
          ("grpadminpswd", 1),
          ("grpip", 2),
          ("timezone", 3),
          ("trapcommunity", 5),
          ("traprecipient", 4))
    )


_EqlApplianceSyncedDataType_Type.__name__ = "Integer32"
_EqlApplianceSyncedDataType_Object = MibTableColumn
eqlApplianceSyncedDataType = _EqlApplianceSyncedDataType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 28, 1, 2),
    _EqlApplianceSyncedDataType_Type()
)
eqlApplianceSyncedDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceSyncedDataType.setStatus("current")
_EqlApplianceSyncedDataIndex_Type = Unsigned32
_EqlApplianceSyncedDataIndex_Object = MibTableColumn
eqlApplianceSyncedDataIndex = _EqlApplianceSyncedDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 28, 1, 3),
    _EqlApplianceSyncedDataIndex_Type()
)
eqlApplianceSyncedDataIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceSyncedDataIndex.setStatus("current")


class _EqlApplianceSyncedDataIndexPayload_Type(OctetString):
    """Custom type eqlApplianceSyncedDataIndexPayload based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1500),
    )


_EqlApplianceSyncedDataIndexPayload_Type.__name__ = "OctetString"
_EqlApplianceSyncedDataIndexPayload_Object = MibTableColumn
eqlApplianceSyncedDataIndexPayload = _EqlApplianceSyncedDataIndexPayload_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 28, 1, 4),
    _EqlApplianceSyncedDataIndexPayload_Type()
)
eqlApplianceSyncedDataIndexPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceSyncedDataIndexPayload.setStatus("current")


class _EqlApplianceSyncedDataEntryPayload_Type(OctetString):
    """Custom type eqlApplianceSyncedDataEntryPayload based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1500),
    )


_EqlApplianceSyncedDataEntryPayload_Type.__name__ = "OctetString"
_EqlApplianceSyncedDataEntryPayload_Object = MibTableColumn
eqlApplianceSyncedDataEntryPayload = _EqlApplianceSyncedDataEntryPayload_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 28, 1, 5),
    _EqlApplianceSyncedDataEntryPayload_Type()
)
eqlApplianceSyncedDataEntryPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceSyncedDataEntryPayload.setStatus("current")


class _EqlApplianceSyncedDataState_Type(Integer32):
    """Custom type eqlApplianceSyncedDataState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sync-initiated", 1),
          ("sync-pending", 0),
          ("synced", 2))
    )


_EqlApplianceSyncedDataState_Type.__name__ = "Integer32"
_EqlApplianceSyncedDataState_Object = MibTableColumn
eqlApplianceSyncedDataState = _EqlApplianceSyncedDataState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 28, 1, 6),
    _EqlApplianceSyncedDataState_Type()
)
eqlApplianceSyncedDataState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceSyncedDataState.setStatus("current")
_EqlApplianceCIFSProtocolTable_Object = MibTable
eqlApplianceCIFSProtocolTable = _EqlApplianceCIFSProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 29)
)
if mibBuilder.loadTexts:
    eqlApplianceCIFSProtocolTable.setStatus("current")
_EqlApplianceCIFSProtocolEntry_Object = MibTableRow
eqlApplianceCIFSProtocolEntry = _EqlApplianceCIFSProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 29, 1)
)
eqlApplianceCIFSProtocolEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceCIFSProtocolEntry.setStatus("current")
_EqlApplianceCIFSProtocolRowStatus_Type = RowStatus
_EqlApplianceCIFSProtocolRowStatus_Object = MibTableColumn
eqlApplianceCIFSProtocolRowStatus = _EqlApplianceCIFSProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 29, 1, 1),
    _EqlApplianceCIFSProtocolRowStatus_Type()
)
eqlApplianceCIFSProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceCIFSProtocolRowStatus.setStatus("current")
_EqlApplianceCIFSProtocolAuthenticationEnabled_Type = TruthValue
_EqlApplianceCIFSProtocolAuthenticationEnabled_Object = MibTableColumn
eqlApplianceCIFSProtocolAuthenticationEnabled = _EqlApplianceCIFSProtocolAuthenticationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 29, 1, 2),
    _EqlApplianceCIFSProtocolAuthenticationEnabled_Type()
)
eqlApplianceCIFSProtocolAuthenticationEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceCIFSProtocolAuthenticationEnabled.setStatus("current")


class _EqlApplianceCIFSProtocolAuthenticationType_Type(Integer32):
    """Custom type eqlApplianceCIFSProtocolAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activedirectory", 1),
          ("guestsonly", 3),
          ("localuser", 2),
          ("unused", 0))
    )


_EqlApplianceCIFSProtocolAuthenticationType_Type.__name__ = "Integer32"
_EqlApplianceCIFSProtocolAuthenticationType_Object = MibTableColumn
eqlApplianceCIFSProtocolAuthenticationType = _EqlApplianceCIFSProtocolAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 29, 1, 3),
    _EqlApplianceCIFSProtocolAuthenticationType_Type()
)
eqlApplianceCIFSProtocolAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceCIFSProtocolAuthenticationType.setStatus("current")


class _EqlApplianceCIFSProtocolAllowGuests_Type(TruthValue):
    """Custom type eqlApplianceCIFSProtocolAllowGuests based on TruthValue"""


_EqlApplianceCIFSProtocolAllowGuests_Object = MibTableColumn
eqlApplianceCIFSProtocolAllowGuests = _EqlApplianceCIFSProtocolAllowGuests_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 29, 1, 4),
    _EqlApplianceCIFSProtocolAllowGuests_Type()
)
eqlApplianceCIFSProtocolAllowGuests.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceCIFSProtocolAllowGuests.setStatus("deprecated")
_EqlApplianceCIFSProtocolMaxConnections_Type = Unsigned32
_EqlApplianceCIFSProtocolMaxConnections_Object = MibTableColumn
eqlApplianceCIFSProtocolMaxConnections = _EqlApplianceCIFSProtocolMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 29, 1, 5),
    _EqlApplianceCIFSProtocolMaxConnections_Type()
)
eqlApplianceCIFSProtocolMaxConnections.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceCIFSProtocolMaxConnections.setStatus("current")


class _EqlApplianceCIFSProtocolUnixCharacterSet_Type(Integer32):
    """Custom type eqlApplianceCIFSProtocolUnixCharacterSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("utf8", 1),
          ("utf8jp", 2))
    )


_EqlApplianceCIFSProtocolUnixCharacterSet_Type.__name__ = "Integer32"
_EqlApplianceCIFSProtocolUnixCharacterSet_Object = MibTableColumn
eqlApplianceCIFSProtocolUnixCharacterSet = _EqlApplianceCIFSProtocolUnixCharacterSet_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 29, 1, 6),
    _EqlApplianceCIFSProtocolUnixCharacterSet_Type()
)
eqlApplianceCIFSProtocolUnixCharacterSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceCIFSProtocolUnixCharacterSet.setStatus("current")


class _EqlApplianceCIFSProtocolDosCodePage_Type(Integer32):
    """Custom type eqlApplianceCIFSProtocolDosCodePage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("cp437", 2),
          ("cp737", 3),
          ("cp775", 4),
          ("cp850", 1),
          ("cp852", 5),
          ("cp857", 6),
          ("cp860", 7),
          ("cp861", 8),
          ("cp862", 9),
          ("cp863", 10),
          ("cp864", 11),
          ("cp865", 12),
          ("cp866", 13),
          ("cp874", 14),
          ("cp932", 15),
          ("cp936", 16),
          ("cp949", 17),
          ("cp950", 18),
          ("eucjp", 19),
          ("unused", 0))
    )


_EqlApplianceCIFSProtocolDosCodePage_Type.__name__ = "Integer32"
_EqlApplianceCIFSProtocolDosCodePage_Object = MibTableColumn
eqlApplianceCIFSProtocolDosCodePage = _EqlApplianceCIFSProtocolDosCodePage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 29, 1, 7),
    _EqlApplianceCIFSProtocolDosCodePage_Type()
)
eqlApplianceCIFSProtocolDosCodePage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceCIFSProtocolDosCodePage.setStatus("current")
_EqlApplianceOptimizationScheduleTable_Object = MibTable
eqlApplianceOptimizationScheduleTable = _EqlApplianceOptimizationScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 30)
)
if mibBuilder.loadTexts:
    eqlApplianceOptimizationScheduleTable.setStatus("current")
_EqlApplianceOptimizationScheduleEntry_Object = MibTableRow
eqlApplianceOptimizationScheduleEntry = _EqlApplianceOptimizationScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 30, 1)
)
eqlApplianceOptimizationScheduleEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceOptimizationScheduleEntry.setStatus("current")
_EqlApplianceOptimizationScheduleRowStatus_Type = RowStatus
_EqlApplianceOptimizationScheduleRowStatus_Object = MibTableColumn
eqlApplianceOptimizationScheduleRowStatus = _EqlApplianceOptimizationScheduleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 30, 1, 1),
    _EqlApplianceOptimizationScheduleRowStatus_Type()
)
eqlApplianceOptimizationScheduleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceOptimizationScheduleRowStatus.setStatus("current")


class _EqlApplianceOptimizationScheduleStatus_Type(TruthValue):
    """Custom type eqlApplianceOptimizationScheduleStatus based on TruthValue"""


_EqlApplianceOptimizationScheduleStatus_Object = MibTableColumn
eqlApplianceOptimizationScheduleStatus = _EqlApplianceOptimizationScheduleStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 30, 1, 2),
    _EqlApplianceOptimizationScheduleStatus_Type()
)
eqlApplianceOptimizationScheduleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceOptimizationScheduleStatus.setStatus("current")


class _EqlApplianceOptimizationContainerIndex_Type(Unsigned32):
    """Custom type eqlApplianceOptimizationContainerIndex based on Unsigned32"""
    defaultValue = 0


_EqlApplianceOptimizationContainerIndex_Object = MibTableColumn
eqlApplianceOptimizationContainerIndex = _EqlApplianceOptimizationContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 30, 1, 3),
    _EqlApplianceOptimizationContainerIndex_Type()
)
eqlApplianceOptimizationContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceOptimizationContainerIndex.setStatus("current")


class _EqlApplianceOptimizationPolicyIndex_Type(Integer32):
    """Custom type eqlApplianceOptimizationPolicyIndex based on Integer32"""
    defaultValue = 0


_EqlApplianceOptimizationPolicyIndex_Object = MibTableColumn
eqlApplianceOptimizationPolicyIndex = _EqlApplianceOptimizationPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 30, 1, 4),
    _EqlApplianceOptimizationPolicyIndex_Type()
)
eqlApplianceOptimizationPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceOptimizationPolicyIndex.setStatus("current")
_EqlApplianceAdminAccountTable_Object = MibTable
eqlApplianceAdminAccountTable = _EqlApplianceAdminAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 31)
)
if mibBuilder.loadTexts:
    eqlApplianceAdminAccountTable.setStatus("current")
_EqlApplianceAdminAccountEntry_Object = MibTableRow
eqlApplianceAdminAccountEntry = _EqlApplianceAdminAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 31, 1)
)
eqlApplianceAdminAccountEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceAdminAccountName"),
)
if mibBuilder.loadTexts:
    eqlApplianceAdminAccountEntry.setStatus("current")


class _EqlApplianceAdminAccountName_Type(DisplayString):
    """Custom type eqlApplianceAdminAccountName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceAdminAccountName_Type.__name__ = "DisplayString"
_EqlApplianceAdminAccountName_Object = MibTableColumn
eqlApplianceAdminAccountName = _EqlApplianceAdminAccountName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 31, 1, 1),
    _EqlApplianceAdminAccountName_Type()
)
eqlApplianceAdminAccountName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAdminAccountName.setStatus("current")
_EqlApplianceAdminAccountRowStatus_Type = RowStatus
_EqlApplianceAdminAccountRowStatus_Object = MibTableColumn
eqlApplianceAdminAccountRowStatus = _EqlApplianceAdminAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 31, 1, 2),
    _EqlApplianceAdminAccountRowStatus_Type()
)
eqlApplianceAdminAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAdminAccountRowStatus.setStatus("current")


class _EqlApplianceAdminAccountPassword_Type(OctetString):
    """Custom type eqlApplianceAdminAccountPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceAdminAccountPassword_Type.__name__ = "OctetString"
_EqlApplianceAdminAccountPassword_Object = MibTableColumn
eqlApplianceAdminAccountPassword = _EqlApplianceAdminAccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 31, 1, 3),
    _EqlApplianceAdminAccountPassword_Type()
)
eqlApplianceAdminAccountPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceAdminAccountPassword.setStatus("current")
_EqlApplianceLicenseTable_Object = MibTable
eqlApplianceLicenseTable = _EqlApplianceLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 32)
)
if mibBuilder.loadTexts:
    eqlApplianceLicenseTable.setStatus("current")
_EqlApplianceLicenseEntry_Object = MibTableRow
eqlApplianceLicenseEntry = _EqlApplianceLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 32, 1)
)
eqlApplianceLicenseEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceLicenseFeatureId"),
)
if mibBuilder.loadTexts:
    eqlApplianceLicenseEntry.setStatus("current")
_EqlApplianceLicenseRowStatus_Type = RowStatus
_EqlApplianceLicenseRowStatus_Object = MibTableColumn
eqlApplianceLicenseRowStatus = _EqlApplianceLicenseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 32, 1, 1),
    _EqlApplianceLicenseRowStatus_Type()
)
eqlApplianceLicenseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLicenseRowStatus.setStatus("current")


class _EqlApplianceLicenseFeatureId_Type(Integer32):
    """Custom type eqlApplianceLicenseFeatureId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advanced-dedupe", 2),
          ("basic-dedupe", 1))
    )


_EqlApplianceLicenseFeatureId_Type.__name__ = "Integer32"
_EqlApplianceLicenseFeatureId_Object = MibTableColumn
eqlApplianceLicenseFeatureId = _EqlApplianceLicenseFeatureId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 32, 1, 2),
    _EqlApplianceLicenseFeatureId_Type()
)
eqlApplianceLicenseFeatureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceLicenseFeatureId.setStatus("current")


class _EqlApplianceLicenseEntitlementId_Type(OctetString):
    """Custom type eqlApplianceLicenseEntitlementId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_EqlApplianceLicenseEntitlementId_Type.__name__ = "OctetString"
_EqlApplianceLicenseEntitlementId_Object = MibTableColumn
eqlApplianceLicenseEntitlementId = _EqlApplianceLicenseEntitlementId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 32, 1, 3),
    _EqlApplianceLicenseEntitlementId_Type()
)
eqlApplianceLicenseEntitlementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceLicenseEntitlementId.setStatus("current")


class _EqlApplianceLicenseState_Type(Integer32):
    """Custom type eqlApplianceLicenseState based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 0),
          ("expired", 2))
    )


_EqlApplianceLicenseState_Type.__name__ = "Integer32"
_EqlApplianceLicenseState_Object = MibTableColumn
eqlApplianceLicenseState = _EqlApplianceLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 32, 1, 4),
    _EqlApplianceLicenseState_Type()
)
eqlApplianceLicenseState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLicenseState.setStatus("current")
_EqlApplianceLicenseExpiry_Type = Counter32
_EqlApplianceLicenseExpiry_Object = MibTableColumn
eqlApplianceLicenseExpiry = _EqlApplianceLicenseExpiry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 32, 1, 5),
    _EqlApplianceLicenseExpiry_Type()
)
eqlApplianceLicenseExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceLicenseExpiry.setStatus("current")


class _EqlApplianceLicenseUsed_Type(TruthValue):
    """Custom type eqlApplianceLicenseUsed based on TruthValue"""


_EqlApplianceLicenseUsed_Object = MibTableColumn
eqlApplianceLicenseUsed = _EqlApplianceLicenseUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 32, 1, 6),
    _EqlApplianceLicenseUsed_Type()
)
eqlApplianceLicenseUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceLicenseUsed.setStatus("current")


class _EqlApplianceLicenseType_Type(Integer32):
    """Custom type eqlApplianceLicenseType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("evaluation", 0),
          ("perpetual", 1))
    )


_EqlApplianceLicenseType_Type.__name__ = "Integer32"
_EqlApplianceLicenseType_Object = MibTableColumn
eqlApplianceLicenseType = _EqlApplianceLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 32, 1, 7),
    _EqlApplianceLicenseType_Type()
)
eqlApplianceLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceLicenseType.setStatus("current")
_EqlApplianceLicenseFileTable_Object = MibTable
eqlApplianceLicenseFileTable = _EqlApplianceLicenseFileTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 33)
)
if mibBuilder.loadTexts:
    eqlApplianceLicenseFileTable.setStatus("current")
_EqlApplianceLicenseFileEntry_Object = MibTableRow
eqlApplianceLicenseFileEntry = _EqlApplianceLicenseFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 33, 1)
)
eqlApplianceLicenseFileEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceLicenseFileEntry.setStatus("current")
_EqlApplianceLicenseFileRowStatus_Type = RowStatus
_EqlApplianceLicenseFileRowStatus_Object = MibTableColumn
eqlApplianceLicenseFileRowStatus = _EqlApplianceLicenseFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 33, 1, 1),
    _EqlApplianceLicenseFileRowStatus_Type()
)
eqlApplianceLicenseFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLicenseFileRowStatus.setStatus("current")


class _EqlApplianceLicenseFileName_Type(OctetString):
    """Custom type eqlApplianceLicenseFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EqlApplianceLicenseFileName_Type.__name__ = "OctetString"
_EqlApplianceLicenseFileName_Object = MibTableColumn
eqlApplianceLicenseFileName = _EqlApplianceLicenseFileName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 33, 1, 2),
    _EqlApplianceLicenseFileName_Type()
)
eqlApplianceLicenseFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceLicenseFileName.setStatus("current")
_EqlApplianceTypeEQLMemberMPVTable_Object = MibTable
eqlApplianceTypeEQLMemberMPVTable = _EqlApplianceTypeEQLMemberMPVTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 34)
)
if mibBuilder.loadTexts:
    eqlApplianceTypeEQLMemberMPVTable.setStatus("current")
_EqlApplianceTypeEQLMemberMPVEntry_Object = MibTableRow
eqlApplianceTypeEQLMemberMPVEntry = _EqlApplianceTypeEQLMemberMPVEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 34, 1)
)
eqlApplianceTypeEQLMemberMPVEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceType"),
)
if mibBuilder.loadTexts:
    eqlApplianceTypeEQLMemberMPVEntry.setStatus("current")
_EqlApplianceTypeEQLMemberMPV_Type = Unsigned32
_EqlApplianceTypeEQLMemberMPV_Object = MibTableColumn
eqlApplianceTypeEQLMemberMPV = _EqlApplianceTypeEQLMemberMPV_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 34, 1, 1),
    _EqlApplianceTypeEQLMemberMPV_Type()
)
eqlApplianceTypeEQLMemberMPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceTypeEQLMemberMPV.setStatus("current")
_EqlApplianceTypeEQLGroupMPVTable_Object = MibTable
eqlApplianceTypeEQLGroupMPVTable = _EqlApplianceTypeEQLGroupMPVTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 35)
)
if mibBuilder.loadTexts:
    eqlApplianceTypeEQLGroupMPVTable.setStatus("current")
_EqlApplianceTypeEQLGroupMPVEntry_Object = MibTableRow
eqlApplianceTypeEQLGroupMPVEntry = _EqlApplianceTypeEQLGroupMPVEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 35, 1)
)
eqlApplianceTypeEQLGroupMPVEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceType"),
)
if mibBuilder.loadTexts:
    eqlApplianceTypeEQLGroupMPVEntry.setStatus("current")
_EqlApplianceTypeEQLGroupMPV_Type = Unsigned32
_EqlApplianceTypeEQLGroupMPV_Object = MibTableColumn
eqlApplianceTypeEQLGroupMPV = _EqlApplianceTypeEQLGroupMPV_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 35, 1, 1),
    _EqlApplianceTypeEQLGroupMPV_Type()
)
eqlApplianceTypeEQLGroupMPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceTypeEQLGroupMPV.setStatus("current")
_EqlApplianceVolumeDiscoveryTable_Object = MibTable
eqlApplianceVolumeDiscoveryTable = _EqlApplianceVolumeDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 36)
)
if mibBuilder.loadTexts:
    eqlApplianceVolumeDiscoveryTable.setStatus("current")
_EqlApplianceVolumeDiscoveryEntry_Object = MibTableRow
eqlApplianceVolumeDiscoveryEntry = _EqlApplianceVolumeDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 36, 1)
)
eqlApplianceVolumeDiscoveryEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNodeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeTargetIscsiName"),
)
if mibBuilder.loadTexts:
    eqlApplianceVolumeDiscoveryEntry.setStatus("current")
_EqlApplianceVolumeDiscoveryRowStatus_Type = RowStatus
_EqlApplianceVolumeDiscoveryRowStatus_Object = MibTableColumn
eqlApplianceVolumeDiscoveryRowStatus = _EqlApplianceVolumeDiscoveryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 36, 1, 1),
    _EqlApplianceVolumeDiscoveryRowStatus_Type()
)
eqlApplianceVolumeDiscoveryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceVolumeDiscoveryRowStatus.setStatus("current")


class _EqlApplianceVolumeDiscoveryVolumeNodeAccessibleStatus_Type(Integer32):
    """Custom type eqlApplianceVolumeDiscoveryVolumeNodeAccessibleStatus based on Integer32"""
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
        *(("fault", 2),
          ("not-optimal", 0),
          ("optimal", 1))
    )


_EqlApplianceVolumeDiscoveryVolumeNodeAccessibleStatus_Type.__name__ = "Integer32"
_EqlApplianceVolumeDiscoveryVolumeNodeAccessibleStatus_Object = MibTableColumn
eqlApplianceVolumeDiscoveryVolumeNodeAccessibleStatus = _EqlApplianceVolumeDiscoveryVolumeNodeAccessibleStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 36, 1, 2),
    _EqlApplianceVolumeDiscoveryVolumeNodeAccessibleStatus_Type()
)
eqlApplianceVolumeDiscoveryVolumeNodeAccessibleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceVolumeDiscoveryVolumeNodeAccessibleStatus.setStatus("current")


class _EqlApplianceVolumeDiscoveryVolumeStatus_Type(Integer32):
    """Custom type eqlApplianceVolumeDiscoveryVolumeStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("expandable", 3),
          ("expanding", 1),
          ("formatted", 2),
          ("formatting", 5),
          ("new", 4),
          ("unknown", 0))
    )


_EqlApplianceVolumeDiscoveryVolumeStatus_Type.__name__ = "Integer32"
_EqlApplianceVolumeDiscoveryVolumeStatus_Object = MibTableColumn
eqlApplianceVolumeDiscoveryVolumeStatus = _EqlApplianceVolumeDiscoveryVolumeStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 36, 1, 3),
    _EqlApplianceVolumeDiscoveryVolumeStatus_Type()
)
eqlApplianceVolumeDiscoveryVolumeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceVolumeDiscoveryVolumeStatus.setStatus("current")


class _EqlApplianceVolumeDiscoveryVolumeLunNumber_Type(Unsigned32):
    """Custom type eqlApplianceVolumeDiscoveryVolumeLunNumber based on Unsigned32"""
    defaultValue = 0


_EqlApplianceVolumeDiscoveryVolumeLunNumber_Object = MibTableColumn
eqlApplianceVolumeDiscoveryVolumeLunNumber = _EqlApplianceVolumeDiscoveryVolumeLunNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 36, 1, 4),
    _EqlApplianceVolumeDiscoveryVolumeLunNumber_Type()
)
eqlApplianceVolumeDiscoveryVolumeLunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlApplianceVolumeDiscoveryVolumeLunNumber.setStatus("current")
_EqlApplianceInitiatorsTable_Object = MibTable
eqlApplianceInitiatorsTable = _EqlApplianceInitiatorsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 37)
)
if mibBuilder.loadTexts:
    eqlApplianceInitiatorsTable.setStatus("current")
_EqlApplianceInitiatorsEntry_Object = MibTableRow
eqlApplianceInitiatorsEntry = _EqlApplianceInitiatorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 37, 1)
)
eqlApplianceInitiatorsEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNodeIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceInitiatorsEntry.setStatus("current")
_EqlApplianceInitiatorRowStatus_Type = RowStatus
_EqlApplianceInitiatorRowStatus_Object = MibTableColumn
eqlApplianceInitiatorRowStatus = _EqlApplianceInitiatorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 37, 1, 1),
    _EqlApplianceInitiatorRowStatus_Type()
)
eqlApplianceInitiatorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceInitiatorRowStatus.setStatus("current")


class _EqlApplianceInitiatorName_Type(OctetString):
    """Custom type eqlApplianceInitiatorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqlApplianceInitiatorName_Type.__name__ = "OctetString"
_EqlApplianceInitiatorName_Object = MibTableColumn
eqlApplianceInitiatorName = _EqlApplianceInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 37, 1, 2),
    _EqlApplianceInitiatorName_Type()
)
eqlApplianceInitiatorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceInitiatorName.setStatus("current")
_EqlApplianceUserQueryTable_Object = MibTable
eqlApplianceUserQueryTable = _EqlApplianceUserQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38)
)
if mibBuilder.loadTexts:
    eqlApplianceUserQueryTable.setStatus("current")
_EqlApplianceUserQueryEntry_Object = MibTableRow
eqlApplianceUserQueryEntry = _EqlApplianceUserQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38, 1)
)
eqlApplianceUserQueryEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceUserQuerySearchString"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceUserQueryDBType"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceUserQueryPageSize"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceUserQueryPageNumber"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceUserQueryUserDomain"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceUserQueryUserName"),
)
if mibBuilder.loadTexts:
    eqlApplianceUserQueryEntry.setStatus("current")


class _EqlApplianceUserQuerySearchString_Type(OctetString):
    """Custom type eqlApplianceUserQuerySearchString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlApplianceUserQuerySearchString_Type.__name__ = "OctetString"
_EqlApplianceUserQuerySearchString_Object = MibTableColumn
eqlApplianceUserQuerySearchString = _EqlApplianceUserQuerySearchString_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38, 1, 1),
    _EqlApplianceUserQuerySearchString_Type()
)
eqlApplianceUserQuerySearchString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUserQuerySearchString.setStatus("current")


class _EqlApplianceUserQueryDBType_Type(Integer32):
    """Custom type eqlApplianceUserQueryDBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ad", 1),
          ("all", 3),
          ("local", 4),
          ("unix", 2),
          ("unused", 0))
    )


_EqlApplianceUserQueryDBType_Type.__name__ = "Integer32"
_EqlApplianceUserQueryDBType_Object = MibTableColumn
eqlApplianceUserQueryDBType = _EqlApplianceUserQueryDBType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38, 1, 2),
    _EqlApplianceUserQueryDBType_Type()
)
eqlApplianceUserQueryDBType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUserQueryDBType.setStatus("current")
_EqlApplianceUserQueryPageSize_Type = Unsigned32
_EqlApplianceUserQueryPageSize_Object = MibTableColumn
eqlApplianceUserQueryPageSize = _EqlApplianceUserQueryPageSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38, 1, 3),
    _EqlApplianceUserQueryPageSize_Type()
)
eqlApplianceUserQueryPageSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUserQueryPageSize.setStatus("current")
_EqlApplianceUserQueryPageNumber_Type = Unsigned32
_EqlApplianceUserQueryPageNumber_Object = MibTableColumn
eqlApplianceUserQueryPageNumber = _EqlApplianceUserQueryPageNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38, 1, 4),
    _EqlApplianceUserQueryPageNumber_Type()
)
eqlApplianceUserQueryPageNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUserQueryPageNumber.setStatus("current")


class _EqlApplianceUserQueryUserDomain_Type(OctetString):
    """Custom type eqlApplianceUserQueryUserDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EqlApplianceUserQueryUserDomain_Type.__name__ = "OctetString"
_EqlApplianceUserQueryUserDomain_Object = MibTableColumn
eqlApplianceUserQueryUserDomain = _EqlApplianceUserQueryUserDomain_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38, 1, 5),
    _EqlApplianceUserQueryUserDomain_Type()
)
eqlApplianceUserQueryUserDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUserQueryUserDomain.setStatus("current")


class _EqlApplianceUserQueryUserName_Type(OctetString):
    """Custom type eqlApplianceUserQueryUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlApplianceUserQueryUserName_Type.__name__ = "OctetString"
_EqlApplianceUserQueryUserName_Object = MibTableColumn
eqlApplianceUserQueryUserName = _EqlApplianceUserQueryUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38, 1, 6),
    _EqlApplianceUserQueryUserName_Type()
)
eqlApplianceUserQueryUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUserQueryUserName.setStatus("current")
_EqlApplianceUserQueryRowStatus_Type = RowStatus
_EqlApplianceUserQueryRowStatus_Object = MibTableColumn
eqlApplianceUserQueryRowStatus = _EqlApplianceUserQueryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38, 1, 7),
    _EqlApplianceUserQueryRowStatus_Type()
)
eqlApplianceUserQueryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUserQueryRowStatus.setStatus("current")
_EqlApplianceUserQueryTotalUsers_Type = Unsigned32
_EqlApplianceUserQueryTotalUsers_Object = MibTableColumn
eqlApplianceUserQueryTotalUsers = _EqlApplianceUserQueryTotalUsers_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38, 1, 8),
    _EqlApplianceUserQueryTotalUsers_Type()
)
eqlApplianceUserQueryTotalUsers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUserQueryTotalUsers.setStatus("current")


class _EqlApplianceUserQueryUserId_Type(OctetString):
    """Custom type eqlApplianceUserQueryUserId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceUserQueryUserId_Type.__name__ = "OctetString"
_EqlApplianceUserQueryUserId_Object = MibTableColumn
eqlApplianceUserQueryUserId = _EqlApplianceUserQueryUserId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38, 1, 9),
    _EqlApplianceUserQueryUserId_Type()
)
eqlApplianceUserQueryUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUserQueryUserId.setStatus("current")


class _EqlApplianceUserQueryUserPrimaryGroup_Type(OctetString):
    """Custom type eqlApplianceUserQueryUserPrimaryGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 184),
    )


_EqlApplianceUserQueryUserPrimaryGroup_Type.__name__ = "OctetString"
_EqlApplianceUserQueryUserPrimaryGroup_Object = MibTableColumn
eqlApplianceUserQueryUserPrimaryGroup = _EqlApplianceUserQueryUserPrimaryGroup_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38, 1, 10),
    _EqlApplianceUserQueryUserPrimaryGroup_Type()
)
eqlApplianceUserQueryUserPrimaryGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUserQueryUserPrimaryGroup.setStatus("current")


class _EqlApplianceUserQueryUserType_Type(Integer32):
    """Custom type eqlApplianceUserQueryUserType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ad", 1),
          ("unix", 2),
          ("unused", 0))
    )


_EqlApplianceUserQueryUserType_Type.__name__ = "Integer32"
_EqlApplianceUserQueryUserType_Object = MibTableColumn
eqlApplianceUserQueryUserType = _EqlApplianceUserQueryUserType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38, 1, 11),
    _EqlApplianceUserQueryUserType_Type()
)
eqlApplianceUserQueryUserType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUserQueryUserType.setStatus("current")


class _EqlApplianceUserQueryUserSource_Type(Integer32):
    """Custom type eqlApplianceUserQueryUserSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("local", 1),
          ("unused", 0))
    )


_EqlApplianceUserQueryUserSource_Type.__name__ = "Integer32"
_EqlApplianceUserQueryUserSource_Object = MibTableColumn
eqlApplianceUserQueryUserSource = _EqlApplianceUserQueryUserSource_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 38, 1, 12),
    _EqlApplianceUserQueryUserSource_Type()
)
eqlApplianceUserQueryUserSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceUserQueryUserSource.setStatus("current")
_EqlApplianceDnsServerTable_Object = MibTable
eqlApplianceDnsServerTable = _EqlApplianceDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 39)
)
if mibBuilder.loadTexts:
    eqlApplianceDnsServerTable.setStatus("current")
_EqlApplianceDnsServerEntry_Object = MibTableRow
eqlApplianceDnsServerEntry = _EqlApplianceDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 39, 1)
)
eqlApplianceDnsServerEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceDnsServerIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceDnsServerEntry.setStatus("current")
_EqlApplianceDnsServerIndex_Type = Unsigned32
_EqlApplianceDnsServerIndex_Object = MibTableColumn
eqlApplianceDnsServerIndex = _EqlApplianceDnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 39, 1, 1),
    _EqlApplianceDnsServerIndex_Type()
)
eqlApplianceDnsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceDnsServerIndex.setStatus("current")
_EqlApplianceDnsServerRowStatus_Type = RowStatus
_EqlApplianceDnsServerRowStatus_Object = MibTableColumn
eqlApplianceDnsServerRowStatus = _EqlApplianceDnsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 39, 1, 2),
    _EqlApplianceDnsServerRowStatus_Type()
)
eqlApplianceDnsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceDnsServerRowStatus.setStatus("current")


class _EqlApplianceDnsServerInetAddressType_Type(InetAddressType):
    """Custom type eqlApplianceDnsServerInetAddressType based on InetAddressType"""


_EqlApplianceDnsServerInetAddressType_Object = MibTableColumn
eqlApplianceDnsServerInetAddressType = _EqlApplianceDnsServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 39, 1, 3),
    _EqlApplianceDnsServerInetAddressType_Type()
)
eqlApplianceDnsServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceDnsServerInetAddressType.setStatus("current")
_EqlApplianceDnsServerInetAddress_Type = InetAddress
_EqlApplianceDnsServerInetAddress_Object = MibTableColumn
eqlApplianceDnsServerInetAddress = _EqlApplianceDnsServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 39, 1, 4),
    _EqlApplianceDnsServerInetAddress_Type()
)
eqlApplianceDnsServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceDnsServerInetAddress.setStatus("current")


class _EqlApplianceDnsServerTransactionState_Type(Integer32):
    """Custom type eqlApplianceDnsServerTransactionState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("configCommit", 3),
          ("configInProgress", 2),
          ("configStart", 1),
          ("configStartCommit", 4),
          ("singleOp", 0))
    )


_EqlApplianceDnsServerTransactionState_Type.__name__ = "Integer32"
_EqlApplianceDnsServerTransactionState_Object = MibTableColumn
eqlApplianceDnsServerTransactionState = _EqlApplianceDnsServerTransactionState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 39, 1, 5),
    _EqlApplianceDnsServerTransactionState_Type()
)
eqlApplianceDnsServerTransactionState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceDnsServerTransactionState.setStatus("current")
_EqlApplianceDnsSuffixTable_Object = MibTable
eqlApplianceDnsSuffixTable = _EqlApplianceDnsSuffixTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 40)
)
if mibBuilder.loadTexts:
    eqlApplianceDnsSuffixTable.setStatus("current")
_EqlApplianceDnsSuffixEntry_Object = MibTableRow
eqlApplianceDnsSuffixEntry = _EqlApplianceDnsSuffixEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 40, 1)
)
eqlApplianceDnsSuffixEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceDnsSuffixIndex"),
)
if mibBuilder.loadTexts:
    eqlApplianceDnsSuffixEntry.setStatus("current")
_EqlApplianceDnsSuffixIndex_Type = Unsigned32
_EqlApplianceDnsSuffixIndex_Object = MibTableColumn
eqlApplianceDnsSuffixIndex = _EqlApplianceDnsSuffixIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 40, 1, 1),
    _EqlApplianceDnsSuffixIndex_Type()
)
eqlApplianceDnsSuffixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlApplianceDnsSuffixIndex.setStatus("current")
_EqlApplianceDnsSuffixRowStatus_Type = RowStatus
_EqlApplianceDnsSuffixRowStatus_Object = MibTableColumn
eqlApplianceDnsSuffixRowStatus = _EqlApplianceDnsSuffixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 40, 1, 2),
    _EqlApplianceDnsSuffixRowStatus_Type()
)
eqlApplianceDnsSuffixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceDnsSuffixRowStatus.setStatus("current")


class _EqlApplianceDnsSuffixString_Type(DisplayString):
    """Custom type eqlApplianceDnsSuffixString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EqlApplianceDnsSuffixString_Type.__name__ = "DisplayString"
_EqlApplianceDnsSuffixString_Object = MibTableColumn
eqlApplianceDnsSuffixString = _EqlApplianceDnsSuffixString_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 40, 1, 3),
    _EqlApplianceDnsSuffixString_Type()
)
eqlApplianceDnsSuffixString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceDnsSuffixString.setStatus("current")


class _EqlApplianceDnsSuffixTransactionState_Type(Integer32):
    """Custom type eqlApplianceDnsSuffixTransactionState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("configCommit", 3),
          ("configInProgress", 2),
          ("configStart", 1),
          ("configStartCommit", 4),
          ("singleOp", 0))
    )


_EqlApplianceDnsSuffixTransactionState_Type.__name__ = "Integer32"
_EqlApplianceDnsSuffixTransactionState_Object = MibTableColumn
eqlApplianceDnsSuffixTransactionState = _EqlApplianceDnsSuffixTransactionState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 40, 1, 4),
    _EqlApplianceDnsSuffixTransactionState_Type()
)
eqlApplianceDnsSuffixTransactionState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceDnsSuffixTransactionState.setStatus("current")
_EqlApplianceDomainListTable_Object = MibTable
eqlApplianceDomainListTable = _EqlApplianceDomainListTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 41)
)
if mibBuilder.loadTexts:
    eqlApplianceDomainListTable.setStatus("current")
_EqlApplianceDomainListEntry_Object = MibTableRow
eqlApplianceDomainListEntry = _EqlApplianceDomainListEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 41, 1)
)
eqlApplianceDomainListEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceDomainName"),
)
if mibBuilder.loadTexts:
    eqlApplianceDomainListEntry.setStatus("current")


class _EqlApplianceDomainName_Type(OctetString):
    """Custom type eqlApplianceDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlApplianceDomainName_Type.__name__ = "OctetString"
_EqlApplianceDomainName_Object = MibTableColumn
eqlApplianceDomainName = _EqlApplianceDomainName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 41, 1, 1),
    _EqlApplianceDomainName_Type()
)
eqlApplianceDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceDomainName.setStatus("current")


class _EqlApplianceDomainType_Type(Integer32):
    """Custom type eqlApplianceDomainType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ad", 1),
          ("local", 3),
          ("unix", 2),
          ("unused", 0))
    )


_EqlApplianceDomainType_Type.__name__ = "Integer32"
_EqlApplianceDomainType_Object = MibTableColumn
eqlApplianceDomainType = _EqlApplianceDomainType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 41, 1, 2),
    _EqlApplianceDomainType_Type()
)
eqlApplianceDomainType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceDomainType.setStatus("current")
_EqlApplianceGroupQueryTable_Object = MibTable
eqlApplianceGroupQueryTable = _EqlApplianceGroupQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 42)
)
if mibBuilder.loadTexts:
    eqlApplianceGroupQueryTable.setStatus("current")
_EqlApplianceGroupQueryEntry_Object = MibTableRow
eqlApplianceGroupQueryEntry = _EqlApplianceGroupQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 42, 1)
)
eqlApplianceGroupQueryEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceGroupQuerySearchString"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceGroupQueryDBType"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceGroupQueryPageSize"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceGroupQueryPageNumber"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceGroupQueryDomain"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceGroupQueryGroupName"),
)
if mibBuilder.loadTexts:
    eqlApplianceGroupQueryEntry.setStatus("current")


class _EqlApplianceGroupQuerySearchString_Type(OctetString):
    """Custom type eqlApplianceGroupQuerySearchString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlApplianceGroupQuerySearchString_Type.__name__ = "OctetString"
_EqlApplianceGroupQuerySearchString_Object = MibTableColumn
eqlApplianceGroupQuerySearchString = _EqlApplianceGroupQuerySearchString_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 42, 1, 1),
    _EqlApplianceGroupQuerySearchString_Type()
)
eqlApplianceGroupQuerySearchString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceGroupQuerySearchString.setStatus("current")


class _EqlApplianceGroupQueryDBType_Type(Integer32):
    """Custom type eqlApplianceGroupQueryDBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ad", 1),
          ("all", 3),
          ("local", 4),
          ("unix", 2),
          ("unused", 0))
    )


_EqlApplianceGroupQueryDBType_Type.__name__ = "Integer32"
_EqlApplianceGroupQueryDBType_Object = MibTableColumn
eqlApplianceGroupQueryDBType = _EqlApplianceGroupQueryDBType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 42, 1, 2),
    _EqlApplianceGroupQueryDBType_Type()
)
eqlApplianceGroupQueryDBType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceGroupQueryDBType.setStatus("current")
_EqlApplianceGroupQueryPageSize_Type = Unsigned32
_EqlApplianceGroupQueryPageSize_Object = MibTableColumn
eqlApplianceGroupQueryPageSize = _EqlApplianceGroupQueryPageSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 42, 1, 3),
    _EqlApplianceGroupQueryPageSize_Type()
)
eqlApplianceGroupQueryPageSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceGroupQueryPageSize.setStatus("current")
_EqlApplianceGroupQueryPageNumber_Type = Unsigned32
_EqlApplianceGroupQueryPageNumber_Object = MibTableColumn
eqlApplianceGroupQueryPageNumber = _EqlApplianceGroupQueryPageNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 42, 1, 4),
    _EqlApplianceGroupQueryPageNumber_Type()
)
eqlApplianceGroupQueryPageNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceGroupQueryPageNumber.setStatus("current")


class _EqlApplianceGroupQueryDomain_Type(OctetString):
    """Custom type eqlApplianceGroupQueryDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EqlApplianceGroupQueryDomain_Type.__name__ = "OctetString"
_EqlApplianceGroupQueryDomain_Object = MibTableColumn
eqlApplianceGroupQueryDomain = _EqlApplianceGroupQueryDomain_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 42, 1, 5),
    _EqlApplianceGroupQueryDomain_Type()
)
eqlApplianceGroupQueryDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceGroupQueryDomain.setStatus("current")


class _EqlApplianceGroupQueryGroupName_Type(OctetString):
    """Custom type eqlApplianceGroupQueryGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlApplianceGroupQueryGroupName_Type.__name__ = "OctetString"
_EqlApplianceGroupQueryGroupName_Object = MibTableColumn
eqlApplianceGroupQueryGroupName = _EqlApplianceGroupQueryGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 42, 1, 6),
    _EqlApplianceGroupQueryGroupName_Type()
)
eqlApplianceGroupQueryGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceGroupQueryGroupName.setStatus("current")
_EqlApplianceGroupQueryRowStatus_Type = RowStatus
_EqlApplianceGroupQueryRowStatus_Object = MibTableColumn
eqlApplianceGroupQueryRowStatus = _EqlApplianceGroupQueryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 42, 1, 7),
    _EqlApplianceGroupQueryRowStatus_Type()
)
eqlApplianceGroupQueryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceGroupQueryRowStatus.setStatus("current")
_EqlApplianceGroupQueryTotalGroups_Type = Unsigned32
_EqlApplianceGroupQueryTotalGroups_Object = MibTableColumn
eqlApplianceGroupQueryTotalGroups = _EqlApplianceGroupQueryTotalGroups_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 42, 1, 8),
    _EqlApplianceGroupQueryTotalGroups_Type()
)
eqlApplianceGroupQueryTotalGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceGroupQueryTotalGroups.setStatus("current")


class _EqlApplianceGroupQueryGroupId_Type(OctetString):
    """Custom type eqlApplianceGroupQueryGroupId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlApplianceGroupQueryGroupId_Type.__name__ = "OctetString"
_EqlApplianceGroupQueryGroupId_Object = MibTableColumn
eqlApplianceGroupQueryGroupId = _EqlApplianceGroupQueryGroupId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 42, 1, 9),
    _EqlApplianceGroupQueryGroupId_Type()
)
eqlApplianceGroupQueryGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceGroupQueryGroupId.setStatus("current")


class _EqlApplianceGroupQueryGroupType_Type(Integer32):
    """Custom type eqlApplianceGroupQueryGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ad", 1),
          ("unix", 2),
          ("unused", 0))
    )


_EqlApplianceGroupQueryGroupType_Type.__name__ = "Integer32"
_EqlApplianceGroupQueryGroupType_Object = MibTableColumn
eqlApplianceGroupQueryGroupType = _EqlApplianceGroupQueryGroupType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 42, 1, 10),
    _EqlApplianceGroupQueryGroupType_Type()
)
eqlApplianceGroupQueryGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceGroupQueryGroupType.setStatus("current")


class _EqlApplianceGroupQueryGroupSource_Type(Integer32):
    """Custom type eqlApplianceGroupQueryGroupSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("local", 1),
          ("unused", 0))
    )


_EqlApplianceGroupQueryGroupSource_Type.__name__ = "Integer32"
_EqlApplianceGroupQueryGroupSource_Object = MibTableColumn
eqlApplianceGroupQueryGroupSource = _EqlApplianceGroupQueryGroupSource_Object(
    (1, 3, 6, 1, 4, 1, 12740, 17, 1, 42, 1, 11),
    _EqlApplianceGroupQueryGroupSource_Type()
)
eqlApplianceGroupQueryGroupSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlApplianceGroupQueryGroupSource.setStatus("current")
eqliscsiVolumeEntry.registerAugmentions(
    ("EQLAPPLIANCE-MIB",
     "eqlVolumeApplianceEntry")
)
eqlVolumeApplianceEntry.setIndexNames(*eqliscsiVolumeEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLAPPLIANCE-MIB",
    **{"eqlApplianceModule": eqlApplianceModule,
       "eqlApplianceObjects": eqlApplianceObjects,
       "eqlApplianceTable": eqlApplianceTable,
       "eqlApplianceEntry": eqlApplianceEntry,
       "eqlApplianceIndex": eqlApplianceIndex,
       "eqlApplianceRowStatus": eqlApplianceRowStatus,
       "eqlApplianceName": eqlApplianceName,
       "eqlApplianceType": eqlApplianceType,
       "eqlApplianceState": eqlApplianceState,
       "eqlApplianceDescription": eqlApplianceDescription,
       "eqlApplianceMgmtAddressType": eqlApplianceMgmtAddressType,
       "eqlApplianceMgmtAddress": eqlApplianceMgmtAddress,
       "eqlApplianceMgmtPort": eqlApplianceMgmtPort,
       "eqlApplianceMajorVersion": eqlApplianceMajorVersion,
       "eqlApplianceMinorVersion": eqlApplianceMinorVersion,
       "eqlApplianceMaintVersion": eqlApplianceMaintVersion,
       "eqlApplianceVendorId": eqlApplianceVendorId,
       "eqlApplianceSharedSecret": eqlApplianceSharedSecret,
       "eqlApplianceUserName": eqlApplianceUserName,
       "eqlApplianceNumberOfNodes": eqlApplianceNumberOfNodes,
       "eqlApplianceUniqueID": eqlApplianceUniqueID,
       "eqlApplianceConfigStatus": eqlApplianceConfigStatus,
       "eqlApplianceAction": eqlApplianceAction,
       "eqlApplianceAdminStatus": eqlApplianceAdminStatus,
       "eqlApplianceGatewayAddrType": eqlApplianceGatewayAddrType,
       "eqlApplianceGatewayAddr": eqlApplianceGatewayAddr,
       "eqlApplianceLastScheduleIndex": eqlApplianceLastScheduleIndex,
       "eqlApplianceMPV": eqlApplianceMPV,
       "eqlApplianceEnableFTP": eqlApplianceEnableFTP,
       "eqlApplianceDesiredServiceMode": eqlApplianceDesiredServiceMode,
       "eqlApplianceServiceModeStatus": eqlApplianceServiceModeStatus,
       "eqlApplianceRequestId": eqlApplianceRequestId,
       "eqlApplianceUniqueIDTable": eqlApplianceUniqueIDTable,
       "eqlApplianceUniqueIDEntry": eqlApplianceUniqueIDEntry,
       "eqlApplianceUniqueIDType": eqlApplianceUniqueIDType,
       "eqlApplianceUniqueIDValueLen": eqlApplianceUniqueIDValueLen,
       "eqlApplianceUniqueIDValue": eqlApplianceUniqueIDValue,
       "eqlApplianceUnInitNodesTable": eqlApplianceUnInitNodesTable,
       "eqlApplianceUnInitNodesEntry": eqlApplianceUnInitNodesEntry,
       "eqlApplianceUnInitNodeProductType": eqlApplianceUnInitNodeProductType,
       "eqlApplianceUnInitNodeServiceTag": eqlApplianceUnInitNodeServiceTag,
       "eqlApplianceUnInitNodeState": eqlApplianceUnInitNodeState,
       "eqlApplianceUnInitNodeModel": eqlApplianceUnInitNodeModel,
       "eqlApplianceUnInitNodeVendor": eqlApplianceUnInitNodeVendor,
       "eqlApplianceUnInitNodeLinkLocalIPType": eqlApplianceUnInitNodeLinkLocalIPType,
       "eqlApplianceUnInitNodeLinkLocalIP": eqlApplianceUnInitNodeLinkLocalIP,
       "eqlApplianceUnInitNodeMajorVersion": eqlApplianceUnInitNodeMajorVersion,
       "eqlApplianceUnInitNodeMinorVersion": eqlApplianceUnInitNodeMinorVersion,
       "eqlApplianceUnInitNodeMaintVersion": eqlApplianceUnInitNodeMaintVersion,
       "eqlApplianceUnInitNodeRowStatus": eqlApplianceUnInitNodeRowStatus,
       "eqlApplianceUnInitNodeClusterMPV": eqlApplianceUnInitNodeClusterMPV,
       "eqlApplianceUnInitNodeChassisTag": eqlApplianceUnInitNodeChassisTag,
       "eqlApplianceNodeTable": eqlApplianceNodeTable,
       "eqlApplianceNodeEntry": eqlApplianceNodeEntry,
       "eqlApplianceNodeIndex": eqlApplianceNodeIndex,
       "eqlApplianceNodeRowStatus": eqlApplianceNodeRowStatus,
       "eqlApplianceNodeProductType": eqlApplianceNodeProductType,
       "eqlApplianceNodeServiceTag": eqlApplianceNodeServiceTag,
       "eqlApplianceNodeModel": eqlApplianceNodeModel,
       "eqlApplianceNodeVendor": eqlApplianceNodeVendor,
       "eqlApplianceNodeLinkLocalIPType": eqlApplianceNodeLinkLocalIPType,
       "eqlApplianceNodeLinkLocalIP": eqlApplianceNodeLinkLocalIP,
       "eqlApplianceNodeMajorVersion": eqlApplianceNodeMajorVersion,
       "eqlApplianceNodeMinorVersion": eqlApplianceNodeMinorVersion,
       "eqlApplianceNodeMaintVersion": eqlApplianceNodeMaintVersion,
       "eqlApplianceNodeName": eqlApplianceNodeName,
       "eqlApplianceNodePeerIndex": eqlApplianceNodePeerIndex,
       "eqlApplianceNodeConfigState": eqlApplianceNodeConfigState,
       "eqlApplianceNodeConfigStatus": eqlApplianceNodeConfigStatus,
       "eqlApplianceNodeGatewayAddrType": eqlApplianceNodeGatewayAddrType,
       "eqlApplianceNodeGatewayAddr": eqlApplianceNodeGatewayAddr,
       "eqlApplianceNodeInitiatorName": eqlApplianceNodeInitiatorName,
       "eqlApplianceNodeAdminStatus": eqlApplianceNodeAdminStatus,
       "eqlApplianceNodeChassisTag": eqlApplianceNodeChassisTag,
       "eqlApplianceNodeChassisName": eqlApplianceNodeChassisName,
       "eqlApplianceNodeOpsRequestId": eqlApplianceNodeOpsRequestId,
       "eqlApplianceNetworksTable": eqlApplianceNetworksTable,
       "eqlApplianceNetworksEntry": eqlApplianceNetworksEntry,
       "eqlApplianceNetworkRowStatus": eqlApplianceNetworkRowStatus,
       "eqlApplianceNetworkType": eqlApplianceNetworkType,
       "eqlApplianceNetworkID": eqlApplianceNetworkID,
       "eqlApplianceNetworkName": eqlApplianceNetworkName,
       "eqlApplianceNetworkBlockIPAddressType": eqlApplianceNetworkBlockIPAddressType,
       "eqlApplianceNetworkBlockIPAddress": eqlApplianceNetworkBlockIPAddress,
       "eqlApplianceNetworkBlockNetmaskAddrType": eqlApplianceNetworkBlockNetmaskAddrType,
       "eqlApplianceNetworkBlockNetmaskAddr": eqlApplianceNetworkBlockNetmaskAddr,
       "eqlApplianceNetworkVLANTag": eqlApplianceNetworkVLANTag,
       "eqlApplianceNetworkAdminState": eqlApplianceNetworkAdminState,
       "eqlApplianceNetworkMTUSize": eqlApplianceNetworkMTUSize,
       "eqlApplianceNetworkBondingMode": eqlApplianceNetworkBondingMode,
       "eqlApplianceIPTable": eqlApplianceIPTable,
       "eqlApplianceIPEntry": eqlApplianceIPEntry,
       "eqlApplianceIPRowStatus": eqlApplianceIPRowStatus,
       "eqlApplianceIPAddressType": eqlApplianceIPAddressType,
       "eqlApplianceIPAddress": eqlApplianceIPAddress,
       "eqlApplianceNodeIPTable": eqlApplianceNodeIPTable,
       "eqlApplianceNodeIPEntry": eqlApplianceNodeIPEntry,
       "eqlApplianceNodeIPRowStatus": eqlApplianceNodeIPRowStatus,
       "eqlApplianceNodeIPAddressType": eqlApplianceNodeIPAddressType,
       "eqlApplianceNodeIPAddress": eqlApplianceNodeIPAddress,
       "eqlApplianceOpsTable": eqlApplianceOpsTable,
       "eqlApplianceOpsEntry": eqlApplianceOpsEntry,
       "eqlApplianceOpsIndex": eqlApplianceOpsIndex,
       "eqlApplianceOpsRowStatus": eqlApplianceOpsRowStatus,
       "eqlApplianceOpsType": eqlApplianceOpsType,
       "eqlApplianceOpsStatus": eqlApplianceOpsStatus,
       "eqlApplianceOpsPercentage": eqlApplianceOpsPercentage,
       "eqlApplianceOpsRequestId": eqlApplianceOpsRequestId,
       "eqlVolumeApplianceTable": eqlVolumeApplianceTable,
       "eqlVolumeApplianceEntry": eqlVolumeApplianceEntry,
       "eqlVolumeApplianceRowStatus": eqlVolumeApplianceRowStatus,
       "eqlVolumeApplianceIndex": eqlVolumeApplianceIndex,
       "eqlVolumeApplianceNodeIndex": eqlVolumeApplianceNodeIndex,
       "eqlVolumeApplianceState": eqlVolumeApplianceState,
       "eqlApplianceOpsFailureTable": eqlApplianceOpsFailureTable,
       "eqlApplianceOpsFailureEntry": eqlApplianceOpsFailureEntry,
       "eqlApplianceOpsFailureIndex": eqlApplianceOpsFailureIndex,
       "eqlApplianceOpsFailureType": eqlApplianceOpsFailureType,
       "eqlApplianceOpsFailureScope": eqlApplianceOpsFailureScope,
       "eqlApplianceOpsFailureCode": eqlApplianceOpsFailureCode,
       "eqlApplianceOpsFailureComponent": eqlApplianceOpsFailureComponent,
       "eqlApplianceOpsFailureSubComponent": eqlApplianceOpsFailureSubComponent,
       "eqlApplianceOpsFailureMessage": eqlApplianceOpsFailureMessage,
       "eqlApplianceNodeHealthFailureTable": eqlApplianceNodeHealthFailureTable,
       "eqlApplianceNodeHealthFailureEntry": eqlApplianceNodeHealthFailureEntry,
       "eqlApplianceNodeHealthFailureIndex": eqlApplianceNodeHealthFailureIndex,
       "eqlApplianceNodeHealthFailureType": eqlApplianceNodeHealthFailureType,
       "eqlApplianceNodeHealthFailureCode": eqlApplianceNodeHealthFailureCode,
       "eqlApplianceNodeHealthFailureComponent": eqlApplianceNodeHealthFailureComponent,
       "eqlApplianceNodeHealthFailureSubComponent": eqlApplianceNodeHealthFailureSubComponent,
       "eqlApplianceNodeHealthFailureMessage": eqlApplianceNodeHealthFailureMessage,
       "eqlApplianceServiceStatusTable": eqlApplianceServiceStatusTable,
       "eqlApplianceServiceStatusEntry": eqlApplianceServiceStatusEntry,
       "eqlApplianceOverallState": eqlApplianceOverallState,
       "eqlApplianceServiceStatus": eqlApplianceServiceStatus,
       "eqlApplianceServiceCriticalConditions": eqlApplianceServiceCriticalConditions,
       "eqlApplianceServiceWarningConditions": eqlApplianceServiceWarningConditions,
       "eqlApplianceServiceAction": eqlApplianceServiceAction,
       "eqlApplianceStatsTable": eqlApplianceStatsTable,
       "eqlApplianceStatsEntry": eqlApplianceStatsEntry,
       "eqlApplianceStatsTotalCapacity": eqlApplianceStatsTotalCapacity,
       "eqlApplianceStatsTotalAllocated": eqlApplianceStatsTotalAllocated,
       "eqlApplianceStatsTotalUsed": eqlApplianceStatsTotalUsed,
       "eqlApplianceStatsTotalFree": eqlApplianceStatsTotalFree,
       "eqlApplianceStatsTotalSnapshots": eqlApplianceStatsTotalSnapshots,
       "eqlApplianceStatsNumberOfContainers": eqlApplianceStatsNumberOfContainers,
       "eqlApplianceStatsNumberOfNfsExports": eqlApplianceStatsNumberOfNfsExports,
       "eqlApplianceStatsNumberOfCifsShares": eqlApplianceStatsNumberOfCifsShares,
       "eqlApplianceStatsNumberOfSnapshots": eqlApplianceStatsNumberOfSnapshots,
       "eqlApplianceStatsTotalOptimizationSpaceSavings": eqlApplianceStatsTotalOptimizationSpaceSavings,
       "eqlApplianceNodeStatusTable": eqlApplianceNodeStatusTable,
       "eqlApplianceNodeStatusEntry": eqlApplianceNodeStatusEntry,
       "eqlApplianceNodeStatusNodeState": eqlApplianceNodeStatusNodeState,
       "eqlApplianceMultiStateOpsTable": eqlApplianceMultiStateOpsTable,
       "eqlApplianceMultiStateOpsEntry": eqlApplianceMultiStateOpsEntry,
       "eqlApplianceMultiStateOpsIndex": eqlApplianceMultiStateOpsIndex,
       "eqlApplianceMultiStateOpsRowStatus": eqlApplianceMultiStateOpsRowStatus,
       "eqlApplianceMultiStateOpsType": eqlApplianceMultiStateOpsType,
       "eqlApplianceMultiStateOpsStatus": eqlApplianceMultiStateOpsStatus,
       "eqlApplianceMultiStateOpsServiceTag": eqlApplianceMultiStateOpsServiceTag,
       "eqlApplianceMultiStateOpsServiceTag2": eqlApplianceMultiStateOpsServiceTag2,
       "eqlApplianceMultiStateOpsNodeIndex": eqlApplianceMultiStateOpsNodeIndex,
       "eqlApplianceMultiStateOpsNodeIndex2": eqlApplianceMultiStateOpsNodeIndex2,
       "eqlApplianceMultiStateOpsState": eqlApplianceMultiStateOpsState,
       "eqlApplianceMultiStateOpsPercentage": eqlApplianceMultiStateOpsPercentage,
       "eqlApplianceMultiStateOpsAction": eqlApplianceMultiStateOpsAction,
       "eqlApplianceMultiStateOpsCurNodeIndex": eqlApplianceMultiStateOpsCurNodeIndex,
       "eqlApplianceMultiStateOpsLongRunningOp": eqlApplianceMultiStateOpsLongRunningOp,
       "eqlApplianceMultiStateOpsRequestId": eqlApplianceMultiStateOpsRequestId,
       "eqlApplianceNdmpTable": eqlApplianceNdmpTable,
       "eqlApplianceNdmpEntry": eqlApplianceNdmpEntry,
       "eqlApplianceNdmpRowStatus": eqlApplianceNdmpRowStatus,
       "eqlApplianceNdmpUserName": eqlApplianceNdmpUserName,
       "eqlApplianceNdmpPasswd": eqlApplianceNdmpPasswd,
       "eqlApplianceNdmpDesiredState": eqlApplianceNdmpDesiredState,
       "eqlApplianceNdmpClientPort": eqlApplianceNdmpClientPort,
       "eqlApplianceNdmpDmaServerTable": eqlApplianceNdmpDmaServerTable,
       "eqlApplianceNdmpDmaServerEntry": eqlApplianceNdmpDmaServerEntry,
       "eqlApplianceNdmpDmaServerRowStatus": eqlApplianceNdmpDmaServerRowStatus,
       "eqlApplianceNdmpDmaServerIPAddressType": eqlApplianceNdmpDmaServerIPAddressType,
       "eqlApplianceNdmpDmaServerIPAddress": eqlApplianceNdmpDmaServerIPAddress,
       "eqlApplianceNdmpDmaServerTransactionState": eqlApplianceNdmpDmaServerTransactionState,
       "eqlApplianceLocalUserAccessTable": eqlApplianceLocalUserAccessTable,
       "eqlApplianceLocalUserAccessEntry": eqlApplianceLocalUserAccessEntry,
       "eqlApplianceLocalUserAccessRowStatus": eqlApplianceLocalUserAccessRowStatus,
       "eqlApplianceLocalUserName": eqlApplianceLocalUserName,
       "eqlApplianceLocalUserPassword": eqlApplianceLocalUserPassword,
       "eqlApplianceLocalUserUid": eqlApplianceLocalUserUid,
       "eqlApplianceLocalUserPrimaryGroup": eqlApplianceLocalUserPrimaryGroup,
       "eqlApplianceLocalUserRealName": eqlApplianceLocalUserRealName,
       "eqlApplianceLocalUserSid": eqlApplianceLocalUserSid,
       "eqlApplianceLocalUserRemarks": eqlApplianceLocalUserRemarks,
       "eqlApplianceLocalUserAdditionalGroups": eqlApplianceLocalUserAdditionalGroups,
       "eqlApplianceLocalUserAccess": eqlApplianceLocalUserAccess,
       "eqlApplianceLocalGroupAccessTable": eqlApplianceLocalGroupAccessTable,
       "eqlApplianceLocalGroupAccessEntry": eqlApplianceLocalGroupAccessEntry,
       "eqlApplianceLocalGroupAccessRowStatus": eqlApplianceLocalGroupAccessRowStatus,
       "eqlApplianceLocalGroupName": eqlApplianceLocalGroupName,
       "eqlApplianceLocalGroupGid": eqlApplianceLocalGroupGid,
       "eqlApplianceLocalGroupGsid": eqlApplianceLocalGroupGsid,
       "eqlApplianceCredentialsDatabaseTable": eqlApplianceCredentialsDatabaseTable,
       "eqlApplianceCredentialsDatabaseEntry": eqlApplianceCredentialsDatabaseEntry,
       "eqlApplianceCredentialsDatabaseRowStatus": eqlApplianceCredentialsDatabaseRowStatus,
       "eqlApplianceCredentialsDatabaseType": eqlApplianceCredentialsDatabaseType,
       "eqlApplianceCredentialsDatabaseLdapBaseDn": eqlApplianceCredentialsDatabaseLdapBaseDn,
       "eqlApplianceCredentialsDatabaseLdapServerAddress": eqlApplianceCredentialsDatabaseLdapServerAddress,
       "eqlApplianceCredentialsDatabaseNisDomain": eqlApplianceCredentialsDatabaseNisDomain,
       "eqlApplianceCredentialsDatabaseNisServerAddress": eqlApplianceCredentialsDatabaseNisServerAddress,
       "eqlApplianceActiveDirectoryAccessTable": eqlApplianceActiveDirectoryAccessTable,
       "eqlApplianceActiveDirectoryAccessEntry": eqlApplianceActiveDirectoryAccessEntry,
       "eqlApplianceActiveDirectoryRowStatus": eqlApplianceActiveDirectoryRowStatus,
       "eqlApplianceActiveDirectoryAdvancedSettings": eqlApplianceActiveDirectoryAdvancedSettings,
       "eqlApplianceActiveDirectoryNetBiosName": eqlApplianceActiveDirectoryNetBiosName,
       "eqlApplianceActiveDirectoryDomain": eqlApplianceActiveDirectoryDomain,
       "eqlApplianceActiveDirectoryUserName": eqlApplianceActiveDirectoryUserName,
       "eqlApplianceActiveDirectoryPassword": eqlApplianceActiveDirectoryPassword,
       "eqlApplianceActiveDirectoryDescription": eqlApplianceActiveDirectoryDescription,
       "eqlApplianceActiveDirectoryFunctionalLevel": eqlApplianceActiveDirectoryFunctionalLevel,
       "eqlApplianceActiveDirectoryWinsServer": eqlApplianceActiveDirectoryWinsServer,
       "eqlApplianceActiveDirectoryWorkGroup": eqlApplianceActiveDirectoryWorkGroup,
       "eqlApplianceActiveDirectoryDomainControllers": eqlApplianceActiveDirectoryDomainControllers,
       "eqlApplianceActiveDirectoryMemberOfDomain": eqlApplianceActiveDirectoryMemberOfDomain,
       "eqlApplianceActiveDirectoryStatus": eqlApplianceActiveDirectoryStatus,
       "eqlApplianceActiveDirectoryAccessibleControllers": eqlApplianceActiveDirectoryAccessibleControllers,
       "eqlApplianceActiveDirectoryPreferredControllers": eqlApplianceActiveDirectoryPreferredControllers,
       "eqlApplianceManualMappingTable": eqlApplianceManualMappingTable,
       "eqlApplianceManualMappingEntry": eqlApplianceManualMappingEntry,
       "eqlApplianceManualMappingRowStatus": eqlApplianceManualMappingRowStatus,
       "eqlApplianceManualMappingUserName": eqlApplianceManualMappingUserName,
       "eqlApplianceManualMappingMappedToUserName": eqlApplianceManualMappingMappedToUserName,
       "eqlApplianceManualMappingDirection": eqlApplianceManualMappingDirection,
       "eqlApplianceMappingPolicyTable": eqlApplianceMappingPolicyTable,
       "eqlApplianceMappingPolicyEntry": eqlApplianceMappingPolicyEntry,
       "eqlApplianceMappingPolicyRowStatus": eqlApplianceMappingPolicyRowStatus,
       "eqlApplianceMappingPolicyAcquireMapping": eqlApplianceMappingPolicyAcquireMapping,
       "eqlApplianceMappingPolicyAllowNotMapped": eqlApplianceMappingPolicyAllowNotMapped,
       "eqlApplianceAllGroupsTable": eqlApplianceAllGroupsTable,
       "eqlApplianceAllGroupsEntry": eqlApplianceAllGroupsEntry,
       "eqlApplianceAllGroupsRowStatus": eqlApplianceAllGroupsRowStatus,
       "eqlApplianceAllGroupsName": eqlApplianceAllGroupsName,
       "eqlApplianceAllGroupsId": eqlApplianceAllGroupsId,
       "eqlApplianceAllGroupsType": eqlApplianceAllGroupsType,
       "eqlApplianceAllGroupsSource": eqlApplianceAllGroupsSource,
       "eqlApplianceAllUsersTable": eqlApplianceAllUsersTable,
       "eqlApplianceAllUsersEntry": eqlApplianceAllUsersEntry,
       "eqlApplianceAllUsersRowStatus": eqlApplianceAllUsersRowStatus,
       "eqlApplianceAllUsersName": eqlApplianceAllUsersName,
       "eqlApplianceAllUsersId": eqlApplianceAllUsersId,
       "eqlApplianceAllUsersType": eqlApplianceAllUsersType,
       "eqlApplianceAllUsersSource": eqlApplianceAllUsersSource,
       "eqlApplianceEQLMemberMPVTable": eqlApplianceEQLMemberMPVTable,
       "eqlApplianceEQLMemberMPVEntry": eqlApplianceEQLMemberMPVEntry,
       "eqlApplianceEQLMemberMPV": eqlApplianceEQLMemberMPV,
       "eqlApplianceMPVTable": eqlApplianceMPVTable,
       "eqlApplianceMPVEntry": eqlApplianceMPVEntry,
       "eqlApplianceEQLGroupMPV": eqlApplianceEQLGroupMPV,
       "eqlApplianceClusterMPV": eqlApplianceClusterMPV,
       "eqlApplianceClusterMajorVersion": eqlApplianceClusterMajorVersion,
       "eqlApplianceClusterMinorVersion": eqlApplianceClusterMinorVersion,
       "eqlApplianceClusterMaintVersion": eqlApplianceClusterMaintVersion,
       "eqlApplianceSyncedDataTable": eqlApplianceSyncedDataTable,
       "eqlApplianceSyncedDataEntry": eqlApplianceSyncedDataEntry,
       "eqlApplianceSyncedDataRowStatus": eqlApplianceSyncedDataRowStatus,
       "eqlApplianceSyncedDataType": eqlApplianceSyncedDataType,
       "eqlApplianceSyncedDataIndex": eqlApplianceSyncedDataIndex,
       "eqlApplianceSyncedDataIndexPayload": eqlApplianceSyncedDataIndexPayload,
       "eqlApplianceSyncedDataEntryPayload": eqlApplianceSyncedDataEntryPayload,
       "eqlApplianceSyncedDataState": eqlApplianceSyncedDataState,
       "eqlApplianceCIFSProtocolTable": eqlApplianceCIFSProtocolTable,
       "eqlApplianceCIFSProtocolEntry": eqlApplianceCIFSProtocolEntry,
       "eqlApplianceCIFSProtocolRowStatus": eqlApplianceCIFSProtocolRowStatus,
       "eqlApplianceCIFSProtocolAuthenticationEnabled": eqlApplianceCIFSProtocolAuthenticationEnabled,
       "eqlApplianceCIFSProtocolAuthenticationType": eqlApplianceCIFSProtocolAuthenticationType,
       "eqlApplianceCIFSProtocolAllowGuests": eqlApplianceCIFSProtocolAllowGuests,
       "eqlApplianceCIFSProtocolMaxConnections": eqlApplianceCIFSProtocolMaxConnections,
       "eqlApplianceCIFSProtocolUnixCharacterSet": eqlApplianceCIFSProtocolUnixCharacterSet,
       "eqlApplianceCIFSProtocolDosCodePage": eqlApplianceCIFSProtocolDosCodePage,
       "eqlApplianceOptimizationScheduleTable": eqlApplianceOptimizationScheduleTable,
       "eqlApplianceOptimizationScheduleEntry": eqlApplianceOptimizationScheduleEntry,
       "eqlApplianceOptimizationScheduleRowStatus": eqlApplianceOptimizationScheduleRowStatus,
       "eqlApplianceOptimizationScheduleStatus": eqlApplianceOptimizationScheduleStatus,
       "eqlApplianceOptimizationContainerIndex": eqlApplianceOptimizationContainerIndex,
       "eqlApplianceOptimizationPolicyIndex": eqlApplianceOptimizationPolicyIndex,
       "eqlApplianceAdminAccountTable": eqlApplianceAdminAccountTable,
       "eqlApplianceAdminAccountEntry": eqlApplianceAdminAccountEntry,
       "eqlApplianceAdminAccountName": eqlApplianceAdminAccountName,
       "eqlApplianceAdminAccountRowStatus": eqlApplianceAdminAccountRowStatus,
       "eqlApplianceAdminAccountPassword": eqlApplianceAdminAccountPassword,
       "eqlApplianceLicenseTable": eqlApplianceLicenseTable,
       "eqlApplianceLicenseEntry": eqlApplianceLicenseEntry,
       "eqlApplianceLicenseRowStatus": eqlApplianceLicenseRowStatus,
       "eqlApplianceLicenseFeatureId": eqlApplianceLicenseFeatureId,
       "eqlApplianceLicenseEntitlementId": eqlApplianceLicenseEntitlementId,
       "eqlApplianceLicenseState": eqlApplianceLicenseState,
       "eqlApplianceLicenseExpiry": eqlApplianceLicenseExpiry,
       "eqlApplianceLicenseUsed": eqlApplianceLicenseUsed,
       "eqlApplianceLicenseType": eqlApplianceLicenseType,
       "eqlApplianceLicenseFileTable": eqlApplianceLicenseFileTable,
       "eqlApplianceLicenseFileEntry": eqlApplianceLicenseFileEntry,
       "eqlApplianceLicenseFileRowStatus": eqlApplianceLicenseFileRowStatus,
       "eqlApplianceLicenseFileName": eqlApplianceLicenseFileName,
       "eqlApplianceTypeEQLMemberMPVTable": eqlApplianceTypeEQLMemberMPVTable,
       "eqlApplianceTypeEQLMemberMPVEntry": eqlApplianceTypeEQLMemberMPVEntry,
       "eqlApplianceTypeEQLMemberMPV": eqlApplianceTypeEQLMemberMPV,
       "eqlApplianceTypeEQLGroupMPVTable": eqlApplianceTypeEQLGroupMPVTable,
       "eqlApplianceTypeEQLGroupMPVEntry": eqlApplianceTypeEQLGroupMPVEntry,
       "eqlApplianceTypeEQLGroupMPV": eqlApplianceTypeEQLGroupMPV,
       "eqlApplianceVolumeDiscoveryTable": eqlApplianceVolumeDiscoveryTable,
       "eqlApplianceVolumeDiscoveryEntry": eqlApplianceVolumeDiscoveryEntry,
       "eqlApplianceVolumeDiscoveryRowStatus": eqlApplianceVolumeDiscoveryRowStatus,
       "eqlApplianceVolumeDiscoveryVolumeNodeAccessibleStatus": eqlApplianceVolumeDiscoveryVolumeNodeAccessibleStatus,
       "eqlApplianceVolumeDiscoveryVolumeStatus": eqlApplianceVolumeDiscoveryVolumeStatus,
       "eqlApplianceVolumeDiscoveryVolumeLunNumber": eqlApplianceVolumeDiscoveryVolumeLunNumber,
       "eqlApplianceInitiatorsTable": eqlApplianceInitiatorsTable,
       "eqlApplianceInitiatorsEntry": eqlApplianceInitiatorsEntry,
       "eqlApplianceInitiatorRowStatus": eqlApplianceInitiatorRowStatus,
       "eqlApplianceInitiatorName": eqlApplianceInitiatorName,
       "eqlApplianceUserQueryTable": eqlApplianceUserQueryTable,
       "eqlApplianceUserQueryEntry": eqlApplianceUserQueryEntry,
       "eqlApplianceUserQuerySearchString": eqlApplianceUserQuerySearchString,
       "eqlApplianceUserQueryDBType": eqlApplianceUserQueryDBType,
       "eqlApplianceUserQueryPageSize": eqlApplianceUserQueryPageSize,
       "eqlApplianceUserQueryPageNumber": eqlApplianceUserQueryPageNumber,
       "eqlApplianceUserQueryUserDomain": eqlApplianceUserQueryUserDomain,
       "eqlApplianceUserQueryUserName": eqlApplianceUserQueryUserName,
       "eqlApplianceUserQueryRowStatus": eqlApplianceUserQueryRowStatus,
       "eqlApplianceUserQueryTotalUsers": eqlApplianceUserQueryTotalUsers,
       "eqlApplianceUserQueryUserId": eqlApplianceUserQueryUserId,
       "eqlApplianceUserQueryUserPrimaryGroup": eqlApplianceUserQueryUserPrimaryGroup,
       "eqlApplianceUserQueryUserType": eqlApplianceUserQueryUserType,
       "eqlApplianceUserQueryUserSource": eqlApplianceUserQueryUserSource,
       "eqlApplianceDnsServerTable": eqlApplianceDnsServerTable,
       "eqlApplianceDnsServerEntry": eqlApplianceDnsServerEntry,
       "eqlApplianceDnsServerIndex": eqlApplianceDnsServerIndex,
       "eqlApplianceDnsServerRowStatus": eqlApplianceDnsServerRowStatus,
       "eqlApplianceDnsServerInetAddressType": eqlApplianceDnsServerInetAddressType,
       "eqlApplianceDnsServerInetAddress": eqlApplianceDnsServerInetAddress,
       "eqlApplianceDnsServerTransactionState": eqlApplianceDnsServerTransactionState,
       "eqlApplianceDnsSuffixTable": eqlApplianceDnsSuffixTable,
       "eqlApplianceDnsSuffixEntry": eqlApplianceDnsSuffixEntry,
       "eqlApplianceDnsSuffixIndex": eqlApplianceDnsSuffixIndex,
       "eqlApplianceDnsSuffixRowStatus": eqlApplianceDnsSuffixRowStatus,
       "eqlApplianceDnsSuffixString": eqlApplianceDnsSuffixString,
       "eqlApplianceDnsSuffixTransactionState": eqlApplianceDnsSuffixTransactionState,
       "eqlApplianceDomainListTable": eqlApplianceDomainListTable,
       "eqlApplianceDomainListEntry": eqlApplianceDomainListEntry,
       "eqlApplianceDomainName": eqlApplianceDomainName,
       "eqlApplianceDomainType": eqlApplianceDomainType,
       "eqlApplianceGroupQueryTable": eqlApplianceGroupQueryTable,
       "eqlApplianceGroupQueryEntry": eqlApplianceGroupQueryEntry,
       "eqlApplianceGroupQuerySearchString": eqlApplianceGroupQuerySearchString,
       "eqlApplianceGroupQueryDBType": eqlApplianceGroupQueryDBType,
       "eqlApplianceGroupQueryPageSize": eqlApplianceGroupQueryPageSize,
       "eqlApplianceGroupQueryPageNumber": eqlApplianceGroupQueryPageNumber,
       "eqlApplianceGroupQueryDomain": eqlApplianceGroupQueryDomain,
       "eqlApplianceGroupQueryGroupName": eqlApplianceGroupQueryGroupName,
       "eqlApplianceGroupQueryRowStatus": eqlApplianceGroupQueryRowStatus,
       "eqlApplianceGroupQueryTotalGroups": eqlApplianceGroupQueryTotalGroups,
       "eqlApplianceGroupQueryGroupId": eqlApplianceGroupQueryGroupId,
       "eqlApplianceGroupQueryGroupType": eqlApplianceGroupQueryGroupType,
       "eqlApplianceGroupQueryGroupSource": eqlApplianceGroupQueryGroupSource}
)
