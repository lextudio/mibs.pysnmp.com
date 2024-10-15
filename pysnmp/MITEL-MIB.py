# SNMP MIB module (MITEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:10 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 internet,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "internet",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""




class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
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





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class TimeStamp(TimeTicks):
    """Custom type TimeStamp based on TimeTicks"""




class TimeInterval(Integer32):
    """Custom type TimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class TDomain(ObjectIdentifier):
    """Custom type TDomain based on ObjectIdentifier"""




class TAddress(OctetString):
    """Custom type TAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )





class MitelIfType(Integer32):
    """Custom type MitelIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dnic", 1)
    )





class MitelNotifyTransportType(Integer32):
    """Custom type MitelNotifyTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mitelNotifTransInform", 3),
          ("mitelNotifTransV1Trap", 1),
          ("mitelNotifTransV2Trap", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelIdentification_ObjectIdentity = ObjectIdentity
mitelIdentification = _MitelIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1)
)
_MitelIdMgmtPlatforms_ObjectIdentity = ObjectIdentity
mitelIdMgmtPlatforms = _MitelIdMgmtPlatforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 1)
)
_MitelIdMgmtOpsMgr_ObjectIdentity = ObjectIdentity
mitelIdMgmtOpsMgr = _MitelIdMgmtOpsMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 1, 1)
)
_MitelIdCallServers_ObjectIdentity = ObjectIdentity
mitelIdCallServers = _MitelIdCallServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2)
)
_MitelIdCsMc2_ObjectIdentity = ObjectIdentity
mitelIdCsMc2 = _MitelIdCsMc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 1)
)
_MitelIdCs2000Light_ObjectIdentity = ObjectIdentity
mitelIdCs2000Light = _MitelIdCs2000Light_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 2)
)
_MitelIdTerminals_ObjectIdentity = ObjectIdentity
mitelIdTerminals = _MitelIdTerminals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 3)
)
_MitelIdInterfaces_ObjectIdentity = ObjectIdentity
mitelIdInterfaces = _MitelIdInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 4)
)
_MitelIdCtiPlatforms_ObjectIdentity = ObjectIdentity
mitelIdCtiPlatforms = _MitelIdCtiPlatforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 5)
)
_MitelExperimental_ObjectIdentity = ObjectIdentity
mitelExperimental = _MitelExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 2)
)
_MitelExtensions_ObjectIdentity = ObjectIdentity
mitelExtensions = _MitelExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 3)
)
_MitelExtInterfaces_ObjectIdentity = ObjectIdentity
mitelExtInterfaces = _MitelExtInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 3, 2)
)
_MitelIfNumber_Type = Integer32
_MitelIfNumber_Object = MibScalar
mitelIfNumber = _MitelIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 1027, 3, 2, 1),
    _MitelIfNumber_Type()
)
mitelIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelIfNumber.setStatus("mandatory")
_MitelIfTable_Object = MibTable
mitelIfTable = _MitelIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 3, 2, 2)
)
if mibBuilder.loadTexts:
    mitelIfTable.setStatus("mandatory")
_MitelIfTableEntry_Object = MibTableRow
mitelIfTableEntry = _MitelIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 3, 2, 2, 1)
)
mitelIfTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mitelIfTableEntry.setStatus("mandatory")
_MitelIfTblType_Type = MitelIfType
_MitelIfTblType_Object = MibTableColumn
mitelIfTblType = _MitelIfTblType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 3, 2, 2, 1, 1),
    _MitelIfTblType_Type()
)
mitelIfTblType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelIfTblType.setStatus("mandatory")
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelPropApplications_ObjectIdentity = ObjectIdentity
mitelPropApplications = _MitelPropApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1)
)
_MitelAppCallServer_ObjectIdentity = ObjectIdentity
mitelAppCallServer = _MitelAppCallServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1)
)
_MitelPropTransmission_ObjectIdentity = ObjectIdentity
mitelPropTransmission = _MitelPropTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2)
)
_MitelPropProtocols_ObjectIdentity = ObjectIdentity
mitelPropProtocols = _MitelPropProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 3)
)
_MitelPropUtilities_ObjectIdentity = ObjectIdentity
mitelPropUtilities = _MitelPropUtilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 4)
)
_MitelPropHardware_ObjectIdentity = ObjectIdentity
mitelPropHardware = _MitelPropHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 5)
)
_MitelPropNotifications_ObjectIdentity = ObjectIdentity
mitelPropNotifications = _MitelPropNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6)
)
_MitelNotifTraps_ObjectIdentity = ObjectIdentity
mitelNotifTraps = _MitelNotifTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 1)
)
_MitelNotifCount_Type = Integer32
_MitelNotifCount_Object = MibScalar
mitelNotifCount = _MitelNotifCount_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 2),
    _MitelNotifCount_Type()
)
mitelNotifCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifCount.setStatus("mandatory")
_MitelNotifEnableTable_Object = MibTable
mitelNotifEnableTable = _MitelNotifEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 3)
)
if mibBuilder.loadTexts:
    mitelNotifEnableTable.setStatus("mandatory")
