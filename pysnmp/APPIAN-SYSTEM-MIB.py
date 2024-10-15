# SNMP MIB module (APPIAN-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:45 2024
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

(acChassisCurrentTime,
 acChassisRingId) = mibBuilder.importSymbols(
    "APPIAN-CHASSIS-MIB",
    "acChassisCurrentTime",
    "acChassisRingId")

(AcAdminStatus,
 AcNodeArchitecture,
 AcNodeId,
 AcOpStatus,
 acOsap) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "AcNodeArchitecture",
    "AcNodeId",
    "AcOpStatus",
    "acOsap")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7)
)
acSystem.setRevisions(
        ("1999-11-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcAccessRights(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2),
          ("security", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AcCommMgr_ObjectIdentity = ObjectIdentity
acCommMgr = _AcCommMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1)
)
_AcCommMgrCommTable_Object = MibTable
acCommMgrCommTable = _AcCommMgrCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    acCommMgrCommTable.setStatus("current")
_AcCommMgrCommEntry_Object = MibTableRow
acCommMgrCommEntry = _AcCommMgrCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 1, 1)
)
acCommMgrCommEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acCommMgrCommNodeId"),
    (0, "APPIAN-SYSTEM-MIB", "acCommMgrCommId"),
)
if mibBuilder.loadTexts:
    acCommMgrCommEntry.setStatus("current")
_AcCommMgrCommNodeId_Type = AcNodeId
_AcCommMgrCommNodeId_Object = MibTableColumn
acCommMgrCommNodeId = _AcCommMgrCommNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 1, 1, 1),
    _AcCommMgrCommNodeId_Type()
)
acCommMgrCommNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acCommMgrCommNodeId.setStatus("current")
_AcCommMgrCommId_Type = Integer32
_AcCommMgrCommId_Object = MibTableColumn
acCommMgrCommId = _AcCommMgrCommId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 1, 1, 2),
    _AcCommMgrCommId_Type()
)
acCommMgrCommId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acCommMgrCommId.setStatus("current")
_AcCommMgrCommAdminStatus_Type = AcAdminStatus
_AcCommMgrCommAdminStatus_Object = MibTableColumn
acCommMgrCommAdminStatus = _AcCommMgrCommAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 1, 1, 3),
    _AcCommMgrCommAdminStatus_Type()
)
acCommMgrCommAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acCommMgrCommAdminStatus.setStatus("current")


class _AcCommMgrCommString_Type(DisplayString):
    """Custom type acCommMgrCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcCommMgrCommString_Type.__name__ = "DisplayString"
_AcCommMgrCommString_Object = MibTableColumn
acCommMgrCommString = _AcCommMgrCommString_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 1, 1, 4),
    _AcCommMgrCommString_Type()
)
acCommMgrCommString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acCommMgrCommString.setStatus("current")
_AcCommMgrCommAccessRights_Type = AcAccessRights
_AcCommMgrCommAccessRights_Object = MibTableColumn
acCommMgrCommAccessRights = _AcCommMgrCommAccessRights_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 1, 1, 5),
    _AcCommMgrCommAccessRights_Type()
)
acCommMgrCommAccessRights.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acCommMgrCommAccessRights.setStatus("current")
_AcCommMgrSourceAddrTable_Object = MibTable
acCommMgrSourceAddrTable = _AcCommMgrSourceAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    acCommMgrSourceAddrTable.setStatus("current")
_AcCommMgrSourceAddrEntry_Object = MibTableRow
acCommMgrSourceAddrEntry = _AcCommMgrSourceAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 2, 1)
)
acCommMgrSourceAddrEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acCommMgrSourceAddrNodeId"),
    (0, "APPIAN-SYSTEM-MIB", "acCommMgrSourceAddrCommId"),
    (0, "APPIAN-SYSTEM-MIB", "acCommMgrSourceAddrIpAddress"),
)
if mibBuilder.loadTexts:
    acCommMgrSourceAddrEntry.setStatus("current")
_AcCommMgrSourceAddrNodeId_Type = AcNodeId
_AcCommMgrSourceAddrNodeId_Object = MibTableColumn
acCommMgrSourceAddrNodeId = _AcCommMgrSourceAddrNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 2, 1, 1),
    _AcCommMgrSourceAddrNodeId_Type()
)
acCommMgrSourceAddrNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acCommMgrSourceAddrNodeId.setStatus("current")
_AcCommMgrSourceAddrCommId_Type = Integer32
_AcCommMgrSourceAddrCommId_Object = MibTableColumn
acCommMgrSourceAddrCommId = _AcCommMgrSourceAddrCommId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 2, 1, 2),
    _AcCommMgrSourceAddrCommId_Type()
)
acCommMgrSourceAddrCommId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acCommMgrSourceAddrCommId.setStatus("current")
_AcCommMgrSourceAddrIpAddress_Type = IpAddress
_AcCommMgrSourceAddrIpAddress_Object = MibTableColumn
acCommMgrSourceAddrIpAddress = _AcCommMgrSourceAddrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 2, 1, 3),
    _AcCommMgrSourceAddrIpAddress_Type()
)
acCommMgrSourceAddrIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acCommMgrSourceAddrIpAddress.setStatus("current")
_AcCommMgrSourceAddrIpSubnet_Type = IpAddress
_AcCommMgrSourceAddrIpSubnet_Object = MibTableColumn
acCommMgrSourceAddrIpSubnet = _AcCommMgrSourceAddrIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 2, 1, 4),
    _AcCommMgrSourceAddrIpSubnet_Type()
)
acCommMgrSourceAddrIpSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acCommMgrSourceAddrIpSubnet.setStatus("current")
_AcCommMgrSourceAddrAdminStatus_Type = AcAdminStatus
_AcCommMgrSourceAddrAdminStatus_Object = MibTableColumn
acCommMgrSourceAddrAdminStatus = _AcCommMgrSourceAddrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 1, 2, 1, 5),
    _AcCommMgrSourceAddrAdminStatus_Type()
)
acCommMgrSourceAddrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acCommMgrSourceAddrAdminStatus.setStatus("current")
_AcStatsMgr_ObjectIdentity = ObjectIdentity
acStatsMgr = _AcStatsMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 2)
)
_AcStatsMgrTable_Object = MibTable
acStatsMgrTable = _AcStatsMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    acStatsMgrTable.setStatus("current")
_AcStatsMgrEntry_Object = MibTableRow
acStatsMgrEntry = _AcStatsMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 2, 1, 1)
)
acStatsMgrEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acStatsMgrNodeId"),
)
if mibBuilder.loadTexts:
    acStatsMgrEntry.setStatus("current")
_AcStatsMgrNodeId_Type = AcNodeId
_AcStatsMgrNodeId_Object = MibTableColumn
acStatsMgrNodeId = _AcStatsMgrNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 2, 1, 1, 1),
    _AcStatsMgrNodeId_Type()
)
acStatsMgrNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acStatsMgrNodeId.setStatus("current")


class _AcStatsMgrAdminStatus_Type(AcAdminStatus):
    """Custom type acStatsMgrAdminStatus based on AcAdminStatus"""


_AcStatsMgrAdminStatus_Object = MibTableColumn
acStatsMgrAdminStatus = _AcStatsMgrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 2, 1, 1, 2),
    _AcStatsMgrAdminStatus_Type()
)
acStatsMgrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acStatsMgrAdminStatus.setStatus("current")
_AcEventMgr_ObjectIdentity = ObjectIdentity
acEventMgr = _AcEventMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3)
)
_AcEventMgrTraps_ObjectIdentity = ObjectIdentity
acEventMgrTraps = _AcEventMgrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 0)
)
_AcEventMgrControlTable_Object = MibTable
acEventMgrControlTable = _AcEventMgrControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1)
)
if mibBuilder.loadTexts:
    acEventMgrControlTable.setStatus("current")
_AcEventMgrControlEntry_Object = MibTableRow
acEventMgrControlEntry = _AcEventMgrControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1)
)
acEventMgrControlEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acEventMgrControlNodeId"),
)
if mibBuilder.loadTexts:
    acEventMgrControlEntry.setStatus("current")
_AcEventMgrControlNodeId_Type = AcNodeId
_AcEventMgrControlNodeId_Object = MibTableColumn
acEventMgrControlNodeId = _AcEventMgrControlNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 1),
    _AcEventMgrControlNodeId_Type()
)
acEventMgrControlNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acEventMgrControlNodeId.setStatus("current")


class _AcEventMgrControlAdminStatus_Type(AcAdminStatus):
    """Custom type acEventMgrControlAdminStatus based on AcAdminStatus"""


_AcEventMgrControlAdminStatus_Object = MibTableColumn
acEventMgrControlAdminStatus = _AcEventMgrControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 2),
    _AcEventMgrControlAdminStatus_Type()
)
acEventMgrControlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEventMgrControlAdminStatus.setStatus("deprecated")


class _AcEventMgrControlLogMode_Type(Integer32):
    """Custom type acEventMgrControlLogMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash-only", 2),
          ("off", 1))
    )


_AcEventMgrControlLogMode_Type.__name__ = "Integer32"
_AcEventMgrControlLogMode_Object = MibTableColumn
acEventMgrControlLogMode = _AcEventMgrControlLogMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 3),
    _AcEventMgrControlLogMode_Type()
)
acEventMgrControlLogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEventMgrControlLogMode.setStatus("current")


