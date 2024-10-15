# SNMP MIB module (RADWIN-MIB-WINLINK1000) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADWIN-MIB-WINLINK1000
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:27 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Radwin_ObjectIdentity = ObjectIdentity
radwin = _Radwin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458)
)
_RadwinProducts_ObjectIdentity = ObjectIdentity
radwinProducts = _RadwinProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20)
)
_Winlink1000Family_ObjectIdentity = ObjectIdentity
winlink1000Family = _Winlink1000Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 2)
)
_Odu_ObjectIdentity = ObjectIdentity
odu = _Odu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 2, 1)
)
_OduIntegratedAntenna_ObjectIdentity = ObjectIdentity
oduIntegratedAntenna = _OduIntegratedAntenna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 2, 1, 1)
)
_OduExternalAntenna_ObjectIdentity = ObjectIdentity
oduExternalAntenna = _OduExternalAntenna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 2, 1, 2)
)
_Radwin2000Family_ObjectIdentity = ObjectIdentity
radwin2000Family = _Radwin2000Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 3)
)
_Odu2000_ObjectIdentity = ObjectIdentity
odu2000 = _Odu2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 3, 1)
)
_Odu2KIntegratedAntenna_ObjectIdentity = ObjectIdentity
odu2KIntegratedAntenna = _Odu2KIntegratedAntenna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 3, 1, 1)
)
_Odu2KExternalAntenna_ObjectIdentity = ObjectIdentity
odu2KExternalAntenna = _Odu2KExternalAntenna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 3, 1, 2)
)
_GpsSynchronizerFamily_ObjectIdentity = ObjectIdentity
gpsSynchronizerFamily = _GpsSynchronizerFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 4)
)
_OduGSU_ObjectIdentity = ObjectIdentity
oduGSU = _OduGSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 4, 1)
)
_OduGSUExternalAntenna_ObjectIdentity = ObjectIdentity
oduGSUExternalAntenna = _OduGSUExternalAntenna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 4, 1, 2)
)
_HssSyncUnits_ObjectIdentity = ObjectIdentity
hssSyncUnits = _HssSyncUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 4, 2)
)
_HssISU_ObjectIdentity = ObjectIdentity
hssISU = _HssISU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 4, 2, 1)
)
_HssGSU_ObjectIdentity = ObjectIdentity
hssGSU = _HssGSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 4, 2, 2)
)
_Radwin5000HBSFamily_ObjectIdentity = ObjectIdentity
radwin5000HBSFamily = _Radwin5000HBSFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 5)
)
_OduHBS_ObjectIdentity = ObjectIdentity
oduHBS = _OduHBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 5, 1)
)
_OduHBSIntegratedAntenna_ObjectIdentity = ObjectIdentity
oduHBSIntegratedAntenna = _OduHBSIntegratedAntenna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 5, 1, 1)
)
_OduHBSExternalAntenna_ObjectIdentity = ObjectIdentity
oduHBSExternalAntenna = _OduHBSExternalAntenna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 5, 1, 2)
)
_Radwin5000HSUFamily_ObjectIdentity = ObjectIdentity
radwin5000HSUFamily = _Radwin5000HSUFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 6)
)
_OduHSU_ObjectIdentity = ObjectIdentity
oduHSU = _OduHSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 6, 1)
)
_OduHSUIntegratedAntenna_ObjectIdentity = ObjectIdentity
oduHSUIntegratedAntenna = _OduHSUIntegratedAntenna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 6, 1, 1)
)
_OduHSUExternalAntenna_ObjectIdentity = ObjectIdentity
oduHSUExternalAntenna = _OduHSUExternalAntenna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 6, 1, 2)
)
_Radwin6000Family_ObjectIdentity = ObjectIdentity
radwin6000Family = _Radwin6000Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 10)
)
_Odu6000_ObjectIdentity = ObjectIdentity
odu6000 = _Odu6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 10, 1)
)
_Odu6K_ObjectIdentity = ObjectIdentity
odu6K = _Odu6K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 10, 1, 1)
)
_Gateway6000_ObjectIdentity = ObjectIdentity
gateway6000 = _Gateway6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 10, 2)
)
_Gateway6K_ObjectIdentity = ObjectIdentity
gateway6K = _Gateway6K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 10, 2, 1)
)
_RadwinWiFiAPFamily_ObjectIdentity = ObjectIdentity
radwinWiFiAPFamily = _RadwinWiFiAPFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 20)
)
_Odu600_ObjectIdentity = ObjectIdentity
odu600 = _Odu600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 20, 1)
)
_OduWiFiAP_ObjectIdentity = ObjectIdentity
oduWiFiAP = _OduWiFiAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 20, 20, 1, 1)
)
_Winlink1000_ObjectIdentity = ObjectIdentity
winlink1000 = _Winlink1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000)
)
_Winlink1000Odu_ObjectIdentity = ObjectIdentity
winlink1000Odu = _Winlink1000Odu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1)
)
_Winlink1000OduAdmin_ObjectIdentity = ObjectIdentity
winlink1000OduAdmin = _Winlink1000OduAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1)
)
_Winlink1000OduAdmProductType_Type = DisplayString
_Winlink1000OduAdmProductType_Object = MibScalar
winlink1000OduAdmProductType = _Winlink1000OduAdmProductType_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 1),
    _Winlink1000OduAdmProductType_Type()
)
winlink1000OduAdmProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmProductType.setStatus("mandatory")
_Winlink1000OduAdmHwRev_Type = DisplayString
_Winlink1000OduAdmHwRev_Object = MibScalar
winlink1000OduAdmHwRev = _Winlink1000OduAdmHwRev_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 2),
    _Winlink1000OduAdmHwRev_Type()
)
winlink1000OduAdmHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmHwRev.setStatus("mandatory")
_Winlink1000OduAdmSwRev_Type = DisplayString
_Winlink1000OduAdmSwRev_Object = MibScalar
winlink1000OduAdmSwRev = _Winlink1000OduAdmSwRev_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 3),
    _Winlink1000OduAdmSwRev_Type()
)
winlink1000OduAdmSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmSwRev.setStatus("mandatory")
_Winlink1000OduAdmLinkName_Type = DisplayString
_Winlink1000OduAdmLinkName_Object = MibScalar
winlink1000OduAdmLinkName = _Winlink1000OduAdmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 4),
    _Winlink1000OduAdmLinkName_Type()
)
winlink1000OduAdmLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmLinkName.setStatus("mandatory")
_Winlink1000OduAdmResetCmd_Type = Integer32
_Winlink1000OduAdmResetCmd_Object = MibScalar
winlink1000OduAdmResetCmd = _Winlink1000OduAdmResetCmd_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 5),
    _Winlink1000OduAdmResetCmd_Type()
)
winlink1000OduAdmResetCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmResetCmd.setStatus("mandatory")
_Winlink1000OduAdmAddres_Type = IpAddress
_Winlink1000OduAdmAddres_Object = MibScalar
winlink1000OduAdmAddres = _Winlink1000OduAdmAddres_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 6),
    _Winlink1000OduAdmAddres_Type()
)
winlink1000OduAdmAddres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmAddres.setStatus("mandatory")
_Winlink1000OduAdmMask_Type = IpAddress
_Winlink1000OduAdmMask_Object = MibScalar
winlink1000OduAdmMask = _Winlink1000OduAdmMask_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 7),
    _Winlink1000OduAdmMask_Type()
)
winlink1000OduAdmMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmMask.setStatus("mandatory")
_Winlink1000OduAdmGateway_Type = IpAddress
_Winlink1000OduAdmGateway_Object = MibScalar
winlink1000OduAdmGateway = _Winlink1000OduAdmGateway_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 8),
    _Winlink1000OduAdmGateway_Type()
)
winlink1000OduAdmGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmGateway.setStatus("mandatory")
_Winlink1000OduAdmBroadcast_Type = Integer32
_Winlink1000OduAdmBroadcast_Object = MibScalar
winlink1000OduAdmBroadcast = _Winlink1000OduAdmBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 10),
    _Winlink1000OduAdmBroadcast_Type()
)
winlink1000OduAdmBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmBroadcast.setStatus("mandatory")
_Winlink1000OduAdmHostsTable_Object = MibTable
winlink1000OduAdmHostsTable = _Winlink1000OduAdmHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 12)
)
if mibBuilder.loadTexts:
    winlink1000OduAdmHostsTable.setStatus("mandatory")
_Winlink1000OduAdmHostsEntry_Object = MibTableRow
winlink1000OduAdmHostsEntry = _Winlink1000OduAdmHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 12, 1)
)
winlink1000OduAdmHostsEntry.setIndexNames(
    (0, "RADWIN-MIB-WINLINK1000", "winlink1000OduAdmHostsIndex"),
)
if mibBuilder.loadTexts:
    winlink1000OduAdmHostsEntry.setStatus("mandatory")
_Winlink1000OduAdmHostsIndex_Type = Integer32
_Winlink1000OduAdmHostsIndex_Object = MibTableColumn
winlink1000OduAdmHostsIndex = _Winlink1000OduAdmHostsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 12, 1, 1),
    _Winlink1000OduAdmHostsIndex_Type()
)
winlink1000OduAdmHostsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmHostsIndex.setStatus("mandatory")
_Winlink1000OduAdmHostsIp_Type = IpAddress
_Winlink1000OduAdmHostsIp_Object = MibTableColumn
winlink1000OduAdmHostsIp = _Winlink1000OduAdmHostsIp_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 12, 1, 2),
    _Winlink1000OduAdmHostsIp_Type()
)
winlink1000OduAdmHostsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmHostsIp.setStatus("mandatory")


class _Winlink1000OduAdmHostsPort_Type(Integer32):
    """Custom type winlink1000OduAdmHostsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Winlink1000OduAdmHostsPort_Type.__name__ = "Integer32"
_Winlink1000OduAdmHostsPort_Object = MibTableColumn
winlink1000OduAdmHostsPort = _Winlink1000OduAdmHostsPort_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 12, 1, 3),
    _Winlink1000OduAdmHostsPort_Type()
)
winlink1000OduAdmHostsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmHostsPort.setStatus("mandatory")


class _Winlink1000OduAdmHostsSecurityModel_Type(Integer32):
    """Custom type winlink1000OduAdmHostsSecurityModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv3", 3))
    )


_Winlink1000OduAdmHostsSecurityModel_Type.__name__ = "Integer32"
_Winlink1000OduAdmHostsSecurityModel_Object = MibTableColumn
winlink1000OduAdmHostsSecurityModel = _Winlink1000OduAdmHostsSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 12, 1, 4),
    _Winlink1000OduAdmHostsSecurityModel_Type()
)
winlink1000OduAdmHostsSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmHostsSecurityModel.setStatus("mandatory")
_Winlink1000OduAdmHostsUserName_Type = DisplayString
_Winlink1000OduAdmHostsUserName_Object = MibTableColumn
winlink1000OduAdmHostsUserName = _Winlink1000OduAdmHostsUserName_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 12, 1, 5),
    _Winlink1000OduAdmHostsUserName_Type()
)
winlink1000OduAdmHostsUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmHostsUserName.setStatus("mandatory")
_Winlink1000OduAdmHostsPassword_Type = DisplayString
_Winlink1000OduAdmHostsPassword_Object = MibTableColumn
winlink1000OduAdmHostsPassword = _Winlink1000OduAdmHostsPassword_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 12, 1, 6),
    _Winlink1000OduAdmHostsPassword_Type()
)
winlink1000OduAdmHostsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmHostsPassword.setStatus("mandatory")
_Winlink1000OduAdmHostsIPv6_Type = DisplayString
_Winlink1000OduAdmHostsIPv6_Object = MibTableColumn
winlink1000OduAdmHostsIPv6 = _Winlink1000OduAdmHostsIPv6_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 12, 1, 7),
    _Winlink1000OduAdmHostsIPv6_Type()
)
winlink1000OduAdmHostsIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmHostsIPv6.setStatus("mandatory")
_Winlink1000OduBuzzerAdminState_Type = Integer32
_Winlink1000OduBuzzerAdminState_Object = MibScalar
winlink1000OduBuzzerAdminState = _Winlink1000OduBuzzerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 13),
    _Winlink1000OduBuzzerAdminState_Type()
)
winlink1000OduBuzzerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduBuzzerAdminState.setStatus("mandatory")
_Winlink1000OduProductId_Type = DisplayString
_Winlink1000OduProductId_Object = MibScalar
winlink1000OduProductId = _Winlink1000OduProductId_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 14),
    _Winlink1000OduProductId_Type()
)
winlink1000OduProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduProductId.setStatus("mandatory")
_Winlink1000OduReadCommunity_Type = DisplayString
_Winlink1000OduReadCommunity_Object = MibScalar
winlink1000OduReadCommunity = _Winlink1000OduReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 15),
    _Winlink1000OduReadCommunity_Type()
)
winlink1000OduReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduReadCommunity.setStatus("mandatory")
_Winlink1000OduReadWriteCommunity_Type = DisplayString
_Winlink1000OduReadWriteCommunity_Object = MibScalar
winlink1000OduReadWriteCommunity = _Winlink1000OduReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 16),
    _Winlink1000OduReadWriteCommunity_Type()
)
winlink1000OduReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduReadWriteCommunity.setStatus("mandatory")
_Winlink1000OduTrapCommunity_Type = DisplayString
_Winlink1000OduTrapCommunity_Object = MibScalar
winlink1000OduTrapCommunity = _Winlink1000OduTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 17),
    _Winlink1000OduTrapCommunity_Type()
)
winlink1000OduTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduTrapCommunity.setStatus("mandatory")
_Winlink1000OduAdmSnmpAgentVersion_Type = Integer32
_Winlink1000OduAdmSnmpAgentVersion_Object = MibScalar
winlink1000OduAdmSnmpAgentVersion = _Winlink1000OduAdmSnmpAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 18),
    _Winlink1000OduAdmSnmpAgentVersion_Type()
)
winlink1000OduAdmSnmpAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmSnmpAgentVersion.setStatus("mandatory")
_Winlink1000OduAdmRemoteSiteName_Type = DisplayString
_Winlink1000OduAdmRemoteSiteName_Object = MibScalar
winlink1000OduAdmRemoteSiteName = _Winlink1000OduAdmRemoteSiteName_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 19),
    _Winlink1000OduAdmRemoteSiteName_Type()
)
winlink1000OduAdmRemoteSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmRemoteSiteName.setStatus("mandatory")
_Winlink1000OduAdmSnmpAgentMinorVersion_Type = Integer32
_Winlink1000OduAdmSnmpAgentMinorVersion_Object = MibScalar
winlink1000OduAdmSnmpAgentMinorVersion = _Winlink1000OduAdmSnmpAgentMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 20),
    _Winlink1000OduAdmSnmpAgentMinorVersion_Type()
)
winlink1000OduAdmSnmpAgentMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmSnmpAgentMinorVersion.setStatus("mandatory")
_Winlink1000OduAdmLinkPassword_Type = DisplayString
_Winlink1000OduAdmLinkPassword_Object = MibScalar
winlink1000OduAdmLinkPassword = _Winlink1000OduAdmLinkPassword_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 21),
    _Winlink1000OduAdmLinkPassword_Type()
)
winlink1000OduAdmLinkPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmLinkPassword.setStatus("mandatory")
_Winlink1000OduAdmSiteLinkPassword_Type = DisplayString
_Winlink1000OduAdmSiteLinkPassword_Object = MibScalar
winlink1000OduAdmSiteLinkPassword = _Winlink1000OduAdmSiteLinkPassword_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 22),
    _Winlink1000OduAdmSiteLinkPassword_Type()
)
winlink1000OduAdmSiteLinkPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmSiteLinkPassword.setStatus("mandatory")


class _Winlink1000OduAdmDefaultPassword_Type(Integer32):
    """Custom type winlink1000OduAdmDefaultPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("nonDefault", 2))
    )


_Winlink1000OduAdmDefaultPassword_Type.__name__ = "Integer32"
_Winlink1000OduAdmDefaultPassword_Object = MibScalar
winlink1000OduAdmDefaultPassword = _Winlink1000OduAdmDefaultPassword_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 23),
    _Winlink1000OduAdmDefaultPassword_Type()
)
winlink1000OduAdmDefaultPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmDefaultPassword.setStatus("mandatory")


class _Winlink1000OduAdmConnectionType_Type(Integer32):
    """Custom type winlink1000OduAdmConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("directConnection", 1),
          ("indirectConnection", 2),
          ("unknown", 3))
    )


_Winlink1000OduAdmConnectionType_Type.__name__ = "Integer32"
_Winlink1000OduAdmConnectionType_Object = MibScalar
winlink1000OduAdmConnectionType = _Winlink1000OduAdmConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 24),
    _Winlink1000OduAdmConnectionType_Type()
)
winlink1000OduAdmConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmConnectionType.setStatus("mandatory")


class _Winlink1000OduAdmBackToFactorySettingsCmd_Type(Integer32):
    """Custom type winlink1000OduAdmBackToFactorySettingsCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("withIP", 1),
          ("withoutIP", 2))
    )


_Winlink1000OduAdmBackToFactorySettingsCmd_Type.__name__ = "Integer32"
_Winlink1000OduAdmBackToFactorySettingsCmd_Object = MibScalar
winlink1000OduAdmBackToFactorySettingsCmd = _Winlink1000OduAdmBackToFactorySettingsCmd_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 25),
    _Winlink1000OduAdmBackToFactorySettingsCmd_Type()
)
winlink1000OduAdmBackToFactorySettingsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmBackToFactorySettingsCmd.setStatus("mandatory")
_Winlink1000OduAdmIpParamsCnfg_Type = DisplayString
_Winlink1000OduAdmIpParamsCnfg_Object = MibScalar
winlink1000OduAdmIpParamsCnfg = _Winlink1000OduAdmIpParamsCnfg_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 26),
    _Winlink1000OduAdmIpParamsCnfg_Type()
)
winlink1000OduAdmIpParamsCnfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmIpParamsCnfg.setStatus("mandatory")


class _Winlink1000OduAdmVlanID_Type(Integer32):
    """Custom type winlink1000OduAdmVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Winlink1000OduAdmVlanID_Type.__name__ = "Integer32"
_Winlink1000OduAdmVlanID_Object = MibScalar
winlink1000OduAdmVlanID = _Winlink1000OduAdmVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 27),
    _Winlink1000OduAdmVlanID_Type()
)
winlink1000OduAdmVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmVlanID.setStatus("mandatory")


class _Winlink1000OduAdmVlanPriority_Type(Integer32):
    """Custom type winlink1000OduAdmVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Winlink1000OduAdmVlanPriority_Type.__name__ = "Integer32"
_Winlink1000OduAdmVlanPriority_Object = MibScalar
winlink1000OduAdmVlanPriority = _Winlink1000OduAdmVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 28),
    _Winlink1000OduAdmVlanPriority_Type()
)
winlink1000OduAdmVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmVlanPriority.setStatus("mandatory")
_Winlink1000OduAdmSN_Type = DisplayString
_Winlink1000OduAdmSN_Object = MibScalar
winlink1000OduAdmSN = _Winlink1000OduAdmSN_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 29),
    _Winlink1000OduAdmSN_Type()
)
winlink1000OduAdmSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmSN.setStatus("mandatory")
_Winlink1000OduAdmProductName_Type = DisplayString
_Winlink1000OduAdmProductName_Object = MibScalar
winlink1000OduAdmProductName = _Winlink1000OduAdmProductName_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 30),
    _Winlink1000OduAdmProductName_Type()
)
winlink1000OduAdmProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmProductName.setStatus("mandatory")
_Winlink1000OduAdmActivationKey_Type = DisplayString
_Winlink1000OduAdmActivationKey_Object = MibScalar
winlink1000OduAdmActivationKey = _Winlink1000OduAdmActivationKey_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 31),
    _Winlink1000OduAdmActivationKey_Type()
)
winlink1000OduAdmActivationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmActivationKey.setStatus("mandatory")
_Winlink1000OduAdmRmtPermittedOduType_Type = DisplayString
_Winlink1000OduAdmRmtPermittedOduType_Object = MibScalar
winlink1000OduAdmRmtPermittedOduType = _Winlink1000OduAdmRmtPermittedOduType_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 32),
    _Winlink1000OduAdmRmtPermittedOduType_Type()
)
winlink1000OduAdmRmtPermittedOduType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmRmtPermittedOduType.setStatus("mandatory")


class _Winlink1000OduAdmCpuID_Type(Integer32):
    """Custom type winlink1000OduAdmCpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Winlink1000OduAdmCpuID_Type.__name__ = "Integer32"
_Winlink1000OduAdmCpuID_Object = MibScalar
winlink1000OduAdmCpuID = _Winlink1000OduAdmCpuID_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 33),
    _Winlink1000OduAdmCpuID_Type()
)
winlink1000OduAdmCpuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmCpuID.setStatus("mandatory")
_Winlink1000OduAdmOvrdCmd_Type = DisplayString
_Winlink1000OduAdmOvrdCmd_Object = MibScalar
winlink1000OduAdmOvrdCmd = _Winlink1000OduAdmOvrdCmd_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 34),
    _Winlink1000OduAdmOvrdCmd_Type()
)
winlink1000OduAdmOvrdCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmOvrdCmd.setStatus("mandatory")


class _Winlink1000OduAdmLinkMode_Type(Integer32):
    """Custom type winlink1000OduAdmLinkMode based on Integer32"""
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
        *(("pmpHbs", 1),
          ("pmpHbsHyb", 4),
          ("pmpHsu", 2),
          ("pmpHsuHyb", 3))
    )


_Winlink1000OduAdmLinkMode_Type.__name__ = "Integer32"
_Winlink1000OduAdmLinkMode_Object = MibScalar
winlink1000OduAdmLinkMode = _Winlink1000OduAdmLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 35),
    _Winlink1000OduAdmLinkMode_Type()
)
winlink1000OduAdmLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmLinkMode.setStatus("mandatory")


class _Winlink1000OduAdmActualConnectMode_Type(Integer32):
    """Custom type winlink1000OduAdmActualConnectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ptmp", 3),
          ("ptp", 2))
    )


_Winlink1000OduAdmActualConnectMode_Type.__name__ = "Integer32"
_Winlink1000OduAdmActualConnectMode_Object = MibScalar
winlink1000OduAdmActualConnectMode = _Winlink1000OduAdmActualConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 36),
    _Winlink1000OduAdmActualConnectMode_Type()
)
winlink1000OduAdmActualConnectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmActualConnectMode.setStatus("mandatory")


class _Winlink1000OduAdmAES256Support_Type(Integer32):
    """Custom type winlink1000OduAdmAES256Support based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_Winlink1000OduAdmAES256Support_Type.__name__ = "Integer32"
