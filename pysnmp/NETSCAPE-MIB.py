# SNMP MIB module (NETSCAPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCAPE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:41 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Netscape_ObjectIdentity = ObjectIdentity
netscape = _Netscape_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1450)
)
_Http_ObjectIdentity = ObjectIdentity
http = _Http_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1450, 1)
)
_HttpEntityInfo_ObjectIdentity = ObjectIdentity
httpEntityInfo = _HttpEntityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1)
)
_HttpEntityTable_Object = MibTable
httpEntityTable = _HttpEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1)
)
if mibBuilder.loadTexts:
    httpEntityTable.setStatus("mandatory")
_HttpEntityEntry_Object = MibTableRow
httpEntityEntry = _HttpEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1)
)
httpEntityEntry.setIndexNames(
    (0, "NETSCAPE-MIB", "httpEntityPort"),
    (0, "NETSCAPE-MIB", "httpEntityAddress"),
)
if mibBuilder.loadTexts:
    httpEntityEntry.setStatus("mandatory")


class _HttpEntityDescr_Type(DisplayString):
    """Custom type httpEntityDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HttpEntityDescr_Type.__name__ = "DisplayString"
_HttpEntityDescr_Object = MibTableColumn
httpEntityDescr = _HttpEntityDescr_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 1),
    _HttpEntityDescr_Type()
)
httpEntityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityDescr.setStatus("mandatory")
_HttpEntityId_Type = ObjectIdentifier
_HttpEntityId_Object = MibTableColumn
httpEntityId = _HttpEntityId_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 2),
    _HttpEntityId_Type()
)
httpEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityId.setStatus("mandatory")
_HttpEntityProtocol_Type = DisplayString
_HttpEntityProtocol_Object = MibTableColumn
httpEntityProtocol = _HttpEntityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 3),
    _HttpEntityProtocol_Type()
)
httpEntityProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityProtocol.setStatus("mandatory")
_HttpEntityVersion_Type = DisplayString
_HttpEntityVersion_Object = MibTableColumn
httpEntityVersion = _HttpEntityVersion_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 4),
    _HttpEntityVersion_Type()
)
httpEntityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityVersion.setStatus("mandatory")


class _HttpEntityOrganization_Type(DisplayString):
    """Custom type httpEntityOrganization based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HttpEntityOrganization_Type.__name__ = "DisplayString"
_HttpEntityOrganization_Object = MibTableColumn
httpEntityOrganization = _HttpEntityOrganization_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 5),
    _HttpEntityOrganization_Type()
)
httpEntityOrganization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityOrganization.setStatus("mandatory")


class _HttpEntityLocation_Type(DisplayString):
    """Custom type httpEntityLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HttpEntityLocation_Type.__name__ = "DisplayString"
_HttpEntityLocation_Object = MibTableColumn
httpEntityLocation = _HttpEntityLocation_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 6),
    _HttpEntityLocation_Type()
)
httpEntityLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityLocation.setStatus("mandatory")


class _HttpEntityContact_Type(DisplayString):
    """Custom type httpEntityContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HttpEntityContact_Type.__name__ = "DisplayString"
