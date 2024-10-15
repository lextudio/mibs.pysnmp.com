# SNMP MIB module (Novell-LANtern-Admin-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Novell-LANtern-Admin-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:27 2024
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
 NotificationType,
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
    "NotificationType",
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



class Time(Integer32):
    """Custom type Time based on Integer32"""




class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class Seconds(Integer32):
    """Custom type Seconds based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_ProductType_ObjectIdentity = ObjectIdentity
productType = _ProductType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 1)
)
_NetworkMonitor_ObjectIdentity = ObjectIdentity
networkMonitor = _NetworkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 1, 1)
)
_EthernetLANtern_ObjectIdentity = ObjectIdentity
ethernetLANtern = _EthernetLANtern_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 1, 1, 1)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_Lantern_ObjectIdentity = ObjectIdentity
lantern = _Lantern_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 1)
)
_LanternAdmin_ObjectIdentity = ObjectIdentity
lanternAdmin = _LanternAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1)
)
_AdminIdentification_Type = DisplayString
_AdminIdentification_Object = MibScalar
adminIdentification = _AdminIdentification_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 1),
    _AdminIdentification_Type()
)
adminIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminIdentification.setStatus("mandatory")
_AdminDateAndTime_Type = Time
_AdminDateAndTime_Object = MibScalar
adminDateAndTime = _AdminDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 2),
    _AdminDateAndTime_Type()
)
adminDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminDateAndTime.setStatus("mandatory")
_AdminTimeZone_Type = DisplayString
_AdminTimeZone_Object = MibScalar
adminTimeZone = _AdminTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 3),
    _AdminTimeZone_Type()
)
adminTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminTimeZone.setStatus("mandatory")
_AdminPowerOnTime_Type = Time
_AdminPowerOnTime_Object = MibScalar
adminPowerOnTime = _AdminPowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 4),
    _AdminPowerOnTime_Type()
)
adminPowerOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminPowerOnTime.setStatus("mandatory")
_AdminPowerOffTime_Type = Time
_AdminPowerOffTime_Object = MibScalar
adminPowerOffTime = _AdminPowerOffTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 5),
    _AdminPowerOffTime_Type()
)
adminPowerOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminPowerOffTime.setStatus("mandatory")


class _AdminNetworkDataLink_Type(Integer32):
    """Custom type adminNetworkDataLink based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethernetDIX", 1)
    )


_AdminNetworkDataLink_Type.__name__ = "Integer32"
_AdminNetworkDataLink_Object = MibScalar
adminNetworkDataLink = _AdminNetworkDataLink_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 6),
    _AdminNetworkDataLink_Type()
)
adminNetworkDataLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNetworkDataLink.setStatus("mandatory")


class _AdminNetworkIPAddr_Type(IpAddress):
    """Custom type adminNetworkIPAddr based on IpAddress"""
    defaultHexValue = "c044cd01"


_AdminNetworkIPAddr_Object = MibScalar
adminNetworkIPAddr = _AdminNetworkIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 7),
    _AdminNetworkIPAddr_Type()
)
adminNetworkIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNetworkIPAddr.setStatus("mandatory")


class _AdminNetworkSubnetMask_Type(IpAddress):
    """Custom type adminNetworkSubnetMask based on IpAddress"""
    defaultHexValue = "ffffff80"


_AdminNetworkSubnetMask_Object = MibScalar
adminNetworkSubnetMask = _AdminNetworkSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 8),
    _AdminNetworkSubnetMask_Type()
)
adminNetworkSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNetworkSubnetMask.setStatus("mandatory")


class _AdminNetworkGateway_Type(IpAddress):
    """Custom type adminNetworkGateway based on IpAddress"""
    defaultHexValue = "00000000"


_AdminNetworkGateway_Object = MibScalar
adminNetworkGateway = _AdminNetworkGateway_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 9),
    _AdminNetworkGateway_Type()
)
adminNetworkGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNetworkGateway.setStatus("mandatory")
_AdminClientTable_Object = MibTable
adminClientTable = _AdminClientTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 10)
)
if mibBuilder.loadTexts:
    adminClientTable.setStatus("mandatory")