_Winlink1000OduAdmAES256Support_Object = MibScalar
winlink1000OduAdmAES256Support = _Winlink1000OduAdmAES256Support_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 37),
    _Winlink1000OduAdmAES256Support_Type()
)
winlink1000OduAdmAES256Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmAES256Support.setStatus("mandatory")


class _Winlink1000OduAdmAES256State_Type(Integer32):
    """Custom type winlink1000OduAdmAES256State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Winlink1000OduAdmAES256State_Type.__name__ = "Integer32"
_Winlink1000OduAdmAES256State_Object = MibScalar
winlink1000OduAdmAES256State = _Winlink1000OduAdmAES256State_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 38),
    _Winlink1000OduAdmAES256State_Type()
)
winlink1000OduAdmAES256State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmAES256State.setStatus("mandatory")


class _Winlink1000OduAdmAES256Status_Type(Integer32):
    """Custom type winlink1000OduAdmAES256Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOperating", 1),
          ("operating", 3),
          ("partiallyOperating", 2))
    )


_Winlink1000OduAdmAES256Status_Type.__name__ = "Integer32"
_Winlink1000OduAdmAES256Status_Object = MibScalar
winlink1000OduAdmAES256Status = _Winlink1000OduAdmAES256Status_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 39),
    _Winlink1000OduAdmAES256Status_Type()
)
winlink1000OduAdmAES256Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmAES256Status.setStatus("mandatory")


class _Winlink1000OduAdmBatterySavingShutdownTime_Type(Integer32):
    """Custom type winlink1000OduAdmBatterySavingShutdownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Winlink1000OduAdmBatterySavingShutdownTime_Type.__name__ = "Integer32"
_Winlink1000OduAdmBatterySavingShutdownTime_Object = MibScalar
winlink1000OduAdmBatterySavingShutdownTime = _Winlink1000OduAdmBatterySavingShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 40),
    _Winlink1000OduAdmBatterySavingShutdownTime_Type()
)
winlink1000OduAdmBatterySavingShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmBatterySavingShutdownTime.setStatus("mandatory")


class _Winlink1000OduAdmWiFiPowerMode_Type(Integer32):
    """Custom type winlink1000OduAdmWiFiPowerMode based on Integer32"""
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
        *(("alwaysON", 4),
          ("powerOFF", 3),
          ("powerON", 2),
          ("undefined", 1))
    )


_Winlink1000OduAdmWiFiPowerMode_Type.__name__ = "Integer32"
_Winlink1000OduAdmWiFiPowerMode_Object = MibScalar
winlink1000OduAdmWiFiPowerMode = _Winlink1000OduAdmWiFiPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 41),
    _Winlink1000OduAdmWiFiPowerMode_Type()
)
winlink1000OduAdmWiFiPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmWiFiPowerMode.setStatus("mandatory")


class _Winlink1000OduAdmShutdownTimer_Type(Integer32):
    """Custom type winlink1000OduAdmShutdownTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Winlink1000OduAdmShutdownTimer_Type.__name__ = "Integer32"
_Winlink1000OduAdmShutdownTimer_Object = MibScalar
winlink1000OduAdmShutdownTimer = _Winlink1000OduAdmShutdownTimer_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 42),
    _Winlink1000OduAdmShutdownTimer_Type()
)
winlink1000OduAdmShutdownTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmShutdownTimer.setStatus("mandatory")


class _Winlink1000OduAdmGPSState_Type(Integer32):
    """Custom type winlink1000OduAdmGPSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 5),
          ("fixed", 3),
          ("notSynchronized", 2),
          ("shortCircuit", 4),
          ("synchronized", 6),
          ("synchronizedGlonass", 7),
          ("undefined", 1))
    )


_Winlink1000OduAdmGPSState_Type.__name__ = "Integer32"
_Winlink1000OduAdmGPSState_Object = MibScalar
winlink1000OduAdmGPSState = _Winlink1000OduAdmGPSState_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 43),
    _Winlink1000OduAdmGPSState_Type()
)
winlink1000OduAdmGPSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmGPSState.setStatus("mandatory")
_Winlink1000OduAdmTemperatureC_Type = Integer32
_Winlink1000OduAdmTemperatureC_Object = MibScalar
winlink1000OduAdmTemperatureC = _Winlink1000OduAdmTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 44),
    _Winlink1000OduAdmTemperatureC_Type()
)
winlink1000OduAdmTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmTemperatureC.setStatus("mandatory")


class _Winlink1000OduAdmIPStackMode_Type(Integer32):
    """Custom type winlink1000OduAdmIPStackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v4", 1),
          ("v4andv6", 3),
          ("v6", 2))
    )


_Winlink1000OduAdmIPStackMode_Type.__name__ = "Integer32"
_Winlink1000OduAdmIPStackMode_Object = MibScalar
winlink1000OduAdmIPStackMode = _Winlink1000OduAdmIPStackMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 45),
    _Winlink1000OduAdmIPStackMode_Type()
)
winlink1000OduAdmIPStackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmIPStackMode.setStatus("mandatory")
_Winlink1000OduAdmIPv6ParamsCnfg_Type = DisplayString
_Winlink1000OduAdmIPv6ParamsCnfg_Object = MibScalar
winlink1000OduAdmIPv6ParamsCnfg = _Winlink1000OduAdmIPv6ParamsCnfg_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 46),
    _Winlink1000OduAdmIPv6ParamsCnfg_Type()
)
winlink1000OduAdmIPv6ParamsCnfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmIPv6ParamsCnfg.setStatus("mandatory")
_Winlink1000OduAdmIPv6Address_Type = DisplayString
_Winlink1000OduAdmIPv6Address_Object = MibScalar
winlink1000OduAdmIPv6Address = _Winlink1000OduAdmIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 47),
    _Winlink1000OduAdmIPv6Address_Type()
)
winlink1000OduAdmIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmIPv6Address.setStatus("mandatory")
_Winlink1000OduAdmIPv6Prefix_Type = Integer32
_Winlink1000OduAdmIPv6Prefix_Object = MibScalar
winlink1000OduAdmIPv6Prefix = _Winlink1000OduAdmIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 48),
    _Winlink1000OduAdmIPv6Prefix_Type()
)
winlink1000OduAdmIPv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmIPv6Prefix.setStatus("mandatory")
_Winlink1000OduAdmIPv6DefaultGateWay_Type = DisplayString
_Winlink1000OduAdmIPv6DefaultGateWay_Object = MibScalar
winlink1000OduAdmIPv6DefaultGateWay = _Winlink1000OduAdmIPv6DefaultGateWay_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 49),
    _Winlink1000OduAdmIPv6DefaultGateWay_Type()
)
winlink1000OduAdmIPv6DefaultGateWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmIPv6DefaultGateWay.setStatus("mandatory")
_Winlink1000OduAdmPowerConsumption_Type = Integer32
_Winlink1000OduAdmPowerConsumption_Object = MibScalar
winlink1000OduAdmPowerConsumption = _Winlink1000OduAdmPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 50),
    _Winlink1000OduAdmPowerConsumption_Type()
)
winlink1000OduAdmPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmPowerConsumption.setStatus("mandatory")
_Winlink1000OduAdmWifi_ObjectIdentity = ObjectIdentity
winlink1000OduAdmWifi = _Winlink1000OduAdmWifi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 51)
)


class _Winlink1000OduAdmWifiChannel_Type(Integer32):
    """Custom type winlink1000OduAdmWifiChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_Winlink1000OduAdmWifiChannel_Type.__name__ = "Integer32"
_Winlink1000OduAdmWifiChannel_Object = MibScalar
winlink1000OduAdmWifiChannel = _Winlink1000OduAdmWifiChannel_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 51, 1),
    _Winlink1000OduAdmWifiChannel_Type()
)
winlink1000OduAdmWifiChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmWifiChannel.setStatus("mandatory")


class _Winlink1000OduAdmWifiTxPower_Type(Integer32):
    """Custom type winlink1000OduAdmWifiTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(11, 15),
    )


_Winlink1000OduAdmWifiTxPower_Type.__name__ = "Integer32"
_Winlink1000OduAdmWifiTxPower_Object = MibScalar
winlink1000OduAdmWifiTxPower = _Winlink1000OduAdmWifiTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 51, 2),
    _Winlink1000OduAdmWifiTxPower_Type()
)
winlink1000OduAdmWifiTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmWifiTxPower.setStatus("mandatory")
_Winlink1000OduAdmWifiSSID_Type = DisplayString
_Winlink1000OduAdmWifiSSID_Object = MibScalar
winlink1000OduAdmWifiSSID = _Winlink1000OduAdmWifiSSID_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 51, 3),
    _Winlink1000OduAdmWifiSSID_Type()
)
winlink1000OduAdmWifiSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmWifiSSID.setStatus("mandatory")


class _Winlink1000OduAdmWifiSecurityType_Type(Integer32):
    """Custom type winlink1000OduAdmWifiSecurityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("wep", 2),
          ("wpa2", 3))
    )


_Winlink1000OduAdmWifiSecurityType_Type.__name__ = "Integer32"
_Winlink1000OduAdmWifiSecurityType_Object = MibScalar
winlink1000OduAdmWifiSecurityType = _Winlink1000OduAdmWifiSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 51, 4),
    _Winlink1000OduAdmWifiSecurityType_Type()
)
winlink1000OduAdmWifiSecurityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmWifiSecurityType.setStatus("mandatory")
_Winlink1000OduAdmWifiPassword_Type = DisplayString
_Winlink1000OduAdmWifiPassword_Object = MibScalar
winlink1000OduAdmWifiPassword = _Winlink1000OduAdmWifiPassword_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 51, 5),
    _Winlink1000OduAdmWifiPassword_Type()
)
winlink1000OduAdmWifiPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmWifiPassword.setStatus("mandatory")
_Winlink1000OduAdmWifiNetwork_Type = IpAddress
_Winlink1000OduAdmWifiNetwork_Object = MibScalar
winlink1000OduAdmWifiNetwork = _Winlink1000OduAdmWifiNetwork_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 51, 6),
    _Winlink1000OduAdmWifiNetwork_Type()
)
winlink1000OduAdmWifiNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmWifiNetwork.setStatus("mandatory")
_Winlink1000OduAdmWifiRssi_Type = Integer32
_Winlink1000OduAdmWifiRssi_Object = MibScalar
winlink1000OduAdmWifiRssi = _Winlink1000OduAdmWifiRssi_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 51, 7),
    _Winlink1000OduAdmWifiRssi_Type()
)
winlink1000OduAdmWifiRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmWifiRssi.setStatus("mandatory")
_Winlink1000OduAdmWifiStationMAC_Type = DisplayString
_Winlink1000OduAdmWifiStationMAC_Object = MibScalar
winlink1000OduAdmWifiStationMAC = _Winlink1000OduAdmWifiStationMAC_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 51, 8),
    _Winlink1000OduAdmWifiStationMAC_Type()
)
winlink1000OduAdmWifiStationMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmWifiStationMAC.setStatus("mandatory")


class _Winlink1000OduAdmWifiRestart_Type(Integer32):
    """Custom type winlink1000OduAdmWifiRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Winlink1000OduAdmWifiRestart_Type.__name__ = "Integer32"
_Winlink1000OduAdmWifiRestart_Object = MibScalar
winlink1000OduAdmWifiRestart = _Winlink1000OduAdmWifiRestart_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 51, 9),
    _Winlink1000OduAdmWifiRestart_Type()
)
winlink1000OduAdmWifiRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmWifiRestart.setStatus("mandatory")


class _Winlink1000OduAdmWifiApStatus_Type(Integer32):
    """Custom type winlink1000OduAdmWifiApStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 3),
          ("off", 1),
          ("on", 2))
    )


_Winlink1000OduAdmWifiApStatus_Type.__name__ = "Integer32"
_Winlink1000OduAdmWifiApStatus_Object = MibScalar
winlink1000OduAdmWifiApStatus = _Winlink1000OduAdmWifiApStatus_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 51, 10),
    _Winlink1000OduAdmWifiApStatus_Type()
)
winlink1000OduAdmWifiApStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmWifiApStatus.setStatus("mandatory")


class _Winlink1000OduAdmBsaOperationMode_Type(Integer32):
    """Custom type winlink1000OduAdmBsaOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hbsTracking", 2),
          ("hsuAlignment", 3),
          ("inactive", 1))
    )


_Winlink1000OduAdmBsaOperationMode_Type.__name__ = "Integer32"
_Winlink1000OduAdmBsaOperationMode_Object = MibScalar
winlink1000OduAdmBsaOperationMode = _Winlink1000OduAdmBsaOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 52),
    _Winlink1000OduAdmBsaOperationMode_Type()
)
winlink1000OduAdmBsaOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmBsaOperationMode.setStatus("mandatory")
_Winlink1000OduAdmMngConnection_Type = DisplayString
_Winlink1000OduAdmMngConnection_Object = MibScalar
winlink1000OduAdmMngConnection = _Winlink1000OduAdmMngConnection_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 53),
    _Winlink1000OduAdmMngConnection_Type()
)
winlink1000OduAdmMngConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmMngConnection.setStatus("mandatory")


class _Winlink1000OduAdm1588TCSupport_Type(Integer32):
    """Custom type winlink1000OduAdm1588TCSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_Winlink1000OduAdm1588TCSupport_Type.__name__ = "Integer32"
_Winlink1000OduAdm1588TCSupport_Object = MibScalar
winlink1000OduAdm1588TCSupport = _Winlink1000OduAdm1588TCSupport_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 54),
    _Winlink1000OduAdm1588TCSupport_Type()
)
winlink1000OduAdm1588TCSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdm1588TCSupport.setStatus("mandatory")


class _Winlink1000OduAdmSyncESupport_Type(Integer32):
    """Custom type winlink1000OduAdmSyncESupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_Winlink1000OduAdmSyncESupport_Type.__name__ = "Integer32"
_Winlink1000OduAdmSyncESupport_Object = MibScalar
winlink1000OduAdmSyncESupport = _Winlink1000OduAdmSyncESupport_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 55),
    _Winlink1000OduAdmSyncESupport_Type()
)
winlink1000OduAdmSyncESupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmSyncESupport.setStatus("mandatory")
_Winlink1000OduAdmRadioRev_Type = DisplayString
_Winlink1000OduAdmRadioRev_Object = MibScalar
winlink1000OduAdmRadioRev = _Winlink1000OduAdmRadioRev_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 56),
    _Winlink1000OduAdmRadioRev_Type()
)
winlink1000OduAdmRadioRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmRadioRev.setStatus("mandatory")
_Winlink1000OduAdmProductRev_Type = DisplayString
_Winlink1000OduAdmProductRev_Object = MibScalar
winlink1000OduAdmProductRev = _Winlink1000OduAdmProductRev_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 57),
    _Winlink1000OduAdmProductRev_Type()
)
winlink1000OduAdmProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmProductRev.setStatus("mandatory")


class _Winlink1000OduAdmPMPSUSupport_Type(Integer32):
    """Custom type winlink1000OduAdmPMPSUSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_Winlink1000OduAdmPMPSUSupport_Type.__name__ = "Integer32"
_Winlink1000OduAdmPMPSUSupport_Object = MibScalar
winlink1000OduAdmPMPSUSupport = _Winlink1000OduAdmPMPSUSupport_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 58),
    _Winlink1000OduAdmPMPSUSupport_Type()
)
winlink1000OduAdmPMPSUSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmPMPSUSupport.setStatus("mandatory")
_Winlink1000OduAdmManagerDownloadURL_Type = DisplayString
_Winlink1000OduAdmManagerDownloadURL_Object = MibScalar
winlink1000OduAdmManagerDownloadURL = _Winlink1000OduAdmManagerDownloadURL_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 59),
    _Winlink1000OduAdmManagerDownloadURL_Type()
)
winlink1000OduAdmManagerDownloadURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAdmManagerDownloadURL.setStatus("mandatory")
_Winlink1000OduAdmAntennaDescription_Type = DisplayString
_Winlink1000OduAdmAntennaDescription_Object = MibScalar
winlink1000OduAdmAntennaDescription = _Winlink1000OduAdmAntennaDescription_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 60),
    _Winlink1000OduAdmAntennaDescription_Type()
)
winlink1000OduAdmAntennaDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmAntennaDescription.setStatus("mandatory")
_Winlink1000OduAdmSwCapabilities_Type = DisplayString
_Winlink1000OduAdmSwCapabilities_Object = MibScalar
winlink1000OduAdmSwCapabilities = _Winlink1000OduAdmSwCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 1, 61),
    _Winlink1000OduAdmSwCapabilities_Type()
)
winlink1000OduAdmSwCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAdmSwCapabilities.setStatus("mandatory")
_Winlink1000OduService_ObjectIdentity = ObjectIdentity
winlink1000OduService = _Winlink1000OduService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2)
)


class _Winlink1000OduSrvMode_Type(Integer32):
    """Custom type winlink1000OduSrvMode based on Integer32"""
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
        *(("inactiveMode", 5),
          ("installMode", 1),
          ("normalMode", 2),
          ("slaveMode", 3),
          ("tempInstallMode", 4))
    )


_Winlink1000OduSrvMode_Type.__name__ = "Integer32"
_Winlink1000OduSrvMode_Object = MibScalar
winlink1000OduSrvMode = _Winlink1000OduSrvMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 1),
    _Winlink1000OduSrvMode_Type()
)
winlink1000OduSrvMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvMode.setStatus("mandatory")
_Winlink1000OduSrvBridging_Type = Integer32
_Winlink1000OduSrvBridging_Object = MibScalar
winlink1000OduSrvBridging = _Winlink1000OduSrvBridging_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 3),
    _Winlink1000OduSrvBridging_Type()
)
winlink1000OduSrvBridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduSrvBridging.setStatus("mandatory")
_Winlink1000OduServiceRingTopology_ObjectIdentity = ObjectIdentity
winlink1000OduServiceRingTopology = _Winlink1000OduServiceRingTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 4)
)


class _Winlink1000OduSrvRingLinkMode_Type(Integer32):
    """Custom type winlink1000OduSrvRingLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("independentLink", 1),
          ("nonRpl", 2),
          ("rpl", 3))
    )


_Winlink1000OduSrvRingLinkMode_Type.__name__ = "Integer32"
_Winlink1000OduSrvRingLinkMode_Object = MibScalar
winlink1000OduSrvRingLinkMode = _Winlink1000OduSrvRingLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 4, 1),
    _Winlink1000OduSrvRingLinkMode_Type()
)
winlink1000OduSrvRingLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvRingLinkMode.setStatus("mandatory")


class _Winlink1000OduSrvRingTopologySupported_Type(Integer32):
    """Custom type winlink1000OduSrvRingTopologySupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_Winlink1000OduSrvRingTopologySupported_Type.__name__ = "Integer32"
_Winlink1000OduSrvRingTopologySupported_Object = MibScalar
winlink1000OduSrvRingTopologySupported = _Winlink1000OduSrvRingTopologySupported_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 4, 2),
    _Winlink1000OduSrvRingTopologySupported_Type()
)
winlink1000OduSrvRingTopologySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduSrvRingTopologySupported.setStatus("mandatory")
_Winlink1000OduSrvRingVlanIdTable_Object = MibTable
winlink1000OduSrvRingVlanIdTable = _Winlink1000OduSrvRingVlanIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    winlink1000OduSrvRingVlanIdTable.setStatus("mandatory")
_Winlink1000OduSrvRingVlanIdEntry_Object = MibTableRow
winlink1000OduSrvRingVlanIdEntry = _Winlink1000OduSrvRingVlanIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 4, 3, 1)
)
winlink1000OduSrvRingVlanIdEntry.setIndexNames(
    (0, "RADWIN-MIB-WINLINK1000", "winlink1000OduSrvRingVlanIdIndex"),
)
if mibBuilder.loadTexts:
    winlink1000OduSrvRingVlanIdEntry.setStatus("mandatory")


class _Winlink1000OduSrvRingVlanIdIndex_Type(Integer32):
    """Custom type winlink1000OduSrvRingVlanIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Winlink1000OduSrvRingVlanIdIndex_Type.__name__ = "Integer32"
_Winlink1000OduSrvRingVlanIdIndex_Object = MibTableColumn
winlink1000OduSrvRingVlanIdIndex = _Winlink1000OduSrvRingVlanIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 4, 3, 1, 1),
    _Winlink1000OduSrvRingVlanIdIndex_Type()
)
winlink1000OduSrvRingVlanIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduSrvRingVlanIdIndex.setStatus("mandatory")


class _Winlink1000OduSrvRingVlanId_Type(Integer32):
    """Custom type winlink1000OduSrvRingVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Winlink1000OduSrvRingVlanId_Type.__name__ = "Integer32"
_Winlink1000OduSrvRingVlanId_Object = MibTableColumn
winlink1000OduSrvRingVlanId = _Winlink1000OduSrvRingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 4, 3, 1, 2),
    _Winlink1000OduSrvRingVlanId_Type()
)
winlink1000OduSrvRingVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvRingVlanId.setStatus("mandatory")


class _Winlink1000OduSrvRingEthStatus_Type(Integer32):
    """Custom type winlink1000OduSrvRingEthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("notApplicable", 3),
          ("unblocked", 1))
    )


_Winlink1000OduSrvRingEthStatus_Type.__name__ = "Integer32"
_Winlink1000OduSrvRingEthStatus_Object = MibScalar
winlink1000OduSrvRingEthStatus = _Winlink1000OduSrvRingEthStatus_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 4, 4),
    _Winlink1000OduSrvRingEthStatus_Type()
)
winlink1000OduSrvRingEthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduSrvRingEthStatus.setStatus("mandatory")
_Winlink1000OduSrvRingMaxAllowedTimeFromLastRpm_Type = Integer32
_Winlink1000OduSrvRingMaxAllowedTimeFromLastRpm_Object = MibScalar
winlink1000OduSrvRingMaxAllowedTimeFromLastRpm = _Winlink1000OduSrvRingMaxAllowedTimeFromLastRpm_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 4, 5),
    _Winlink1000OduSrvRingMaxAllowedTimeFromLastRpm_Type()
)
winlink1000OduSrvRingMaxAllowedTimeFromLastRpm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvRingMaxAllowedTimeFromLastRpm.setStatus("mandatory")
_Winlink1000OduSrvRingWTR_Type = Integer32
_Winlink1000OduSrvRingWTR_Object = MibScalar
winlink1000OduSrvRingWTR = _Winlink1000OduSrvRingWTR_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 4, 6),
    _Winlink1000OduSrvRingWTR_Type()
)
winlink1000OduSrvRingWTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvRingWTR.setStatus("mandatory")
_Winlink1000OduServiceQoS_ObjectIdentity = ObjectIdentity
winlink1000OduServiceQoS = _Winlink1000OduServiceQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 5)
)


