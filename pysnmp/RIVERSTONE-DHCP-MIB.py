# SNMP MIB module (RIVERSTONE-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:44 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RIVERSTONE-SMI-MIB",
    "riverstoneMibs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50)
)
rsDhcpMIB.setRevisions(
        ("2002-09-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RsErrorCode(Integer32, TextualConvention):
    status = "current"
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
        *(("commandCompleted", 6),
          ("internalError", 7),
          ("invalidConfig", 5),
          ("networkError", 3),
          ("noSpace", 4),
          ("noStatus", 1),
          ("tftpServerError", 8),
          ("timeout", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RsDhcpNotifications_ObjectIdentity = ObjectIdentity
rsDhcpNotifications = _RsDhcpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 0)
)
if mibBuilder.loadTexts:
    rsDhcpNotifications.setStatus("current")
_RsDhcpConformance_ObjectIdentity = ObjectIdentity
rsDhcpConformance = _RsDhcpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 3)
)
_RsDhcpCompliances_ObjectIdentity = ObjectIdentity
rsDhcpCompliances = _RsDhcpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 3, 1)
)
_RsDhcpGroups_ObjectIdentity = ObjectIdentity
rsDhcpGroups = _RsDhcpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 3, 2)
)
_RsDhcpLeaseFileGroup_ObjectIdentity = ObjectIdentity
rsDhcpLeaseFileGroup = _RsDhcpLeaseFileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 5)
)
if mibBuilder.loadTexts:
    rsDhcpLeaseFileGroup.setStatus("current")


