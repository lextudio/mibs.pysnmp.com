# SNMP MIB module (ASCEND-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-SESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:42 2024
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

(sessionStatusGroup,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "sessionStatusGroup")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SsnStatusMaximumSessions_Type = Integer32
_SsnStatusMaximumSessions_Object = MibScalar
ssnStatusMaximumSessions = _SsnStatusMaximumSessions_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 1),
    _SsnStatusMaximumSessions_Type()
)
ssnStatusMaximumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnStatusMaximumSessions.setStatus("mandatory")
_SessionStatusTable_Object = MibTable
sessionStatusTable = _SessionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 2)
)
if mibBuilder.loadTexts:
    sessionStatusTable.setStatus("mandatory")
_SessionStatusEntry_Object = MibTableRow
sessionStatusEntry = _SessionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 2, 1)
)
sessionStatusEntry.setIndexNames(
    (0, "ASCEND-SESSION-MIB", "ssnStatusIndex"),
)
if mibBuilder.loadTexts:
    sessionStatusEntry.setStatus("mandatory")
_SsnStatusIndex_Type = Integer32
_SsnStatusIndex_Object = MibTableColumn
ssnStatusIndex = _SsnStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 1),
    _SsnStatusIndex_Type()
)
ssnStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnStatusIndex.setStatus("mandatory")


class _SsnStatusValidFlag_Type(Integer32):
    """Custom type ssnStatusValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_SsnStatusValidFlag_Type.__name__ = "Integer32"
_SsnStatusValidFlag_Object = MibTableColumn
ssnStatusValidFlag = _SsnStatusValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 2),
    _SsnStatusValidFlag_Type()
)
ssnStatusValidFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssnStatusValidFlag.setStatus("mandatory")
_SsnStatusUserName_Type = DisplayString
_SsnStatusUserName_Object = MibTableColumn
ssnStatusUserName = _SsnStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 3),
    _SsnStatusUserName_Type()
)
ssnStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnStatusUserName.setStatus("mandatory")
_SsnStatusUserIPAddress_Type = IpAddress
_SsnStatusUserIPAddress_Object = MibTableColumn
ssnStatusUserIPAddress = _SsnStatusUserIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 4),
    _SsnStatusUserIPAddress_Type()
)
ssnStatusUserIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnStatusUserIPAddress.setStatus("mandatory")
_SsnStatusUserSubnetMask_Type = IpAddress
_SsnStatusUserSubnetMask_Object = MibTableColumn
ssnStatusUserSubnetMask = _SsnStatusUserSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 5),
    _SsnStatusUserSubnetMask_Type()
)
ssnStatusUserSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnStatusUserSubnetMask.setStatus("mandatory")


class _SsnStatusCurrentService_Type(Integer32):
    """Custom type ssnStatusCurrentService based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("atm", 20),
          ("combinet", 7),
          ("dchannelX25", 17),
          ("dtpt", 18),
          ("euraw", 9),
          ("euui", 10),
          ("frameRelay", 8),
          ("hdlcNrm", 21),
          ("ipFax", 19),
          ("mp", 15),
          ("mpp", 5),
          ("netToNet", 25),
          ("none", 1),
          ("other", 2),
          ("ppp", 3),
          ("rawTcp", 13),
          ("slip", 4),
          ("telnet", 11),
          ("telnetBinary", 12),
          ("terminalServer", 14),
          ("virtualConnect", 16),
          ("visa2", 23),
          ("voip", 22),
          ("x25", 6))
    )


_SsnStatusCurrentService_Type.__name__ = "Integer32"
_SsnStatusCurrentService_Object = MibTableColumn
ssnStatusCurrentService = _SsnStatusCurrentService_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 6),
    _SsnStatusCurrentService_Type()
)
ssnStatusCurrentService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnStatusCurrentService.setStatus("mandatory")
_SsnStatusCallReferenceNum_Type = Integer32
_SsnStatusCallReferenceNum_Object = MibTableColumn
ssnStatusCallReferenceNum = _SsnStatusCallReferenceNum_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 7),
    _SsnStatusCallReferenceNum_Type()
)
ssnStatusCallReferenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnStatusCallReferenceNum.setStatus("mandatory")
_SessionActiveTable_Object = MibTable
sessionActiveTable = _SessionActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 3)
)
if mibBuilder.loadTexts:
    sessionActiveTable.setStatus("mandatory")
