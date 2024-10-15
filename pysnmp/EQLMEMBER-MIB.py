# SNMP MIB module (EQLMEMBER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLMEMBER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:55 2024
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
 eqlGroupId,
 eqlStorageGroupAdminAccountIndex) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "UTFString",
    "eqlGroupId",
    "eqlStorageGroupAdminAccountIndex")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eqlmemberModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 2)
)
eqlmemberModule.setRevisions(
        ("2012-09-22 00:00",
         "2012-08-15 00:00",
         "2011-08-09 00:00",
         "2002-09-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EqlMemberSEDShareType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 163),
    )



# MIB Managed Objects in the order of their OIDs

_EqlmemberObjects_ObjectIdentity = ObjectIdentity
eqlmemberObjects = _EqlmemberObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1)
)
_EqlMemberTable_Object = MibTable
eqlMemberTable = _EqlMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eqlMemberTable.setStatus("current")
_EqlMemberEntry_Object = MibTableRow
eqlMemberEntry = _EqlMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1)
)
eqlMemberEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberEntry.setStatus("current")
_EqlMemberIndex_Type = Unsigned32
_EqlMemberIndex_Object = MibTableColumn
eqlMemberIndex = _EqlMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 1),
    _EqlMemberIndex_Type()
)
eqlMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlMemberIndex.setStatus("current")
_EqlMemberDateAndTime_Type = Counter32
_EqlMemberDateAndTime_Object = MibTableColumn
eqlMemberDateAndTime = _EqlMemberDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 2),
    _EqlMemberDateAndTime_Type()
)
eqlMemberDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberDateAndTime.setStatus("current")


class _EqlMemberTimeZone_Type(Integer32):
    """Custom type eqlMemberTimeZone based on Integer32"""
    defaultValue = 7

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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("act", 22),
          ("aet", 23),
          ("agt", 28),
          ("ast", 2),
          ("bet", 29),
          ("bst", 18),
          ("cat", 30),
          ("cnt", 27),
          ("cst", 6),
          ("ctt", 20),
          ("eat", 13),
          ("ect", 11),
          ("eet", 12),
          ("est", 7),
          ("gmt", 10),
          ("hst", 1),
          ("iet", 8),
          ("ist", 17),
          ("jst", 21),
          ("met", 14),
          ("mit", 26),
          ("mst", 5),
          ("net", 15),
          ("nst", 25),
          ("plt", 16),
          ("pnt", 4),
          ("prt", 9),
          ("pst", 3),
          ("sst", 24),
          ("vst", 19))
    )


_EqlMemberTimeZone_Type.__name__ = "Integer32"
_EqlMemberTimeZone_Object = MibTableColumn
eqlMemberTimeZone = _EqlMemberTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 3),
    _EqlMemberTimeZone_Type()
)
eqlMemberTimeZone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberTimeZone.setStatus("current")


class _EqlMemberAdjustDaylightSavTime_Type(Integer32):
    """Custom type eqlMemberAdjustDaylightSavTime based on Integer32"""
    defaultValue = 1

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


_EqlMemberAdjustDaylightSavTime_Type.__name__ = "Integer32"
_EqlMemberAdjustDaylightSavTime_Object = MibTableColumn
eqlMemberAdjustDaylightSavTime = _EqlMemberAdjustDaylightSavTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 4),
    _EqlMemberAdjustDaylightSavTime_Type()
)
eqlMemberAdjustDaylightSavTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberAdjustDaylightSavTime.setStatus("current")
_EqlMemberDefaultRoute_Type = IpAddress
_EqlMemberDefaultRoute_Object = MibTableColumn
eqlMemberDefaultRoute = _EqlMemberDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 5),
    _EqlMemberDefaultRoute_Type()
)
eqlMemberDefaultRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberDefaultRoute.setStatus("current")


class _EqlMemberSite_Type(DisplayString):
    """Custom type eqlMemberSite based on DisplayString"""
    defaultValue = OctetString("default")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlMemberSite_Type.__name__ = "DisplayString"
_EqlMemberSite_Object = MibTableColumn
eqlMemberSite = _EqlMemberSite_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 6),
    _EqlMemberSite_Type()
)
eqlMemberSite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberSite.setStatus("current")


class _EqlMemberDescription_Type(UTFString):
    """Custom type eqlMemberDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlMemberDescription_Type.__name__ = "UTFString"
_EqlMemberDescription_Object = MibTableColumn
eqlMemberDescription = _EqlMemberDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 7),
    _EqlMemberDescription_Type()
)
eqlMemberDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberDescription.setStatus("current")


class _EqlMemberUUID_Type(OctetString):
    """Custom type eqlMemberUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlMemberUUID_Type.__name__ = "OctetString"
_EqlMemberUUID_Object = MibTableColumn
eqlMemberUUID = _EqlMemberUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 8),
    _EqlMemberUUID_Type()
)
eqlMemberUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberUUID.setStatus("current")


class _EqlMemberName_Type(DisplayString):
    """Custom type eqlMemberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlMemberName_Type.__name__ = "DisplayString"
_EqlMemberName_Object = MibTableColumn
eqlMemberName = _EqlMemberName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 9),
    _EqlMemberName_Type()
)
eqlMemberName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberName.setStatus("current")
_EqlMemberRowStatus_Type = RowStatus
_EqlMemberRowStatus_Object = MibTableColumn
eqlMemberRowStatus = _EqlMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 10),
    _EqlMemberRowStatus_Type()
)
eqlMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberRowStatus.setStatus("current")


class _EqlMemberState_Type(Integer32):
    """Custom type eqlMemberState based on Integer32"""
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
        *(("off-line", 2),
          ("on-line", 1),
          ("vacate", 3),
          ("vacated", 4))
    )


_EqlMemberState_Type.__name__ = "Integer32"
_EqlMemberState_Object = MibTableColumn
eqlMemberState = _EqlMemberState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 11),
    _EqlMemberState_Type()
)
eqlMemberState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberState.setStatus("current")


class _EqlMemberPolicySingleControllerSafe_Type(Integer32):
    """Custom type eqlMemberPolicySingleControllerSafe based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("safe-disabled", 2),
          ("safe-enabled", 1))
    )


_EqlMemberPolicySingleControllerSafe_Type.__name__ = "Integer32"
_EqlMemberPolicySingleControllerSafe_Object = MibTableColumn
eqlMemberPolicySingleControllerSafe = _EqlMemberPolicySingleControllerSafe_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 12),
    _EqlMemberPolicySingleControllerSafe_Type()
)
eqlMemberPolicySingleControllerSafe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberPolicySingleControllerSafe.setStatus("current")


class _EqlMemberPolicyLowBatterySafe_Type(Integer32):
    """Custom type eqlMemberPolicyLowBatterySafe based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("safe-disabled", 2),
          ("safe-enabled", 1))
    )


_EqlMemberPolicyLowBatterySafe_Type.__name__ = "Integer32"
_EqlMemberPolicyLowBatterySafe_Object = MibTableColumn
eqlMemberPolicyLowBatterySafe = _EqlMemberPolicyLowBatterySafe_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 13),
    _EqlMemberPolicyLowBatterySafe_Type()
)
eqlMemberPolicyLowBatterySafe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberPolicyLowBatterySafe.setStatus("current")
_EqlMemberVersion_Type = Unsigned32
_EqlMemberVersion_Object = MibTableColumn
eqlMemberVersion = _EqlMemberVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 14),
    _EqlMemberVersion_Type()
)
eqlMemberVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberVersion.setStatus("current")


class _EqlMemberDelayDataMove_Type(Integer32):
    """Custom type eqlMemberDelayDataMove based on Integer32"""
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
        *(("unconfigured", 0),
          ("use-member-space", 2),
          ("wait", 1))
    )


_EqlMemberDelayDataMove_Type.__name__ = "Integer32"
_EqlMemberDelayDataMove_Object = MibTableColumn
eqlMemberDelayDataMove = _EqlMemberDelayDataMove_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 15),
    _EqlMemberDelayDataMove_Type()
)
eqlMemberDelayDataMove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberDelayDataMove.setStatus("current")
_EqlMemberDefaultInetRouteType_Type = InetAddressType
_EqlMemberDefaultInetRouteType_Object = MibTableColumn
eqlMemberDefaultInetRouteType = _EqlMemberDefaultInetRouteType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 16),
    _EqlMemberDefaultInetRouteType_Type()
)
eqlMemberDefaultInetRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberDefaultInetRouteType.setStatus("current")
_EqlMemberDefaultInetRoute_Type = InetAddress
_EqlMemberDefaultInetRoute_Object = MibTableColumn
eqlMemberDefaultInetRoute = _EqlMemberDefaultInetRoute_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 17),
    _EqlMemberDefaultInetRoute_Type()
)
eqlMemberDefaultInetRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberDefaultInetRoute.setStatus("current")


class _EqlMemberDriveMirroring_Type(Integer32):
    """Custom type eqlMemberDriveMirroring based on Integer32"""
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


_EqlMemberDriveMirroring_Type.__name__ = "Integer32"
_EqlMemberDriveMirroring_Object = MibTableColumn
eqlMemberDriveMirroring = _EqlMemberDriveMirroring_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 18),
    _EqlMemberDriveMirroring_Type()
)
eqlMemberDriveMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberDriveMirroring.setStatus("current")


class _EqlMemberProfileIndex_Type(Unsigned32):
    """Custom type eqlMemberProfileIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EqlMemberProfileIndex_Type.__name__ = "Unsigned32"
_EqlMemberProfileIndex_Object = MibTableColumn
eqlMemberProfileIndex = _EqlMemberProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 19),
    _EqlMemberProfileIndex_Type()
)
eqlMemberProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberProfileIndex.setStatus("current")


class _EqlMemberControllerType_Type(DisplayString):
    """Custom type eqlMemberControllerType based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlMemberControllerType_Type.__name__ = "DisplayString"
_EqlMemberControllerType_Object = MibTableColumn
eqlMemberControllerType = _EqlMemberControllerType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 20),
    _EqlMemberControllerType_Type()
)
eqlMemberControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberControllerType.setStatus("current")


class _EqlMemberControllerMajorVersion_Type(Unsigned32):
    """Custom type eqlMemberControllerMajorVersion based on Unsigned32"""
    defaultValue = 1


_EqlMemberControllerMajorVersion_Object = MibTableColumn
eqlMemberControllerMajorVersion = _EqlMemberControllerMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 21),
    _EqlMemberControllerMajorVersion_Type()
)
eqlMemberControllerMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberControllerMajorVersion.setStatus("current")


class _EqlMemberControllerMinorVersion_Type(Unsigned32):
    """Custom type eqlMemberControllerMinorVersion based on Unsigned32"""
    defaultValue = 1


_EqlMemberControllerMinorVersion_Object = MibTableColumn
eqlMemberControllerMinorVersion = _EqlMemberControllerMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 22),
    _EqlMemberControllerMinorVersion_Type()
)
eqlMemberControllerMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberControllerMinorVersion.setStatus("current")


class _EqlMemberControllerMaintenanceVersion_Type(Unsigned32):
    """Custom type eqlMemberControllerMaintenanceVersion based on Unsigned32"""
    defaultValue = 0


_EqlMemberControllerMaintenanceVersion_Object = MibTableColumn
eqlMemberControllerMaintenanceVersion = _EqlMemberControllerMaintenanceVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 23),
    _EqlMemberControllerMaintenanceVersion_Type()
)
eqlMemberControllerMaintenanceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberControllerMaintenanceVersion.setStatus("current")


class _EqlMemberCompressionCapable_Type(TruthValue):
    """Custom type eqlMemberCompressionCapable based on TruthValue"""


_EqlMemberCompressionCapable_Object = MibTableColumn
eqlMemberCompressionCapable = _EqlMemberCompressionCapable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 1, 1, 24),
    _EqlMemberCompressionCapable_Type()
)
eqlMemberCompressionCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberCompressionCapable.setStatus("current")
_EqlMemberStatusTable_Object = MibTable
eqlMemberStatusTable = _EqlMemberStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3)
)
if mibBuilder.loadTexts:
    eqlMemberStatusTable.setStatus("current")
_EqlMemberStatusEntry_Object = MibTableRow
eqlMemberStatusEntry = _EqlMemberStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1)
)
eqlMemberStatusEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberStatusEntry.setStatus("current")
_EqlMemberStatusTotalSpace_Type = Integer32
_EqlMemberStatusTotalSpace_Object = MibTableColumn
eqlMemberStatusTotalSpace = _EqlMemberStatusTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 1),
    _EqlMemberStatusTotalSpace_Type()
)
eqlMemberStatusTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusTotalSpace.setStatus("current")
_EqlMemberStatusTotalSpaceUsed_Type = Integer32
_EqlMemberStatusTotalSpaceUsed_Object = MibTableColumn
eqlMemberStatusTotalSpaceUsed = _EqlMemberStatusTotalSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 2),
    _EqlMemberStatusTotalSpaceUsed_Type()
)
eqlMemberStatusTotalSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusTotalSpaceUsed.setStatus("current")


class _EqlMemberStatusModel_Type(DisplayString):
    """Custom type eqlMemberStatusModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlMemberStatusModel_Type.__name__ = "DisplayString"
_EqlMemberStatusModel_Object = MibTableColumn
eqlMemberStatusModel = _EqlMemberStatusModel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 3),
    _EqlMemberStatusModel_Type()
)
eqlMemberStatusModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusModel.setStatus("current")


class _EqlMemberStatusSerialNumber_Type(DisplayString):
    """Custom type eqlMemberStatusSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlMemberStatusSerialNumber_Type.__name__ = "DisplayString"
_EqlMemberStatusSerialNumber_Object = MibTableColumn
eqlMemberStatusSerialNumber = _EqlMemberStatusSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 4),
    _EqlMemberStatusSerialNumber_Type()
)
eqlMemberStatusSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusSerialNumber.setStatus("current")


class _EqlMemberStatusNumberOfControllers_Type(Integer32):
    """Custom type eqlMemberStatusNumberOfControllers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dual", 2),
          ("single", 1))
    )


_EqlMemberStatusNumberOfControllers_Type.__name__ = "Integer32"
_EqlMemberStatusNumberOfControllers_Object = MibTableColumn
eqlMemberStatusNumberOfControllers = _EqlMemberStatusNumberOfControllers_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 5),
    _EqlMemberStatusNumberOfControllers_Type()
)
eqlMemberStatusNumberOfControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusNumberOfControllers.setStatus("current")
_EqlMemberStatusNumberOfDisks_Type = Integer32
_EqlMemberStatusNumberOfDisks_Object = MibTableColumn
eqlMemberStatusNumberOfDisks = _EqlMemberStatusNumberOfDisks_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 6),
    _EqlMemberStatusNumberOfDisks_Type()
)
eqlMemberStatusNumberOfDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusNumberOfDisks.setStatus("current")
_EqlMemberStatusNumberOfSpares_Type = Integer32
_EqlMemberStatusNumberOfSpares_Object = MibTableColumn
eqlMemberStatusNumberOfSpares = _EqlMemberStatusNumberOfSpares_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 7),
    _EqlMemberStatusNumberOfSpares_Type()
)
eqlMemberStatusNumberOfSpares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusNumberOfSpares.setStatus("current")
_EqlMemberStatusCacheSize_Type = Integer32
_EqlMemberStatusCacheSize_Object = MibTableColumn
eqlMemberStatusCacheSize = _EqlMemberStatusCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 8),
    _EqlMemberStatusCacheSize_Type()
)
eqlMemberStatusCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusCacheSize.setStatus("current")


class _EqlMemberStatusCacheMode_Type(Integer32):
    """Custom type eqlMemberStatusCacheMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("write-back", 2),
          ("write-thru", 1))
    )


_EqlMemberStatusCacheMode_Type.__name__ = "Integer32"
_EqlMemberStatusCacheMode_Object = MibTableColumn
eqlMemberStatusCacheMode = _EqlMemberStatusCacheMode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 9),
    _EqlMemberStatusCacheMode_Type()
)
eqlMemberStatusCacheMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusCacheMode.setStatus("current")
_EqlMemberStatusNumberOfConnections_Type = Integer32
_EqlMemberStatusNumberOfConnections_Object = MibTableColumn
eqlMemberStatusNumberOfConnections = _EqlMemberStatusNumberOfConnections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 11),
    _EqlMemberStatusNumberOfConnections_Type()
)
eqlMemberStatusNumberOfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusNumberOfConnections.setStatus("current")
_EqlMemberStatusAverageTemp_Type = Integer32
_EqlMemberStatusAverageTemp_Object = MibTableColumn
eqlMemberStatusAverageTemp = _EqlMemberStatusAverageTemp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 12),
    _EqlMemberStatusAverageTemp_Type()
)
eqlMemberStatusAverageTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusAverageTemp.setStatus("current")


class _EqlMemberStatusTempStatus_Type(Integer32):
    """Custom type eqlMemberStatusTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1))
    )


_EqlMemberStatusTempStatus_Type.__name__ = "Integer32"
_EqlMemberStatusTempStatus_Object = MibTableColumn
eqlMemberStatusTempStatus = _EqlMemberStatusTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 13),
    _EqlMemberStatusTempStatus_Type()
)
eqlMemberStatusTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusTempStatus.setStatus("current")
_EqlMemberStatusBackplaneTempSensor1_Type = Integer32
_EqlMemberStatusBackplaneTempSensor1_Object = MibTableColumn
eqlMemberStatusBackplaneTempSensor1 = _EqlMemberStatusBackplaneTempSensor1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 14),
    _EqlMemberStatusBackplaneTempSensor1_Type()
)
eqlMemberStatusBackplaneTempSensor1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusBackplaneTempSensor1.setStatus("current")
_EqlMemberStatusBackplaneTempSensor2_Type = Integer32
_EqlMemberStatusBackplaneTempSensor2_Object = MibTableColumn
eqlMemberStatusBackplaneTempSensor2 = _EqlMemberStatusBackplaneTempSensor2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 15),
    _EqlMemberStatusBackplaneTempSensor2_Type()
)
eqlMemberStatusBackplaneTempSensor2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusBackplaneTempSensor2.setStatus("current")


class _EqlMemberStatusPowerSupply1Status_Type(Integer32):
    """Custom type eqlMemberStatusPowerSupply1Status based on Integer32"""
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
        *(("failed", 3),
          ("fan-failed", 4),
          ("no-power", 2),
          ("not-present", 5),
          ("on", 1))
    )


_EqlMemberStatusPowerSupply1Status_Type.__name__ = "Integer32"
_EqlMemberStatusPowerSupply1Status_Object = MibTableColumn
eqlMemberStatusPowerSupply1Status = _EqlMemberStatusPowerSupply1Status_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 16),
    _EqlMemberStatusPowerSupply1Status_Type()
)
eqlMemberStatusPowerSupply1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusPowerSupply1Status.setStatus("current")


class _EqlMemberStatusPowerSupply2Status_Type(Integer32):
    """Custom type eqlMemberStatusPowerSupply2Status based on Integer32"""
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
        *(("failed", 3),
          ("fan-failed", 4),
          ("no-power", 2),
          ("not-present", 5),
          ("on", 1))
    )


