# SNMP MIB module (CL-PKTC-EUE-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CL-PKTC-EUE-USER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:35 2024
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

(PktcEUETCActStatus,
 PktcEUETCActStatusInfo,
 PktcEUETCAppIdentifier,
 PktcEUETCAppOrgIdentifier,
 PktcEUETCCreds,
 PktcEUETCCredsType,
 PktcEUETCID,
 PktcEUETCIDType,
 PktcEUETCUsrAppIndexType,
 PktcEUETCUsrElementIndexType) = mibBuilder.importSymbols(
    "CL-PKTC-EUE-TC-MIB",
    "PktcEUETCActStatus",
    "PktcEUETCActStatusInfo",
    "PktcEUETCAppIdentifier",
    "PktcEUETCAppOrgIdentifier",
    "PktcEUETCCreds",
    "PktcEUETCCredsType",
    "PktcEUETCID",
    "PktcEUETCIDType",
    "PktcEUETCUsrAppIndexType",
    "PktcEUETCUsrElementIndexType")

(pktcEUEMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcEUEMibs")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcEUEUserMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PktcEUEUsrNotification_ObjectIdentity = ObjectIdentity
pktcEUEUsrNotification = _PktcEUEUsrNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 0)
)
_PktcEUEUsrObjects_ObjectIdentity = ObjectIdentity
pktcEUEUsrObjects = _PktcEUEUsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1)
)
_PktcEUEUsrProfile_ObjectIdentity = ObjectIdentity
pktcEUEUsrProfile = _PktcEUEUsrProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1)
)