_AdminClientEntry_Object = MibTableRow
adminClientEntry = _AdminClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 10, 1)
)
adminClientEntry.setIndexNames(
    (0, "Novell-LANtern-Admin-MIB", "adminClientIPAddr"),
)
if mibBuilder.loadTexts:
    adminClientEntry.setStatus("mandatory")
_AdminClientIPAddr_Type = IpAddress
_AdminClientIPAddr_Object = MibTableColumn
adminClientIPAddr = _AdminClientIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 10, 1, 1),
    _AdminClientIPAddr_Type()
)
adminClientIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminClientIPAddr.setStatus("mandatory")


class _AdminClientIPMask_Type(IpAddress):
    """Custom type adminClientIPMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AdminClientIPMask_Object = MibTableColumn
adminClientIPMask = _AdminClientIPMask_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 10, 1, 2),
    _AdminClientIPMask_Type()
)
adminClientIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminClientIPMask.setStatus("mandatory")


class _AdminClientCommunities_Type(Integer32):
    """Custom type adminClientCommunities based on Integer32"""
    defaultValue = 4


_AdminClientCommunities_Object = MibTableColumn
adminClientCommunities = _AdminClientCommunities_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 10, 1, 3),
    _AdminClientCommunities_Type()
)
adminClientCommunities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminClientCommunities.setStatus("mandatory")
_AdminClientDelete_Type = Integer32
_AdminClientDelete_Object = MibTableColumn
adminClientDelete = _AdminClientDelete_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 10, 1, 4),
    _AdminClientDelete_Type()
)
adminClientDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    adminClientDelete.setStatus("mandatory")
_AdminUnauthorizedIPAddr_Type = IpAddress
_AdminUnauthorizedIPAddr_Object = MibScalar
adminUnauthorizedIPAddr = _AdminUnauthorizedIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 11),
    _AdminUnauthorizedIPAddr_Type()
)
adminUnauthorizedIPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adminUnauthorizedIPAddr.setStatus("mandatory")
_AdminUnauthorizedCommunity_Type = OctetString
_AdminUnauthorizedCommunity_Object = MibScalar
adminUnauthorizedCommunity = _AdminUnauthorizedCommunity_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 12),
    _AdminUnauthorizedCommunity_Type()
)
adminUnauthorizedCommunity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adminUnauthorizedCommunity.setStatus("mandatory")
_AdminNotificationTable_Object = MibTable
adminNotificationTable = _AdminNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 13)
)
if mibBuilder.loadTexts:
    adminNotificationTable.setStatus("mandatory")
_AdminNotificationEntry_Object = MibTableRow
adminNotificationEntry = _AdminNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 13, 1)
)
adminNotificationEntry.setIndexNames(
    (0, "Novell-LANtern-Admin-MIB", "adminNotificationIPAddr"),
)
if mibBuilder.loadTexts:
    adminNotificationEntry.setStatus("mandatory")
_AdminNotificationIPAddr_Type = IpAddress
_AdminNotificationIPAddr_Object = MibTableColumn
adminNotificationIPAddr = _AdminNotificationIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 13, 1, 1),
    _AdminNotificationIPAddr_Type()
)
adminNotificationIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminNotificationIPAddr.setStatus("mandatory")


class _AdminNotificationStatus_Type(Integer32):
    """Custom type adminNotificationStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backupContact", 2),
          ("primaryContact", 1))
    )


_AdminNotificationStatus_Type.__name__ = "Integer32"
_AdminNotificationStatus_Object = MibTableColumn
adminNotificationStatus = _AdminNotificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 13, 1, 2),
    _AdminNotificationStatus_Type()
)
adminNotificationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNotificationStatus.setStatus("mandatory")


class _AdminNotificationTrapMask_Type(Integer32):
    """Custom type adminNotificationTrapMask based on Integer32"""
    defaultValue = 0