class _AcEventMgrControlLogMaxFileSize_Type(Integer32):
    """Custom type acEventMgrControlLogMaxFileSize based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1024),
    )


_AcEventMgrControlLogMaxFileSize_Type.__name__ = "Integer32"
_AcEventMgrControlLogMaxFileSize_Object = MibTableColumn
acEventMgrControlLogMaxFileSize = _AcEventMgrControlLogMaxFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 4),
    _AcEventMgrControlLogMaxFileSize_Type()
)
acEventMgrControlLogMaxFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEventMgrControlLogMaxFileSize.setStatus("current")
_AcEventMgrControlLogCurrentSize_Type = Integer32
_AcEventMgrControlLogCurrentSize_Object = MibTableColumn
acEventMgrControlLogCurrentSize = _AcEventMgrControlLogCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 5),
    _AcEventMgrControlLogCurrentSize_Type()
)
acEventMgrControlLogCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEventMgrControlLogCurrentSize.setStatus("current")


class _AcEventMgrControlLogFileName_Type(DisplayString):
    """Custom type acEventMgrControlLogFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcEventMgrControlLogFileName_Type.__name__ = "DisplayString"
_AcEventMgrControlLogFileName_Object = MibTableColumn
acEventMgrControlLogFileName = _AcEventMgrControlLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 6),
    _AcEventMgrControlLogFileName_Type()
)
acEventMgrControlLogFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEventMgrControlLogFileName.setStatus("current")


class _AcEventMgrControlLogFileWrapEnable_Type(TruthValue):
    """Custom type acEventMgrControlLogFileWrapEnable based on TruthValue"""


_AcEventMgrControlLogFileWrapEnable_Object = MibTableColumn
acEventMgrControlLogFileWrapEnable = _AcEventMgrControlLogFileWrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 7),
    _AcEventMgrControlLogFileWrapEnable_Type()
)
acEventMgrControlLogFileWrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEventMgrControlLogFileWrapEnable.setStatus("deprecated")


class _AcEventMgrControlSecurityLogMode_Type(Integer32):
    """Custom type acEventMgrControlSecurityLogMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash-only", 2),
          ("off", 1))
    )


_AcEventMgrControlSecurityLogMode_Type.__name__ = "Integer32"
_AcEventMgrControlSecurityLogMode_Object = MibTableColumn
acEventMgrControlSecurityLogMode = _AcEventMgrControlSecurityLogMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 8),
    _AcEventMgrControlSecurityLogMode_Type()
)
acEventMgrControlSecurityLogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEventMgrControlSecurityLogMode.setStatus("current")


class _AcEventMgrControlSecurityLogMaxFileSize_Type(Integer32):
    """Custom type acEventMgrControlSecurityLogMaxFileSize based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1024),
    )


_AcEventMgrControlSecurityLogMaxFileSize_Type.__name__ = "Integer32"
_AcEventMgrControlSecurityLogMaxFileSize_Object = MibTableColumn
acEventMgrControlSecurityLogMaxFileSize = _AcEventMgrControlSecurityLogMaxFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 9),
    _AcEventMgrControlSecurityLogMaxFileSize_Type()
)
acEventMgrControlSecurityLogMaxFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEventMgrControlSecurityLogMaxFileSize.setStatus("current")
_AcEventMgrControlSecurityLogCurrentSize_Type = Integer32
_AcEventMgrControlSecurityLogCurrentSize_Object = MibTableColumn
acEventMgrControlSecurityLogCurrentSize = _AcEventMgrControlSecurityLogCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 10),
    _AcEventMgrControlSecurityLogCurrentSize_Type()
)
acEventMgrControlSecurityLogCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEventMgrControlSecurityLogCurrentSize.setStatus("current")


class _AcEventMgrControlSecurityLogFileName_Type(DisplayString):
    """Custom type acEventMgrControlSecurityLogFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcEventMgrControlSecurityLogFileName_Type.__name__ = "DisplayString"
_AcEventMgrControlSecurityLogFileName_Object = MibTableColumn
acEventMgrControlSecurityLogFileName = _AcEventMgrControlSecurityLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 11),
    _AcEventMgrControlSecurityLogFileName_Type()
)
acEventMgrControlSecurityLogFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEventMgrControlSecurityLogFileName.setStatus("current")


class _AcEventMgrControlSecurityLogFileWrapEnable_Type(TruthValue):
    """Custom type acEventMgrControlSecurityLogFileWrapEnable based on TruthValue"""


_AcEventMgrControlSecurityLogFileWrapEnable_Object = MibTableColumn
acEventMgrControlSecurityLogFileWrapEnable = _AcEventMgrControlSecurityLogFileWrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 12),
    _AcEventMgrControlSecurityLogFileWrapEnable_Type()
)
acEventMgrControlSecurityLogFileWrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEventMgrControlSecurityLogFileWrapEnable.setStatus("deprecated")


class _AcEventMgrControlRedirectTraceSlot1_Type(TruthValue):
    """Custom type acEventMgrControlRedirectTraceSlot1 based on TruthValue"""


_AcEventMgrControlRedirectTraceSlot1_Object = MibTableColumn
acEventMgrControlRedirectTraceSlot1 = _AcEventMgrControlRedirectTraceSlot1_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 13),
    _AcEventMgrControlRedirectTraceSlot1_Type()
)
acEventMgrControlRedirectTraceSlot1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEventMgrControlRedirectTraceSlot1.setStatus("current")


class _AcEventMgrControlRedirectTraceSlot2_Type(TruthValue):
    """Custom type acEventMgrControlRedirectTraceSlot2 based on TruthValue"""


_AcEventMgrControlRedirectTraceSlot2_Object = MibTableColumn
acEventMgrControlRedirectTraceSlot2 = _AcEventMgrControlRedirectTraceSlot2_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 1, 1, 14),
    _AcEventMgrControlRedirectTraceSlot2_Type()
)
acEventMgrControlRedirectTraceSlot2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEventMgrControlRedirectTraceSlot2.setStatus("current")
_AcEventMgrAgentTable_Object = MibTable
acEventMgrAgentTable = _AcEventMgrAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 2)
)
if mibBuilder.loadTexts:
    acEventMgrAgentTable.setStatus("current")
_AcEventMgrAgentEntry_Object = MibTableRow
acEventMgrAgentEntry = _AcEventMgrAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 2, 1)
)
acEventMgrAgentEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acEventMgrAgentNodeId"),
    (0, "APPIAN-SYSTEM-MIB", "acEventMgrAgentSlot"),
    (0, "APPIAN-SYSTEM-MIB", "acEventMgrAgentId"),
)
if mibBuilder.loadTexts:
    acEventMgrAgentEntry.setStatus("current")
_AcEventMgrAgentNodeId_Type = AcNodeId
_AcEventMgrAgentNodeId_Object = MibTableColumn
acEventMgrAgentNodeId = _AcEventMgrAgentNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 2, 1, 1),
    _AcEventMgrAgentNodeId_Type()
)
acEventMgrAgentNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acEventMgrAgentNodeId.setStatus("current")


class _AcEventMgrAgentId_Type(Integer32):
    """Custom type acEventMgrAgentId based on Integer32"""
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
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48)
        )
    )
    namedValues = NamedValues(
        *(("almmgr", 8),
          ("appiandcc", 28),
          ("asrt", 20),
          ("bpm", 23),
          ("cfgmgr", 7),
          ("clisvc", 9),
          ("clkdrv", 41),
          ("common", 2),
          ("ds1Tdm", 14),
          ("ds3Net", 16),
          ("ds3Tdm", 15),
          ("enetIME", 13),
          ("enetaccess", 11),
          ("enetagg", 44),
          ("eventmgr", 45),
          ("excep", 29),
          ("fr", 21),
          ("fwdmgr", 4),
          ("hdlc", 38),
          ("iasmgr", 5),
          ("kernel", 1),
          ("loader", 48),
          ("lpta", 31),
          ("mach", 43),
          ("mgmtapi", 30),
          ("mgmtrem", 46),
          ("mlc", 37),
          ("modmgr", 39),
          ("msgsvc", 3),
          ("oc3Net", 17),
          ("plc", 42),
          ("ppp", 18),
          ("qos", 35),
          ("rdp", 47),
          ("scmctrl", 32),
          ("scpplt", 40),
          ("serial", 26),
          ("service", 36),
          ("snmp", 24),
          ("sntp", 22),
          ("sonet", 33),
          ("statsmgr", 27),
          ("system", 12),
          ("telnet", 25),
          ("temux", 34),
          ("tl1svc", 10),
          ("tlsmgr", 6),
          ("tta", 19))
    )


_AcEventMgrAgentId_Type.__name__ = "Integer32"
_AcEventMgrAgentId_Object = MibTableColumn
acEventMgrAgentId = _AcEventMgrAgentId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 2, 1, 2),
    _AcEventMgrAgentId_Type()
)
acEventMgrAgentId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acEventMgrAgentId.setStatus("current")


class _AcEventMgrAgentName_Type(DisplayString):
    """Custom type acEventMgrAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AcEventMgrAgentName_Type.__name__ = "DisplayString"
_AcEventMgrAgentName_Object = MibTableColumn
acEventMgrAgentName = _AcEventMgrAgentName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 2, 1, 3),
    _AcEventMgrAgentName_Type()
)
acEventMgrAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEventMgrAgentName.setStatus("current")


class _AcEventMgrAgentAdminStatus_Type(AcAdminStatus):
    """Custom type acEventMgrAgentAdminStatus based on AcAdminStatus"""


_AcEventMgrAgentAdminStatus_Object = MibTableColumn
acEventMgrAgentAdminStatus = _AcEventMgrAgentAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 2, 1, 4),
    _AcEventMgrAgentAdminStatus_Type()
)
acEventMgrAgentAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEventMgrAgentAdminStatus.setStatus("deprecated")