_MitelNotifEnableTableEntry_Object = MibTableRow
mitelNotifEnableTableEntry = _MitelNotifEnableTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1)
)
mitelNotifEnableTableEntry.setIndexNames(
    (0, "MITEL-MIB", "mitelNotifEnblTblIndex"),
)
if mibBuilder.loadTexts:
    mitelNotifEnableTableEntry.setStatus("mandatory")
_MitelNotifEnblTblIndex_Type = Integer32
_MitelNotifEnblTblIndex_Object = MibTableColumn
mitelNotifEnblTblIndex = _MitelNotifEnblTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 1),
    _MitelNotifEnblTblIndex_Type()
)
mitelNotifEnblTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifEnblTblIndex.setStatus("mandatory")
_MitelNotifEnblTblOid_Type = ObjectIdentifier
_MitelNotifEnblTblOid_Object = MibTableColumn
mitelNotifEnblTblOid = _MitelNotifEnblTblOid_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 2),
    _MitelNotifEnblTblOid_Type()
)
mitelNotifEnblTblOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifEnblTblOid.setStatus("mandatory")
_MitelNotifEnblTblEnable_Type = TruthValue
_MitelNotifEnblTblEnable_Object = MibTableColumn
mitelNotifEnblTblEnable = _MitelNotifEnblTblEnable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 3),
    _MitelNotifEnblTblEnable_Type()
)
mitelNotifEnblTblEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNotifEnblTblEnable.setStatus("mandatory")
_MitelNotifEnblTblAck_Type = TruthValue
_MitelNotifEnblTblAck_Object = MibTableColumn
mitelNotifEnblTblAck = _MitelNotifEnblTblAck_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 4),
    _MitelNotifEnblTblAck_Type()
)
mitelNotifEnblTblAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNotifEnblTblAck.setStatus("mandatory")
_MitelNotifEnblTblOccurrences_Type = Counter32
_MitelNotifEnblTblOccurrences_Object = MibTableColumn
mitelNotifEnblTblOccurrences = _MitelNotifEnblTblOccurrences_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 5),
    _MitelNotifEnblTblOccurrences_Type()
)
mitelNotifEnblTblOccurrences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifEnblTblOccurrences.setStatus("mandatory")
_MitelNotifEnblTblDescr_Type = DisplayString
_MitelNotifEnblTblDescr_Object = MibTableColumn
mitelNotifEnblTblDescr = _MitelNotifEnblTblDescr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 3, 1, 6),
    _MitelNotifEnblTblDescr_Type()
)
mitelNotifEnblTblDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifEnblTblDescr.setStatus("mandatory")
_MitelNotifManagerTable_Object = MibTable
mitelNotifManagerTable = _MitelNotifManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 4)
)
if mibBuilder.loadTexts:
    mitelNotifManagerTable.setStatus("mandatory")
_MitelNotifManagerTableEntry_Object = MibTableRow
mitelNotifManagerTableEntry = _MitelNotifManagerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1)
)
mitelNotifManagerTableEntry.setIndexNames(
    (0, "MITEL-MIB", "mitelNotifMgrTblIndex"),
)
if mibBuilder.loadTexts:
    mitelNotifManagerTableEntry.setStatus("mandatory")
_MitelNotifMgrTblIndex_Type = Integer32
_MitelNotifMgrTblIndex_Object = MibTableColumn
mitelNotifMgrTblIndex = _MitelNotifMgrTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 1),
    _MitelNotifMgrTblIndex_Type()
)
mitelNotifMgrTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifMgrTblIndex.setStatus("mandatory")