_AdminNotificationTrapMask_Object = MibTableColumn
adminNotificationTrapMask = _AdminNotificationTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 13, 1, 3),
    _AdminNotificationTrapMask_Type()
)
adminNotificationTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNotificationTrapMask.setStatus("mandatory")


class _AdminNotificationConfirmMask_Type(Integer32):
    """Custom type adminNotificationConfirmMask based on Integer32"""
    defaultValue = 0


_AdminNotificationConfirmMask_Object = MibTableColumn
adminNotificationConfirmMask = _AdminNotificationConfirmMask_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 13, 1, 4),
    _AdminNotificationConfirmMask_Type()
)
adminNotificationConfirmMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNotificationConfirmMask.setStatus("mandatory")


class _AdminNotificationTimeout_Type(Seconds):
    """Custom type adminNotificationTimeout based on Seconds"""
    defaultValue = 10


_AdminNotificationTimeout_Object = MibTableColumn
adminNotificationTimeout = _AdminNotificationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 13, 1, 5),
    _AdminNotificationTimeout_Type()
)
adminNotificationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNotificationTimeout.setStatus("mandatory")


class _AdminNotificationRetries_Type(Integer32):
    """Custom type adminNotificationRetries based on Integer32"""
    defaultValue = 2


_AdminNotificationRetries_Object = MibTableColumn
adminNotificationRetries = _AdminNotificationRetries_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 13, 1, 6),
    _AdminNotificationRetries_Type()
)
adminNotificationRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNotificationRetries.setStatus("mandatory")


class _AdminNotificationBackupIPAddr_Type(IpAddress):
    """Custom type adminNotificationBackupIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AdminNotificationBackupIPAddr_Object = MibTableColumn
adminNotificationBackupIPAddr = _AdminNotificationBackupIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 13, 1, 7),
    _AdminNotificationBackupIPAddr_Type()
)
adminNotificationBackupIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNotificationBackupIPAddr.setStatus("mandatory")
_AdminNotificationDelete_Type = Integer32
_AdminNotificationDelete_Object = MibTableColumn
adminNotificationDelete = _AdminNotificationDelete_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 13, 1, 8),
    _AdminNotificationDelete_Type()
)
adminNotificationDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    adminNotificationDelete.setStatus("mandatory")
_AdminTrapHandle_Type = Integer32
_AdminTrapHandle_Object = MibScalar
adminTrapHandle = _AdminTrapHandle_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 14),
    _AdminTrapHandle_Type()
)
adminTrapHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adminTrapHandle.setStatus("mandatory")
_AdminTrapAcknowledge_Type = Integer32
_AdminTrapAcknowledge_Object = MibScalar
adminTrapAcknowledge = _AdminTrapAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 15),
    _AdminTrapAcknowledge_Type()
)
adminTrapAcknowledge.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    adminTrapAcknowledge.setStatus("mandatory")
_AdminDownLoadFile_Type = OctetString
_AdminDownLoadFile_Object = MibScalar
adminDownLoadFile = _AdminDownLoadFile_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 16),
    _AdminDownLoadFile_Type()
)
adminDownLoadFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminDownLoadFile.setStatus("mandatory")
_AdminDownLoadServer_Type = IpAddress
_AdminDownLoadServer_Object = MibScalar
adminDownLoadServer = _AdminDownLoadServer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 17),
    _AdminDownLoadServer_Type()
)
adminDownLoadServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminDownLoadServer.setStatus("mandatory")


class _AdminDownload_Type(Integer32):
    """Custom type adminDownload based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("badFile", 5),
          ("downloadSuccess", 3),
          ("permanentChange", 2),
          ("temporaryChange", 1),
          ("tftpAccessViolation", 8),
          ("tftpFailed", 4),
          ("tftpFileNotFound", 7),
          ("tftpIllegalOperation", 10),
          ("tftpUndefined", 6),
          ("tftpUnknownTransferID", 11))
    )


_AdminDownload_Type.__name__ = "Integer32"
_AdminDownload_Object = MibScalar
adminDownload = _AdminDownload_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 18),
    _AdminDownload_Type()
)
adminDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminDownload.setStatus("mandatory")