class _RsDhcpLeaseFileTransferOp_Type(Integer32):
    """Custom type rsDhcpLeaseFileTransferOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("receiveLeaseFileFromAgent", 3),
          ("sendLeaseFileToAgent", 2))
    )


_RsDhcpLeaseFileTransferOp_Type.__name__ = "Integer32"
_RsDhcpLeaseFileTransferOp_Object = MibScalar
rsDhcpLeaseFileTransferOp = _RsDhcpLeaseFileTransferOp_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 5, 1),
    _RsDhcpLeaseFileTransferOp_Type()
)
rsDhcpLeaseFileTransferOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDhcpLeaseFileTransferOp.setStatus("current")


class _RsDhcpLeaseFileManagerAddressType_Type(InetAddressType):
    """Custom type rsDhcpLeaseFileManagerAddressType based on InetAddressType"""


_RsDhcpLeaseFileManagerAddressType_Object = MibScalar
rsDhcpLeaseFileManagerAddressType = _RsDhcpLeaseFileManagerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 5, 2),
    _RsDhcpLeaseFileManagerAddressType_Type()
)
rsDhcpLeaseFileManagerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDhcpLeaseFileManagerAddressType.setStatus("current")
_RsDhcpLeaseFileManagerAddress_Type = InetAddress
_RsDhcpLeaseFileManagerAddress_Object = MibScalar
rsDhcpLeaseFileManagerAddress = _RsDhcpLeaseFileManagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 5, 3),
    _RsDhcpLeaseFileManagerAddress_Type()
)
rsDhcpLeaseFileManagerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDhcpLeaseFileManagerAddress.setStatus("current")
_RsDhcpLeaseFileFileName_Type = DisplayString
_RsDhcpLeaseFileFileName_Object = MibScalar
rsDhcpLeaseFileFileName = _RsDhcpLeaseFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 5, 4),
    _RsDhcpLeaseFileFileName_Type()
)
rsDhcpLeaseFileFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDhcpLeaseFileFileName.setStatus("current")
_RsDhcpLeaseFileActivateTransfer_Type = TruthValue
_RsDhcpLeaseFileActivateTransfer_Object = MibScalar
rsDhcpLeaseFileActivateTransfer = _RsDhcpLeaseFileActivateTransfer_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 5, 5),
    _RsDhcpLeaseFileActivateTransfer_Type()
)
rsDhcpLeaseFileActivateTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDhcpLeaseFileActivateTransfer.setStatus("current")


class _RsDhcpLeaseFileTransferStatus_Type(Integer32):
    """Custom type rsDhcpLeaseFileTransferStatus based on Integer32"""
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
        *(("error", 5),
          ("idle", 1),
          ("receiving", 3),
          ("sending", 2),
          ("transferComplete", 4))
    )


_RsDhcpLeaseFileTransferStatus_Type.__name__ = "Integer32"
_RsDhcpLeaseFileTransferStatus_Object = MibScalar
rsDhcpLeaseFileTransferStatus = _RsDhcpLeaseFileTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 5, 6),
    _RsDhcpLeaseFileTransferStatus_Type()
)
rsDhcpLeaseFileTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDhcpLeaseFileTransferStatus.setStatus("current")
_RsDhcpLeaseFileLastError_Type = RsErrorCode
_RsDhcpLeaseFileLastError_Object = MibScalar
rsDhcpLeaseFileLastError = _RsDhcpLeaseFileLastError_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 5, 7),
    _RsDhcpLeaseFileLastError_Type()
)
rsDhcpLeaseFileLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDhcpLeaseFileLastError.setStatus("current")
_RsDhcpLeaseFileLastErrorReason_Type = DisplayString
_RsDhcpLeaseFileLastErrorReason_Object = MibScalar
rsDhcpLeaseFileLastErrorReason = _RsDhcpLeaseFileLastErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 5, 8),
    _RsDhcpLeaseFileLastErrorReason_Type()
)
rsDhcpLeaseFileLastErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDhcpLeaseFileLastErrorReason.setStatus("current")
_RsDhcpConfigGroup_ObjectIdentity = ObjectIdentity
rsDhcpConfigGroup = _RsDhcpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 10)
)
if mibBuilder.loadTexts:
    rsDhcpConfigGroup.setStatus("current")
_RsDhcpStatisticsGroup_ObjectIdentity = ObjectIdentity
rsDhcpStatisticsGroup = _RsDhcpStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 15)
)
if mibBuilder.loadTexts:
    rsDhcpStatisticsGroup.setStatus("current")
_RsDhcpMaxClientsAllowed_Type = Integer32
_RsDhcpMaxClientsAllowed_Object = MibScalar
rsDhcpMaxClientsAllowed = _RsDhcpMaxClientsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 15, 1),
    _RsDhcpMaxClientsAllowed_Type()
)
rsDhcpMaxClientsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDhcpMaxClientsAllowed.setStatus("current")
_RsDhcpNumberOfClients_Type = Integer32
_RsDhcpNumberOfClients_Object = MibScalar
rsDhcpNumberOfClients = _RsDhcpNumberOfClients_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 15, 2),
    _RsDhcpNumberOfClients_Type()
)
rsDhcpNumberOfClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDhcpNumberOfClients.setStatus("current")

# Managed Objects groups

rsDhcpGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 3, 2, 1)
)
rsDhcpGroup1.setObjects(
      *(("RIVERSTONE-DHCP-MIB", "rsDhcpLeaseFileTransferOp"),
        ("RIVERSTONE-DHCP-MIB", "rsDhcpLeaseFileManagerAddressType"),
        ("RIVERSTONE-DHCP-MIB", "rsDhcpLeaseFileManagerAddress"),
        ("RIVERSTONE-DHCP-MIB", "rsDhcpLeaseFileFileName"),
        ("RIVERSTONE-DHCP-MIB", "rsDhcpLeaseFileActivateTransfer"),
        ("RIVERSTONE-DHCP-MIB", "rsDhcpLeaseFileTransferStatus"),
        ("RIVERSTONE-DHCP-MIB", "rsDhcpLeaseFileLastError"),
        ("RIVERSTONE-DHCP-MIB", "rsDhcpLeaseFileLastErrorReason"))
)
if mibBuilder.loadTexts:
    rsDhcpGroup1.setStatus("current")

rsDhcpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 3, 2, 2)
)
rsDhcpGroup2.setObjects(
      *(("RIVERSTONE-DHCP-MIB", "rsDhcpMaxClientsAllowed"),
        ("RIVERSTONE-DHCP-MIB", "rsDhcpNumberOfClients"))
)
if mibBuilder.loadTexts:
    rsDhcpGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsDhcpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 50, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rsDhcpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-DHCP-MIB",
    **{"RsErrorCode": RsErrorCode,
       "rsDhcpMIB": rsDhcpMIB,
       "rsDhcpNotifications": rsDhcpNotifications,
       "rsDhcpConformance": rsDhcpConformance,
       "rsDhcpCompliances": rsDhcpCompliances,
       "rsDhcpCompliance": rsDhcpCompliance,
       "rsDhcpGroups": rsDhcpGroups,
       "rsDhcpGroup1": rsDhcpGroup1,
       "rsDhcpGroup2": rsDhcpGroup2,
       "rsDhcpLeaseFileGroup": rsDhcpLeaseFileGroup,
       "rsDhcpLeaseFileTransferOp": rsDhcpLeaseFileTransferOp,
       "rsDhcpLeaseFileManagerAddressType": rsDhcpLeaseFileManagerAddressType,
       "rsDhcpLeaseFileManagerAddress": rsDhcpLeaseFileManagerAddress,
       "rsDhcpLeaseFileFileName": rsDhcpLeaseFileFileName,
       "rsDhcpLeaseFileActivateTransfer": rsDhcpLeaseFileActivateTransfer,
       "rsDhcpLeaseFileTransferStatus": rsDhcpLeaseFileTransferStatus,
       "rsDhcpLeaseFileLastError": rsDhcpLeaseFileLastError,
       "rsDhcpLeaseFileLastErrorReason": rsDhcpLeaseFileLastErrorReason,
       "rsDhcpConfigGroup": rsDhcpConfigGroup,
       "rsDhcpStatisticsGroup": rsDhcpStatisticsGroup,
       "rsDhcpMaxClientsAllowed": rsDhcpMaxClientsAllowed,
       "rsDhcpNumberOfClients": rsDhcpNumberOfClients}
)