class _AcEventMgrAgentLogLevel_Type(Integer32):
    """Custom type acEventMgrAgentLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_AcEventMgrAgentLogLevel_Type.__name__ = "Integer32"
_AcEventMgrAgentLogLevel_Object = MibTableColumn
acEventMgrAgentLogLevel = _AcEventMgrAgentLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 2, 1, 5),
    _AcEventMgrAgentLogLevel_Type()
)
acEventMgrAgentLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEventMgrAgentLogLevel.setStatus("current")
_AcEventMgrAgentNumberEvents_Type = Integer32
_AcEventMgrAgentNumberEvents_Object = MibTableColumn
acEventMgrAgentNumberEvents = _AcEventMgrAgentNumberEvents_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 2, 1, 6),
    _AcEventMgrAgentNumberEvents_Type()
)
acEventMgrAgentNumberEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEventMgrAgentNumberEvents.setStatus("deprecated")
_AcEventMgrAgentLastEventCode_Type = Integer32
_AcEventMgrAgentLastEventCode_Object = MibTableColumn
acEventMgrAgentLastEventCode = _AcEventMgrAgentLastEventCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 2, 1, 7),
    _AcEventMgrAgentLastEventCode_Type()
)
acEventMgrAgentLastEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEventMgrAgentLastEventCode.setStatus("deprecated")
_AcEventMgrAgentLastEventCount_Type = Integer32
_AcEventMgrAgentLastEventCount_Object = MibTableColumn
acEventMgrAgentLastEventCount = _AcEventMgrAgentLastEventCount_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 2, 1, 8),
    _AcEventMgrAgentLastEventCount_Type()
)
acEventMgrAgentLastEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEventMgrAgentLastEventCount.setStatus("deprecated")


class _AcEventMgrAgentSlot_Type(Integer32):
    """Custom type acEventMgrAgentSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcEventMgrAgentSlot_Type.__name__ = "Integer32"
_AcEventMgrAgentSlot_Object = MibTableColumn
acEventMgrAgentSlot = _AcEventMgrAgentSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 2, 1, 9),
    _AcEventMgrAgentSlot_Type()
)
acEventMgrAgentSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acEventMgrAgentSlot.setStatus("current")


class _AcEventMgrAgentTraceLevel_Type(Integer32):
    """Custom type acEventMgrAgentTraceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_AcEventMgrAgentTraceLevel_Type.__name__ = "Integer32"
_AcEventMgrAgentTraceLevel_Object = MibTableColumn
acEventMgrAgentTraceLevel = _AcEventMgrAgentTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 2, 1, 10),
    _AcEventMgrAgentTraceLevel_Type()
)
acEventMgrAgentTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEventMgrAgentTraceLevel.setStatus("current")
_AcConfigMgr_ObjectIdentity = ObjectIdentity
acConfigMgr = _AcConfigMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4)
)
_AcConfigMgrTraps_ObjectIdentity = ObjectIdentity
acConfigMgrTraps = _AcConfigMgrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4, 0)
)
_AcConfigMgrTable_Object = MibTable
acConfigMgrTable = _AcConfigMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4, 1)
)
if mibBuilder.loadTexts:
    acConfigMgrTable.setStatus("current")
_AcConfigMgrEntry_Object = MibTableRow
acConfigMgrEntry = _AcConfigMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4, 1, 1)
)
acConfigMgrEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acConfigMgrNodeId"),
)
if mibBuilder.loadTexts:
    acConfigMgrEntry.setStatus("current")
_AcConfigMgrNodeId_Type = AcNodeId
_AcConfigMgrNodeId_Object = MibTableColumn
acConfigMgrNodeId = _AcConfigMgrNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4, 1, 1, 1),
    _AcConfigMgrNodeId_Type()
)
acConfigMgrNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acConfigMgrNodeId.setStatus("current")


class _AcConfigMgrAdminStatus_Type(AcAdminStatus):
    """Custom type acConfigMgrAdminStatus based on AcAdminStatus"""


_AcConfigMgrAdminStatus_Object = MibTableColumn
acConfigMgrAdminStatus = _AcConfigMgrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4, 1, 1, 2),
    _AcConfigMgrAdminStatus_Type()
)
acConfigMgrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acConfigMgrAdminStatus.setStatus("current")
_AcConfigMgrCurrentRevision_Type = Integer32
_AcConfigMgrCurrentRevision_Object = MibTableColumn
acConfigMgrCurrentRevision = _AcConfigMgrCurrentRevision_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4, 1, 1, 3),
    _AcConfigMgrCurrentRevision_Type()
)
acConfigMgrCurrentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acConfigMgrCurrentRevision.setStatus("current")


class _AcConfigMgrFileName_Type(DisplayString):
    """Custom type acConfigMgrFileName based on DisplayString"""
    defaultValue = OctetString("config.dat")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcConfigMgrFileName_Type.__name__ = "DisplayString"
_AcConfigMgrFileName_Object = MibTableColumn
acConfigMgrFileName = _AcConfigMgrFileName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4, 1, 1, 4),
    _AcConfigMgrFileName_Type()
)
acConfigMgrFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acConfigMgrFileName.setStatus("current")


class _AcConfigMgrAutoSaveInterval_Type(Integer32):
    """Custom type acConfigMgrAutoSaveInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_AcConfigMgrAutoSaveInterval_Type.__name__ = "Integer32"
_AcConfigMgrAutoSaveInterval_Object = MibTableColumn
acConfigMgrAutoSaveInterval = _AcConfigMgrAutoSaveInterval_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4, 1, 1, 5),
    _AcConfigMgrAutoSaveInterval_Type()
)
acConfigMgrAutoSaveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acConfigMgrAutoSaveInterval.setStatus("current")


class _AcConfigMgrAutoSaveEnable_Type(TruthValue):
    """Custom type acConfigMgrAutoSaveEnable based on TruthValue"""


_AcConfigMgrAutoSaveEnable_Object = MibTableColumn
acConfigMgrAutoSaveEnable = _AcConfigMgrAutoSaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4, 1, 1, 6),
    _AcConfigMgrAutoSaveEnable_Type()
)
acConfigMgrAutoSaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acConfigMgrAutoSaveEnable.setStatus("current")
_AcConfigMgrLastWritten_Type = DateAndTime
_AcConfigMgrLastWritten_Object = MibTableColumn
acConfigMgrLastWritten = _AcConfigMgrLastWritten_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4, 1, 1, 7),
    _AcConfigMgrLastWritten_Type()
)
acConfigMgrLastWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acConfigMgrLastWritten.setStatus("current")


class _AcConfigMgrSaveConfig_Type(TruthValue):
    """Custom type acConfigMgrSaveConfig based on TruthValue"""


_AcConfigMgrSaveConfig_Object = MibTableColumn
acConfigMgrSaveConfig = _AcConfigMgrSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4, 1, 1, 8),
    _AcConfigMgrSaveConfig_Type()
)
acConfigMgrSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acConfigMgrSaveConfig.setStatus("current")


class _AcConfigMgrOpStatus_Type(Integer32):
    """Custom type acConfigMgrOpStatus based on Integer32"""
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
        *(("failed", 2),
          ("succeeded", 1),
          ("writing", 3))
    )


_AcConfigMgrOpStatus_Type.__name__ = "Integer32"
_AcConfigMgrOpStatus_Object = MibTableColumn
acConfigMgrOpStatus = _AcConfigMgrOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4, 1, 1, 9),
    _AcConfigMgrOpStatus_Type()
)
acConfigMgrOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acConfigMgrOpStatus.setStatus("current")
_AcSntpMgr_ObjectIdentity = ObjectIdentity
acSntpMgr = _AcSntpMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7)
)
_AcSntpMgrTraps_ObjectIdentity = ObjectIdentity
acSntpMgrTraps = _AcSntpMgrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 0)
)
_AcSntpMgrTable_Object = MibTable
acSntpMgrTable = _AcSntpMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1)
)
if mibBuilder.loadTexts:
    acSntpMgrTable.setStatus("current")
_AcSntpMgrEntry_Object = MibTableRow
acSntpMgrEntry = _AcSntpMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1, 1)
)
acSntpMgrEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acSntpMgrNodeId"),
)
if mibBuilder.loadTexts:
    acSntpMgrEntry.setStatus("current")
_AcSntpMgrNodeId_Type = AcNodeId
_AcSntpMgrNodeId_Object = MibTableColumn
acSntpMgrNodeId = _AcSntpMgrNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1, 1, 1),
    _AcSntpMgrNodeId_Type()
)
acSntpMgrNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acSntpMgrNodeId.setStatus("current")
_AcSntpMgrAdminStatus_Type = AcAdminStatus
_AcSntpMgrAdminStatus_Object = MibTableColumn
acSntpMgrAdminStatus = _AcSntpMgrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1, 1, 2),
    _AcSntpMgrAdminStatus_Type()
)
acSntpMgrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSntpMgrAdminStatus.setStatus("current")
_AcSntpMgrOpStatus_Type = AcOpStatus
_AcSntpMgrOpStatus_Object = MibTableColumn
acSntpMgrOpStatus = _AcSntpMgrOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1, 1, 3),
    _AcSntpMgrOpStatus_Type()
)
acSntpMgrOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSntpMgrOpStatus.setStatus("current")
_AcSntpMgrErrorCode_Type = Integer32
_AcSntpMgrErrorCode_Object = MibTableColumn
acSntpMgrErrorCode = _AcSntpMgrErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1, 1, 4),
    _AcSntpMgrErrorCode_Type()
)
acSntpMgrErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSntpMgrErrorCode.setStatus("current")
_AcSntpMgrPeerIpAddress_Type = IpAddress
_AcSntpMgrPeerIpAddress_Object = MibTableColumn
acSntpMgrPeerIpAddress = _AcSntpMgrPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1, 1, 5),
    _AcSntpMgrPeerIpAddress_Type()
)
acSntpMgrPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSntpMgrPeerIpAddress.setStatus("current")


class _AcSntpMgrQueryInterval_Type(Integer32):
    """Custom type acSntpMgrQueryInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_AcSntpMgrQueryInterval_Type.__name__ = "Integer32"
_AcSntpMgrQueryInterval_Object = MibTableColumn
acSntpMgrQueryInterval = _AcSntpMgrQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1, 1, 6),
    _AcSntpMgrQueryInterval_Type()
)
acSntpMgrQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSntpMgrQueryInterval.setStatus("current")


class _AcSntpMgrRetryCount_Type(Integer32):
    """Custom type acSntpMgrRetryCount based on Integer32"""
    defaultValue = 3


_AcSntpMgrRetryCount_Object = MibTableColumn
acSntpMgrRetryCount = _AcSntpMgrRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1, 1, 7),
    _AcSntpMgrRetryCount_Type()
)
acSntpMgrRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSntpMgrRetryCount.setStatus("current")


class _AcSntpMgrMaxVariance_Type(Integer32):
    """Custom type acSntpMgrMaxVariance based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200000),
    )