_SessionActiveEntry_Object = MibTableRow
sessionActiveEntry = _SessionActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 3, 1)
)
sessionActiveEntry.setIndexNames(
    (0, "ASCEND-SESSION-MIB", "ssnActiveCallReferenceNum"),
)
if mibBuilder.loadTexts:
    sessionActiveEntry.setStatus("mandatory")
_SsnActiveCallReferenceNum_Type = Integer32
_SsnActiveCallReferenceNum_Object = MibTableColumn
ssnActiveCallReferenceNum = _SsnActiveCallReferenceNum_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 1),
    _SsnActiveCallReferenceNum_Type()
)
ssnActiveCallReferenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnActiveCallReferenceNum.setStatus("mandatory")
_SsnActiveIndex_Type = Integer32
_SsnActiveIndex_Object = MibTableColumn
ssnActiveIndex = _SsnActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 2),
    _SsnActiveIndex_Type()
)
ssnActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnActiveIndex.setStatus("mandatory")


class _SsnActiveValidFlag_Type(Integer32):
    """Custom type ssnActiveValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_SsnActiveValidFlag_Type.__name__ = "Integer32"
_SsnActiveValidFlag_Object = MibTableColumn
ssnActiveValidFlag = _SsnActiveValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 3),
    _SsnActiveValidFlag_Type()
)
ssnActiveValidFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssnActiveValidFlag.setStatus("mandatory")
_SsnActiveUserName_Type = DisplayString
_SsnActiveUserName_Object = MibTableColumn
ssnActiveUserName = _SsnActiveUserName_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 4),
    _SsnActiveUserName_Type()
)
ssnActiveUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnActiveUserName.setStatus("mandatory")
_SsnActiveUserIPAddress_Type = IpAddress
_SsnActiveUserIPAddress_Object = MibTableColumn
ssnActiveUserIPAddress = _SsnActiveUserIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 5),
    _SsnActiveUserIPAddress_Type()
)
ssnActiveUserIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnActiveUserIPAddress.setStatus("mandatory")
_SsnActiveUserSubnetMask_Type = IpAddress
_SsnActiveUserSubnetMask_Object = MibTableColumn
ssnActiveUserSubnetMask = _SsnActiveUserSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 6),
    _SsnActiveUserSubnetMask_Type()
)
ssnActiveUserSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnActiveUserSubnetMask.setStatus("mandatory")


class _SsnActiveCurrentService_Type(Integer32):
    """Custom type ssnActiveCurrentService based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("atm", 20),
          ("combinet", 7),
          ("dchannelX25", 17),
          ("dtpt", 18),
          ("euraw", 9),
          ("euui", 10),
          ("frameRelay", 8),
          ("hdlcNrm", 21),
          ("ipFax", 19),
          ("mp", 15),
          ("mpp", 5),
          ("netToNet", 25),
          ("none", 1),
          ("other", 2),
          ("ppp", 3),
          ("rawTcp", 13),
          ("slip", 4),
          ("telnet", 11),
          ("telnetBinary", 12),
          ("terminalServer", 14),
          ("virtualConnect", 16),
          ("visa2", 23),
          ("voip", 22),
          ("x25", 6))
    )


_SsnActiveCurrentService_Type.__name__ = "Integer32"
_SsnActiveCurrentService_Object = MibTableColumn
ssnActiveCurrentService = _SsnActiveCurrentService_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 7),
    _SsnActiveCurrentService_Type()
)
ssnActiveCurrentService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnActiveCurrentService.setStatus("mandatory")
_SsnActiveIdleTime_Type = TimeTicks
_SsnActiveIdleTime_Object = MibTableColumn
ssnActiveIdleTime = _SsnActiveIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 8),
    _SsnActiveIdleTime_Type()
)
ssnActiveIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssnActiveIdleTime.setStatus("mandatory")
_MppActiveStatsTable_Object = MibTable
mppActiveStatsTable = _MppActiveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 4)
)
if mibBuilder.loadTexts:
    mppActiveStatsTable.setStatus("mandatory")
_MppActiveStatsEntry_Object = MibTableRow
mppActiveStatsEntry = _MppActiveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 4, 1)
)
mppActiveStatsEntry.setIndexNames(
    (0, "ASCEND-SESSION-MIB", "mppStatsMpID"),
)
if mibBuilder.loadTexts:
    mppActiveStatsEntry.setStatus("mandatory")