_EqlMemberStatusPowerSupply2Status_Type.__name__ = "Integer32"
_EqlMemberStatusPowerSupply2Status_Object = MibTableColumn
eqlMemberStatusPowerSupply2Status = _EqlMemberStatusPowerSupply2Status_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 17),
    _EqlMemberStatusPowerSupply2Status_Type()
)
eqlMemberStatusPowerSupply2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusPowerSupply2Status.setStatus("current")
_EqlMemberStatusTrayOneFanOneSpeed_Type = Integer32
_EqlMemberStatusTrayOneFanOneSpeed_Object = MibTableColumn
eqlMemberStatusTrayOneFanOneSpeed = _EqlMemberStatusTrayOneFanOneSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 18),
    _EqlMemberStatusTrayOneFanOneSpeed_Type()
)
eqlMemberStatusTrayOneFanOneSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusTrayOneFanOneSpeed.setStatus("current")
_EqlMemberStatusTrayOneFanTwoSpeed_Type = Integer32
_EqlMemberStatusTrayOneFanTwoSpeed_Object = MibTableColumn
eqlMemberStatusTrayOneFanTwoSpeed = _EqlMemberStatusTrayOneFanTwoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 19),
    _EqlMemberStatusTrayOneFanTwoSpeed_Type()
)
eqlMemberStatusTrayOneFanTwoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusTrayOneFanTwoSpeed.setStatus("current")
_EqlMemberStatusTrayTwoFanOneSpeed_Type = Integer32
_EqlMemberStatusTrayTwoFanOneSpeed_Object = MibTableColumn
eqlMemberStatusTrayTwoFanOneSpeed = _EqlMemberStatusTrayTwoFanOneSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 20),
    _EqlMemberStatusTrayTwoFanOneSpeed_Type()
)
eqlMemberStatusTrayTwoFanOneSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusTrayTwoFanOneSpeed.setStatus("current")
_EqlMemberStatusTrayTwoFanTwoSpeed_Type = Integer32
_EqlMemberStatusTrayTwoFanTwoSpeed_Object = MibTableColumn
eqlMemberStatusTrayTwoFanTwoSpeed = _EqlMemberStatusTrayTwoFanTwoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 21),
    _EqlMemberStatusTrayTwoFanTwoSpeed_Type()
)
eqlMemberStatusTrayTwoFanTwoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusTrayTwoFanTwoSpeed.setStatus("current")


class _EqlMemberStatusPowerSupplyOneFanStatus_Type(Integer32):
    """Custom type eqlMemberStatusPowerSupplyOneFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off-line", 2),
          ("on-line", 1))
    )


_EqlMemberStatusPowerSupplyOneFanStatus_Type.__name__ = "Integer32"
_EqlMemberStatusPowerSupplyOneFanStatus_Object = MibTableColumn
eqlMemberStatusPowerSupplyOneFanStatus = _EqlMemberStatusPowerSupplyOneFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 22),
    _EqlMemberStatusPowerSupplyOneFanStatus_Type()
)
eqlMemberStatusPowerSupplyOneFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusPowerSupplyOneFanStatus.setStatus("current")


class _EqlMemberStatusPowerSupplyTwoFanStatus_Type(Integer32):
    """Custom type eqlMemberStatusPowerSupplyTwoFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off-line", 2),
          ("on-line", 1))
    )


_EqlMemberStatusPowerSupplyTwoFanStatus_Type.__name__ = "Integer32"
_EqlMemberStatusPowerSupplyTwoFanStatus_Object = MibTableColumn
eqlMemberStatusPowerSupplyTwoFanStatus = _EqlMemberStatusPowerSupplyTwoFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 23),
    _EqlMemberStatusPowerSupplyTwoFanStatus_Type()
)
eqlMemberStatusPowerSupplyTwoFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusPowerSupplyTwoFanStatus.setStatus("current")


class _EqlMemberStatusRaidStatus_Type(Integer32):
    """Custom type eqlMemberStatusRaidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("catastrophicLoss", 6),
          ("degraded", 2),
          ("expanding", 7),
          ("failed", 5),
          ("ok", 1),
          ("reconstructing", 4),
          ("verifying", 3))
    )


_EqlMemberStatusRaidStatus_Type.__name__ = "Integer32"
_EqlMemberStatusRaidStatus_Object = MibTableColumn
eqlMemberStatusRaidStatus = _EqlMemberStatusRaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 24),
    _EqlMemberStatusRaidStatus_Type()
)
eqlMemberStatusRaidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusRaidStatus.setStatus("current")


class _EqlMemberStatusRaidPercentage_Type(Integer32):
    """Custom type eqlMemberStatusRaidPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqlMemberStatusRaidPercentage_Type.__name__ = "Integer32"
_EqlMemberStatusRaidPercentage_Object = MibTableColumn
eqlMemberStatusRaidPercentage = _EqlMemberStatusRaidPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 25),
    _EqlMemberStatusRaidPercentage_Type()
)
eqlMemberStatusRaidPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusRaidPercentage.setStatus("current")


class _EqlMemberStatusLostRaidBlocks_Type(Integer32):
    """Custom type eqlMemberStatusLostRaidBlocks based on Integer32"""
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


_EqlMemberStatusLostRaidBlocks_Type.__name__ = "Integer32"
_EqlMemberStatusLostRaidBlocks_Object = MibTableColumn
eqlMemberStatusLostRaidBlocks = _EqlMemberStatusLostRaidBlocks_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 26),
    _EqlMemberStatusLostRaidBlocks_Type()
)
eqlMemberStatusLostRaidBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberStatusLostRaidBlocks.setStatus("current")


class _EqlMemberStatusHealth_Type(Integer32):
    """Custom type eqlMemberStatusHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqlMemberStatusHealth_Type.__name__ = "Integer32"
_EqlMemberStatusHealth_Object = MibTableColumn
eqlMemberStatusHealth = _EqlMemberStatusHealth_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 27),
    _EqlMemberStatusHealth_Type()
)
eqlMemberStatusHealth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberStatusHealth.setStatus("current")
_EqlMemberStatusShortId_Type = Integer32
_EqlMemberStatusShortId_Object = MibTableColumn
eqlMemberStatusShortId = _EqlMemberStatusShortId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 3, 1, 28),
    _EqlMemberStatusShortId_Type()
)
eqlMemberStatusShortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberStatusShortId.setStatus("current")
_EqlMemberInfoTable_Object = MibTable
eqlMemberInfoTable = _EqlMemberInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 4)
)
if mibBuilder.loadTexts:
    eqlMemberInfoTable.setStatus("current")
_EqlMemberInfoEntry_Object = MibTableRow
eqlMemberInfoEntry = _EqlMemberInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 4, 1)
)
eqlMemberInfoEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlTargetMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberInfoEntry.setStatus("current")
_EqlTargetMemberIndex_Type = Integer32
_EqlTargetMemberIndex_Object = MibTableColumn
eqlTargetMemberIndex = _EqlTargetMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 4, 1, 1),
    _EqlTargetMemberIndex_Type()
)
eqlTargetMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlTargetMemberIndex.setStatus("current")


class _EqlMemberInfoStatus_Type(Integer32):
    """Custom type eqlMemberInfoStatus based on Integer32"""
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
        *(("off-line", 2),
          ("on-line", 1),
          ("vacated", 4),
          ("vacating-in-progress", 3))
    )


_EqlMemberInfoStatus_Type.__name__ = "Integer32"
_EqlMemberInfoStatus_Object = MibTableColumn
eqlMemberInfoStatus = _EqlMemberInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 4, 1, 2),
    _EqlMemberInfoStatus_Type()
)
eqlMemberInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberInfoStatus.setStatus("current")
_EqlMemberHealthTable_Object = MibTable
eqlMemberHealthTable = _EqlMemberHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 5)
)
if mibBuilder.loadTexts:
    eqlMemberHealthTable.setStatus("current")
_EqlMemberHealthEntry_Object = MibTableRow
eqlMemberHealthEntry = _EqlMemberHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 5, 1)
)
eqlMemberHealthEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberHealthEntry.setStatus("current")


class _EqlMemberHealthStatus_Type(Integer32):
    """Custom type eqlMemberHealthStatus based on Integer32"""
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
        *(("critical", 3),
          ("normal", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_EqlMemberHealthStatus_Type.__name__ = "Integer32"
_EqlMemberHealthStatus_Object = MibTableColumn
eqlMemberHealthStatus = _EqlMemberHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 5, 1, 1),
    _EqlMemberHealthStatus_Type()
)
eqlMemberHealthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberHealthStatus.setStatus("current")


class _EqlMemberHealthWarningConditions_Type(Bits):
    """Custom type eqlMemberHealthWarningConditions based on Bits"""
    namedValues = NamedValues(
        *(("b2bFailure", 10),
          ("batteryEndOfLifeWarning", 31),
          ("batteryLessthan72hours", 20),
          ("cacheSyncing", 5),
          ("controlModuleRemoved", 2),
          ("cpuFanNotSpinning", 21),
          ("driveNotApproved", 25),
          ("fanRemovedCondition", 27),
          ("fanSpeed", 4),
          ("highTemp", 7),
          ("hwComponentFailedWarn", 0),
          ("incorrectPhysRamSize", 16),
          ("lowTemp", 13),
          ("mixedMedia", 17),
          ("nandHighBadBlockCount", 29),
          ("networkStorm", 30),
          ("noEthernetFlowControl", 26),
          ("powerSupplyFailed", 14),
          ("powerSupplyRemoved", 1),
          ("psfanOffline", 3),
          ("raidMoreSparesExpected", 22),
          ("raidSetFaulted", 6),
          ("raidSetLostblkEntry", 8),
          ("raidSpareTooSmall", 12),
          ("raidSpareWrongType", 23),
          ("raidSsdRaidsetHasHdd", 24),
          ("replicationNoProg", 11),
          ("secondaryEjectSWOpen", 9),
          ("smartBatteryLowCharge", 28),
          ("sumoChannelCardFailed", 19),
          ("sumoChannelCardMissing", 18),
          ("timeOfDayClkBatteryLow", 15))
    )

_EqlMemberHealthWarningConditions_Type.__name__ = "Bits"
_EqlMemberHealthWarningConditions_Object = MibTableColumn
eqlMemberHealthWarningConditions = _EqlMemberHealthWarningConditions_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 5, 1, 2),
    _EqlMemberHealthWarningConditions_Type()
)
eqlMemberHealthWarningConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthWarningConditions.setStatus("current")


class _EqlMemberHealthCriticalConditions_Type(Bits):
    """Custom type eqlMemberHealthCriticalConditions based on Bits"""
    namedValues = NamedValues(
        *(("batteryEndOfLife", 31),
          ("bothFanTraysRemoved", 1),
          ("c2fPowerModuleFailureCondition", 22),
          ("cemiUpdateInProgress", 25),
          ("colossusCannotStart", 26),
          ("colossusDeniedFullPower", 24),
          ("critbit29", 29),
          ("emmLinkFailure", 15),
          ("enclosureOpenPerm", 17),
          ("fanTrayRemoved", 5),
          ("highAmbientTemp", 2),
          ("highBatteryTemperature", 16),
          ("hwComponentFailedCrit", 11),
          ("incompatControlModule", 12),
          ("lowAmbientTemp", 13),
          ("moreThanOneFanSpeedCondition", 4),
          ("multipleFansRemoved", 27),
          ("nVRAMBatteryFailed", 10),
          ("nandFailure", 30),
          ("opsPanelFailure", 14),
          ("raidDeviceIncompatible", 7),
          ("raidLostCache", 3),
          ("raidMultipleRaidSets", 9),
          ("raidOrphanCache", 8),
          ("raidSetDoubleFaulted", 0),
          ("raidSetLostblkTableFull", 6),
          ("raidsedUnresolved", 23),
          ("smartBatteryFailure", 28),
          ("staleMirrorDiskFailure", 21),
          ("sumoChannelBothFailed", 20),
          ("sumoChannelBothMissing", 18),
          ("sumoEIPFailureCOndition", 19))
    )

_EqlMemberHealthCriticalConditions_Type.__name__ = "Bits"
_EqlMemberHealthCriticalConditions_Object = MibTableColumn
eqlMemberHealthCriticalConditions = _EqlMemberHealthCriticalConditions_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 5, 1, 3),
    _EqlMemberHealthCriticalConditions_Type()
)
eqlMemberHealthCriticalConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthCriticalConditions.setStatus("current")
_EqlMemberHealthDetailsTemperatureTable_Object = MibTable
eqlMemberHealthDetailsTemperatureTable = _EqlMemberHealthDetailsTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 6)
)
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsTemperatureTable.setStatus("current")
_EqlMemberHealthDetailsTemperatureEntry_Object = MibTableRow
eqlMemberHealthDetailsTemperatureEntry = _EqlMemberHealthDetailsTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 6, 1)
)
eqlMemberHealthDetailsTemperatureEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlMemberHealthDetailsTempSensorIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsTemperatureEntry.setStatus("current")


class _EqlMemberHealthDetailsTempSensorIndex_Type(Integer32):
    """Custom type eqlMemberHealthDetailsTempSensorIndex based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40)
        )
    )
    namedValues = NamedValues(
        *(("backplaneSensor0", 2),
          ("backplaneSensor1", 3),
          ("bottomplane0d0", 23),
          ("bottomplane0d1", 24),
          ("bottomplane0d2", 25),
          ("bottomplane0d3", 26),
          ("bottomplane0d4", 27),
          ("bottomplane1d0", 28),
          ("bottomplane1d1", 29),
          ("bottomplane1d2", 30),
          ("bottomplane1d3", 31),
          ("bottomplane1d4", 32),
          ("cemi0", 15),
          ("cemi1", 16),
          ("controlModule0batteryThermistor", 17),
          ("controlModule0chipset", 5),
          ("controlModule0processor", 4),
          ("controlModule0sasController", 8),
          ("controlModule0sasExpander", 9),
          ("controlModule0sesEnclosure", 10),
          ("controlModule1batteryThermistor", 18),
          ("controlModule1chipset", 7),
          ("controlModule1processor", 6),
          ("controlModule1sasController", 11),
          ("controlModule1sasExpander", 12),
          ("controlModule1sesEnclosure", 13),
          ("integratedSystemTemperature", 1),
          ("sesOpsPanel", 14),
          ("subExpanderModule0", 19),
          ("subExpanderModule0expander0", 33),
          ("subExpanderModule0expander1", 34),
          ("subExpanderModule1", 20),
          ("subExpanderModule1expander0", 35),
          ("subExpanderModule1expander1", 36),
          ("subExpanderModule2", 21),
          ("subExpanderModule2expander0", 37),
          ("subExpanderModule2expander1", 38),
          ("subExpanderModule3", 22),
          ("subExpanderModule3expander0", 39),
          ("subExpanderModule3expander1", 40))
    )


_EqlMemberHealthDetailsTempSensorIndex_Type.__name__ = "Integer32"
_EqlMemberHealthDetailsTempSensorIndex_Object = MibTableColumn
eqlMemberHealthDetailsTempSensorIndex = _EqlMemberHealthDetailsTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 6, 1, 1),
    _EqlMemberHealthDetailsTempSensorIndex_Type()
)
eqlMemberHealthDetailsTempSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsTempSensorIndex.setStatus("current")


class _EqlMemberHealthDetailsTemperatureName_Type(DisplayString):
    """Custom type eqlMemberHealthDetailsTemperatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlMemberHealthDetailsTemperatureName_Type.__name__ = "DisplayString"
_EqlMemberHealthDetailsTemperatureName_Object = MibTableColumn
eqlMemberHealthDetailsTemperatureName = _EqlMemberHealthDetailsTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 6, 1, 2),
    _EqlMemberHealthDetailsTemperatureName_Type()
)
eqlMemberHealthDetailsTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsTemperatureName.setStatus("current")


class _EqlMemberHealthDetailsTemperatureValue_Type(Integer32):
    """Custom type eqlMemberHealthDetailsTemperatureValue based on Integer32"""
    defaultValue = 0


_EqlMemberHealthDetailsTemperatureValue_Object = MibTableColumn
eqlMemberHealthDetailsTemperatureValue = _EqlMemberHealthDetailsTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 6, 1, 3),
    _EqlMemberHealthDetailsTemperatureValue_Type()
)
eqlMemberHealthDetailsTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsTemperatureValue.setStatus("current")


class _EqlMemberHealthDetailsTemperatureCurrentState_Type(Integer32):
    """Custom type eqlMemberHealthDetailsTemperatureCurrentState based on Integer32"""
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
        *(("critical", 3),
          ("normal", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_EqlMemberHealthDetailsTemperatureCurrentState_Type.__name__ = "Integer32"
_EqlMemberHealthDetailsTemperatureCurrentState_Object = MibTableColumn
eqlMemberHealthDetailsTemperatureCurrentState = _EqlMemberHealthDetailsTemperatureCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 6, 1, 4),
    _EqlMemberHealthDetailsTemperatureCurrentState_Type()
)
eqlMemberHealthDetailsTemperatureCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsTemperatureCurrentState.setStatus("current")


class _EqlMemberHealthDetailsTemperatureHighCriticalThreshold_Type(Integer32):
    """Custom type eqlMemberHealthDetailsTemperatureHighCriticalThreshold based on Integer32"""
    defaultValue = 0


_EqlMemberHealthDetailsTemperatureHighCriticalThreshold_Object = MibTableColumn
eqlMemberHealthDetailsTemperatureHighCriticalThreshold = _EqlMemberHealthDetailsTemperatureHighCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 6, 1, 5),
    _EqlMemberHealthDetailsTemperatureHighCriticalThreshold_Type()
)
eqlMemberHealthDetailsTemperatureHighCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsTemperatureHighCriticalThreshold.setStatus("current")


class _EqlMemberHealthDetailsTemperatureHighWarningThreshold_Type(Integer32):
    """Custom type eqlMemberHealthDetailsTemperatureHighWarningThreshold based on Integer32"""
    defaultValue = 0


_EqlMemberHealthDetailsTemperatureHighWarningThreshold_Object = MibTableColumn
eqlMemberHealthDetailsTemperatureHighWarningThreshold = _EqlMemberHealthDetailsTemperatureHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 6, 1, 6),
    _EqlMemberHealthDetailsTemperatureHighWarningThreshold_Type()
)
eqlMemberHealthDetailsTemperatureHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsTemperatureHighWarningThreshold.setStatus("current")


class _EqlMemberHealthDetailsTemperatureLowCriticalThreshold_Type(Integer32):
    """Custom type eqlMemberHealthDetailsTemperatureLowCriticalThreshold based on Integer32"""
    defaultValue = 0


_EqlMemberHealthDetailsTemperatureLowCriticalThreshold_Object = MibTableColumn
eqlMemberHealthDetailsTemperatureLowCriticalThreshold = _EqlMemberHealthDetailsTemperatureLowCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 6, 1, 7),
    _EqlMemberHealthDetailsTemperatureLowCriticalThreshold_Type()
)
eqlMemberHealthDetailsTemperatureLowCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsTemperatureLowCriticalThreshold.setStatus("current")


class _EqlMemberHealthDetailsTemperatureLowWarningThreshold_Type(Integer32):
    """Custom type eqlMemberHealthDetailsTemperatureLowWarningThreshold based on Integer32"""
    defaultValue = 0


_EqlMemberHealthDetailsTemperatureLowWarningThreshold_Object = MibTableColumn
eqlMemberHealthDetailsTemperatureLowWarningThreshold = _EqlMemberHealthDetailsTemperatureLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 6, 1, 8),
    _EqlMemberHealthDetailsTemperatureLowWarningThreshold_Type()
)
eqlMemberHealthDetailsTemperatureLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsTemperatureLowWarningThreshold.setStatus("current")
_EqlMemberHealthDetailsTemperatureNameID_Type = Unsigned32
_EqlMemberHealthDetailsTemperatureNameID_Object = MibTableColumn
eqlMemberHealthDetailsTemperatureNameID = _EqlMemberHealthDetailsTemperatureNameID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 6, 1, 9),
    _EqlMemberHealthDetailsTemperatureNameID_Type()
)
eqlMemberHealthDetailsTemperatureNameID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsTemperatureNameID.setStatus("current")
_EqlMemberHealthDetailsFanTable_Object = MibTable
eqlMemberHealthDetailsFanTable = _EqlMemberHealthDetailsFanTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 7)
)
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsFanTable.setStatus("current")
_EqlMemberHealthDetailsFanEntry_Object = MibTableRow
eqlMemberHealthDetailsFanEntry = _EqlMemberHealthDetailsFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 7, 1)
)
eqlMemberHealthDetailsFanEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlMemberHealthDetailsFanIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsFanEntry.setStatus("current")


class _EqlMemberHealthDetailsFanIndex_Type(Integer32):
    """Custom type eqlMemberHealthDetailsFanIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("emm0fan0", 1),
          ("emm0fan1", 2),
          ("emm1fan0", 3),
          ("emm1fan1", 4),
          ("emm2fan0", 5),
          ("emm2fan1", 6),
          ("emm3fan0", 7),
          ("emm3fan1", 8))
    )


