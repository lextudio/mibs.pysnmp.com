# SNMP MIB module (EXTREME-AUTOPROVISION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-AUTOPROVISION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:19 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeAutoProvision = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40)
)
extremeAutoProvision.setRevisions(
        ("2010-06-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeAutoProvisionGeneral_ObjectIdentity = ObjectIdentity
extremeAutoProvisionGeneral = _ExtremeAutoProvisionGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 1)
)
_ExtremeAutoProvisionConfig_Type = TruthValue
_ExtremeAutoProvisionConfig_Object = MibScalar
extremeAutoProvisionConfig = _ExtremeAutoProvisionConfig_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 1, 1),
    _ExtremeAutoProvisionConfig_Type()
)
extremeAutoProvisionConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAutoProvisionConfig.setStatus("current")
_ExtremeAutoProvisionNotificationObjects_ObjectIdentity = ObjectIdentity
extremeAutoProvisionNotificationObjects = _ExtremeAutoProvisionNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 2)
)


class _ExtremeAutoProvisionResult_Type(Integer32):
    """Custom type extremeAutoProvisionResult based on Integer32"""
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
        *(("fileNotExist", 3),
          ("invalidConfigFileExtension", 1),
          ("success", 4),
          ("tftpUnReachable", 2))
    )


_ExtremeAutoProvisionResult_Type.__name__ = "Integer32"
_ExtremeAutoProvisionResult_Object = MibScalar
extremeAutoProvisionResult = _ExtremeAutoProvisionResult_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 1),
    _ExtremeAutoProvisionResult_Type()
)
extremeAutoProvisionResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeAutoProvisionResult.setStatus("current")
_ExtremeAutoProvisionIpAddress_Type = IpAddress
_ExtremeAutoProvisionIpAddress_Object = MibScalar
extremeAutoProvisionIpAddress = _ExtremeAutoProvisionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 2),
    _ExtremeAutoProvisionIpAddress_Type()
)
extremeAutoProvisionIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeAutoProvisionIpAddress.setStatus("current")
_ExtremeAutoProvisionGateway_Type = IpAddress
_ExtremeAutoProvisionGateway_Object = MibScalar
extremeAutoProvisionGateway = _ExtremeAutoProvisionGateway_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 3),
    _ExtremeAutoProvisionGateway_Type()
)
extremeAutoProvisionGateway.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeAutoProvisionGateway.setStatus("current")
_ExtremeAutoProvisionTFTPServer_Type = IpAddress
_ExtremeAutoProvisionTFTPServer_Object = MibScalar
extremeAutoProvisionTFTPServer = _ExtremeAutoProvisionTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 4),
    _ExtremeAutoProvisionTFTPServer_Type()
)
extremeAutoProvisionTFTPServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeAutoProvisionTFTPServer.setStatus("current")
_ExtremeAutoProvisionConfigFileName_Type = DisplayString
_ExtremeAutoProvisionConfigFileName_Object = MibScalar
extremeAutoProvisionConfigFileName = _ExtremeAutoProvisionConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 5),
    _ExtremeAutoProvisionConfigFileName_Type()
)
extremeAutoProvisionConfigFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeAutoProvisionConfigFileName.setStatus("current")
_ExtremeAutoProvisionNotification_ObjectIdentity = ObjectIdentity
extremeAutoProvisionNotification = _ExtremeAutoProvisionNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 3)
)
_ExtremeAutoProvisionTrapPrefix_ObjectIdentity = ObjectIdentity
extremeAutoProvisionTrapPrefix = _ExtremeAutoProvisionTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 3, 0)
)

# Managed Objects groups


# Notification objects

extremeAutoProvisionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40, 3, 0, 1)
)
extremeAutoProvisionStatus.setObjects(
      *(("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionResult"),
        ("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionIpAddress"),
        ("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionGateway"),
        ("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionTFTPServer"),
        ("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionConfigFileName"))
)
if mibBuilder.loadTexts:
    extremeAutoProvisionStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-AUTOPROVISION-MIB",
    **{"extremeAutoProvision": extremeAutoProvision,
       "extremeAutoProvisionGeneral": extremeAutoProvisionGeneral,
       "extremeAutoProvisionConfig": extremeAutoProvisionConfig,
       "extremeAutoProvisionNotificationObjects": extremeAutoProvisionNotificationObjects,
       "extremeAutoProvisionResult": extremeAutoProvisionResult,
       "extremeAutoProvisionIpAddress": extremeAutoProvisionIpAddress,
       "extremeAutoProvisionGateway": extremeAutoProvisionGateway,
       "extremeAutoProvisionTFTPServer": extremeAutoProvisionTFTPServer,
       "extremeAutoProvisionConfigFileName": extremeAutoProvisionConfigFileName,
       "extremeAutoProvisionNotification": extremeAutoProvisionNotification,
       "extremeAutoProvisionTrapPrefix": extremeAutoProvisionTrapPrefix,
       "extremeAutoProvisionStatus": extremeAutoProvisionStatus}
)