_MppStatsMpID_Type = Integer32
_MppStatsMpID_Object = MibTableColumn
mppStatsMpID = _MppStatsMpID_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 1),
    _MppStatsMpID_Type()
)
mppStatsMpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mppStatsMpID.setStatus("mandatory")
_MppStatsRemoteName_Type = DisplayString
_MppStatsRemoteName_Object = MibTableColumn
mppStatsRemoteName = _MppStatsRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 2),
    _MppStatsRemoteName_Type()
)
mppStatsRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mppStatsRemoteName.setStatus("mandatory")


class _MppStatsQuality_Type(Integer32):
    """Custom type mppStatsQuality based on Integer32"""
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
        *(("fair", 2),
          ("good", 1),
          ("marginal", 3),
          ("na", 5),
          ("poor", 4))
    )


_MppStatsQuality_Type.__name__ = "Integer32"
_MppStatsQuality_Object = MibTableColumn
mppStatsQuality = _MppStatsQuality_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 3),
    _MppStatsQuality_Type()
)
mppStatsQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mppStatsQuality.setStatus("mandatory")
_MppStatsBandwidth_Type = Integer32
_MppStatsBandwidth_Object = MibTableColumn
mppStatsBandwidth = _MppStatsBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 4),
    _MppStatsBandwidth_Type()
)
mppStatsBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mppStatsBandwidth.setStatus("mandatory")
_MppStatsTotalChannels_Type = Integer32
_MppStatsTotalChannels_Object = MibTableColumn
mppStatsTotalChannels = _MppStatsTotalChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 5),
    _MppStatsTotalChannels_Type()
)
mppStatsTotalChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mppStatsTotalChannels.setStatus("mandatory")
_MppStatsCLU_Type = Integer32
_MppStatsCLU_Object = MibTableColumn
mppStatsCLU = _MppStatsCLU_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 6),
    _MppStatsCLU_Type()
)
mppStatsCLU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mppStatsCLU.setStatus("mandatory")
_MppStatsALU_Type = Integer32
_MppStatsALU_Object = MibTableColumn
mppStatsALU = _MppStatsALU_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 7),
    _MppStatsALU_Type()
)
mppStatsALU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mppStatsALU.setStatus("mandatory")
_MppStatsStartingTimeStamp_Type = Integer32
_MppStatsStartingTimeStamp_Object = MibTableColumn
mppStatsStartingTimeStamp = _MppStatsStartingTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 8),
    _MppStatsStartingTimeStamp_Type()
)
mppStatsStartingTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mppStatsStartingTimeStamp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-SESSION-MIB",
    **{"DisplayString": DisplayString,
       "ssnStatusMaximumSessions": ssnStatusMaximumSessions,
       "sessionStatusTable": sessionStatusTable,
       "sessionStatusEntry": sessionStatusEntry,
       "ssnStatusIndex": ssnStatusIndex,
       "ssnStatusValidFlag": ssnStatusValidFlag,
       "ssnStatusUserName": ssnStatusUserName,
       "ssnStatusUserIPAddress": ssnStatusUserIPAddress,
       "ssnStatusUserSubnetMask": ssnStatusUserSubnetMask,
       "ssnStatusCurrentService": ssnStatusCurrentService,
       "ssnStatusCallReferenceNum": ssnStatusCallReferenceNum,
       "sessionActiveTable": sessionActiveTable,
       "sessionActiveEntry": sessionActiveEntry,
       "ssnActiveCallReferenceNum": ssnActiveCallReferenceNum,
       "ssnActiveIndex": ssnActiveIndex,
       "ssnActiveValidFlag": ssnActiveValidFlag,
       "ssnActiveUserName": ssnActiveUserName,
       "ssnActiveUserIPAddress": ssnActiveUserIPAddress,
       "ssnActiveUserSubnetMask": ssnActiveUserSubnetMask,
       "ssnActiveCurrentService": ssnActiveCurrentService,
       "ssnActiveIdleTime": ssnActiveIdleTime,
       "mppActiveStatsTable": mppActiveStatsTable,
       "mppActiveStatsEntry": mppActiveStatsEntry,
       "mppStatsMpID": mppStatsMpID,
       "mppStatsRemoteName": mppStatsRemoteName,
       "mppStatsQuality": mppStatsQuality,
       "mppStatsBandwidth": mppStatsBandwidth,
       "mppStatsTotalChannels": mppStatsTotalChannels,
       "mppStatsCLU": mppStatsCLU,
       "mppStatsALU": mppStatsALU,
       "mppStatsStartingTimeStamp": mppStatsStartingTimeStamp}
)