class _Winlink1000OduSrvQoSMode_Type(Integer32):
    """Custom type winlink1000OduSrvQoSMode based on Integer32"""
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
        *(("classDiffserv", 4),
          ("classVlan", 3),
          ("notActive", 2),
          ("notSupported", 1))
    )


_Winlink1000OduSrvQoSMode_Type.__name__ = "Integer32"
_Winlink1000OduSrvQoSMode_Object = MibScalar
winlink1000OduSrvQoSMode = _Winlink1000OduSrvQoSMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 5, 1),
    _Winlink1000OduSrvQoSMode_Type()
)
winlink1000OduSrvQoSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvQoSMode.setStatus("mandatory")
_Winlink1000OduSrvQoSConfTable_Object = MibTable
winlink1000OduSrvQoSConfTable = _Winlink1000OduSrvQoSConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    winlink1000OduSrvQoSConfTable.setStatus("mandatory")
_Winlink1000OduSrvQoSConfEntry_Object = MibTableRow
winlink1000OduSrvQoSConfEntry = _Winlink1000OduSrvQoSConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 5, 2, 1)
)
winlink1000OduSrvQoSConfEntry.setIndexNames(
    (0, "RADWIN-MIB-WINLINK1000", "winlink1000OduSrvQoSConfIndex"),
)
if mibBuilder.loadTexts:
    winlink1000OduSrvQoSConfEntry.setStatus("mandatory")


class _Winlink1000OduSrvQoSConfIndex_Type(Integer32):
    """Custom type winlink1000OduSrvQoSConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Winlink1000OduSrvQoSConfIndex_Type.__name__ = "Integer32"
_Winlink1000OduSrvQoSConfIndex_Object = MibTableColumn
winlink1000OduSrvQoSConfIndex = _Winlink1000OduSrvQoSConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 5, 2, 1, 1),
    _Winlink1000OduSrvQoSConfIndex_Type()
)
winlink1000OduSrvQoSConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduSrvQoSConfIndex.setStatus("mandatory")


class _Winlink1000OduSrvConfVlanQGroups_Type(Integer32):
    """Custom type winlink1000OduSrvConfVlanQGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Winlink1000OduSrvConfVlanQGroups_Type.__name__ = "Integer32"
_Winlink1000OduSrvConfVlanQGroups_Object = MibTableColumn
winlink1000OduSrvConfVlanQGroups = _Winlink1000OduSrvConfVlanQGroups_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 5, 2, 1, 2),
    _Winlink1000OduSrvConfVlanQGroups_Type()
)
winlink1000OduSrvConfVlanQGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduSrvConfVlanQGroups.setStatus("mandatory")


class _Winlink1000OduSrvConfDiffservQGroups_Type(Integer32):
    """Custom type winlink1000OduSrvConfDiffservQGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_Winlink1000OduSrvConfDiffservQGroups_Type.__name__ = "Integer32"
_Winlink1000OduSrvConfDiffservQGroups_Object = MibTableColumn
winlink1000OduSrvConfDiffservQGroups = _Winlink1000OduSrvConfDiffservQGroups_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 5, 2, 1, 3),
    _Winlink1000OduSrvConfDiffservQGroups_Type()
)
winlink1000OduSrvConfDiffservQGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduSrvConfDiffservQGroups.setStatus("mandatory")
_Winlink1000OduSrvConfQueMir_Type = Integer32
_Winlink1000OduSrvConfQueMir_Object = MibTableColumn
winlink1000OduSrvConfQueMir = _Winlink1000OduSrvConfQueMir_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 5, 2, 1, 4),
    _Winlink1000OduSrvConfQueMir_Type()
)
winlink1000OduSrvConfQueMir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvConfQueMir.setStatus("mandatory")


class _Winlink1000OduSrvConfQueWeight_Type(Integer32):
    """Custom type winlink1000OduSrvConfQueWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Winlink1000OduSrvConfQueWeight_Type.__name__ = "Integer32"
_Winlink1000OduSrvConfQueWeight_Object = MibTableColumn
winlink1000OduSrvConfQueWeight = _Winlink1000OduSrvConfQueWeight_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 5, 2, 1, 5),
    _Winlink1000OduSrvConfQueWeight_Type()
)
winlink1000OduSrvConfQueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvConfQueWeight.setStatus("mandatory")
_Winlink1000OduSrvQoSVlanQGroupsSetStr_Type = DisplayString
_Winlink1000OduSrvQoSVlanQGroupsSetStr_Object = MibScalar
winlink1000OduSrvQoSVlanQGroupsSetStr = _Winlink1000OduSrvQoSVlanQGroupsSetStr_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 5, 3),
    _Winlink1000OduSrvQoSVlanQGroupsSetStr_Type()
)
winlink1000OduSrvQoSVlanQGroupsSetStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvQoSVlanQGroupsSetStr.setStatus("mandatory")
_Winlink1000OduSrvQoSDiffservQGroupsSetStr_Type = DisplayString
_Winlink1000OduSrvQoSDiffservQGroupsSetStr_Object = MibScalar
winlink1000OduSrvQoSDiffservQGroupsSetStr = _Winlink1000OduSrvQoSDiffservQGroupsSetStr_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 5, 4),
    _Winlink1000OduSrvQoSDiffservQGroupsSetStr_Type()
)
winlink1000OduSrvQoSDiffservQGroupsSetStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvQoSDiffservQGroupsSetStr.setStatus("mandatory")


class _Winlink1000OduSrvQoSMaxRTQuePercent_Type(Integer32):
    """Custom type winlink1000OduSrvQoSMaxRTQuePercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Winlink1000OduSrvQoSMaxRTQuePercent_Type.__name__ = "Integer32"
_Winlink1000OduSrvQoSMaxRTQuePercent_Object = MibScalar
winlink1000OduSrvQoSMaxRTQuePercent = _Winlink1000OduSrvQoSMaxRTQuePercent_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 5, 5),
    _Winlink1000OduSrvQoSMaxRTQuePercent_Type()
)
winlink1000OduSrvQoSMaxRTQuePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduSrvQoSMaxRTQuePercent.setStatus("mandatory")
_Winlink1000OduServiceVlan_ObjectIdentity = ObjectIdentity
winlink1000OduServiceVlan = _Winlink1000OduServiceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 6)
)


class _Winlink1000OduSrvVlanSupport_Type(Integer32):
    """Custom type winlink1000OduSrvVlanSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 3),
          ("notSupported", 1),
          ("supported", 2))
    )


_Winlink1000OduSrvVlanSupport_Type.__name__ = "Integer32"
_Winlink1000OduSrvVlanSupport_Object = MibScalar
winlink1000OduSrvVlanSupport = _Winlink1000OduSrvVlanSupport_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 6, 1),
    _Winlink1000OduSrvVlanSupport_Type()
)
winlink1000OduSrvVlanSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduSrvVlanSupport.setStatus("mandatory")


class _Winlink1000OduSrvVlanIngressMode_Type(Integer32):
    """Custom type winlink1000OduSrvVlanIngressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 3),
          ("transparent", 1),
          ("untagAll", 2))
    )


_Winlink1000OduSrvVlanIngressMode_Type.__name__ = "Integer32"
_Winlink1000OduSrvVlanIngressMode_Object = MibScalar
winlink1000OduSrvVlanIngressMode = _Winlink1000OduSrvVlanIngressMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 6, 2),
    _Winlink1000OduSrvVlanIngressMode_Type()
)
winlink1000OduSrvVlanIngressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvVlanIngressMode.setStatus("mandatory")


class _Winlink1000OduSrvVlanEgressMode_Type(Integer32):
    """Custom type winlink1000OduSrvVlanEgressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("provider", 3),
          ("tag", 2),
          ("transparent", 1))
    )


_Winlink1000OduSrvVlanEgressMode_Type.__name__ = "Integer32"
_Winlink1000OduSrvVlanEgressMode_Object = MibScalar
winlink1000OduSrvVlanEgressMode = _Winlink1000OduSrvVlanEgressMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 6, 3),
    _Winlink1000OduSrvVlanEgressMode_Type()
)
winlink1000OduSrvVlanEgressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvVlanEgressMode.setStatus("mandatory")


class _Winlink1000OduSrvEgressTag_Type(Integer32):
    """Custom type winlink1000OduSrvEgressTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40947),
    )


_Winlink1000OduSrvEgressTag_Type.__name__ = "Integer32"
_Winlink1000OduSrvEgressTag_Object = MibScalar
winlink1000OduSrvEgressTag = _Winlink1000OduSrvEgressTag_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 6, 4),
    _Winlink1000OduSrvEgressTag_Type()
)
winlink1000OduSrvEgressTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvEgressTag.setStatus("mandatory")


class _Winlink1000OduSrvEgressProviderTag_Type(Integer32):
    """Custom type winlink1000OduSrvEgressProviderTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40947),
    )


_Winlink1000OduSrvEgressProviderTag_Type.__name__ = "Integer32"
_Winlink1000OduSrvEgressProviderTag_Object = MibScalar
winlink1000OduSrvEgressProviderTag = _Winlink1000OduSrvEgressProviderTag_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 6, 5),
    _Winlink1000OduSrvEgressProviderTag_Type()
)
winlink1000OduSrvEgressProviderTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvEgressProviderTag.setStatus("mandatory")
_Winlink1000OduSrvVlanIngressAllowedVIDs_Type = DisplayString
_Winlink1000OduSrvVlanIngressAllowedVIDs_Object = MibScalar
winlink1000OduSrvVlanIngressAllowedVIDs = _Winlink1000OduSrvVlanIngressAllowedVIDs_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 6, 6),
    _Winlink1000OduSrvVlanIngressAllowedVIDs_Type()
)
winlink1000OduSrvVlanIngressAllowedVIDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvVlanIngressAllowedVIDs.setStatus("mandatory")
_Winlink1000OduSrvVlanDisable_Type = Integer32
_Winlink1000OduSrvVlanDisable_Object = MibScalar
winlink1000OduSrvVlanDisable = _Winlink1000OduSrvVlanDisable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 6, 7),
    _Winlink1000OduSrvVlanDisable_Type()
)
winlink1000OduSrvVlanDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduSrvVlanDisable.setStatus("mandatory")
_Winlink1000OduServiceVlanProviderListTPIDstr_Type = DisplayString
_Winlink1000OduServiceVlanProviderListTPIDstr_Object = MibScalar
winlink1000OduServiceVlanProviderListTPIDstr = _Winlink1000OduServiceVlanProviderListTPIDstr_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 2, 6, 8),
    _Winlink1000OduServiceVlanProviderListTPIDstr_Type()
)
winlink1000OduServiceVlanProviderListTPIDstr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduServiceVlanProviderListTPIDstr.setStatus("mandatory")
_Winlink1000OduEthernet_ObjectIdentity = ObjectIdentity
winlink1000OduEthernet = _Winlink1000OduEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3)
)
_Winlink1000OduEthernetRemainingRate_Type = Integer32
_Winlink1000OduEthernetRemainingRate_Object = MibScalar
winlink1000OduEthernetRemainingRate = _Winlink1000OduEthernetRemainingRate_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3, 1),
    _Winlink1000OduEthernetRemainingRate_Type()
)
winlink1000OduEthernetRemainingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduEthernetRemainingRate.setStatus("mandatory")
_Winlink1000OduEthernetIfTable_Object = MibTable
winlink1000OduEthernetIfTable = _Winlink1000OduEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3, 2)
)
if mibBuilder.loadTexts:
    winlink1000OduEthernetIfTable.setStatus("mandatory")
_Winlink1000OduEthernetIfEntry_Object = MibTableRow
winlink1000OduEthernetIfEntry = _Winlink1000OduEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3, 2, 1)
)
winlink1000OduEthernetIfEntry.setIndexNames(
    (0, "RADWIN-MIB-WINLINK1000", "winlink1000OduEthernetIfIndex"),
)
if mibBuilder.loadTexts:
    winlink1000OduEthernetIfEntry.setStatus("mandatory")
_Winlink1000OduEthernetIfIndex_Type = Integer32
_Winlink1000OduEthernetIfIndex_Object = MibTableColumn
winlink1000OduEthernetIfIndex = _Winlink1000OduEthernetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3, 2, 1, 1),
    _Winlink1000OduEthernetIfIndex_Type()
)
winlink1000OduEthernetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduEthernetIfIndex.setStatus("mandatory")
_Winlink1000OduEthernetIfAddress_Type = DisplayString
_Winlink1000OduEthernetIfAddress_Object = MibTableColumn
winlink1000OduEthernetIfAddress = _Winlink1000OduEthernetIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3, 2, 1, 5),
    _Winlink1000OduEthernetIfAddress_Type()
)
winlink1000OduEthernetIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduEthernetIfAddress.setStatus("mandatory")


class _Winlink1000OduEthernetIfAdminStatus_Type(Integer32):
    """Custom type winlink1000OduEthernetIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              10,
              11,
              15,
              16,
              21,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disablePoePort", 254),
          ("disablePort", 255),
          ("forceFullDuplex1000Mbps", 21),
          ("forceFullDuplex100Mbps", 16),
          ("forceFullDuplex10Mbps", 11),
          ("forceHalfDuplex100Mbps", 15),
          ("forceHalfDuplex10Mbps", 10),
          ("portAutoSense", 1),
          ("portAutoSense100Mbps", 5))
    )


_Winlink1000OduEthernetIfAdminStatus_Type.__name__ = "Integer32"
_Winlink1000OduEthernetIfAdminStatus_Object = MibTableColumn
winlink1000OduEthernetIfAdminStatus = _Winlink1000OduEthernetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3, 2, 1, 6),
    _Winlink1000OduEthernetIfAdminStatus_Type()
)
winlink1000OduEthernetIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduEthernetIfAdminStatus.setStatus("mandatory")


class _Winlink1000OduEthernetIfOperStatus_Type(Integer32):
    """Custom type winlink1000OduEthernetIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              11,
              15,
              16,
              20,
              21,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("connectedFullDuplex1000Mbps", 21),
          ("connectedFullDuplex100Mbps", 16),
          ("connectedFullDuplex10Mbps", 11),
          ("connectedHalfDuplex1000Mbps", 20),
          ("connectedHalfDuplex100Mbps", 15),
          ("connectedHalfDuplex10Mbps", 10),
          ("notConnected", 1),
          ("unknown", 65535))
    )


_Winlink1000OduEthernetIfOperStatus_Type.__name__ = "Integer32"
_Winlink1000OduEthernetIfOperStatus_Object = MibTableColumn
winlink1000OduEthernetIfOperStatus = _Winlink1000OduEthernetIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3, 2, 1, 7),
    _Winlink1000OduEthernetIfOperStatus_Type()
)
winlink1000OduEthernetIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduEthernetIfOperStatus.setStatus("mandatory")


class _Winlink1000OduEthernetIfFailAction_Type(Integer32):
    """Custom type winlink1000OduEthernetIfFailAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              11,
              255)
        )
    )
    namedValues = NamedValues(
        *(("faDisablePort", 255),
          ("faForceFullDuplex10Mbps", 11),
          ("faForceHalfDuplex10Mbps", 10),
          ("faNoAction", 1))
    )


_Winlink1000OduEthernetIfFailAction_Type.__name__ = "Integer32"
_Winlink1000OduEthernetIfFailAction_Object = MibTableColumn
winlink1000OduEthernetIfFailAction = _Winlink1000OduEthernetIfFailAction_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3, 2, 1, 8),
    _Winlink1000OduEthernetIfFailAction_Type()
)
winlink1000OduEthernetIfFailAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduEthernetIfFailAction.setStatus("mandatory")
_Winlink1000OduEthernetIf1588v2PTPEventRXRate_Type = Integer32
_Winlink1000OduEthernetIf1588v2PTPEventRXRate_Object = MibTableColumn
winlink1000OduEthernetIf1588v2PTPEventRXRate = _Winlink1000OduEthernetIf1588v2PTPEventRXRate_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3, 2, 1, 9),
    _Winlink1000OduEthernetIf1588v2PTPEventRXRate_Type()
)
winlink1000OduEthernetIf1588v2PTPEventRXRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduEthernetIf1588v2PTPEventRXRate.setStatus("mandatory")
_Winlink1000OduEthernetIf1588v2PTPEventTXRate_Type = Integer32
_Winlink1000OduEthernetIf1588v2PTPEventTXRate_Object = MibTableColumn
winlink1000OduEthernetIf1588v2PTPEventTXRate = _Winlink1000OduEthernetIf1588v2PTPEventTXRate_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3, 2, 1, 10),
    _Winlink1000OduEthernetIf1588v2PTPEventTXRate_Type()
)
winlink1000OduEthernetIf1588v2PTPEventTXRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduEthernetIf1588v2PTPEventTXRate.setStatus("mandatory")
_Winlink1000OduEthernetNumOfPorts_Type = Integer32
_Winlink1000OduEthernetNumOfPorts_Object = MibScalar
winlink1000OduEthernetNumOfPorts = _Winlink1000OduEthernetNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3, 3),
    _Winlink1000OduEthernetNumOfPorts_Type()
)
winlink1000OduEthernetNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduEthernetNumOfPorts.setStatus("mandatory")


class _Winlink1000OduEthernetGbeSupported_Type(Integer32):
    """Custom type winlink1000OduEthernetGbeSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_Winlink1000OduEthernetGbeSupported_Type.__name__ = "Integer32"
_Winlink1000OduEthernetGbeSupported_Object = MibScalar
winlink1000OduEthernetGbeSupported = _Winlink1000OduEthernetGbeSupported_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3, 4),
    _Winlink1000OduEthernetGbeSupported_Type()
)
winlink1000OduEthernetGbeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduEthernetGbeSupported.setStatus("mandatory")
_Winlink1000OduEthernetSfpProperties_Type = DisplayString
_Winlink1000OduEthernetSfpProperties_Object = MibScalar
winlink1000OduEthernetSfpProperties = _Winlink1000OduEthernetSfpProperties_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 3, 5),
    _Winlink1000OduEthernetSfpProperties_Type()
)
winlink1000OduEthernetSfpProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduEthernetSfpProperties.setStatus("mandatory")
_Winlink1000OduBridge_ObjectIdentity = ObjectIdentity
winlink1000OduBridge = _Winlink1000OduBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4)
)
_Winlink1000OduBridgeBase_ObjectIdentity = ObjectIdentity
winlink1000OduBridgeBase = _Winlink1000OduBridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 1)
)
_Winlink1000OduBridgeBasePortTable_Object = MibTable
winlink1000OduBridgeBasePortTable = _Winlink1000OduBridgeBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    winlink1000OduBridgeBasePortTable.setStatus("mandatory")
_Winlink1000OduBridgeBasePortEntry_Object = MibTableRow
winlink1000OduBridgeBasePortEntry = _Winlink1000OduBridgeBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 1, 4, 1)
)
winlink1000OduBridgeBasePortEntry.setIndexNames(
    (0, "RADWIN-MIB-WINLINK1000", "winlink1000OduBridgeBasePortIndex"),
)
if mibBuilder.loadTexts:
    winlink1000OduBridgeBasePortEntry.setStatus("mandatory")
_Winlink1000OduBridgeBasePortIndex_Type = Integer32
_Winlink1000OduBridgeBasePortIndex_Object = MibTableColumn
winlink1000OduBridgeBasePortIndex = _Winlink1000OduBridgeBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 1, 4, 1, 1),
    _Winlink1000OduBridgeBasePortIndex_Type()
)
winlink1000OduBridgeBasePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduBridgeBasePortIndex.setStatus("mandatory")
_Winlink1000OduBridgeBaseIfIndex_Type = Integer32
_Winlink1000OduBridgeBaseIfIndex_Object = MibTableColumn
winlink1000OduBridgeBaseIfIndex = _Winlink1000OduBridgeBaseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 1, 4, 1, 2),
    _Winlink1000OduBridgeBaseIfIndex_Type()
)
winlink1000OduBridgeBaseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduBridgeBaseIfIndex.setStatus("mandatory")
_Winlink1000OduBridgeTp_ObjectIdentity = ObjectIdentity
winlink1000OduBridgeTp = _Winlink1000OduBridgeTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 4)
)
_Winlink1000OduBridgeTpPortTable_Object = MibTable
winlink1000OduBridgeTpPortTable = _Winlink1000OduBridgeTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 4, 3)
)
if mibBuilder.loadTexts:
    winlink1000OduBridgeTpPortTable.setStatus("mandatory")
_Winlink1000OduBridgeTpPortEntry_Object = MibTableRow
winlink1000OduBridgeTpPortEntry = _Winlink1000OduBridgeTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 4, 3, 1)
)
winlink1000OduBridgeTpPortEntry.setIndexNames(
    (0, "RADWIN-MIB-WINLINK1000", "winlink1000OduBridgeTpPortIndex"),
)
if mibBuilder.loadTexts:
    winlink1000OduBridgeTpPortEntry.setStatus("mandatory")