class _AdminReset_Type(Integer32):
    """Custom type adminReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coldRestart", 1),
          ("warmRestart", 2))
    )


_AdminReset_Type.__name__ = "Integer32"
_AdminReset_Object = MibScalar
adminReset = _AdminReset_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 19),
    _AdminReset_Type()
)
adminReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    adminReset.setStatus("mandatory")


class _AdminSerialDataLink_Type(Integer32):
    """Custom type adminSerialDataLink based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("slip", 1)
    )


_AdminSerialDataLink_Type.__name__ = "Integer32"
_AdminSerialDataLink_Object = MibScalar
adminSerialDataLink = _AdminSerialDataLink_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 20),
    _AdminSerialDataLink_Type()
)
adminSerialDataLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSerialDataLink.setStatus("mandatory")


class _AdminSerialIPAddr_Type(IpAddress):
    """Custom type adminSerialIPAddr based on IpAddress"""
    defaultHexValue = "c044cd81"


_AdminSerialIPAddr_Object = MibScalar
adminSerialIPAddr = _AdminSerialIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 21),
    _AdminSerialIPAddr_Type()
)
adminSerialIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSerialIPAddr.setStatus("mandatory")


class _AdminSerialSubnetMask_Type(IpAddress):
    """Custom type adminSerialSubnetMask based on IpAddress"""
    defaultHexValue = "ffffff80"


_AdminSerialSubnetMask_Object = MibScalar
adminSerialSubnetMask = _AdminSerialSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 22),
    _AdminSerialSubnetMask_Type()
)
adminSerialSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSerialSubnetMask.setStatus("mandatory")


class _AdminSerialBaudRate_Type(Integer32):
    """Custom type adminSerialBaudRate based on Integer32"""
    defaultValue = 3

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
        *(("baud1200", 2),
          ("baud19200", 7),
          ("baud2400", 3),
          ("baud300", 1),
          ("baud38400", 8),
          ("baud4800", 4),
          ("baud7200", 5),
          ("baud9600", 6))
    )


_AdminSerialBaudRate_Type.__name__ = "Integer32"
_AdminSerialBaudRate_Object = MibScalar
adminSerialBaudRate = _AdminSerialBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 23),
    _AdminSerialBaudRate_Type()
)
adminSerialBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSerialBaudRate.setStatus("mandatory")


class _AdminSerialTimeout_Type(Seconds):
    """Custom type adminSerialTimeout based on Seconds"""
    defaultValue = 60


_AdminSerialTimeout_Object = MibScalar
adminSerialTimeout = _AdminSerialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 24),
    _AdminSerialTimeout_Type()
)
adminSerialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSerialTimeout.setStatus("mandatory")


class _AdminSerialConnection_Type(Integer32):
    """Custom type adminSerialConnection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 2),
          ("modem", 1))
    )


_AdminSerialConnection_Type.__name__ = "Integer32"
_AdminSerialConnection_Object = MibScalar
adminSerialConnection = _AdminSerialConnection_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 25),
    _AdminSerialConnection_Type()
)
adminSerialConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSerialConnection.setStatus("mandatory")


class _AdminSerialFlowControl_Type(Integer32):
    """Custom type adminSerialFlowControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rts-cts", 2))
    )


_AdminSerialFlowControl_Type.__name__ = "Integer32"
_AdminSerialFlowControl_Object = MibScalar
adminSerialFlowControl = _AdminSerialFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 26),
    _AdminSerialFlowControl_Type()
)
adminSerialFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSerialFlowControl.setStatus("mandatory")


class _AdminModemControl_Type(OctetString):
    """Custom type adminModemControl based on OctetString"""
    defaultValue = OctetString("""\
#^ATS0=1 Q0 V1 X4 &S1 &D2^M^1AT &W0
                     &Y0^M#^1ATDT#^2+++^2ATH0^M#""")


_AdminModemControl_Object = MibScalar
adminModemControl = _AdminModemControl_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 27),
    _AdminModemControl_Type()
)
adminModemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminModemControl.setStatus("mandatory")