_HttpEntityContact_Object = MibTableColumn
httpEntityContact = _HttpEntityContact_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 7),
    _HttpEntityContact_Type()
)
httpEntityContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityContact.setStatus("mandatory")
_HttpEntityAddress_Type = IpAddress
_HttpEntityAddress_Object = MibTableColumn
httpEntityAddress = _HttpEntityAddress_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 8),
    _HttpEntityAddress_Type()
)
httpEntityAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityAddress.setStatus("mandatory")
_HttpEntityPort_Type = Integer32
_HttpEntityPort_Object = MibTableColumn
httpEntityPort = _HttpEntityPort_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 9),
    _HttpEntityPort_Type()
)
httpEntityPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityPort.setStatus("mandatory")
_HttpEntityName_Type = DisplayString
_HttpEntityName_Object = MibTableColumn
httpEntityName = _HttpEntityName_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 10),
    _HttpEntityName_Type()
)
httpEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityName.setStatus("mandatory")
_HttpEntityType_Type = DisplayString
_HttpEntityType_Object = MibTableColumn
httpEntityType = _HttpEntityType_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 11),
    _HttpEntityType_Type()
)
httpEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityType.setStatus("mandatory")
_HttpEntityMethods_Type = DisplayString
_HttpEntityMethods_Object = MibTableColumn
httpEntityMethods = _HttpEntityMethods_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 12),
    _HttpEntityMethods_Type()
)
httpEntityMethods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityMethods.setStatus("mandatory")
_HttpEntityMaxProcess_Type = Integer32
_HttpEntityMaxProcess_Object = MibTableColumn
httpEntityMaxProcess = _HttpEntityMaxProcess_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 13),
    _HttpEntityMaxProcess_Type()
)
httpEntityMaxProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityMaxProcess.setStatus("mandatory")
_HttpEntityMinProcess_Type = Integer32
_HttpEntityMinProcess_Object = MibTableColumn
httpEntityMinProcess = _HttpEntityMinProcess_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 14),
    _HttpEntityMinProcess_Type()
)
httpEntityMinProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityMinProcess.setStatus("mandatory")
_HttpEntityMaxThread_Type = Integer32
_HttpEntityMaxThread_Object = MibTableColumn
httpEntityMaxThread = _HttpEntityMaxThread_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 15),
    _HttpEntityMaxThread_Type()
)
httpEntityMaxThread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityMaxThread.setStatus("mandatory")
_HttpEntityMinThread_Type = Integer32
_HttpEntityMinThread_Object = MibTableColumn
httpEntityMinThread = _HttpEntityMinThread_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 1, 1, 16),
    _HttpEntityMinThread_Type()
)
httpEntityMinThread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpEntityMinThread.setStatus("mandatory")
_HttpStatisticsTable_Object = MibTable
httpStatisticsTable = _HttpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 2)
)
if mibBuilder.loadTexts:
    httpStatisticsTable.setStatus("mandatory")
_HttpStatisticsEntry_Object = MibTableRow
httpStatisticsEntry = _HttpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 2, 1)
)
httpStatisticsEntry.setIndexNames(
    (0, "NETSCAPE-MIB", "httpStatisticsPort"),
    (0, "NETSCAPE-MIB", "httpStatisticsAddress"),
)
if mibBuilder.loadTexts:
    httpStatisticsEntry.setStatus("mandatory")
_HttpStatisticsPort_Type = Integer32
_HttpStatisticsPort_Object = MibTableColumn
httpStatisticsPort = _HttpStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 2, 1, 1),
    _HttpStatisticsPort_Type()
)
httpStatisticsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsPort.setStatus("mandatory")
_HttpStatisticsAddress_Type = IpAddress
_HttpStatisticsAddress_Object = MibTableColumn
httpStatisticsAddress = _HttpStatisticsAddress_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 2, 1, 2),
    _HttpStatisticsAddress_Type()
)
httpStatisticsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsAddress.setStatus("mandatory")
_HttpStatisticsStatus_Type = Integer32
_HttpStatisticsStatus_Object = MibTableColumn
httpStatisticsStatus = _HttpStatisticsStatus_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 2, 1, 3),
    _HttpStatisticsStatus_Type()
)
httpStatisticsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsStatus.setStatus("mandatory")
_HttpStatisticsUptime_Type = TimeTicks
_HttpStatisticsUptime_Object = MibTableColumn
httpStatisticsUptime = _HttpStatisticsUptime_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 2, 1, 4),
    _HttpStatisticsUptime_Type()
)
httpStatisticsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsUptime.setStatus("mandatory")
_HttpStatisticsNumProcessIdle_Type = Integer32
_HttpStatisticsNumProcessIdle_Object = MibTableColumn
httpStatisticsNumProcessIdle = _HttpStatisticsNumProcessIdle_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 2, 1, 5),
    _HttpStatisticsNumProcessIdle_Type()
)
httpStatisticsNumProcessIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsNumProcessIdle.setStatus("mandatory")
_HttpStatisticsNumProcessProc_Type = Integer32
_HttpStatisticsNumProcessProc_Object = MibTableColumn
httpStatisticsNumProcessProc = _HttpStatisticsNumProcessProc_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 2, 1, 6),
    _HttpStatisticsNumProcessProc_Type()
)
httpStatisticsNumProcessProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsNumProcessProc.setStatus("mandatory")
_HttpStatisticsNumProcessDns_Type = Integer32
_HttpStatisticsNumProcessDns_Object = MibTableColumn
httpStatisticsNumProcessDns = _HttpStatisticsNumProcessDns_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 2, 1, 7),
    _HttpStatisticsNumProcessDns_Type()
)
httpStatisticsNumProcessDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsNumProcessDns.setStatus("mandatory")
_HttpStatisticsRequests_Type = Counter32
_HttpStatisticsRequests_Object = MibTableColumn
httpStatisticsRequests = _HttpStatisticsRequests_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 2, 1, 8),
    _HttpStatisticsRequests_Type()
)
httpStatisticsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsRequests.setStatus("mandatory")
_HttpStatisticsRequestError_Type = Counter32
_HttpStatisticsRequestError_Object = MibTableColumn
httpStatisticsRequestError = _HttpStatisticsRequestError_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 2, 1, 9),
    _HttpStatisticsRequestError_Type()
)
httpStatisticsRequestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsRequestError.setStatus("mandatory")
_HttpStatisticsProcessNum_Type = Integer32
_HttpStatisticsProcessNum_Object = MibTableColumn
httpStatisticsProcessNum = _HttpStatisticsProcessNum_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 2, 1, 14),
    _HttpStatisticsProcessNum_Type()
)
httpStatisticsProcessNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsProcessNum.setStatus("mandatory")
_HttpStatisticsThreadNum_Type = Integer32
_HttpStatisticsThreadNum_Object = MibTableColumn
httpStatisticsThreadNum = _HttpStatisticsThreadNum_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 2, 1, 15),
    _HttpStatisticsThreadNum_Type()
)
httpStatisticsThreadNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsThreadNum.setStatus("mandatory")
_HttpNTStatisticsTable_Object = MibTable
httpNTStatisticsTable = _HttpNTStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 3)
)
if mibBuilder.loadTexts:
    httpNTStatisticsTable.setStatus("mandatory")
