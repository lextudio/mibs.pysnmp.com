# SNMP MIB module (WS-INFRA-AUTO-UPDATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WS-INFRA-AUTO-UPDATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:24 2024
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

(wsInfraAutoUpdate,) = mibBuilder.importSymbols(
    "WS-INFRA-SMI-MIB",
    "wsInfraAutoUpdate")

(DoActionNow,) = mibBuilder.importSymbols(
    "WS-TYPE-MIB",
    "DoActionNow")


# MODULE-IDENTITY

wsInfraAutoUpdateModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1)
)
wsInfraAutoUpdateModule.setRevisions(
        ("2007-05-02 15:56",
         "2007-01-22 17:34",
         "2006-10-07 15:17",
         "2006-08-11 16:34",
         "2006-08-09 15:40")
)


# Types definitions



class DoActionState(Integer32):
    """Custom type DoActionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("inProgress", 3),
          ("success", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsInfraAutoUpdateTable_Object = MibTable
wsInfraAutoUpdateTable = _WsInfraAutoUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    wsInfraAutoUpdateTable.setStatus("current")
_WsInfraAutoUpdateEntry_Object = MibTableRow
wsInfraAutoUpdateEntry = _WsInfraAutoUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 1, 1)
)
wsInfraAutoUpdateEntry.setIndexNames(
    (0, "WS-INFRA-AUTO-UPDATE-MIB", "wsInfraAutoUpdateIndex"),
)
if mibBuilder.loadTexts:
    wsInfraAutoUpdateEntry.setStatus("current")


class _WsInfraAutoUpdateIndex_Type(Unsigned32):
    """Custom type wsInfraAutoUpdateIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WsInfraAutoUpdateIndex_Type.__name__ = "Unsigned32"
_WsInfraAutoUpdateIndex_Object = MibTableColumn
wsInfraAutoUpdateIndex = _WsInfraAutoUpdateIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 1, 1, 1),
    _WsInfraAutoUpdateIndex_Type()
)
wsInfraAutoUpdateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraAutoUpdateIndex.setStatus("current")
_WsInfraAutoUpdateEnableUpdate_Type = TruthValue
_WsInfraAutoUpdateEnableUpdate_Object = MibTableColumn
wsInfraAutoUpdateEnableUpdate = _WsInfraAutoUpdateEnableUpdate_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 1, 1, 2),
    _WsInfraAutoUpdateEnableUpdate_Type()
)
wsInfraAutoUpdateEnableUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraAutoUpdateEnableUpdate.setStatus("current")


class _WsInfraAutoUpdateFileLoc_Type(DisplayString):
    """Custom type wsInfraAutoUpdateFileLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WsInfraAutoUpdateFileLoc_Type.__name__ = "DisplayString"
_WsInfraAutoUpdateFileLoc_Object = MibTableColumn
wsInfraAutoUpdateFileLoc = _WsInfraAutoUpdateFileLoc_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 1, 1, 3),
    _WsInfraAutoUpdateFileLoc_Type()
)
wsInfraAutoUpdateFileLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraAutoUpdateFileLoc.setStatus("current")
_WsInfraAutoUpdateSvrIpAddr_Type = IpAddress
_WsInfraAutoUpdateSvrIpAddr_Object = MibTableColumn
wsInfraAutoUpdateSvrIpAddr = _WsInfraAutoUpdateSvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 1, 1, 4),
    _WsInfraAutoUpdateSvrIpAddr_Type()
)
wsInfraAutoUpdateSvrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraAutoUpdateSvrIpAddr.setStatus("current")


class _WsInfraAutoUpdateSvrProtocol_Type(Integer32):
    """Custom type wsInfraAutoUpdateSvrProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("cf", 11),
          ("flash", 4),
          ("ftp", 9),
          ("http", 8),
          ("tftp", 10),
          ("unset", 0),
          ("usb1", 12),
          ("usb2", 13))
    )


_WsInfraAutoUpdateSvrProtocol_Type.__name__ = "Integer32"
_WsInfraAutoUpdateSvrProtocol_Object = MibTableColumn
wsInfraAutoUpdateSvrProtocol = _WsInfraAutoUpdateSvrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 1, 1, 5),
    _WsInfraAutoUpdateSvrProtocol_Type()
)
wsInfraAutoUpdateSvrProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraAutoUpdateSvrProtocol.setStatus("current")


class _WsInfraAutoUpdateSvrUsername_Type(DisplayString):
    """Custom type wsInfraAutoUpdateSvrUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_WsInfraAutoUpdateSvrUsername_Type.__name__ = "DisplayString"
_WsInfraAutoUpdateSvrUsername_Object = MibTableColumn
wsInfraAutoUpdateSvrUsername = _WsInfraAutoUpdateSvrUsername_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 1, 1, 6),
    _WsInfraAutoUpdateSvrUsername_Type()
)
wsInfraAutoUpdateSvrUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraAutoUpdateSvrUsername.setStatus("current")


class _WsInfraAutoUpdateSvrPassword_Type(DisplayString):
    """Custom type wsInfraAutoUpdateSvrPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_WsInfraAutoUpdateSvrPassword_Type.__name__ = "DisplayString"