_EqlMemberHealthDetailsFanIndex_Type.__name__ = "Integer32"
_EqlMemberHealthDetailsFanIndex_Object = MibTableColumn
eqlMemberHealthDetailsFanIndex = _EqlMemberHealthDetailsFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 7, 1, 1),
    _EqlMemberHealthDetailsFanIndex_Type()
)
eqlMemberHealthDetailsFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsFanIndex.setStatus("current")


class _EqlMemberHealthDetailsFanName_Type(DisplayString):
    """Custom type eqlMemberHealthDetailsFanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlMemberHealthDetailsFanName_Type.__name__ = "DisplayString"
_EqlMemberHealthDetailsFanName_Object = MibTableColumn
eqlMemberHealthDetailsFanName = _EqlMemberHealthDetailsFanName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 7, 1, 2),
    _EqlMemberHealthDetailsFanName_Type()
)
eqlMemberHealthDetailsFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsFanName.setStatus("current")


class _EqlMemberHealthDetailsFanValue_Type(Unsigned32):
    """Custom type eqlMemberHealthDetailsFanValue based on Unsigned32"""
    defaultValue = 0


_EqlMemberHealthDetailsFanValue_Object = MibTableColumn
eqlMemberHealthDetailsFanValue = _EqlMemberHealthDetailsFanValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 7, 1, 3),
    _EqlMemberHealthDetailsFanValue_Type()
)
eqlMemberHealthDetailsFanValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsFanValue.setStatus("current")


class _EqlMemberHealthDetailsFanCurrentState_Type(Integer32):
    """Custom type eqlMemberHealthDetailsFanCurrentState based on Integer32"""
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
        *(("critical", 3),
          ("normal", 1),
          ("unknown", 0),
          ("warning", 2))
    )


_EqlMemberHealthDetailsFanCurrentState_Type.__name__ = "Integer32"
_EqlMemberHealthDetailsFanCurrentState_Object = MibTableColumn
eqlMemberHealthDetailsFanCurrentState = _EqlMemberHealthDetailsFanCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 7, 1, 4),
    _EqlMemberHealthDetailsFanCurrentState_Type()
)
eqlMemberHealthDetailsFanCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsFanCurrentState.setStatus("current")


class _EqlMemberHealthDetailsFanHighCriticalThreshold_Type(Unsigned32):
    """Custom type eqlMemberHealthDetailsFanHighCriticalThreshold based on Unsigned32"""
    defaultValue = 0


_EqlMemberHealthDetailsFanHighCriticalThreshold_Object = MibTableColumn
eqlMemberHealthDetailsFanHighCriticalThreshold = _EqlMemberHealthDetailsFanHighCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 7, 1, 5),
    _EqlMemberHealthDetailsFanHighCriticalThreshold_Type()
)
eqlMemberHealthDetailsFanHighCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsFanHighCriticalThreshold.setStatus("current")


class _EqlMemberHealthDetailsFanHighWarningThreshold_Type(Unsigned32):
    """Custom type eqlMemberHealthDetailsFanHighWarningThreshold based on Unsigned32"""
    defaultValue = 0


_EqlMemberHealthDetailsFanHighWarningThreshold_Object = MibTableColumn
eqlMemberHealthDetailsFanHighWarningThreshold = _EqlMemberHealthDetailsFanHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 7, 1, 6),
    _EqlMemberHealthDetailsFanHighWarningThreshold_Type()
)
eqlMemberHealthDetailsFanHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsFanHighWarningThreshold.setStatus("current")


class _EqlMemberHealthDetailsFanLowCriticalThreshold_Type(Unsigned32):
    """Custom type eqlMemberHealthDetailsFanLowCriticalThreshold based on Unsigned32"""
    defaultValue = 0


_EqlMemberHealthDetailsFanLowCriticalThreshold_Object = MibTableColumn
eqlMemberHealthDetailsFanLowCriticalThreshold = _EqlMemberHealthDetailsFanLowCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 7, 1, 7),
    _EqlMemberHealthDetailsFanLowCriticalThreshold_Type()
)
eqlMemberHealthDetailsFanLowCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsFanLowCriticalThreshold.setStatus("current")


class _EqlMemberHealthDetailsFanLowWarningThreshold_Type(Unsigned32):
    """Custom type eqlMemberHealthDetailsFanLowWarningThreshold based on Unsigned32"""
    defaultValue = 0


_EqlMemberHealthDetailsFanLowWarningThreshold_Object = MibTableColumn
eqlMemberHealthDetailsFanLowWarningThreshold = _EqlMemberHealthDetailsFanLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 7, 1, 8),
    _EqlMemberHealthDetailsFanLowWarningThreshold_Type()
)
eqlMemberHealthDetailsFanLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsFanLowWarningThreshold.setStatus("current")
_EqlMemberHealthDetailsFanNameID_Type = Unsigned32
_EqlMemberHealthDetailsFanNameID_Object = MibTableColumn
eqlMemberHealthDetailsFanNameID = _EqlMemberHealthDetailsFanNameID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 7, 1, 9),
    _EqlMemberHealthDetailsFanNameID_Type()
)
eqlMemberHealthDetailsFanNameID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsFanNameID.setStatus("current")
_EqlMemberHealthDetailsPowerSupplyTable_Object = MibTable
eqlMemberHealthDetailsPowerSupplyTable = _EqlMemberHealthDetailsPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 8)
)
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsPowerSupplyTable.setStatus("current")
_EqlMemberHealthDetailsPowerSupplyEntry_Object = MibTableRow
eqlMemberHealthDetailsPowerSupplyEntry = _EqlMemberHealthDetailsPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 8, 1)
)
eqlMemberHealthDetailsPowerSupplyEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlMemberHealthDetailsPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsPowerSupplyEntry.setStatus("current")


class _EqlMemberHealthDetailsPowerSupplyIndex_Type(Integer32):
    """Custom type eqlMemberHealthDetailsPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("powerSupply0", 1),
          ("powerSupply1", 2),
          ("powerSupply2", 3))
    )


_EqlMemberHealthDetailsPowerSupplyIndex_Type.__name__ = "Integer32"
_EqlMemberHealthDetailsPowerSupplyIndex_Object = MibTableColumn
eqlMemberHealthDetailsPowerSupplyIndex = _EqlMemberHealthDetailsPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 8, 1, 1),
    _EqlMemberHealthDetailsPowerSupplyIndex_Type()
)
eqlMemberHealthDetailsPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsPowerSupplyIndex.setStatus("current")


class _EqlMemberHealthDetailsPowerSupplyName_Type(DisplayString):
    """Custom type eqlMemberHealthDetailsPowerSupplyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlMemberHealthDetailsPowerSupplyName_Type.__name__ = "DisplayString"
_EqlMemberHealthDetailsPowerSupplyName_Object = MibTableColumn
eqlMemberHealthDetailsPowerSupplyName = _EqlMemberHealthDetailsPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 8, 1, 2),
    _EqlMemberHealthDetailsPowerSupplyName_Type()
)
eqlMemberHealthDetailsPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsPowerSupplyName.setStatus("current")


class _EqlMemberHealthDetailsPowerSupplyCurrentState_Type(Integer32):
    """Custom type eqlMemberHealthDetailsPowerSupplyCurrentState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed-or-no-data", 3),
          ("no-ac-power", 2),
          ("on-and-operating", 1))
    )


_EqlMemberHealthDetailsPowerSupplyCurrentState_Type.__name__ = "Integer32"
_EqlMemberHealthDetailsPowerSupplyCurrentState_Object = MibTableColumn
eqlMemberHealthDetailsPowerSupplyCurrentState = _EqlMemberHealthDetailsPowerSupplyCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 8, 1, 3),
    _EqlMemberHealthDetailsPowerSupplyCurrentState_Type()
)
eqlMemberHealthDetailsPowerSupplyCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsPowerSupplyCurrentState.setStatus("current")


class _EqlMemberHealthDetailsPowerSupplyFanStatus_Type(Integer32):
    """Custom type eqlMemberHealthDetailsPowerSupplyFanStatus based on Integer32"""
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
        *(("fan-is-operational", 1),
          ("fan-not-operational", 2),
          ("not-applicable", 0))
    )


_EqlMemberHealthDetailsPowerSupplyFanStatus_Type.__name__ = "Integer32"
_EqlMemberHealthDetailsPowerSupplyFanStatus_Object = MibTableColumn
eqlMemberHealthDetailsPowerSupplyFanStatus = _EqlMemberHealthDetailsPowerSupplyFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 8, 1, 4),
    _EqlMemberHealthDetailsPowerSupplyFanStatus_Type()
)
eqlMemberHealthDetailsPowerSupplyFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsPowerSupplyFanStatus.setStatus("current")


class _EqlMemberHealthDetailsPowerSupplyFirmwareVersion_Type(DisplayString):
    """Custom type eqlMemberHealthDetailsPowerSupplyFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlMemberHealthDetailsPowerSupplyFirmwareVersion_Type.__name__ = "DisplayString"
_EqlMemberHealthDetailsPowerSupplyFirmwareVersion_Object = MibTableColumn
eqlMemberHealthDetailsPowerSupplyFirmwareVersion = _EqlMemberHealthDetailsPowerSupplyFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 8, 1, 5),
    _EqlMemberHealthDetailsPowerSupplyFirmwareVersion_Type()
)
eqlMemberHealthDetailsPowerSupplyFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsPowerSupplyFirmwareVersion.setStatus("current")
_EqlMemberHealthDetailsPowerSupplyNameID_Type = Unsigned32
_EqlMemberHealthDetailsPowerSupplyNameID_Object = MibTableColumn
eqlMemberHealthDetailsPowerSupplyNameID = _EqlMemberHealthDetailsPowerSupplyNameID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 8, 1, 6),
    _EqlMemberHealthDetailsPowerSupplyNameID_Type()
)
eqlMemberHealthDetailsPowerSupplyNameID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHealthDetailsPowerSupplyNameID.setStatus("current")
_EqlMemberIdentificationTable_Object = MibTable
eqlMemberIdentificationTable = _EqlMemberIdentificationTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 9)
)
if mibBuilder.loadTexts:
    eqlMemberIdentificationTable.setStatus("current")
_EqlMemberIdentificationEntry_Object = MibTableRow
eqlMemberIdentificationEntry = _EqlMemberIdentificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    eqlMemberIdentificationEntry.setStatus("current")


class _EqlMemberIdentificationLEDsBlinking_Type(TruthValue):
    """Custom type eqlMemberIdentificationLEDsBlinking based on TruthValue"""


_EqlMemberIdentificationLEDsBlinking_Object = MibTableColumn
eqlMemberIdentificationLEDsBlinking = _EqlMemberIdentificationLEDsBlinking_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 9, 1, 1),
    _EqlMemberIdentificationLEDsBlinking_Type()
)
eqlMemberIdentificationLEDsBlinking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberIdentificationLEDsBlinking.setStatus("current")
_EqlMemberStorageTable_Object = MibTable
eqlMemberStorageTable = _EqlMemberStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 10)
)
if mibBuilder.loadTexts:
    eqlMemberStorageTable.setStatus("current")
_EqlMemberStorageEntry_Object = MibTableRow
eqlMemberStorageEntry = _EqlMemberStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    eqlMemberStorageEntry.setStatus("current")
_EqlMemberTotalStorage_Type = Integer32
_EqlMemberTotalStorage_Object = MibTableColumn
eqlMemberTotalStorage = _EqlMemberTotalStorage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 10, 1, 1),
    _EqlMemberTotalStorage_Type()
)
eqlMemberTotalStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberTotalStorage.setStatus("current")
_EqlMemberUsedStorage_Type = Integer32
_EqlMemberUsedStorage_Object = MibTableColumn
eqlMemberUsedStorage = _EqlMemberUsedStorage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 10, 1, 2),
    _EqlMemberUsedStorage_Type()
)
eqlMemberUsedStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberUsedStorage.setStatus("current")
_EqlMemberSnapStorage_Type = Integer32
_EqlMemberSnapStorage_Object = MibTableColumn
eqlMemberSnapStorage = _EqlMemberSnapStorage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 10, 1, 3),
    _EqlMemberSnapStorage_Type()
)
eqlMemberSnapStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberSnapStorage.setStatus("current")
_EqlMemberReplStorage_Type = Integer32
_EqlMemberReplStorage_Object = MibTableColumn
eqlMemberReplStorage = _EqlMemberReplStorage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 10, 1, 4),
    _EqlMemberReplStorage_Type()
)
eqlMemberReplStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberReplStorage.setStatus("current")
_EqlMemberVirtualStorage_Type = Counter64
_EqlMemberVirtualStorage_Object = MibTableColumn
eqlMemberVirtualStorage = _EqlMemberVirtualStorage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 10, 1, 5),
    _EqlMemberVirtualStorage_Type()
)
eqlMemberVirtualStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberVirtualStorage.setStatus("current")
_EqlMemberCompressionStackStorage_Type = Counter64
_EqlMemberCompressionStackStorage_Object = MibTableColumn
eqlMemberCompressionStackStorage = _EqlMemberCompressionStackStorage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 10, 1, 6),
    _EqlMemberCompressionStackStorage_Type()
)
eqlMemberCompressionStackStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberCompressionStackStorage.setStatus("current")
_EqlMemberChassisTable_Object = MibTable
eqlMemberChassisTable = _EqlMemberChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 11)
)
if mibBuilder.loadTexts:
    eqlMemberChassisTable.setStatus("current")
_EqlMemberChassisEntry_Object = MibTableRow
eqlMemberChassisEntry = _EqlMemberChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    eqlMemberChassisEntry.setStatus("current")


class _EqlMemberModel_Type(DisplayString):
    """Custom type eqlMemberModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlMemberModel_Type.__name__ = "DisplayString"
_EqlMemberModel_Object = MibTableColumn
eqlMemberModel = _EqlMemberModel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 11, 1, 1),
    _EqlMemberModel_Type()
)
eqlMemberModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberModel.setStatus("current")


class _EqlMemberSerialNumber_Type(DisplayString):
    """Custom type eqlMemberSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlMemberSerialNumber_Type.__name__ = "DisplayString"
_EqlMemberSerialNumber_Object = MibTableColumn
eqlMemberSerialNumber = _EqlMemberSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 11, 1, 2),
    _EqlMemberSerialNumber_Type()
)
eqlMemberSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberSerialNumber.setStatus("current")


class _EqlMemberNumberOfControllers_Type(Integer32):
    """Custom type eqlMemberNumberOfControllers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dual", 2),
          ("single", 1))
    )


_EqlMemberNumberOfControllers_Type.__name__ = "Integer32"
_EqlMemberNumberOfControllers_Object = MibTableColumn
eqlMemberNumberOfControllers = _EqlMemberNumberOfControllers_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 11, 1, 3),
    _EqlMemberNumberOfControllers_Type()
)
eqlMemberNumberOfControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberNumberOfControllers.setStatus("current")
_EqlMemberNumberOfDisks_Type = Integer32
_EqlMemberNumberOfDisks_Object = MibTableColumn
eqlMemberNumberOfDisks = _EqlMemberNumberOfDisks_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 11, 1, 4),
    _EqlMemberNumberOfDisks_Type()
)
eqlMemberNumberOfDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberNumberOfDisks.setStatus("current")
_EqlMemberCacheSize_Type = Integer32
_EqlMemberCacheSize_Object = MibTableColumn
eqlMemberCacheSize = _EqlMemberCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 11, 1, 5),
    _EqlMemberCacheSize_Type()
)
eqlMemberCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberCacheSize.setStatus("current")


class _EqlMemberCacheMode_Type(Integer32):
    """Custom type eqlMemberCacheMode based on Integer32"""
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
        *(("unknown", 0),
          ("write-back", 2),
          ("write-thru", 1))
    )


_EqlMemberCacheMode_Type.__name__ = "Integer32"
_EqlMemberCacheMode_Object = MibTableColumn
eqlMemberCacheMode = _EqlMemberCacheMode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 11, 1, 6),
    _EqlMemberCacheMode_Type()
)
eqlMemberCacheMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberCacheMode.setStatus("current")


class _EqlMemberChassisType_Type(Integer32):
    """Custom type eqlMemberChassisType based on Integer32"""
    defaultValue = 0

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("t1403", 1),
          ("t1603", 2),
          ("t4835", 3),
          ("tDELL2WB1425V1", 7),
          ("tDELLSBB2u1235", 4),
          ("tDELLSBB2u2425", 5),
          ("tDELLSBB4u2435", 6),
          ("tDELLSBB5u6035", 8),
          ("unknown", 0))
    )


_EqlMemberChassisType_Type.__name__ = "Integer32"
_EqlMemberChassisType_Object = MibTableColumn
eqlMemberChassisType = _EqlMemberChassisType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 11, 1, 7),
    _EqlMemberChassisType_Type()
)
eqlMemberChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberChassisType.setStatus("current")


class _EqlMemberServiceTag_Type(DisplayString):
    """Custom type eqlMemberServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlMemberServiceTag_Type.__name__ = "DisplayString"
_EqlMemberServiceTag_Object = MibTableColumn
eqlMemberServiceTag = _EqlMemberServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 11, 1, 8),
    _EqlMemberServiceTag_Type()
)
eqlMemberServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberServiceTag.setStatus("current")


class _EqlMemberProductFamily_Type(DisplayString):
    """Custom type eqlMemberProductFamily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlMemberProductFamily_Type.__name__ = "DisplayString"
_EqlMemberProductFamily_Object = MibTableColumn
eqlMemberProductFamily = _EqlMemberProductFamily_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 11, 1, 9),
    _EqlMemberProductFamily_Type()
)
eqlMemberProductFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberProductFamily.setStatus("current")