_HttpNTStatisticsEntry_Object = MibTableRow
httpNTStatisticsEntry = _HttpNTStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 3, 1)
)
httpNTStatisticsEntry.setIndexNames(
    (0, "NETSCAPE-MIB", "httpStatisticsPort"),
    (0, "NETSCAPE-MIB", "httpStatisticsAddress"),
)
if mibBuilder.loadTexts:
    httpNTStatisticsEntry.setStatus("mandatory")
_HttpStatisticsNumBytes_Type = Counter32
_HttpStatisticsNumBytes_Object = MibTableColumn
httpStatisticsNumBytes = _HttpStatisticsNumBytes_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 3, 1, 1),
    _HttpStatisticsNumBytes_Type()
)
httpStatisticsNumBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsNumBytes.setStatus("mandatory")
_HttpStatisticsNum2xx_Type = Counter32
_HttpStatisticsNum2xx_Object = MibTableColumn
httpStatisticsNum2xx = _HttpStatisticsNum2xx_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 3, 1, 2),
    _HttpStatisticsNum2xx_Type()
)
httpStatisticsNum2xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsNum2xx.setStatus("mandatory")
_HttpStatisticsNum3xx_Type = Counter32
_HttpStatisticsNum3xx_Object = MibTableColumn
httpStatisticsNum3xx = _HttpStatisticsNum3xx_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 3, 1, 3),
    _HttpStatisticsNum3xx_Type()
)
httpStatisticsNum3xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsNum3xx.setStatus("mandatory")
_HttpStatisticsNum4xx_Type = Counter32
_HttpStatisticsNum4xx_Object = MibTableColumn
httpStatisticsNum4xx = _HttpStatisticsNum4xx_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 3, 1, 4),
    _HttpStatisticsNum4xx_Type()
)
httpStatisticsNum4xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsNum4xx.setStatus("mandatory")
_HttpStatisticsNum5xx_Type = Counter32
_HttpStatisticsNum5xx_Object = MibTableColumn
httpStatisticsNum5xx = _HttpStatisticsNum5xx_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 3, 1, 5),
    _HttpStatisticsNum5xx_Type()
)
httpStatisticsNum5xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsNum5xx.setStatus("mandatory")
_HttpStatisticsNum200_Type = Counter32
_HttpStatisticsNum200_Object = MibTableColumn
httpStatisticsNum200 = _HttpStatisticsNum200_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 3, 1, 6),
    _HttpStatisticsNum200_Type()
)
httpStatisticsNum200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsNum200.setStatus("mandatory")
_HttpStatisticsNum302_Type = Counter32
_HttpStatisticsNum302_Object = MibTableColumn
httpStatisticsNum302 = _HttpStatisticsNum302_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 3, 1, 7),
    _HttpStatisticsNum302_Type()
)
httpStatisticsNum302.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsNum302.setStatus("mandatory")
_HttpStatisticsNum304_Type = Counter32
_HttpStatisticsNum304_Object = MibTableColumn
httpStatisticsNum304 = _HttpStatisticsNum304_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 3, 1, 8),
    _HttpStatisticsNum304_Type()
)
httpStatisticsNum304.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsNum304.setStatus("mandatory")
_HttpStatisticsNum401_Type = Counter32
_HttpStatisticsNum401_Object = MibTableColumn
httpStatisticsNum401 = _HttpStatisticsNum401_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 3, 1, 9),
    _HttpStatisticsNum401_Type()
)
httpStatisticsNum401.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsNum401.setStatus("mandatory")
_HttpStatisticsNum403_Type = Counter32
_HttpStatisticsNum403_Object = MibTableColumn
httpStatisticsNum403 = _HttpStatisticsNum403_Object(
    (1, 3, 6, 1, 4, 1, 1450, 1, 1, 3, 1, 10),
    _HttpStatisticsNum403_Type()
)
httpStatisticsNum403.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpStatisticsNum403.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCAPE-MIB",
    **{"netscape": netscape,
       "http": http,
       "httpEntityInfo": httpEntityInfo,
       "httpEntityTable": httpEntityTable,
       "httpEntityEntry": httpEntityEntry,
       "httpEntityDescr": httpEntityDescr,
       "httpEntityId": httpEntityId,
       "httpEntityProtocol": httpEntityProtocol,
       "httpEntityVersion": httpEntityVersion,
       "httpEntityOrganization": httpEntityOrganization,
       "httpEntityLocation": httpEntityLocation,
       "httpEntityContact": httpEntityContact,
       "httpEntityAddress": httpEntityAddress,
       "httpEntityPort": httpEntityPort,
       "httpEntityName": httpEntityName,
       "httpEntityType": httpEntityType,
       "httpEntityMethods": httpEntityMethods,
       "httpEntityMaxProcess": httpEntityMaxProcess,
       "httpEntityMinProcess": httpEntityMinProcess,
       "httpEntityMaxThread": httpEntityMaxThread,
       "httpEntityMinThread": httpEntityMinThread,
       "httpStatisticsTable": httpStatisticsTable,
       "httpStatisticsEntry": httpStatisticsEntry,
       "httpStatisticsPort": httpStatisticsPort,
       "httpStatisticsAddress": httpStatisticsAddress,
       "httpStatisticsStatus": httpStatisticsStatus,
       "httpStatisticsUptime": httpStatisticsUptime,
       "httpStatisticsNumProcessIdle": httpStatisticsNumProcessIdle,
       "httpStatisticsNumProcessProc": httpStatisticsNumProcessProc,
       "httpStatisticsNumProcessDns": httpStatisticsNumProcessDns,
       "httpStatisticsRequests": httpStatisticsRequests,
       "httpStatisticsRequestError": httpStatisticsRequestError,
       "httpStatisticsProcessNum": httpStatisticsProcessNum,
       "httpStatisticsThreadNum": httpStatisticsThreadNum,
       "httpNTStatisticsTable": httpNTStatisticsTable,
       "httpNTStatisticsEntry": httpNTStatisticsEntry,
       "httpStatisticsNumBytes": httpStatisticsNumBytes,
       "httpStatisticsNum2xx": httpStatisticsNum2xx,
       "httpStatisticsNum3xx": httpStatisticsNum3xx,
       "httpStatisticsNum4xx": httpStatisticsNum4xx,
       "httpStatisticsNum5xx": httpStatisticsNum5xx,
       "httpStatisticsNum200": httpStatisticsNum200,
       "httpStatisticsNum302": httpStatisticsNum302,
       "httpStatisticsNum304": httpStatisticsNum304,
       "httpStatisticsNum401": httpStatisticsNum401,
       "httpStatisticsNum403": httpStatisticsNum403}
)