class _AdminModemConnect_Type(OctetString):
    """Custom type adminModemConnect based on OctetString"""
    defaultValue = OctetString("""\
#19200#CONNECT 19200#9600#CONNECT
                     9600#4800#CONNECT 4800#2400#CONNECT
                     2400#1200#CONNECT 1200#300#CONNECT#""")


_AdminModemConnect_Object = MibScalar
adminModemConnect = _AdminModemConnect_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 28),
    _AdminModemConnect_Type()
)
adminModemConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminModemConnect.setStatus("mandatory")


class _AdminModemNoConnect_Type(OctetString):
    """Custom type adminModemNoConnect based on OctetString"""
    defaultValue = OctetString("#NO DIALTONE#NO CARRIER#BUSY#VOICE#TIMEOUT#")


_AdminModemNoConnect_Object = MibScalar
adminModemNoConnect = _AdminModemNoConnect_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 29),
    _AdminModemNoConnect_Type()
)
adminModemNoConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminModemNoConnect.setStatus("mandatory")


class _AdminGatewayControl_Type(Integer32):
    """Custom type adminGatewayControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gateway-off", 1),
          ("gateway-on", 2))
    )


_AdminGatewayControl_Type.__name__ = "Integer32"
_AdminGatewayControl_Object = MibScalar
adminGatewayControl = _AdminGatewayControl_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 30),
    _AdminGatewayControl_Type()
)
adminGatewayControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminGatewayControl.setStatus("mandatory")
_AdminPhoneTable_Object = MibTable
adminPhoneTable = _AdminPhoneTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 31)
)
if mibBuilder.loadTexts:
    adminPhoneTable.setStatus("mandatory")
_AdminPhoneEntry_Object = MibTableRow
adminPhoneEntry = _AdminPhoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 31, 1)
)
adminPhoneEntry.setIndexNames(
    (0, "Novell-LANtern-Admin-MIB", "adminPhoneIPAddr"),
)
if mibBuilder.loadTexts:
    adminPhoneEntry.setStatus("mandatory")
_AdminPhoneIPAddr_Type = IpAddress
_AdminPhoneIPAddr_Object = MibTableColumn
adminPhoneIPAddr = _AdminPhoneIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 31, 1, 1),
    _AdminPhoneIPAddr_Type()
)
adminPhoneIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminPhoneIPAddr.setStatus("mandatory")


class _AdminPhoneIPMask_Type(IpAddress):
    """Custom type adminPhoneIPMask based on IpAddress"""
    defaultHexValue = "00000000"


_AdminPhoneIPMask_Object = MibTableColumn
adminPhoneIPMask = _AdminPhoneIPMask_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 31, 1, 2),
    _AdminPhoneIPMask_Type()
)
adminPhoneIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminPhoneIPMask.setStatus("mandatory")


class _AdminPhoneLocalIPAddr_Type(IpAddress):
    """Custom type adminPhoneLocalIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AdminPhoneLocalIPAddr_Object = MibTableColumn
adminPhoneLocalIPAddr = _AdminPhoneLocalIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 31, 1, 3),
    _AdminPhoneLocalIPAddr_Type()
)
adminPhoneLocalIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminPhoneLocalIPAddr.setStatus("mandatory")
_AdminPhoneNumber_Type = OctetString
_AdminPhoneNumber_Object = MibTableColumn
adminPhoneNumber = _AdminPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 31, 1, 4),
    _AdminPhoneNumber_Type()
)
adminPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminPhoneNumber.setStatus("mandatory")
_AdminPhoneConnectionProtocol_Type = OctetString
_AdminPhoneConnectionProtocol_Object = MibTableColumn
adminPhoneConnectionProtocol = _AdminPhoneConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 31, 1, 5),
    _AdminPhoneConnectionProtocol_Type()
)
adminPhoneConnectionProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminPhoneConnectionProtocol.setStatus("mandatory")
_AdminPhoneDelete_Type = Integer32
_AdminPhoneDelete_Object = MibTableColumn
adminPhoneDelete = _AdminPhoneDelete_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 31, 1, 6),
    _AdminPhoneDelete_Type()
)
adminPhoneDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    adminPhoneDelete.setStatus("mandatory")