_WsInfraAutoUpdateSvrPassword_Object = MibTableColumn
wsInfraAutoUpdateSvrPassword = _WsInfraAutoUpdateSvrPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 1, 1, 7),
    _WsInfraAutoUpdateSvrPassword_Type()
)
wsInfraAutoUpdateSvrPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraAutoUpdateSvrPassword.setStatus("current")
_WsInfraAutoUpdateRowStatus_Type = RowStatus
_WsInfraAutoUpdateRowStatus_Object = MibTableColumn
wsInfraAutoUpdateRowStatus = _WsInfraAutoUpdateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 1, 1, 8),
    _WsInfraAutoUpdateRowStatus_Type()
)
wsInfraAutoUpdateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraAutoUpdateRowStatus.setStatus("current")


class _WsInfraAutoUpdateImageFileVersion_Type(DisplayString):
    """Custom type wsInfraAutoUpdateImageFileVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_WsInfraAutoUpdateImageFileVersion_Type.__name__ = "DisplayString"
_WsInfraAutoUpdateImageFileVersion_Object = MibScalar
wsInfraAutoUpdateImageFileVersion = _WsInfraAutoUpdateImageFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 2),
    _WsInfraAutoUpdateImageFileVersion_Type()
)
wsInfraAutoUpdateImageFileVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraAutoUpdateImageFileVersion.setStatus("current")
_WsInfraAutoUpdateStart_Type = DoActionNow
_WsInfraAutoUpdateStart_Object = MibScalar
wsInfraAutoUpdateStart = _WsInfraAutoUpdateStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 3),
    _WsInfraAutoUpdateStart_Type()
)
wsInfraAutoUpdateStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraAutoUpdateStart.setStatus("current")
_WsInfraAutoUpdateMIBConformance_ObjectIdentity = ObjectIdentity
wsInfraAutoUpdateMIBConformance = _WsInfraAutoUpdateMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 100)
)
_WsInfraAutoUpdateMIBGroups_ObjectIdentity = ObjectIdentity
wsInfraAutoUpdateMIBGroups = _WsInfraAutoUpdateMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 100, 1)
)
_WsInfraAutoUpdateMIBCompliances_ObjectIdentity = ObjectIdentity
wsInfraAutoUpdateMIBCompliances = _WsInfraAutoUpdateMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 100, 2)
)

# Managed Objects groups

wsInfraAutoUpdateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 100, 1, 1)
)
wsInfraAutoUpdateGroup.setObjects(
      *(("WS-INFRA-AUTO-UPDATE-MIB", "wsInfraAutoUpdateIndex"),
        ("WS-INFRA-AUTO-UPDATE-MIB", "wsInfraAutoUpdateEnableUpdate"),
        ("WS-INFRA-AUTO-UPDATE-MIB", "wsInfraAutoUpdateFileLoc"),
        ("WS-INFRA-AUTO-UPDATE-MIB", "wsInfraAutoUpdateSvrIpAddr"),
        ("WS-INFRA-AUTO-UPDATE-MIB", "wsInfraAutoUpdateSvrProtocol"),
        ("WS-INFRA-AUTO-UPDATE-MIB", "wsInfraAutoUpdateSvrUsername"),
        ("WS-INFRA-AUTO-UPDATE-MIB", "wsInfraAutoUpdateSvrPassword"),
        ("WS-INFRA-AUTO-UPDATE-MIB", "wsInfraAutoUpdateStart"),
        ("WS-INFRA-AUTO-UPDATE-MIB", "wsInfraAutoUpdateImageFileVersion"),
        ("WS-INFRA-AUTO-UPDATE-MIB", "wsInfraAutoUpdateRowStatus"))
)
if mibBuilder.loadTexts:
    wsInfraAutoUpdateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wsInfraAutoUpdateMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11, 1, 100, 2, 1)
)
if mibBuilder.loadTexts:
    wsInfraAutoUpdateMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-INFRA-AUTO-UPDATE-MIB",
    **{"DoActionState": DoActionState,
       "wsInfraAutoUpdateModule": wsInfraAutoUpdateModule,
       "wsInfraAutoUpdateTable": wsInfraAutoUpdateTable,
       "wsInfraAutoUpdateEntry": wsInfraAutoUpdateEntry,
       "wsInfraAutoUpdateIndex": wsInfraAutoUpdateIndex,
       "wsInfraAutoUpdateEnableUpdate": wsInfraAutoUpdateEnableUpdate,
       "wsInfraAutoUpdateFileLoc": wsInfraAutoUpdateFileLoc,
       "wsInfraAutoUpdateSvrIpAddr": wsInfraAutoUpdateSvrIpAddr,
       "wsInfraAutoUpdateSvrProtocol": wsInfraAutoUpdateSvrProtocol,
       "wsInfraAutoUpdateSvrUsername": wsInfraAutoUpdateSvrUsername,
       "wsInfraAutoUpdateSvrPassword": wsInfraAutoUpdateSvrPassword,
       "wsInfraAutoUpdateRowStatus": wsInfraAutoUpdateRowStatus,
       "wsInfraAutoUpdateImageFileVersion": wsInfraAutoUpdateImageFileVersion,
       "wsInfraAutoUpdateStart": wsInfraAutoUpdateStart,
       "wsInfraAutoUpdateMIBConformance": wsInfraAutoUpdateMIBConformance,
       "wsInfraAutoUpdateMIBGroups": wsInfraAutoUpdateMIBGroups,
       "wsInfraAutoUpdateGroup": wsInfraAutoUpdateGroup,
       "wsInfraAutoUpdateMIBCompliances": wsInfraAutoUpdateMIBCompliances,
       "wsInfraAutoUpdateMibCompliance": wsInfraAutoUpdateMibCompliance}
)