_AcSntpMgrMaxVariance_Type.__name__ = "Integer32"
_AcSntpMgrMaxVariance_Object = MibTableColumn
acSntpMgrMaxVariance = _AcSntpMgrMaxVariance_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1, 1, 8),
    _AcSntpMgrMaxVariance_Type()
)
acSntpMgrMaxVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSntpMgrMaxVariance.setStatus("current")
_AcSntpMgrVariance_Type = Integer32
_AcSntpMgrVariance_Object = MibTableColumn
acSntpMgrVariance = _AcSntpMgrVariance_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1, 1, 9),
    _AcSntpMgrVariance_Type()
)
acSntpMgrVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSntpMgrVariance.setStatus("current")


class _AcSntpMgrVarianceDetectEnable_Type(TruthValue):
    """Custom type acSntpMgrVarianceDetectEnable based on TruthValue"""


_AcSntpMgrVarianceDetectEnable_Object = MibTableColumn
acSntpMgrVarianceDetectEnable = _AcSntpMgrVarianceDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1, 1, 10),
    _AcSntpMgrVarianceDetectEnable_Type()
)
acSntpMgrVarianceDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSntpMgrVarianceDetectEnable.setStatus("current")


class _AcSntpMgrTimeZone_Type(Integer32):
    """Custom type acSntpMgrTimeZone based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AcSntpMgrTimeZone_Type.__name__ = "Integer32"
_AcSntpMgrTimeZone_Object = MibTableColumn
acSntpMgrTimeZone = _AcSntpMgrTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1, 1, 11),
    _AcSntpMgrTimeZone_Type()
)
acSntpMgrTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSntpMgrTimeZone.setStatus("current")


class _AcSntpMgrDayLightSaving_Type(TruthValue):
    """Custom type acSntpMgrDayLightSaving based on TruthValue"""


_AcSntpMgrDayLightSaving_Object = MibTableColumn
acSntpMgrDayLightSaving = _AcSntpMgrDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 1, 1, 12),
    _AcSntpMgrDayLightSaving_Type()
)
acSntpMgrDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSntpMgrDayLightSaving.setStatus("current")
_AcAuthMgr_ObjectIdentity = ObjectIdentity
acAuthMgr = _AcAuthMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8)
)
_AcAuthMgrTraps_ObjectIdentity = ObjectIdentity
acAuthMgrTraps = _AcAuthMgrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 0)
)
_AcAuthMgrTable_Object = MibTable
acAuthMgrTable = _AcAuthMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 1)
)
if mibBuilder.loadTexts:
    acAuthMgrTable.setStatus("current")
_AcAuthMgrEntry_Object = MibTableRow
acAuthMgrEntry = _AcAuthMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 1, 1)
)
acAuthMgrEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acAuthMgrNodeId"),
    (0, "APPIAN-SYSTEM-MIB", "acAuthMgrUserId"),
)
if mibBuilder.loadTexts:
    acAuthMgrEntry.setStatus("current")
_AcAuthMgrNodeId_Type = AcNodeId
_AcAuthMgrNodeId_Object = MibTableColumn
acAuthMgrNodeId = _AcAuthMgrNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 1, 1, 1),
    _AcAuthMgrNodeId_Type()
)
acAuthMgrNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acAuthMgrNodeId.setStatus("current")
_AcAuthMgrUserId_Type = Integer32
_AcAuthMgrUserId_Object = MibTableColumn
acAuthMgrUserId = _AcAuthMgrUserId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 1, 1, 2),
    _AcAuthMgrUserId_Type()
)
acAuthMgrUserId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acAuthMgrUserId.setStatus("current")


class _AcAuthMgrUserName_Type(DisplayString):
    """Custom type acAuthMgrUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_AcAuthMgrUserName_Type.__name__ = "DisplayString"
_AcAuthMgrUserName_Object = MibTableColumn
acAuthMgrUserName = _AcAuthMgrUserName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 1, 1, 3),
    _AcAuthMgrUserName_Type()
)
acAuthMgrUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAuthMgrUserName.setStatus("current")


class _AcAuthMgrAccessMode_Type(Integer32):
    """Custom type acAuthMgrAccessMode based on Integer32"""
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
        *(("ftp", 4),
          ("rlogin", 3),
          ("serial", 1),
          ("telnet", 2),
          ("unknown", 0))
    )


_AcAuthMgrAccessMode_Type.__name__ = "Integer32"
_AcAuthMgrAccessMode_Object = MibTableColumn
acAuthMgrAccessMode = _AcAuthMgrAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 1, 1, 4),
    _AcAuthMgrAccessMode_Type()
)
acAuthMgrAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAuthMgrAccessMode.setStatus("current")
_AcAuthMgrLogonTime_Type = DateAndTime
_AcAuthMgrLogonTime_Object = MibTableColumn
acAuthMgrLogonTime = _AcAuthMgrLogonTime_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 1, 1, 5),
    _AcAuthMgrLogonTime_Type()
)
acAuthMgrLogonTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAuthMgrLogonTime.setStatus("current")
_AcAuthMgrFailures_Type = Integer32
_AcAuthMgrFailures_Object = MibTableColumn
acAuthMgrFailures = _AcAuthMgrFailures_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 1, 1, 6),
    _AcAuthMgrFailures_Type()
)
acAuthMgrFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAuthMgrFailures.setStatus("current")
_AcAuthMgrLockOut_Type = TruthValue
_AcAuthMgrLockOut_Object = MibTableColumn
acAuthMgrLockOut = _AcAuthMgrLockOut_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 1, 1, 7),
    _AcAuthMgrLockOut_Type()
)
acAuthMgrLockOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAuthMgrLockOut.setStatus("current")
_AcAuthMgrDeleteEntry_Type = TruthValue
_AcAuthMgrDeleteEntry_Object = MibTableColumn
acAuthMgrDeleteEntry = _AcAuthMgrDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 1, 1, 8),
    _AcAuthMgrDeleteEntry_Type()
)
acAuthMgrDeleteEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAuthMgrDeleteEntry.setStatus("current")
_AcTrapMgr_ObjectIdentity = ObjectIdentity
acTrapMgr = _AcTrapMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9)
)
_AcTrapMgrDestAddrTable_Object = MibTable
acTrapMgrDestAddrTable = _AcTrapMgrDestAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 1)
)
if mibBuilder.loadTexts:
    acTrapMgrDestAddrTable.setStatus("current")
_AcTrapMgrDestAddrEntry_Object = MibTableRow
acTrapMgrDestAddrEntry = _AcTrapMgrDestAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 1, 1)
)
acTrapMgrDestAddrEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acTrapMgrDestAddrNodeId"),
    (0, "APPIAN-SYSTEM-MIB", "acTrapMgrDestAddrCommId"),
    (0, "APPIAN-SYSTEM-MIB", "acTrapMgrDestAddrIpAddress"),
)
if mibBuilder.loadTexts:
    acTrapMgrDestAddrEntry.setStatus("current")
_AcTrapMgrDestAddrNodeId_Type = AcNodeId
_AcTrapMgrDestAddrNodeId_Object = MibTableColumn
acTrapMgrDestAddrNodeId = _AcTrapMgrDestAddrNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 1, 1, 1),
    _AcTrapMgrDestAddrNodeId_Type()
)
acTrapMgrDestAddrNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTrapMgrDestAddrNodeId.setStatus("current")
_AcTrapMgrDestAddrCommId_Type = Integer32
_AcTrapMgrDestAddrCommId_Object = MibTableColumn
acTrapMgrDestAddrCommId = _AcTrapMgrDestAddrCommId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 1, 1, 2),
    _AcTrapMgrDestAddrCommId_Type()
)
acTrapMgrDestAddrCommId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTrapMgrDestAddrCommId.setStatus("current")
_AcTrapMgrDestAddrIpAddress_Type = IpAddress
_AcTrapMgrDestAddrIpAddress_Object = MibTableColumn
acTrapMgrDestAddrIpAddress = _AcTrapMgrDestAddrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 1, 1, 3),
    _AcTrapMgrDestAddrIpAddress_Type()
)
acTrapMgrDestAddrIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTrapMgrDestAddrIpAddress.setStatus("current")
_AcTrapMgrDestAddrAdminStatus_Type = AcAdminStatus
_AcTrapMgrDestAddrAdminStatus_Object = MibTableColumn
acTrapMgrDestAddrAdminStatus = _AcTrapMgrDestAddrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 1, 1, 4),
    _AcTrapMgrDestAddrAdminStatus_Type()
)
acTrapMgrDestAddrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTrapMgrDestAddrAdminStatus.setStatus("current")
_AcTrapMgrFilterTable_Object = MibTable
acTrapMgrFilterTable = _AcTrapMgrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 2)
)
if mibBuilder.loadTexts:
    acTrapMgrFilterTable.setStatus("current")
_AcTrapMgrFilterEntry_Object = MibTableRow
acTrapMgrFilterEntry = _AcTrapMgrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 2, 1)
)
acTrapMgrFilterEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acTrapMgrFilterNodeId"),
    (0, "APPIAN-SYSTEM-MIB", "acTrapMgrFilterCommId"),
    (0, "APPIAN-SYSTEM-MIB", "acTrapMgrFilterId"),
)
if mibBuilder.loadTexts:
    acTrapMgrFilterEntry.setStatus("current")