_Winlink1000OduBridgeTpPortIndex_Type = Integer32
_Winlink1000OduBridgeTpPortIndex_Object = MibTableColumn
winlink1000OduBridgeTpPortIndex = _Winlink1000OduBridgeTpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 4, 3, 1, 1),
    _Winlink1000OduBridgeTpPortIndex_Type()
)
winlink1000OduBridgeTpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduBridgeTpPortIndex.setStatus("mandatory")
_Winlink1000OduBridgeTpPortInFrames_Type = Counter32
_Winlink1000OduBridgeTpPortInFrames_Object = MibTableColumn
winlink1000OduBridgeTpPortInFrames = _Winlink1000OduBridgeTpPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 4, 3, 1, 3),
    _Winlink1000OduBridgeTpPortInFrames_Type()
)
winlink1000OduBridgeTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduBridgeTpPortInFrames.setStatus("mandatory")
_Winlink1000OduBridgeTpPortOutFrames_Type = Counter32
_Winlink1000OduBridgeTpPortOutFrames_Object = MibTableColumn
winlink1000OduBridgeTpPortOutFrames = _Winlink1000OduBridgeTpPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 4, 3, 1, 4),
    _Winlink1000OduBridgeTpPortOutFrames_Type()
)
winlink1000OduBridgeTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduBridgeTpPortOutFrames.setStatus("mandatory")
_Winlink1000OduBridgeTpPortInBytes_Type = Counter32
_Winlink1000OduBridgeTpPortInBytes_Object = MibTableColumn
winlink1000OduBridgeTpPortInBytes = _Winlink1000OduBridgeTpPortInBytes_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 4, 3, 1, 101),
    _Winlink1000OduBridgeTpPortInBytes_Type()
)
winlink1000OduBridgeTpPortInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduBridgeTpPortInBytes.setStatus("mandatory")
_Winlink1000OduBridgeTpPortOutBytes_Type = Counter32
_Winlink1000OduBridgeTpPortOutBytes_Object = MibTableColumn
winlink1000OduBridgeTpPortOutBytes = _Winlink1000OduBridgeTpPortOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 4, 3, 1, 102),
    _Winlink1000OduBridgeTpPortOutBytes_Type()
)
winlink1000OduBridgeTpPortOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduBridgeTpPortOutBytes.setStatus("mandatory")
_Winlink1000OduBridgeTpMode_Type = Integer32
_Winlink1000OduBridgeTpMode_Object = MibScalar
winlink1000OduBridgeTpMode = _Winlink1000OduBridgeTpMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 4, 101),
    _Winlink1000OduBridgeTpMode_Type()
)
winlink1000OduBridgeTpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduBridgeTpMode.setStatus("mandatory")


class _Winlink1000OduBridgeConfigMode_Type(Integer32):
    """Custom type winlink1000OduBridgeConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Winlink1000OduBridgeConfigMode_Type.__name__ = "Integer32"
_Winlink1000OduBridgeConfigMode_Object = MibScalar
winlink1000OduBridgeConfigMode = _Winlink1000OduBridgeConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 4, 4, 102),
    _Winlink1000OduBridgeConfigMode_Type()
)
winlink1000OduBridgeConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduBridgeConfigMode.setStatus("mandatory")
_Winlink1000OduAir_ObjectIdentity = ObjectIdentity
winlink1000OduAir = _Winlink1000OduAir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5)
)
_Winlink1000OduAirFreq_Type = Integer32
_Winlink1000OduAirFreq_Object = MibScalar
winlink1000OduAirFreq = _Winlink1000OduAirFreq_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 1),
    _Winlink1000OduAirFreq_Type()
)
winlink1000OduAirFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirFreq.setStatus("mandatory")
_Winlink1000OduAirDesiredRate_Type = Integer32
_Winlink1000OduAirDesiredRate_Object = MibScalar
winlink1000OduAirDesiredRate = _Winlink1000OduAirDesiredRate_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 2),
    _Winlink1000OduAirDesiredRate_Type()
)
winlink1000OduAirDesiredRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirDesiredRate.setStatus("deprecated")
_Winlink1000OduAirSSID_Type = DisplayString
_Winlink1000OduAirSSID_Object = MibScalar
winlink1000OduAirSSID = _Winlink1000OduAirSSID_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 3),
    _Winlink1000OduAirSSID_Type()
)
winlink1000OduAirSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirSSID.setStatus("mandatory")
_Winlink1000OduAirTxPower_Type = Integer32
_Winlink1000OduAirTxPower_Object = MibScalar
winlink1000OduAirTxPower = _Winlink1000OduAirTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 4),
    _Winlink1000OduAirTxPower_Type()
)
winlink1000OduAirTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirTxPower.setStatus("mandatory")


class _Winlink1000OduAirSesState_Type(Integer32):
    """Custom type winlink1000OduAirSesState based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("activeWithDefaultEncryptionKey", 8),
          ("activeWithVersionsMismatch", 11),
          ("basicRate", 2),
          ("bitFailed", 10),
          ("iduIncompatible", 14),
          ("inactive", 13),
          ("installation", 4),
          ("installationWithDefaultEncryptionKey", 9),
          ("installationWithVersionsMismatch", 12),
          ("probing", 6),
          ("scanning", 5),
          ("sessionDown", 1),
          ("spectrumAnalysis", 15),
          ("transmitting", 7))
    )


_Winlink1000OduAirSesState_Type.__name__ = "Integer32"
_Winlink1000OduAirSesState_Object = MibScalar
winlink1000OduAirSesState = _Winlink1000OduAirSesState_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 5),
    _Winlink1000OduAirSesState_Type()
)
winlink1000OduAirSesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirSesState.setStatus("mandatory")
_Winlink1000OduAirMstrSlv_Type = Integer32
_Winlink1000OduAirMstrSlv_Object = MibScalar
winlink1000OduAirMstrSlv = _Winlink1000OduAirMstrSlv_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 6),
    _Winlink1000OduAirMstrSlv_Type()
)
winlink1000OduAirMstrSlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirMstrSlv.setStatus("mandatory")
_Winlink1000OduAirResync_Type = Integer32
_Winlink1000OduAirResync_Object = MibScalar
winlink1000OduAirResync = _Winlink1000OduAirResync_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 8),
    _Winlink1000OduAirResync_Type()
)
winlink1000OduAirResync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirResync.setStatus("mandatory")
_Winlink1000OduAirPerf_ObjectIdentity = ObjectIdentity
winlink1000OduAirPerf = _Winlink1000OduAirPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 9)
)
_Winlink1000OduAirRxPower_Type = Integer32
_Winlink1000OduAirRxPower_Object = MibScalar
winlink1000OduAirRxPower = _Winlink1000OduAirRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 9, 1),
    _Winlink1000OduAirRxPower_Type()
)
winlink1000OduAirRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirRxPower.setStatus("mandatory")
_Winlink1000OduAirTotalFrames_Type = Counter32
_Winlink1000OduAirTotalFrames_Object = MibScalar
winlink1000OduAirTotalFrames = _Winlink1000OduAirTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 9, 2),
    _Winlink1000OduAirTotalFrames_Type()
)
winlink1000OduAirTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirTotalFrames.setStatus("mandatory")
_Winlink1000OduAirBadFrames_Type = Counter32
_Winlink1000OduAirBadFrames_Object = MibScalar
winlink1000OduAirBadFrames = _Winlink1000OduAirBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 9, 3),
    _Winlink1000OduAirBadFrames_Type()
)
winlink1000OduAirBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirBadFrames.setStatus("mandatory")
_Winlink1000OduAirCurrentRate_Type = Integer32
_Winlink1000OduAirCurrentRate_Object = MibScalar
winlink1000OduAirCurrentRate = _Winlink1000OduAirCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 9, 4),
    _Winlink1000OduAirCurrentRate_Type()
)
winlink1000OduAirCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirCurrentRate.setStatus("deprecated")
_Winlink1000OduAirCurrentRateIdx_Type = Integer32
_Winlink1000OduAirCurrentRateIdx_Object = MibScalar
winlink1000OduAirCurrentRateIdx = _Winlink1000OduAirCurrentRateIdx_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 9, 5),
    _Winlink1000OduAirCurrentRateIdx_Type()
)
winlink1000OduAirCurrentRateIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirCurrentRateIdx.setStatus("mandatory")
_Winlink1000OduAirChainsRxPower_Type = OctetString
_Winlink1000OduAirChainsRxPower_Object = MibScalar
winlink1000OduAirChainsRxPower = _Winlink1000OduAirChainsRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 9, 6),
    _Winlink1000OduAirChainsRxPower_Type()
)
winlink1000OduAirChainsRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirChainsRxPower.setStatus("mandatory")
_Winlink1000OduAirCurrentRateCBW_Type = Integer32
_Winlink1000OduAirCurrentRateCBW_Object = MibScalar
winlink1000OduAirCurrentRateCBW = _Winlink1000OduAirCurrentRateCBW_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 9, 7),
    _Winlink1000OduAirCurrentRateCBW_Type()
)
winlink1000OduAirCurrentRateCBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirCurrentRateCBW.setStatus("mandatory")
_Winlink1000OduAirCurrentRateGI_Type = Integer32
_Winlink1000OduAirCurrentRateGI_Object = MibScalar
winlink1000OduAirCurrentRateGI = _Winlink1000OduAirCurrentRateGI_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 9, 8),
    _Winlink1000OduAirCurrentRateGI_Type()
)
winlink1000OduAirCurrentRateGI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirCurrentRateGI.setStatus("mandatory")
_Winlink1000OduAirTxPower36_Type = Integer32
_Winlink1000OduAirTxPower36_Object = MibScalar
winlink1000OduAirTxPower36 = _Winlink1000OduAirTxPower36_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 10),
    _Winlink1000OduAirTxPower36_Type()
)
winlink1000OduAirTxPower36.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirTxPower36.setStatus("deprecated")
_Winlink1000OduAirTxPower48_Type = Integer32
_Winlink1000OduAirTxPower48_Object = MibScalar
winlink1000OduAirTxPower48 = _Winlink1000OduAirTxPower48_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 11),
    _Winlink1000OduAirTxPower48_Type()
)
winlink1000OduAirTxPower48.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirTxPower48.setStatus("deprecated")
_Winlink1000OduAirCurrentTxPower_Type = Integer32
_Winlink1000OduAirCurrentTxPower_Object = MibScalar
winlink1000OduAirCurrentTxPower = _Winlink1000OduAirCurrentTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 12),
    _Winlink1000OduAirCurrentTxPower_Type()
)
winlink1000OduAirCurrentTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirCurrentTxPower.setStatus("mandatory")
_Winlink1000OduAirMinFrequency_Type = Integer32
_Winlink1000OduAirMinFrequency_Object = MibScalar
winlink1000OduAirMinFrequency = _Winlink1000OduAirMinFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 13),
    _Winlink1000OduAirMinFrequency_Type()
)
winlink1000OduAirMinFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirMinFrequency.setStatus("mandatory")
_Winlink1000OduAirMaxFrequency_Type = Integer32
_Winlink1000OduAirMaxFrequency_Object = MibScalar
winlink1000OduAirMaxFrequency = _Winlink1000OduAirMaxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 14),
    _Winlink1000OduAirMaxFrequency_Type()
)
winlink1000OduAirMaxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirMaxFrequency.setStatus("mandatory")
_Winlink1000OduAirFreqResolution_Type = Integer32
_Winlink1000OduAirFreqResolution_Object = MibScalar
winlink1000OduAirFreqResolution = _Winlink1000OduAirFreqResolution_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 15),
    _Winlink1000OduAirFreqResolution_Type()
)
winlink1000OduAirFreqResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirFreqResolution.setStatus("mandatory")
_Winlink1000OduAirCurrentFreq_Type = Integer32
_Winlink1000OduAirCurrentFreq_Object = MibScalar
winlink1000OduAirCurrentFreq = _Winlink1000OduAirCurrentFreq_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 16),
    _Winlink1000OduAirCurrentFreq_Type()
)
winlink1000OduAirCurrentFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirCurrentFreq.setStatus("mandatory")
_Winlink1000OduAirNumberOfChannels_Type = Integer32
_Winlink1000OduAirNumberOfChannels_Object = MibScalar
winlink1000OduAirNumberOfChannels = _Winlink1000OduAirNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 17),
    _Winlink1000OduAirNumberOfChannels_Type()
)
winlink1000OduAirNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirNumberOfChannels.setStatus("mandatory")
_Winlink1000OduAirChannelsTable_Object = MibTable
winlink1000OduAirChannelsTable = _Winlink1000OduAirChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 18)
)
if mibBuilder.loadTexts:
    winlink1000OduAirChannelsTable.setStatus("mandatory")
_Winlink1000OduAirChannelsEntry_Object = MibTableRow
winlink1000OduAirChannelsEntry = _Winlink1000OduAirChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 18, 1)
)
winlink1000OduAirChannelsEntry.setIndexNames(
    (0, "RADWIN-MIB-WINLINK1000", "winlink1000OduAirChannelsIndex"),
)
if mibBuilder.loadTexts:
    winlink1000OduAirChannelsEntry.setStatus("mandatory")
_Winlink1000OduAirChannelsIndex_Type = Integer32
_Winlink1000OduAirChannelsIndex_Object = MibTableColumn
winlink1000OduAirChannelsIndex = _Winlink1000OduAirChannelsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 18, 1, 1),
    _Winlink1000OduAirChannelsIndex_Type()
)
winlink1000OduAirChannelsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirChannelsIndex.setStatus("mandatory")
_Winlink1000OduAirChannelsFrequency_Type = Integer32
_Winlink1000OduAirChannelsFrequency_Object = MibTableColumn
winlink1000OduAirChannelsFrequency = _Winlink1000OduAirChannelsFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 18, 1, 2),
    _Winlink1000OduAirChannelsFrequency_Type()
)
winlink1000OduAirChannelsFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirChannelsFrequency.setStatus("mandatory")
_Winlink1000OduAirChannelsOperState_Type = Integer32
_Winlink1000OduAirChannelsOperState_Object = MibTableColumn
winlink1000OduAirChannelsOperState = _Winlink1000OduAirChannelsOperState_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 18, 1, 3),
    _Winlink1000OduAirChannelsOperState_Type()
)
winlink1000OduAirChannelsOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirChannelsOperState.setStatus("mandatory")
_Winlink1000OduAirChannelsAvail_Type = Integer32
_Winlink1000OduAirChannelsAvail_Object = MibTableColumn
winlink1000OduAirChannelsAvail = _Winlink1000OduAirChannelsAvail_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 18, 1, 4),
    _Winlink1000OduAirChannelsAvail_Type()
)
winlink1000OduAirChannelsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirChannelsAvail.setStatus("mandatory")
_Winlink1000OduAirChannelsDefaultFreq_Type = Integer32
_Winlink1000OduAirChannelsDefaultFreq_Object = MibTableColumn
winlink1000OduAirChannelsDefaultFreq = _Winlink1000OduAirChannelsDefaultFreq_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 18, 1, 5),
    _Winlink1000OduAirChannelsDefaultFreq_Type()
)
winlink1000OduAirChannelsDefaultFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirChannelsDefaultFreq.setStatus("mandatory")
_Winlink1000OduAirDfsState_Type = Integer32
_Winlink1000OduAirDfsState_Object = MibScalar
winlink1000OduAirDfsState = _Winlink1000OduAirDfsState_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 19),
    _Winlink1000OduAirDfsState_Type()
)
winlink1000OduAirDfsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirDfsState.setStatus("mandatory")
_Winlink1000OduAirAutoChannelSelectionState_Type = Integer32
_Winlink1000OduAirAutoChannelSelectionState_Object = MibScalar
winlink1000OduAirAutoChannelSelectionState = _Winlink1000OduAirAutoChannelSelectionState_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 20),
    _Winlink1000OduAirAutoChannelSelectionState_Type()
)
winlink1000OduAirAutoChannelSelectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirAutoChannelSelectionState.setStatus("deprecated")


class _Winlink1000OduAirEnableTxPower_Type(Integer32):
    """Custom type winlink1000OduAirEnableTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Winlink1000OduAirEnableTxPower_Type.__name__ = "Integer32"
_Winlink1000OduAirEnableTxPower_Object = MibScalar
winlink1000OduAirEnableTxPower = _Winlink1000OduAirEnableTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 21),
    _Winlink1000OduAirEnableTxPower_Type()
)
winlink1000OduAirEnableTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirEnableTxPower.setStatus("mandatory")
_Winlink1000OduAirMinTxPower_Type = Integer32
_Winlink1000OduAirMinTxPower_Object = MibScalar
winlink1000OduAirMinTxPower = _Winlink1000OduAirMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 22),
    _Winlink1000OduAirMinTxPower_Type()
)
winlink1000OduAirMinTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirMinTxPower.setStatus("mandatory")
_Winlink1000OduAirMaxTxPowerTable_Object = MibTable
winlink1000OduAirMaxTxPowerTable = _Winlink1000OduAirMaxTxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 23)
)
if mibBuilder.loadTexts:
    winlink1000OduAirMaxTxPowerTable.setStatus("mandatory")
_Winlink1000OduAirMaxTxPowerEntry_Object = MibTableRow
winlink1000OduAirMaxTxPowerEntry = _Winlink1000OduAirMaxTxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 23, 1)
)
winlink1000OduAirMaxTxPowerEntry.setIndexNames(
    (0, "RADWIN-MIB-WINLINK1000", "winlink1000OduAirMaxTxPowerIndex"),
)
if mibBuilder.loadTexts:
    winlink1000OduAirMaxTxPowerEntry.setStatus("mandatory")
_Winlink1000OduAirMaxTxPowerIndex_Type = Integer32
_Winlink1000OduAirMaxTxPowerIndex_Object = MibTableColumn
winlink1000OduAirMaxTxPowerIndex = _Winlink1000OduAirMaxTxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 23, 1, 1),
    _Winlink1000OduAirMaxTxPowerIndex_Type()
)
winlink1000OduAirMaxTxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirMaxTxPowerIndex.setStatus("mandatory")
_Winlink1000OduAirMaxTxPower_Type = Integer32
_Winlink1000OduAirMaxTxPower_Object = MibTableColumn
winlink1000OduAirMaxTxPower = _Winlink1000OduAirMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 23, 1, 2),
    _Winlink1000OduAirMaxTxPower_Type()
)
winlink1000OduAirMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirMaxTxPower.setStatus("mandatory")
_Winlink1000OduAirChannelBandwidth_Type = Integer32
_Winlink1000OduAirChannelBandwidth_Object = MibScalar
winlink1000OduAirChannelBandwidth = _Winlink1000OduAirChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 24),
    _Winlink1000OduAirChannelBandwidth_Type()
)
winlink1000OduAirChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirChannelBandwidth.setStatus("mandatory")
_Winlink1000OduAirChannelBWTable_Object = MibTable
winlink1000OduAirChannelBWTable = _Winlink1000OduAirChannelBWTable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 25)
)
if mibBuilder.loadTexts:
    winlink1000OduAirChannelBWTable.setStatus("mandatory")
_Winlink1000OduAirChannelBWEntry_Object = MibTableRow
winlink1000OduAirChannelBWEntry = _Winlink1000OduAirChannelBWEntry_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 25, 1)
)
winlink1000OduAirChannelBWEntry.setIndexNames(
    (0, "RADWIN-MIB-WINLINK1000", "winlink1000OduAirChannelBWIndex"),
)
if mibBuilder.loadTexts:
    winlink1000OduAirChannelBWEntry.setStatus("mandatory")


class _Winlink1000OduAirChannelBWIndex_Type(Integer32):
    """Custom type winlink1000OduAirChannelBWIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("channelBW10MHz", 2),
          ("channelBW14MHz", 7),
          ("channelBW20MHz", 3),
          ("channelBW40MHz", 4),
          ("channelBW5MHz", 1),
          ("channelBW7MHz", 6),
          ("channelBW80MHz", 5))
    )


_Winlink1000OduAirChannelBWIndex_Type.__name__ = "Integer32"
_Winlink1000OduAirChannelBWIndex_Object = MibTableColumn
winlink1000OduAirChannelBWIndex = _Winlink1000OduAirChannelBWIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 25, 1, 1),
    _Winlink1000OduAirChannelBWIndex_Type()
)
winlink1000OduAirChannelBWIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirChannelBWIndex.setStatus("mandatory")


class _Winlink1000OduAirChannelBWAvail_Type(Integer32):
    """Custom type winlink1000OduAirChannelBWAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supportedManual", 2),
          ("supportedWithACS", 3))
    )


_Winlink1000OduAirChannelBWAvail_Type.__name__ = "Integer32"
_Winlink1000OduAirChannelBWAvail_Object = MibTableColumn
winlink1000OduAirChannelBWAvail = _Winlink1000OduAirChannelBWAvail_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 25, 1, 2),
    _Winlink1000OduAirChannelBWAvail_Type()
)
winlink1000OduAirChannelBWAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirChannelBWAvail.setStatus("mandatory")
_Winlink1000OduAirChannelsAdminState_Type = DisplayString
_Winlink1000OduAirChannelsAdminState_Object = MibTableColumn
winlink1000OduAirChannelsAdminState = _Winlink1000OduAirChannelsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 25, 1, 3),
    _Winlink1000OduAirChannelsAdminState_Type()
)
winlink1000OduAirChannelsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirChannelsAdminState.setStatus("mandatory")


class _Winlink1000OduAirChannelBWHSSATDDConflictPerCBW_Type(Integer32):
    """Custom type winlink1000OduAirChannelBWHSSATDDConflictPerCBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("conflictDual", 3),
          ("conflictSingle", 2),
          ("noConflict", 1))
    )


_Winlink1000OduAirChannelBWHSSATDDConflictPerCBW_Type.__name__ = "Integer32"
_Winlink1000OduAirChannelBWHSSATDDConflictPerCBW_Object = MibTableColumn
winlink1000OduAirChannelBWHSSATDDConflictPerCBW = _Winlink1000OduAirChannelBWHSSATDDConflictPerCBW_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 25, 1, 4),
    _Winlink1000OduAirChannelBWHSSATDDConflictPerCBW_Type()
)
winlink1000OduAirChannelBWHSSATDDConflictPerCBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirChannelBWHSSATDDConflictPerCBW.setStatus("mandatory")
_Winlink1000OduAirChannelBWMinRatioForSupporting_Type = Integer32
_Winlink1000OduAirChannelBWMinRatioForSupporting_Object = MibTableColumn
winlink1000OduAirChannelBWMinRatioForSupporting = _Winlink1000OduAirChannelBWMinRatioForSupporting_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 25, 1, 5),
    _Winlink1000OduAirChannelBWMinRatioForSupporting_Type()
)
winlink1000OduAirChannelBWMinRatioForSupporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirChannelBWMinRatioForSupporting.setStatus("mandatory")
_Winlink1000OduAirChannelBWMaxRatioForSupporting_Type = Integer32
_Winlink1000OduAirChannelBWMaxRatioForSupporting_Object = MibTableColumn
winlink1000OduAirChannelBWMaxRatioForSupporting = _Winlink1000OduAirChannelBWMaxRatioForSupporting_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 25, 1, 6),
    _Winlink1000OduAirChannelBWMaxRatioForSupporting_Type()
)
winlink1000OduAirChannelBWMaxRatioForSupporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirChannelBWMaxRatioForSupporting.setStatus("mandatory")
_Winlink1000OduAirRFD_Type = Integer32
_Winlink1000OduAirRFD_Object = MibScalar
winlink1000OduAirRFD = _Winlink1000OduAirRFD_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 26),
    _Winlink1000OduAirRFD_Type()
)
winlink1000OduAirRFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirRFD.setStatus("mandatory")
_Winlink1000OduAirRatesTable_Object = MibTable
winlink1000OduAirRatesTable = _Winlink1000OduAirRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 27)
)
if mibBuilder.loadTexts:
    winlink1000OduAirRatesTable.setStatus("mandatory")