class _MitelNotifMgrTblStatus_Type(RowStatus):
    """Custom type mitelNotifMgrTblStatus based on RowStatus"""


_MitelNotifMgrTblStatus_Object = MibTableColumn
mitelNotifMgrTblStatus = _MitelNotifMgrTblStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 2),
    _MitelNotifMgrTblStatus_Type()
)
mitelNotifMgrTblStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNotifMgrTblStatus.setStatus("mandatory")


class _MitelNotifMgrTblTransport_Type(MitelNotifyTransportType):
    """Custom type mitelNotifMgrTblTransport based on MitelNotifyTransportType"""


_MitelNotifMgrTblTransport_Object = MibTableColumn
mitelNotifMgrTblTransport = _MitelNotifMgrTblTransport_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 3),
    _MitelNotifMgrTblTransport_Type()
)
mitelNotifMgrTblTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNotifMgrTblTransport.setStatus("mandatory")


class _MitelNotifMgrTblDomain_Type(TDomain):
    """Custom type mitelNotifMgrTblDomain based on TDomain"""
    defaultValue = (1, 3, 6, 1, 6, 1, 1)


_MitelNotifMgrTblDomain_Object = MibTableColumn
mitelNotifMgrTblDomain = _MitelNotifMgrTblDomain_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 4),
    _MitelNotifMgrTblDomain_Type()
)
mitelNotifMgrTblDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNotifMgrTblDomain.setStatus("mandatory")


class _MitelNotifMgrTblAddress_Type(TAddress):
    """Custom type mitelNotifMgrTblAddress based on TAddress"""
    defaultHexValue = "c00002000489"


_MitelNotifMgrTblAddress_Object = MibTableColumn
mitelNotifMgrTblAddress = _MitelNotifMgrTblAddress_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 5),
    _MitelNotifMgrTblAddress_Type()
)
mitelNotifMgrTblAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNotifMgrTblAddress.setStatus("mandatory")


class _MitelNotifMgrTblTimeout_Type(TimeInterval):
    """Custom type mitelNotifMgrTblTimeout based on TimeInterval"""
    defaultValue = 1000


_MitelNotifMgrTblTimeout_Object = MibTableColumn
mitelNotifMgrTblTimeout = _MitelNotifMgrTblTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 6),
    _MitelNotifMgrTblTimeout_Type()
)
mitelNotifMgrTblTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNotifMgrTblTimeout.setStatus("mandatory")