_AcTrapMgrFilterNodeId_Type = AcNodeId
_AcTrapMgrFilterNodeId_Object = MibTableColumn
acTrapMgrFilterNodeId = _AcTrapMgrFilterNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 2, 1, 1),
    _AcTrapMgrFilterNodeId_Type()
)
acTrapMgrFilterNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTrapMgrFilterNodeId.setStatus("current")
_AcTrapMgrFilterCommId_Type = Integer32
_AcTrapMgrFilterCommId_Object = MibTableColumn
acTrapMgrFilterCommId = _AcTrapMgrFilterCommId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 2, 1, 2),
    _AcTrapMgrFilterCommId_Type()
)
acTrapMgrFilterCommId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTrapMgrFilterCommId.setStatus("current")
_AcTrapMgrFilterId_Type = Integer32
_AcTrapMgrFilterId_Object = MibTableColumn
acTrapMgrFilterId = _AcTrapMgrFilterId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 2, 1, 3),
    _AcTrapMgrFilterId_Type()
)
acTrapMgrFilterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTrapMgrFilterId.setStatus("current")
_AcTrapMgrFilterAdminStatus_Type = AcAdminStatus
_AcTrapMgrFilterAdminStatus_Object = MibTableColumn
acTrapMgrFilterAdminStatus = _AcTrapMgrFilterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 2, 1, 4),
    _AcTrapMgrFilterAdminStatus_Type()
)
acTrapMgrFilterAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTrapMgrFilterAdminStatus.setStatus("current")
_AcTrapMgrFilterTrapOid_Type = ObjectIdentifier
_AcTrapMgrFilterTrapOid_Object = MibTableColumn
acTrapMgrFilterTrapOid = _AcTrapMgrFilterTrapOid_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 2, 1, 5),
    _AcTrapMgrFilterTrapOid_Type()
)
acTrapMgrFilterTrapOid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acTrapMgrFilterTrapOid.setStatus("current")
_AcTrapMgrResendTable_Object = MibTable
acTrapMgrResendTable = _AcTrapMgrResendTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 3)
)
if mibBuilder.loadTexts:
    acTrapMgrResendTable.setStatus("current")
_AcTrapMgrResendEntry_Object = MibTableRow
acTrapMgrResendEntry = _AcTrapMgrResendEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 3, 1)
)
acTrapMgrResendEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acTrapMgrResendNodeId"),
)
if mibBuilder.loadTexts:
    acTrapMgrResendEntry.setStatus("current")
_AcTrapMgrResendNodeId_Type = AcNodeId
_AcTrapMgrResendNodeId_Object = MibTableColumn
acTrapMgrResendNodeId = _AcTrapMgrResendNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 3, 1, 1),
    _AcTrapMgrResendNodeId_Type()
)
acTrapMgrResendNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acTrapMgrResendNodeId.setStatus("current")
_AcTrapMgrResendAdminStatus_Type = AcAdminStatus
_AcTrapMgrResendAdminStatus_Object = MibTableColumn
acTrapMgrResendAdminStatus = _AcTrapMgrResendAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 3, 1, 2),
    _AcTrapMgrResendAdminStatus_Type()
)
acTrapMgrResendAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrapMgrResendAdminStatus.setStatus("current")
_AcTrapMgrResendFromSeqId_Type = Integer32
_AcTrapMgrResendFromSeqId_Object = MibTableColumn
acTrapMgrResendFromSeqId = _AcTrapMgrResendFromSeqId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 3, 1, 3),
    _AcTrapMgrResendFromSeqId_Type()
)
acTrapMgrResendFromSeqId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrapMgrResendFromSeqId.setStatus("current")
_AcTrapMgrResendToSeqId_Type = Integer32
_AcTrapMgrResendToSeqId_Object = MibTableColumn
acTrapMgrResendToSeqId = _AcTrapMgrResendToSeqId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 9, 3, 1, 4),
    _AcTrapMgrResendToSeqId_Type()
)
acTrapMgrResendToSeqId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrapMgrResendToSeqId.setStatus("current")
_AcFileXferMgr_ObjectIdentity = ObjectIdentity
acFileXferMgr = _AcFileXferMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10)
)
_AcFileXferMgrTraps_ObjectIdentity = ObjectIdentity
acFileXferMgrTraps = _AcFileXferMgrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 0)
)
_AcFileXferMgrTable_Object = MibTable
acFileXferMgrTable = _AcFileXferMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1)
)
if mibBuilder.loadTexts:
    acFileXferMgrTable.setStatus("current")
_AcFileXferMgrEntry_Object = MibTableRow
acFileXferMgrEntry = _AcFileXferMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1)
)
acFileXferMgrEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acFileXferMgrNodeId"),
    (0, "APPIAN-SYSTEM-MIB", "acFileXferMgrRowId"),
)
if mibBuilder.loadTexts:
    acFileXferMgrEntry.setStatus("current")
_AcFileXferMgrNodeId_Type = AcNodeId
_AcFileXferMgrNodeId_Object = MibTableColumn
acFileXferMgrNodeId = _AcFileXferMgrNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 1),
    _AcFileXferMgrNodeId_Type()
)
acFileXferMgrNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acFileXferMgrNodeId.setStatus("current")


class _AcFileXferMgrRowId_Type(Integer32):
    """Custom type acFileXferMgrRowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AcFileXferMgrRowId_Type.__name__ = "Integer32"
_AcFileXferMgrRowId_Object = MibTableColumn
acFileXferMgrRowId = _AcFileXferMgrRowId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 2),
    _AcFileXferMgrRowId_Type()
)
acFileXferMgrRowId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acFileXferMgrRowId.setStatus("current")


class _AcFileXferMgrAdminStatus_Type(AcAdminStatus):
    """Custom type acFileXferMgrAdminStatus based on AcAdminStatus"""


_AcFileXferMgrAdminStatus_Object = MibTableColumn
acFileXferMgrAdminStatus = _AcFileXferMgrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 3),
    _AcFileXferMgrAdminStatus_Type()
)
acFileXferMgrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFileXferMgrAdminStatus.setStatus("current")


class _AcFileXferMgrOperation_Type(Integer32):
    """Custom type acFileXferMgrOperation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("upload", 1))
    )


_AcFileXferMgrOperation_Type.__name__ = "Integer32"
_AcFileXferMgrOperation_Object = MibTableColumn
acFileXferMgrOperation = _AcFileXferMgrOperation_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 4),
    _AcFileXferMgrOperation_Type()
)
acFileXferMgrOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFileXferMgrOperation.setStatus("current")


class _AcFileXferMgrFiletype_Type(Integer32):
    """Custom type acFileXferMgrFiletype based on Integer32"""
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
        *(("config", 3),
          ("eventlog", 2),
          ("generic", 4),
          ("image", 1))
    )


_AcFileXferMgrFiletype_Type.__name__ = "Integer32"
_AcFileXferMgrFiletype_Object = MibTableColumn
acFileXferMgrFiletype = _AcFileXferMgrFiletype_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 5),
    _AcFileXferMgrFiletype_Type()
)
acFileXferMgrFiletype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFileXferMgrFiletype.setStatus("current")


class _AcFileXferMgrFilesubtype_Type(Integer32):
    """Custom type acFileXferMgrFilesubtype based on Integer32"""
    defaultValue = 1

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
        *(("namedbootimage", 2),
          ("none", 5),
          ("primaryimage", 1),
          ("regularlog", 3),
          ("securitylog", 4))
    )


_AcFileXferMgrFilesubtype_Type.__name__ = "Integer32"
_AcFileXferMgrFilesubtype_Object = MibTableColumn
acFileXferMgrFilesubtype = _AcFileXferMgrFilesubtype_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 6),
    _AcFileXferMgrFilesubtype_Type()
)
acFileXferMgrFilesubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFileXferMgrFilesubtype.setStatus("current")
_AcFileXferMgrFtpServerIpAddress_Type = IpAddress
_AcFileXferMgrFtpServerIpAddress_Object = MibTableColumn
acFileXferMgrFtpServerIpAddress = _AcFileXferMgrFtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 7),
    _AcFileXferMgrFtpServerIpAddress_Type()
)
acFileXferMgrFtpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFileXferMgrFtpServerIpAddress.setStatus("current")


class _AcFileXferMgrUsername_Type(DisplayString):
    """Custom type acFileXferMgrUsername based on DisplayString"""
    defaultValue = OctetString("anonymous")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcFileXferMgrUsername_Type.__name__ = "DisplayString"
_AcFileXferMgrUsername_Object = MibTableColumn
acFileXferMgrUsername = _AcFileXferMgrUsername_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 8),
    _AcFileXferMgrUsername_Type()
)
acFileXferMgrUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFileXferMgrUsername.setStatus("current")


class _AcFileXferMgrPassword_Type(DisplayString):
    """Custom type acFileXferMgrPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcFileXferMgrPassword_Type.__name__ = "DisplayString"
_AcFileXferMgrPassword_Object = MibTableColumn
acFileXferMgrPassword = _AcFileXferMgrPassword_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 9),
    _AcFileXferMgrPassword_Type()
)
acFileXferMgrPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFileXferMgrPassword.setStatus("current")


class _AcFileXferMgrSourceDirectory_Type(DisplayString):
    """Custom type acFileXferMgrSourceDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcFileXferMgrSourceDirectory_Type.__name__ = "DisplayString"
_AcFileXferMgrSourceDirectory_Object = MibTableColumn
acFileXferMgrSourceDirectory = _AcFileXferMgrSourceDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 10),
    _AcFileXferMgrSourceDirectory_Type()
)
acFileXferMgrSourceDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFileXferMgrSourceDirectory.setStatus("current")


class _AcFileXferMgrSourceFilename_Type(DisplayString):
    """Custom type acFileXferMgrSourceFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcFileXferMgrSourceFilename_Type.__name__ = "DisplayString"
_AcFileXferMgrSourceFilename_Object = MibTableColumn
acFileXferMgrSourceFilename = _AcFileXferMgrSourceFilename_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 11),
    _AcFileXferMgrSourceFilename_Type()
)
acFileXferMgrSourceFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFileXferMgrSourceFilename.setStatus("current")


class _AcFileXferMgrDestDirectory_Type(DisplayString):
    """Custom type acFileXferMgrDestDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcFileXferMgrDestDirectory_Type.__name__ = "DisplayString"