_Winlink1000OduAirRatesEntry_Object = MibTableRow
winlink1000OduAirRatesEntry = _Winlink1000OduAirRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 27, 1)
)
winlink1000OduAirRatesEntry.setIndexNames(
    (0, "RADWIN-MIB-WINLINK1000", "winlink1000OduAirRatesIndex"),
)
if mibBuilder.loadTexts:
    winlink1000OduAirRatesEntry.setStatus("mandatory")
_Winlink1000OduAirRatesIndex_Type = Integer32
_Winlink1000OduAirRatesIndex_Object = MibTableColumn
winlink1000OduAirRatesIndex = _Winlink1000OduAirRatesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 27, 1, 1),
    _Winlink1000OduAirRatesIndex_Type()
)
winlink1000OduAirRatesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirRatesIndex.setStatus("mandatory")


class _Winlink1000OduAirRatesAvail_Type(Integer32):
    """Custom type winlink1000OduAirRatesAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rateAvailable", 2),
          ("rateNotAvailable", 1))
    )


_Winlink1000OduAirRatesAvail_Type.__name__ = "Integer32"
_Winlink1000OduAirRatesAvail_Object = MibTableColumn
winlink1000OduAirRatesAvail = _Winlink1000OduAirRatesAvail_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 27, 1, 2),
    _Winlink1000OduAirRatesAvail_Type()
)
winlink1000OduAirRatesAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirRatesAvail.setStatus("mandatory")
_Winlink1000OduAirDesiredRateIdx_Type = Integer32
_Winlink1000OduAirDesiredRateIdx_Object = MibScalar
winlink1000OduAirDesiredRateIdx = _Winlink1000OduAirDesiredRateIdx_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 28),
    _Winlink1000OduAirDesiredRateIdx_Type()
)
winlink1000OduAirDesiredRateIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirDesiredRateIdx.setStatus("mandatory")
_Winlink1000OduAirLinkDistance_Type = Integer32
_Winlink1000OduAirLinkDistance_Object = MibScalar
winlink1000OduAirLinkDistance = _Winlink1000OduAirLinkDistance_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 29),
    _Winlink1000OduAirLinkDistance_Type()
)
winlink1000OduAirLinkDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirLinkDistance.setStatus("mandatory")


class _Winlink1000OduAirLinkWorkingMode_Type(Integer32):
    """Custom type winlink1000OduAirLinkWorkingMode based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("fullCompatibilityLocalUpgradeAvailable", 4),
          ("fullCompatibilityRemoteUpgradeAvailable", 3),
          ("normal", 2),
          ("restrictedCompatibilityLocalUpgradeRecomended", 6),
          ("restrictedCompatibilityRemoteUpgradeRecomended", 5),
          ("softwareUpgradeLocalUpgradeRequired", 8),
          ("softwareUpgradeRemoteUpgradeRequired", 7),
          ("unknown", 1),
          ("versionsIncompatibilityLocalUpgradeRequired", 10),
          ("versionsIncompatibilityRemoteUpgradeRequired", 9))
    )


_Winlink1000OduAirLinkWorkingMode_Type.__name__ = "Integer32"
_Winlink1000OduAirLinkWorkingMode_Object = MibScalar
winlink1000OduAirLinkWorkingMode = _Winlink1000OduAirLinkWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 30),
    _Winlink1000OduAirLinkWorkingMode_Type()
)
winlink1000OduAirLinkWorkingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirLinkWorkingMode.setStatus("mandatory")
_Winlink1000OduAirMajorLinkIfVersion_Type = Integer32
_Winlink1000OduAirMajorLinkIfVersion_Object = MibScalar
winlink1000OduAirMajorLinkIfVersion = _Winlink1000OduAirMajorLinkIfVersion_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 31),
    _Winlink1000OduAirMajorLinkIfVersion_Type()
)
winlink1000OduAirMajorLinkIfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirMajorLinkIfVersion.setStatus("mandatory")
_Winlink1000OduAirMinorLinkIfVersion_Type = Integer32
_Winlink1000OduAirMinorLinkIfVersion_Object = MibScalar
winlink1000OduAirMinorLinkIfVersion = _Winlink1000OduAirMinorLinkIfVersion_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 32),
    _Winlink1000OduAirMinorLinkIfVersion_Type()
)
winlink1000OduAirMinorLinkIfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirMinorLinkIfVersion.setStatus("mandatory")
_Winlink1000OduAirHss_ObjectIdentity = ObjectIdentity
winlink1000OduAirHss = _Winlink1000OduAirHss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40)
)


class _Winlink1000OduAirHssDesiredOpState_Type(Integer32):
    """Custom type winlink1000OduAirHssDesiredOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("gpsSync", 6),
          ("hubSyncClientContinueTx", 4),
          ("hubSyncClientDisableTx", 5),
          ("hubSyncMaster", 3),
          ("independentSyncUnit-ISU", 7),
          ("independentUnit", 2),
          ("notSupported", 1))
    )


_Winlink1000OduAirHssDesiredOpState_Type.__name__ = "Integer32"
_Winlink1000OduAirHssDesiredOpState_Object = MibScalar
winlink1000OduAirHssDesiredOpState = _Winlink1000OduAirHssDesiredOpState_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 1),
    _Winlink1000OduAirHssDesiredOpState_Type()
)
winlink1000OduAirHssDesiredOpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirHssDesiredOpState.setStatus("mandatory")


class _Winlink1000OduAirHssCurrentOpState_Type(Integer32):
    """Custom type winlink1000OduAirHssCurrentOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("gpsSync", 6),
          ("hubSyncClientContinueTx", 4),
          ("hubSyncClientDisableTx", 5),
          ("hubSyncMaster", 3),
          ("independentSyncUnit-ISU", 7),
          ("independentUnit", 2),
          ("notSupported", 1))
    )


_Winlink1000OduAirHssCurrentOpState_Type.__name__ = "Integer32"
_Winlink1000OduAirHssCurrentOpState_Object = MibScalar
winlink1000OduAirHssCurrentOpState = _Winlink1000OduAirHssCurrentOpState_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 2),
    _Winlink1000OduAirHssCurrentOpState_Type()
)
winlink1000OduAirHssCurrentOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssCurrentOpState.setStatus("mandatory")


class _Winlink1000OduAirHssSyncStatus_Type(Integer32):
    """Custom type winlink1000OduAirHssSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("notSynchronized", 2),
          ("synchronized", 3))
    )


_Winlink1000OduAirHssSyncStatus_Type.__name__ = "Integer32"
_Winlink1000OduAirHssSyncStatus_Object = MibScalar
winlink1000OduAirHssSyncStatus = _Winlink1000OduAirHssSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 3),
    _Winlink1000OduAirHssSyncStatus_Type()
)
winlink1000OduAirHssSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssSyncStatus.setStatus("mandatory")


class _Winlink1000OduAirHssExtPulseStatus_Type(Integer32):
    """Custom type winlink1000OduAirHssExtPulseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("detected", 5),
          ("generating", 2),
          ("generatingAndDetected", 3),
          ("generatingAndImproperDetected", 4),
          ("improperDetected", 6),
          ("multipleSourcesDetected", 7),
          ("notDetected", 1))
    )


_Winlink1000OduAirHssExtPulseStatus_Type.__name__ = "Integer32"
_Winlink1000OduAirHssExtPulseStatus_Object = MibScalar
winlink1000OduAirHssExtPulseStatus = _Winlink1000OduAirHssExtPulseStatus_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 4),
    _Winlink1000OduAirHssExtPulseStatus_Type()
)
winlink1000OduAirHssExtPulseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssExtPulseStatus.setStatus("mandatory")


class _Winlink1000OduAirHssExtPulseType_Type(Integer32):
    """Custom type winlink1000OduAirHssExtPulseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("typeA", 2),
          ("typeB", 3),
          ("typeC", 4),
          ("typeD", 5),
          ("typeE", 6),
          ("typeF", 7))
    )


_Winlink1000OduAirHssExtPulseType_Type.__name__ = "Integer32"
_Winlink1000OduAirHssExtPulseType_Object = MibScalar
winlink1000OduAirHssExtPulseType = _Winlink1000OduAirHssExtPulseType_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 5),
    _Winlink1000OduAirHssExtPulseType_Type()
)
winlink1000OduAirHssExtPulseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssExtPulseType.setStatus("mandatory")


class _Winlink1000OduAirHssDesiredExtPulseType_Type(Integer32):
    """Custom type winlink1000OduAirHssDesiredExtPulseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("typeA", 2),
          ("typeB", 3),
          ("typeC", 4),
          ("typeD", 5),
          ("typeE", 6),
          ("typeF", 7))
    )


_Winlink1000OduAirHssDesiredExtPulseType_Type.__name__ = "Integer32"
_Winlink1000OduAirHssDesiredExtPulseType_Object = MibScalar
winlink1000OduAirHssDesiredExtPulseType = _Winlink1000OduAirHssDesiredExtPulseType_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 6),
    _Winlink1000OduAirHssDesiredExtPulseType_Type()
)
winlink1000OduAirHssDesiredExtPulseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirHssDesiredExtPulseType.setStatus("mandatory")
_Winlink1000OduAirHssRfpTable_Object = MibTable
winlink1000OduAirHssRfpTable = _Winlink1000OduAirHssRfpTable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7)
)
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpTable.setStatus("mandatory")
_Winlink1000OduAirHssRfpEntry_Object = MibTableRow
winlink1000OduAirHssRfpEntry = _Winlink1000OduAirHssRfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7, 1)
)
winlink1000OduAirHssRfpEntry.setIndexNames(
    (0, "RADWIN-MIB-WINLINK1000", "winlink1000OduAirHssRfpIndex"),
)
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpEntry.setStatus("mandatory")


class _Winlink1000OduAirHssRfpIndex_Type(Integer32):
    """Custom type winlink1000OduAirHssRfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_Winlink1000OduAirHssRfpIndex_Type.__name__ = "Integer32"
_Winlink1000OduAirHssRfpIndex_Object = MibTableColumn
winlink1000OduAirHssRfpIndex = _Winlink1000OduAirHssRfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7, 1, 1),
    _Winlink1000OduAirHssRfpIndex_Type()
)
winlink1000OduAirHssRfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpIndex.setStatus("mandatory")


class _Winlink1000OduAirHssRfpEthChannelBW5MHz_Type(Integer32):
    """Custom type winlink1000OduAirHssRfpEthChannelBW5MHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestFit", 1),
          ("nonOptimal", 2),
          ("notAvailable", 3))
    )


_Winlink1000OduAirHssRfpEthChannelBW5MHz_Type.__name__ = "Integer32"
_Winlink1000OduAirHssRfpEthChannelBW5MHz_Object = MibTableColumn
winlink1000OduAirHssRfpEthChannelBW5MHz = _Winlink1000OduAirHssRfpEthChannelBW5MHz_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7, 1, 2),
    _Winlink1000OduAirHssRfpEthChannelBW5MHz_Type()
)
winlink1000OduAirHssRfpEthChannelBW5MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpEthChannelBW5MHz.setStatus("mandatory")


class _Winlink1000OduAirHssRfpTdmChannelBW5MHz_Type(Integer32):
    """Custom type winlink1000OduAirHssRfpTdmChannelBW5MHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestFit", 1),
          ("nonOptimal", 2),
          ("notAvailable", 3))
    )


_Winlink1000OduAirHssRfpTdmChannelBW5MHz_Type.__name__ = "Integer32"
_Winlink1000OduAirHssRfpTdmChannelBW5MHz_Object = MibTableColumn
winlink1000OduAirHssRfpTdmChannelBW5MHz = _Winlink1000OduAirHssRfpTdmChannelBW5MHz_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7, 1, 3),
    _Winlink1000OduAirHssRfpTdmChannelBW5MHz_Type()
)
winlink1000OduAirHssRfpTdmChannelBW5MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpTdmChannelBW5MHz.setStatus("mandatory")


class _Winlink1000OduAirHssRfpEthChannelBW10MHz_Type(Integer32):
    """Custom type winlink1000OduAirHssRfpEthChannelBW10MHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestFit", 1),
          ("nonOptimal", 2),
          ("notAvailable", 3))
    )


_Winlink1000OduAirHssRfpEthChannelBW10MHz_Type.__name__ = "Integer32"
_Winlink1000OduAirHssRfpEthChannelBW10MHz_Object = MibTableColumn
winlink1000OduAirHssRfpEthChannelBW10MHz = _Winlink1000OduAirHssRfpEthChannelBW10MHz_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7, 1, 4),
    _Winlink1000OduAirHssRfpEthChannelBW10MHz_Type()
)
winlink1000OduAirHssRfpEthChannelBW10MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpEthChannelBW10MHz.setStatus("mandatory")


class _Winlink1000OduAirHssRfpTdmChannelBW10MHz_Type(Integer32):
    """Custom type winlink1000OduAirHssRfpTdmChannelBW10MHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestFit", 1),
          ("nonOptimal", 2),
          ("notAvailable", 3))
    )


_Winlink1000OduAirHssRfpTdmChannelBW10MHz_Type.__name__ = "Integer32"
_Winlink1000OduAirHssRfpTdmChannelBW10MHz_Object = MibTableColumn
winlink1000OduAirHssRfpTdmChannelBW10MHz = _Winlink1000OduAirHssRfpTdmChannelBW10MHz_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7, 1, 5),
    _Winlink1000OduAirHssRfpTdmChannelBW10MHz_Type()
)
winlink1000OduAirHssRfpTdmChannelBW10MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpTdmChannelBW10MHz.setStatus("mandatory")


class _Winlink1000OduAirHssRfpEthChannelBW20MHz_Type(Integer32):
    """Custom type winlink1000OduAirHssRfpEthChannelBW20MHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestFit", 1),
          ("nonOptimal", 2),
          ("notAvailable", 3))
    )


_Winlink1000OduAirHssRfpEthChannelBW20MHz_Type.__name__ = "Integer32"
_Winlink1000OduAirHssRfpEthChannelBW20MHz_Object = MibTableColumn
winlink1000OduAirHssRfpEthChannelBW20MHz = _Winlink1000OduAirHssRfpEthChannelBW20MHz_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7, 1, 6),
    _Winlink1000OduAirHssRfpEthChannelBW20MHz_Type()
)
winlink1000OduAirHssRfpEthChannelBW20MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpEthChannelBW20MHz.setStatus("mandatory")


class _Winlink1000OduAirHssRfpTdmChannelBW20MHz_Type(Integer32):
    """Custom type winlink1000OduAirHssRfpTdmChannelBW20MHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestFit", 1),
          ("nonOptimal", 2),
          ("notAvailable", 3))
    )


_Winlink1000OduAirHssRfpTdmChannelBW20MHz_Type.__name__ = "Integer32"
_Winlink1000OduAirHssRfpTdmChannelBW20MHz_Object = MibTableColumn
winlink1000OduAirHssRfpTdmChannelBW20MHz = _Winlink1000OduAirHssRfpTdmChannelBW20MHz_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7, 1, 7),
    _Winlink1000OduAirHssRfpTdmChannelBW20MHz_Type()
)
winlink1000OduAirHssRfpTdmChannelBW20MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpTdmChannelBW20MHz.setStatus("mandatory")


class _Winlink1000OduAirHssRfpEthChannelBW40MHz_Type(Integer32):
    """Custom type winlink1000OduAirHssRfpEthChannelBW40MHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestFit", 1),
          ("nonOptimal", 2),
          ("notAvailable", 3))
    )


_Winlink1000OduAirHssRfpEthChannelBW40MHz_Type.__name__ = "Integer32"
_Winlink1000OduAirHssRfpEthChannelBW40MHz_Object = MibTableColumn
winlink1000OduAirHssRfpEthChannelBW40MHz = _Winlink1000OduAirHssRfpEthChannelBW40MHz_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7, 1, 8),
    _Winlink1000OduAirHssRfpEthChannelBW40MHz_Type()
)
winlink1000OduAirHssRfpEthChannelBW40MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpEthChannelBW40MHz.setStatus("mandatory")


class _Winlink1000OduAirHssRfpTdmChannelBW40MHz_Type(Integer32):
    """Custom type winlink1000OduAirHssRfpTdmChannelBW40MHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestFit", 1),
          ("nonOptimal", 2),
          ("notAvailable", 3))
    )


_Winlink1000OduAirHssRfpTdmChannelBW40MHz_Type.__name__ = "Integer32"
_Winlink1000OduAirHssRfpTdmChannelBW40MHz_Object = MibTableColumn
winlink1000OduAirHssRfpTdmChannelBW40MHz = _Winlink1000OduAirHssRfpTdmChannelBW40MHz_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7, 1, 9),
    _Winlink1000OduAirHssRfpTdmChannelBW40MHz_Type()
)
winlink1000OduAirHssRfpTdmChannelBW40MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpTdmChannelBW40MHz.setStatus("mandatory")


class _Winlink1000OduAirHssRfpEthChannelBW80MHz_Type(Integer32):
    """Custom type winlink1000OduAirHssRfpEthChannelBW80MHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestFit", 1),
          ("nonOptimal", 2),
          ("notAvailable", 3))
    )


_Winlink1000OduAirHssRfpEthChannelBW80MHz_Type.__name__ = "Integer32"
_Winlink1000OduAirHssRfpEthChannelBW80MHz_Object = MibTableColumn
winlink1000OduAirHssRfpEthChannelBW80MHz = _Winlink1000OduAirHssRfpEthChannelBW80MHz_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7, 1, 10),
    _Winlink1000OduAirHssRfpEthChannelBW80MHz_Type()
)
winlink1000OduAirHssRfpEthChannelBW80MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpEthChannelBW80MHz.setStatus("mandatory")


class _Winlink1000OduAirHssRfpEthChannelBW7MHz_Type(Integer32):
    """Custom type winlink1000OduAirHssRfpEthChannelBW7MHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestFit", 1),
          ("nonOptimal", 2),
          ("notAvailable", 3))
    )


_Winlink1000OduAirHssRfpEthChannelBW7MHz_Type.__name__ = "Integer32"
_Winlink1000OduAirHssRfpEthChannelBW7MHz_Object = MibTableColumn
winlink1000OduAirHssRfpEthChannelBW7MHz = _Winlink1000OduAirHssRfpEthChannelBW7MHz_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7, 1, 11),
    _Winlink1000OduAirHssRfpEthChannelBW7MHz_Type()
)
winlink1000OduAirHssRfpEthChannelBW7MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpEthChannelBW7MHz.setStatus("mandatory")


class _Winlink1000OduAirHssRfpEthChannelBW14MHz_Type(Integer32):
    """Custom type winlink1000OduAirHssRfpEthChannelBW14MHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestFit", 1),
          ("nonOptimal", 2),
          ("notAvailable", 3))
    )


_Winlink1000OduAirHssRfpEthChannelBW14MHz_Type.__name__ = "Integer32"
_Winlink1000OduAirHssRfpEthChannelBW14MHz_Object = MibTableColumn
winlink1000OduAirHssRfpEthChannelBW14MHz = _Winlink1000OduAirHssRfpEthChannelBW14MHz_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 7, 1, 12),
    _Winlink1000OduAirHssRfpEthChannelBW14MHz_Type()
)
winlink1000OduAirHssRfpEthChannelBW14MHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpEthChannelBW14MHz.setStatus("mandatory")
_Winlink1000OduAirHssRfpStr_Type = DisplayString
_Winlink1000OduAirHssRfpStr_Object = MibScalar
winlink1000OduAirHssRfpStr = _Winlink1000OduAirHssRfpStr_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 8),
    _Winlink1000OduAirHssRfpStr_Type()
)
winlink1000OduAirHssRfpStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpStr.setStatus("mandatory")
_Winlink1000OduAirHssHsmID_Type = Integer32
_Winlink1000OduAirHssHsmID_Object = MibScalar
winlink1000OduAirHssHsmID = _Winlink1000OduAirHssHsmID_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 9),
    _Winlink1000OduAirHssHsmID_Type()
)
winlink1000OduAirHssHsmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssHsmID.setStatus("mandatory")
_Winlink1000OduAirHssTime_Type = DisplayString
_Winlink1000OduAirHssTime_Object = MibScalar
winlink1000OduAirHssTime = _Winlink1000OduAirHssTime_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 10),
    _Winlink1000OduAirHssTime_Type()
)
winlink1000OduAirHssTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssTime.setStatus("mandatory")
_Winlink1000OduAirHssLatitude_Type = DisplayString
_Winlink1000OduAirHssLatitude_Object = MibScalar
winlink1000OduAirHssLatitude = _Winlink1000OduAirHssLatitude_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 11),
    _Winlink1000OduAirHssLatitude_Type()
)
winlink1000OduAirHssLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssLatitude.setStatus("mandatory")
_Winlink1000OduAirHssNSIndicator_Type = DisplayString
_Winlink1000OduAirHssNSIndicator_Object = MibScalar
winlink1000OduAirHssNSIndicator = _Winlink1000OduAirHssNSIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 12),
    _Winlink1000OduAirHssNSIndicator_Type()
)
winlink1000OduAirHssNSIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssNSIndicator.setStatus("mandatory")
_Winlink1000OduAirHssLongitude_Type = DisplayString
_Winlink1000OduAirHssLongitude_Object = MibScalar
winlink1000OduAirHssLongitude = _Winlink1000OduAirHssLongitude_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 13),
    _Winlink1000OduAirHssLongitude_Type()
)
winlink1000OduAirHssLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssLongitude.setStatus("mandatory")
_Winlink1000OduAirHssEWIndicator_Type = DisplayString
_Winlink1000OduAirHssEWIndicator_Object = MibScalar
winlink1000OduAirHssEWIndicator = _Winlink1000OduAirHssEWIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 14),
    _Winlink1000OduAirHssEWIndicator_Type()
)
winlink1000OduAirHssEWIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssEWIndicator.setStatus("mandatory")
_Winlink1000OduAirHssNumSatellites_Type = DisplayString
_Winlink1000OduAirHssNumSatellites_Object = MibScalar
winlink1000OduAirHssNumSatellites = _Winlink1000OduAirHssNumSatellites_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 15),
    _Winlink1000OduAirHssNumSatellites_Type()
)
winlink1000OduAirHssNumSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssNumSatellites.setStatus("mandatory")
_Winlink1000OduAirHssAltitude_Type = DisplayString
_Winlink1000OduAirHssAltitude_Object = MibScalar
winlink1000OduAirHssAltitude = _Winlink1000OduAirHssAltitude_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 16),
    _Winlink1000OduAirHssAltitude_Type()
)
winlink1000OduAirHssAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssAltitude.setStatus("mandatory")