class _MitelNotifMgrTblRetries_Type(Integer32):
    """Custom type mitelNotifMgrTblRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MitelNotifMgrTblRetries_Type.__name__ = "Integer32"
_MitelNotifMgrTblRetries_Object = MibTableColumn
mitelNotifMgrTblRetries = _MitelNotifMgrTblRetries_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 7),
    _MitelNotifMgrTblRetries_Type()
)
mitelNotifMgrTblRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNotifMgrTblRetries.setStatus("mandatory")


class _MitelNotifMgrTblLife_Type(TimeInterval):
    """Custom type mitelNotifMgrTblLife based on TimeInterval"""
    defaultValue = 8640000


_MitelNotifMgrTblLife_Object = MibTableColumn
mitelNotifMgrTblLife = _MitelNotifMgrTblLife_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 8),
    _MitelNotifMgrTblLife_Type()
)
mitelNotifMgrTblLife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNotifMgrTblLife.setStatus("mandatory")


class _MitelNotifMgrTblCommunity_Type(OctetString):
    """Custom type mitelNotifMgrTblCommunity based on OctetString"""
    defaultValue = OctetString("public")


_MitelNotifMgrTblCommunity_Object = MibTableColumn
mitelNotifMgrTblCommunity = _MitelNotifMgrTblCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 9),
    _MitelNotifMgrTblCommunity_Type()
)
mitelNotifMgrTblCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNotifMgrTblCommunity.setStatus("mandatory")


class _MitelNotifMgrTblName_Type(DisplayString):
    """Custom type mitelNotifMgrTblName based on DisplayString"""
    defaultValue = OctetString("None specified.")


_MitelNotifMgrTblName_Object = MibTableColumn
mitelNotifMgrTblName = _MitelNotifMgrTblName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 4, 1, 10),
    _MitelNotifMgrTblName_Type()
)
mitelNotifMgrTblName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNotifMgrTblName.setStatus("mandatory")


class _MitelNotifHistoryMax_Type(Integer32):
    """Custom type mitelNotifHistoryMax based on Integer32"""
    defaultValue = 100


_MitelNotifHistoryMax_Object = MibScalar
mitelNotifHistoryMax = _MitelNotifHistoryMax_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 5),
    _MitelNotifHistoryMax_Type()
)
mitelNotifHistoryMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNotifHistoryMax.setStatus("mandatory")
_MitelNotifHistorySize_Type = Integer32
_MitelNotifHistorySize_Object = MibScalar
mitelNotifHistorySize = _MitelNotifHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 6),
    _MitelNotifHistorySize_Type()
)
mitelNotifHistorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifHistorySize.setStatus("mandatory")
_MitelNotifHistoryTable_Object = MibTable
mitelNotifHistoryTable = _MitelNotifHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 7)
)
if mibBuilder.loadTexts:
    mitelNotifHistoryTable.setStatus("mandatory")
_MitelNotifHistoryTableEntry_Object = MibTableRow
mitelNotifHistoryTableEntry = _MitelNotifHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1)
)
mitelNotifHistoryTableEntry.setIndexNames(
    (0, "MITEL-MIB", "mitelNotifHistTblIndex"),
)
if mibBuilder.loadTexts:
    mitelNotifHistoryTableEntry.setStatus("mandatory")
_MitelNotifHistTblIndex_Type = Integer32
_MitelNotifHistTblIndex_Object = MibTableColumn
mitelNotifHistTblIndex = _MitelNotifHistTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 1),
    _MitelNotifHistTblIndex_Type()
)
mitelNotifHistTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifHistTblIndex.setStatus("mandatory")
_MitelNotifHistTblId_Type = Integer32
_MitelNotifHistTblId_Object = MibTableColumn
mitelNotifHistTblId = _MitelNotifHistTblId_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 2),
    _MitelNotifHistTblId_Type()
)
mitelNotifHistTblId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifHistTblId.setStatus("mandatory")
_MitelNotifHistTblTime_Type = TimeStamp
_MitelNotifHistTblTime_Object = MibTableColumn
mitelNotifHistTblTime = _MitelNotifHistTblTime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 3),
    _MitelNotifHistTblTime_Type()
)
mitelNotifHistTblTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifHistTblTime.setStatus("mandatory")
_MitelNotifHistTblIfIndex_Type = InterfaceIndex
_MitelNotifHistTblIfIndex_Object = MibTableColumn
mitelNotifHistTblIfIndex = _MitelNotifHistTblIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 4),
    _MitelNotifHistTblIfIndex_Type()
)
mitelNotifHistTblIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifHistTblIfIndex.setStatus("mandatory")
_MitelNotifHistTblConfirmed_Type = TruthValue
_MitelNotifHistTblConfirmed_Object = MibTableColumn
mitelNotifHistTblConfirmed = _MitelNotifHistTblConfirmed_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 7, 1, 5),
    _MitelNotifHistTblConfirmed_Type()
)
mitelNotifHistTblConfirmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifHistTblConfirmed.setStatus("mandatory")
_MitelNotifUnackTable_Object = MibTable
mitelNotifUnackTable = _MitelNotifUnackTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 8)
)
if mibBuilder.loadTexts:
    mitelNotifUnackTable.setStatus("mandatory")
_MitelNotifUnackTableEntry_Object = MibTableRow
mitelNotifUnackTableEntry = _MitelNotifUnackTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1)
)
mitelNotifUnackTableEntry.setIndexNames(
    (0, "MITEL-MIB", "mitelNotifUnackTblIndex"),
)
if mibBuilder.loadTexts:
    mitelNotifUnackTableEntry.setStatus("mandatory")
_MitelNotifUnackTblIndex_Type = Integer32
_MitelNotifUnackTblIndex_Object = MibTableColumn
mitelNotifUnackTblIndex = _MitelNotifUnackTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 1),
    _MitelNotifUnackTblIndex_Type()
)
mitelNotifUnackTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifUnackTblIndex.setStatus("mandatory")


class _MitelNotifUnackTblStatus_Type(Integer32):
    """Custom type mitelNotifUnackTblStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destory", 6),
          ("notInService", 2))
    )