_AcFileXferMgrDestDirectory_Object = MibTableColumn
acFileXferMgrDestDirectory = _AcFileXferMgrDestDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 12),
    _AcFileXferMgrDestDirectory_Type()
)
acFileXferMgrDestDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFileXferMgrDestDirectory.setStatus("current")


class _AcFileXferMgrDestFilename_Type(DisplayString):
    """Custom type acFileXferMgrDestFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcFileXferMgrDestFilename_Type.__name__ = "DisplayString"
_AcFileXferMgrDestFilename_Object = MibTableColumn
acFileXferMgrDestFilename = _AcFileXferMgrDestFilename_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 13),
    _AcFileXferMgrDestFilename_Type()
)
acFileXferMgrDestFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFileXferMgrDestFilename.setStatus("current")


class _AcFileXferMgrXferMode_Type(Integer32):
    """Custom type acFileXferMgrXferMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2))
    )


_AcFileXferMgrXferMode_Type.__name__ = "Integer32"
_AcFileXferMgrXferMode_Object = MibTableColumn
acFileXferMgrXferMode = _AcFileXferMgrXferMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 14),
    _AcFileXferMgrXferMode_Type()
)
acFileXferMgrXferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFileXferMgrXferMode.setStatus("current")


class _AcFileXferMgrOpStatus_Type(Integer32):
    """Custom type acFileXferMgrOpStatus based on Integer32"""
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
        *(("failed", 2),
          ("inprogress", 3),
          ("succeeded", 1))
    )


_AcFileXferMgrOpStatus_Type.__name__ = "Integer32"
_AcFileXferMgrOpStatus_Object = MibTableColumn
acFileXferMgrOpStatus = _AcFileXferMgrOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 1, 1, 15),
    _AcFileXferMgrOpStatus_Type()
)
acFileXferMgrOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFileXferMgrOpStatus.setStatus("current")
_AcRdpMgr_ObjectIdentity = ObjectIdentity
acRdpMgr = _AcRdpMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11)
)
_AcRdpMgrTraps_ObjectIdentity = ObjectIdentity
acRdpMgrTraps = _AcRdpMgrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 0)
)
_AcRdpMgrTable_Object = MibTable
acRdpMgrTable = _AcRdpMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 1)
)
if mibBuilder.loadTexts:
    acRdpMgrTable.setStatus("current")
_AcRdpMgrEntry_Object = MibTableRow
acRdpMgrEntry = _AcRdpMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 1, 1)
)
acRdpMgrEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acRdpMgrNodeId"),
)
if mibBuilder.loadTexts:
    acRdpMgrEntry.setStatus("current")
_AcRdpMgrNodeId_Type = AcNodeId
_AcRdpMgrNodeId_Object = MibTableColumn
acRdpMgrNodeId = _AcRdpMgrNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 1, 1, 1),
    _AcRdpMgrNodeId_Type()
)
acRdpMgrNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acRdpMgrNodeId.setStatus("current")


class _AcRdpMgrFsmState_Type(Integer32):
    """Custom type acRdpMgrFsmState based on Integer32"""
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
        *(("discovery", 1),
          ("isolated", 0),
          ("master", 2),
          ("pleb", 3))
    )


_AcRdpMgrFsmState_Type.__name__ = "Integer32"
_AcRdpMgrFsmState_Object = MibTableColumn
acRdpMgrFsmState = _AcRdpMgrFsmState_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 1, 1, 2),
    _AcRdpMgrFsmState_Type()
)
acRdpMgrFsmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acRdpMgrFsmState.setStatus("current")
_AcRdpMgrRingMasterNodeMac_Type = MacAddress
_AcRdpMgrRingMasterNodeMac_Object = MibTableColumn
acRdpMgrRingMasterNodeMac = _AcRdpMgrRingMasterNodeMac_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 1, 1, 3),
    _AcRdpMgrRingMasterNodeMac_Type()
)
acRdpMgrRingMasterNodeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acRdpMgrRingMasterNodeMac.setStatus("current")


class _AcRdpMgrRingTopology_Type(Integer32):
    """Custom type acRdpMgrRingTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1),
          ("unknown", 0))
    )


_AcRdpMgrRingTopology_Type.__name__ = "Integer32"
_AcRdpMgrRingTopology_Object = MibTableColumn
acRdpMgrRingTopology = _AcRdpMgrRingTopology_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 1, 1, 4),
    _AcRdpMgrRingTopology_Type()
)
acRdpMgrRingTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acRdpMgrRingTopology.setStatus("current")


class _AcRdpMgrRingState_Type(Integer32):
    """Custom type acRdpMgrRingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complete", 1),
          ("incomplete", 2),
          ("unknown", 0))
    )


_AcRdpMgrRingState_Type.__name__ = "Integer32"
_AcRdpMgrRingState_Object = MibTableColumn
acRdpMgrRingState = _AcRdpMgrRingState_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 1, 1, 5),
    _AcRdpMgrRingState_Type()
)
acRdpMgrRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acRdpMgrRingState.setStatus("current")
_AcRdpMgrRingSize_Type = Integer32
_AcRdpMgrRingSize_Object = MibTableColumn
acRdpMgrRingSize = _AcRdpMgrRingSize_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 1, 1, 6),
    _AcRdpMgrRingSize_Type()
)
acRdpMgrRingSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acRdpMgrRingSize.setStatus("current")
_AcRdpMgrRdpVersion_Type = Integer32
_AcRdpMgrRdpVersion_Object = MibTableColumn
acRdpMgrRdpVersion = _AcRdpMgrRdpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 1, 1, 7),
    _AcRdpMgrRdpVersion_Type()
)
acRdpMgrRdpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acRdpMgrRdpVersion.setStatus("current")
_AcRdpMgrNodeTable_Object = MibTable
acRdpMgrNodeTable = _AcRdpMgrNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 2)
)
if mibBuilder.loadTexts:
    acRdpMgrNodeTable.setStatus("current")
_AcRdpMgrNodeEntry_Object = MibTableRow
acRdpMgrNodeEntry = _AcRdpMgrNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 2, 1)
)
acRdpMgrNodeEntry.setIndexNames(
    (0, "APPIAN-SYSTEM-MIB", "acRdpMgrNodeNodeId"),
    (0, "APPIAN-SYSTEM-MIB", "acRdpMgrNodeRowId"),
)
if mibBuilder.loadTexts:
    acRdpMgrNodeEntry.setStatus("current")
_AcRdpMgrNodeThisNodeId_Type = AcNodeId
_AcRdpMgrNodeThisNodeId_Object = MibTableColumn
acRdpMgrNodeThisNodeId = _AcRdpMgrNodeThisNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 2, 1, 1),
    _AcRdpMgrNodeThisNodeId_Type()
)
acRdpMgrNodeThisNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acRdpMgrNodeThisNodeId.setStatus("current")
_AcRdpMgrNodeRowId_Type = Integer32
_AcRdpMgrNodeRowId_Object = MibTableColumn
acRdpMgrNodeRowId = _AcRdpMgrNodeRowId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 2, 1, 2),
    _AcRdpMgrNodeRowId_Type()
)
acRdpMgrNodeRowId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acRdpMgrNodeRowId.setStatus("current")
_AcRdpMgrNodeNodeId_Type = AcNodeId
_AcRdpMgrNodeNodeId_Object = MibTableColumn
acRdpMgrNodeNodeId = _AcRdpMgrNodeNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 2, 1, 3),
    _AcRdpMgrNodeNodeId_Type()
)
acRdpMgrNodeNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acRdpMgrNodeNodeId.setStatus("current")
_AcRdpMgrNodeADccIpAddress_Type = IpAddress
_AcRdpMgrNodeADccIpAddress_Object = MibTableColumn
acRdpMgrNodeADccIpAddress = _AcRdpMgrNodeADccIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 2, 1, 4),
    _AcRdpMgrNodeADccIpAddress_Type()
)
acRdpMgrNodeADccIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acRdpMgrNodeADccIpAddress.setStatus("current")
_AcRdpMgrNodeADccMacAddress_Type = MacAddress
_AcRdpMgrNodeADccMacAddress_Object = MibTableColumn
acRdpMgrNodeADccMacAddress = _AcRdpMgrNodeADccMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 2, 1, 5),
    _AcRdpMgrNodeADccMacAddress_Type()
)
acRdpMgrNodeADccMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acRdpMgrNodeADccMacAddress.setStatus("current")


class _AcRdpMgrNodeADccConfig_Type(Integer32):
    """Custom type acRdpMgrNodeADccConfig based on Integer32"""
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
        *(("ese", 2),
          ("esw", 3),
          ("is", 1),
          ("unknown", 0))
    )


_AcRdpMgrNodeADccConfig_Type.__name__ = "Integer32"
_AcRdpMgrNodeADccConfig_Object = MibTableColumn
acRdpMgrNodeADccConfig = _AcRdpMgrNodeADccConfig_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 2, 1, 6),
    _AcRdpMgrNodeADccConfig_Type()
)
acRdpMgrNodeADccConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acRdpMgrNodeADccConfig.setStatus("current")
_AcRdpMgrNodeADccEastOk_Type = TruthValue
_AcRdpMgrNodeADccEastOk_Object = MibTableColumn
acRdpMgrNodeADccEastOk = _AcRdpMgrNodeADccEastOk_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 2, 1, 7),
    _AcRdpMgrNodeADccEastOk_Type()
)
acRdpMgrNodeADccEastOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acRdpMgrNodeADccEastOk.setStatus("current")
_AcRdpMgrNodeADccWestOk_Type = TruthValue
_AcRdpMgrNodeADccWestOk_Object = MibTableColumn
acRdpMgrNodeADccWestOk = _AcRdpMgrNodeADccWestOk_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 2, 1, 8),
    _AcRdpMgrNodeADccWestOk_Type()
)
acRdpMgrNodeADccWestOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acRdpMgrNodeADccWestOk.setStatus("current")
_AcRdpMgrNodeNodeArch_Type = AcNodeArchitecture
_AcRdpMgrNodeNodeArch_Object = MibTableColumn
acRdpMgrNodeNodeArch = _AcRdpMgrNodeNodeArch_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 2, 1, 9),
    _AcRdpMgrNodeNodeArch_Type()
)
acRdpMgrNodeNodeArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acRdpMgrNodeNodeArch.setStatus("current")