class _PktcEUEUsrProfileVersion_Type(SnmpAdminString):
    """Custom type pktcEUEUsrProfileVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_PktcEUEUsrProfileVersion_Type.__name__ = "SnmpAdminString"
_PktcEUEUsrProfileVersion_Object = MibScalar
pktcEUEUsrProfileVersion = _PktcEUEUsrProfileVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 1),
    _PktcEUEUsrProfileVersion_Type()
)
pktcEUEUsrProfileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEUsrProfileVersion.setStatus("current")
_PktcEUEUsrIMPUTable_Object = MibTable
pktcEUEUsrIMPUTable = _PktcEUEUsrIMPUTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUTable.setStatus("current")
_PktcEUEUsrIMPUEntry_Object = MibTableRow
pktcEUEUsrIMPUEntry = _PktcEUEUsrIMPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1)
)
pktcEUEUsrIMPUEntry.setIndexNames(
    (0, "CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUEntry.setStatus("current")
_PktcEUEUsrIMPUIndex_Type = PktcEUETCUsrElementIndexType
_PktcEUEUsrIMPUIndex_Object = MibTableColumn
pktcEUEUsrIMPUIndex = _PktcEUEUsrIMPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 1),
    _PktcEUEUsrIMPUIndex_Type()
)
pktcEUEUsrIMPUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUIndex.setStatus("current")


class _PktcEUEUsrIMPUIdType_Type(PktcEUETCIDType):
    """Custom type pktcEUEUsrIMPUIdType based on PktcEUETCIDType"""


_PktcEUEUsrIMPUIdType_Object = MibTableColumn
pktcEUEUsrIMPUIdType = _PktcEUEUsrIMPUIdType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 2),
    _PktcEUEUsrIMPUIdType_Type()
)
pktcEUEUsrIMPUIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUIdType.setStatus("current")
_PktcEUEUsrIMPUId_Type = PktcEUETCID
_PktcEUEUsrIMPUId_Object = MibTableColumn
pktcEUEUsrIMPUId = _PktcEUEUsrIMPUId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 3),
    _PktcEUEUsrIMPUId_Type()
)
pktcEUEUsrIMPUId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUId.setStatus("current")


class _PktcEUEUsrIMPUIMPIIndexRef_Type(PktcEUETCUsrElementIndexType):
    """Custom type pktcEUEUsrIMPUIMPIIndexRef based on PktcEUETCUsrElementIndexType"""
    defaultValue = 0


_PktcEUEUsrIMPUIMPIIndexRef_Object = MibTableColumn
pktcEUEUsrIMPUIMPIIndexRef = _PktcEUEUsrIMPUIMPIIndexRef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 4),
    _PktcEUEUsrIMPUIMPIIndexRef_Type()
)
pktcEUEUsrIMPUIMPIIndexRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUIMPIIndexRef.setStatus("current")
_PktcEUEUsrIMPUDispInfo_Type = SnmpAdminString
_PktcEUEUsrIMPUDispInfo_Object = MibTableColumn
pktcEUEUsrIMPUDispInfo = _PktcEUEUsrIMPUDispInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 5),
    _PktcEUEUsrIMPUDispInfo_Type()
)
pktcEUEUsrIMPUDispInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUDispInfo.setStatus("current")
_PktcEUEUsrIMPUOpIndexRefs_Type = SnmpAdminString
_PktcEUEUsrIMPUOpIndexRefs_Object = MibTableColumn
pktcEUEUsrIMPUOpIndexRefs = _PktcEUEUsrIMPUOpIndexRefs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 6),
    _PktcEUEUsrIMPUOpIndexRefs_Type()
)
pktcEUEUsrIMPUOpIndexRefs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUOpIndexRefs.setStatus("current")


class _PktcEUEUsrIMPUNWActStat_Type(PktcEUETCActStatus):
    """Custom type pktcEUEUsrIMPUNWActStat based on PktcEUETCActStatus"""


_PktcEUEUsrIMPUNWActStat_Object = MibTableColumn
pktcEUEUsrIMPUNWActStat = _PktcEUEUsrIMPUNWActStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 7),
    _PktcEUEUsrIMPUNWActStat_Type()
)
pktcEUEUsrIMPUNWActStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUNWActStat.setStatus("current")
_PktcEUEUsrIMPUNWActStatInfo_Type = SnmpAdminString
_PktcEUEUsrIMPUNWActStatInfo_Object = MibTableColumn
pktcEUEUsrIMPUNWActStatInfo = _PktcEUEUsrIMPUNWActStatInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 8),
    _PktcEUEUsrIMPUNWActStatInfo_Type()
)
pktcEUEUsrIMPUNWActStatInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUNWActStatInfo.setStatus("current")


class _PktcEUEUsrIMPUUEActStat_Type(PktcEUETCActStatus):
    """Custom type pktcEUEUsrIMPUUEActStat based on PktcEUETCActStatus"""


_PktcEUEUsrIMPUUEActStat_Object = MibTableColumn
pktcEUEUsrIMPUUEActStat = _PktcEUEUsrIMPUUEActStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 9),
    _PktcEUEUsrIMPUUEActStat_Type()
)
pktcEUEUsrIMPUUEActStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUUEActStat.setStatus("current")
_PktcEUEUsrIMPUUEActStatInfo_Type = SnmpAdminString
_PktcEUEUsrIMPUUEActStatInfo_Object = MibTableColumn
pktcEUEUsrIMPUUEActStatInfo = _PktcEUEUsrIMPUUEActStatInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 10),
    _PktcEUEUsrIMPUUEActStatInfo_Type()
)
pktcEUEUsrIMPUUEActStatInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUUEActStatInfo.setStatus("current")


class _PktcEUEUsrIMPUSigSecurity_Type(TruthValue):
    """Custom type pktcEUEUsrIMPUSigSecurity based on TruthValue"""


_PktcEUEUsrIMPUSigSecurity_Object = MibTableColumn
pktcEUEUsrIMPUSigSecurity = _PktcEUEUsrIMPUSigSecurity_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 11),
    _PktcEUEUsrIMPUSigSecurity_Type()
)
pktcEUEUsrIMPUSigSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUSigSecurity.setStatus("current")
_PktcEUEUsrIMPUAdditionalInfo_Type = SnmpAdminString
_PktcEUEUsrIMPUAdditionalInfo_Object = MibTableColumn
pktcEUEUsrIMPUAdditionalInfo = _PktcEUEUsrIMPUAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 12),
    _PktcEUEUsrIMPUAdditionalInfo_Type()
)
pktcEUEUsrIMPUAdditionalInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUAdditionalInfo.setStatus("current")
_PktcEUEUsrIMPURowStatus_Type = RowStatus
_PktcEUEUsrIMPURowStatus_Object = MibTableColumn
pktcEUEUsrIMPURowStatus = _PktcEUEUsrIMPURowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 13),
    _PktcEUEUsrIMPURowStatus_Type()
)
pktcEUEUsrIMPURowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPURowStatus.setStatus("current")
_PktcEUEUsrIMPITable_Object = MibTable
pktcEUEUsrIMPITable = _PktcEUEUsrIMPITable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pktcEUEUsrIMPITable.setStatus("current")
_PktcEUEUsrIMPIEntry_Object = MibTableRow
pktcEUEUsrIMPIEntry = _PktcEUEUsrIMPIEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3, 1)
)
pktcEUEUsrIMPIEntry.setIndexNames(
    (0, "CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPIIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEUsrIMPIEntry.setStatus("current")
_PktcEUEUsrIMPIIndex_Type = PktcEUETCUsrElementIndexType
_PktcEUEUsrIMPIIndex_Object = MibTableColumn
pktcEUEUsrIMPIIndex = _PktcEUEUsrIMPIIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3, 1, 1),
    _PktcEUEUsrIMPIIndex_Type()
)
pktcEUEUsrIMPIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPIIndex.setStatus("current")


class _PktcEUEUsrIMPIIdType_Type(PktcEUETCIDType):
    """Custom type pktcEUEUsrIMPIIdType based on PktcEUETCIDType"""


_PktcEUEUsrIMPIIdType_Object = MibTableColumn
pktcEUEUsrIMPIIdType = _PktcEUEUsrIMPIIdType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3, 1, 2),
    _PktcEUEUsrIMPIIdType_Type()
)
pktcEUEUsrIMPIIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPIIdType.setStatus("current")
_PktcEUEUsrIMPIId_Type = PktcEUETCID
_PktcEUEUsrIMPIId_Object = MibTableColumn
pktcEUEUsrIMPIId = _PktcEUEUsrIMPIId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3, 1, 3),
    _PktcEUEUsrIMPIId_Type()
)
pktcEUEUsrIMPIId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPIId.setStatus("current")


class _PktcEUEUsrIMPICredsType_Type(PktcEUETCCredsType):
    """Custom type pktcEUEUsrIMPICredsType based on PktcEUETCCredsType"""


_PktcEUEUsrIMPICredsType_Object = MibTableColumn
pktcEUEUsrIMPICredsType = _PktcEUEUsrIMPICredsType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3, 1, 4),
    _PktcEUEUsrIMPICredsType_Type()
)
pktcEUEUsrIMPICredsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPICredsType.setStatus("current")
_PktcEUEUsrIMPICredentials_Type = PktcEUETCCreds
_PktcEUEUsrIMPICredentials_Object = MibTableColumn
pktcEUEUsrIMPICredentials = _PktcEUEUsrIMPICredentials_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3, 1, 5),
    _PktcEUEUsrIMPICredentials_Type()
)
pktcEUEUsrIMPICredentials.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPICredentials.setStatus("current")
_PktcEUEUsrIMPIRowStatus_Type = RowStatus
_PktcEUEUsrIMPIRowStatus_Object = MibTableColumn
pktcEUEUsrIMPIRowStatus = _PktcEUEUsrIMPIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3, 1, 6),
    _PktcEUEUsrIMPIRowStatus_Type()
)
pktcEUEUsrIMPIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPIRowStatus.setStatus("current")
_PktcEUEUsrAppMapTable_Object = MibTable
pktcEUEUsrAppMapTable = _PktcEUEUsrAppMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapTable.setStatus("current")
_PktcEUEUsrAppMapEntry_Object = MibTableRow
pktcEUEUsrAppMapEntry = _PktcEUEUsrAppMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1)
)
pktcEUEUsrAppMapEntry.setIndexNames(
    (0, "CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUIndex"),
    (0, "CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapEntry.setStatus("current")
_PktcEUEUsrAppMapAppIndex_Type = PktcEUETCUsrAppIndexType
_PktcEUEUsrAppMapAppIndex_Object = MibTableColumn
pktcEUEUsrAppMapAppIndex = _PktcEUEUsrAppMapAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 1),
    _PktcEUEUsrAppMapAppIndex_Type()
)
pktcEUEUsrAppMapAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppIndex.setStatus("current")
_PktcEUEUsrAppMapAppOrgID_Type = PktcEUETCAppOrgIdentifier
_PktcEUEUsrAppMapAppOrgID_Object = MibTableColumn
pktcEUEUsrAppMapAppOrgID = _PktcEUEUsrAppMapAppOrgID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 2),
    _PktcEUEUsrAppMapAppOrgID_Type()
)
pktcEUEUsrAppMapAppOrgID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppOrgID.setStatus("current")
_PktcEUEUsrAppMapAppIdentifier_Type = PktcEUETCAppIdentifier
_PktcEUEUsrAppMapAppIdentifier_Object = MibTableColumn
pktcEUEUsrAppMapAppIdentifier = _PktcEUEUsrAppMapAppIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 3),
    _PktcEUEUsrAppMapAppIdentifier_Type()
)
pktcEUEUsrAppMapAppIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppIdentifier.setStatus("current")


class _PktcEUEUsrAppMapAppIndexRef_Type(PktcEUETCUsrAppIndexType):
    """Custom type pktcEUEUsrAppMapAppIndexRef based on PktcEUETCUsrAppIndexType"""
    defaultValue = 0


_PktcEUEUsrAppMapAppIndexRef_Object = MibTableColumn
pktcEUEUsrAppMapAppIndexRef = _PktcEUEUsrAppMapAppIndexRef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 4),
    _PktcEUEUsrAppMapAppIndexRef_Type()
)
pktcEUEUsrAppMapAppIndexRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppIndexRef.setStatus("current")


class _PktcEUEUsrAppMapAppNWActStat_Type(PktcEUETCActStatus):
    """Custom type pktcEUEUsrAppMapAppNWActStat based on PktcEUETCActStatus"""


_PktcEUEUsrAppMapAppNWActStat_Object = MibTableColumn
pktcEUEUsrAppMapAppNWActStat = _PktcEUEUsrAppMapAppNWActStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 5),
    _PktcEUEUsrAppMapAppNWActStat_Type()
)
pktcEUEUsrAppMapAppNWActStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppNWActStat.setStatus("current")
_PktcEUEUsrAppMapAppNWActStatInfo_Type = PktcEUETCActStatusInfo
_PktcEUEUsrAppMapAppNWActStatInfo_Object = MibTableColumn
pktcEUEUsrAppMapAppNWActStatInfo = _PktcEUEUsrAppMapAppNWActStatInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 6),
    _PktcEUEUsrAppMapAppNWActStatInfo_Type()
)
pktcEUEUsrAppMapAppNWActStatInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppNWActStatInfo.setStatus("current")


class _PktcEUEUsrAppMapAppUEActStat_Type(PktcEUETCActStatus):
    """Custom type pktcEUEUsrAppMapAppUEActStat based on PktcEUETCActStatus"""


_PktcEUEUsrAppMapAppUEActStat_Object = MibTableColumn
pktcEUEUsrAppMapAppUEActStat = _PktcEUEUsrAppMapAppUEActStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 7),
    _PktcEUEUsrAppMapAppUEActStat_Type()
)
pktcEUEUsrAppMapAppUEActStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppUEActStat.setStatus("current")
_PktcEUEUsrAppMapAppUEActStatInfo_Type = PktcEUETCActStatusInfo
_PktcEUEUsrAppMapAppUEActStatInfo_Object = MibTableColumn
pktcEUEUsrAppMapAppUEActStatInfo = _PktcEUEUsrAppMapAppUEActStatInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 8),
    _PktcEUEUsrAppMapAppUEActStatInfo_Type()
)
pktcEUEUsrAppMapAppUEActStatInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppUEActStatInfo.setStatus("current")
_PktcEUEUsrAppMapRowStatus_Type = RowStatus
_PktcEUEUsrAppMapRowStatus_Object = MibTableColumn
pktcEUEUsrAppMapRowStatus = _PktcEUEUsrAppMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 9),
    _PktcEUEUsrAppMapRowStatus_Type()
)
pktcEUEUsrAppMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapRowStatus.setStatus("current")
_PktcEUEUsrConformance_ObjectIdentity = ObjectIdentity
pktcEUEUsrConformance = _PktcEUEUsrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2)
)
_PktcEUEUsrCompliances_ObjectIdentity = ObjectIdentity
pktcEUEUsrCompliances = _PktcEUEUsrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 1)
)
_PktcEUEUsrMIBCompliances_ObjectIdentity = ObjectIdentity
pktcEUEUsrMIBCompliances = _PktcEUEUsrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 1)
)
_PktcEUEUsrGroups_ObjectIdentity = ObjectIdentity
pktcEUEUsrGroups = _PktcEUEUsrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 2)
)
_PktcEUEUsrMIBGroups_ObjectIdentity = ObjectIdentity
pktcEUEUsrMIBGroups = _PktcEUEUsrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 2)
)

# Managed Objects groups

pktcEUEUsrIMPUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 1, 2)
)
pktcEUEUsrIMPUGroup.setObjects(
      *(("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUIdType"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUId"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUIMPIIndexRef"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUDispInfo"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUOpIndexRefs"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUNWActStat"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUNWActStatInfo"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUUEActStat"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUUEActStatInfo"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUSigSecurity"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUAdditionalInfo"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPURowStatus"))
)
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUGroup.setStatus("current")

pktcEUEUsrIMPIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 1, 3)
)
pktcEUEUsrIMPIGroup.setObjects(
      *(("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPICredsType"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPICredentials"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPIIdType"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPIId"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPIRowStatus"))
)
if mibBuilder.loadTexts:
    pktcEUEUsrIMPIGroup.setStatus("current")

pktcEUEUsrAppMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 1, 4)
)
pktcEUEUsrAppMapGroup.setObjects(
      *(("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppOrgID"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppIdentifier"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppIndexRef"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppNWActStat"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppNWActStatInfo"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppUEActStat"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppUEActStatInfo"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapRowStatus"))
)
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapGroup.setStatus("current")

pktcEUEUsrProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 2, 1)
)
pktcEUEUsrProfileGroup.setObjects(
    ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrProfileVersion")
)
if mibBuilder.loadTexts:
    pktcEUEUsrProfileGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcEUEUsrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcEUEUsrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PKTC-EUE-USER-MIB",
    **{"pktcEUEUserMIB": pktcEUEUserMIB,
       "pktcEUEUsrNotification": pktcEUEUsrNotification,
       "pktcEUEUsrObjects": pktcEUEUsrObjects,
       "pktcEUEUsrProfile": pktcEUEUsrProfile,
       "pktcEUEUsrProfileVersion": pktcEUEUsrProfileVersion,
       "pktcEUEUsrIMPUTable": pktcEUEUsrIMPUTable,
       "pktcEUEUsrIMPUEntry": pktcEUEUsrIMPUEntry,
       "pktcEUEUsrIMPUIndex": pktcEUEUsrIMPUIndex,
       "pktcEUEUsrIMPUIdType": pktcEUEUsrIMPUIdType,
       "pktcEUEUsrIMPUId": pktcEUEUsrIMPUId,
       "pktcEUEUsrIMPUIMPIIndexRef": pktcEUEUsrIMPUIMPIIndexRef,
       "pktcEUEUsrIMPUDispInfo": pktcEUEUsrIMPUDispInfo,
       "pktcEUEUsrIMPUOpIndexRefs": pktcEUEUsrIMPUOpIndexRefs,
       "pktcEUEUsrIMPUNWActStat": pktcEUEUsrIMPUNWActStat,
       "pktcEUEUsrIMPUNWActStatInfo": pktcEUEUsrIMPUNWActStatInfo,
       "pktcEUEUsrIMPUUEActStat": pktcEUEUsrIMPUUEActStat,
       "pktcEUEUsrIMPUUEActStatInfo": pktcEUEUsrIMPUUEActStatInfo,
       "pktcEUEUsrIMPUSigSecurity": pktcEUEUsrIMPUSigSecurity,
       "pktcEUEUsrIMPUAdditionalInfo": pktcEUEUsrIMPUAdditionalInfo,
       "pktcEUEUsrIMPURowStatus": pktcEUEUsrIMPURowStatus,
       "pktcEUEUsrIMPITable": pktcEUEUsrIMPITable,
       "pktcEUEUsrIMPIEntry": pktcEUEUsrIMPIEntry,
       "pktcEUEUsrIMPIIndex": pktcEUEUsrIMPIIndex,
       "pktcEUEUsrIMPIIdType": pktcEUEUsrIMPIIdType,
       "pktcEUEUsrIMPIId": pktcEUEUsrIMPIId,
       "pktcEUEUsrIMPICredsType": pktcEUEUsrIMPICredsType,
       "pktcEUEUsrIMPICredentials": pktcEUEUsrIMPICredentials,
       "pktcEUEUsrIMPIRowStatus": pktcEUEUsrIMPIRowStatus,
       "pktcEUEUsrAppMapTable": pktcEUEUsrAppMapTable,
       "pktcEUEUsrAppMapEntry": pktcEUEUsrAppMapEntry,
       "pktcEUEUsrAppMapAppIndex": pktcEUEUsrAppMapAppIndex,
       "pktcEUEUsrAppMapAppOrgID": pktcEUEUsrAppMapAppOrgID,
       "pktcEUEUsrAppMapAppIdentifier": pktcEUEUsrAppMapAppIdentifier,
       "pktcEUEUsrAppMapAppIndexRef": pktcEUEUsrAppMapAppIndexRef,
       "pktcEUEUsrAppMapAppNWActStat": pktcEUEUsrAppMapAppNWActStat,
       "pktcEUEUsrAppMapAppNWActStatInfo": pktcEUEUsrAppMapAppNWActStatInfo,
       "pktcEUEUsrAppMapAppUEActStat": pktcEUEUsrAppMapAppUEActStat,
       "pktcEUEUsrAppMapAppUEActStatInfo": pktcEUEUsrAppMapAppUEActStatInfo,
       "pktcEUEUsrAppMapRowStatus": pktcEUEUsrAppMapRowStatus,
       "pktcEUEUsrConformance": pktcEUEUsrConformance,
       "pktcEUEUsrCompliances": pktcEUEUsrCompliances,
       "pktcEUEUsrMIBCompliances": pktcEUEUsrMIBCompliances,
       "pktcEUEUsrMIBCompliance": pktcEUEUsrMIBCompliance,
       "pktcEUEUsrIMPUGroup": pktcEUEUsrIMPUGroup,
       "pktcEUEUsrIMPIGroup": pktcEUEUsrIMPIGroup,
       "pktcEUEUsrAppMapGroup": pktcEUEUsrAppMapGroup,
       "pktcEUEUsrGroups": pktcEUEUsrGroups,
       "pktcEUEUsrMIBGroups": pktcEUEUsrMIBGroups,
       "pktcEUEUsrProfileGroup": pktcEUEUsrProfileGroup}
)