_MitelNotifUnackTblStatus_Type.__name__ = "Integer32"
_MitelNotifUnackTblStatus_Object = MibTableColumn
mitelNotifUnackTblStatus = _MitelNotifUnackTblStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 2),
    _MitelNotifUnackTblStatus_Type()
)
mitelNotifUnackTblStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNotifUnackTblStatus.setStatus("mandatory")
_MitelNotifUnackTblHistory_Type = Integer32
_MitelNotifUnackTblHistory_Object = MibTableColumn
mitelNotifUnackTblHistory = _MitelNotifUnackTblHistory_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 3),
    _MitelNotifUnackTblHistory_Type()
)
mitelNotifUnackTblHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifUnackTblHistory.setStatus("mandatory")
_MitelNotifUnackTblManager_Type = Integer32
_MitelNotifUnackTblManager_Object = MibTableColumn
mitelNotifUnackTblManager = _MitelNotifUnackTblManager_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 4),
    _MitelNotifUnackTblManager_Type()
)
mitelNotifUnackTblManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifUnackTblManager.setStatus("mandatory")
_MitelNotifUnackTblRetriesLeft_Type = Integer32
_MitelNotifUnackTblRetriesLeft_Object = MibTableColumn
mitelNotifUnackTblRetriesLeft = _MitelNotifUnackTblRetriesLeft_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 8, 1, 5),
    _MitelNotifUnackTblRetriesLeft_Type()
)
mitelNotifUnackTblRetriesLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifUnackTblRetriesLeft.setStatus("mandatory")
_MitelNotifAgentAddress_Type = TAddress
_MitelNotifAgentAddress_Object = MibScalar
mitelNotifAgentAddress = _MitelNotifAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 9),
    _MitelNotifAgentAddress_Type()
)
mitelNotifAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNotifAgentAddress.setStatus("mandatory")
_MitelPropReset_ObjectIdentity = ObjectIdentity
mitelPropReset = _MitelPropReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 7)
)