class _AdminFCBControl_Type(Integer32):
    """Custom type adminFCBControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdminFCBControl_Type.__name__ = "Integer32"
_AdminFCBControl_Object = MibScalar
adminFCBControl = _AdminFCBControl_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 1, 1, 32),
    _AdminFCBControl_Type()
)
adminFCBControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminFCBControl.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Novell-LANtern-Admin-MIB",
    **{"Time": Time,
       "DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "Seconds": Seconds,
       "novell": novell,
       "productType": productType,
       "networkMonitor": networkMonitor,
       "ethernetLANtern": ethernetLANtern,
       "mibDoc": mibDoc,
       "lantern": lantern,
       "lanternAdmin": lanternAdmin,
       "adminIdentification": adminIdentification,
       "adminDateAndTime": adminDateAndTime,
       "adminTimeZone": adminTimeZone,
       "adminPowerOnTime": adminPowerOnTime,
       "adminPowerOffTime": adminPowerOffTime,
       "adminNetworkDataLink": adminNetworkDataLink,
       "adminNetworkIPAddr": adminNetworkIPAddr,
       "adminNetworkSubnetMask": adminNetworkSubnetMask,
       "adminNetworkGateway": adminNetworkGateway,
       "adminClientTable": adminClientTable,
       "adminClientEntry": adminClientEntry,
       "adminClientIPAddr": adminClientIPAddr,
       "adminClientIPMask": adminClientIPMask,
       "adminClientCommunities": adminClientCommunities,
       "adminClientDelete": adminClientDelete,
       "adminUnauthorizedIPAddr": adminUnauthorizedIPAddr,
       "adminUnauthorizedCommunity": adminUnauthorizedCommunity,
       "adminNotificationTable": adminNotificationTable,
       "adminNotificationEntry": adminNotificationEntry,
       "adminNotificationIPAddr": adminNotificationIPAddr,
       "adminNotificationStatus": adminNotificationStatus,
       "adminNotificationTrapMask": adminNotificationTrapMask,
       "adminNotificationConfirmMask": adminNotificationConfirmMask,
       "adminNotificationTimeout": adminNotificationTimeout,
       "adminNotificationRetries": adminNotificationRetries,
       "adminNotificationBackupIPAddr": adminNotificationBackupIPAddr,
       "adminNotificationDelete": adminNotificationDelete,
       "adminTrapHandle": adminTrapHandle,
       "adminTrapAcknowledge": adminTrapAcknowledge,
       "adminDownLoadFile": adminDownLoadFile,
       "adminDownLoadServer": adminDownLoadServer,
       "adminDownload": adminDownload,
       "adminReset": adminReset,
       "adminSerialDataLink": adminSerialDataLink,
       "adminSerialIPAddr": adminSerialIPAddr,
       "adminSerialSubnetMask": adminSerialSubnetMask,
       "adminSerialBaudRate": adminSerialBaudRate,
       "adminSerialTimeout": adminSerialTimeout,
       "adminSerialConnection": adminSerialConnection,
       "adminSerialFlowControl": adminSerialFlowControl,
       "adminModemControl": adminModemControl,
       "adminModemConnect": adminModemConnect,
       "adminModemNoConnect": adminModemNoConnect,
       "adminGatewayControl": adminGatewayControl,
       "adminPhoneTable": adminPhoneTable,
       "adminPhoneEntry": adminPhoneEntry,
       "adminPhoneIPAddr": adminPhoneIPAddr,
       "adminPhoneIPMask": adminPhoneIPMask,
       "adminPhoneLocalIPAddr": adminPhoneLocalIPAddr,
       "adminPhoneNumber": adminPhoneNumber,
       "adminPhoneConnectionProtocol": adminPhoneConnectionProtocol,
       "adminPhoneDelete": adminPhoneDelete,
       "adminFCBControl": adminFCBControl}
)