class _EqlMemberChassisFlags_Type(Bits):
    """Custom type eqlMemberChassisFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("flag10", 10),
          ("flag11", 11),
          ("flag12", 12),
          ("flag13", 13),
          ("flag14", 14),
          ("flag15", 15),
          ("flag16", 16),
          ("flag17", 17),
          ("flag18", 18),
          ("flag19", 19),
          ("flag2", 2),
          ("flag20", 20),
          ("flag21", 21),
          ("flag22", 22),
          ("flag23", 23),
          ("flag24", 24),
          ("flag25", 25),
          ("flag26", 26),
          ("flag27", 27),
          ("flag28", 28),
          ("flag29", 29),
          ("flag3", 3),
          ("flag30", 30),
          ("flag31", 31),
          ("flag4", 4),
          ("flag5", 5),
          ("flag6", 6),
          ("flag7", 7),
          ("flag8", 8),
          ("flag9", 9),
          ("isAccelerated", 0),
          ("isAllSedDisks", 1))
    )

_EqlMemberChassisFlags_Type.__name__ = "Bits"
_EqlMemberChassisFlags_Object = MibTableColumn
eqlMemberChassisFlags = _EqlMemberChassisFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 11, 1, 10),
    _EqlMemberChassisFlags_Type()
)
eqlMemberChassisFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberChassisFlags.setStatus("current")


class _EqlMemberChassisDiskSectorSize_Type(Integer32):
    """Custom type eqlMemberChassisDiskSectorSize based on Integer32"""
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
        *(("sector-size-4096-bytes", 1),
          ("sector-size-512-bytes", 0),
          ("sector-size-mixed", 3),
          ("sector-size-unknown", 2))
    )


_EqlMemberChassisDiskSectorSize_Type.__name__ = "Integer32"
_EqlMemberChassisDiskSectorSize_Object = MibTableColumn
eqlMemberChassisDiskSectorSize = _EqlMemberChassisDiskSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 11, 1, 11),
    _EqlMemberChassisDiskSectorSize_Type()
)
eqlMemberChassisDiskSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberChassisDiskSectorSize.setStatus("current")
_EqlMemberConnTable_Object = MibTable
eqlMemberConnTable = _EqlMemberConnTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 12)
)
if mibBuilder.loadTexts:
    eqlMemberConnTable.setStatus("current")
_EqlMemberConnEntry_Object = MibTableRow
eqlMemberConnEntry = _EqlMemberConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    eqlMemberConnEntry.setStatus("current")
_EqlMemberNumberOfConnections_Type = Integer32
_EqlMemberNumberOfConnections_Object = MibTableColumn
eqlMemberNumberOfConnections = _EqlMemberNumberOfConnections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 12, 1, 1),
    _EqlMemberNumberOfConnections_Type()
)
eqlMemberNumberOfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberNumberOfConnections.setStatus("current")
_EqlMemberReadLatency_Type = Counter64
_EqlMemberReadLatency_Object = MibTableColumn
eqlMemberReadLatency = _EqlMemberReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 12, 1, 2),
    _EqlMemberReadLatency_Type()
)
eqlMemberReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberReadLatency.setStatus("current")
_EqlMemberWriteLatency_Type = Counter64
_EqlMemberWriteLatency_Object = MibTableColumn
eqlMemberWriteLatency = _EqlMemberWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 12, 1, 3),
    _EqlMemberWriteLatency_Type()
)
eqlMemberWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberWriteLatency.setStatus("current")
_EqlMemberReadAvgLatency_Type = Gauge32
_EqlMemberReadAvgLatency_Object = MibTableColumn
eqlMemberReadAvgLatency = _EqlMemberReadAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 12, 1, 4),
    _EqlMemberReadAvgLatency_Type()
)
eqlMemberReadAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberReadAvgLatency.setStatus("current")
_EqlMemberWriteAvgLatency_Type = Gauge32
_EqlMemberWriteAvgLatency_Object = MibTableColumn
eqlMemberWriteAvgLatency = _EqlMemberWriteAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 12, 1, 5),
    _EqlMemberWriteAvgLatency_Type()
)
eqlMemberWriteAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberWriteAvgLatency.setStatus("current")
_EqlMemberReadOpCount_Type = Counter64
_EqlMemberReadOpCount_Object = MibTableColumn
eqlMemberReadOpCount = _EqlMemberReadOpCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 12, 1, 6),
    _EqlMemberReadOpCount_Type()
)
eqlMemberReadOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberReadOpCount.setStatus("current")
_EqlMemberWriteOpCount_Type = Counter64
_EqlMemberWriteOpCount_Object = MibTableColumn
eqlMemberWriteOpCount = _EqlMemberWriteOpCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 12, 1, 7),
    _EqlMemberWriteOpCount_Type()
)
eqlMemberWriteOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberWriteOpCount.setStatus("current")
_EqlMemberTxData_Type = Counter64
_EqlMemberTxData_Object = MibTableColumn
eqlMemberTxData = _EqlMemberTxData_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 12, 1, 8),
    _EqlMemberTxData_Type()
)
eqlMemberTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberTxData.setStatus("current")
_EqlMemberRxData_Type = Counter64
_EqlMemberRxData_Object = MibTableColumn
eqlMemberRxData = _EqlMemberRxData_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 12, 1, 9),
    _EqlMemberRxData_Type()
)
eqlMemberRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberRxData.setStatus("current")
_EqlMemberNumberOfExtConnections_Type = Integer32
_EqlMemberNumberOfExtConnections_Object = MibTableColumn
eqlMemberNumberOfExtConnections = _EqlMemberNumberOfExtConnections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 12, 1, 10),
    _EqlMemberNumberOfExtConnections_Type()
)
eqlMemberNumberOfExtConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberNumberOfExtConnections.setStatus("current")
_EqlMemberRAIDTable_Object = MibTable
eqlMemberRAIDTable = _EqlMemberRAIDTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 13)
)
if mibBuilder.loadTexts:
    eqlMemberRAIDTable.setStatus("current")
_EqlMemberRAIDEntry_Object = MibTableRow
eqlMemberRAIDEntry = _EqlMemberRAIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 13, 1)
)
if mibBuilder.loadTexts:
    eqlMemberRAIDEntry.setStatus("current")


class _EqlMemberRaidStatus_Type(Integer32):
    """Custom type eqlMemberRaidStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("catastrophicLoss", 6),
          ("degraded", 2),
          ("expanding", 7),
          ("failed", 5),
          ("mirroring", 8),
          ("ok", 1),
          ("reconstructing", 4),
          ("verifying", 3))
    )


_EqlMemberRaidStatus_Type.__name__ = "Integer32"
_EqlMemberRaidStatus_Object = MibTableColumn
eqlMemberRaidStatus = _EqlMemberRaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 13, 1, 1),
    _EqlMemberRaidStatus_Type()
)
eqlMemberRaidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberRaidStatus.setStatus("current")


class _EqlMemberRaidPercentage_Type(Integer32):
    """Custom type eqlMemberRaidPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqlMemberRaidPercentage_Type.__name__ = "Integer32"
_EqlMemberRaidPercentage_Object = MibTableColumn
eqlMemberRaidPercentage = _EqlMemberRaidPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 13, 1, 2),
    _EqlMemberRaidPercentage_Type()
)
eqlMemberRaidPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberRaidPercentage.setStatus("current")


class _EqlMemberLostRaidBlocks_Type(Integer32):
    """Custom type eqlMemberLostRaidBlocks based on Integer32"""
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


_EqlMemberLostRaidBlocks_Type.__name__ = "Integer32"
_EqlMemberLostRaidBlocks_Object = MibTableColumn
eqlMemberLostRaidBlocks = _EqlMemberLostRaidBlocks_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 13, 1, 3),
    _EqlMemberLostRaidBlocks_Type()
)
eqlMemberLostRaidBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberLostRaidBlocks.setStatus("current")
_EqlMemberNumberOfSpares_Type = Integer32
_EqlMemberNumberOfSpares_Object = MibTableColumn
eqlMemberNumberOfSpares = _EqlMemberNumberOfSpares_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 13, 1, 4),
    _EqlMemberNumberOfSpares_Type()
)
eqlMemberNumberOfSpares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberNumberOfSpares.setStatus("current")


class _EqlMemberRaidProgress_Type(Unsigned32):
    """Custom type eqlMemberRaidProgress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_EqlMemberRaidProgress_Type.__name__ = "Unsigned32"
_EqlMemberRaidProgress_Object = MibTableColumn
eqlMemberRaidProgress = _EqlMemberRaidProgress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 13, 1, 5),
    _EqlMemberRaidProgress_Type()
)
eqlMemberRaidProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberRaidProgress.setStatus("current")
_EqlMemberPSGMapTable_Object = MibTable
eqlMemberPSGMapTable = _EqlMemberPSGMapTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 14)
)
if mibBuilder.loadTexts:
    eqlMemberPSGMapTable.setStatus("current")
_EqlMemberPSGMapEntry_Object = MibTableRow
eqlMemberPSGMapEntry = _EqlMemberPSGMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 14, 1)
)
if mibBuilder.loadTexts:
    eqlMemberPSGMapEntry.setStatus("current")
_EqlMemberShortId_Type = Integer32
_EqlMemberShortId_Object = MibTableColumn
eqlMemberShortId = _EqlMemberShortId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 14, 1, 1),
    _EqlMemberShortId_Type()
)
eqlMemberShortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberShortId.setStatus("current")
_EqlDriveGroupTable_Object = MibTable
eqlDriveGroupTable = _EqlDriveGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 15)
)
if mibBuilder.loadTexts:
    eqlDriveGroupTable.setStatus("current")
_EqlDriveGroupEntry_Object = MibTableRow
eqlDriveGroupEntry = _EqlDriveGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 15, 1)
)
eqlDriveGroupEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlDriveGroupIndex"),
)
if mibBuilder.loadTexts:
    eqlDriveGroupEntry.setStatus("current")
_EqlDriveGroupIndex_Type = Unsigned32
_EqlDriveGroupIndex_Object = MibTableColumn
eqlDriveGroupIndex = _EqlDriveGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 15, 1, 1),
    _EqlDriveGroupIndex_Type()
)
eqlDriveGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlDriveGroupIndex.setStatus("current")


class _EqlDriveGroupStoragePoolIndex_Type(Unsigned32):
    """Custom type eqlDriveGroupStoragePoolIndex based on Unsigned32"""
    defaultValue = 1


_EqlDriveGroupStoragePoolIndex_Object = MibTableColumn
eqlDriveGroupStoragePoolIndex = _EqlDriveGroupStoragePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 15, 1, 2),
    _EqlDriveGroupStoragePoolIndex_Type()
)
eqlDriveGroupStoragePoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDriveGroupStoragePoolIndex.setStatus("current")


class _EqlDriveGroupRAIDPolicy_Type(Integer32):
    """Custom type eqlDriveGroupRAIDPolicy based on Integer32"""
    defaultValue = 0

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("hvs-storage", 10),
          ("raid10", 2),
          ("raid10-nospares", 5),
          ("raid5", 3),
          ("raid5-nospares", 6),
          ("raid50", 1),
          ("raid50-nospares", 4),
          ("raid6", 7),
          ("raid6-accelerated", 9),
          ("raid6-nospares", 8),
          ("unconfigured", 0))
    )


_EqlDriveGroupRAIDPolicy_Type.__name__ = "Integer32"
_EqlDriveGroupRAIDPolicy_Object = MibTableColumn
eqlDriveGroupRAIDPolicy = _EqlDriveGroupRAIDPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 15, 1, 3),
    _EqlDriveGroupRAIDPolicy_Type()
)
eqlDriveGroupRAIDPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDriveGroupRAIDPolicy.setStatus("current")
_EqlDriveGroupOpsTable_Object = MibTable
eqlDriveGroupOpsTable = _EqlDriveGroupOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 16)
)
if mibBuilder.loadTexts:
    eqlDriveGroupOpsTable.setStatus("current")
_EqlDriveGroupOpsEntry_Object = MibTableRow
eqlDriveGroupOpsEntry = _EqlDriveGroupOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 16, 1)
)
eqlDriveGroupOpsEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlDriveGroupIndex"),
    (0, "EQLMEMBER-MIB", "eqlDriveGroupOpsIndex"),
)
if mibBuilder.loadTexts:
    eqlDriveGroupOpsEntry.setStatus("current")
_EqlDriveGroupOpsIndex_Type = Unsigned32
_EqlDriveGroupOpsIndex_Object = MibTableColumn
eqlDriveGroupOpsIndex = _EqlDriveGroupOpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 16, 1, 1),
    _EqlDriveGroupOpsIndex_Type()
)
eqlDriveGroupOpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlDriveGroupOpsIndex.setStatus("current")
_EqlDriveGroupOpsRowStatus_Type = RowStatus
_EqlDriveGroupOpsRowStatus_Object = MibTableColumn
eqlDriveGroupOpsRowStatus = _EqlDriveGroupOpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 16, 1, 2),
    _EqlDriveGroupOpsRowStatus_Type()
)
eqlDriveGroupOpsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDriveGroupOpsRowStatus.setStatus("current")


class _EqlDriveGroupOpsOperation_Type(Integer32):
    """Custom type eqlDriveGroupOpsOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("movePool", 1),
          ("none", 0),
          ("vacate", 2))
    )


_EqlDriveGroupOpsOperation_Type.__name__ = "Integer32"
_EqlDriveGroupOpsOperation_Object = MibTableColumn
eqlDriveGroupOpsOperation = _EqlDriveGroupOpsOperation_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 16, 1, 3),
    _EqlDriveGroupOpsOperation_Type()
)
eqlDriveGroupOpsOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDriveGroupOpsOperation.setStatus("current")


class _EqlDriveGroupOpsExec_Type(Integer32):
    """Custom type eqlDriveGroupOpsExec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 1),
          ("failed", 2),
          ("none", 0))
    )


_EqlDriveGroupOpsExec_Type.__name__ = "Integer32"
_EqlDriveGroupOpsExec_Object = MibTableColumn
eqlDriveGroupOpsExec = _EqlDriveGroupOpsExec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 16, 1, 4),
    _EqlDriveGroupOpsExec_Type()
)
eqlDriveGroupOpsExec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDriveGroupOpsExec.setStatus("current")
_EqlDriveGroupOpsStartTime_Type = Counter32
_EqlDriveGroupOpsStartTime_Object = MibTableColumn
eqlDriveGroupOpsStartTime = _EqlDriveGroupOpsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 16, 1, 5),
    _EqlDriveGroupOpsStartTime_Type()
)
eqlDriveGroupOpsStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDriveGroupOpsStartTime.setStatus("current")


class _EqlDriveGroupOpsStoragePoolSourceIndex_Type(Unsigned32):
    """Custom type eqlDriveGroupOpsStoragePoolSourceIndex based on Unsigned32"""
    defaultValue = 1


_EqlDriveGroupOpsStoragePoolSourceIndex_Object = MibTableColumn
eqlDriveGroupOpsStoragePoolSourceIndex = _EqlDriveGroupOpsStoragePoolSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 16, 1, 6),
    _EqlDriveGroupOpsStoragePoolSourceIndex_Type()
)
eqlDriveGroupOpsStoragePoolSourceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDriveGroupOpsStoragePoolSourceIndex.setStatus("current")


class _EqlDriveGroupOpsStoragePoolDestinationIndex_Type(Unsigned32):
    """Custom type eqlDriveGroupOpsStoragePoolDestinationIndex based on Unsigned32"""
    defaultValue = 1


_EqlDriveGroupOpsStoragePoolDestinationIndex_Object = MibTableColumn
eqlDriveGroupOpsStoragePoolDestinationIndex = _EqlDriveGroupOpsStoragePoolDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 16, 1, 7),
    _EqlDriveGroupOpsStoragePoolDestinationIndex_Type()
)
eqlDriveGroupOpsStoragePoolDestinationIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlDriveGroupOpsStoragePoolDestinationIndex.setStatus("current")
_EqlDriveGroupOpsVolBalCommandIndex_Type = Unsigned32
_EqlDriveGroupOpsVolBalCommandIndex_Object = MibTableColumn
eqlDriveGroupOpsVolBalCommandIndex = _EqlDriveGroupOpsVolBalCommandIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 16, 1, 8),
    _EqlDriveGroupOpsVolBalCommandIndex_Type()
)
eqlDriveGroupOpsVolBalCommandIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDriveGroupOpsVolBalCommandIndex.setStatus("current")
_EqlDriveGroupOpsVolBalCommandiscsiLocalMemberId_Type = Unsigned32
_EqlDriveGroupOpsVolBalCommandiscsiLocalMemberId_Object = MibTableColumn
eqlDriveGroupOpsVolBalCommandiscsiLocalMemberId = _EqlDriveGroupOpsVolBalCommandiscsiLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 16, 1, 9),
    _EqlDriveGroupOpsVolBalCommandiscsiLocalMemberId_Type()
)
eqlDriveGroupOpsVolBalCommandiscsiLocalMemberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDriveGroupOpsVolBalCommandiscsiLocalMemberId.setStatus("current")
_EqlAdminAccountMemberTable_Object = MibTable
eqlAdminAccountMemberTable = _EqlAdminAccountMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 17)
)
if mibBuilder.loadTexts:
    eqlAdminAccountMemberTable.setStatus("current")
_EqlAdminAccountMemberEntry_Object = MibTableRow
eqlAdminAccountMemberEntry = _EqlAdminAccountMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 17, 1)
)
eqlAdminAccountMemberEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlAdminAccountMemberEntry.setStatus("current")


class _EqlAdminAccountMemberAccess_Type(Integer32):
    """Custom type eqlAdminAccountMemberAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 1),
          ("read-write", 2))
    )


_EqlAdminAccountMemberAccess_Type.__name__ = "Integer32"
_EqlAdminAccountMemberAccess_Object = MibTableColumn
eqlAdminAccountMemberAccess = _EqlAdminAccountMemberAccess_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 17, 1, 1),
    _EqlAdminAccountMemberAccess_Type()
)
eqlAdminAccountMemberAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAdminAccountMemberAccess.setStatus("current")
_EqlDriveGroupOpsStatusTable_Object = MibTable
eqlDriveGroupOpsStatusTable = _EqlDriveGroupOpsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 18)
)
if mibBuilder.loadTexts:
    eqlDriveGroupOpsStatusTable.setStatus("current")
_EqlDriveGroupOpsStatusEntry_Object = MibTableRow
eqlDriveGroupOpsStatusEntry = _EqlDriveGroupOpsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 18, 1)
)
if mibBuilder.loadTexts:
    eqlDriveGroupOpsStatusEntry.setStatus("current")
_EqlDriveGroupOpsStatusCompletePct_Type = Unsigned32
_EqlDriveGroupOpsStatusCompletePct_Object = MibTableColumn
eqlDriveGroupOpsStatusCompletePct = _EqlDriveGroupOpsStatusCompletePct_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 18, 1, 1),
    _EqlDriveGroupOpsStatusCompletePct_Type()
)
eqlDriveGroupOpsStatusCompletePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDriveGroupOpsStatusCompletePct.setStatus("current")
_EqlMemberOpsTable_Object = MibTable
eqlMemberOpsTable = _EqlMemberOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 19)
)
if mibBuilder.loadTexts:
    eqlMemberOpsTable.setStatus("current")
_EqlMemberOpsEntry_Object = MibTableRow
eqlMemberOpsEntry = _EqlMemberOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 19, 1)
)
eqlMemberOpsEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlMemberOpsIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberOpsEntry.setStatus("current")
_EqlMemberOpsIndex_Type = Unsigned32
_EqlMemberOpsIndex_Object = MibTableColumn
eqlMemberOpsIndex = _EqlMemberOpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 19, 1, 1),
    _EqlMemberOpsIndex_Type()
)
eqlMemberOpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlMemberOpsIndex.setStatus("current")
_EqlMemberOpsRowStatus_Type = RowStatus
_EqlMemberOpsRowStatus_Object = MibTableColumn
eqlMemberOpsRowStatus = _EqlMemberOpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 19, 1, 2),
    _EqlMemberOpsRowStatus_Type()
)
eqlMemberOpsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberOpsRowStatus.setStatus("current")


class _EqlMemberOpsOperation_Type(Integer32):
    """Custom type eqlMemberOpsOperation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("cli-update", 9),
          ("delete-pending", 7),
          ("diagnose", 3),
          ("install-software-component", 8),
          ("none", 0),
          ("restart", 5),
          ("shutdown", 6),
          ("update", 4))
    )


_EqlMemberOpsOperation_Type.__name__ = "Integer32"
_EqlMemberOpsOperation_Object = MibTableColumn
eqlMemberOpsOperation = _EqlMemberOpsOperation_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 19, 1, 3),
    _EqlMemberOpsOperation_Type()
)
eqlMemberOpsOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberOpsOperation.setStatus("current")


class _EqlMemberOpsExec_Type(Integer32):
    """Custom type eqlMemberOpsExec based on Integer32"""
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
        *(("cancel", 1),
          ("failed", 2),
          ("none", 0))
    )


_EqlMemberOpsExec_Type.__name__ = "Integer32"
_EqlMemberOpsExec_Object = MibTableColumn
eqlMemberOpsExec = _EqlMemberOpsExec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 19, 1, 4),
    _EqlMemberOpsExec_Type()
)
eqlMemberOpsExec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberOpsExec.setStatus("current")


class _EqlMemberOpsCompletePct_Type(Integer32):
    """Custom type eqlMemberOpsCompletePct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqlMemberOpsCompletePct_Type.__name__ = "Integer32"
_EqlMemberOpsCompletePct_Object = MibTableColumn
eqlMemberOpsCompletePct = _EqlMemberOpsCompletePct_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 19, 1, 5),
    _EqlMemberOpsCompletePct_Type()
)
eqlMemberOpsCompletePct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberOpsCompletePct.setStatus("current")


class _EqlMemberOpsOperationArg_Type(DisplayString):
    """Custom type eqlMemberOpsOperationArg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlMemberOpsOperationArg_Type.__name__ = "DisplayString"
_EqlMemberOpsOperationArg_Object = MibTableColumn
eqlMemberOpsOperationArg = _EqlMemberOpsOperationArg_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 19, 1, 6),
    _EqlMemberOpsOperationArg_Type()
)
eqlMemberOpsOperationArg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberOpsOperationArg.setStatus("current")