class _Winlink1000OduAirHssRfpPhase_Type(Integer32):
    """Custom type winlink1000OduAirHssRfpPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfpNormalPhase", 1),
          ("rfpShiftedPhase", 2))
    )


_Winlink1000OduAirHssRfpPhase_Type.__name__ = "Integer32"
_Winlink1000OduAirHssRfpPhase_Object = MibScalar
winlink1000OduAirHssRfpPhase = _Winlink1000OduAirHssRfpPhase_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 17),
    _Winlink1000OduAirHssRfpPhase_Type()
)
winlink1000OduAirHssRfpPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirHssRfpPhase.setStatus("mandatory")


class _Winlink1000OduAirHssInterSiteSynchronizationMode_Type(Integer32):
    """Custom type winlink1000OduAirHssInterSiteSynchronizationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("synchronized", 2))
    )


_Winlink1000OduAirHssInterSiteSynchronizationMode_Type.__name__ = "Integer32"
_Winlink1000OduAirHssInterSiteSynchronizationMode_Object = MibScalar
winlink1000OduAirHssInterSiteSynchronizationMode = _Winlink1000OduAirHssInterSiteSynchronizationMode_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 18),
    _Winlink1000OduAirHssInterSiteSynchronizationMode_Type()
)
winlink1000OduAirHssInterSiteSynchronizationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirHssInterSiteSynchronizationMode.setStatus("mandatory")


class _Winlink1000OduAirHssInterSiteSynchronizationAvailability_Type(Integer32):
    """Custom type winlink1000OduAirHssInterSiteSynchronizationAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 1))
    )


_Winlink1000OduAirHssInterSiteSynchronizationAvailability_Type.__name__ = "Integer32"
_Winlink1000OduAirHssInterSiteSynchronizationAvailability_Object = MibScalar
winlink1000OduAirHssInterSiteSynchronizationAvailability = _Winlink1000OduAirHssInterSiteSynchronizationAvailability_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 19),
    _Winlink1000OduAirHssInterSiteSynchronizationAvailability_Type()
)
winlink1000OduAirHssInterSiteSynchronizationAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssInterSiteSynchronizationAvailability.setStatus("mandatory")


class _Winlink1000OduAirHssSatellitesSatSyncRequired_Type(Integer32):
    """Custom type winlink1000OduAirHssSatellitesSatSyncRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRequired", 1),
          ("required", 2))
    )


_Winlink1000OduAirHssSatellitesSatSyncRequired_Type.__name__ = "Integer32"
_Winlink1000OduAirHssSatellitesSatSyncRequired_Object = MibScalar
winlink1000OduAirHssSatellitesSatSyncRequired = _Winlink1000OduAirHssSatellitesSatSyncRequired_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 20),
    _Winlink1000OduAirHssSatellitesSatSyncRequired_Type()
)
winlink1000OduAirHssSatellitesSatSyncRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirHssSatellitesSatSyncRequired.setStatus("mandatory")
_Winlink1000OduAirHssDomainID_Type = DisplayString
_Winlink1000OduAirHssDomainID_Object = MibScalar
winlink1000OduAirHssDomainID = _Winlink1000OduAirHssDomainID_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 21),
    _Winlink1000OduAirHssDomainID_Type()
)
winlink1000OduAirHssDomainID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirHssDomainID.setStatus("mandatory")


class _Winlink1000OduAirHssSupportedSynchronizationProtocol_Type(Integer32):
    """Custom type winlink1000OduAirHssSupportedSynchronizationProtocol based on Integer32"""
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
        *(("both", 3),
          ("ethOnly", 2),
          ("ghssAndEth", 4),
          ("ghssEthSerial", 5),
          ("serialOnly", 1))
    )


_Winlink1000OduAirHssSupportedSynchronizationProtocol_Type.__name__ = "Integer32"
_Winlink1000OduAirHssSupportedSynchronizationProtocol_Object = MibScalar
winlink1000OduAirHssSupportedSynchronizationProtocol = _Winlink1000OduAirHssSupportedSynchronizationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 22),
    _Winlink1000OduAirHssSupportedSynchronizationProtocol_Type()
)
winlink1000OduAirHssSupportedSynchronizationProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssSupportedSynchronizationProtocol.setStatus("mandatory")


class _Winlink1000OduAirHssDesiredSynchronizationProtocol_Type(Integer32):
    """Custom type winlink1000OduAirHssDesiredSynchronizationProtocol based on Integer32"""
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
        *(("both", 3),
          ("ethOnly", 2),
          ("ghssOnly", 4),
          ("serialOnly", 1))
    )


_Winlink1000OduAirHssDesiredSynchronizationProtocol_Type.__name__ = "Integer32"
_Winlink1000OduAirHssDesiredSynchronizationProtocol_Object = MibScalar
winlink1000OduAirHssDesiredSynchronizationProtocol = _Winlink1000OduAirHssDesiredSynchronizationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 23),
    _Winlink1000OduAirHssDesiredSynchronizationProtocol_Type()
)
winlink1000OduAirHssDesiredSynchronizationProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirHssDesiredSynchronizationProtocol.setStatus("mandatory")


class _Winlink1000OduAirHssDiscover_Type(Integer32):
    """Custom type winlink1000OduAirHssDiscover based on Integer32"""
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
        *(("startAll", 1),
          ("startAllMstr", 2),
          ("startMyDmn", 3),
          ("startMyMstr", 4))
    )


_Winlink1000OduAirHssDiscover_Type.__name__ = "Integer32"
_Winlink1000OduAirHssDiscover_Object = MibScalar
winlink1000OduAirHssDiscover = _Winlink1000OduAirHssDiscover_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 24),
    _Winlink1000OduAirHssDiscover_Type()
)
winlink1000OduAirHssDiscover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirHssDiscover.setStatus("mandatory")


class _Winlink1000OduAirHssNumberOfDiscoveredODUs_Type(Integer32):
    """Custom type winlink1000OduAirHssNumberOfDiscoveredODUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Winlink1000OduAirHssNumberOfDiscoveredODUs_Type.__name__ = "Integer32"
_Winlink1000OduAirHssNumberOfDiscoveredODUs_Object = MibScalar
winlink1000OduAirHssNumberOfDiscoveredODUs = _Winlink1000OduAirHssNumberOfDiscoveredODUs_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 25),
    _Winlink1000OduAirHssNumberOfDiscoveredODUs_Type()
)
winlink1000OduAirHssNumberOfDiscoveredODUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssNumberOfDiscoveredODUs.setStatus("mandatory")
_Winlink1000OduAirHssDiscoverTable_Object = MibTable
winlink1000OduAirHssDiscoverTable = _Winlink1000OduAirHssDiscoverTable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 26)
)
if mibBuilder.loadTexts:
    winlink1000OduAirHssDiscoverTable.setStatus("mandatory")
_Winlink1000OduAirHssDiscoverEntry_Object = MibTableRow
winlink1000OduAirHssDiscoverEntry = _Winlink1000OduAirHssDiscoverEntry_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 26, 1)
)
winlink1000OduAirHssDiscoverEntry.setIndexNames(
    (0, "RADWIN-MIB-WINLINK1000", "winlink1000OduAirHssDiscoverIndex"),
)
if mibBuilder.loadTexts:
    winlink1000OduAirHssDiscoverEntry.setStatus("mandatory")


class _Winlink1000OduAirHssDiscoverIndex_Type(Integer32):
    """Custom type winlink1000OduAirHssDiscoverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Winlink1000OduAirHssDiscoverIndex_Type.__name__ = "Integer32"
_Winlink1000OduAirHssDiscoverIndex_Object = MibTableColumn
winlink1000OduAirHssDiscoverIndex = _Winlink1000OduAirHssDiscoverIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 26, 1, 1),
    _Winlink1000OduAirHssDiscoverIndex_Type()
)
winlink1000OduAirHssDiscoverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssDiscoverIndex.setStatus("mandatory")
_Winlink1000OduAirHssDiscoverODUDescription_Type = DisplayString
_Winlink1000OduAirHssDiscoverODUDescription_Object = MibTableColumn
winlink1000OduAirHssDiscoverODUDescription = _Winlink1000OduAirHssDiscoverODUDescription_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 26, 1, 2),
    _Winlink1000OduAirHssDiscoverODUDescription_Type()
)
winlink1000OduAirHssDiscoverODUDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssDiscoverODUDescription.setStatus("mandatory")


class _Winlink1000OduAirHssMasterSlaveCompatibility_Type(Integer32):
    """Custom type winlink1000OduAirHssMasterSlaveCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compatible", 1),
          ("notCompatible", 2))
    )


_Winlink1000OduAirHssMasterSlaveCompatibility_Type.__name__ = "Integer32"
_Winlink1000OduAirHssMasterSlaveCompatibility_Object = MibScalar
winlink1000OduAirHssMasterSlaveCompatibility = _Winlink1000OduAirHssMasterSlaveCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 27),
    _Winlink1000OduAirHssMasterSlaveCompatibility_Type()
)
winlink1000OduAirHssMasterSlaveCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssMasterSlaveCompatibility.setStatus("mandatory")


class _Winlink1000OduAirHssNumberOfAssociatedCU_Type(Integer32):
    """Custom type winlink1000OduAirHssNumberOfAssociatedCU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Winlink1000OduAirHssNumberOfAssociatedCU_Type.__name__ = "Integer32"
_Winlink1000OduAirHssNumberOfAssociatedCU_Object = MibScalar
winlink1000OduAirHssNumberOfAssociatedCU = _Winlink1000OduAirHssNumberOfAssociatedCU_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 28),
    _Winlink1000OduAirHssNumberOfAssociatedCU_Type()
)
winlink1000OduAirHssNumberOfAssociatedCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssNumberOfAssociatedCU.setStatus("mandatory")
_Winlink1000OduAirHssAssociatedCUTable_Object = MibTable
winlink1000OduAirHssAssociatedCUTable = _Winlink1000OduAirHssAssociatedCUTable_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 29)
)
if mibBuilder.loadTexts:
    winlink1000OduAirHssAssociatedCUTable.setStatus("mandatory")
_Winlink1000OduAirHssAssociatedCUTableEntry_Object = MibTableRow
winlink1000OduAirHssAssociatedCUTableEntry = _Winlink1000OduAirHssAssociatedCUTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 29, 1)
)
winlink1000OduAirHssAssociatedCUTableEntry.setIndexNames(
    (0, "RADWIN-MIB-WINLINK1000", "winlink1000OduAirHssAssociatedCUIndex"),
)
if mibBuilder.loadTexts:
    winlink1000OduAirHssAssociatedCUTableEntry.setStatus("mandatory")


class _Winlink1000OduAirHssAssociatedCUIndex_Type(Integer32):
    """Custom type winlink1000OduAirHssAssociatedCUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Winlink1000OduAirHssAssociatedCUIndex_Type.__name__ = "Integer32"
_Winlink1000OduAirHssAssociatedCUIndex_Object = MibTableColumn
winlink1000OduAirHssAssociatedCUIndex = _Winlink1000OduAirHssAssociatedCUIndex_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 29, 1, 1),
    _Winlink1000OduAirHssAssociatedCUIndex_Type()
)
winlink1000OduAirHssAssociatedCUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssAssociatedCUIndex.setStatus("mandatory")
_Winlink1000OduAirHssAssociatedCUDescription_Type = DisplayString
_Winlink1000OduAirHssAssociatedCUDescription_Object = MibTableColumn
winlink1000OduAirHssAssociatedCUDescription = _Winlink1000OduAirHssAssociatedCUDescription_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 29, 1, 2),
    _Winlink1000OduAirHssAssociatedCUDescription_Type()
)
winlink1000OduAirHssAssociatedCUDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssAssociatedCUDescription.setStatus("mandatory")


class _Winlink1000OduAirHssSyncStatusEth_Type(Integer32):
    """Custom type winlink1000OduAirHssSyncStatusEth based on Integer32"""
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
        *(("badSynchronizationLevel", 5),
          ("goodSynchronizationLevel", 3),
          ("mediumSynchronizationLevel", 4),
          ("notApplicable", 1),
          ("notSynchronized", 2),
          ("startSynchronization", 6))
    )


_Winlink1000OduAirHssSyncStatusEth_Type.__name__ = "Integer32"
_Winlink1000OduAirHssSyncStatusEth_Object = MibScalar
winlink1000OduAirHssSyncStatusEth = _Winlink1000OduAirHssSyncStatusEth_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 30),
    _Winlink1000OduAirHssSyncStatusEth_Type()
)
winlink1000OduAirHssSyncStatusEth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssSyncStatusEth.setStatus("mandatory")


class _Winlink1000OduAirHssEthVLANTag_Type(Integer32):
    """Custom type winlink1000OduAirHssEthVLANTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40947),
    )


_Winlink1000OduAirHssEthVLANTag_Type.__name__ = "Integer32"
_Winlink1000OduAirHssEthVLANTag_Object = MibScalar
winlink1000OduAirHssEthVLANTag = _Winlink1000OduAirHssEthVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 31),
    _Winlink1000OduAirHssEthVLANTag_Type()
)
winlink1000OduAirHssEthVLANTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirHssEthVLANTag.setStatus("mandatory")
_Winlink1000OduAirHssHSMIPAddress_Type = IpAddress
_Winlink1000OduAirHssHSMIPAddress_Object = MibScalar
winlink1000OduAirHssHSMIPAddress = _Winlink1000OduAirHssHSMIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 32),
    _Winlink1000OduAirHssHSMIPAddress_Type()
)
winlink1000OduAirHssHSMIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssHSMIPAddress.setStatus("mandatory")


class _Winlink1000OduAirHssDelayToHSM_Type(Integer32):
    """Custom type winlink1000OduAirHssDelayToHSM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_Winlink1000OduAirHssDelayToHSM_Type.__name__ = "Integer32"
_Winlink1000OduAirHssDelayToHSM_Object = MibScalar
winlink1000OduAirHssDelayToHSM = _Winlink1000OduAirHssDelayToHSM_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 33),
    _Winlink1000OduAirHssDelayToHSM_Type()
)
winlink1000OduAirHssDelayToHSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssDelayToHSM.setStatus("mandatory")
_Winlink1000OduAirHssSyncAcquisitionSeconds_Type = Integer32
_Winlink1000OduAirHssSyncAcquisitionSeconds_Object = MibScalar
winlink1000OduAirHssSyncAcquisitionSeconds = _Winlink1000OduAirHssSyncAcquisitionSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 34),
    _Winlink1000OduAirHssSyncAcquisitionSeconds_Type()
)
winlink1000OduAirHssSyncAcquisitionSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirHssSyncAcquisitionSeconds.setStatus("mandatory")
_Winlink1000OduAirHssHSMIPv6Address_Type = DisplayString
_Winlink1000OduAirHssHSMIPv6Address_Object = MibScalar
winlink1000OduAirHssHSMIPv6Address = _Winlink1000OduAirHssHSMIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 40, 35),
    _Winlink1000OduAirHssHSMIPv6Address_Type()
)
winlink1000OduAirHssHSMIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    winlink1000OduAirHssHSMIPv6Address.setStatus("mandatory")


class _Winlink1000OduAirLockRemote_Type(Integer32):
    """Custom type winlink1000OduAirLockRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 2),
          ("unlock", 1))
    )


_Winlink1000OduAirLockRemote_Type.__name__ = "Integer32"
_Winlink1000OduAirLockRemote_Object = MibScalar
winlink1000OduAirLockRemote = _Winlink1000OduAirLockRemote_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 41),
    _Winlink1000OduAirLockRemote_Type()
)
winlink1000OduAirLockRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirLockRemote.setStatus("mandatory")
_Winlink1000OduAirAntennaGain_Type = Integer32
_Winlink1000OduAirAntennaGain_Object = MibScalar
winlink1000OduAirAntennaGain = _Winlink1000OduAirAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 1, 5, 42),
    _Winlink1000OduAirAntennaGain_Type()
)
winlink1000OduAirAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    winlink1000OduAirAntennaGain.setStatus("mandatory")

# Managed Objects groups


# Notification objects

externalAlarmInPort1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 105)
)
externalAlarmInPort1Alarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    externalAlarmInPort1Alarm.setStatus(
        ""
    )

externalAlarmInPort2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 106)
)
externalAlarmInPort2Alarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    externalAlarmInPort2Alarm.setStatus(
        ""
    )

bitFailedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 107)
)
bitFailedAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    bitFailedAlarm.setStatus(
        ""
    )

wrongConfigurationLoadedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 108)
)
wrongConfigurationLoadedAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    wrongConfigurationLoadedAlarm.setStatus(
        ""
    )

lanPort1DisconnectedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 109)
)
lanPort1DisconnectedAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    lanPort1DisconnectedAlarm.setStatus(
        ""
    )

lanPort2DisconnectedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 110)
)
lanPort2DisconnectedAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    lanPort2DisconnectedAlarm.setStatus(
        ""
    )

mngPortDisconnectedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 111)
)
mngPortDisconnectedAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    mngPortDisconnectedAlarm.setStatus(
        ""
    )

externalAlarmInPort3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 112)
)
externalAlarmInPort3Alarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    externalAlarmInPort3Alarm.setStatus(
        ""
    )

externalAlarmInPort4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 113)
)
externalAlarmInPort4Alarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    externalAlarmInPort4Alarm.setStatus(
        ""
    )

swVersionsMismatchFullCompatibilityAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 114)
)
swVersionsMismatchFullCompatibilityAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    swVersionsMismatchFullCompatibilityAlarm.setStatus(
        ""
    )

swVersionsMismatchRestrictedCompatibilityAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 115)
)
swVersionsMismatchRestrictedCompatibilityAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    swVersionsMismatchRestrictedCompatibilityAlarm.setStatus(
        ""
    )

swVersionsMismatchSoftwareUpgradeRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 116)
)
swVersionsMismatchSoftwareUpgradeRequired.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    swVersionsMismatchSoftwareUpgradeRequired.setStatus(
        ""
    )

swVersionsIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 117)
)
swVersionsIncompatible.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    swVersionsIncompatible.setStatus(
        ""
    )

hssMultipleSourcesDetectedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 118)
)
hssMultipleSourcesDetectedAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hssMultipleSourcesDetectedAlarm.setStatus(
        ""
    )

hssSyncToProperSourceStoppedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 119)
)
hssSyncToProperSourceStoppedAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hssSyncToProperSourceStoppedAlarm.setStatus(
        ""
    )

hssSyncPulseDetectedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 120)
)
hssSyncPulseDetectedAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hssSyncPulseDetectedAlarm.setStatus(
        ""
    )

tdmBackupAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 121)
)
tdmBackupAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    tdmBackupAlarm.setStatus(
        ""
    )

linkLockUnauthorizedRemoteODU = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 122)
)
linkLockUnauthorizedRemoteODU.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    linkLockUnauthorizedRemoteODU.setStatus(
        ""
    )

linkLockUnauthorizedODU = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 123)
)
linkLockUnauthorizedODU.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    linkLockUnauthorizedODU.setStatus(
        ""
    )

hotStandbyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 124)
)
hotStandbyAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hotStandbyAlarm.setStatus(
        ""
    )

sfpInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 126)
)
sfpInsertion.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    sfpInsertion.setStatus(
        ""
    )

sfpPort1DisconnectedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 127)
)
sfpPort1DisconnectedAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    sfpPort1DisconnectedAlarm.setStatus(
        ""
    )

ringRplStateActiveAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 128)
)
ringRplStateActiveAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    ringRplStateActiveAlarm.setStatus(
        ""
    )

desiredRatioCanNotBeAppliedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 129)
)
desiredRatioCanNotBeAppliedAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    desiredRatioCanNotBeAppliedAlarm.setStatus(
        ""
    )

cbwMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 130)
)
cbwMismatch.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    cbwMismatch.setStatus(
        ""
    )

gpsNotSynchronized = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 131)
)
gpsNotSynchronized.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    gpsNotSynchronized.setStatus(
        ""
    )

pdTooHighDueCbwLimitations = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 132)
)
pdTooHighDueCbwLimitations.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    pdTooHighDueCbwLimitations.setStatus(
        ""
    )

hbsEncryptionAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 133)
)
hbsEncryptionAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hbsEncryptionAlarm.setStatus(
        ""
    )

hbsEhServiceClosedToHsu = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 134)
)
hbsEhServiceClosedToHsu.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hbsEhServiceClosedToHsu.setStatus(
        ""
    )

hbsUnsynchronizedHsuAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 135)
)
hbsUnsynchronizedHsuAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hbsUnsynchronizedHsuAlarm.setStatus(
        ""
    )

hbsInactiveHbsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 136)
)
hbsInactiveHbsAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hbsInactiveHbsAlarm.setStatus(
        ""
    )

incompatibleHsu = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 137)
)
incompatibleHsu.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    incompatibleHsu.setStatus(
        ""
    )

hsuUnsupportedBeacon = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 138)
)
hsuUnsupportedBeacon.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hsuUnsupportedBeacon.setStatus(
        ""
    )

lanPortDisconnectedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 139)
)
lanPortDisconnectedAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    lanPortDisconnectedAlarm.setStatus(
        ""
    )

poePortDisconnectedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 140)
)
poePortDisconnectedAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    poePortDisconnectedAlarm.setStatus(
        ""
    )

poePowerConsumptionAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 141)
)
poePowerConsumptionAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    poePowerConsumptionAlarm.setStatus(
        ""
    )

hobupFaultyStateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 149)
)
hobupFaultyStateAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hobupFaultyStateAlarm.setStatus(
        ""
    )

gpsOverCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 150)
)
gpsOverCurrentAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    gpsOverCurrentAlarm.setStatus(
        ""
    )

gpsCommunicationFailiureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 151)
)
gpsCommunicationFailiureAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    gpsCommunicationFailiureAlarm.setStatus(
        ""
    )

temperatureThresholdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 152)
)
temperatureThresholdAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    temperatureThresholdAlarm.setStatus(
        ""
    )

localRouterDiscoveryStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 153)
)
localRouterDiscoveryStatus.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    localRouterDiscoveryStatus.setStatus(
        ""
    )

trackRouterDiscoveryStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 154)
)
trackRouterDiscoveryStatus.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    trackRouterDiscoveryStatus.setStatus(
        ""
    )

lastUserSnmpAccessOverHourAgo = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 155)
)
lastUserSnmpAccessOverHourAgo.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    lastUserSnmpAccessOverHourAgo.setStatus(
        ""
    )

btsTargetUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 156)
)
btsTargetUnreachable.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    btsTargetUnreachable.setStatus(
        ""
    )

tdmServiceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 200)
)
tdmServiceClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    tdmServiceClear.setStatus(
        ""
    )

ethServiceOpened = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 201)
)
ethServiceOpened.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    ethServiceOpened.setStatus(
        ""
    )

encryptionClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 203)
)
encryptionClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    encryptionClear.setStatus(
        ""
    )

changeLinkPasswordClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 204)
)
changeLinkPasswordClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    changeLinkPasswordClear.setStatus(
        ""
    )

externalAlarmInPort1Clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 205)
)
externalAlarmInPort1Clear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    externalAlarmInPort1Clear.setStatus(
        ""
    )

externalAlarmInPort2Clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 206)
)
externalAlarmInPort2Clear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    externalAlarmInPort2Clear.setStatus(
        ""
    )

lanPort1Clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 209)
)
lanPort1Clear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    lanPort1Clear.setStatus(
        ""
    )

lanPort2Clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 210)
)
lanPort2Clear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    lanPort2Clear.setStatus(
        ""
    )

mngPortClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 211)
)
mngPortClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    mngPortClear.setStatus(
        ""
    )

externalAlarmInPort3Clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 212)
)
externalAlarmInPort3Clear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    externalAlarmInPort3Clear.setStatus(
        ""
    )

externalAlarmInPort4Clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 213)
)
externalAlarmInPort4Clear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    externalAlarmInPort4Clear.setStatus(
        ""
    )

swVersionsMatchFullCompatibilityClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 214)
)
swVersionsMatchFullCompatibilityClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    swVersionsMatchFullCompatibilityClear.setStatus(
        ""
    )

swVersionsMatchRestrictedCompatibilityClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 215)
)
swVersionsMatchRestrictedCompatibilityClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    swVersionsMatchRestrictedCompatibilityClear.setStatus(
        ""
    )

swVersionsMatchSoftwareUpgradeRequiredClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 216)
)
swVersionsMatchSoftwareUpgradeRequiredClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    swVersionsMatchSoftwareUpgradeRequiredClear.setStatus(
        ""
    )

swVersionsCompatibleClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 217)
)
swVersionsCompatibleClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    swVersionsCompatibleClear.setStatus(
        ""
    )

hssMultipleSourcesDisappearedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 218)
)
hssMultipleSourcesDisappearedClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hssMultipleSourcesDisappearedClear.setStatus(
        ""
    )

hssSyncToProperSourceAchievedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 219)
)
hssSyncToProperSourceAchievedClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hssSyncToProperSourceAchievedClear.setStatus(
        ""
    )

hssSyncPulseDisappearedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 220)
)
hssSyncPulseDisappearedClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hssSyncPulseDisappearedClear.setStatus(
        ""
    )

tdmBackupClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 221)
)
tdmBackupClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    tdmBackupClear.setStatus(
        ""
    )

linkLockAuthorizedRemoteODU = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 222)
)
linkLockAuthorizedRemoteODU.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    linkLockAuthorizedRemoteODU.setStatus(
        ""
    )

linkLockAuthorizedODU = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 223)
)
linkLockAuthorizedODU.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    linkLockAuthorizedODU.setStatus(
        ""
    )

linkAuthenticationDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 224)
)
linkAuthenticationDisabled.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    linkAuthenticationDisabled.setStatus(
        ""
    )

hotStandbyClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 225)
)
hotStandbyClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hotStandbyClear.setStatus(
        ""
    )

sfpExtraction = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 226)
)
sfpExtraction.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    sfpExtraction.setStatus(
        ""
    )

sfpPort1Clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 227)
)
sfpPort1Clear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    sfpPort1Clear.setStatus(
        ""
    )

compatibleIdus = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 228)
)
compatibleIdus.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    compatibleIdus.setStatus(
        ""
    )

desiredRatioCanNotBeAppliedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 229)
)
desiredRatioCanNotBeAppliedClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    desiredRatioCanNotBeAppliedClear.setStatus(
        ""
    )

cbwMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 230)
)
cbwMatch.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    cbwMatch.setStatus(
        ""
    )

switchCbwAndChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 231)
)
switchCbwAndChannel.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    switchCbwAndChannel.setStatus(
        ""
    )

ringRplStateIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 232)
)
ringRplStateIdle.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    ringRplStateIdle.setStatus(
        ""
    )

ringEthServiceStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 233)
)
ringEthServiceStatus.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    ringEthServiceStatus.setStatus(
        ""
    )

ringFirstRpmReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 234)
)
ringFirstRpmReceived.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    ringFirstRpmReceived.setStatus(
        ""
    )

ringEthernetSrviceUnblockedTO = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 235)
)
ringEthernetSrviceUnblockedTO.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    ringEthernetSrviceUnblockedTO.setStatus(
        ""
    )

gpsSynchronized = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 236)
)
gpsSynchronized.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    gpsSynchronized.setStatus(
        ""
    )

hbsEncryptionClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 237)
)
hbsEncryptionClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hbsEncryptionClear.setStatus(
        ""
    )

hbsEhServiceOpenedToHsu = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 238)
)
hbsEhServiceOpenedToHsu.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hbsEhServiceOpenedToHsu.setStatus(
        ""
    )

hbsSynchronizedHsuAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 239)
)
hbsSynchronizedHsuAlarm.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hbsSynchronizedHsuAlarm.setStatus(
        ""
    )

hbsActiveHbs = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 240)
)
hbsActiveHbs.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hbsActiveHbs.setStatus(
        ""
    )

switchCBW = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 241)
)
switchCBW.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    switchCBW.setStatus(
        ""
    )

changeRatio = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 242)
)
changeRatio.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    changeRatio.setStatus(
        ""
    )

lanPortClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 243)
)
lanPortClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    lanPortClear.setStatus(
        ""
    )

poePortClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 244)
)
poePortClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    poePortClear.setStatus(
        ""
    )

poePowerConsumptionClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 245)
)
poePowerConsumptionClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    poePowerConsumptionClear.setStatus(
        ""
    )

incompatibleHbsHsu = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 246)
)
incompatibleHbsHsu.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    incompatibleHbsHsu.setStatus(
        ""
    )

mobilityLinkOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 247)
)
mobilityLinkOff.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    mobilityLinkOff.setStatus(
        ""
    )

enterLocalConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 248)
)
enterLocalConnection.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    enterLocalConnection.setStatus(
        ""
    )

hobupActiveStateFaultyClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 249)
)
hobupActiveStateFaultyClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hobupActiveStateFaultyClear.setStatus(
        ""
    )

hobupStandbyState = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 250)
)
hobupStandbyState.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    hobupStandbyState.setStatus(
        ""
    )

gpsOverCurrentClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 251)
)
gpsOverCurrentClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    gpsOverCurrentClear.setStatus(
        ""
    )

temperatureThresholdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 252)
)
temperatureThresholdClear.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    temperatureThresholdClear.setStatus(
        ""
    )

localRouterDiscoverySucceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 253)
)
localRouterDiscoverySucceed.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    localRouterDiscoverySucceed.setStatus(
        ""
    )

trackRouterDiscoverySucceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 254)
)
trackRouterDiscoverySucceed.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    trackRouterDiscoverySucceed.setStatus(
        ""
    )

qosVersion2StrictMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 255)
)
qosVersion2StrictMismatch.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    qosVersion2StrictMismatch.setStatus(
        ""
    )

qosVersion2TtlMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 256)
)
qosVersion2TtlMismatch.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    qosVersion2TtlMismatch.setStatus(
        ""
    )

btsTargetIsReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 257)
)
btsTargetIsReachable.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    btsTargetIsReachable.setStatus(
        ""
    )

tcNotSupportedByHSU = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 258)
)
tcNotSupportedByHSU.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    tcNotSupportedByHSU.setStatus(
        ""
    )

syncEPortHOStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 259)
)
syncEPortHOStateChange.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    syncEPortHOStateChange.setStatus(
        ""
    )

syncEPortFailureStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 260)
)
syncEPortFailureStateChange.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    syncEPortFailureStateChange.setStatus(
        ""
    )

btsCpeUpdateServiceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 261)
)
btsCpeUpdateServiceFailed.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    btsCpeUpdateServiceFailed.setStatus(
        ""
    )

btsCpeUpdateServiceSucceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 262)
)
btsCpeUpdateServiceSucceed.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    btsCpeUpdateServiceSucceed.setStatus(
        ""
    )

radiusServerNoREsponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 263)
)
radiusServerNoREsponse.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    radiusServerNoREsponse.setStatus(
        ""
    )

noRadiusServerRespond = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 264)
)
noRadiusServerRespond.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    noRadiusServerRespond.setStatus(
        ""
    )

radiusServerRespondedSuccessfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 265)
)
radiusServerRespondedSuccessfully.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    radiusServerRespondedSuccessfully.setStatus(
        ""
    )

bsaAlignmentStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 266)
)
bsaAlignmentStarted.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    bsaAlignmentStarted.setStatus(
        ""
    )

bsaAlignmentFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 267)
)
bsaAlignmentFinished.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    bsaAlignmentFinished.setStatus(
        ""
    )