# Managed Objects groups


# Notification objects

acEventMgrLogFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 0, 1)
)
acEventMgrLogFullTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acEventMgrControlNodeId"),
        ("APPIAN-SYSTEM-MIB", "acEventMgrControlLogCurrentSize"))
)
if mibBuilder.loadTexts:
    acEventMgrLogFullTrap.setStatus(
        "deprecated"
    )

acEventMgrSecurityLogFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 0, 2)
)
acEventMgrSecurityLogFullTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acEventMgrControlNodeId"),
        ("APPIAN-SYSTEM-MIB", "acEventMgrControlSecurityLogCurrentSize"))
)
if mibBuilder.loadTexts:
    acEventMgrSecurityLogFullTrap.setStatus(
        "deprecated"
    )

acEventMgrLogFileCloseFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 0, 3)
)
acEventMgrLogFileCloseFailedTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acEventMgrControlNodeId"),
        ("APPIAN-SYSTEM-MIB", "acEventMgrControlLogFileName"))
)
if mibBuilder.loadTexts:
    acEventMgrLogFileCloseFailedTrap.setStatus(
        "deprecated"
    )

acEventMgrSecurityLogFileCloseFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 3, 0, 4)
)
acEventMgrSecurityLogFileCloseFailedTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acEventMgrControlNodeId"),
        ("APPIAN-SYSTEM-MIB", "acEventMgrControlSecurityLogFileName"))
)
if mibBuilder.loadTexts:
    acEventMgrSecurityLogFileCloseFailedTrap.setStatus(
        "deprecated"
    )

acConfigMgrConfigFileCloseFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 4, 0, 1)
)
acConfigMgrConfigFileCloseFailedTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acConfigMgrNodeId"),
        ("APPIAN-SYSTEM-MIB", "acConfigMgrFileName"))
)
if mibBuilder.loadTexts:
    acConfigMgrConfigFileCloseFailedTrap.setStatus(
        "current"
    )

acSntpMgrPeerFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 0, 1)
)
acSntpMgrPeerFailureTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acSntpMgrNodeId"),
        ("APPIAN-SYSTEM-MIB", "acSntpMgrPeerIpAddress"))
)
if mibBuilder.loadTexts:
    acSntpMgrPeerFailureTrap.setStatus(
        "current"
    )

acSntpMgrVarianceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 0, 2)
)
acSntpMgrVarianceTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acSntpMgrNodeId"),
        ("APPIAN-SYSTEM-MIB", "acSntpMgrMaxVariance"),
        ("APPIAN-SYSTEM-MIB", "acSntpMgrVariance"))
)
if mibBuilder.loadTexts:
    acSntpMgrVarianceTrap.setStatus(
        "current"
    )

acSntpMgrHardwareTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 7, 0, 3)
)
acSntpMgrHardwareTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acSntpMgrNodeId"),
        ("APPIAN-SYSTEM-MIB", "acSntpMgrErrorCode"))
)
if mibBuilder.loadTexts:
    acSntpMgrHardwareTrap.setStatus(
        "current"
    )

acAuthenticationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 0, 1)
)
acAuthenticationFailureTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acAuthMgrNodeId"),
        ("APPIAN-SYSTEM-MIB", "acAuthMgrUserName"),
        ("APPIAN-SYSTEM-MIB", "acAuthMgrAccessMode"),
        ("APPIAN-SYSTEM-MIB", "acAuthMgrFailures"))
)
if mibBuilder.loadTexts:
    acAuthenticationFailureTrap.setStatus(
        "current"
    )

acAuthenticationExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 0, 2)
)
acAuthenticationExceededTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acAuthMgrNodeId"),
        ("APPIAN-SYSTEM-MIB", "acAuthMgrUserName"),
        ("APPIAN-SYSTEM-MIB", "acAuthMgrAccessMode"),
        ("APPIAN-SYSTEM-MIB", "acAuthMgrFailures"))
)
if mibBuilder.loadTexts:
    acAuthenticationExceededTrap.setStatus(
        "current"
    )

acAuthenticationSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 8, 0, 3)
)
acAuthenticationSuccessTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acAuthMgrNodeId"),
        ("APPIAN-SYSTEM-MIB", "acAuthMgrUserName"),
        ("APPIAN-SYSTEM-MIB", "acAuthMgrAccessMode"))
)
if mibBuilder.loadTexts:
    acAuthenticationSuccessTrap.setStatus(
        "current"
    )

acFileXferMgrXferFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 0, 1)
)
acFileXferMgrXferFailedTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acFileXferMgrNodeId"),
        ("APPIAN-SYSTEM-MIB", "acFileXferMgrRowId"),
        ("APPIAN-SYSTEM-MIB", "acFileXferMgrSourceFilename"),
        ("APPIAN-SYSTEM-MIB", "acFileXferMgrDestFilename"),
        ("APPIAN-SYSTEM-MIB", "acFileXferMgrOperation"))
)
if mibBuilder.loadTexts:
    acFileXferMgrXferFailedTrap.setStatus(
        "current"
    )

acFileXferMgrXferCompletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 10, 0, 2)
)
acFileXferMgrXferCompletedTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acFileXferMgrNodeId"),
        ("APPIAN-SYSTEM-MIB", "acFileXferMgrRowId"),
        ("APPIAN-SYSTEM-MIB", "acFileXferMgrSourceFilename"),
        ("APPIAN-SYSTEM-MIB", "acFileXferMgrDestFilename"),
        ("APPIAN-SYSTEM-MIB", "acFileXferMgrOperation"))
)
if mibBuilder.loadTexts:
    acFileXferMgrXferCompletedTrap.setStatus(
        "current"
    )

acRdpMgrRingMapChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 0, 1)
)
acRdpMgrRingMapChangedTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acRdpMgrNodeId"))
)
if mibBuilder.loadTexts:
    acRdpMgrRingMapChangedTrap.setStatus(
        "current"
    )

acRdpMgrDuplicateNodeIdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 7, 11, 0, 2)
)
acRdpMgrDuplicateNodeIdTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-SYSTEM-MIB", "acRdpMgrNodeId"))
)
if mibBuilder.loadTexts:
    acRdpMgrDuplicateNodeIdTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-SYSTEM-MIB",
    **{"AcAccessRights": AcAccessRights,
       "acSystem": acSystem,
       "acCommMgr": acCommMgr,
       "acCommMgrCommTable": acCommMgrCommTable,
       "acCommMgrCommEntry": acCommMgrCommEntry,
       "acCommMgrCommNodeId": acCommMgrCommNodeId,
       "acCommMgrCommId": acCommMgrCommId,
       "acCommMgrCommAdminStatus": acCommMgrCommAdminStatus,
       "acCommMgrCommString": acCommMgrCommString,
       "acCommMgrCommAccessRights": acCommMgrCommAccessRights,
       "acCommMgrSourceAddrTable": acCommMgrSourceAddrTable,
       "acCommMgrSourceAddrEntry": acCommMgrSourceAddrEntry,
       "acCommMgrSourceAddrNodeId": acCommMgrSourceAddrNodeId,
       "acCommMgrSourceAddrCommId": acCommMgrSourceAddrCommId,
       "acCommMgrSourceAddrIpAddress": acCommMgrSourceAddrIpAddress,
       "acCommMgrSourceAddrIpSubnet": acCommMgrSourceAddrIpSubnet,
       "acCommMgrSourceAddrAdminStatus": acCommMgrSourceAddrAdminStatus,
       "acStatsMgr": acStatsMgr,
       "acStatsMgrTable": acStatsMgrTable,
       "acStatsMgrEntry": acStatsMgrEntry,
       "acStatsMgrNodeId": acStatsMgrNodeId,
       "acStatsMgrAdminStatus": acStatsMgrAdminStatus,
       "acEventMgr": acEventMgr,
       "acEventMgrTraps": acEventMgrTraps,
       "acEventMgrLogFullTrap": acEventMgrLogFullTrap,
       "acEventMgrSecurityLogFullTrap": acEventMgrSecurityLogFullTrap,
       "acEventMgrLogFileCloseFailedTrap": acEventMgrLogFileCloseFailedTrap,
       "acEventMgrSecurityLogFileCloseFailedTrap": acEventMgrSecurityLogFileCloseFailedTrap,
       "acEventMgrControlTable": acEventMgrControlTable,
       "acEventMgrControlEntry": acEventMgrControlEntry,
       "acEventMgrControlNodeId": acEventMgrControlNodeId,
       "acEventMgrControlAdminStatus": acEventMgrControlAdminStatus,
       "acEventMgrControlLogMode": acEventMgrControlLogMode,
       "acEventMgrControlLogMaxFileSize": acEventMgrControlLogMaxFileSize,
       "acEventMgrControlLogCurrentSize": acEventMgrControlLogCurrentSize,
       "acEventMgrControlLogFileName": acEventMgrControlLogFileName,
       "acEventMgrControlLogFileWrapEnable": acEventMgrControlLogFileWrapEnable,
       "acEventMgrControlSecurityLogMode": acEventMgrControlSecurityLogMode,
       "acEventMgrControlSecurityLogMaxFileSize": acEventMgrControlSecurityLogMaxFileSize,
       "acEventMgrControlSecurityLogCurrentSize": acEventMgrControlSecurityLogCurrentSize,
       "acEventMgrControlSecurityLogFileName": acEventMgrControlSecurityLogFileName,
       "acEventMgrControlSecurityLogFileWrapEnable": acEventMgrControlSecurityLogFileWrapEnable,
       "acEventMgrControlRedirectTraceSlot1": acEventMgrControlRedirectTraceSlot1,
       "acEventMgrControlRedirectTraceSlot2": acEventMgrControlRedirectTraceSlot2,
       "acEventMgrAgentTable": acEventMgrAgentTable,
       "acEventMgrAgentEntry": acEventMgrAgentEntry,
       "acEventMgrAgentNodeId": acEventMgrAgentNodeId,
       "acEventMgrAgentId": acEventMgrAgentId,
       "acEventMgrAgentName": acEventMgrAgentName,
       "acEventMgrAgentAdminStatus": acEventMgrAgentAdminStatus,
       "acEventMgrAgentLogLevel": acEventMgrAgentLogLevel,
       "acEventMgrAgentNumberEvents": acEventMgrAgentNumberEvents,
       "acEventMgrAgentLastEventCode": acEventMgrAgentLastEventCode,
       "acEventMgrAgentLastEventCount": acEventMgrAgentLastEventCount,
       "acEventMgrAgentSlot": acEventMgrAgentSlot,
       "acEventMgrAgentTraceLevel": acEventMgrAgentTraceLevel,
       "acConfigMgr": acConfigMgr,
       "acConfigMgrTraps": acConfigMgrTraps,
       "acConfigMgrConfigFileCloseFailedTrap": acConfigMgrConfigFileCloseFailedTrap,
       "acConfigMgrTable": acConfigMgrTable,
       "acConfigMgrEntry": acConfigMgrEntry,
       "acConfigMgrNodeId": acConfigMgrNodeId,
       "acConfigMgrAdminStatus": acConfigMgrAdminStatus,
       "acConfigMgrCurrentRevision": acConfigMgrCurrentRevision,
       "acConfigMgrFileName": acConfigMgrFileName,
       "acConfigMgrAutoSaveInterval": acConfigMgrAutoSaveInterval,
       "acConfigMgrAutoSaveEnable": acConfigMgrAutoSaveEnable,
       "acConfigMgrLastWritten": acConfigMgrLastWritten,
       "acConfigMgrSaveConfig": acConfigMgrSaveConfig,
       "acConfigMgrOpStatus": acConfigMgrOpStatus,
       "acSntpMgr": acSntpMgr,
       "acSntpMgrTraps": acSntpMgrTraps,
       "acSntpMgrPeerFailureTrap": acSntpMgrPeerFailureTrap,
       "acSntpMgrVarianceTrap": acSntpMgrVarianceTrap,
       "acSntpMgrHardwareTrap": acSntpMgrHardwareTrap,
       "acSntpMgrTable": acSntpMgrTable,
       "acSntpMgrEntry": acSntpMgrEntry,
       "acSntpMgrNodeId": acSntpMgrNodeId,
       "acSntpMgrAdminStatus": acSntpMgrAdminStatus,
       "acSntpMgrOpStatus": acSntpMgrOpStatus,
       "acSntpMgrErrorCode": acSntpMgrErrorCode,
       "acSntpMgrPeerIpAddress": acSntpMgrPeerIpAddress,
       "acSntpMgrQueryInterval": acSntpMgrQueryInterval,
       "acSntpMgrRetryCount": acSntpMgrRetryCount,
       "acSntpMgrMaxVariance": acSntpMgrMaxVariance,
       "acSntpMgrVariance": acSntpMgrVariance,
       "acSntpMgrVarianceDetectEnable": acSntpMgrVarianceDetectEnable,
       "acSntpMgrTimeZone": acSntpMgrTimeZone,
       "acSntpMgrDayLightSaving": acSntpMgrDayLightSaving,
       "acAuthMgr": acAuthMgr,
       "acAuthMgrTraps": acAuthMgrTraps,
       "acAuthenticationFailureTrap": acAuthenticationFailureTrap,
       "acAuthenticationExceededTrap": acAuthenticationExceededTrap,
       "acAuthenticationSuccessTrap": acAuthenticationSuccessTrap,
       "acAuthMgrTable": acAuthMgrTable,
       "acAuthMgrEntry": acAuthMgrEntry,
       "acAuthMgrNodeId": acAuthMgrNodeId,
       "acAuthMgrUserId": acAuthMgrUserId,
       "acAuthMgrUserName": acAuthMgrUserName,
       "acAuthMgrAccessMode": acAuthMgrAccessMode,
       "acAuthMgrLogonTime": acAuthMgrLogonTime,
       "acAuthMgrFailures": acAuthMgrFailures,
       "acAuthMgrLockOut": acAuthMgrLockOut,
       "acAuthMgrDeleteEntry": acAuthMgrDeleteEntry,
       "acTrapMgr": acTrapMgr,
       "acTrapMgrDestAddrTable": acTrapMgrDestAddrTable,
       "acTrapMgrDestAddrEntry": acTrapMgrDestAddrEntry,
       "acTrapMgrDestAddrNodeId": acTrapMgrDestAddrNodeId,
       "acTrapMgrDestAddrCommId": acTrapMgrDestAddrCommId,
       "acTrapMgrDestAddrIpAddress": acTrapMgrDestAddrIpAddress,
       "acTrapMgrDestAddrAdminStatus": acTrapMgrDestAddrAdminStatus,
       "acTrapMgrFilterTable": acTrapMgrFilterTable,
       "acTrapMgrFilterEntry": acTrapMgrFilterEntry,
       "acTrapMgrFilterNodeId": acTrapMgrFilterNodeId,
       "acTrapMgrFilterCommId": acTrapMgrFilterCommId,
       "acTrapMgrFilterId": acTrapMgrFilterId,
       "acTrapMgrFilterAdminStatus": acTrapMgrFilterAdminStatus,
       "acTrapMgrFilterTrapOid": acTrapMgrFilterTrapOid,
       "acTrapMgrResendTable": acTrapMgrResendTable,
       "acTrapMgrResendEntry": acTrapMgrResendEntry,
       "acTrapMgrResendNodeId": acTrapMgrResendNodeId,
       "acTrapMgrResendAdminStatus": acTrapMgrResendAdminStatus,
       "acTrapMgrResendFromSeqId": acTrapMgrResendFromSeqId,
       "acTrapMgrResendToSeqId": acTrapMgrResendToSeqId,
       "acFileXferMgr": acFileXferMgr,
       "acFileXferMgrTraps": acFileXferMgrTraps,
       "acFileXferMgrXferFailedTrap": acFileXferMgrXferFailedTrap,
       "acFileXferMgrXferCompletedTrap": acFileXferMgrXferCompletedTrap,
       "acFileXferMgrTable": acFileXferMgrTable,
       "acFileXferMgrEntry": acFileXferMgrEntry,
       "acFileXferMgrNodeId": acFileXferMgrNodeId,
       "acFileXferMgrRowId": acFileXferMgrRowId,
       "acFileXferMgrAdminStatus": acFileXferMgrAdminStatus,
       "acFileXferMgrOperation": acFileXferMgrOperation,
       "acFileXferMgrFiletype": acFileXferMgrFiletype,
       "acFileXferMgrFilesubtype": acFileXferMgrFilesubtype,
       "acFileXferMgrFtpServerIpAddress": acFileXferMgrFtpServerIpAddress,
       "acFileXferMgrUsername": acFileXferMgrUsername,
       "acFileXferMgrPassword": acFileXferMgrPassword,
       "acFileXferMgrSourceDirectory": acFileXferMgrSourceDirectory,
       "acFileXferMgrSourceFilename": acFileXferMgrSourceFilename,
       "acFileXferMgrDestDirectory": acFileXferMgrDestDirectory,
       "acFileXferMgrDestFilename": acFileXferMgrDestFilename,
       "acFileXferMgrXferMode": acFileXferMgrXferMode,
       "acFileXferMgrOpStatus": acFileXferMgrOpStatus,
       "acRdpMgr": acRdpMgr,
       "acRdpMgrTraps": acRdpMgrTraps,
       "acRdpMgrRingMapChangedTrap": acRdpMgrRingMapChangedTrap,
       "acRdpMgrDuplicateNodeIdTrap": acRdpMgrDuplicateNodeIdTrap,
       "acRdpMgrTable": acRdpMgrTable,
       "acRdpMgrEntry": acRdpMgrEntry,
       "acRdpMgrNodeId": acRdpMgrNodeId,
       "acRdpMgrFsmState": acRdpMgrFsmState,
       "acRdpMgrRingMasterNodeMac": acRdpMgrRingMasterNodeMac,
       "acRdpMgrRingTopology": acRdpMgrRingTopology,
       "acRdpMgrRingState": acRdpMgrRingState,
       "acRdpMgrRingSize": acRdpMgrRingSize,
       "acRdpMgrRdpVersion": acRdpMgrRdpVersion,
       "acRdpMgrNodeTable": acRdpMgrNodeTable,
       "acRdpMgrNodeEntry": acRdpMgrNodeEntry,
       "acRdpMgrNodeThisNodeId": acRdpMgrNodeThisNodeId,
       "acRdpMgrNodeRowId": acRdpMgrNodeRowId,
       "acRdpMgrNodeNodeId": acRdpMgrNodeNodeId,
       "acRdpMgrNodeADccIpAddress": acRdpMgrNodeADccIpAddress,
       "acRdpMgrNodeADccMacAddress": acRdpMgrNodeADccMacAddress,
       "acRdpMgrNodeADccConfig": acRdpMgrNodeADccConfig,
       "acRdpMgrNodeADccEastOk": acRdpMgrNodeADccEastOk,
       "acRdpMgrNodeADccWestOk": acRdpMgrNodeADccWestOk,
       "acRdpMgrNodeNodeArch": acRdpMgrNodeNodeArch}
)