class _EqlMemberOpsOperationStatus_Type(Integer32):
    """Custom type eqlMemberOpsOperationStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("success", 0))
    )


_EqlMemberOpsOperationStatus_Type.__name__ = "Integer32"
_EqlMemberOpsOperationStatus_Object = MibTableColumn
eqlMemberOpsOperationStatus = _EqlMemberOpsOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 19, 1, 7),
    _EqlMemberOpsOperationStatus_Type()
)
eqlMemberOpsOperationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberOpsOperationStatus.setStatus("current")
_EqlMemberOpsStartTime_Type = Unsigned32
_EqlMemberOpsStartTime_Object = MibTableColumn
eqlMemberOpsStartTime = _EqlMemberOpsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 19, 1, 8),
    _EqlMemberOpsStartTime_Type()
)
eqlMemberOpsStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberOpsStartTime.setStatus("current")


class _EqlMemberOpsOperationArg1_Type(DisplayString):
    """Custom type eqlMemberOpsOperationArg1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlMemberOpsOperationArg1_Type.__name__ = "DisplayString"
_EqlMemberOpsOperationArg1_Object = MibTableColumn
eqlMemberOpsOperationArg1 = _EqlMemberOpsOperationArg1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 19, 1, 9),
    _EqlMemberOpsOperationArg1_Type()
)
eqlMemberOpsOperationArg1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberOpsOperationArg1.setStatus("current")
_EqlMemberHWComponentTable_Object = MibTable
eqlMemberHWComponentTable = _EqlMemberHWComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 20)
)
if mibBuilder.loadTexts:
    eqlMemberHWComponentTable.setStatus("current")
_EqlMemberHWComponentEntry_Object = MibTableRow
eqlMemberHWComponentEntry = _EqlMemberHWComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 20, 1)
)
eqlMemberHWComponentEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlMemberHWComponentIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberHWComponentEntry.setStatus("current")


class _EqlMemberHWComponentIndex_Type(Integer32):
    """Custom type eqlMemberHWComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eip", 1)
    )


_EqlMemberHWComponentIndex_Type.__name__ = "Integer32"
_EqlMemberHWComponentIndex_Object = MibTableColumn
eqlMemberHWComponentIndex = _EqlMemberHWComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 20, 1, 1),
    _EqlMemberHWComponentIndex_Type()
)
eqlMemberHWComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlMemberHWComponentIndex.setStatus("current")


class _EqlMemberHWComponentName_Type(DisplayString):
    """Custom type eqlMemberHWComponentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlMemberHWComponentName_Type.__name__ = "DisplayString"
_EqlMemberHWComponentName_Object = MibTableColumn
eqlMemberHWComponentName = _EqlMemberHWComponentName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 20, 1, 2),
    _EqlMemberHWComponentName_Type()
)
eqlMemberHWComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHWComponentName.setStatus("current")


class _EqlMemberHWComponentSerialNumber_Type(DisplayString):
    """Custom type eqlMemberHWComponentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlMemberHWComponentSerialNumber_Type.__name__ = "DisplayString"
_EqlMemberHWComponentSerialNumber_Object = MibTableColumn
eqlMemberHWComponentSerialNumber = _EqlMemberHWComponentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 20, 1, 3),
    _EqlMemberHWComponentSerialNumber_Type()
)
eqlMemberHWComponentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHWComponentSerialNumber.setStatus("current")


class _EqlMemberHWComponentFirmwareRev_Type(DisplayString):
    """Custom type eqlMemberHWComponentFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlMemberHWComponentFirmwareRev_Type.__name__ = "DisplayString"
_EqlMemberHWComponentFirmwareRev_Object = MibTableColumn
eqlMemberHWComponentFirmwareRev = _EqlMemberHWComponentFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 20, 1, 4),
    _EqlMemberHWComponentFirmwareRev_Type()
)
eqlMemberHWComponentFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHWComponentFirmwareRev.setStatus("current")


class _EqlMemberHWComponentStatus_Type(Integer32):
    """Custom type eqlMemberHWComponentStatus based on Integer32"""
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
        *(("failed", 2),
          ("good", 3),
          ("not-present", 1),
          ("unknown", 0))
    )


_EqlMemberHWComponentStatus_Type.__name__ = "Integer32"
_EqlMemberHWComponentStatus_Object = MibTableColumn
eqlMemberHWComponentStatus = _EqlMemberHWComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 20, 1, 5),
    _EqlMemberHWComponentStatus_Type()
)
eqlMemberHWComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHWComponentStatus.setStatus("current")
_EqlMemberDynamicInfoTable_Object = MibTable
eqlMemberDynamicInfoTable = _EqlMemberDynamicInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 21)
)
if mibBuilder.loadTexts:
    eqlMemberDynamicInfoTable.setStatus("current")
_EqlMemberDynamicInfoEntry_Object = MibTableRow
eqlMemberDynamicInfoEntry = _EqlMemberDynamicInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 21, 1)
)
eqlMemberDynamicInfoEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberDynamicInfoEntry.setStatus("current")


class _EqlMemberDynamicInfoPendingUpdateVersion_Type(DisplayString):
    """Custom type eqlMemberDynamicInfoPendingUpdateVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlMemberDynamicInfoPendingUpdateVersion_Type.__name__ = "DisplayString"
_EqlMemberDynamicInfoPendingUpdateVersion_Object = MibTableColumn
eqlMemberDynamicInfoPendingUpdateVersion = _EqlMemberDynamicInfoPendingUpdateVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 21, 1, 1),
    _EqlMemberDynamicInfoPendingUpdateVersion_Type()
)
eqlMemberDynamicInfoPendingUpdateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberDynamicInfoPendingUpdateVersion.setStatus("current")


class _EqlMemberDynamicInfoIsRestartRunning_Type(Integer32):
    """Custom type eqlMemberDynamicInfoIsRestartRunning based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-running", 0),
          ("running", 1))
    )


_EqlMemberDynamicInfoIsRestartRunning_Type.__name__ = "Integer32"
_EqlMemberDynamicInfoIsRestartRunning_Object = MibTableColumn
eqlMemberDynamicInfoIsRestartRunning = _EqlMemberDynamicInfoIsRestartRunning_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 21, 1, 2),
    _EqlMemberDynamicInfoIsRestartRunning_Type()
)
eqlMemberDynamicInfoIsRestartRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberDynamicInfoIsRestartRunning.setStatus("current")


class _EqlMemberDynamicInfoIsUpdateRunning_Type(Integer32):
    """Custom type eqlMemberDynamicInfoIsUpdateRunning based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-running", 0),
          ("running", 1))
    )


_EqlMemberDynamicInfoIsUpdateRunning_Type.__name__ = "Integer32"
_EqlMemberDynamicInfoIsUpdateRunning_Object = MibTableColumn
eqlMemberDynamicInfoIsUpdateRunning = _EqlMemberDynamicInfoIsUpdateRunning_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 21, 1, 3),
    _EqlMemberDynamicInfoIsUpdateRunning_Type()
)
eqlMemberDynamicInfoIsUpdateRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberDynamicInfoIsUpdateRunning.setStatus("current")
_EqlMemberCacheStatisticsTable_Object = MibTable
eqlMemberCacheStatisticsTable = _EqlMemberCacheStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 22)
)
if mibBuilder.loadTexts:
    eqlMemberCacheStatisticsTable.setStatus("current")
_EqlMemberCacheStatisticsEntry_Object = MibTableRow
eqlMemberCacheStatisticsEntry = _EqlMemberCacheStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 22, 1)
)
eqlMemberCacheStatisticsEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberCacheStatisticsEntry.setStatus("current")
_EqlMemberTotalPageCount_Type = Counter64
_EqlMemberTotalPageCount_Object = MibTableColumn
eqlMemberTotalPageCount = _EqlMemberTotalPageCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 22, 1, 1),
    _EqlMemberTotalPageCount_Type()
)
eqlMemberTotalPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberTotalPageCount.setStatus("current")
_EqlMemberHotPageCount_Type = Counter64
_EqlMemberHotPageCount_Object = MibTableColumn
eqlMemberHotPageCount = _EqlMemberHotPageCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 22, 1, 2),
    _EqlMemberHotPageCount_Type()
)
eqlMemberHotPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberHotPageCount.setStatus("current")
_EqlMemberWarmPageCount_Type = Counter64
_EqlMemberWarmPageCount_Object = MibTableColumn
eqlMemberWarmPageCount = _EqlMemberWarmPageCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 22, 1, 3),
    _EqlMemberWarmPageCount_Type()
)
eqlMemberWarmPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberWarmPageCount.setStatus("current")
_EqlMemberColdPageCount_Type = Counter64
_EqlMemberColdPageCount_Object = MibTableColumn
eqlMemberColdPageCount = _EqlMemberColdPageCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 22, 1, 4),
    _EqlMemberColdPageCount_Type()
)
eqlMemberColdPageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberColdPageCount.setStatus("current")
_EqlMemberPageSize_Type = Unsigned32
_EqlMemberPageSize_Object = MibTableColumn
eqlMemberPageSize = _EqlMemberPageSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 22, 1, 5),
    _EqlMemberPageSize_Type()
)
eqlMemberPageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPageSize.setStatus("current")
if mibBuilder.loadTexts:
    eqlMemberPageSize.setUnits("KB")
_EqlMemberSSDAcceleratorSize_Type = Unsigned32
_EqlMemberSSDAcceleratorSize_Object = MibTableColumn
eqlMemberSSDAcceleratorSize = _EqlMemberSSDAcceleratorSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 22, 1, 6),
    _EqlMemberSSDAcceleratorSize_Type()
)
eqlMemberSSDAcceleratorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberSSDAcceleratorSize.setStatus("current")
if mibBuilder.loadTexts:
    eqlMemberSSDAcceleratorSize.setUnits("GB")
_EqlMemberSSDCacheSize_Type = Unsigned32
_EqlMemberSSDCacheSize_Object = MibTableColumn
eqlMemberSSDCacheSize = _EqlMemberSSDCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 22, 1, 7),
    _EqlMemberSSDCacheSize_Type()
)
eqlMemberSSDCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberSSDCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    eqlMemberSSDCacheSize.setUnits("GB")
_EqlMemberSSDAcceleratorEntriesTotal_Type = Unsigned32
_EqlMemberSSDAcceleratorEntriesTotal_Object = MibTableColumn
eqlMemberSSDAcceleratorEntriesTotal = _EqlMemberSSDAcceleratorEntriesTotal_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 22, 1, 8),
    _EqlMemberSSDAcceleratorEntriesTotal_Type()
)
eqlMemberSSDAcceleratorEntriesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberSSDAcceleratorEntriesTotal.setStatus("current")
_EqlMemberSSDAcceleratorEntriesUsed_Type = Unsigned32
_EqlMemberSSDAcceleratorEntriesUsed_Object = MibTableColumn
eqlMemberSSDAcceleratorEntriesUsed = _EqlMemberSSDAcceleratorEntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 22, 1, 9),
    _EqlMemberSSDAcceleratorEntriesUsed_Type()
)
eqlMemberSSDAcceleratorEntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberSSDAcceleratorEntriesUsed.setStatus("current")
_EqlMemberSEDEncryptionTable_Object = MibTable
eqlMemberSEDEncryptionTable = _EqlMemberSEDEncryptionTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 23)
)
if mibBuilder.loadTexts:
    eqlMemberSEDEncryptionTable.setStatus("current")
_EqlMemberSEDEncryptionEntry_Object = MibTableRow
eqlMemberSEDEncryptionEntry = _EqlMemberSEDEncryptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 23, 1)
)
eqlMemberSEDEncryptionEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberSEDEncryptionEntry.setStatus("current")
_EqlMemberSEDEncryptionRowStatus_Type = RowStatus
_EqlMemberSEDEncryptionRowStatus_Object = MibTableColumn
eqlMemberSEDEncryptionRowStatus = _EqlMemberSEDEncryptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 23, 1, 1),
    _EqlMemberSEDEncryptionRowStatus_Type()
)
eqlMemberSEDEncryptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberSEDEncryptionRowStatus.setStatus("current")
_EqlMemberSEDEncryptionShare1_Type = EqlMemberSEDShareType
_EqlMemberSEDEncryptionShare1_Object = MibTableColumn
eqlMemberSEDEncryptionShare1 = _EqlMemberSEDEncryptionShare1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 23, 1, 2),
    _EqlMemberSEDEncryptionShare1_Type()
)
eqlMemberSEDEncryptionShare1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberSEDEncryptionShare1.setStatus("current")
_EqlMemberSEDEncryptionShare2_Type = EqlMemberSEDShareType
_EqlMemberSEDEncryptionShare2_Object = MibTableColumn
eqlMemberSEDEncryptionShare2 = _EqlMemberSEDEncryptionShare2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 23, 1, 3),
    _EqlMemberSEDEncryptionShare2_Type()
)
eqlMemberSEDEncryptionShare2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberSEDEncryptionShare2.setStatus("current")
_EqlMemberSEDEncryptionShare3_Type = EqlMemberSEDShareType
_EqlMemberSEDEncryptionShare3_Object = MibTableColumn
eqlMemberSEDEncryptionShare3 = _EqlMemberSEDEncryptionShare3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 23, 1, 4),
    _EqlMemberSEDEncryptionShare3_Type()
)
eqlMemberSEDEncryptionShare3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberSEDEncryptionShare3.setStatus("current")
_EqlMemberDynamicOpsTable_Object = MibTable
eqlMemberDynamicOpsTable = _EqlMemberDynamicOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 24)
)
if mibBuilder.loadTexts:
    eqlMemberDynamicOpsTable.setStatus("current")
_EqlMemberDynamicOpsEntry_Object = MibTableRow
eqlMemberDynamicOpsEntry = _EqlMemberDynamicOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 24, 1)
)
eqlMemberDynamicOpsEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlMemberDynamicOpsOperation"),
)
if mibBuilder.loadTexts:
    eqlMemberDynamicOpsEntry.setStatus("current")


class _EqlMemberDynamicOpsOperation_Type(Integer32):
    """Custom type eqlMemberDynamicOpsOperation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("delete-pending", 7),
          ("none", 0))
    )


_EqlMemberDynamicOpsOperation_Type.__name__ = "Integer32"
_EqlMemberDynamicOpsOperation_Object = MibTableColumn
eqlMemberDynamicOpsOperation = _EqlMemberDynamicOpsOperation_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 24, 1, 1),
    _EqlMemberDynamicOpsOperation_Type()
)
eqlMemberDynamicOpsOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberDynamicOpsOperation.setStatus("current")


class _EqlMemberDynamicOpsOperationArg_Type(OctetString):
    """Custom type eqlMemberDynamicOpsOperationArg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlMemberDynamicOpsOperationArg_Type.__name__ = "OctetString"
_EqlMemberDynamicOpsOperationArg_Object = MibTableColumn
eqlMemberDynamicOpsOperationArg = _EqlMemberDynamicOpsOperationArg_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 24, 1, 2),
    _EqlMemberDynamicOpsOperationArg_Type()
)
eqlMemberDynamicOpsOperationArg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberDynamicOpsOperationArg.setStatus("current")
_EqlMemberGroupInfoAtMemberTable_Object = MibTable
eqlMemberGroupInfoAtMemberTable = _EqlMemberGroupInfoAtMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 25)
)
if mibBuilder.loadTexts:
    eqlMemberGroupInfoAtMemberTable.setStatus("current")
_EqlMemberGroupInfoAtMemberEntry_Object = MibTableRow
eqlMemberGroupInfoAtMemberEntry = _EqlMemberGroupInfoAtMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 25, 1)
)
eqlMemberGroupInfoAtMemberEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberGroupInfoAtMemberEntry.setStatus("current")


class _EqlMemberGroupInfoAtMemberPasswd1_Type(OctetString):
    """Custom type eqlMemberGroupInfoAtMemberPasswd1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqlMemberGroupInfoAtMemberPasswd1_Type.__name__ = "OctetString"
_EqlMemberGroupInfoAtMemberPasswd1_Object = MibTableColumn
eqlMemberGroupInfoAtMemberPasswd1 = _EqlMemberGroupInfoAtMemberPasswd1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 25, 1, 1),
    _EqlMemberGroupInfoAtMemberPasswd1_Type()
)
eqlMemberGroupInfoAtMemberPasswd1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberGroupInfoAtMemberPasswd1.setStatus("current")
_EqlMemberGroupInfoAtMemberPasswd1Len_Type = Unsigned32
_EqlMemberGroupInfoAtMemberPasswd1Len_Object = MibTableColumn
eqlMemberGroupInfoAtMemberPasswd1Len = _EqlMemberGroupInfoAtMemberPasswd1Len_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 25, 1, 2),
    _EqlMemberGroupInfoAtMemberPasswd1Len_Type()
)
eqlMemberGroupInfoAtMemberPasswd1Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberGroupInfoAtMemberPasswd1Len.setStatus("current")
_EqlDriveGroupStatisticsTable_Object = MibTable
eqlDriveGroupStatisticsTable = _EqlDriveGroupStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 26)
)
if mibBuilder.loadTexts:
    eqlDriveGroupStatisticsTable.setStatus("current")
_EqlDriveGroupStatisticsEntry_Object = MibTableRow
eqlDriveGroupStatisticsEntry = _EqlDriveGroupStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 26, 1)
)
eqlDriveGroupStatisticsEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlDriveGroupStatisticsIndex"),
)
if mibBuilder.loadTexts:
    eqlDriveGroupStatisticsEntry.setStatus("current")
_EqlDriveGroupStatisticsIndex_Type = Integer32
_EqlDriveGroupStatisticsIndex_Object = MibTableColumn
eqlDriveGroupStatisticsIndex = _EqlDriveGroupStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 26, 1, 1),
    _EqlDriveGroupStatisticsIndex_Type()
)
eqlDriveGroupStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlDriveGroupStatisticsIndex.setStatus("current")
_EqlDriveGroupStatisticsHeadroom_Type = Unsigned32
_EqlDriveGroupStatisticsHeadroom_Object = MibTableColumn
eqlDriveGroupStatisticsHeadroom = _EqlDriveGroupStatisticsHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 26, 1, 2),
    _EqlDriveGroupStatisticsHeadroom_Type()
)
eqlDriveGroupStatisticsHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDriveGroupStatisticsHeadroom.setStatus("current")
_EqlMemberFirmwareInfoTable_Object = MibTable
eqlMemberFirmwareInfoTable = _EqlMemberFirmwareInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 27)
)
if mibBuilder.loadTexts:
    eqlMemberFirmwareInfoTable.setStatus("current")
_EqlMemberFirmwareInfoEntry_Object = MibTableRow
eqlMemberFirmwareInfoEntry = _EqlMemberFirmwareInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 27, 1)
)
eqlMemberFirmwareInfoEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberFirmwareInfoEntry.setStatus("current")