class _MitelResetReason_Type(Integer32):
    """Custom type mitelResetReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldStart", 2),
          ("shutdown", 1),
          ("warmStart", 3))
    )


_MitelResetReason_Type.__name__ = "Integer32"
_MitelResetReason_Object = MibScalar
mitelResetReason = _MitelResetReason_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 7, 1),
    _MitelResetReason_Type()
)
mitelResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelResetReason.setStatus("mandatory")
_MitelResetPlatform_Type = TruthValue
_MitelResetPlatform_Object = MibScalar
mitelResetPlatform = _MitelResetPlatform_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 7, 2),
    _MitelResetPlatform_Type()
)
mitelResetPlatform.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelResetPlatform.setStatus("mandatory")
_MitelResetAgent_Type = TruthValue
_MitelResetAgent_Object = MibScalar
mitelResetAgent = _MitelResetAgent_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 7, 3),
    _MitelResetAgent_Type()
)
mitelResetAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelResetAgent.setStatus("mandatory")
_MitelConformance_ObjectIdentity = ObjectIdentity
mitelConformance = _MitelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5)
)
_MitelConfCompliances_ObjectIdentity = ObjectIdentity
mitelConfCompliances = _MitelConfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 1)
)
_MitelComplMitel_ObjectIdentity = ObjectIdentity
mitelComplMitel = _MitelComplMitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 1, 1)
)
_MitelConfGroups_ObjectIdentity = ObjectIdentity
mitelConfGroups = _MitelConfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2)
)
_MitelGrpCommon_ObjectIdentity = ObjectIdentity
mitelGrpCommon = _MitelGrpCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 1)
)
_MitelGrpCmnNotifBasic_ObjectIdentity = ObjectIdentity
mitelGrpCmnNotifBasic = _MitelGrpCmnNotifBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 2)
)
_MitelGrpCmnNotifManagers_ObjectIdentity = ObjectIdentity
mitelGrpCmnNotifManagers = _MitelGrpCmnNotifManagers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 3)
)
_MitelGrpCmnNotifHistory_ObjectIdentity = ObjectIdentity
mitelGrpCmnNotifHistory = _MitelGrpCmnNotifHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 4)
)
_MitelGrpCmnNotifAck_ObjectIdentity = ObjectIdentity
mitelGrpCmnNotifAck = _MitelGrpCmnNotifAck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 5)
)
_MitelGrpCmnInterfaces_ObjectIdentity = ObjectIdentity
mitelGrpCmnInterfaces = _MitelGrpCmnInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 6)
)
_MitelGrpCmnReset_ObjectIdentity = ObjectIdentity
mitelGrpCmnReset = _MitelGrpCmnReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 7)
)
_MitelGrpOpsMgr_ObjectIdentity = ObjectIdentity
mitelGrpOpsMgr = _MitelGrpOpsMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 2)
)
_MitelGrpCs2000_ObjectIdentity = ObjectIdentity
mitelGrpCs2000 = _MitelGrpCs2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 3)
)
_MitelConfAgents_ObjectIdentity = ObjectIdentity
mitelConfAgents = _MitelConfAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 3)
)
_SnmpV2_ObjectIdentity = ObjectIdentity
snmpV2 = _SnmpV2_ObjectIdentity(
    (1, 3, 6, 1, 6)
)
_SnmpDomains_ObjectIdentity = ObjectIdentity
snmpDomains = _SnmpDomains_ObjectIdentity(
    (1, 3, 6, 1, 6, 1)
)
_SnmpUDPDomain_ObjectIdentity = ObjectIdentity
snmpUDPDomain = _SnmpUDPDomain_ObjectIdentity(
    (1, 3, 6, 1, 6, 1, 1)
)

# Managed Objects groups


# Notification objects

mitelTrapsCommLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 1, 0, 1)
)
mitelTrapsCommLost.setObjects(
      *(("MITEL-MIB", "mitelNotifUnackTblStatus"),
        ("MITEL-MIB", "mitelNotifMgrTblDomain"),
        ("MITEL-MIB", "mitelNotifMgrTblAddress"))
)
if mibBuilder.loadTexts:
    mitelTrapsCommLost.setStatus(
        ""
    )

mitelTrapsReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 1027, 4, 6, 1, 0, 2)
)
mitelTrapsReset.setObjects(
      *(("MITEL-MIB", "mitelNotifUnackTblStatus"),
        ("MITEL-MIB", "mitelResetReason"))
)
if mibBuilder.loadTexts:
    mitelTrapsReset.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "TruthValue": TruthValue,
       "RowStatus": RowStatus,
       "TimeStamp": TimeStamp,
       "TimeInterval": TimeInterval,
       "TDomain": TDomain,
       "TAddress": TAddress,
       "MitelIfType": MitelIfType,
       "MitelNotifyTransportType": MitelNotifyTransportType,
       "mitel": mitel,
       "mitelIdentification": mitelIdentification,
       "mitelIdMgmtPlatforms": mitelIdMgmtPlatforms,
       "mitelIdMgmtOpsMgr": mitelIdMgmtOpsMgr,
       "mitelIdCallServers": mitelIdCallServers,
       "mitelIdCsMc2": mitelIdCsMc2,
       "mitelIdCs2000Light": mitelIdCs2000Light,
       "mitelIdTerminals": mitelIdTerminals,
       "mitelIdInterfaces": mitelIdInterfaces,
       "mitelIdCtiPlatforms": mitelIdCtiPlatforms,
       "mitelExperimental": mitelExperimental,
       "mitelExtensions": mitelExtensions,
       "mitelExtInterfaces": mitelExtInterfaces,
       "mitelIfNumber": mitelIfNumber,
       "mitelIfTable": mitelIfTable,
       "mitelIfTableEntry": mitelIfTableEntry,
       "mitelIfTblType": mitelIfTblType,
       "mitelProprietary": mitelProprietary,
       "mitelPropApplications": mitelPropApplications,
       "mitelAppCallServer": mitelAppCallServer,
       "mitelPropTransmission": mitelPropTransmission,
       "mitelPropProtocols": mitelPropProtocols,
       "mitelPropUtilities": mitelPropUtilities,
       "mitelPropHardware": mitelPropHardware,
       "mitelPropNotifications": mitelPropNotifications,
       "mitelNotifTraps": mitelNotifTraps,
       "mitelTrapsCommLost": mitelTrapsCommLost,
       "mitelTrapsReset": mitelTrapsReset,
       "mitelNotifCount": mitelNotifCount,
       "mitelNotifEnableTable": mitelNotifEnableTable,
       "mitelNotifEnableTableEntry": mitelNotifEnableTableEntry,
       "mitelNotifEnblTblIndex": mitelNotifEnblTblIndex,
       "mitelNotifEnblTblOid": mitelNotifEnblTblOid,
       "mitelNotifEnblTblEnable": mitelNotifEnblTblEnable,
       "mitelNotifEnblTblAck": mitelNotifEnblTblAck,
       "mitelNotifEnblTblOccurrences": mitelNotifEnblTblOccurrences,
       "mitelNotifEnblTblDescr": mitelNotifEnblTblDescr,
       "mitelNotifManagerTable": mitelNotifManagerTable,
       "mitelNotifManagerTableEntry": mitelNotifManagerTableEntry,
       "mitelNotifMgrTblIndex": mitelNotifMgrTblIndex,
       "mitelNotifMgrTblStatus": mitelNotifMgrTblStatus,
       "mitelNotifMgrTblTransport": mitelNotifMgrTblTransport,
       "mitelNotifMgrTblDomain": mitelNotifMgrTblDomain,
       "mitelNotifMgrTblAddress": mitelNotifMgrTblAddress,
       "mitelNotifMgrTblTimeout": mitelNotifMgrTblTimeout,
       "mitelNotifMgrTblRetries": mitelNotifMgrTblRetries,
       "mitelNotifMgrTblLife": mitelNotifMgrTblLife,
       "mitelNotifMgrTblCommunity": mitelNotifMgrTblCommunity,
       "mitelNotifMgrTblName": mitelNotifMgrTblName,
       "mitelNotifHistoryMax": mitelNotifHistoryMax,
       "mitelNotifHistorySize": mitelNotifHistorySize,
       "mitelNotifHistoryTable": mitelNotifHistoryTable,
       "mitelNotifHistoryTableEntry": mitelNotifHistoryTableEntry,
       "mitelNotifHistTblIndex": mitelNotifHistTblIndex,
       "mitelNotifHistTblId": mitelNotifHistTblId,
       "mitelNotifHistTblTime": mitelNotifHistTblTime,
       "mitelNotifHistTblIfIndex": mitelNotifHistTblIfIndex,
       "mitelNotifHistTblConfirmed": mitelNotifHistTblConfirmed,
       "mitelNotifUnackTable": mitelNotifUnackTable,
       "mitelNotifUnackTableEntry": mitelNotifUnackTableEntry,
       "mitelNotifUnackTblIndex": mitelNotifUnackTblIndex,
       "mitelNotifUnackTblStatus": mitelNotifUnackTblStatus,
       "mitelNotifUnackTblHistory": mitelNotifUnackTblHistory,
       "mitelNotifUnackTblManager": mitelNotifUnackTblManager,
       "mitelNotifUnackTblRetriesLeft": mitelNotifUnackTblRetriesLeft,
       "mitelNotifAgentAddress": mitelNotifAgentAddress,
       "mitelPropReset": mitelPropReset,
       "mitelResetReason": mitelResetReason,
       "mitelResetPlatform": mitelResetPlatform,
       "mitelResetAgent": mitelResetAgent,
       "mitelConformance": mitelConformance,
       "mitelConfCompliances": mitelConfCompliances,
       "mitelComplMitel": mitelComplMitel,
       "mitelConfGroups": mitelConfGroups,
       "mitelGrpCommon": mitelGrpCommon,
       "mitelGrpCmnNotifBasic": mitelGrpCmnNotifBasic,
       "mitelGrpCmnNotifManagers": mitelGrpCmnNotifManagers,
       "mitelGrpCmnNotifHistory": mitelGrpCmnNotifHistory,
       "mitelGrpCmnNotifAck": mitelGrpCmnNotifAck,
       "mitelGrpCmnInterfaces": mitelGrpCmnInterfaces,
       "mitelGrpCmnReset": mitelGrpCmnReset,
       "mitelGrpOpsMgr": mitelGrpOpsMgr,
       "mitelGrpCs2000": mitelGrpCs2000,
       "mitelConfAgents": mitelConfAgents,
       "snmpV2": snmpV2,
       "snmpDomains": snmpDomains,
       "snmpUDPDomain": snmpUDPDomain}
)
