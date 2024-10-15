# SNMP MIB module (CISCO-CDSTV-FSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDSTV-FSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:17 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoCdstvFsiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 735)
)
ciscoCdstvFsiMIB.setRevisions(
        ("2010-05-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCdstvFsiMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCdstvFsiMIBNotifs = _CiscoCdstvFsiMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 0)
)
_CiscoCdstvFsiMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCdstvFsiMIBObjects = _CiscoCdstvFsiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 1)
)
_CdstvFsiIpAddressType_Type = InetAddressType
_CdstvFsiIpAddressType_Object = MibScalar
cdstvFsiIpAddressType = _CdstvFsiIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 1, 1),
    _CdstvFsiIpAddressType_Type()
)
cdstvFsiIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvFsiIpAddressType.setStatus("current")
_CdstvFsiIpAddress_Type = InetAddress
_CdstvFsiIpAddress_Object = MibScalar
cdstvFsiIpAddress = _CdstvFsiIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 1, 2),
    _CdstvFsiIpAddress_Type()
)
cdstvFsiIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvFsiIpAddress.setStatus("current")
_CdstvFsiServerPort_Type = InetPortNumber
_CdstvFsiServerPort_Object = MibScalar
cdstvFsiServerPort = _CdstvFsiServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 1, 3),
    _CdstvFsiServerPort_Type()
)
cdstvFsiServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvFsiServerPort.setStatus("current")
_CdstvFsiFtpClientPort_Type = InetPortNumber
_CdstvFsiFtpClientPort_Object = MibScalar
cdstvFsiFtpClientPort = _CdstvFsiFtpClientPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 1, 4),
    _CdstvFsiFtpClientPort_Type()
)
cdstvFsiFtpClientPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvFsiFtpClientPort.setStatus("current")
_CdstvFsiFtpOutServerPort_Type = InetPortNumber
_CdstvFsiFtpOutServerPort_Object = MibScalar
cdstvFsiFtpOutServerPort = _CdstvFsiFtpOutServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 1, 5),
    _CdstvFsiFtpOutServerPort_Type()
)
cdstvFsiFtpOutServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvFsiFtpOutServerPort.setStatus("current")
_CdstvFsiFtpOutLoginTTL_Type = Unsigned32
_CdstvFsiFtpOutLoginTTL_Object = MibScalar
cdstvFsiFtpOutLoginTTL = _CdstvFsiFtpOutLoginTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 1, 6),
    _CdstvFsiFtpOutLoginTTL_Type()
)
cdstvFsiFtpOutLoginTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvFsiFtpOutLoginTTL.setStatus("current")
if mibBuilder.loadTexts:
    cdstvFsiFtpOutLoginTTL.setUnits("hops")


class _CdstvFsiLogLevel_Type(Integer32):
    """Custom type cdstvFsiLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 2),
          ("off", 1))
    )


_CdstvFsiLogLevel_Type.__name__ = "Integer32"
_CdstvFsiLogLevel_Object = MibScalar
cdstvFsiLogLevel = _CdstvFsiLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 1, 7),
    _CdstvFsiLogLevel_Type()
)
cdstvFsiLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvFsiLogLevel.setStatus("current")
_CdstvFsiContentRootPath_Type = SnmpAdminString
_CdstvFsiContentRootPath_Object = MibScalar
cdstvFsiContentRootPath = _CdstvFsiContentRootPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 1, 8),
    _CdstvFsiContentRootPath_Type()
)
cdstvFsiContentRootPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvFsiContentRootPath.setStatus("current")
_CdstvFsiAsyncCallbackURL_Type = CiscoURLString
_CdstvFsiAsyncCallbackURL_Object = MibScalar
cdstvFsiAsyncCallbackURL = _CdstvFsiAsyncCallbackURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 1, 9),
    _CdstvFsiAsyncCallbackURL_Type()
)
cdstvFsiAsyncCallbackURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvFsiAsyncCallbackURL.setStatus("current")
_CiscoCdstvFsiMIBConform_ObjectIdentity = ObjectIdentity
ciscoCdstvFsiMIBConform = _CiscoCdstvFsiMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 2)
)
_CiscoCdstvFsiMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCdstvFsiMIBCompliances = _CiscoCdstvFsiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 2, 1)
)
_CiscoCdstvFsiMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCdstvFsiMIBGroups = _CiscoCdstvFsiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 2, 2)
)

# Managed Objects groups

ciscoCdstvFsiMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 2, 2, 1)
)
ciscoCdstvFsiMIBMainObjectGroup.setObjects(
      *(("CISCO-CDSTV-FSI-MIB", "cdstvFsiIpAddress"),
        ("CISCO-CDSTV-FSI-MIB", "cdstvFsiServerPort"),
        ("CISCO-CDSTV-FSI-MIB", "cdstvFsiFtpClientPort"),
        ("CISCO-CDSTV-FSI-MIB", "cdstvFsiFtpOutServerPort"),
        ("CISCO-CDSTV-FSI-MIB", "cdstvFsiFtpOutLoginTTL"),
        ("CISCO-CDSTV-FSI-MIB", "cdstvFsiLogLevel"),
        ("CISCO-CDSTV-FSI-MIB", "cdstvFsiContentRootPath"),
        ("CISCO-CDSTV-FSI-MIB", "cdstvFsiAsyncCallbackURL"),
        ("CISCO-CDSTV-FSI-MIB", "cdstvFsiIpAddressType"))
)
if mibBuilder.loadTexts:
    ciscoCdstvFsiMIBMainObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCdstvFsiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 735, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCdstvFsiMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDSTV-FSI-MIB",
    **{"ciscoCdstvFsiMIB": ciscoCdstvFsiMIB,
       "ciscoCdstvFsiMIBNotifs": ciscoCdstvFsiMIBNotifs,
       "ciscoCdstvFsiMIBObjects": ciscoCdstvFsiMIBObjects,
       "cdstvFsiIpAddressType": cdstvFsiIpAddressType,
       "cdstvFsiIpAddress": cdstvFsiIpAddress,
       "cdstvFsiServerPort": cdstvFsiServerPort,
       "cdstvFsiFtpClientPort": cdstvFsiFtpClientPort,
       "cdstvFsiFtpOutServerPort": cdstvFsiFtpOutServerPort,
       "cdstvFsiFtpOutLoginTTL": cdstvFsiFtpOutLoginTTL,
       "cdstvFsiLogLevel": cdstvFsiLogLevel,
       "cdstvFsiContentRootPath": cdstvFsiContentRootPath,
       "cdstvFsiAsyncCallbackURL": cdstvFsiAsyncCallbackURL,
       "ciscoCdstvFsiMIBConform": ciscoCdstvFsiMIBConform,
       "ciscoCdstvFsiMIBCompliances": ciscoCdstvFsiMIBCompliances,
       "ciscoCdstvFsiMIBCompliance": ciscoCdstvFsiMIBCompliance,
       "ciscoCdstvFsiMIBGroups": ciscoCdstvFsiMIBGroups,
       "ciscoCdstvFsiMIBMainObjectGroup": ciscoCdstvFsiMIBMainObjectGroup}
)