class _EqlMemberLanguageVersion_Type(DisplayString):
    """Custom type eqlMemberLanguageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlMemberLanguageVersion_Type.__name__ = "DisplayString"
_EqlMemberLanguageVersion_Object = MibTableColumn
eqlMemberLanguageVersion = _EqlMemberLanguageVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 27, 1, 1),
    _EqlMemberLanguageVersion_Type()
)
eqlMemberLanguageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberLanguageVersion.setStatus("current")


class _EqlMemberFirmwareInfoDataReduction_Type(Integer32):
    """Custom type eqlMemberFirmwareInfoDataReduction based on Integer32"""
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
        *(("compression-paused", 5),
          ("compression-running", 4),
          ("disabled", 1),
          ("no-capable-hardware", 2),
          ("no-capable-raid", 3),
          ("unknown", 0))
    )


_EqlMemberFirmwareInfoDataReduction_Type.__name__ = "Integer32"
_EqlMemberFirmwareInfoDataReduction_Object = MibTableColumn
eqlMemberFirmwareInfoDataReduction = _EqlMemberFirmwareInfoDataReduction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 27, 1, 2),
    _EqlMemberFirmwareInfoDataReduction_Type()
)
eqlMemberFirmwareInfoDataReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlMemberFirmwareInfoDataReduction.setStatus("current")
_EqlDriveGroupHeatProfileInfoTable_Object = MibTable
eqlDriveGroupHeatProfileInfoTable = _EqlDriveGroupHeatProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 28)
)
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfileInfoTable.setStatus("current")
_EqlDriveGroupHeatProfileInfoEntry_Object = MibTableRow
eqlDriveGroupHeatProfileInfoEntry = _EqlDriveGroupHeatProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 28, 1)
)
eqlDriveGroupHeatProfileInfoEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlDriveGroupStatisticsIndex"),
    (0, "EQLMEMBER-MIB", "eqlDriveGroupHeatProfilePart"),
)
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfileInfoEntry.setStatus("current")
_EqlDriveGroupHeatProfilePart_Type = Unsigned32
_EqlDriveGroupHeatProfilePart_Object = MibTableColumn
eqlDriveGroupHeatProfilePart = _EqlDriveGroupHeatProfilePart_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 28, 1, 1),
    _EqlDriveGroupHeatProfilePart_Type()
)
eqlDriveGroupHeatProfilePart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfilePart.setStatus("current")
_EqlDriveGroupHeatProfileColdCount_Type = Counter64
_EqlDriveGroupHeatProfileColdCount_Object = MibTableColumn
eqlDriveGroupHeatProfileColdCount = _EqlDriveGroupHeatProfileColdCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 28, 1, 2),
    _EqlDriveGroupHeatProfileColdCount_Type()
)
eqlDriveGroupHeatProfileColdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfileColdCount.setStatus("current")
_EqlDriveGroupHeatProfileMinMagnitude_Type = Integer32
_EqlDriveGroupHeatProfileMinMagnitude_Object = MibTableColumn
eqlDriveGroupHeatProfileMinMagnitude = _EqlDriveGroupHeatProfileMinMagnitude_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 28, 1, 3),
    _EqlDriveGroupHeatProfileMinMagnitude_Type()
)
eqlDriveGroupHeatProfileMinMagnitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfileMinMagnitude.setStatus("current")
_EqlDriveGroupHeatProfileMinMultiplier_Type = Unsigned32
_EqlDriveGroupHeatProfileMinMultiplier_Object = MibTableColumn
eqlDriveGroupHeatProfileMinMultiplier = _EqlDriveGroupHeatProfileMinMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 28, 1, 4),
    _EqlDriveGroupHeatProfileMinMultiplier_Type()
)
eqlDriveGroupHeatProfileMinMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfileMinMultiplier.setStatus("current")
_EqlDriveGroupHeatProfileMaxMagnitude_Type = Integer32
_EqlDriveGroupHeatProfileMaxMagnitude_Object = MibTableColumn
eqlDriveGroupHeatProfileMaxMagnitude = _EqlDriveGroupHeatProfileMaxMagnitude_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 28, 1, 5),
    _EqlDriveGroupHeatProfileMaxMagnitude_Type()
)
eqlDriveGroupHeatProfileMaxMagnitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfileMaxMagnitude.setStatus("current")
_EqlDriveGroupHeatProfileMaxMultiplier_Type = Unsigned32
_EqlDriveGroupHeatProfileMaxMultiplier_Object = MibTableColumn
eqlDriveGroupHeatProfileMaxMultiplier = _EqlDriveGroupHeatProfileMaxMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 28, 1, 6),
    _EqlDriveGroupHeatProfileMaxMultiplier_Type()
)
eqlDriveGroupHeatProfileMaxMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfileMaxMultiplier.setStatus("current")
_EqlDriveGroupHeatProfileBinTable_Object = MibTable
eqlDriveGroupHeatProfileBinTable = _EqlDriveGroupHeatProfileBinTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 29)
)
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfileBinTable.setStatus("current")
_EqlDriveGroupHeatProfileBinEntry_Object = MibTableRow
eqlDriveGroupHeatProfileBinEntry = _EqlDriveGroupHeatProfileBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 29, 1)
)
eqlDriveGroupHeatProfileBinEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlDriveGroupStatisticsIndex"),
    (0, "EQLMEMBER-MIB", "eqlDriveGroupHeatProfilePart"),
    (0, "EQLMEMBER-MIB", "eqlDriveGroupHeatProfileBinId"),
)
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfileBinEntry.setStatus("current")
_EqlDriveGroupHeatProfileBinId_Type = Unsigned32
_EqlDriveGroupHeatProfileBinId_Object = MibTableColumn
eqlDriveGroupHeatProfileBinId = _EqlDriveGroupHeatProfileBinId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 29, 1, 1),
    _EqlDriveGroupHeatProfileBinId_Type()
)
eqlDriveGroupHeatProfileBinId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfileBinId.setStatus("current")
_EqlDriveGroupHeatProfileAccessRateMagnitude_Type = Integer32
_EqlDriveGroupHeatProfileAccessRateMagnitude_Object = MibTableColumn
eqlDriveGroupHeatProfileAccessRateMagnitude = _EqlDriveGroupHeatProfileAccessRateMagnitude_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 29, 1, 2),
    _EqlDriveGroupHeatProfileAccessRateMagnitude_Type()
)
eqlDriveGroupHeatProfileAccessRateMagnitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfileAccessRateMagnitude.setStatus("current")
_EqlDriveGroupHeatProfileAccessRateMultiplier_Type = Unsigned32
_EqlDriveGroupHeatProfileAccessRateMultiplier_Object = MibTableColumn
eqlDriveGroupHeatProfileAccessRateMultiplier = _EqlDriveGroupHeatProfileAccessRateMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 29, 1, 3),
    _EqlDriveGroupHeatProfileAccessRateMultiplier_Type()
)
eqlDriveGroupHeatProfileAccessRateMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfileAccessRateMultiplier.setStatus("current")
_EqlDriveGroupHeatProfileCount_Type = Counter64
_EqlDriveGroupHeatProfileCount_Object = MibTableColumn
eqlDriveGroupHeatProfileCount = _EqlDriveGroupHeatProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 29, 1, 4),
    _EqlDriveGroupHeatProfileCount_Type()
)
eqlDriveGroupHeatProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDriveGroupHeatProfileCount.setStatus("current")
_EqlTaggedHeatProfileInfoTable_Object = MibTable
eqlTaggedHeatProfileInfoTable = _EqlTaggedHeatProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 30)
)
if mibBuilder.loadTexts:
    eqlTaggedHeatProfileInfoTable.setStatus("current")
_EqlTaggedHeatProfileInfoEntry_Object = MibTableRow
eqlTaggedHeatProfileInfoEntry = _EqlTaggedHeatProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 30, 1)
)
eqlTaggedHeatProfileInfoEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlTaggedHeatTag"),
)
if mibBuilder.loadTexts:
    eqlTaggedHeatProfileInfoEntry.setStatus("current")
_EqlTaggedHeatTag_Type = Unsigned32
_EqlTaggedHeatTag_Object = MibTableColumn
eqlTaggedHeatTag = _EqlTaggedHeatTag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 30, 1, 1),
    _EqlTaggedHeatTag_Type()
)
eqlTaggedHeatTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlTaggedHeatTag.setStatus("current")
_EqlTaggedHeatProfileColdCount_Type = Counter64
_EqlTaggedHeatProfileColdCount_Object = MibTableColumn
eqlTaggedHeatProfileColdCount = _EqlTaggedHeatProfileColdCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 30, 1, 2),
    _EqlTaggedHeatProfileColdCount_Type()
)
eqlTaggedHeatProfileColdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlTaggedHeatProfileColdCount.setStatus("current")
_EqlTaggedHeatProfileMinMagnitude_Type = Integer32
_EqlTaggedHeatProfileMinMagnitude_Object = MibTableColumn
eqlTaggedHeatProfileMinMagnitude = _EqlTaggedHeatProfileMinMagnitude_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 30, 1, 3),
    _EqlTaggedHeatProfileMinMagnitude_Type()
)
eqlTaggedHeatProfileMinMagnitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlTaggedHeatProfileMinMagnitude.setStatus("current")
_EqlTaggedHeatProfileMinMultiplier_Type = Unsigned32
_EqlTaggedHeatProfileMinMultiplier_Object = MibTableColumn
eqlTaggedHeatProfileMinMultiplier = _EqlTaggedHeatProfileMinMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 30, 1, 4),
    _EqlTaggedHeatProfileMinMultiplier_Type()
)
eqlTaggedHeatProfileMinMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlTaggedHeatProfileMinMultiplier.setStatus("current")
_EqlTaggedHeatProfileMaxMagnitude_Type = Integer32
_EqlTaggedHeatProfileMaxMagnitude_Object = MibTableColumn
eqlTaggedHeatProfileMaxMagnitude = _EqlTaggedHeatProfileMaxMagnitude_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 30, 1, 5),
    _EqlTaggedHeatProfileMaxMagnitude_Type()
)
eqlTaggedHeatProfileMaxMagnitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlTaggedHeatProfileMaxMagnitude.setStatus("current")
_EqlTaggedHeatProfileMaxMultiplier_Type = Unsigned32
_EqlTaggedHeatProfileMaxMultiplier_Object = MibTableColumn
eqlTaggedHeatProfileMaxMultiplier = _EqlTaggedHeatProfileMaxMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 30, 1, 6),
    _EqlTaggedHeatProfileMaxMultiplier_Type()
)
eqlTaggedHeatProfileMaxMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlTaggedHeatProfileMaxMultiplier.setStatus("current")
_EqlTaggedHeatProfileBinTable_Object = MibTable
eqlTaggedHeatProfileBinTable = _EqlTaggedHeatProfileBinTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 31)
)
if mibBuilder.loadTexts:
    eqlTaggedHeatProfileBinTable.setStatus("current")
_EqlTaggedHeatProfileBinEntry_Object = MibTableRow
eqlTaggedHeatProfileBinEntry = _EqlTaggedHeatProfileBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 31, 1)
)
eqlTaggedHeatProfileBinEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlTaggedHeatTag"),
    (0, "EQLMEMBER-MIB", "eqlTaggedHeatProfileBinId"),
)
if mibBuilder.loadTexts:
    eqlTaggedHeatProfileBinEntry.setStatus("current")
_EqlTaggedHeatProfileBinId_Type = Unsigned32
_EqlTaggedHeatProfileBinId_Object = MibTableColumn
eqlTaggedHeatProfileBinId = _EqlTaggedHeatProfileBinId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 31, 1, 1),
    _EqlTaggedHeatProfileBinId_Type()
)
eqlTaggedHeatProfileBinId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlTaggedHeatProfileBinId.setStatus("current")
_EqlTaggedHeatProfileAccessRateMagnitude_Type = Integer32
_EqlTaggedHeatProfileAccessRateMagnitude_Object = MibTableColumn
eqlTaggedHeatProfileAccessRateMagnitude = _EqlTaggedHeatProfileAccessRateMagnitude_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 31, 1, 2),
    _EqlTaggedHeatProfileAccessRateMagnitude_Type()
)
eqlTaggedHeatProfileAccessRateMagnitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlTaggedHeatProfileAccessRateMagnitude.setStatus("current")
_EqlTaggedHeatProfileAccessRateMultiplier_Type = Unsigned32
_EqlTaggedHeatProfileAccessRateMultiplier_Object = MibTableColumn
eqlTaggedHeatProfileAccessRateMultiplier = _EqlTaggedHeatProfileAccessRateMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 31, 1, 3),
    _EqlTaggedHeatProfileAccessRateMultiplier_Type()
)
eqlTaggedHeatProfileAccessRateMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlTaggedHeatProfileAccessRateMultiplier.setStatus("current")
_EqlTaggedHeatProfileCount_Type = Counter64
_EqlTaggedHeatProfileCount_Object = MibTableColumn
eqlTaggedHeatProfileCount = _EqlTaggedHeatProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 31, 1, 4),
    _EqlTaggedHeatProfileCount_Type()
)
eqlTaggedHeatProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlTaggedHeatProfileCount.setStatus("current")
_EqlMemberRaidPoliciesTable_Object = MibTable
eqlMemberRaidPoliciesTable = _EqlMemberRaidPoliciesTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 32)
)
if mibBuilder.loadTexts:
    eqlMemberRaidPoliciesTable.setStatus("current")
_EqlMemberRaidPoliciesEntry_Object = MibTableRow
eqlMemberRaidPoliciesEntry = _EqlMemberRaidPoliciesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 32, 1)
)
eqlMemberRaidPoliciesEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlDriveGroupRAIDPolicy"),
)
if mibBuilder.loadTexts:
    eqlMemberRaidPoliciesEntry.setStatus("current")


class _EqlMemberRaidPoliciesBehavior_Type(Integer32):
    """Custom type eqlMemberRaidPoliciesBehavior based on Integer32"""
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
        *(("always", 1),
          ("cli", 3),
          ("cliSanHQ", 4),
          ("never", 2))
    )


_EqlMemberRaidPoliciesBehavior_Type.__name__ = "Integer32"
_EqlMemberRaidPoliciesBehavior_Object = MibTableColumn
eqlMemberRaidPoliciesBehavior = _EqlMemberRaidPoliciesBehavior_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 32, 1, 1),
    _EqlMemberRaidPoliciesBehavior_Type()
)
eqlMemberRaidPoliciesBehavior.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberRaidPoliciesBehavior.setStatus("current")
_EqlMemberRaidPoliciesRAIDCapacity_Type = Counter64
_EqlMemberRaidPoliciesRAIDCapacity_Object = MibTableColumn
eqlMemberRaidPoliciesRAIDCapacity = _EqlMemberRaidPoliciesRAIDCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 32, 1, 2),
    _EqlMemberRaidPoliciesRAIDCapacity_Type()
)
eqlMemberRaidPoliciesRAIDCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberRaidPoliciesRAIDCapacity.setStatus("current")
_EqlMemberPerTCPConnectionStatsTable_Object = MibTable
eqlMemberPerTCPConnectionStatsTable = _EqlMemberPerTCPConnectionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33)
)
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsTable.setStatus("current")
_EqlMemberPerTCPConnectionStatsEntry_Object = MibTableRow
eqlMemberPerTCPConnectionStatsEntry = _EqlMemberPerTCPConnectionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1)
)
eqlMemberPerTCPConnectionStatsEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlMemberPerTCPConnectionStatsIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsEntry.setStatus("current")
_EqlMemberPerTCPConnectionStatsIndex_Type = Unsigned32
_EqlMemberPerTCPConnectionStatsIndex_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsIndex = _EqlMemberPerTCPConnectionStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 1),
    _EqlMemberPerTCPConnectionStatsIndex_Type()
)
eqlMemberPerTCPConnectionStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsIndex.setStatus("current")
_EqlMemberPerTCPConnectionStatsLocalAddrType_Type = InetAddressType
_EqlMemberPerTCPConnectionStatsLocalAddrType_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsLocalAddrType = _EqlMemberPerTCPConnectionStatsLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 2),
    _EqlMemberPerTCPConnectionStatsLocalAddrType_Type()
)
eqlMemberPerTCPConnectionStatsLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsLocalAddrType.setStatus("current")
_EqlMemberPerTCPConnectionStatsLocalAddr_Type = InetAddress
_EqlMemberPerTCPConnectionStatsLocalAddr_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsLocalAddr = _EqlMemberPerTCPConnectionStatsLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 3),
    _EqlMemberPerTCPConnectionStatsLocalAddr_Type()
)
eqlMemberPerTCPConnectionStatsLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsLocalAddr.setStatus("current")
_EqlMemberPerTCPConnectionStatsLocalPort_Type = Unsigned32
_EqlMemberPerTCPConnectionStatsLocalPort_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsLocalPort = _EqlMemberPerTCPConnectionStatsLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 4),
    _EqlMemberPerTCPConnectionStatsLocalPort_Type()
)
eqlMemberPerTCPConnectionStatsLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsLocalPort.setStatus("current")
_EqlMemberPerTCPConnectionStatsForeignAddrType_Type = InetAddressType
_EqlMemberPerTCPConnectionStatsForeignAddrType_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsForeignAddrType = _EqlMemberPerTCPConnectionStatsForeignAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 5),
    _EqlMemberPerTCPConnectionStatsForeignAddrType_Type()
)
eqlMemberPerTCPConnectionStatsForeignAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsForeignAddrType.setStatus("current")
_EqlMemberPerTCPConnectionStatsForeignAddr_Type = InetAddress
_EqlMemberPerTCPConnectionStatsForeignAddr_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsForeignAddr = _EqlMemberPerTCPConnectionStatsForeignAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 6),
    _EqlMemberPerTCPConnectionStatsForeignAddr_Type()
)
eqlMemberPerTCPConnectionStatsForeignAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsForeignAddr.setStatus("current")
_EqlMemberPerTCPConnectionStatsForeignPort_Type = Unsigned32
_EqlMemberPerTCPConnectionStatsForeignPort_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsForeignPort = _EqlMemberPerTCPConnectionStatsForeignPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 7),
    _EqlMemberPerTCPConnectionStatsForeignPort_Type()
)
eqlMemberPerTCPConnectionStatsForeignPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsForeignPort.setStatus("current")
_EqlMemberPerTCPConnectionStatsMss_Type = Unsigned32
_EqlMemberPerTCPConnectionStatsMss_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsMss = _EqlMemberPerTCPConnectionStatsMss_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 8),
    _EqlMemberPerTCPConnectionStatsMss_Type()
)
eqlMemberPerTCPConnectionStatsMss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsMss.setStatus("current")


class _EqlMemberPerTCPConnectionStatsState_Type(Integer32):
    """Custom type eqlMemberPerTCPConnectionStatsState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("tcps-close-wait", 5),
          ("tcps-closed", 0),
          ("tcps-closing", 7),
          ("tcps-established", 4),
          ("tcps-fin-wait1", 6),
          ("tcps-fin-wait2", 9),
          ("tcps-last-ack", 8),
          ("tcps-listen", 1),
          ("tcps-syn-received", 3),
          ("tcps-syn-sent", 2),
          ("tcps-time-wait", 10))
    )