bsaAlignmentTriggered = NotificationType(
    (1, 3, 6, 1, 4, 1, 4458, 1000, 0, 268)
)
bsaAlignmentTriggered.setObjects(
      *(("RADWIN-MIB-WINLINK1000", "winlink1000GeneralTrapDescription"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmSeverity"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmIfIndex"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmUnit"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmTimeT"),
        ("RADWIN-MIB-WINLINK1000", "winlink1000OduAgnCurrAlarmId"))
)
if mibBuilder.loadTexts:
    bsaAlignmentTriggered.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADWIN-MIB-WINLINK1000",
    **{"radwin": radwin,
       "radwinProducts": radwinProducts,
       "winlink1000Family": winlink1000Family,
       "odu": odu,
       "oduIntegratedAntenna": oduIntegratedAntenna,
       "oduExternalAntenna": oduExternalAntenna,
       "radwin2000Family": radwin2000Family,
       "odu2000": odu2000,
       "odu2KIntegratedAntenna": odu2KIntegratedAntenna,
       "odu2KExternalAntenna": odu2KExternalAntenna,
       "gpsSynchronizerFamily": gpsSynchronizerFamily,
       "oduGSU": oduGSU,
       "oduGSUExternalAntenna": oduGSUExternalAntenna,
       "hssSyncUnits": hssSyncUnits,
       "hssISU": hssISU,
       "hssGSU": hssGSU,
       "radwin5000HBSFamily": radwin5000HBSFamily,
       "oduHBS": oduHBS,
       "oduHBSIntegratedAntenna": oduHBSIntegratedAntenna,
       "oduHBSExternalAntenna": oduHBSExternalAntenna,
       "radwin5000HSUFamily": radwin5000HSUFamily,
       "oduHSU": oduHSU,
       "oduHSUIntegratedAntenna": oduHSUIntegratedAntenna,
       "oduHSUExternalAntenna": oduHSUExternalAntenna,
       "radwin6000Family": radwin6000Family,
       "odu6000": odu6000,
       "odu6K": odu6K,
       "gateway6000": gateway6000,
       "gateway6K": gateway6K,
       "radwinWiFiAPFamily": radwinWiFiAPFamily,
       "odu600": odu600,
       "oduWiFiAP": oduWiFiAP,
       "winlink1000": winlink1000,
       "externalAlarmInPort1Alarm": externalAlarmInPort1Alarm,
       "externalAlarmInPort2Alarm": externalAlarmInPort2Alarm,
       "bitFailedAlarm": bitFailedAlarm,
       "wrongConfigurationLoadedAlarm": wrongConfigurationLoadedAlarm,
       "lanPort1DisconnectedAlarm": lanPort1DisconnectedAlarm,
       "lanPort2DisconnectedAlarm": lanPort2DisconnectedAlarm,
       "mngPortDisconnectedAlarm": mngPortDisconnectedAlarm,
       "externalAlarmInPort3Alarm": externalAlarmInPort3Alarm,
       "externalAlarmInPort4Alarm": externalAlarmInPort4Alarm,
       "swVersionsMismatchFullCompatibilityAlarm": swVersionsMismatchFullCompatibilityAlarm,
       "swVersionsMismatchRestrictedCompatibilityAlarm": swVersionsMismatchRestrictedCompatibilityAlarm,
       "swVersionsMismatchSoftwareUpgradeRequired": swVersionsMismatchSoftwareUpgradeRequired,
       "swVersionsIncompatible": swVersionsIncompatible,
       "hssMultipleSourcesDetectedAlarm": hssMultipleSourcesDetectedAlarm,
       "hssSyncToProperSourceStoppedAlarm": hssSyncToProperSourceStoppedAlarm,
       "hssSyncPulseDetectedAlarm": hssSyncPulseDetectedAlarm,
       "tdmBackupAlarm": tdmBackupAlarm,
       "linkLockUnauthorizedRemoteODU": linkLockUnauthorizedRemoteODU,
       "linkLockUnauthorizedODU": linkLockUnauthorizedODU,
       "hotStandbyAlarm": hotStandbyAlarm,
       "sfpInsertion": sfpInsertion,
       "sfpPort1DisconnectedAlarm": sfpPort1DisconnectedAlarm,
       "ringRplStateActiveAlarm": ringRplStateActiveAlarm,
       "desiredRatioCanNotBeAppliedAlarm": desiredRatioCanNotBeAppliedAlarm,
       "cbwMismatch": cbwMismatch,
       "gpsNotSynchronized": gpsNotSynchronized,
       "pdTooHighDueCbwLimitations": pdTooHighDueCbwLimitations,
       "hbsEncryptionAlarm": hbsEncryptionAlarm,
       "hbsEhServiceClosedToHsu": hbsEhServiceClosedToHsu,
       "hbsUnsynchronizedHsuAlarm": hbsUnsynchronizedHsuAlarm,
       "hbsInactiveHbsAlarm": hbsInactiveHbsAlarm,
       "incompatibleHsu": incompatibleHsu,
       "hsuUnsupportedBeacon": hsuUnsupportedBeacon,
       "lanPortDisconnectedAlarm": lanPortDisconnectedAlarm,
       "poePortDisconnectedAlarm": poePortDisconnectedAlarm,
       "poePowerConsumptionAlarm": poePowerConsumptionAlarm,
       "hobupFaultyStateAlarm": hobupFaultyStateAlarm,
       "gpsOverCurrentAlarm": gpsOverCurrentAlarm,
       "gpsCommunicationFailiureAlarm": gpsCommunicationFailiureAlarm,
       "temperatureThresholdAlarm": temperatureThresholdAlarm,
       "localRouterDiscoveryStatus": localRouterDiscoveryStatus,
       "trackRouterDiscoveryStatus": trackRouterDiscoveryStatus,
       "lastUserSnmpAccessOverHourAgo": lastUserSnmpAccessOverHourAgo,
       "btsTargetUnreachable": btsTargetUnreachable,
       "tdmServiceClear": tdmServiceClear,
       "ethServiceOpened": ethServiceOpened,
       "encryptionClear": encryptionClear,
       "changeLinkPasswordClear": changeLinkPasswordClear,
       "externalAlarmInPort1Clear": externalAlarmInPort1Clear,
       "externalAlarmInPort2Clear": externalAlarmInPort2Clear,
       "lanPort1Clear": lanPort1Clear,
       "lanPort2Clear": lanPort2Clear,
       "mngPortClear": mngPortClear,
       "externalAlarmInPort3Clear": externalAlarmInPort3Clear,
       "externalAlarmInPort4Clear": externalAlarmInPort4Clear,
       "swVersionsMatchFullCompatibilityClear": swVersionsMatchFullCompatibilityClear,
       "swVersionsMatchRestrictedCompatibilityClear": swVersionsMatchRestrictedCompatibilityClear,
       "swVersionsMatchSoftwareUpgradeRequiredClear": swVersionsMatchSoftwareUpgradeRequiredClear,
       "swVersionsCompatibleClear": swVersionsCompatibleClear,
       "hssMultipleSourcesDisappearedClear": hssMultipleSourcesDisappearedClear,
       "hssSyncToProperSourceAchievedClear": hssSyncToProperSourceAchievedClear,
       "hssSyncPulseDisappearedClear": hssSyncPulseDisappearedClear,
       "tdmBackupClear": tdmBackupClear,
       "linkLockAuthorizedRemoteODU": linkLockAuthorizedRemoteODU,
       "linkLockAuthorizedODU": linkLockAuthorizedODU,
       "linkAuthenticationDisabled": linkAuthenticationDisabled,
       "hotStandbyClear": hotStandbyClear,
       "sfpExtraction": sfpExtraction,
       "sfpPort1Clear": sfpPort1Clear,
       "compatibleIdus": compatibleIdus,
       "desiredRatioCanNotBeAppliedClear": desiredRatioCanNotBeAppliedClear,
       "cbwMatch": cbwMatch,
       "switchCbwAndChannel": switchCbwAndChannel,
       "ringRplStateIdle": ringRplStateIdle,
       "ringEthServiceStatus": ringEthServiceStatus,
       "ringFirstRpmReceived": ringFirstRpmReceived,
       "ringEthernetSrviceUnblockedTO": ringEthernetSrviceUnblockedTO,
       "gpsSynchronized": gpsSynchronized,
       "hbsEncryptionClear": hbsEncryptionClear,
       "hbsEhServiceOpenedToHsu": hbsEhServiceOpenedToHsu,
       "hbsSynchronizedHsuAlarm": hbsSynchronizedHsuAlarm,
       "hbsActiveHbs": hbsActiveHbs,
       "switchCBW": switchCBW,
       "changeRatio": changeRatio,
       "lanPortClear": lanPortClear,
       "poePortClear": poePortClear,
       "poePowerConsumptionClear": poePowerConsumptionClear,
       "incompatibleHbsHsu": incompatibleHbsHsu,
       "mobilityLinkOff": mobilityLinkOff,
       "enterLocalConnection": enterLocalConnection,
       "hobupActiveStateFaultyClear": hobupActiveStateFaultyClear,
       "hobupStandbyState": hobupStandbyState,
       "gpsOverCurrentClear": gpsOverCurrentClear,
       "temperatureThresholdClear": temperatureThresholdClear,
       "localRouterDiscoverySucceed": localRouterDiscoverySucceed,
       "trackRouterDiscoverySucceed": trackRouterDiscoverySucceed,
       "qosVersion2StrictMismatch": qosVersion2StrictMismatch,
       "qosVersion2TtlMismatch": qosVersion2TtlMismatch,
       "btsTargetIsReachable": btsTargetIsReachable,
       "tcNotSupportedByHSU": tcNotSupportedByHSU,
       "syncEPortHOStateChange": syncEPortHOStateChange,
       "syncEPortFailureStateChange": syncEPortFailureStateChange,
       "btsCpeUpdateServiceFailed": btsCpeUpdateServiceFailed,
       "btsCpeUpdateServiceSucceed": btsCpeUpdateServiceSucceed,
       "radiusServerNoREsponse": radiusServerNoREsponse,
       "noRadiusServerRespond": noRadiusServerRespond,
       "radiusServerRespondedSuccessfully": radiusServerRespondedSuccessfully,
       "bsaAlignmentStarted": bsaAlignmentStarted,
       "bsaAlignmentFinished": bsaAlignmentFinished,
       "bsaAlignmentTriggered": bsaAlignmentTriggered,
       "winlink1000Odu": winlink1000Odu,
       "winlink1000OduAdmin": winlink1000OduAdmin,
       "winlink1000OduAdmProductType": winlink1000OduAdmProductType,
       "winlink1000OduAdmHwRev": winlink1000OduAdmHwRev,
       "winlink1000OduAdmSwRev": winlink1000OduAdmSwRev,
       "winlink1000OduAdmLinkName": winlink1000OduAdmLinkName,
       "winlink1000OduAdmResetCmd": winlink1000OduAdmResetCmd,
       "winlink1000OduAdmAddres": winlink1000OduAdmAddres,
       "winlink1000OduAdmMask": winlink1000OduAdmMask,
       "winlink1000OduAdmGateway": winlink1000OduAdmGateway,
       "winlink1000OduAdmBroadcast": winlink1000OduAdmBroadcast,
       "winlink1000OduAdmHostsTable": winlink1000OduAdmHostsTable,
       "winlink1000OduAdmHostsEntry": winlink1000OduAdmHostsEntry,
       "winlink1000OduAdmHostsIndex": winlink1000OduAdmHostsIndex,
       "winlink1000OduAdmHostsIp": winlink1000OduAdmHostsIp,
       "winlink1000OduAdmHostsPort": winlink1000OduAdmHostsPort,
       "winlink1000OduAdmHostsSecurityModel": winlink1000OduAdmHostsSecurityModel,
       "winlink1000OduAdmHostsUserName": winlink1000OduAdmHostsUserName,
       "winlink1000OduAdmHostsPassword": winlink1000OduAdmHostsPassword,
       "winlink1000OduAdmHostsIPv6": winlink1000OduAdmHostsIPv6,
       "winlink1000OduBuzzerAdminState": winlink1000OduBuzzerAdminState,
       "winlink1000OduProductId": winlink1000OduProductId,
       "winlink1000OduReadCommunity": winlink1000OduReadCommunity,
       "winlink1000OduReadWriteCommunity": winlink1000OduReadWriteCommunity,
       "winlink1000OduTrapCommunity": winlink1000OduTrapCommunity,
       "winlink1000OduAdmSnmpAgentVersion": winlink1000OduAdmSnmpAgentVersion,
       "winlink1000OduAdmRemoteSiteName": winlink1000OduAdmRemoteSiteName,
       "winlink1000OduAdmSnmpAgentMinorVersion": winlink1000OduAdmSnmpAgentMinorVersion,
       "winlink1000OduAdmLinkPassword": winlink1000OduAdmLinkPassword,
       "winlink1000OduAdmSiteLinkPassword": winlink1000OduAdmSiteLinkPassword,
       "winlink1000OduAdmDefaultPassword": winlink1000OduAdmDefaultPassword,
       "winlink1000OduAdmConnectionType": winlink1000OduAdmConnectionType,
       "winlink1000OduAdmBackToFactorySettingsCmd": winlink1000OduAdmBackToFactorySettingsCmd,
       "winlink1000OduAdmIpParamsCnfg": winlink1000OduAdmIpParamsCnfg,
       "winlink1000OduAdmVlanID": winlink1000OduAdmVlanID,
       "winlink1000OduAdmVlanPriority": winlink1000OduAdmVlanPriority,
       "winlink1000OduAdmSN": winlink1000OduAdmSN,
       "winlink1000OduAdmProductName": winlink1000OduAdmProductName,
       "winlink1000OduAdmActivationKey": winlink1000OduAdmActivationKey,
       "winlink1000OduAdmRmtPermittedOduType": winlink1000OduAdmRmtPermittedOduType,
       "winlink1000OduAdmCpuID": winlink1000OduAdmCpuID,
       "winlink1000OduAdmOvrdCmd": winlink1000OduAdmOvrdCmd,
       "winlink1000OduAdmLinkMode": winlink1000OduAdmLinkMode,
       "winlink1000OduAdmActualConnectMode": winlink1000OduAdmActualConnectMode,
       "winlink1000OduAdmAES256Support": winlink1000OduAdmAES256Support,
       "winlink1000OduAdmAES256State": winlink1000OduAdmAES256State,
       "winlink1000OduAdmAES256Status": winlink1000OduAdmAES256Status,
       "winlink1000OduAdmBatterySavingShutdownTime": winlink1000OduAdmBatterySavingShutdownTime,
       "winlink1000OduAdmWiFiPowerMode": winlink1000OduAdmWiFiPowerMode,
       "winlink1000OduAdmShutdownTimer": winlink1000OduAdmShutdownTimer,
       "winlink1000OduAdmGPSState": winlink1000OduAdmGPSState,
       "winlink1000OduAdmTemperatureC": winlink1000OduAdmTemperatureC,
       "winlink1000OduAdmIPStackMode": winlink1000OduAdmIPStackMode,
       "winlink1000OduAdmIPv6ParamsCnfg": winlink1000OduAdmIPv6ParamsCnfg,
       "winlink1000OduAdmIPv6Address": winlink1000OduAdmIPv6Address,
       "winlink1000OduAdmIPv6Prefix": winlink1000OduAdmIPv6Prefix,
       "winlink1000OduAdmIPv6DefaultGateWay": winlink1000OduAdmIPv6DefaultGateWay,
       "winlink1000OduAdmPowerConsumption": winlink1000OduAdmPowerConsumption,
       "winlink1000OduAdmWifi": winlink1000OduAdmWifi,
       "winlink1000OduAdmWifiChannel": winlink1000OduAdmWifiChannel,
       "winlink1000OduAdmWifiTxPower": winlink1000OduAdmWifiTxPower,
       "winlink1000OduAdmWifiSSID": winlink1000OduAdmWifiSSID,
       "winlink1000OduAdmWifiSecurityType": winlink1000OduAdmWifiSecurityType,
       "winlink1000OduAdmWifiPassword": winlink1000OduAdmWifiPassword,
       "winlink1000OduAdmWifiNetwork": winlink1000OduAdmWifiNetwork,
       "winlink1000OduAdmWifiRssi": winlink1000OduAdmWifiRssi,
       "winlink1000OduAdmWifiStationMAC": winlink1000OduAdmWifiStationMAC,
       "winlink1000OduAdmWifiRestart": winlink1000OduAdmWifiRestart,
       "winlink1000OduAdmWifiApStatus": winlink1000OduAdmWifiApStatus,
       "winlink1000OduAdmBsaOperationMode": winlink1000OduAdmBsaOperationMode,
       "winlink1000OduAdmMngConnection": winlink1000OduAdmMngConnection,
       "winlink1000OduAdm1588TCSupport": winlink1000OduAdm1588TCSupport,
       "winlink1000OduAdmSyncESupport": winlink1000OduAdmSyncESupport,
       "winlink1000OduAdmRadioRev": winlink1000OduAdmRadioRev,
       "winlink1000OduAdmProductRev": winlink1000OduAdmProductRev,
       "winlink1000OduAdmPMPSUSupport": winlink1000OduAdmPMPSUSupport,
       "winlink1000OduAdmManagerDownloadURL": winlink1000OduAdmManagerDownloadURL,
       "winlink1000OduAdmAntennaDescription": winlink1000OduAdmAntennaDescription,
       "winlink1000OduAdmSwCapabilities": winlink1000OduAdmSwCapabilities,
       "winlink1000OduService": winlink1000OduService,
       "winlink1000OduSrvMode": winlink1000OduSrvMode,
       "winlink1000OduSrvBridging": winlink1000OduSrvBridging,
       "winlink1000OduServiceRingTopology": winlink1000OduServiceRingTopology,
       "winlink1000OduSrvRingLinkMode": winlink1000OduSrvRingLinkMode,
       "winlink1000OduSrvRingTopologySupported": winlink1000OduSrvRingTopologySupported,
       "winlink1000OduSrvRingVlanIdTable": winlink1000OduSrvRingVlanIdTable,
       "winlink1000OduSrvRingVlanIdEntry": winlink1000OduSrvRingVlanIdEntry,
       "winlink1000OduSrvRingVlanIdIndex": winlink1000OduSrvRingVlanIdIndex,
       "winlink1000OduSrvRingVlanId": winlink1000OduSrvRingVlanId,
       "winlink1000OduSrvRingEthStatus": winlink1000OduSrvRingEthStatus,
       "winlink1000OduSrvRingMaxAllowedTimeFromLastRpm": winlink1000OduSrvRingMaxAllowedTimeFromLastRpm,
       "winlink1000OduSrvRingWTR": winlink1000OduSrvRingWTR,
       "winlink1000OduServiceQoS": winlink1000OduServiceQoS,
       "winlink1000OduSrvQoSMode": winlink1000OduSrvQoSMode,
       "winlink1000OduSrvQoSConfTable": winlink1000OduSrvQoSConfTable,
       "winlink1000OduSrvQoSConfEntry": winlink1000OduSrvQoSConfEntry,
       "winlink1000OduSrvQoSConfIndex": winlink1000OduSrvQoSConfIndex,
       "winlink1000OduSrvConfVlanQGroups": winlink1000OduSrvConfVlanQGroups,
       "winlink1000OduSrvConfDiffservQGroups": winlink1000OduSrvConfDiffservQGroups,
       "winlink1000OduSrvConfQueMir": winlink1000OduSrvConfQueMir,
       "winlink1000OduSrvConfQueWeight": winlink1000OduSrvConfQueWeight,
       "winlink1000OduSrvQoSVlanQGroupsSetStr": winlink1000OduSrvQoSVlanQGroupsSetStr,
       "winlink1000OduSrvQoSDiffservQGroupsSetStr": winlink1000OduSrvQoSDiffservQGroupsSetStr,
       "winlink1000OduSrvQoSMaxRTQuePercent": winlink1000OduSrvQoSMaxRTQuePercent,
       "winlink1000OduServiceVlan": winlink1000OduServiceVlan,
       "winlink1000OduSrvVlanSupport": winlink1000OduSrvVlanSupport,
       "winlink1000OduSrvVlanIngressMode": winlink1000OduSrvVlanIngressMode,
       "winlink1000OduSrvVlanEgressMode": winlink1000OduSrvVlanEgressMode,
       "winlink1000OduSrvEgressTag": winlink1000OduSrvEgressTag,
       "winlink1000OduSrvEgressProviderTag": winlink1000OduSrvEgressProviderTag,
       "winlink1000OduSrvVlanIngressAllowedVIDs": winlink1000OduSrvVlanIngressAllowedVIDs,
       "winlink1000OduSrvVlanDisable": winlink1000OduSrvVlanDisable,
       "winlink1000OduServiceVlanProviderListTPIDstr": winlink1000OduServiceVlanProviderListTPIDstr,
       "winlink1000OduEthernet": winlink1000OduEthernet,
       "winlink1000OduEthernetRemainingRate": winlink1000OduEthernetRemainingRate,
       "winlink1000OduEthernetIfTable": winlink1000OduEthernetIfTable,
       "winlink1000OduEthernetIfEntry": winlink1000OduEthernetIfEntry,
       "winlink1000OduEthernetIfIndex": winlink1000OduEthernetIfIndex,
       "winlink1000OduEthernetIfAddress": winlink1000OduEthernetIfAddress,
       "winlink1000OduEthernetIfAdminStatus": winlink1000OduEthernetIfAdminStatus,
       "winlink1000OduEthernetIfOperStatus": winlink1000OduEthernetIfOperStatus,
       "winlink1000OduEthernetIfFailAction": winlink1000OduEthernetIfFailAction,
       "winlink1000OduEthernetIf1588v2PTPEventRXRate": winlink1000OduEthernetIf1588v2PTPEventRXRate,
       "winlink1000OduEthernetIf1588v2PTPEventTXRate": winlink1000OduEthernetIf1588v2PTPEventTXRate,
       "winlink1000OduEthernetNumOfPorts": winlink1000OduEthernetNumOfPorts,
       "winlink1000OduEthernetGbeSupported": winlink1000OduEthernetGbeSupported,
       "winlink1000OduEthernetSfpProperties": winlink1000OduEthernetSfpProperties,
       "winlink1000OduBridge": winlink1000OduBridge,
       "winlink1000OduBridgeBase": winlink1000OduBridgeBase,
       "winlink1000OduBridgeBasePortTable": winlink1000OduBridgeBasePortTable,
       "winlink1000OduBridgeBasePortEntry": winlink1000OduBridgeBasePortEntry,
       "winlink1000OduBridgeBasePortIndex": winlink1000OduBridgeBasePortIndex,
       "winlink1000OduBridgeBaseIfIndex": winlink1000OduBridgeBaseIfIndex,
       "winlink1000OduBridgeTp": winlink1000OduBridgeTp,
       "winlink1000OduBridgeTpPortTable": winlink1000OduBridgeTpPortTable,
       "winlink1000OduBridgeTpPortEntry": winlink1000OduBridgeTpPortEntry,
       "winlink1000OduBridgeTpPortIndex": winlink1000OduBridgeTpPortIndex,
       "winlink1000OduBridgeTpPortInFrames": winlink1000OduBridgeTpPortInFrames,
       "winlink1000OduBridgeTpPortOutFrames": winlink1000OduBridgeTpPortOutFrames,
       "winlink1000OduBridgeTpPortInBytes": winlink1000OduBridgeTpPortInBytes,
       "winlink1000OduBridgeTpPortOutBytes": winlink1000OduBridgeTpPortOutBytes,
       "winlink1000OduBridgeTpMode": winlink1000OduBridgeTpMode,
       "winlink1000OduBridgeConfigMode": winlink1000OduBridgeConfigMode,
       "winlink1000OduAir": winlink1000OduAir,
       "winlink1000OduAirFreq": winlink1000OduAirFreq,
       "winlink1000OduAirDesiredRate": winlink1000OduAirDesiredRate,
       "winlink1000OduAirSSID": winlink1000OduAirSSID,
       "winlink1000OduAirTxPower": winlink1000OduAirTxPower,
       "winlink1000OduAirSesState": winlink1000OduAirSesState,
       "winlink1000OduAirMstrSlv": winlink1000OduAirMstrSlv,
       "winlink1000OduAirResync": winlink1000OduAirResync,
       "winlink1000OduAirPerf": winlink1000OduAirPerf,
       "winlink1000OduAirRxPower": winlink1000OduAirRxPower,
       "winlink1000OduAirTotalFrames": winlink1000OduAirTotalFrames,
       "winlink1000OduAirBadFrames": winlink1000OduAirBadFrames,
       "winlink1000OduAirCurrentRate": winlink1000OduAirCurrentRate,
       "winlink1000OduAirCurrentRateIdx": winlink1000OduAirCurrentRateIdx,
       "winlink1000OduAirChainsRxPower": winlink1000OduAirChainsRxPower,
       "winlink1000OduAirCurrentRateCBW": winlink1000OduAirCurrentRateCBW,
       "winlink1000OduAirCurrentRateGI": winlink1000OduAirCurrentRateGI,
       "winlink1000OduAirTxPower36": winlink1000OduAirTxPower36,
       "winlink1000OduAirTxPower48": winlink1000OduAirTxPower48,
       "winlink1000OduAirCurrentTxPower": winlink1000OduAirCurrentTxPower,
       "winlink1000OduAirMinFrequency": winlink1000OduAirMinFrequency,
       "winlink1000OduAirMaxFrequency": winlink1000OduAirMaxFrequency,
       "winlink1000OduAirFreqResolution": winlink1000OduAirFreqResolution,
       "winlink1000OduAirCurrentFreq": winlink1000OduAirCurrentFreq,
       "winlink1000OduAirNumberOfChannels": winlink1000OduAirNumberOfChannels,
       "winlink1000OduAirChannelsTable": winlink1000OduAirChannelsTable,
       "winlink1000OduAirChannelsEntry": winlink1000OduAirChannelsEntry,
       "winlink1000OduAirChannelsIndex": winlink1000OduAirChannelsIndex,
       "winlink1000OduAirChannelsFrequency": winlink1000OduAirChannelsFrequency,
       "winlink1000OduAirChannelsOperState": winlink1000OduAirChannelsOperState,
       "winlink1000OduAirChannelsAvail": winlink1000OduAirChannelsAvail,
       "winlink1000OduAirChannelsDefaultFreq": winlink1000OduAirChannelsDefaultFreq,
       "winlink1000OduAirDfsState": winlink1000OduAirDfsState,
       "winlink1000OduAirAutoChannelSelectionState": winlink1000OduAirAutoChannelSelectionState,
       "winlink1000OduAirEnableTxPower": winlink1000OduAirEnableTxPower,
       "winlink1000OduAirMinTxPower": winlink1000OduAirMinTxPower,
       "winlink1000OduAirMaxTxPowerTable": winlink1000OduAirMaxTxPowerTable,
       "winlink1000OduAirMaxTxPowerEntry": winlink1000OduAirMaxTxPowerEntry,
       "winlink1000OduAirMaxTxPowerIndex": winlink1000OduAirMaxTxPowerIndex,
       "winlink1000OduAirMaxTxPower": winlink1000OduAirMaxTxPower,
       "winlink1000OduAirChannelBandwidth": winlink1000OduAirChannelBandwidth,
       "winlink1000OduAirChannelBWTable": winlink1000OduAirChannelBWTable,
       "winlink1000OduAirChannelBWEntry": winlink1000OduAirChannelBWEntry,
       "winlink1000OduAirChannelBWIndex": winlink1000OduAirChannelBWIndex,
       "winlink1000OduAirChannelBWAvail": winlink1000OduAirChannelBWAvail,
       "winlink1000OduAirChannelsAdminState": winlink1000OduAirChannelsAdminState,
       "winlink1000OduAirChannelBWHSSATDDConflictPerCBW": winlink1000OduAirChannelBWHSSATDDConflictPerCBW,
       "winlink1000OduAirChannelBWMinRatioForSupporting": winlink1000OduAirChannelBWMinRatioForSupporting,
       "winlink1000OduAirChannelBWMaxRatioForSupporting": winlink1000OduAirChannelBWMaxRatioForSupporting,
       "winlink1000OduAirRFD": winlink1000OduAirRFD,
       "winlink1000OduAirRatesTable": winlink1000OduAirRatesTable,
       "winlink1000OduAirRatesEntry": winlink1000OduAirRatesEntry,
       "winlink1000OduAirRatesIndex": winlink1000OduAirRatesIndex,
       "winlink1000OduAirRatesAvail": winlink1000OduAirRatesAvail,
       "winlink1000OduAirDesiredRateIdx": winlink1000OduAirDesiredRateIdx,
       "winlink1000OduAirLinkDistance": winlink1000OduAirLinkDistance,
       "winlink1000OduAirLinkWorkingMode": winlink1000OduAirLinkWorkingMode,
       "winlink1000OduAirMajorLinkIfVersion": winlink1000OduAirMajorLinkIfVersion,
       "winlink1000OduAirMinorLinkIfVersion": winlink1000OduAirMinorLinkIfVersion,
       "winlink1000OduAirHss": winlink1000OduAirHss,
       "winlink1000OduAirHssDesiredOpState": winlink1000OduAirHssDesiredOpState,
       "winlink1000OduAirHssCurrentOpState": winlink1000OduAirHssCurrentOpState,
       "winlink1000OduAirHssSyncStatus": winlink1000OduAirHssSyncStatus,
       "winlink1000OduAirHssExtPulseStatus": winlink1000OduAirHssExtPulseStatus,
       "winlink1000OduAirHssExtPulseType": winlink1000OduAirHssExtPulseType,
       "winlink1000OduAirHssDesiredExtPulseType": winlink1000OduAirHssDesiredExtPulseType,
       "winlink1000OduAirHssRfpTable": winlink1000OduAirHssRfpTable,
       "winlink1000OduAirHssRfpEntry": winlink1000OduAirHssRfpEntry,
       "winlink1000OduAirHssRfpIndex": winlink1000OduAirHssRfpIndex,
       "winlink1000OduAirHssRfpEthChannelBW5MHz": winlink1000OduAirHssRfpEthChannelBW5MHz,
       "winlink1000OduAirHssRfpTdmChannelBW5MHz": winlink1000OduAirHssRfpTdmChannelBW5MHz,
       "winlink1000OduAirHssRfpEthChannelBW10MHz": winlink1000OduAirHssRfpEthChannelBW10MHz,
       "winlink1000OduAirHssRfpTdmChannelBW10MHz": winlink1000OduAirHssRfpTdmChannelBW10MHz,
       "winlink1000OduAirHssRfpEthChannelBW20MHz": winlink1000OduAirHssRfpEthChannelBW20MHz,
       "winlink1000OduAirHssRfpTdmChannelBW20MHz": winlink1000OduAirHssRfpTdmChannelBW20MHz,
       "winlink1000OduAirHssRfpEthChannelBW40MHz": winlink1000OduAirHssRfpEthChannelBW40MHz,
       "winlink1000OduAirHssRfpTdmChannelBW40MHz": winlink1000OduAirHssRfpTdmChannelBW40MHz,
       "winlink1000OduAirHssRfpEthChannelBW80MHz": winlink1000OduAirHssRfpEthChannelBW80MHz,
       "winlink1000OduAirHssRfpEthChannelBW7MHz": winlink1000OduAirHssRfpEthChannelBW7MHz,
       "winlink1000OduAirHssRfpEthChannelBW14MHz": winlink1000OduAirHssRfpEthChannelBW14MHz,
       "winlink1000OduAirHssRfpStr": winlink1000OduAirHssRfpStr,
       "winlink1000OduAirHssHsmID": winlink1000OduAirHssHsmID,
       "winlink1000OduAirHssTime": winlink1000OduAirHssTime,
       "winlink1000OduAirHssLatitude": winlink1000OduAirHssLatitude,
       "winlink1000OduAirHssNSIndicator": winlink1000OduAirHssNSIndicator,
       "winlink1000OduAirHssLongitude": winlink1000OduAirHssLongitude,
       "winlink1000OduAirHssEWIndicator": winlink1000OduAirHssEWIndicator,
       "winlink1000OduAirHssNumSatellites": winlink1000OduAirHssNumSatellites,
       "winlink1000OduAirHssAltitude": winlink1000OduAirHssAltitude,
       "winlink1000OduAirHssRfpPhase": winlink1000OduAirHssRfpPhase,
       "winlink1000OduAirHssInterSiteSynchronizationMode": winlink1000OduAirHssInterSiteSynchronizationMode,
       "winlink1000OduAirHssInterSiteSynchronizationAvailability": winlink1000OduAirHssInterSiteSynchronizationAvailability,
       "winlink1000OduAirHssSatellitesSatSyncRequired": winlink1000OduAirHssSatellitesSatSyncRequired,
       "winlink1000OduAirHssDomainID": winlink1000OduAirHssDomainID,
       "winlink1000OduAirHssSupportedSynchronizationProtocol": winlink1000OduAirHssSupportedSynchronizationProtocol,
       "winlink1000OduAirHssDesiredSynchronizationProtocol": winlink1000OduAirHssDesiredSynchronizationProtocol,
       "winlink1000OduAirHssDiscover": winlink1000OduAirHssDiscover,
       "winlink1000OduAirHssNumberOfDiscoveredODUs": winlink1000OduAirHssNumberOfDiscoveredODUs,
       "winlink1000OduAirHssDiscoverTable": winlink1000OduAirHssDiscoverTable,
       "winlink1000OduAirHssDiscoverEntry": winlink1000OduAirHssDiscoverEntry,
       "winlink1000OduAirHssDiscoverIndex": winlink1000OduAirHssDiscoverIndex,
       "winlink1000OduAirHssDiscoverODUDescription": winlink1000OduAirHssDiscoverODUDescription,
       "winlink1000OduAirHssMasterSlaveCompatibility": winlink1000OduAirHssMasterSlaveCompatibility,
       "winlink1000OduAirHssNumberOfAssociatedCU": winlink1000OduAirHssNumberOfAssociatedCU,
       "winlink1000OduAirHssAssociatedCUTable": winlink1000OduAirHssAssociatedCUTable,
       "winlink1000OduAirHssAssociatedCUTableEntry": winlink1000OduAirHssAssociatedCUTableEntry,
       "winlink1000OduAirHssAssociatedCUIndex": winlink1000OduAirHssAssociatedCUIndex,
       "winlink1000OduAirHssAssociatedCUDescription": winlink1000OduAirHssAssociatedCUDescription,
       "winlink1000OduAirHssSyncStatusEth": winlink1000OduAirHssSyncStatusEth,
       "winlink1000OduAirHssEthVLANTag": winlink1000OduAirHssEthVLANTag,
       "winlink1000OduAirHssHSMIPAddress": winlink1000OduAirHssHSMIPAddress,
       "winlink1000OduAirHssDelayToHSM": winlink1000OduAirHssDelayToHSM,
       "winlink1000OduAirHssSyncAcquisitionSeconds": winlink1000OduAirHssSyncAcquisitionSeconds,
       "winlink1000OduAirHssHSMIPv6Address": winlink1000OduAirHssHSMIPv6Address,
       "winlink1000OduAirLockRemote": winlink1000OduAirLockRemote,
       "winlink1000OduAirAntennaGain": winlink1000OduAirAntennaGain}
)