_EqlMemberPerTCPConnectionStatsState_Type.__name__ = "Integer32"
_EqlMemberPerTCPConnectionStatsState_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsState = _EqlMemberPerTCPConnectionStatsState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 9),
    _EqlMemberPerTCPConnectionStatsState_Type()
)
eqlMemberPerTCPConnectionStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsState.setStatus("current")
_EqlMemberPerTCPConnectionStatsSndpack_Type = Counter64
_EqlMemberPerTCPConnectionStatsSndpack_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsSndpack = _EqlMemberPerTCPConnectionStatsSndpack_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 10),
    _EqlMemberPerTCPConnectionStatsSndpack_Type()
)
eqlMemberPerTCPConnectionStatsSndpack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsSndpack.setStatus("current")
_EqlMemberPerTCPConnectionStatsSndbyte_Type = Counter64
_EqlMemberPerTCPConnectionStatsSndbyte_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsSndbyte = _EqlMemberPerTCPConnectionStatsSndbyte_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 11),
    _EqlMemberPerTCPConnectionStatsSndbyte_Type()
)
eqlMemberPerTCPConnectionStatsSndbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsSndbyte.setStatus("current")
_EqlMemberPerTCPConnectionStatsSndrexmitpack_Type = Counter64
_EqlMemberPerTCPConnectionStatsSndrexmitpack_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsSndrexmitpack = _EqlMemberPerTCPConnectionStatsSndrexmitpack_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 12),
    _EqlMemberPerTCPConnectionStatsSndrexmitpack_Type()
)
eqlMemberPerTCPConnectionStatsSndrexmitpack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsSndrexmitpack.setStatus("current")
_EqlMemberPerTCPConnectionStatsSndrexmitbyte_Type = Counter64
_EqlMemberPerTCPConnectionStatsSndrexmitbyte_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsSndrexmitbyte = _EqlMemberPerTCPConnectionStatsSndrexmitbyte_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 13),
    _EqlMemberPerTCPConnectionStatsSndrexmitbyte_Type()
)
eqlMemberPerTCPConnectionStatsSndrexmitbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsSndrexmitbyte.setStatus("current")
_EqlMemberPerTCPConnectionStatsRexmttimeout_Type = Counter64
_EqlMemberPerTCPConnectionStatsRexmttimeout_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsRexmttimeout = _EqlMemberPerTCPConnectionStatsRexmttimeout_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 14),
    _EqlMemberPerTCPConnectionStatsRexmttimeout_Type()
)
eqlMemberPerTCPConnectionStatsRexmttimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsRexmttimeout.setStatus("current")
_EqlMemberPerTCPConnectionStatsFastrexmt_Type = Counter64
_EqlMemberPerTCPConnectionStatsFastrexmt_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsFastrexmt = _EqlMemberPerTCPConnectionStatsFastrexmt_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 15),
    _EqlMemberPerTCPConnectionStatsFastrexmt_Type()
)
eqlMemberPerTCPConnectionStatsFastrexmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsFastrexmt.setStatus("current")
_EqlMemberPerTCPConnectionStatsSndprobe_Type = Counter64
_EqlMemberPerTCPConnectionStatsSndprobe_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsSndprobe = _EqlMemberPerTCPConnectionStatsSndprobe_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 16),
    _EqlMemberPerTCPConnectionStatsSndprobe_Type()
)
eqlMemberPerTCPConnectionStatsSndprobe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsSndprobe.setStatus("current")
_EqlMemberPerTCPConnectionStatsRcvpack_Type = Counter64
_EqlMemberPerTCPConnectionStatsRcvpack_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsRcvpack = _EqlMemberPerTCPConnectionStatsRcvpack_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 17),
    _EqlMemberPerTCPConnectionStatsRcvpack_Type()
)
eqlMemberPerTCPConnectionStatsRcvpack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsRcvpack.setStatus("current")
_EqlMemberPerTCPConnectionStatsRcvbyte_Type = Counter64
_EqlMemberPerTCPConnectionStatsRcvbyte_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsRcvbyte = _EqlMemberPerTCPConnectionStatsRcvbyte_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 18),
    _EqlMemberPerTCPConnectionStatsRcvbyte_Type()
)
eqlMemberPerTCPConnectionStatsRcvbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsRcvbyte.setStatus("current")
_EqlMemberPerTCPConnectionStatsRcvwinprobe_Type = Counter64
_EqlMemberPerTCPConnectionStatsRcvwinprobe_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsRcvwinprobe = _EqlMemberPerTCPConnectionStatsRcvwinprobe_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 19),
    _EqlMemberPerTCPConnectionStatsRcvwinprobe_Type()
)
eqlMemberPerTCPConnectionStatsRcvwinprobe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsRcvwinprobe.setStatus("current")
_EqlMemberPerTCPConnectionStatsRcvbadsum_Type = Counter64
_EqlMemberPerTCPConnectionStatsRcvbadsum_Object = MibTableColumn
eqlMemberPerTCPConnectionStatsRcvbadsum = _EqlMemberPerTCPConnectionStatsRcvbadsum_Object(
    (1, 3, 6, 1, 4, 1, 12740, 2, 1, 33, 1, 20),
    _EqlMemberPerTCPConnectionStatsRcvbadsum_Type()
)
eqlMemberPerTCPConnectionStatsRcvbadsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberPerTCPConnectionStatsRcvbadsum.setStatus("current")
_EqlmemberNotifications_ObjectIdentity = ObjectIdentity
eqlmemberNotifications = _EqlmemberNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2)
)
_EqlMemberEnclosureMgmtNotifications_ObjectIdentity = ObjectIdentity
eqlMemberEnclosureMgmtNotifications = _EqlMemberEnclosureMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1)
)
_EqlmemberConformance_ObjectIdentity = ObjectIdentity
eqlmemberConformance = _EqlmemberConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 2, 3)
)
eqlMemberStatusEntry.registerAugmentions(
    ("EQLMEMBER-MIB",
     "eqlMemberIdentificationEntry")
)
eqlMemberIdentificationEntry.setIndexNames(*eqlMemberStatusEntry.getIndexNames())
eqlMemberIdentificationEntry.registerAugmentions(
    ("EQLMEMBER-MIB",
     "eqlMemberStorageEntry")
)
eqlMemberStorageEntry.setIndexNames(*eqlMemberIdentificationEntry.getIndexNames())
eqlMemberIdentificationEntry.registerAugmentions(
    ("EQLMEMBER-MIB",
     "eqlMemberChassisEntry")
)
eqlMemberChassisEntry.setIndexNames(*eqlMemberIdentificationEntry.getIndexNames())
eqlMemberIdentificationEntry.registerAugmentions(
    ("EQLMEMBER-MIB",
     "eqlMemberConnEntry")
)
eqlMemberConnEntry.setIndexNames(*eqlMemberIdentificationEntry.getIndexNames())
eqlMemberIdentificationEntry.registerAugmentions(
    ("EQLMEMBER-MIB",
     "eqlMemberRAIDEntry")
)
eqlMemberRAIDEntry.setIndexNames(*eqlMemberIdentificationEntry.getIndexNames())
eqlMemberIdentificationEntry.registerAugmentions(
    ("EQLMEMBER-MIB",
     "eqlMemberPSGMapEntry")
)
eqlMemberPSGMapEntry.setIndexNames(*eqlMemberIdentificationEntry.getIndexNames())
eqlDriveGroupOpsEntry.registerAugmentions(
    ("EQLMEMBER-MIB",
     "eqlDriveGroupOpsStatusEntry")
)
eqlDriveGroupOpsStatusEntry.setIndexNames(*eqlDriveGroupOpsEntry.getIndexNames())

# Managed Objects groups


# Notification objects

eqlMemberHealthTempSensorHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 1)
)
eqlMemberHealthTempSensorHighThreshold.setObjects(
      *(("EQLMEMBER-MIB", "eqlMemberHealthDetailsTemperatureName"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsTemperatureValue"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsTemperatureCurrentState"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsTemperatureHighCriticalThreshold"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsTemperatureHighWarningThreshold"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsTemperatureNameID"))
)
if mibBuilder.loadTexts:
    eqlMemberHealthTempSensorHighThreshold.setStatus(
        "current"
    )

eqlMemberHealthTempSensorLowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 2)
)
eqlMemberHealthTempSensorLowThreshold.setObjects(
      *(("EQLMEMBER-MIB", "eqlMemberHealthDetailsTemperatureName"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsTemperatureValue"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsTemperatureCurrentState"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsTemperatureLowCriticalThreshold"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsTemperatureLowWarningThreshold"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsTemperatureNameID"))
)
if mibBuilder.loadTexts:
    eqlMemberHealthTempSensorLowThreshold.setStatus(
        "current"
    )

eqlMemberHealthFanSpeedHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 3)
)
eqlMemberHealthFanSpeedHighThreshold.setObjects(
      *(("EQLMEMBER-MIB", "eqlMemberHealthDetailsFanName"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsFanValue"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsFanCurrentState"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsFanHighCriticalThreshold"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsFanHighWarningThreshold"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsFanNameID"))
)
if mibBuilder.loadTexts:
    eqlMemberHealthFanSpeedHighThreshold.setStatus(
        "current"
    )

eqlMemberHealthFanSpeedLowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 4)
)
eqlMemberHealthFanSpeedLowThreshold.setObjects(
      *(("EQLMEMBER-MIB", "eqlMemberHealthDetailsFanName"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsFanValue"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsFanCurrentState"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsFanLowCriticalThreshold"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsFanLowWarningThreshold"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsFanNameID"))
)
if mibBuilder.loadTexts:
    eqlMemberHealthFanSpeedLowThreshold.setStatus(
        "current"
    )

eqlMemberHealthPowerSupplyFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 5)
)
eqlMemberHealthPowerSupplyFanFailure.setObjects(
      *(("EQLMEMBER-MIB", "eqlMemberHealthDetailsPowerSupplyName"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsPowerSupplyFanStatus"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsPowerSupplyNameID"))
)
if mibBuilder.loadTexts:
    eqlMemberHealthPowerSupplyFanFailure.setStatus(
        "current"
    )

eqlMemberHealthPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 6)
)
eqlMemberHealthPowerSupplyFailure.setObjects(
      *(("EQLMEMBER-MIB", "eqlMemberHealthDetailsPowerSupplyName"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsPowerSupplyCurrentState"),
        ("EQLMEMBER-MIB", "eqlMemberHealthDetailsPowerSupplyNameID"))
)
if mibBuilder.loadTexts:
    eqlMemberHealthPowerSupplyFailure.setStatus(
        "current"
    )

eqlMemberHealthRAIDSetDoubleFaulted = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 7)
)
eqlMemberHealthRAIDSetDoubleFaulted.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthRAIDSetDoubleFaulted.setStatus(
        "current"
    )

eqlMemberHealthBothFanTraysRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 8)
)
eqlMemberHealthBothFanTraysRemoved.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthBothFanTraysRemoved.setStatus(
        "current"
    )

eqlMemberHealthRAIDlostCache = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 9)
)
eqlMemberHealthRAIDlostCache.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthRAIDlostCache.setStatus(
        "current"
    )

eqlMemberHealthFanTrayRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 10)
)
eqlMemberHealthFanTrayRemoved.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthFanTrayRemoved.setStatus(
        "current"
    )

eqlMemberHealthRAIDSetLostBlkTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 11)
)
eqlMemberHealthRAIDSetLostBlkTableFull.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthRAIDSetLostBlkTableFull.setStatus(
        "current"
    )

eqlMemberHealthBatteryLessThan72Hours = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 12)
)
eqlMemberHealthBatteryLessThan72Hours.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthBatteryLessThan72Hours.setStatus(
        "current"
    )

eqlMemberHealthRaidOrphanCache = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 13)
)
eqlMemberHealthRaidOrphanCache.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthRaidOrphanCache.setStatus(
        "current"
    )

eqlMemberHealthRaidMultipleRaidSets = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 14)
)
eqlMemberHealthRaidMultipleRaidSets.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthRaidMultipleRaidSets.setStatus(
        "current"
    )

eqlMemberHealthNVRAMBatteryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 15)
)
eqlMemberHealthNVRAMBatteryFailed.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthNVRAMBatteryFailed.setStatus(
        "current"
    )

eqlMemberHealthhwComponentFailedCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 16)
)
eqlMemberHealthhwComponentFailedCrit.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthhwComponentFailedCrit.setStatus(
        "current"
    )

eqlMemberHealthincompatControlModule = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 17)
)
eqlMemberHealthincompatControlModule.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthincompatControlModule.setStatus(
        "current"
    )

eqlMemberHealthlowAmbientTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 18)
)
eqlMemberHealthlowAmbientTemp.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthlowAmbientTemp.setStatus(
        "current"
    )

eqlMemberHealthopsPanelFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 19)
)
eqlMemberHealthopsPanelFailure.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthopsPanelFailure.setStatus(
        "current"
    )

eqlMemberHealthemmLinkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 20)
)
eqlMemberHealthemmLinkFailure.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthemmLinkFailure.setStatus(
        "current"
    )

eqlMemberHealthhighBatteryTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 21)
)
eqlMemberHealthhighBatteryTemperature.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthhighBatteryTemperature.setStatus(
        "current"
    )

eqlMemberHealthenclosureOpenPerm = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 22)
)
eqlMemberHealthenclosureOpenPerm.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthenclosureOpenPerm.setStatus(
        "current"
    )

eqlMemberHealthsumoChannelBothMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 23)
)
eqlMemberHealthsumoChannelBothMissing.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthsumoChannelBothMissing.setStatus(
        "current"
    )

eqlMemberHealthsumoEIPFailureCOndition = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 24)
)
eqlMemberHealthsumoEIPFailureCOndition.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthsumoEIPFailureCOndition.setStatus(
        "current"
    )

eqlMemberHealthsumoChannelBothFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 12740, 2, 2, 1, 25)
)
eqlMemberHealthsumoChannelBothFailed.setObjects(
    ("EQLMEMBER-MIB", "eqlMemberHealthStatus")
)
if mibBuilder.loadTexts:
    eqlMemberHealthsumoChannelBothFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLMEMBER-MIB",
    **{"EqlMemberSEDShareType": EqlMemberSEDShareType,
       "eqlmemberModule": eqlmemberModule,
       "eqlmemberObjects": eqlmemberObjects,
       "eqlMemberTable": eqlMemberTable,
       "eqlMemberEntry": eqlMemberEntry,
       "eqlMemberIndex": eqlMemberIndex,
       "eqlMemberDateAndTime": eqlMemberDateAndTime,
       "eqlMemberTimeZone": eqlMemberTimeZone,
       "eqlMemberAdjustDaylightSavTime": eqlMemberAdjustDaylightSavTime,
       "eqlMemberDefaultRoute": eqlMemberDefaultRoute,
       "eqlMemberSite": eqlMemberSite,
       "eqlMemberDescription": eqlMemberDescription,
       "eqlMemberUUID": eqlMemberUUID,
       "eqlMemberName": eqlMemberName,
       "eqlMemberRowStatus": eqlMemberRowStatus,
       "eqlMemberState": eqlMemberState,
       "eqlMemberPolicySingleControllerSafe": eqlMemberPolicySingleControllerSafe,
       "eqlMemberPolicyLowBatterySafe": eqlMemberPolicyLowBatterySafe,
       "eqlMemberVersion": eqlMemberVersion,
       "eqlMemberDelayDataMove": eqlMemberDelayDataMove,
       "eqlMemberDefaultInetRouteType": eqlMemberDefaultInetRouteType,
       "eqlMemberDefaultInetRoute": eqlMemberDefaultInetRoute,
       "eqlMemberDriveMirroring": eqlMemberDriveMirroring,
       "eqlMemberProfileIndex": eqlMemberProfileIndex,
       "eqlMemberControllerType": eqlMemberControllerType,
       "eqlMemberControllerMajorVersion": eqlMemberControllerMajorVersion,
       "eqlMemberControllerMinorVersion": eqlMemberControllerMinorVersion,
       "eqlMemberControllerMaintenanceVersion": eqlMemberControllerMaintenanceVersion,
       "eqlMemberCompressionCapable": eqlMemberCompressionCapable,
       "eqlMemberStatusTable": eqlMemberStatusTable,
       "eqlMemberStatusEntry": eqlMemberStatusEntry,
       "eqlMemberStatusTotalSpace": eqlMemberStatusTotalSpace,
       "eqlMemberStatusTotalSpaceUsed": eqlMemberStatusTotalSpaceUsed,
       "eqlMemberStatusModel": eqlMemberStatusModel,
       "eqlMemberStatusSerialNumber": eqlMemberStatusSerialNumber,
       "eqlMemberStatusNumberOfControllers": eqlMemberStatusNumberOfControllers,
       "eqlMemberStatusNumberOfDisks": eqlMemberStatusNumberOfDisks,
       "eqlMemberStatusNumberOfSpares": eqlMemberStatusNumberOfSpares,
       "eqlMemberStatusCacheSize": eqlMemberStatusCacheSize,
       "eqlMemberStatusCacheMode": eqlMemberStatusCacheMode,
       "eqlMemberStatusNumberOfConnections": eqlMemberStatusNumberOfConnections,
       "eqlMemberStatusAverageTemp": eqlMemberStatusAverageTemp,
       "eqlMemberStatusTempStatus": eqlMemberStatusTempStatus,
       "eqlMemberStatusBackplaneTempSensor1": eqlMemberStatusBackplaneTempSensor1,
       "eqlMemberStatusBackplaneTempSensor2": eqlMemberStatusBackplaneTempSensor2,
       "eqlMemberStatusPowerSupply1Status": eqlMemberStatusPowerSupply1Status,
       "eqlMemberStatusPowerSupply2Status": eqlMemberStatusPowerSupply2Status,
       "eqlMemberStatusTrayOneFanOneSpeed": eqlMemberStatusTrayOneFanOneSpeed,
       "eqlMemberStatusTrayOneFanTwoSpeed": eqlMemberStatusTrayOneFanTwoSpeed,
       "eqlMemberStatusTrayTwoFanOneSpeed": eqlMemberStatusTrayTwoFanOneSpeed,
       "eqlMemberStatusTrayTwoFanTwoSpeed": eqlMemberStatusTrayTwoFanTwoSpeed,
       "eqlMemberStatusPowerSupplyOneFanStatus": eqlMemberStatusPowerSupplyOneFanStatus,
       "eqlMemberStatusPowerSupplyTwoFanStatus": eqlMemberStatusPowerSupplyTwoFanStatus,
       "eqlMemberStatusRaidStatus": eqlMemberStatusRaidStatus,
       "eqlMemberStatusRaidPercentage": eqlMemberStatusRaidPercentage,
       "eqlMemberStatusLostRaidBlocks": eqlMemberStatusLostRaidBlocks,
       "eqlMemberStatusHealth": eqlMemberStatusHealth,
       "eqlMemberStatusShortId": eqlMemberStatusShortId,
       "eqlMemberInfoTable": eqlMemberInfoTable,
       "eqlMemberInfoEntry": eqlMemberInfoEntry,
       "eqlTargetMemberIndex": eqlTargetMemberIndex,
       "eqlMemberInfoStatus": eqlMemberInfoStatus,
       "eqlMemberHealthTable": eqlMemberHealthTable,
       "eqlMemberHealthEntry": eqlMemberHealthEntry,
       "eqlMemberHealthStatus": eqlMemberHealthStatus,
       "eqlMemberHealthWarningConditions": eqlMemberHealthWarningConditions,
       "eqlMemberHealthCriticalConditions": eqlMemberHealthCriticalConditions,
       "eqlMemberHealthDetailsTemperatureTable": eqlMemberHealthDetailsTemperatureTable,
       "eqlMemberHealthDetailsTemperatureEntry": eqlMemberHealthDetailsTemperatureEntry,
       "eqlMemberHealthDetailsTempSensorIndex": eqlMemberHealthDetailsTempSensorIndex,
       "eqlMemberHealthDetailsTemperatureName": eqlMemberHealthDetailsTemperatureName,
       "eqlMemberHealthDetailsTemperatureValue": eqlMemberHealthDetailsTemperatureValue,
       "eqlMemberHealthDetailsTemperatureCurrentState": eqlMemberHealthDetailsTemperatureCurrentState,
       "eqlMemberHealthDetailsTemperatureHighCriticalThreshold": eqlMemberHealthDetailsTemperatureHighCriticalThreshold,
       "eqlMemberHealthDetailsTemperatureHighWarningThreshold": eqlMemberHealthDetailsTemperatureHighWarningThreshold,
       "eqlMemberHealthDetailsTemperatureLowCriticalThreshold": eqlMemberHealthDetailsTemperatureLowCriticalThreshold,
       "eqlMemberHealthDetailsTemperatureLowWarningThreshold": eqlMemberHealthDetailsTemperatureLowWarningThreshold,
       "eqlMemberHealthDetailsTemperatureNameID": eqlMemberHealthDetailsTemperatureNameID,
       "eqlMemberHealthDetailsFanTable": eqlMemberHealthDetailsFanTable,
       "eqlMemberHealthDetailsFanEntry": eqlMemberHealthDetailsFanEntry,
       "eqlMemberHealthDetailsFanIndex": eqlMemberHealthDetailsFanIndex,
       "eqlMemberHealthDetailsFanName": eqlMemberHealthDetailsFanName,
       "eqlMemberHealthDetailsFanValue": eqlMemberHealthDetailsFanValue,
       "eqlMemberHealthDetailsFanCurrentState": eqlMemberHealthDetailsFanCurrentState,
       "eqlMemberHealthDetailsFanHighCriticalThreshold": eqlMemberHealthDetailsFanHighCriticalThreshold,
       "eqlMemberHealthDetailsFanHighWarningThreshold": eqlMemberHealthDetailsFanHighWarningThreshold,
       "eqlMemberHealthDetailsFanLowCriticalThreshold": eqlMemberHealthDetailsFanLowCriticalThreshold,
       "eqlMemberHealthDetailsFanLowWarningThreshold": eqlMemberHealthDetailsFanLowWarningThreshold,
       "eqlMemberHealthDetailsFanNameID": eqlMemberHealthDetailsFanNameID,
       "eqlMemberHealthDetailsPowerSupplyTable": eqlMemberHealthDetailsPowerSupplyTable,
       "eqlMemberHealthDetailsPowerSupplyEntry": eqlMemberHealthDetailsPowerSupplyEntry,
       "eqlMemberHealthDetailsPowerSupplyIndex": eqlMemberHealthDetailsPowerSupplyIndex,
       "eqlMemberHealthDetailsPowerSupplyName": eqlMemberHealthDetailsPowerSupplyName,
       "eqlMemberHealthDetailsPowerSupplyCurrentState": eqlMemberHealthDetailsPowerSupplyCurrentState,
       "eqlMemberHealthDetailsPowerSupplyFanStatus": eqlMemberHealthDetailsPowerSupplyFanStatus,
       "eqlMemberHealthDetailsPowerSupplyFirmwareVersion": eqlMemberHealthDetailsPowerSupplyFirmwareVersion,
       "eqlMemberHealthDetailsPowerSupplyNameID": eqlMemberHealthDetailsPowerSupplyNameID,
       "eqlMemberIdentificationTable": eqlMemberIdentificationTable,
       "eqlMemberIdentificationEntry": eqlMemberIdentificationEntry,
       "eqlMemberIdentificationLEDsBlinking": eqlMemberIdentificationLEDsBlinking,
       "eqlMemberStorageTable": eqlMemberStorageTable,
       "eqlMemberStorageEntry": eqlMemberStorageEntry,
       "eqlMemberTotalStorage": eqlMemberTotalStorage,
       "eqlMemberUsedStorage": eqlMemberUsedStorage,
       "eqlMemberSnapStorage": eqlMemberSnapStorage,
       "eqlMemberReplStorage": eqlMemberReplStorage,
       "eqlMemberVirtualStorage": eqlMemberVirtualStorage,
       "eqlMemberCompressionStackStorage": eqlMemberCompressionStackStorage,
       "eqlMemberChassisTable": eqlMemberChassisTable,
       "eqlMemberChassisEntry": eqlMemberChassisEntry,
       "eqlMemberModel": eqlMemberModel,
       "eqlMemberSerialNumber": eqlMemberSerialNumber,
       "eqlMemberNumberOfControllers": eqlMemberNumberOfControllers,
       "eqlMemberNumberOfDisks": eqlMemberNumberOfDisks,
       "eqlMemberCacheSize": eqlMemberCacheSize,
       "eqlMemberCacheMode": eqlMemberCacheMode,
       "eqlMemberChassisType": eqlMemberChassisType,
       "eqlMemberServiceTag": eqlMemberServiceTag,
       "eqlMemberProductFamily": eqlMemberProductFamily,
       "eqlMemberChassisFlags": eqlMemberChassisFlags,
       "eqlMemberChassisDiskSectorSize": eqlMemberChassisDiskSectorSize,
       "eqlMemberConnTable": eqlMemberConnTable,
       "eqlMemberConnEntry": eqlMemberConnEntry,
       "eqlMemberNumberOfConnections": eqlMemberNumberOfConnections,
       "eqlMemberReadLatency": eqlMemberReadLatency,
       "eqlMemberWriteLatency": eqlMemberWriteLatency,
       "eqlMemberReadAvgLatency": eqlMemberReadAvgLatency,
       "eqlMemberWriteAvgLatency": eqlMemberWriteAvgLatency,
       "eqlMemberReadOpCount": eqlMemberReadOpCount,
       "eqlMemberWriteOpCount": eqlMemberWriteOpCount,
       "eqlMemberTxData": eqlMemberTxData,
       "eqlMemberRxData": eqlMemberRxData,
       "eqlMemberNumberOfExtConnections": eqlMemberNumberOfExtConnections,
       "eqlMemberRAIDTable": eqlMemberRAIDTable,
       "eqlMemberRAIDEntry": eqlMemberRAIDEntry,
       "eqlMemberRaidStatus": eqlMemberRaidStatus,
       "eqlMemberRaidPercentage": eqlMemberRaidPercentage,
       "eqlMemberLostRaidBlocks": eqlMemberLostRaidBlocks,
       "eqlMemberNumberOfSpares": eqlMemberNumberOfSpares,
       "eqlMemberRaidProgress": eqlMemberRaidProgress,
       "eqlMemberPSGMapTable": eqlMemberPSGMapTable,
       "eqlMemberPSGMapEntry": eqlMemberPSGMapEntry,
       "eqlMemberShortId": eqlMemberShortId,
       "eqlDriveGroupTable": eqlDriveGroupTable,
       "eqlDriveGroupEntry": eqlDriveGroupEntry,
       "eqlDriveGroupIndex": eqlDriveGroupIndex,
       "eqlDriveGroupStoragePoolIndex": eqlDriveGroupStoragePoolIndex,
       "eqlDriveGroupRAIDPolicy": eqlDriveGroupRAIDPolicy,
       "eqlDriveGroupOpsTable": eqlDriveGroupOpsTable,
       "eqlDriveGroupOpsEntry": eqlDriveGroupOpsEntry,
       "eqlDriveGroupOpsIndex": eqlDriveGroupOpsIndex,
       "eqlDriveGroupOpsRowStatus": eqlDriveGroupOpsRowStatus,
       "eqlDriveGroupOpsOperation": eqlDriveGroupOpsOperation,
       "eqlDriveGroupOpsExec": eqlDriveGroupOpsExec,
       "eqlDriveGroupOpsStartTime": eqlDriveGroupOpsStartTime,
       "eqlDriveGroupOpsStoragePoolSourceIndex": eqlDriveGroupOpsStoragePoolSourceIndex,
       "eqlDriveGroupOpsStoragePoolDestinationIndex": eqlDriveGroupOpsStoragePoolDestinationIndex,
       "eqlDriveGroupOpsVolBalCommandIndex": eqlDriveGroupOpsVolBalCommandIndex,
       "eqlDriveGroupOpsVolBalCommandiscsiLocalMemberId": eqlDriveGroupOpsVolBalCommandiscsiLocalMemberId,
       "eqlAdminAccountMemberTable": eqlAdminAccountMemberTable,
       "eqlAdminAccountMemberEntry": eqlAdminAccountMemberEntry,
       "eqlAdminAccountMemberAccess": eqlAdminAccountMemberAccess,
       "eqlDriveGroupOpsStatusTable": eqlDriveGroupOpsStatusTable,
       "eqlDriveGroupOpsStatusEntry": eqlDriveGroupOpsStatusEntry,
       "eqlDriveGroupOpsStatusCompletePct": eqlDriveGroupOpsStatusCompletePct,
       "eqlMemberOpsTable": eqlMemberOpsTable,
       "eqlMemberOpsEntry": eqlMemberOpsEntry,
       "eqlMemberOpsIndex": eqlMemberOpsIndex,
       "eqlMemberOpsRowStatus": eqlMemberOpsRowStatus,
       "eqlMemberOpsOperation": eqlMemberOpsOperation,
       "eqlMemberOpsExec": eqlMemberOpsExec,
       "eqlMemberOpsCompletePct": eqlMemberOpsCompletePct,
       "eqlMemberOpsOperationArg": eqlMemberOpsOperationArg,
       "eqlMemberOpsOperationStatus": eqlMemberOpsOperationStatus,
       "eqlMemberOpsStartTime": eqlMemberOpsStartTime,
       "eqlMemberOpsOperationArg1": eqlMemberOpsOperationArg1,
       "eqlMemberHWComponentTable": eqlMemberHWComponentTable,
       "eqlMemberHWComponentEntry": eqlMemberHWComponentEntry,
       "eqlMemberHWComponentIndex": eqlMemberHWComponentIndex,
       "eqlMemberHWComponentName": eqlMemberHWComponentName,
       "eqlMemberHWComponentSerialNumber": eqlMemberHWComponentSerialNumber,
       "eqlMemberHWComponentFirmwareRev": eqlMemberHWComponentFirmwareRev,
       "eqlMemberHWComponentStatus": eqlMemberHWComponentStatus,
       "eqlMemberDynamicInfoTable": eqlMemberDynamicInfoTable,
       "eqlMemberDynamicInfoEntry": eqlMemberDynamicInfoEntry,
       "eqlMemberDynamicInfoPendingUpdateVersion": eqlMemberDynamicInfoPendingUpdateVersion,
       "eqlMemberDynamicInfoIsRestartRunning": eqlMemberDynamicInfoIsRestartRunning,
       "eqlMemberDynamicInfoIsUpdateRunning": eqlMemberDynamicInfoIsUpdateRunning,
       "eqlMemberCacheStatisticsTable": eqlMemberCacheStatisticsTable,
       "eqlMemberCacheStatisticsEntry": eqlMemberCacheStatisticsEntry,
       "eqlMemberTotalPageCount": eqlMemberTotalPageCount,
       "eqlMemberHotPageCount": eqlMemberHotPageCount,
       "eqlMemberWarmPageCount": eqlMemberWarmPageCount,
       "eqlMemberColdPageCount": eqlMemberColdPageCount,
       "eqlMemberPageSize": eqlMemberPageSize,
       "eqlMemberSSDAcceleratorSize": eqlMemberSSDAcceleratorSize,
       "eqlMemberSSDCacheSize": eqlMemberSSDCacheSize,
       "eqlMemberSSDAcceleratorEntriesTotal": eqlMemberSSDAcceleratorEntriesTotal,
       "eqlMemberSSDAcceleratorEntriesUsed": eqlMemberSSDAcceleratorEntriesUsed,
       "eqlMemberSEDEncryptionTable": eqlMemberSEDEncryptionTable,
       "eqlMemberSEDEncryptionEntry": eqlMemberSEDEncryptionEntry,
       "eqlMemberSEDEncryptionRowStatus": eqlMemberSEDEncryptionRowStatus,
       "eqlMemberSEDEncryptionShare1": eqlMemberSEDEncryptionShare1,
       "eqlMemberSEDEncryptionShare2": eqlMemberSEDEncryptionShare2,
       "eqlMemberSEDEncryptionShare3": eqlMemberSEDEncryptionShare3,
       "eqlMemberDynamicOpsTable": eqlMemberDynamicOpsTable,
       "eqlMemberDynamicOpsEntry": eqlMemberDynamicOpsEntry,
       "eqlMemberDynamicOpsOperation": eqlMemberDynamicOpsOperation,
       "eqlMemberDynamicOpsOperationArg": eqlMemberDynamicOpsOperationArg,
       "eqlMemberGroupInfoAtMemberTable": eqlMemberGroupInfoAtMemberTable,
       "eqlMemberGroupInfoAtMemberEntry": eqlMemberGroupInfoAtMemberEntry,
       "eqlMemberGroupInfoAtMemberPasswd1": eqlMemberGroupInfoAtMemberPasswd1,
       "eqlMemberGroupInfoAtMemberPasswd1Len": eqlMemberGroupInfoAtMemberPasswd1Len,
       "eqlDriveGroupStatisticsTable": eqlDriveGroupStatisticsTable,
       "eqlDriveGroupStatisticsEntry": eqlDriveGroupStatisticsEntry,
       "eqlDriveGroupStatisticsIndex": eqlDriveGroupStatisticsIndex,
       "eqlDriveGroupStatisticsHeadroom": eqlDriveGroupStatisticsHeadroom,
       "eqlMemberFirmwareInfoTable": eqlMemberFirmwareInfoTable,
       "eqlMemberFirmwareInfoEntry": eqlMemberFirmwareInfoEntry,
       "eqlMemberLanguageVersion": eqlMemberLanguageVersion,
       "eqlMemberFirmwareInfoDataReduction": eqlMemberFirmwareInfoDataReduction,
       "eqlDriveGroupHeatProfileInfoTable": eqlDriveGroupHeatProfileInfoTable,
       "eqlDriveGroupHeatProfileInfoEntry": eqlDriveGroupHeatProfileInfoEntry,
       "eqlDriveGroupHeatProfilePart": eqlDriveGroupHeatProfilePart,
       "eqlDriveGroupHeatProfileColdCount": eqlDriveGroupHeatProfileColdCount,
       "eqlDriveGroupHeatProfileMinMagnitude": eqlDriveGroupHeatProfileMinMagnitude,
       "eqlDriveGroupHeatProfileMinMultiplier": eqlDriveGroupHeatProfileMinMultiplier,
       "eqlDriveGroupHeatProfileMaxMagnitude": eqlDriveGroupHeatProfileMaxMagnitude,
       "eqlDriveGroupHeatProfileMaxMultiplier": eqlDriveGroupHeatProfileMaxMultiplier,
       "eqlDriveGroupHeatProfileBinTable": eqlDriveGroupHeatProfileBinTable,
       "eqlDriveGroupHeatProfileBinEntry": eqlDriveGroupHeatProfileBinEntry,
       "eqlDriveGroupHeatProfileBinId": eqlDriveGroupHeatProfileBinId,
       "eqlDriveGroupHeatProfileAccessRateMagnitude": eqlDriveGroupHeatProfileAccessRateMagnitude,
       "eqlDriveGroupHeatProfileAccessRateMultiplier": eqlDriveGroupHeatProfileAccessRateMultiplier,
       "eqlDriveGroupHeatProfileCount": eqlDriveGroupHeatProfileCount,
       "eqlTaggedHeatProfileInfoTable": eqlTaggedHeatProfileInfoTable,
       "eqlTaggedHeatProfileInfoEntry": eqlTaggedHeatProfileInfoEntry,
       "eqlTaggedHeatTag": eqlTaggedHeatTag,
       "eqlTaggedHeatProfileColdCount": eqlTaggedHeatProfileColdCount,
       "eqlTaggedHeatProfileMinMagnitude": eqlTaggedHeatProfileMinMagnitude,
       "eqlTaggedHeatProfileMinMultiplier": eqlTaggedHeatProfileMinMultiplier,
       "eqlTaggedHeatProfileMaxMagnitude": eqlTaggedHeatProfileMaxMagnitude,
       "eqlTaggedHeatProfileMaxMultiplier": eqlTaggedHeatProfileMaxMultiplier,
       "eqlTaggedHeatProfileBinTable": eqlTaggedHeatProfileBinTable,
       "eqlTaggedHeatProfileBinEntry": eqlTaggedHeatProfileBinEntry,
       "eqlTaggedHeatProfileBinId": eqlTaggedHeatProfileBinId,
       "eqlTaggedHeatProfileAccessRateMagnitude": eqlTaggedHeatProfileAccessRateMagnitude,
       "eqlTaggedHeatProfileAccessRateMultiplier": eqlTaggedHeatProfileAccessRateMultiplier,
       "eqlTaggedHeatProfileCount": eqlTaggedHeatProfileCount,
       "eqlMemberRaidPoliciesTable": eqlMemberRaidPoliciesTable,
       "eqlMemberRaidPoliciesEntry": eqlMemberRaidPoliciesEntry,
       "eqlMemberRaidPoliciesBehavior": eqlMemberRaidPoliciesBehavior,
       "eqlMemberRaidPoliciesRAIDCapacity": eqlMemberRaidPoliciesRAIDCapacity,
       "eqlMemberPerTCPConnectionStatsTable": eqlMemberPerTCPConnectionStatsTable,
       "eqlMemberPerTCPConnectionStatsEntry": eqlMemberPerTCPConnectionStatsEntry,
       "eqlMemberPerTCPConnectionStatsIndex": eqlMemberPerTCPConnectionStatsIndex,
       "eqlMemberPerTCPConnectionStatsLocalAddrType": eqlMemberPerTCPConnectionStatsLocalAddrType,
       "eqlMemberPerTCPConnectionStatsLocalAddr": eqlMemberPerTCPConnectionStatsLocalAddr,
       "eqlMemberPerTCPConnectionStatsLocalPort": eqlMemberPerTCPConnectionStatsLocalPort,
       "eqlMemberPerTCPConnectionStatsForeignAddrType": eqlMemberPerTCPConnectionStatsForeignAddrType,
       "eqlMemberPerTCPConnectionStatsForeignAddr": eqlMemberPerTCPConnectionStatsForeignAddr,
       "eqlMemberPerTCPConnectionStatsForeignPort": eqlMemberPerTCPConnectionStatsForeignPort,
       "eqlMemberPerTCPConnectionStatsMss": eqlMemberPerTCPConnectionStatsMss,
       "eqlMemberPerTCPConnectionStatsState": eqlMemberPerTCPConnectionStatsState,
       "eqlMemberPerTCPConnectionStatsSndpack": eqlMemberPerTCPConnectionStatsSndpack,
       "eqlMemberPerTCPConnectionStatsSndbyte": eqlMemberPerTCPConnectionStatsSndbyte,
       "eqlMemberPerTCPConnectionStatsSndrexmitpack": eqlMemberPerTCPConnectionStatsSndrexmitpack,
       "eqlMemberPerTCPConnectionStatsSndrexmitbyte": eqlMemberPerTCPConnectionStatsSndrexmitbyte,
       "eqlMemberPerTCPConnectionStatsRexmttimeout": eqlMemberPerTCPConnectionStatsRexmttimeout,
       "eqlMemberPerTCPConnectionStatsFastrexmt": eqlMemberPerTCPConnectionStatsFastrexmt,
       "eqlMemberPerTCPConnectionStatsSndprobe": eqlMemberPerTCPConnectionStatsSndprobe,
       "eqlMemberPerTCPConnectionStatsRcvpack": eqlMemberPerTCPConnectionStatsRcvpack,
       "eqlMemberPerTCPConnectionStatsRcvbyte": eqlMemberPerTCPConnectionStatsRcvbyte,
       "eqlMemberPerTCPConnectionStatsRcvwinprobe": eqlMemberPerTCPConnectionStatsRcvwinprobe,
       "eqlMemberPerTCPConnectionStatsRcvbadsum": eqlMemberPerTCPConnectionStatsRcvbadsum,
       "eqlmemberNotifications": eqlmemberNotifications,
       "eqlMemberEnclosureMgmtNotifications": eqlMemberEnclosureMgmtNotifications,
       "eqlMemberHealthTempSensorHighThreshold": eqlMemberHealthTempSensorHighThreshold,
       "eqlMemberHealthTempSensorLowThreshold": eqlMemberHealthTempSensorLowThreshold,
       "eqlMemberHealthFanSpeedHighThreshold": eqlMemberHealthFanSpeedHighThreshold,
       "eqlMemberHealthFanSpeedLowThreshold": eqlMemberHealthFanSpeedLowThreshold,
       "eqlMemberHealthPowerSupplyFanFailure": eqlMemberHealthPowerSupplyFanFailure,
       "eqlMemberHealthPowerSupplyFailure": eqlMemberHealthPowerSupplyFailure,
       "eqlMemberHealthRAIDSetDoubleFaulted": eqlMemberHealthRAIDSetDoubleFaulted,
       "eqlMemberHealthBothFanTraysRemoved": eqlMemberHealthBothFanTraysRemoved,
       "eqlMemberHealthRAIDlostCache": eqlMemberHealthRAIDlostCache,
       "eqlMemberHealthFanTrayRemoved": eqlMemberHealthFanTrayRemoved,
       "eqlMemberHealthRAIDSetLostBlkTableFull": eqlMemberHealthRAIDSetLostBlkTableFull,
       "eqlMemberHealthBatteryLessThan72Hours": eqlMemberHealthBatteryLessThan72Hours,
       "eqlMemberHealthRaidOrphanCache": eqlMemberHealthRaidOrphanCache,
       "eqlMemberHealthRaidMultipleRaidSets": eqlMemberHealthRaidMultipleRaidSets,
       "eqlMemberHealthNVRAMBatteryFailed": eqlMemberHealthNVRAMBatteryFailed,
       "eqlMemberHealthhwComponentFailedCrit": eqlMemberHealthhwComponentFailedCrit,
       "eqlMemberHealthincompatControlModule": eqlMemberHealthincompatControlModule,
       "eqlMemberHealthlowAmbientTemp": eqlMemberHealthlowAmbientTemp,
       "eqlMemberHealthopsPanelFailure": eqlMemberHealthopsPanelFailure,
       "eqlMemberHealthemmLinkFailure": eqlMemberHealthemmLinkFailure,
       "eqlMemberHealthhighBatteryTemperature": eqlMemberHealthhighBatteryTemperature,
       "eqlMemberHealthenclosureOpenPerm": eqlMemberHealthenclosureOpenPerm,
       "eqlMemberHealthsumoChannelBothMissing": eqlMemberHealthsumoChannelBothMissing,
       "eqlMemberHealthsumoEIPFailureCOndition": eqlMemberHealthsumoEIPFailureCOndition,
       "eqlMemberHealthsumoChannelBothFailed": eqlMemberHealthsumoChannelBothFailed,
       "eqlmemberConformance": eqlmemberConformance}
)
