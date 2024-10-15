# SNMP MIB module (VPNPOLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VPNPOLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:17 2024
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



class VpIpAddress(OctetString):
    """Custom type VpIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbmIROCVPNpolicy_ObjectIdentity = ObjectIdentity
ibmIROCVPNpolicy = _IbmIROCVPNpolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15)
)
_VpSystem_ObjectIdentity = ObjectIdentity
vpSystem = _VpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1)
)
_VpSystemGlobal_ObjectIdentity = ObjectIdentity
vpSystemGlobal = _VpSystemGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 1)
)
_VpSysMibLevel_Type = Integer32
_VpSysMibLevel_Object = MibScalar
vpSysMibLevel = _VpSysMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 1, 1),
    _VpSysMibLevel_Type()
)
vpSysMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSysMibLevel.setStatus("mandatory")
_VpSysUpTime_Type = TimeTicks
_VpSysUpTime_Object = MibScalar
vpSysUpTime = _VpSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 1, 2),
    _VpSysUpTime_Type()
)
vpSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSysUpTime.setStatus("mandatory")


class _VpSysCurTime_Type(OctetString):
    """Custom type vpSysCurTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_VpSysCurTime_Type.__name__ = "OctetString"
_VpSysCurTime_Object = MibScalar
vpSysCurTime = _VpSysCurTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 1, 3),
    _VpSysCurTime_Type()
)
vpSysCurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSysCurTime.setStatus("mandatory")


class _VpSysHoursFromCut_Type(Integer32):
    """Custom type vpSysHoursFromCut based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("utcMinus0", 1),
          ("utcMinus1", 2),
          ("utcMinus10", 11),
          ("utcMinus11", 12),
          ("utcMinus2", 3),
          ("utcMinus3", 4),
          ("utcMinus4", 5),
          ("utcMinus5", 6),
          ("utcMinus6", 7),
          ("utcMinus7", 8),
          ("utcMinus8", 9),
          ("utcMinus9", 10),
          ("utcPlus1", 13),
          ("utcPlus10", 22),
          ("utcPlus11", 23),
          ("utcPlus12", 24),
          ("utcPlus2", 14),
          ("utcPlus3", 15),
          ("utcPlus4", 16),
          ("utcPlus5", 17),
          ("utcPlus6", 18),
          ("utcPlus7", 19),
          ("utcPlus8", 20),
          ("utcPlus9", 21))
    )


_VpSysHoursFromCut_Type.__name__ = "Integer32"
_VpSysHoursFromCut_Object = MibScalar
vpSysHoursFromCut = _VpSysHoursFromCut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 1, 4),
    _VpSysHoursFromCut_Type()
)
vpSysHoursFromCut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSysHoursFromCut.setStatus("mandatory")


class _VpSysCurConfigSource_Type(Integer32):
    """Custom type vpSysCurConfigSource based on Integer32"""
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
        *(("allSources", 3),
          ("ldap", 5),
          ("none", 2),
          ("refreshInProgress", 1),
          ("sram", 4))
    )


_VpSysCurConfigSource_Type.__name__ = "Integer32"
_VpSysCurConfigSource_Object = MibScalar
vpSysCurConfigSource = _VpSysCurConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 1, 5),
    _VpSysCurConfigSource_Type()
)
vpSysCurConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSysCurConfigSource.setStatus("mandatory")


class _VpSysRefreshConfig_Type(Integer32):
    """Custom type vpSysRefreshConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fromAdminDefs", 2),
          ("fromOperDefs", 1))
    )


_VpSysRefreshConfig_Type.__name__ = "Integer32"
_VpSysRefreshConfig_Object = MibScalar
vpSysRefreshConfig = _VpSysRefreshConfig_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 1, 6),
    _VpSysRefreshConfig_Type()
)
vpSysRefreshConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpSysRefreshConfig.setStatus("mandatory")
_VpSystemLdap_ObjectIdentity = ObjectIdentity
vpSystemLdap = _VpSystemLdap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2)
)
_VpLdapGlobal_ObjectIdentity = ObjectIdentity
vpLdapGlobal = _VpLdapGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1)
)
_VpLdapGlobalOper_ObjectIdentity = ObjectIdentity
vpLdapGlobalOper = _VpLdapGlobalOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 1)
)


class _VpLdapGblOperLdapStatus_Type(Integer32):
    """Custom type vpLdapGblOperLdapStatus based on Integer32"""
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


_VpLdapGblOperLdapStatus_Type.__name__ = "Integer32"
_VpLdapGblOperLdapStatus_Object = MibScalar
vpLdapGblOperLdapStatus = _VpLdapGblOperLdapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 1, 1),
    _VpLdapGblOperLdapStatus_Type()
)
vpLdapGblOperLdapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpLdapGblOperLdapStatus.setStatus("mandatory")
_VpLdapGblOperPrimServerAddr_Type = VpIpAddress
_VpLdapGblOperPrimServerAddr_Object = MibScalar
vpLdapGblOperPrimServerAddr = _VpLdapGblOperPrimServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 1, 2),
    _VpLdapGblOperPrimServerAddr_Type()
)
vpLdapGblOperPrimServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpLdapGblOperPrimServerAddr.setStatus("mandatory")
_VpLdapGblOperSecServerAddr_Type = VpIpAddress
_VpLdapGblOperSecServerAddr_Object = MibScalar
vpLdapGblOperSecServerAddr = _VpLdapGblOperSecServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 1, 3),
    _VpLdapGblOperSecServerAddr_Type()
)
vpLdapGblOperSecServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpLdapGblOperSecServerAddr.setStatus("mandatory")
_VpLdapGblOperServerLdapLvl_Type = Integer32
_VpLdapGblOperServerLdapLvl_Object = MibScalar
vpLdapGblOperServerLdapLvl = _VpLdapGblOperServerLdapLvl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 1, 4),
    _VpLdapGblOperServerLdapLvl_Type()
)
vpLdapGblOperServerLdapLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpLdapGblOperServerLdapLvl.setStatus("mandatory")
_VpLdapGblOperPolicyBaseName_Type = DisplayString
_VpLdapGblOperPolicyBaseName_Object = MibScalar
vpLdapGblOperPolicyBaseName = _VpLdapGblOperPolicyBaseName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 1, 5),
    _VpLdapGblOperPolicyBaseName_Type()
)
vpLdapGblOperPolicyBaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpLdapGblOperPolicyBaseName.setStatus("mandatory")
_VpLdapGblOperPortNumber_Type = Integer32
_VpLdapGblOperPortNumber_Object = MibScalar
vpLdapGblOperPortNumber = _VpLdapGblOperPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 1, 6),
    _VpLdapGblOperPortNumber_Type()
)
vpLdapGblOperPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpLdapGblOperPortNumber.setStatus("mandatory")
_VpLdapGblOperTimeOut_Type = Integer32
_VpLdapGblOperTimeOut_Object = MibScalar
vpLdapGblOperTimeOut = _VpLdapGblOperTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 1, 7),
    _VpLdapGblOperTimeOut_Type()
)
vpLdapGblOperTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpLdapGblOperTimeOut.setStatus("mandatory")
_VpLdapGblOperRetryInterval_Type = Integer32
_VpLdapGblOperRetryInterval_Object = MibScalar
vpLdapGblOperRetryInterval = _VpLdapGblOperRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 1, 8),
    _VpLdapGblOperRetryInterval_Type()
)
vpLdapGblOperRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpLdapGblOperRetryInterval.setStatus("mandatory")
_VpLdapGblOperUserId_Type = DisplayString
_VpLdapGblOperUserId_Object = MibScalar
vpLdapGblOperUserId = _VpLdapGblOperUserId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 1, 9),
    _VpLdapGblOperUserId_Type()
)
vpLdapGblOperUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpLdapGblOperUserId.setStatus("mandatory")
_VpLdapGlobalAdmin_ObjectIdentity = ObjectIdentity
vpLdapGlobalAdmin = _VpLdapGlobalAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 2)
)


class _VpLdapGblAdminLdapStatus_Type(Integer32):
    """Custom type vpLdapGblAdminLdapStatus based on Integer32"""
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


_VpLdapGblAdminLdapStatus_Type.__name__ = "Integer32"
_VpLdapGblAdminLdapStatus_Object = MibScalar
vpLdapGblAdminLdapStatus = _VpLdapGblAdminLdapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 2, 1),
    _VpLdapGblAdminLdapStatus_Type()
)
vpLdapGblAdminLdapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpLdapGblAdminLdapStatus.setStatus("mandatory")
_VpLdapGblAdminPrimServerAddr_Type = VpIpAddress
_VpLdapGblAdminPrimServerAddr_Object = MibScalar
vpLdapGblAdminPrimServerAddr = _VpLdapGblAdminPrimServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 2, 2),
    _VpLdapGblAdminPrimServerAddr_Type()
)
vpLdapGblAdminPrimServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpLdapGblAdminPrimServerAddr.setStatus("mandatory")
_VpLdapGblAdminSecServerAddr_Type = VpIpAddress
_VpLdapGblAdminSecServerAddr_Object = MibScalar
vpLdapGblAdminSecServerAddr = _VpLdapGblAdminSecServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 2, 3),
    _VpLdapGblAdminSecServerAddr_Type()
)
vpLdapGblAdminSecServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpLdapGblAdminSecServerAddr.setStatus("mandatory")
_VpLdapGblAdminServerLdapLvl_Type = Integer32
_VpLdapGblAdminServerLdapLvl_Object = MibScalar
vpLdapGblAdminServerLdapLvl = _VpLdapGblAdminServerLdapLvl_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 2, 4),
    _VpLdapGblAdminServerLdapLvl_Type()
)
vpLdapGblAdminServerLdapLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpLdapGblAdminServerLdapLvl.setStatus("mandatory")
_VpLdapGblAdminPolicyBaseName_Type = DisplayString
_VpLdapGblAdminPolicyBaseName_Object = MibScalar
vpLdapGblAdminPolicyBaseName = _VpLdapGblAdminPolicyBaseName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 2, 5),
    _VpLdapGblAdminPolicyBaseName_Type()
)
vpLdapGblAdminPolicyBaseName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpLdapGblAdminPolicyBaseName.setStatus("mandatory")
_VpLdapGblAdminPortNumber_Type = Integer32
_VpLdapGblAdminPortNumber_Object = MibScalar
vpLdapGblAdminPortNumber = _VpLdapGblAdminPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 2, 6),
    _VpLdapGblAdminPortNumber_Type()
)
vpLdapGblAdminPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpLdapGblAdminPortNumber.setStatus("mandatory")
_VpLdapGblAdminTimeOut_Type = Integer32
_VpLdapGblAdminTimeOut_Object = MibScalar
vpLdapGblAdminTimeOut = _VpLdapGblAdminTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 2, 7),
    _VpLdapGblAdminTimeOut_Type()
)
vpLdapGblAdminTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpLdapGblAdminTimeOut.setStatus("mandatory")
_VpLdapGblAdminRetryInterval_Type = Integer32
_VpLdapGblAdminRetryInterval_Object = MibScalar
vpLdapGblAdminRetryInterval = _VpLdapGblAdminRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 2, 8),
    _VpLdapGblAdminRetryInterval_Type()
)
vpLdapGblAdminRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpLdapGblAdminRetryInterval.setStatus("mandatory")
_VpLdapGblAdminUserId_Type = DisplayString
_VpLdapGblAdminUserId_Object = MibScalar
vpLdapGblAdminUserId = _VpLdapGblAdminUserId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 1, 2, 1, 2, 9),
    _VpLdapGblAdminUserId_Type()
)
vpLdapGblAdminUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpLdapGblAdminUserId.setStatus("mandatory")
_VpPolicy_ObjectIdentity = ObjectIdentity
vpPolicy = _VpPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2)
)
_VpPolicyTable_Object = MibTable
vpPolicyTable = _VpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1)
)
if mibBuilder.loadTexts:
    vpPolicyTable.setStatus("mandatory")
_VpPolicyEntry_Object = MibTableRow
vpPolicyEntry = _VpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1, 1)
)
vpPolicyEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpPolName"),
)
if mibBuilder.loadTexts:
    vpPolicyEntry.setStatus("mandatory")
_VpPolName_Type = DisplayString
_VpPolName_Object = MibTableColumn
vpPolName = _VpPolName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1, 1, 1),
    _VpPolName_Type()
)
vpPolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolName.setStatus("mandatory")


class _VpPolStatus_Type(Integer32):
    """Custom type vpPolStatus based on Integer32"""
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


_VpPolStatus_Type.__name__ = "Integer32"
_VpPolStatus_Object = MibTableColumn
vpPolStatus = _VpPolStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1, 1, 2),
    _VpPolStatus_Type()
)
vpPolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpPolStatus.setStatus("mandatory")


class _VpPolPriority_Type(Integer32):
    """Custom type vpPolPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VpPolPriority_Type.__name__ = "Integer32"
_VpPolPriority_Object = MibTableColumn
vpPolPriority = _VpPolPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1, 1, 3),
    _VpPolPriority_Type()
)
vpPolPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolPriority.setStatus("mandatory")


class _VpPolValidity_Type(Integer32):
    """Custom type vpPolValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_VpPolValidity_Type.__name__ = "Integer32"
_VpPolValidity_Object = MibTableColumn
vpPolValidity = _VpPolValidity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1, 1, 4),
    _VpPolValidity_Type()
)
vpPolValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolValidity.setStatus("mandatory")
_VpPolTrafficProfileRef_Type = DisplayString
_VpPolTrafficProfileRef_Object = MibTableColumn
vpPolTrafficProfileRef = _VpPolTrafficProfileRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1, 1, 5),
    _VpPolTrafficProfileRef_Type()
)
vpPolTrafficProfileRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolTrafficProfileRef.setStatus("mandatory")
_VpPolValidityPeriodRef_Type = DisplayString
_VpPolValidityPeriodRef_Object = MibTableColumn
vpPolValidityPeriodRef = _VpPolValidityPeriodRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1, 1, 6),
    _VpPolValidityPeriodRef_Type()
)
vpPolValidityPeriodRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolValidityPeriodRef.setStatus("mandatory")
_VpPolRsvpActionRef_Type = DisplayString
_VpPolRsvpActionRef_Object = MibTableColumn
vpPolRsvpActionRef = _VpPolRsvpActionRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1, 1, 7),
    _VpPolRsvpActionRef_Type()
)
vpPolRsvpActionRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolRsvpActionRef.setStatus("mandatory")
_VpPolDiffServActionRef_Type = DisplayString
_VpPolDiffServActionRef_Object = MibTableColumn
vpPolDiffServActionRef = _VpPolDiffServActionRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1, 1, 8),
    _VpPolDiffServActionRef_Type()
)
vpPolDiffServActionRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolDiffServActionRef.setStatus("mandatory")
_VpPolIsakmpActionRef_Type = DisplayString
_VpPolIsakmpActionRef_Object = MibTableColumn
vpPolIsakmpActionRef = _VpPolIsakmpActionRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1, 1, 9),
    _VpPolIsakmpActionRef_Type()
)
vpPolIsakmpActionRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolIsakmpActionRef.setStatus("mandatory")
_VpPolSecurityActionRef_Type = DisplayString
_VpPolSecurityActionRef_Object = MibTableColumn
vpPolSecurityActionRef = _VpPolSecurityActionRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1, 1, 10),
    _VpPolSecurityActionRef_Type()
)
vpPolSecurityActionRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolSecurityActionRef.setStatus("mandatory")
_VpPolIpsecManualTunId_Type = Integer32
_VpPolIpsecManualTunId_Object = MibTableColumn
vpPolIpsecManualTunId = _VpPolIpsecManualTunId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1, 1, 11),
    _VpPolIpsecManualTunId_Type()
)
vpPolIpsecManualTunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolIpsecManualTunId.setStatus("mandatory")
_VpPolMatches_Type = Counter32
_VpPolMatches_Object = MibTableColumn
vpPolMatches = _VpPolMatches_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 1, 1, 12),
    _VpPolMatches_Type()
)
vpPolMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolMatches.setStatus("mandatory")
_VpPolicyRulePriTable_Object = MibTable
vpPolicyRulePriTable = _VpPolicyRulePriTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 2)
)
if mibBuilder.loadTexts:
    vpPolicyRulePriTable.setStatus("mandatory")
_VpPolicyRulePriEntry_Object = MibTableRow
vpPolicyRulePriEntry = _VpPolicyRulePriEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 2, 1)
)
vpPolicyRulePriEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpPolRulePriOrder"),
)
if mibBuilder.loadTexts:
    vpPolicyRulePriEntry.setStatus("mandatory")
_VpPolRulePriOrder_Type = Integer32
_VpPolRulePriOrder_Object = MibTableColumn
vpPolRulePriOrder = _VpPolRulePriOrder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 2, 1, 1),
    _VpPolRulePriOrder_Type()
)
vpPolRulePriOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolRulePriOrder.setStatus("mandatory")
_VpPolRulePriName_Type = DisplayString
_VpPolRulePriName_Object = MibTableColumn
vpPolRulePriName = _VpPolRulePriName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 2, 1, 2),
    _VpPolRulePriName_Type()
)
vpPolRulePriName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolRulePriName.setStatus("mandatory")


class _VpPolRulePriStatus_Type(Integer32):
    """Custom type vpPolRulePriStatus based on Integer32"""
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


_VpPolRulePriStatus_Type.__name__ = "Integer32"
_VpPolRulePriStatus_Object = MibTableColumn
vpPolRulePriStatus = _VpPolRulePriStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 2, 1, 3),
    _VpPolRulePriStatus_Type()
)
vpPolRulePriStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpPolRulePriStatus.setStatus("mandatory")
_VpPolRulePriPriority_Type = Integer32
_VpPolRulePriPriority_Object = MibTableColumn
vpPolRulePriPriority = _VpPolRulePriPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 2, 1, 4),
    _VpPolRulePriPriority_Type()
)
vpPolRulePriPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolRulePriPriority.setStatus("mandatory")
_VpPolRulePriTrafficProfileRef_Type = DisplayString
_VpPolRulePriTrafficProfileRef_Object = MibTableColumn
vpPolRulePriTrafficProfileRef = _VpPolRulePriTrafficProfileRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 2, 1, 5),
    _VpPolRulePriTrafficProfileRef_Type()
)
vpPolRulePriTrafficProfileRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolRulePriTrafficProfileRef.setStatus("mandatory")
_VpPolRulePriValidityPeriodRef_Type = DisplayString
_VpPolRulePriValidityPeriodRef_Object = MibTableColumn
vpPolRulePriValidityPeriodRef = _VpPolRulePriValidityPeriodRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 2, 1, 6),
    _VpPolRulePriValidityPeriodRef_Type()
)
vpPolRulePriValidityPeriodRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolRulePriValidityPeriodRef.setStatus("mandatory")
_VpPolRulePriRsvpActionRef_Type = DisplayString
_VpPolRulePriRsvpActionRef_Object = MibTableColumn
vpPolRulePriRsvpActionRef = _VpPolRulePriRsvpActionRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 2, 1, 7),
    _VpPolRulePriRsvpActionRef_Type()
)
vpPolRulePriRsvpActionRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolRulePriRsvpActionRef.setStatus("mandatory")
_VpPolRulePriDiffServActionRef_Type = DisplayString
_VpPolRulePriDiffServActionRef_Object = MibTableColumn
vpPolRulePriDiffServActionRef = _VpPolRulePriDiffServActionRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 2, 1, 8),
    _VpPolRulePriDiffServActionRef_Type()
)
vpPolRulePriDiffServActionRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolRulePriDiffServActionRef.setStatus("mandatory")
_VpPolRulePriIsakmpActionRef_Type = DisplayString
_VpPolRulePriIsakmpActionRef_Object = MibTableColumn
vpPolRulePriIsakmpActionRef = _VpPolRulePriIsakmpActionRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 2, 1, 9),
    _VpPolRulePriIsakmpActionRef_Type()
)
vpPolRulePriIsakmpActionRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolRulePriIsakmpActionRef.setStatus("mandatory")
_VpPolRulePriSecurityActionRef_Type = DisplayString
_VpPolRulePriSecurityActionRef_Object = MibTableColumn
vpPolRulePriSecurityActionRef = _VpPolRulePriSecurityActionRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 2, 1, 10),
    _VpPolRulePriSecurityActionRef_Type()
)
vpPolRulePriSecurityActionRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolRulePriSecurityActionRef.setStatus("mandatory")
_VpPolRulePriIpsecManualTunId_Type = Integer32
_VpPolRulePriIpsecManualTunId_Object = MibTableColumn
vpPolRulePriIpsecManualTunId = _VpPolRulePriIpsecManualTunId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 2, 1, 11),
    _VpPolRulePriIpsecManualTunId_Type()
)
vpPolRulePriIpsecManualTunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolRulePriIpsecManualTunId.setStatus("mandatory")
_VpPolicyCorTable_Object = MibTable
vpPolicyCorTable = _VpPolicyCorTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 3)
)
if mibBuilder.loadTexts:
    vpPolicyCorTable.setStatus("mandatory")
_VpPolicyCorEntry_Object = MibTableRow
vpPolicyCorEntry = _VpPolicyCorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 3, 1)
)
vpPolicyCorEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpPolName"),
    (0, "VPNPOLICY-MIB", "vpPolCorRuleOrder"),
)
if mibBuilder.loadTexts:
    vpPolicyCorEntry.setStatus("mandatory")
_VpPolCorRuleOrder_Type = Integer32
_VpPolCorRuleOrder_Object = MibTableColumn
vpPolCorRuleOrder = _VpPolCorRuleOrder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 3, 1, 1),
    _VpPolCorRuleOrder_Type()
)
vpPolCorRuleOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolCorRuleOrder.setStatus("mandatory")
_VpPolCorRulePriOrder_Type = Integer32
_VpPolCorRulePriOrder_Object = MibTableColumn
vpPolCorRulePriOrder = _VpPolCorRulePriOrder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 2, 3, 1, 2),
    _VpPolCorRulePriOrder_Type()
)
vpPolCorRulePriOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpPolCorRulePriOrder.setStatus("mandatory")
_VpConditions_ObjectIdentity = ObjectIdentity
vpConditions = _VpConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3)
)
_VpTrafficProfile_ObjectIdentity = ObjectIdentity
vpTrafficProfile = _VpTrafficProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1)
)
_VpTrafficProfileTable_Object = MibTable
vpTrafficProfileTable = _VpTrafficProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vpTrafficProfileTable.setStatus("mandatory")
_VpTrafficProfileEntry_Object = MibTableRow
vpTrafficProfileEntry = _VpTrafficProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1)
)
vpTrafficProfileEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpTrafProfName"),
)
if mibBuilder.loadTexts:
    vpTrafficProfileEntry.setStatus("mandatory")
_VpTrafProfName_Type = DisplayString
_VpTrafProfName_Object = MibTableColumn
vpTrafProfName = _VpTrafProfName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 1),
    _VpTrafProfName_Type()
)
vpTrafProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfName.setStatus("mandatory")
_VpTrafProfHiProtocol_Type = Integer32
_VpTrafProfHiProtocol_Object = MibTableColumn
vpTrafProfHiProtocol = _VpTrafProfHiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 2),
    _VpTrafProfHiProtocol_Type()
)
vpTrafProfHiProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfHiProtocol.setStatus("mandatory")
_VpTrafProfLoProtocol_Type = Integer32
_VpTrafProfLoProtocol_Object = MibTableColumn
vpTrafProfLoProtocol = _VpTrafProfLoProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 3),
    _VpTrafProfLoProtocol_Type()
)
vpTrafProfLoProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfLoProtocol.setStatus("mandatory")
_VpTrafProfSrcHiAddr_Type = VpIpAddress
_VpTrafProfSrcHiAddr_Object = MibTableColumn
vpTrafProfSrcHiAddr = _VpTrafProfSrcHiAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 4),
    _VpTrafProfSrcHiAddr_Type()
)
vpTrafProfSrcHiAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfSrcHiAddr.setStatus("mandatory")
_VpTrafProfSrcLoAddr_Type = VpIpAddress
_VpTrafProfSrcLoAddr_Object = MibTableColumn
vpTrafProfSrcLoAddr = _VpTrafProfSrcLoAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 5),
    _VpTrafProfSrcLoAddr_Type()
)
vpTrafProfSrcLoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfSrcLoAddr.setStatus("mandatory")
_VpTrafProfSrcHiPort_Type = Integer32
_VpTrafProfSrcHiPort_Object = MibTableColumn
vpTrafProfSrcHiPort = _VpTrafProfSrcHiPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 6),
    _VpTrafProfSrcHiPort_Type()
)
vpTrafProfSrcHiPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfSrcHiPort.setStatus("mandatory")
_VpTrafProfSrcLoPort_Type = Integer32
_VpTrafProfSrcLoPort_Object = MibTableColumn
vpTrafProfSrcLoPort = _VpTrafProfSrcLoPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 7),
    _VpTrafProfSrcLoPort_Type()
)
vpTrafProfSrcLoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfSrcLoPort.setStatus("mandatory")
_VpTrafProfDstHiAddr_Type = VpIpAddress
_VpTrafProfDstHiAddr_Object = MibTableColumn
vpTrafProfDstHiAddr = _VpTrafProfDstHiAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 8),
    _VpTrafProfDstHiAddr_Type()
)
vpTrafProfDstHiAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfDstHiAddr.setStatus("mandatory")
_VpTrafProfDstLoAddr_Type = VpIpAddress
_VpTrafProfDstLoAddr_Object = MibTableColumn
vpTrafProfDstLoAddr = _VpTrafProfDstLoAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 9),
    _VpTrafProfDstLoAddr_Type()
)
vpTrafProfDstLoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfDstLoAddr.setStatus("mandatory")
_VpTrafProfDstHiPort_Type = Integer32
_VpTrafProfDstHiPort_Object = MibTableColumn
vpTrafProfDstHiPort = _VpTrafProfDstHiPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 10),
    _VpTrafProfDstHiPort_Type()
)
vpTrafProfDstHiPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfDstHiPort.setStatus("mandatory")
_VpTrafProfDstLoPort_Type = Integer32
_VpTrafProfDstLoPort_Object = MibTableColumn
vpTrafProfDstLoPort = _VpTrafProfDstLoPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 11),
    _VpTrafProfDstLoPort_Type()
)
vpTrafProfDstLoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfDstLoPort.setStatus("mandatory")


class _VpTrafProfRcvTosByteMask_Type(OctetString):
    """Custom type vpTrafProfRcvTosByteMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VpTrafProfRcvTosByteMask_Type.__name__ = "OctetString"
_VpTrafProfRcvTosByteMask_Object = MibTableColumn
vpTrafProfRcvTosByteMask = _VpTrafProfRcvTosByteMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 12),
    _VpTrafProfRcvTosByteMask_Type()
)
vpTrafProfRcvTosByteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfRcvTosByteMask.setStatus("mandatory")


class _VpTrafProfRcvTosByteMatch_Type(OctetString):
    """Custom type vpTrafProfRcvTosByteMatch based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VpTrafProfRcvTosByteMatch_Type.__name__ = "OctetString"
_VpTrafProfRcvTosByteMatch_Object = MibTableColumn
vpTrafProfRcvTosByteMatch = _VpTrafProfRcvTosByteMatch_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 13),
    _VpTrafProfRcvTosByteMatch_Type()
)
vpTrafProfRcvTosByteMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfRcvTosByteMatch.setStatus("mandatory")


class _VpTrafProfLocIdType_Type(Integer32):
    """Custom type vpTrafProfLocIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9,
              10,
              11,
              99)
        )
    )
    namedValues = NamedValues(
        *(("any", 99),
          ("dn", 9),
          ("fqdn", 2),
          ("gn", 10),
          ("ipV4Addr", 1),
          ("keyId", 11),
          ("userFqdn", 3))
    )


_VpTrafProfLocIdType_Type.__name__ = "Integer32"
_VpTrafProfLocIdType_Object = MibTableColumn
vpTrafProfLocIdType = _VpTrafProfLocIdType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 14),
    _VpTrafProfLocIdType_Type()
)
vpTrafProfLocIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfLocIdType.setStatus("mandatory")
_VpTrafProfLocIdValue_Type = DisplayString
_VpTrafProfLocIdValue_Object = MibTableColumn
vpTrafProfLocIdValue = _VpTrafProfLocIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 15),
    _VpTrafProfLocIdValue_Type()
)
vpTrafProfLocIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfLocIdValue.setStatus("mandatory")
_VpTrafProfRemGroup_Type = DisplayString
_VpTrafProfRemGroup_Object = MibTableColumn
vpTrafProfRemGroup = _VpTrafProfRemGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 1, 1, 16),
    _VpTrafProfRemGroup_Type()
)
vpTrafProfRemGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafProfRemGroup.setStatus("mandatory")
_VpTrafficIfTable_Object = MibTable
vpTrafficIfTable = _VpTrafficIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 2)
)
if mibBuilder.loadTexts:
    vpTrafficIfTable.setStatus("mandatory")
_VpTrafficIfEntry_Object = MibTableRow
vpTrafficIfEntry = _VpTrafficIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 2, 1)
)
vpTrafficIfEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpTrafProfName"),
    (0, "VPNPOLICY-MIB", "vpTrafIfIndex"),
)
if mibBuilder.loadTexts:
    vpTrafficIfEntry.setStatus("mandatory")
_VpTrafIfIndex_Type = Integer32
_VpTrafIfIndex_Object = MibTableColumn
vpTrafIfIndex = _VpTrafIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 2, 1, 1),
    _VpTrafIfIndex_Type()
)
vpTrafIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafIfIndex.setStatus("mandatory")
_VpTrafIfInAddr_Type = VpIpAddress
_VpTrafIfInAddr_Object = MibTableColumn
vpTrafIfInAddr = _VpTrafIfInAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 2, 1, 2),
    _VpTrafIfInAddr_Type()
)
vpTrafIfInAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafIfInAddr.setStatus("mandatory")
_VpTrafIfOutAddr_Type = VpIpAddress
_VpTrafIfOutAddr_Object = MibTableColumn
vpTrafIfOutAddr = _VpTrafIfOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 2, 1, 3),
    _VpTrafIfOutAddr_Type()
)
vpTrafIfOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafIfOutAddr.setStatus("mandatory")
_VpTrafficRemIdTable_Object = MibTable
vpTrafficRemIdTable = _VpTrafficRemIdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 3)
)
if mibBuilder.loadTexts:
    vpTrafficRemIdTable.setStatus("mandatory")
_VpTrafficRemIdEntry_Object = MibTableRow
vpTrafficRemIdEntry = _VpTrafficRemIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 3, 1)
)
vpTrafficRemIdEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpTrafProfRemGroup"),
    (0, "VPNPOLICY-MIB", "vpTrafRemIdIndex"),
)
if mibBuilder.loadTexts:
    vpTrafficRemIdEntry.setStatus("mandatory")
_VpTrafRemIdIndex_Type = Integer32
_VpTrafRemIdIndex_Object = MibTableColumn
vpTrafRemIdIndex = _VpTrafRemIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 3, 1, 1),
    _VpTrafRemIdIndex_Type()
)
vpTrafRemIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafRemIdIndex.setStatus("mandatory")


class _VpTrafRemIdType_Type(Integer32):
    """Custom type vpTrafRemIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("dn", 9),
          ("fqdn", 2),
          ("gn", 10),
          ("ipV4Addr", 1),
          ("keyId", 11),
          ("userFqdn", 3))
    )


_VpTrafRemIdType_Type.__name__ = "Integer32"
_VpTrafRemIdType_Object = MibTableColumn
vpTrafRemIdType = _VpTrafRemIdType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 3, 1, 2),
    _VpTrafRemIdType_Type()
)
vpTrafRemIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafRemIdType.setStatus("mandatory")
_VpTrafRemIdValue_Type = DisplayString
_VpTrafRemIdValue_Object = MibTableColumn
vpTrafRemIdValue = _VpTrafRemIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 3, 1, 3),
    _VpTrafRemIdValue_Type()
)
vpTrafRemIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafRemIdValue.setStatus("mandatory")


class _VpTrafRemIdAuthMode_Type(Integer32):
    """Custom type vpTrafRemIdAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cert", 2),
          ("preShareKey", 1))
    )


_VpTrafRemIdAuthMode_Type.__name__ = "Integer32"
_VpTrafRemIdAuthMode_Object = MibTableColumn
vpTrafRemIdAuthMode = _VpTrafRemIdAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 1, 3, 1, 4),
    _VpTrafRemIdAuthMode_Type()
)
vpTrafRemIdAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTrafRemIdAuthMode.setStatus("mandatory")
_VpValidityPeriod_ObjectIdentity = ObjectIdentity
vpValidityPeriod = _VpValidityPeriod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 2)
)
_VpValidityPeriodTable_Object = MibTable
vpValidityPeriodTable = _VpValidityPeriodTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vpValidityPeriodTable.setStatus("mandatory")
_VpValidityPeriodEntry_Object = MibTableRow
vpValidityPeriodEntry = _VpValidityPeriodEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 2, 1, 1)
)
vpValidityPeriodEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpValPrdName"),
)
if mibBuilder.loadTexts:
    vpValidityPeriodEntry.setStatus("mandatory")
_VpValPrdName_Type = DisplayString
_VpValPrdName_Object = MibTableColumn
vpValPrdName = _VpValPrdName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 2, 1, 1, 1),
    _VpValPrdName_Type()
)
vpValPrdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpValPrdName.setStatus("mandatory")


class _VpValPrdStartTime_Type(OctetString):
    """Custom type vpValPrdStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_VpValPrdStartTime_Type.__name__ = "OctetString"
_VpValPrdStartTime_Object = MibTableColumn
vpValPrdStartTime = _VpValPrdStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 2, 1, 1, 2),
    _VpValPrdStartTime_Type()
)
vpValPrdStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpValPrdStartTime.setStatus("mandatory")


class _VpValPrdEndTime_Type(OctetString):
    """Custom type vpValPrdEndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_VpValPrdEndTime_Type.__name__ = "OctetString"
_VpValPrdEndTime_Object = MibTableColumn
vpValPrdEndTime = _VpValPrdEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 2, 1, 1, 3),
    _VpValPrdEndTime_Type()
)
vpValPrdEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpValPrdEndTime.setStatus("mandatory")


class _VpValPrdMonthMask_Type(OctetString):
    """Custom type vpValPrdMonthMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VpValPrdMonthMask_Type.__name__ = "OctetString"
_VpValPrdMonthMask_Object = MibTableColumn
vpValPrdMonthMask = _VpValPrdMonthMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 2, 1, 1, 4),
    _VpValPrdMonthMask_Type()
)
vpValPrdMonthMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpValPrdMonthMask.setStatus("mandatory")


class _VpValPrdDaysMask_Type(OctetString):
    """Custom type vpValPrdDaysMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VpValPrdDaysMask_Type.__name__ = "OctetString"
_VpValPrdDaysMask_Object = MibTableColumn
vpValPrdDaysMask = _VpValPrdDaysMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 2, 1, 1, 5),
    _VpValPrdDaysMask_Type()
)
vpValPrdDaysMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpValPrdDaysMask.setStatus("mandatory")


class _VpValPrdStartTod_Type(OctetString):
    """Custom type vpValPrdStartTod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_VpValPrdStartTod_Type.__name__ = "OctetString"
_VpValPrdStartTod_Object = MibTableColumn
vpValPrdStartTod = _VpValPrdStartTod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 2, 1, 1, 6),
    _VpValPrdStartTod_Type()
)
vpValPrdStartTod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpValPrdStartTod.setStatus("mandatory")


class _VpValPrdStopTod_Type(OctetString):
    """Custom type vpValPrdStopTod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_VpValPrdStopTod_Type.__name__ = "OctetString"
_VpValPrdStopTod_Object = MibTableColumn
vpValPrdStopTod = _VpValPrdStopTod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 3, 2, 1, 1, 7),
    _VpValPrdStopTod_Type()
)
vpValPrdStopTod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpValPrdStopTod.setStatus("mandatory")
_VpActions_ObjectIdentity = ObjectIdentity
vpActions = _VpActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4)
)
_VpRsvpAction_ObjectIdentity = ObjectIdentity
vpRsvpAction = _VpRsvpAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 1)
)
_VpRsvpActionTable_Object = MibTable
vpRsvpActionTable = _VpRsvpActionTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 1, 1)
)
if mibBuilder.loadTexts:
    vpRsvpActionTable.setStatus("mandatory")
_VpRsvpActionEntry_Object = MibTableRow
vpRsvpActionEntry = _VpRsvpActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 1, 1, 1)
)
vpRsvpActionEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpRsvpActName"),
)
if mibBuilder.loadTexts:
    vpRsvpActionEntry.setStatus("mandatory")
_VpRsvpActName_Type = DisplayString
_VpRsvpActName_Object = MibTableColumn
vpRsvpActName = _VpRsvpActName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 1, 1, 1, 1),
    _VpRsvpActName_Type()
)
vpRsvpActName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpRsvpActName.setStatus("mandatory")


class _VpRsvpActPermission_Type(Integer32):
    """Custom type vpRsvpActPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_VpRsvpActPermission_Type.__name__ = "Integer32"
_VpRsvpActPermission_Object = MibTableColumn
vpRsvpActPermission = _VpRsvpActPermission_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 1, 1, 1, 2),
    _VpRsvpActPermission_Type()
)
vpRsvpActPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpRsvpActPermission.setStatus("mandatory")
_VpRsvpActMaxRatePerFlow_Type = Integer32
_VpRsvpActMaxRatePerFlow_Object = MibTableColumn
vpRsvpActMaxRatePerFlow = _VpRsvpActMaxRatePerFlow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 1, 1, 1, 3),
    _VpRsvpActMaxRatePerFlow_Type()
)
vpRsvpActMaxRatePerFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpRsvpActMaxRatePerFlow.setStatus("mandatory")
_VpRsvpActMaxTokenBucketPerFlow_Type = Integer32
_VpRsvpActMaxTokenBucketPerFlow_Object = MibTableColumn
vpRsvpActMaxTokenBucketPerFlow = _VpRsvpActMaxTokenBucketPerFlow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 1, 1, 1, 4),
    _VpRsvpActMaxTokenBucketPerFlow_Type()
)
vpRsvpActMaxTokenBucketPerFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpRsvpActMaxTokenBucketPerFlow.setStatus("mandatory")
_VpRsvpActMaxFlowDuration_Type = Integer32
_VpRsvpActMaxFlowDuration_Object = MibTableColumn
vpRsvpActMaxFlowDuration = _VpRsvpActMaxFlowDuration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 1, 1, 1, 5),
    _VpRsvpActMaxFlowDuration_Type()
)
vpRsvpActMaxFlowDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpRsvpActMaxFlowDuration.setStatus("mandatory")
_VpRsvpActMinDelay_Type = Integer32
_VpRsvpActMinDelay_Object = MibTableColumn
vpRsvpActMinDelay = _VpRsvpActMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 1, 1, 1, 6),
    _VpRsvpActMinDelay_Type()
)
vpRsvpActMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpRsvpActMinDelay.setStatus("mandatory")
_VpRsvpActDiffSvrRef_Type = DisplayString
_VpRsvpActDiffSvrRef_Object = MibTableColumn
vpRsvpActDiffSvrRef = _VpRsvpActDiffSvrRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 1, 1, 1, 7),
    _VpRsvpActDiffSvrRef_Type()
)
vpRsvpActDiffSvrRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpRsvpActDiffSvrRef.setStatus("mandatory")
_VpRsvpActMatches_Type = Counter32
_VpRsvpActMatches_Object = MibTableColumn
vpRsvpActMatches = _VpRsvpActMatches_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 1, 1, 1, 8),
    _VpRsvpActMatches_Type()
)
vpRsvpActMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpRsvpActMatches.setStatus("mandatory")
_VpDiffServAction_ObjectIdentity = ObjectIdentity
vpDiffServAction = _VpDiffServAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 2)
)
_VpDiffServActionTable_Object = MibTable
vpDiffServActionTable = _VpDiffServActionTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vpDiffServActionTable.setStatus("mandatory")
_VpDiffServActionEntry_Object = MibTableRow
vpDiffServActionEntry = _VpDiffServActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 2, 1, 1)
)
vpDiffServActionEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpDifSrvActName"),
)
if mibBuilder.loadTexts:
    vpDiffServActionEntry.setStatus("mandatory")
_VpDifSrvActName_Type = DisplayString
_VpDifSrvActName_Object = MibTableColumn
vpDifSrvActName = _VpDifSrvActName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 2, 1, 1, 1),
    _VpDifSrvActName_Type()
)
vpDifSrvActName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpDifSrvActName.setStatus("mandatory")


class _VpDifSrvActPermission_Type(Integer32):
    """Custom type vpDifSrvActPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_VpDifSrvActPermission_Type.__name__ = "Integer32"
_VpDifSrvActPermission_Object = MibTableColumn
vpDifSrvActPermission = _VpDifSrvActPermission_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 2, 1, 1, 2),
    _VpDifSrvActPermission_Type()
)
vpDifSrvActPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpDifSrvActPermission.setStatus("mandatory")


class _VpDifSrvActQuePriority_Type(Integer32):
    """Custom type vpDifSrvActQuePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 2),
          ("premium", 1))
    )


_VpDifSrvActQuePriority_Type.__name__ = "Integer32"
_VpDifSrvActQuePriority_Object = MibTableColumn
vpDifSrvActQuePriority = _VpDifSrvActQuePriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 2, 1, 1, 3),
    _VpDifSrvActQuePriority_Type()
)
vpDifSrvActQuePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpDifSrvActQuePriority.setStatus("mandatory")


class _VpDifSrvActBwType_Type(Integer32):
    """Custom type vpDifSrvActBwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("percent", 2))
    )


_VpDifSrvActBwType_Type.__name__ = "Integer32"
_VpDifSrvActBwType_Object = MibTableColumn
vpDifSrvActBwType = _VpDifSrvActBwType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 2, 1, 1, 4),
    _VpDifSrvActBwType_Type()
)
vpDifSrvActBwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpDifSrvActBwType.setStatus("mandatory")
_VpDifSrvActBwShare_Type = Integer32
_VpDifSrvActBwShare_Object = MibTableColumn
vpDifSrvActBwShare = _VpDifSrvActBwShare_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 2, 1, 1, 5),
    _VpDifSrvActBwShare_Type()
)
vpDifSrvActBwShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpDifSrvActBwShare.setStatus("mandatory")


class _VpDifSrvActTransTosByteMask_Type(OctetString):
    """Custom type vpDifSrvActTransTosByteMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VpDifSrvActTransTosByteMask_Type.__name__ = "OctetString"
_VpDifSrvActTransTosByteMask_Object = MibTableColumn
vpDifSrvActTransTosByteMask = _VpDifSrvActTransTosByteMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 2, 1, 1, 6),
    _VpDifSrvActTransTosByteMask_Type()
)
vpDifSrvActTransTosByteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpDifSrvActTransTosByteMask.setStatus("mandatory")


class _VpDifSrvActTransTosByteMatch_Type(OctetString):
    """Custom type vpDifSrvActTransTosByteMatch based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VpDifSrvActTransTosByteMatch_Type.__name__ = "OctetString"
_VpDifSrvActTransTosByteMatch_Object = MibTableColumn
vpDifSrvActTransTosByteMatch = _VpDifSrvActTransTosByteMatch_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 2, 1, 1, 7),
    _VpDifSrvActTransTosByteMatch_Type()
)
vpDifSrvActTransTosByteMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpDifSrvActTransTosByteMatch.setStatus("mandatory")
_VpDifSrvActMatches_Type = Counter32
_VpDifSrvActMatches_Object = MibTableColumn
vpDifSrvActMatches = _VpDifSrvActMatches_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 2, 1, 1, 8),
    _VpDifSrvActMatches_Type()
)
vpDifSrvActMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpDifSrvActMatches.setStatus("mandatory")
_VpIsakmpAction_ObjectIdentity = ObjectIdentity
vpIsakmpAction = _VpIsakmpAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3)
)
_VpIsakmpActionTable_Object = MibTable
vpIsakmpActionTable = _VpIsakmpActionTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 1)
)
if mibBuilder.loadTexts:
    vpIsakmpActionTable.setStatus("mandatory")
_VpIsakmpActionEntry_Object = MibTableRow
vpIsakmpActionEntry = _VpIsakmpActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 1, 1)
)
vpIsakmpActionEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpIkActName"),
)
if mibBuilder.loadTexts:
    vpIsakmpActionEntry.setStatus("mandatory")
_VpIkActName_Type = DisplayString
_VpIkActName_Object = MibTableColumn
vpIkActName = _VpIkActName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 1, 1, 1),
    _VpIkActName_Type()
)
vpIkActName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkActName.setStatus("mandatory")


class _VpIkActExchangeMode_Type(Integer32):
    """Custom type vpIkActExchangeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("main", 1))
    )


_VpIkActExchangeMode_Type.__name__ = "Integer32"
_VpIkActExchangeMode_Object = MibTableColumn
vpIkActExchangeMode = _VpIkActExchangeMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 1, 1, 2),
    _VpIkActExchangeMode_Type()
)
vpIkActExchangeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkActExchangeMode.setStatus("mandatory")
_VpIkActConnSaLifeTime_Type = Integer32
_VpIkActConnSaLifeTime_Object = MibTableColumn
vpIkActConnSaLifeTime = _VpIkActConnSaLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 1, 1, 3),
    _VpIkActConnSaLifeTime_Type()
)
vpIkActConnSaLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkActConnSaLifeTime.setStatus("mandatory")
_VpIkActConnSaLifeSize_Type = Integer32
_VpIkActConnSaLifeSize_Object = MibTableColumn
vpIkActConnSaLifeSize = _VpIkActConnSaLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 1, 1, 4),
    _VpIkActConnSaLifeSize_Type()
)
vpIkActConnSaLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkActConnSaLifeSize.setStatus("mandatory")


class _VpIkActPolicyRole_Type(Integer32):
    """Custom type vpIkActPolicyRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initAndResp", 3),
          ("initiator", 1),
          ("responder", 2))
    )


_VpIkActPolicyRole_Type.__name__ = "Integer32"
_VpIkActPolicyRole_Object = MibTableColumn
vpIkActPolicyRole = _VpIkActPolicyRole_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 1, 1, 5),
    _VpIkActPolicyRole_Type()
)
vpIkActPolicyRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkActPolicyRole.setStatus("mandatory")


class _VpIkActMinPercentRefresh_Type(Integer32):
    """Custom type vpIkActMinPercentRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VpIkActMinPercentRefresh_Type.__name__ = "Integer32"
_VpIkActMinPercentRefresh_Object = MibTableColumn
vpIkActMinPercentRefresh = _VpIkActMinPercentRefresh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 1, 1, 6),
    _VpIkActMinPercentRefresh_Type()
)
vpIkActMinPercentRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkActMinPercentRefresh.setStatus("mandatory")


class _VpIkActAutoStart_Type(Integer32):
    """Custom type vpIkActAutoStart based on Integer32"""
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


_VpIkActAutoStart_Type.__name__ = "Integer32"
_VpIkActAutoStart_Object = MibTableColumn
vpIkActAutoStart = _VpIkActAutoStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 1, 1, 7),
    _VpIkActAutoStart_Type()
)
vpIkActAutoStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkActAutoStart.setStatus("mandatory")
_VpIkActMatches_Type = Counter32
_VpIkActMatches_Object = MibTableColumn
vpIkActMatches = _VpIkActMatches_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 1, 1, 8),
    _VpIkActMatches_Type()
)
vpIkActMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkActMatches.setStatus("mandatory")
_VpIsakmpProposalTable_Object = MibTable
vpIsakmpProposalTable = _VpIsakmpProposalTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 2)
)
if mibBuilder.loadTexts:
    vpIsakmpProposalTable.setStatus("mandatory")
_VpIsakmpProposalEntry_Object = MibTableRow
vpIsakmpProposalEntry = _VpIsakmpProposalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 2, 1)
)
vpIsakmpProposalEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpIkPropName"),
)
if mibBuilder.loadTexts:
    vpIsakmpProposalEntry.setStatus("mandatory")
_VpIkPropName_Type = DisplayString
_VpIkPropName_Object = MibTableColumn
vpIkPropName = _VpIkPropName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 2, 1, 1),
    _VpIkPropName_Type()
)
vpIkPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkPropName.setStatus("mandatory")


class _VpIkPropAuthMethod_Type(Integer32):
    """Custom type vpIkPropAuthMethod based on Integer32"""
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
        *(("dssSig", 2),
          ("preShardKey", 1),
          ("revRsaEncrypt", 5),
          ("rsaEncrypt", 4),
          ("rsaSig", 3))
    )


_VpIkPropAuthMethod_Type.__name__ = "Integer32"
_VpIkPropAuthMethod_Object = MibTableColumn
vpIkPropAuthMethod = _VpIkPropAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 2, 1, 2),
    _VpIkPropAuthMethod_Type()
)
vpIkPropAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkPropAuthMethod.setStatus("mandatory")


class _VpIkPropHashAlgo_Type(Integer32):
    """Custom type vpIkPropHashAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_VpIkPropHashAlgo_Type.__name__ = "Integer32"
_VpIkPropHashAlgo_Object = MibTableColumn
vpIkPropHashAlgo = _VpIkPropHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 2, 1, 3),
    _VpIkPropHashAlgo_Type()
)
vpIkPropHashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkPropHashAlgo.setStatus("mandatory")


class _VpIkPropCipherAlgo_Type(Integer32):
    """Custom type vpIkPropCipherAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("des", 1),
          ("des3", 2))
    )


_VpIkPropCipherAlgo_Type.__name__ = "Integer32"
_VpIkPropCipherAlgo_Object = MibTableColumn
vpIkPropCipherAlgo = _VpIkPropCipherAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 2, 1, 4),
    _VpIkPropCipherAlgo_Type()
)
vpIkPropCipherAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkPropCipherAlgo.setStatus("mandatory")


class _VpIkPropDiffHellmanGrpId_Type(Integer32):
    """Custom type vpIkPropDiffHellmanGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhGrp1", 1),
          ("dhGrp2", 2))
    )


_VpIkPropDiffHellmanGrpId_Type.__name__ = "Integer32"
_VpIkPropDiffHellmanGrpId_Object = MibTableColumn
vpIkPropDiffHellmanGrpId = _VpIkPropDiffHellmanGrpId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 2, 1, 5),
    _VpIkPropDiffHellmanGrpId_Type()
)
vpIkPropDiffHellmanGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkPropDiffHellmanGrpId.setStatus("mandatory")
_VpIkPropSaLifeTime_Type = Integer32
_VpIkPropSaLifeTime_Object = MibTableColumn
vpIkPropSaLifeTime = _VpIkPropSaLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 2, 1, 6),
    _VpIkPropSaLifeTime_Type()
)
vpIkPropSaLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkPropSaLifeTime.setStatus("mandatory")
_VpIkPropSaLifeSize_Type = Integer32
_VpIkPropSaLifeSize_Object = MibTableColumn
vpIkPropSaLifeSize = _VpIkPropSaLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 2, 1, 7),
    _VpIkPropSaLifeSize_Type()
)
vpIkPropSaLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkPropSaLifeSize.setStatus("mandatory")
_VpIsakmpCorTable_Object = MibTable
vpIsakmpCorTable = _VpIsakmpCorTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 3)
)
if mibBuilder.loadTexts:
    vpIsakmpCorTable.setStatus("mandatory")
_VpIsakmpCorEntry_Object = MibTableRow
vpIsakmpCorEntry = _VpIsakmpCorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 3, 1)
)
vpIsakmpCorEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpIkActName"),
    (0, "VPNPOLICY-MIB", "vpIkCorPropOrder"),
)
if mibBuilder.loadTexts:
    vpIsakmpCorEntry.setStatus("mandatory")
_VpIkCorPropOrder_Type = Integer32
_VpIkCorPropOrder_Object = MibTableColumn
vpIkCorPropOrder = _VpIkCorPropOrder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 3, 1, 1),
    _VpIkCorPropOrder_Type()
)
vpIkCorPropOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkCorPropOrder.setStatus("mandatory")
_VpIkCorPropName_Type = DisplayString
_VpIkCorPropName_Object = MibTableColumn
vpIkCorPropName = _VpIkCorPropName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 3, 1, 2),
    _VpIkCorPropName_Type()
)
vpIkCorPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkCorPropName.setStatus("mandatory")
_VpIsakmpActiveInstTable_Object = MibTable
vpIsakmpActiveInstTable = _VpIsakmpActiveInstTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 4)
)
if mibBuilder.loadTexts:
    vpIsakmpActiveInstTable.setStatus("mandatory")
_VpIsakmpActiveInstEntry_Object = MibTableRow
vpIsakmpActiveInstEntry = _VpIsakmpActiveInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 4, 1)
)
vpIsakmpActiveInstEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpIkActName"),
    (0, "VPNPOLICY-MIB", "vpIkActInstOrder"),
)
if mibBuilder.loadTexts:
    vpIsakmpActiveInstEntry.setStatus("mandatory")
_VpIkActInstOrder_Type = Integer32
_VpIkActInstOrder_Object = MibTableColumn
vpIkActInstOrder = _VpIkActInstOrder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 4, 1, 1),
    _VpIkActInstOrder_Type()
)
vpIkActInstOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkActInstOrder.setStatus("mandatory")
_VpIkActInstTunnelId_Type = OctetString
_VpIkActInstTunnelId_Object = MibTableColumn
vpIkActInstTunnelId = _VpIkActInstTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 4, 1, 2),
    _VpIkActInstTunnelId_Type()
)
vpIkActInstTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkActInstTunnelId.setStatus("mandatory")
_VpIkActInstTunnelIndex_Type = Integer32
_VpIkActInstTunnelIndex_Object = MibTableColumn
vpIkActInstTunnelIndex = _VpIkActInstTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 3, 4, 1, 3),
    _VpIkActInstTunnelIndex_Type()
)
vpIkActInstTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpIkActInstTunnelIndex.setStatus("mandatory")
_VpSecurityAction_ObjectIdentity = ObjectIdentity
vpSecurityAction = _VpSecurityAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4)
)
_VpSecurityActionTable_Object = MibTable
vpSecurityActionTable = _VpSecurityActionTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1)
)
if mibBuilder.loadTexts:
    vpSecurityActionTable.setStatus("mandatory")
_VpSecurityActionEntry_Object = MibTableRow
vpSecurityActionEntry = _VpSecurityActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1)
)
vpSecurityActionEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpSecActName"),
)
if mibBuilder.loadTexts:
    vpSecurityActionEntry.setStatus("mandatory")
_VpSecActName_Type = DisplayString
_VpSecActName_Object = MibTableColumn
vpSecActName = _VpSecActName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 1),
    _VpSecActName_Type()
)
vpSecActName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActName.setStatus("mandatory")


class _VpSecActType_Type(Integer32):
    """Custom type vpSecActType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("permit", 1))
    )


_VpSecActType_Type.__name__ = "Integer32"
_VpSecActType_Object = MibTableColumn
vpSecActType = _VpSecActType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 2),
    _VpSecActType_Type()
)
vpSecActType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActType.setStatus("mandatory")
_VpSecActTunStartAddr_Type = VpIpAddress
_VpSecActTunStartAddr_Object = MibTableColumn
vpSecActTunStartAddr = _VpSecActTunStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 3),
    _VpSecActTunStartAddr_Type()
)
vpSecActTunStartAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActTunStartAddr.setStatus("mandatory")
_VpSecActTunEndAddr_Type = VpIpAddress
_VpSecActTunEndAddr_Object = MibTableColumn
vpSecActTunEndAddr = _VpSecActTunEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 4),
    _VpSecActTunEndAddr_Type()
)
vpSecActTunEndAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActTunEndAddr.setStatus("mandatory")


class _VpSecActLocProxyType_Type(Integer32):
    """Custom type vpSecActLocProxyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("dn", 9),
          ("fqdn", 2),
          ("gn", 10),
          ("ipV4Addr", 1),
          ("ipV4Range", 7),
          ("ipV4Subnet", 4),
          ("keyId", 11),
          ("userFqdn", 3))
    )


_VpSecActLocProxyType_Type.__name__ = "Integer32"
_VpSecActLocProxyType_Object = MibTableColumn
vpSecActLocProxyType = _VpSecActLocProxyType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 5),
    _VpSecActLocProxyType_Type()
)
vpSecActLocProxyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActLocProxyType.setStatus("mandatory")
_VpSecActLocProxyValue_Type = DisplayString
_VpSecActLocProxyValue_Object = MibTableColumn
vpSecActLocProxyValue = _VpSecActLocProxyValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 6),
    _VpSecActLocProxyValue_Type()
)
vpSecActLocProxyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActLocProxyValue.setStatus("mandatory")
_VpSecActLocProxyProtocol_Type = Integer32
_VpSecActLocProxyProtocol_Object = MibTableColumn
vpSecActLocProxyProtocol = _VpSecActLocProxyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 7),
    _VpSecActLocProxyProtocol_Type()
)
vpSecActLocProxyProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActLocProxyProtocol.setStatus("mandatory")
_VpSecActLocProxySrcPort_Type = Integer32
_VpSecActLocProxySrcPort_Object = MibTableColumn
vpSecActLocProxySrcPort = _VpSecActLocProxySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 8),
    _VpSecActLocProxySrcPort_Type()
)
vpSecActLocProxySrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActLocProxySrcPort.setStatus("mandatory")


class _VpSecActRemProxyType_Type(Integer32):
    """Custom type vpSecActRemProxyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("dn", 9),
          ("fqdn", 2),
          ("gn", 10),
          ("ipV4Addr", 1),
          ("ipV4Range", 7),
          ("ipV4Subnet", 4),
          ("keyId", 11),
          ("userFqdn", 3))
    )


_VpSecActRemProxyType_Type.__name__ = "Integer32"
_VpSecActRemProxyType_Object = MibTableColumn
vpSecActRemProxyType = _VpSecActRemProxyType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 9),
    _VpSecActRemProxyType_Type()
)
vpSecActRemProxyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActRemProxyType.setStatus("mandatory")
_VpSecActRemProxyValue_Type = DisplayString
_VpSecActRemProxyValue_Object = MibTableColumn
vpSecActRemProxyValue = _VpSecActRemProxyValue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 10),
    _VpSecActRemProxyValue_Type()
)
vpSecActRemProxyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActRemProxyValue.setStatus("mandatory")
_VpSecActRemProxyProtocol_Type = Integer32
_VpSecActRemProxyProtocol_Object = MibTableColumn
vpSecActRemProxyProtocol = _VpSecActRemProxyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 11),
    _VpSecActRemProxyProtocol_Type()
)
vpSecActRemProxyProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActRemProxyProtocol.setStatus("mandatory")
_VpSecActRemProxySrcPort_Type = Integer32
_VpSecActRemProxySrcPort_Object = MibTableColumn
vpSecActRemProxySrcPort = _VpSecActRemProxySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 12),
    _VpSecActRemProxySrcPort_Type()
)
vpSecActRemProxySrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActRemProxySrcPort.setStatus("mandatory")


class _VpSecActSaRefreshThresh_Type(Integer32):
    """Custom type vpSecActSaRefreshThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VpSecActSaRefreshThresh_Type.__name__ = "Integer32"
_VpSecActSaRefreshThresh_Object = MibTableColumn
vpSecActSaRefreshThresh = _VpSecActSaRefreshThresh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 13),
    _VpSecActSaRefreshThresh_Type()
)
vpSecActSaRefreshThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActSaRefreshThresh.setStatus("mandatory")


class _VpSecActMinPercentRefresh_Type(Integer32):
    """Custom type vpSecActMinPercentRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VpSecActMinPercentRefresh_Type.__name__ = "Integer32"
_VpSecActMinPercentRefresh_Object = MibTableColumn
vpSecActMinPercentRefresh = _VpSecActMinPercentRefresh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 14),
    _VpSecActMinPercentRefresh_Type()
)
vpSecActMinPercentRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActMinPercentRefresh.setStatus("mandatory")


class _VpSecActTunnelInTunnel_Type(Integer32):
    """Custom type vpSecActTunnelInTunnel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_VpSecActTunnelInTunnel_Type.__name__ = "Integer32"
_VpSecActTunnelInTunnel_Object = MibTableColumn
vpSecActTunnelInTunnel = _VpSecActTunnelInTunnel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 15),
    _VpSecActTunnelInTunnel_Type()
)
vpSecActTunnelInTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActTunnelInTunnel.setStatus("mandatory")


class _VpSecActAutoStart_Type(Integer32):
    """Custom type vpSecActAutoStart based on Integer32"""
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


_VpSecActAutoStart_Type.__name__ = "Integer32"
_VpSecActAutoStart_Object = MibTableColumn
vpSecActAutoStart = _VpSecActAutoStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 16),
    _VpSecActAutoStart_Type()
)
vpSecActAutoStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActAutoStart.setStatus("mandatory")


class _VpSecActDontFragBitHandling_Type(Integer32):
    """Custom type vpSecActDontFragBitHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearDfBit", 3),
          ("copyDfBit", 1),
          ("setDfBit", 2))
    )


_VpSecActDontFragBitHandling_Type.__name__ = "Integer32"
_VpSecActDontFragBitHandling_Object = MibTableColumn
vpSecActDontFragBitHandling = _VpSecActDontFragBitHandling_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 17),
    _VpSecActDontFragBitHandling_Type()
)
vpSecActDontFragBitHandling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActDontFragBitHandling.setStatus("mandatory")


class _VpSecActReplayPrevention_Type(Integer32):
    """Custom type vpSecActReplayPrevention based on Integer32"""
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


_VpSecActReplayPrevention_Type.__name__ = "Integer32"
_VpSecActReplayPrevention_Object = MibTableColumn
vpSecActReplayPrevention = _VpSecActReplayPrevention_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 18),
    _VpSecActReplayPrevention_Type()
)
vpSecActReplayPrevention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActReplayPrevention.setStatus("mandatory")
_VpSecActMatches_Type = Counter32
_VpSecActMatches_Object = MibTableColumn
vpSecActMatches = _VpSecActMatches_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 1, 1, 19),
    _VpSecActMatches_Type()
)
vpSecActMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActMatches.setStatus("mandatory")
_VpSecurityProposalTable_Object = MibTable
vpSecurityProposalTable = _VpSecurityProposalTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 2)
)
if mibBuilder.loadTexts:
    vpSecurityProposalTable.setStatus("mandatory")
_VpSecurityProposalEntry_Object = MibTableRow
vpSecurityProposalEntry = _VpSecurityProposalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 2, 1)
)
vpSecurityProposalEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpSecPropName"),
)
if mibBuilder.loadTexts:
    vpSecurityProposalEntry.setStatus("mandatory")
_VpSecPropName_Type = DisplayString
_VpSecPropName_Object = MibTableColumn
vpSecPropName = _VpSecPropName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 2, 1, 1),
    _VpSecPropName_Type()
)
vpSecPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecPropName.setStatus("mandatory")


class _VpSecPropPrfFwdSecr_Type(Integer32):
    """Custom type vpSecPropPrfFwdSecr based on Integer32"""
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


_VpSecPropPrfFwdSecr_Type.__name__ = "Integer32"
_VpSecPropPrfFwdSecr_Object = MibTableColumn
vpSecPropPrfFwdSecr = _VpSecPropPrfFwdSecr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 2, 1, 2),
    _VpSecPropPrfFwdSecr_Type()
)
vpSecPropPrfFwdSecr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecPropPrfFwdSecr.setStatus("mandatory")


class _VpSecPropDiffHellmanGrpId_Type(Integer32):
    """Custom type vpSecPropDiffHellmanGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhGrp1", 1),
          ("dhGrp2", 2))
    )


_VpSecPropDiffHellmanGrpId_Type.__name__ = "Integer32"
_VpSecPropDiffHellmanGrpId_Object = MibTableColumn
vpSecPropDiffHellmanGrpId = _VpSecPropDiffHellmanGrpId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 2, 1, 3),
    _VpSecPropDiffHellmanGrpId_Type()
)
vpSecPropDiffHellmanGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecPropDiffHellmanGrpId.setStatus("mandatory")
_VpSecurityAhTransTable_Object = MibTable
vpSecurityAhTransTable = _VpSecurityAhTransTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 3)
)
if mibBuilder.loadTexts:
    vpSecurityAhTransTable.setStatus("mandatory")
_VpSecurityAhTransEntry_Object = MibTableRow
vpSecurityAhTransEntry = _VpSecurityAhTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 3, 1)
)
vpSecurityAhTransEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpSecAhTransName"),
)
if mibBuilder.loadTexts:
    vpSecurityAhTransEntry.setStatus("mandatory")
_VpSecAhTransName_Type = DisplayString
_VpSecAhTransName_Object = MibTableColumn
vpSecAhTransName = _VpSecAhTransName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 3, 1, 1),
    _VpSecAhTransName_Type()
)
vpSecAhTransName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecAhTransName.setStatus("mandatory")


class _VpSecAhTransIntgAlgo_Type(Integer32):
    """Custom type vpSecAhTransIntgAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmacMd5", 1),
          ("hmacSha", 2))
    )


_VpSecAhTransIntgAlgo_Type.__name__ = "Integer32"
_VpSecAhTransIntgAlgo_Object = MibTableColumn
vpSecAhTransIntgAlgo = _VpSecAhTransIntgAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 3, 1, 2),
    _VpSecAhTransIntgAlgo_Type()
)
vpSecAhTransIntgAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecAhTransIntgAlgo.setStatus("mandatory")


class _VpSecAhTransEncapMode_Type(Integer32):
    """Custom type vpSecAhTransEncapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1))
    )


_VpSecAhTransEncapMode_Type.__name__ = "Integer32"
_VpSecAhTransEncapMode_Object = MibTableColumn
vpSecAhTransEncapMode = _VpSecAhTransEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 3, 1, 3),
    _VpSecAhTransEncapMode_Type()
)
vpSecAhTransEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecAhTransEncapMode.setStatus("mandatory")
_VpSecAhTransSaLifeTime_Type = Integer32
_VpSecAhTransSaLifeTime_Object = MibTableColumn
vpSecAhTransSaLifeTime = _VpSecAhTransSaLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 3, 1, 4),
    _VpSecAhTransSaLifeTime_Type()
)
vpSecAhTransSaLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecAhTransSaLifeTime.setStatus("mandatory")
_VpSecAhTransSaLifeSize_Type = Integer32
_VpSecAhTransSaLifeSize_Object = MibTableColumn
vpSecAhTransSaLifeSize = _VpSecAhTransSaLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 3, 1, 5),
    _VpSecAhTransSaLifeSize_Type()
)
vpSecAhTransSaLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecAhTransSaLifeSize.setStatus("mandatory")
_VpSecurityEspTransTable_Object = MibTable
vpSecurityEspTransTable = _VpSecurityEspTransTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 4)
)
if mibBuilder.loadTexts:
    vpSecurityEspTransTable.setStatus("mandatory")
_VpSecurityEspTransEntry_Object = MibTableRow
vpSecurityEspTransEntry = _VpSecurityEspTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 4, 1)
)
vpSecurityEspTransEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpSecEspTransName"),
)
if mibBuilder.loadTexts:
    vpSecurityEspTransEntry.setStatus("mandatory")
_VpSecEspTransName_Type = DisplayString
_VpSecEspTransName_Object = MibTableColumn
vpSecEspTransName = _VpSecEspTransName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 4, 1, 1),
    _VpSecEspTransName_Type()
)
vpSecEspTransName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecEspTransName.setStatus("mandatory")


class _VpSecEspTransEncapMode_Type(Integer32):
    """Custom type vpSecEspTransEncapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1))
    )


_VpSecEspTransEncapMode_Type.__name__ = "Integer32"
_VpSecEspTransEncapMode_Object = MibTableColumn
vpSecEspTransEncapMode = _VpSecEspTransEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 4, 1, 2),
    _VpSecEspTransEncapMode_Type()
)
vpSecEspTransEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecEspTransEncapMode.setStatus("mandatory")


class _VpSecEspTransIntgAlgo_Type(Integer32):
    """Custom type vpSecEspTransIntgAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 1),
          ("sha", 3))
    )


_VpSecEspTransIntgAlgo_Type.__name__ = "Integer32"
_VpSecEspTransIntgAlgo_Object = MibTableColumn
vpSecEspTransIntgAlgo = _VpSecEspTransIntgAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 4, 1, 3),
    _VpSecEspTransIntgAlgo_Type()
)
vpSecEspTransIntgAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecEspTransIntgAlgo.setStatus("mandatory")


class _VpSecEspTransCipherAlgo_Type(Integer32):
    """Custom type vpSecEspTransCipherAlgo based on Integer32"""
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
        *(("cdmf", 4),
          ("des", 2),
          ("des3", 3),
          ("none", 1))
    )


_VpSecEspTransCipherAlgo_Type.__name__ = "Integer32"
_VpSecEspTransCipherAlgo_Object = MibTableColumn
vpSecEspTransCipherAlgo = _VpSecEspTransCipherAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 4, 1, 4),
    _VpSecEspTransCipherAlgo_Type()
)
vpSecEspTransCipherAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecEspTransCipherAlgo.setStatus("mandatory")
_VpSecEspTransSaLifeTime_Type = Integer32
_VpSecEspTransSaLifeTime_Object = MibTableColumn
vpSecEspTransSaLifeTime = _VpSecEspTransSaLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 4, 1, 5),
    _VpSecEspTransSaLifeTime_Type()
)
vpSecEspTransSaLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecEspTransSaLifeTime.setStatus("mandatory")
_VpSecEspTransSaLifeSize_Type = Integer32
_VpSecEspTransSaLifeSize_Object = MibTableColumn
vpSecEspTransSaLifeSize = _VpSecEspTransSaLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 4, 1, 6),
    _VpSecEspTransSaLifeSize_Type()
)
vpSecEspTransSaLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecEspTransSaLifeSize.setStatus("mandatory")
_VpSecurityIpcompTransTable_Object = MibTable
vpSecurityIpcompTransTable = _VpSecurityIpcompTransTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 5)
)
if mibBuilder.loadTexts:
    vpSecurityIpcompTransTable.setStatus("mandatory")
_VpSecurityIpcompTransEntry_Object = MibTableRow
vpSecurityIpcompTransEntry = _VpSecurityIpcompTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 5, 1)
)
vpSecurityIpcompTransEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpSecIpcompTransName"),
)
if mibBuilder.loadTexts:
    vpSecurityIpcompTransEntry.setStatus("mandatory")
_VpSecIpcompTransName_Type = DisplayString
_VpSecIpcompTransName_Object = MibTableColumn
vpSecIpcompTransName = _VpSecIpcompTransName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 5, 1, 1),
    _VpSecIpcompTransName_Type()
)
vpSecIpcompTransName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecIpcompTransName.setStatus("mandatory")
_VpSecIpcompTransAlgo_Type = Integer32
_VpSecIpcompTransAlgo_Object = MibTableColumn
vpSecIpcompTransAlgo = _VpSecIpcompTransAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 5, 1, 2),
    _VpSecIpcompTransAlgo_Type()
)
vpSecIpcompTransAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecIpcompTransAlgo.setStatus("mandatory")
_VpSecIpcompTransVendAlgo_Type = Integer32
_VpSecIpcompTransVendAlgo_Object = MibTableColumn
vpSecIpcompTransVendAlgo = _VpSecIpcompTransVendAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 5, 1, 3),
    _VpSecIpcompTransVendAlgo_Type()
)
vpSecIpcompTransVendAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecIpcompTransVendAlgo.setStatus("mandatory")
_VpSecIpcompTransSaLifeTime_Type = Integer32
_VpSecIpcompTransSaLifeTime_Object = MibTableColumn
vpSecIpcompTransSaLifeTime = _VpSecIpcompTransSaLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 5, 1, 4),
    _VpSecIpcompTransSaLifeTime_Type()
)
vpSecIpcompTransSaLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecIpcompTransSaLifeTime.setStatus("mandatory")
_VpSecIpcompTransSaLifeSize_Type = Integer32
_VpSecIpcompTransSaLifeSize_Object = MibTableColumn
vpSecIpcompTransSaLifeSize = _VpSecIpcompTransSaLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 5, 1, 5),
    _VpSecIpcompTransSaLifeSize_Type()
)
vpSecIpcompTransSaLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecIpcompTransSaLifeSize.setStatus("mandatory")
_VpSecurityPropCorTable_Object = MibTable
vpSecurityPropCorTable = _VpSecurityPropCorTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 6)
)
if mibBuilder.loadTexts:
    vpSecurityPropCorTable.setStatus("mandatory")
_VpSecurityPropCorEntry_Object = MibTableRow
vpSecurityPropCorEntry = _VpSecurityPropCorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 6, 1)
)
vpSecurityPropCorEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpSecActName"),
    (0, "VPNPOLICY-MIB", "vpSecCorPropOrder"),
)
if mibBuilder.loadTexts:
    vpSecurityPropCorEntry.setStatus("mandatory")
_VpSecCorPropOrder_Type = Integer32
_VpSecCorPropOrder_Object = MibTableColumn
vpSecCorPropOrder = _VpSecCorPropOrder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 6, 1, 1),
    _VpSecCorPropOrder_Type()
)
vpSecCorPropOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecCorPropOrder.setStatus("mandatory")
_VpSecCorPropRef_Type = DisplayString
_VpSecCorPropRef_Object = MibTableColumn
vpSecCorPropRef = _VpSecCorPropRef_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 6, 1, 2),
    _VpSecCorPropRef_Type()
)
vpSecCorPropRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecCorPropRef.setStatus("mandatory")
_VpSecurityAhCorTable_Object = MibTable
vpSecurityAhCorTable = _VpSecurityAhCorTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 7)
)
if mibBuilder.loadTexts:
    vpSecurityAhCorTable.setStatus("mandatory")
_VpSecurityAhCorEntry_Object = MibTableRow
vpSecurityAhCorEntry = _VpSecurityAhCorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 7, 1)
)
vpSecurityAhCorEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpSecPropName"),
    (0, "VPNPOLICY-MIB", "vpSecAhTransCorOrder"),
)
if mibBuilder.loadTexts:
    vpSecurityAhCorEntry.setStatus("mandatory")
_VpSecAhTransCorOrder_Type = Integer32
_VpSecAhTransCorOrder_Object = MibTableColumn
vpSecAhTransCorOrder = _VpSecAhTransCorOrder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 7, 1, 1),
    _VpSecAhTransCorOrder_Type()
)
vpSecAhTransCorOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecAhTransCorOrder.setStatus("mandatory")
_VpSecAhTransCorName_Type = DisplayString
_VpSecAhTransCorName_Object = MibTableColumn
vpSecAhTransCorName = _VpSecAhTransCorName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 7, 1, 2),
    _VpSecAhTransCorName_Type()
)
vpSecAhTransCorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecAhTransCorName.setStatus("mandatory")
_VpSecurityEspCorTable_Object = MibTable
vpSecurityEspCorTable = _VpSecurityEspCorTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 8)
)
if mibBuilder.loadTexts:
    vpSecurityEspCorTable.setStatus("mandatory")
_VpSecurityEspCorEntry_Object = MibTableRow
vpSecurityEspCorEntry = _VpSecurityEspCorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 8, 1)
)
vpSecurityEspCorEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpSecPropName"),
    (0, "VPNPOLICY-MIB", "vpSecEspTransCorOrder"),
)
if mibBuilder.loadTexts:
    vpSecurityEspCorEntry.setStatus("mandatory")
_VpSecEspTransCorOrder_Type = Integer32
_VpSecEspTransCorOrder_Object = MibTableColumn
vpSecEspTransCorOrder = _VpSecEspTransCorOrder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 8, 1, 1),
    _VpSecEspTransCorOrder_Type()
)
vpSecEspTransCorOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecEspTransCorOrder.setStatus("mandatory")
_VpSecEspTransCorName_Type = DisplayString
_VpSecEspTransCorName_Object = MibTableColumn
vpSecEspTransCorName = _VpSecEspTransCorName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 8, 1, 2),
    _VpSecEspTransCorName_Type()
)
vpSecEspTransCorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecEspTransCorName.setStatus("mandatory")
_VpSecurityIpcompCorTable_Object = MibTable
vpSecurityIpcompCorTable = _VpSecurityIpcompCorTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 9)
)
if mibBuilder.loadTexts:
    vpSecurityIpcompCorTable.setStatus("mandatory")
_VpSecurityIpcompCorEntry_Object = MibTableRow
vpSecurityIpcompCorEntry = _VpSecurityIpcompCorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 9, 1)
)
vpSecurityIpcompCorEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpSecPropName"),
    (0, "VPNPOLICY-MIB", "vpSecIpcompTransCorOrder"),
)
if mibBuilder.loadTexts:
    vpSecurityIpcompCorEntry.setStatus("mandatory")
_VpSecIpcompTransCorOrder_Type = Integer32
_VpSecIpcompTransCorOrder_Object = MibTableColumn
vpSecIpcompTransCorOrder = _VpSecIpcompTransCorOrder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 9, 1, 1),
    _VpSecIpcompTransCorOrder_Type()
)
vpSecIpcompTransCorOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecIpcompTransCorOrder.setStatus("mandatory")
_VpSecIpcompTransCorName_Type = DisplayString
_VpSecIpcompTransCorName_Object = MibTableColumn
vpSecIpcompTransCorName = _VpSecIpcompTransCorName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 9, 1, 2),
    _VpSecIpcompTransCorName_Type()
)
vpSecIpcompTransCorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecIpcompTransCorName.setStatus("mandatory")
_VpSecurityActiveInstTable_Object = MibTable
vpSecurityActiveInstTable = _VpSecurityActiveInstTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 10)
)
if mibBuilder.loadTexts:
    vpSecurityActiveInstTable.setStatus("mandatory")
_VpSecurityActiveInstEntry_Object = MibTableRow
vpSecurityActiveInstEntry = _VpSecurityActiveInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 10, 1)
)
vpSecurityActiveInstEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpSecActName"),
    (0, "VPNPOLICY-MIB", "vpSecActInstOrder"),
)
if mibBuilder.loadTexts:
    vpSecurityActiveInstEntry.setStatus("mandatory")
_VpSecActInstOrder_Type = Integer32
_VpSecActInstOrder_Object = MibTableColumn
vpSecActInstOrder = _VpSecActInstOrder_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 10, 1, 1),
    _VpSecActInstOrder_Type()
)
vpSecActInstOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActInstOrder.setStatus("mandatory")
_VpSecActInstTunnelId_Type = Integer32
_VpSecActInstTunnelId_Object = MibTableColumn
vpSecActInstTunnelId = _VpSecActInstTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 10, 1, 2),
    _VpSecActInstTunnelId_Type()
)
vpSecActInstTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActInstTunnelId.setStatus("mandatory")
_VpSecActInstTunnelIndex_Type = Integer32
_VpSecActInstTunnelIndex_Object = MibTableColumn
vpSecActInstTunnelIndex = _VpSecActInstTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 4, 4, 10, 1, 3),
    _VpSecActInstTunnelIndex_Type()
)
vpSecActInstTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpSecActInstTunnelIndex.setStatus("mandatory")
_VpTests_ObjectIdentity = ObjectIdentity
vpTests = _VpTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5)
)
_VpTestPolicyTable_Object = MibTable
vpTestPolicyTable = _VpTestPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1)
)
if mibBuilder.loadTexts:
    vpTestPolicyTable.setStatus("mandatory")
_VpTestPolicyEntry_Object = MibTableRow
vpTestPolicyEntry = _VpTestPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1)
)
vpTestPolicyEntry.setIndexNames(
    (0, "VPNPOLICY-MIB", "vpTestPolIndex"),
)
if mibBuilder.loadTexts:
    vpTestPolicyEntry.setStatus("mandatory")
_VpTestPolIndex_Type = Integer32
_VpTestPolIndex_Object = MibTableColumn
vpTestPolIndex = _VpTestPolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 1),
    _VpTestPolIndex_Type()
)
vpTestPolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTestPolIndex.setStatus("mandatory")
_VpTestPolSrcAddr_Type = VpIpAddress
_VpTestPolSrcAddr_Object = MibTableColumn
vpTestPolSrcAddr = _VpTestPolSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 2),
    _VpTestPolSrcAddr_Type()
)
vpTestPolSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpTestPolSrcAddr.setStatus("mandatory")
_VpTestPolSrcPort_Type = Integer32
_VpTestPolSrcPort_Object = MibTableColumn
vpTestPolSrcPort = _VpTestPolSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 3),
    _VpTestPolSrcPort_Type()
)
vpTestPolSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpTestPolSrcPort.setStatus("mandatory")
_VpTestPolDstAddr_Type = VpIpAddress
_VpTestPolDstAddr_Object = MibTableColumn
vpTestPolDstAddr = _VpTestPolDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 4),
    _VpTestPolDstAddr_Type()
)
vpTestPolDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpTestPolDstAddr.setStatus("mandatory")
_VpTestPolDstPort_Type = Integer32
_VpTestPolDstPort_Object = MibTableColumn
vpTestPolDstPort = _VpTestPolDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 5),
    _VpTestPolDstPort_Type()
)
vpTestPolDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpTestPolDstPort.setStatus("mandatory")
_VpTestPolProtocol_Type = Integer32
_VpTestPolProtocol_Object = MibTableColumn
vpTestPolProtocol = _VpTestPolProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 6),
    _VpTestPolProtocol_Type()
)
vpTestPolProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpTestPolProtocol.setStatus("mandatory")


class _VpTestPolTosByte_Type(OctetString):
    """Custom type vpTestPolTosByte based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VpTestPolTosByte_Type.__name__ = "OctetString"
_VpTestPolTosByte_Object = MibTableColumn
vpTestPolTosByte = _VpTestPolTosByte_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 7),
    _VpTestPolTosByte_Type()
)
vpTestPolTosByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpTestPolTosByte.setStatus("mandatory")
_VpTestPolIngressAddr_Type = VpIpAddress
_VpTestPolIngressAddr_Object = MibTableColumn
vpTestPolIngressAddr = _VpTestPolIngressAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 8),
    _VpTestPolIngressAddr_Type()
)
vpTestPolIngressAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpTestPolIngressAddr.setStatus("mandatory")
_VpTestPolEgressAddr_Type = VpIpAddress
_VpTestPolEgressAddr_Object = MibTableColumn
vpTestPolEgressAddr = _VpTestPolEgressAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 9),
    _VpTestPolEgressAddr_Type()
)
vpTestPolEgressAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpTestPolEgressAddr.setStatus("mandatory")


class _VpTestPolResult_Type(Integer32):
    """Custom type vpTestPolResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("noPolicyMatch", 3),
          ("successful", 2))
    )


_VpTestPolResult_Type.__name__ = "Integer32"
_VpTestPolResult_Object = MibTableColumn
vpTestPolResult = _VpTestPolResult_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 10),
    _VpTestPolResult_Type()
)
vpTestPolResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTestPolResult.setStatus("mandatory")


class _VpTestPolStatus_Type(Integer32):
    """Custom type vpTestPolStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4))
    )


_VpTestPolStatus_Type.__name__ = "Integer32"
_VpTestPolStatus_Object = MibTableColumn
vpTestPolStatus = _VpTestPolStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 11),
    _VpTestPolStatus_Type()
)
vpTestPolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpTestPolStatus.setStatus("mandatory")
_VpTestPolRsvpPolicy_Type = DisplayString
_VpTestPolRsvpPolicy_Object = MibTableColumn
vpTestPolRsvpPolicy = _VpTestPolRsvpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 12),
    _VpTestPolRsvpPolicy_Type()
)
vpTestPolRsvpPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTestPolRsvpPolicy.setStatus("mandatory")
_VpTestPolRsvpAction_Type = DisplayString
_VpTestPolRsvpAction_Object = MibTableColumn
vpTestPolRsvpAction = _VpTestPolRsvpAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 13),
    _VpTestPolRsvpAction_Type()
)
vpTestPolRsvpAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTestPolRsvpAction.setStatus("mandatory")
_VpTestPolDiffServPolicy_Type = DisplayString
_VpTestPolDiffServPolicy_Object = MibTableColumn
vpTestPolDiffServPolicy = _VpTestPolDiffServPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 14),
    _VpTestPolDiffServPolicy_Type()
)
vpTestPolDiffServPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTestPolDiffServPolicy.setStatus("mandatory")
_VpTestPolDiffServAction_Type = DisplayString
_VpTestPolDiffServAction_Object = MibTableColumn
vpTestPolDiffServAction = _VpTestPolDiffServAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 15),
    _VpTestPolDiffServAction_Type()
)
vpTestPolDiffServAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTestPolDiffServAction.setStatus("mandatory")
_VpTestPolIsakmpPolicy_Type = DisplayString
_VpTestPolIsakmpPolicy_Object = MibTableColumn
vpTestPolIsakmpPolicy = _VpTestPolIsakmpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 16),
    _VpTestPolIsakmpPolicy_Type()
)
vpTestPolIsakmpPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTestPolIsakmpPolicy.setStatus("mandatory")
_VpTestPolIsakmpAction_Type = DisplayString
_VpTestPolIsakmpAction_Object = MibTableColumn
vpTestPolIsakmpAction = _VpTestPolIsakmpAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 17),
    _VpTestPolIsakmpAction_Type()
)
vpTestPolIsakmpAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTestPolIsakmpAction.setStatus("mandatory")
_VpTestPolIPSecPolicy_Type = DisplayString
_VpTestPolIPSecPolicy_Object = MibTableColumn
vpTestPolIPSecPolicy = _VpTestPolIPSecPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 18),
    _VpTestPolIPSecPolicy_Type()
)
vpTestPolIPSecPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTestPolIPSecPolicy.setStatus("mandatory")
_VpTestPolIPSecAction_Type = DisplayString
_VpTestPolIPSecAction_Object = MibTableColumn
vpTestPolIPSecAction = _VpTestPolIPSecAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 15, 5, 1, 1, 19),
    _VpTestPolIPSecAction_Type()
)
vpTestPolIPSecAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpTestPolIPSecAction.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VPNPOLICY-MIB",
    **{"VpIpAddress": VpIpAddress,
       "ibmIROCVPNpolicy": ibmIROCVPNpolicy,
       "vpSystem": vpSystem,
       "vpSystemGlobal": vpSystemGlobal,
       "vpSysMibLevel": vpSysMibLevel,
       "vpSysUpTime": vpSysUpTime,
       "vpSysCurTime": vpSysCurTime,
       "vpSysHoursFromCut": vpSysHoursFromCut,
       "vpSysCurConfigSource": vpSysCurConfigSource,
       "vpSysRefreshConfig": vpSysRefreshConfig,
       "vpSystemLdap": vpSystemLdap,
       "vpLdapGlobal": vpLdapGlobal,
       "vpLdapGlobalOper": vpLdapGlobalOper,
       "vpLdapGblOperLdapStatus": vpLdapGblOperLdapStatus,
       "vpLdapGblOperPrimServerAddr": vpLdapGblOperPrimServerAddr,
       "vpLdapGblOperSecServerAddr": vpLdapGblOperSecServerAddr,
       "vpLdapGblOperServerLdapLvl": vpLdapGblOperServerLdapLvl,
       "vpLdapGblOperPolicyBaseName": vpLdapGblOperPolicyBaseName,
       "vpLdapGblOperPortNumber": vpLdapGblOperPortNumber,
       "vpLdapGblOperTimeOut": vpLdapGblOperTimeOut,
       "vpLdapGblOperRetryInterval": vpLdapGblOperRetryInterval,
       "vpLdapGblOperUserId": vpLdapGblOperUserId,
       "vpLdapGlobalAdmin": vpLdapGlobalAdmin,
       "vpLdapGblAdminLdapStatus": vpLdapGblAdminLdapStatus,
       "vpLdapGblAdminPrimServerAddr": vpLdapGblAdminPrimServerAddr,
       "vpLdapGblAdminSecServerAddr": vpLdapGblAdminSecServerAddr,
       "vpLdapGblAdminServerLdapLvl": vpLdapGblAdminServerLdapLvl,
       "vpLdapGblAdminPolicyBaseName": vpLdapGblAdminPolicyBaseName,
       "vpLdapGblAdminPortNumber": vpLdapGblAdminPortNumber,
       "vpLdapGblAdminTimeOut": vpLdapGblAdminTimeOut,
       "vpLdapGblAdminRetryInterval": vpLdapGblAdminRetryInterval,
       "vpLdapGblAdminUserId": vpLdapGblAdminUserId,
       "vpPolicy": vpPolicy,
       "vpPolicyTable": vpPolicyTable,
       "vpPolicyEntry": vpPolicyEntry,
       "vpPolName": vpPolName,
       "vpPolStatus": vpPolStatus,
       "vpPolPriority": vpPolPriority,
       "vpPolValidity": vpPolValidity,
       "vpPolTrafficProfileRef": vpPolTrafficProfileRef,
       "vpPolValidityPeriodRef": vpPolValidityPeriodRef,
       "vpPolRsvpActionRef": vpPolRsvpActionRef,
       "vpPolDiffServActionRef": vpPolDiffServActionRef,
       "vpPolIsakmpActionRef": vpPolIsakmpActionRef,
       "vpPolSecurityActionRef": vpPolSecurityActionRef,
       "vpPolIpsecManualTunId": vpPolIpsecManualTunId,
       "vpPolMatches": vpPolMatches,
       "vpPolicyRulePriTable": vpPolicyRulePriTable,
       "vpPolicyRulePriEntry": vpPolicyRulePriEntry,
       "vpPolRulePriOrder": vpPolRulePriOrder,
       "vpPolRulePriName": vpPolRulePriName,
       "vpPolRulePriStatus": vpPolRulePriStatus,
       "vpPolRulePriPriority": vpPolRulePriPriority,
       "vpPolRulePriTrafficProfileRef": vpPolRulePriTrafficProfileRef,
       "vpPolRulePriValidityPeriodRef": vpPolRulePriValidityPeriodRef,
       "vpPolRulePriRsvpActionRef": vpPolRulePriRsvpActionRef,
       "vpPolRulePriDiffServActionRef": vpPolRulePriDiffServActionRef,
       "vpPolRulePriIsakmpActionRef": vpPolRulePriIsakmpActionRef,
       "vpPolRulePriSecurityActionRef": vpPolRulePriSecurityActionRef,
       "vpPolRulePriIpsecManualTunId": vpPolRulePriIpsecManualTunId,
       "vpPolicyCorTable": vpPolicyCorTable,
       "vpPolicyCorEntry": vpPolicyCorEntry,
       "vpPolCorRuleOrder": vpPolCorRuleOrder,
       "vpPolCorRulePriOrder": vpPolCorRulePriOrder,
       "vpConditions": vpConditions,
       "vpTrafficProfile": vpTrafficProfile,
       "vpTrafficProfileTable": vpTrafficProfileTable,
       "vpTrafficProfileEntry": vpTrafficProfileEntry,
       "vpTrafProfName": vpTrafProfName,
       "vpTrafProfHiProtocol": vpTrafProfHiProtocol,
       "vpTrafProfLoProtocol": vpTrafProfLoProtocol,
       "vpTrafProfSrcHiAddr": vpTrafProfSrcHiAddr,
       "vpTrafProfSrcLoAddr": vpTrafProfSrcLoAddr,
       "vpTrafProfSrcHiPort": vpTrafProfSrcHiPort,
       "vpTrafProfSrcLoPort": vpTrafProfSrcLoPort,
       "vpTrafProfDstHiAddr": vpTrafProfDstHiAddr,
       "vpTrafProfDstLoAddr": vpTrafProfDstLoAddr,
       "vpTrafProfDstHiPort": vpTrafProfDstHiPort,
       "vpTrafProfDstLoPort": vpTrafProfDstLoPort,
       "vpTrafProfRcvTosByteMask": vpTrafProfRcvTosByteMask,
       "vpTrafProfRcvTosByteMatch": vpTrafProfRcvTosByteMatch,
       "vpTrafProfLocIdType": vpTrafProfLocIdType,
       "vpTrafProfLocIdValue": vpTrafProfLocIdValue,
       "vpTrafProfRemGroup": vpTrafProfRemGroup,
       "vpTrafficIfTable": vpTrafficIfTable,
       "vpTrafficIfEntry": vpTrafficIfEntry,
       "vpTrafIfIndex": vpTrafIfIndex,
       "vpTrafIfInAddr": vpTrafIfInAddr,
       "vpTrafIfOutAddr": vpTrafIfOutAddr,
       "vpTrafficRemIdTable": vpTrafficRemIdTable,
       "vpTrafficRemIdEntry": vpTrafficRemIdEntry,
       "vpTrafRemIdIndex": vpTrafRemIdIndex,
       "vpTrafRemIdType": vpTrafRemIdType,
       "vpTrafRemIdValue": vpTrafRemIdValue,
       "vpTrafRemIdAuthMode": vpTrafRemIdAuthMode,
       "vpValidityPeriod": vpValidityPeriod,
       "vpValidityPeriodTable": vpValidityPeriodTable,
       "vpValidityPeriodEntry": vpValidityPeriodEntry,
       "vpValPrdName": vpValPrdName,
       "vpValPrdStartTime": vpValPrdStartTime,
       "vpValPrdEndTime": vpValPrdEndTime,
       "vpValPrdMonthMask": vpValPrdMonthMask,
       "vpValPrdDaysMask": vpValPrdDaysMask,
       "vpValPrdStartTod": vpValPrdStartTod,
       "vpValPrdStopTod": vpValPrdStopTod,
       "vpActions": vpActions,
       "vpRsvpAction": vpRsvpAction,
       "vpRsvpActionTable": vpRsvpActionTable,
       "vpRsvpActionEntry": vpRsvpActionEntry,
       "vpRsvpActName": vpRsvpActName,
       "vpRsvpActPermission": vpRsvpActPermission,
       "vpRsvpActMaxRatePerFlow": vpRsvpActMaxRatePerFlow,
       "vpRsvpActMaxTokenBucketPerFlow": vpRsvpActMaxTokenBucketPerFlow,
       "vpRsvpActMaxFlowDuration": vpRsvpActMaxFlowDuration,
       "vpRsvpActMinDelay": vpRsvpActMinDelay,
       "vpRsvpActDiffSvrRef": vpRsvpActDiffSvrRef,
       "vpRsvpActMatches": vpRsvpActMatches,
       "vpDiffServAction": vpDiffServAction,
       "vpDiffServActionTable": vpDiffServActionTable,
       "vpDiffServActionEntry": vpDiffServActionEntry,
       "vpDifSrvActName": vpDifSrvActName,
       "vpDifSrvActPermission": vpDifSrvActPermission,
       "vpDifSrvActQuePriority": vpDifSrvActQuePriority,
       "vpDifSrvActBwType": vpDifSrvActBwType,
       "vpDifSrvActBwShare": vpDifSrvActBwShare,
       "vpDifSrvActTransTosByteMask": vpDifSrvActTransTosByteMask,
       "vpDifSrvActTransTosByteMatch": vpDifSrvActTransTosByteMatch,
       "vpDifSrvActMatches": vpDifSrvActMatches,
       "vpIsakmpAction": vpIsakmpAction,
       "vpIsakmpActionTable": vpIsakmpActionTable,
       "vpIsakmpActionEntry": vpIsakmpActionEntry,
       "vpIkActName": vpIkActName,
       "vpIkActExchangeMode": vpIkActExchangeMode,
       "vpIkActConnSaLifeTime": vpIkActConnSaLifeTime,
       "vpIkActConnSaLifeSize": vpIkActConnSaLifeSize,
       "vpIkActPolicyRole": vpIkActPolicyRole,
       "vpIkActMinPercentRefresh": vpIkActMinPercentRefresh,
       "vpIkActAutoStart": vpIkActAutoStart,
       "vpIkActMatches": vpIkActMatches,
       "vpIsakmpProposalTable": vpIsakmpProposalTable,
       "vpIsakmpProposalEntry": vpIsakmpProposalEntry,
       "vpIkPropName": vpIkPropName,
       "vpIkPropAuthMethod": vpIkPropAuthMethod,
       "vpIkPropHashAlgo": vpIkPropHashAlgo,
       "vpIkPropCipherAlgo": vpIkPropCipherAlgo,
       "vpIkPropDiffHellmanGrpId": vpIkPropDiffHellmanGrpId,
       "vpIkPropSaLifeTime": vpIkPropSaLifeTime,
       "vpIkPropSaLifeSize": vpIkPropSaLifeSize,
       "vpIsakmpCorTable": vpIsakmpCorTable,
       "vpIsakmpCorEntry": vpIsakmpCorEntry,
       "vpIkCorPropOrder": vpIkCorPropOrder,
       "vpIkCorPropName": vpIkCorPropName,
       "vpIsakmpActiveInstTable": vpIsakmpActiveInstTable,
       "vpIsakmpActiveInstEntry": vpIsakmpActiveInstEntry,
       "vpIkActInstOrder": vpIkActInstOrder,
       "vpIkActInstTunnelId": vpIkActInstTunnelId,
       "vpIkActInstTunnelIndex": vpIkActInstTunnelIndex,
       "vpSecurityAction": vpSecurityAction,
       "vpSecurityActionTable": vpSecurityActionTable,
       "vpSecurityActionEntry": vpSecurityActionEntry,
       "vpSecActName": vpSecActName,
       "vpSecActType": vpSecActType,
       "vpSecActTunStartAddr": vpSecActTunStartAddr,
       "vpSecActTunEndAddr": vpSecActTunEndAddr,
       "vpSecActLocProxyType": vpSecActLocProxyType,
       "vpSecActLocProxyValue": vpSecActLocProxyValue,
       "vpSecActLocProxyProtocol": vpSecActLocProxyProtocol,
       "vpSecActLocProxySrcPort": vpSecActLocProxySrcPort,
       "vpSecActRemProxyType": vpSecActRemProxyType,
       "vpSecActRemProxyValue": vpSecActRemProxyValue,
       "vpSecActRemProxyProtocol": vpSecActRemProxyProtocol,
       "vpSecActRemProxySrcPort": vpSecActRemProxySrcPort,
       "vpSecActSaRefreshThresh": vpSecActSaRefreshThresh,
       "vpSecActMinPercentRefresh": vpSecActMinPercentRefresh,
       "vpSecActTunnelInTunnel": vpSecActTunnelInTunnel,
       "vpSecActAutoStart": vpSecActAutoStart,
       "vpSecActDontFragBitHandling": vpSecActDontFragBitHandling,
       "vpSecActReplayPrevention": vpSecActReplayPrevention,
       "vpSecActMatches": vpSecActMatches,
       "vpSecurityProposalTable": vpSecurityProposalTable,
       "vpSecurityProposalEntry": vpSecurityProposalEntry,
       "vpSecPropName": vpSecPropName,
       "vpSecPropPrfFwdSecr": vpSecPropPrfFwdSecr,
       "vpSecPropDiffHellmanGrpId": vpSecPropDiffHellmanGrpId,
       "vpSecurityAhTransTable": vpSecurityAhTransTable,
       "vpSecurityAhTransEntry": vpSecurityAhTransEntry,
       "vpSecAhTransName": vpSecAhTransName,
       "vpSecAhTransIntgAlgo": vpSecAhTransIntgAlgo,
       "vpSecAhTransEncapMode": vpSecAhTransEncapMode,
       "vpSecAhTransSaLifeTime": vpSecAhTransSaLifeTime,
       "vpSecAhTransSaLifeSize": vpSecAhTransSaLifeSize,
       "vpSecurityEspTransTable": vpSecurityEspTransTable,
       "vpSecurityEspTransEntry": vpSecurityEspTransEntry,
       "vpSecEspTransName": vpSecEspTransName,
       "vpSecEspTransEncapMode": vpSecEspTransEncapMode,
       "vpSecEspTransIntgAlgo": vpSecEspTransIntgAlgo,
       "vpSecEspTransCipherAlgo": vpSecEspTransCipherAlgo,
       "vpSecEspTransSaLifeTime": vpSecEspTransSaLifeTime,
       "vpSecEspTransSaLifeSize": vpSecEspTransSaLifeSize,
       "vpSecurityIpcompTransTable": vpSecurityIpcompTransTable,
       "vpSecurityIpcompTransEntry": vpSecurityIpcompTransEntry,
       "vpSecIpcompTransName": vpSecIpcompTransName,
       "vpSecIpcompTransAlgo": vpSecIpcompTransAlgo,
       "vpSecIpcompTransVendAlgo": vpSecIpcompTransVendAlgo,
       "vpSecIpcompTransSaLifeTime": vpSecIpcompTransSaLifeTime,
       "vpSecIpcompTransSaLifeSize": vpSecIpcompTransSaLifeSize,
       "vpSecurityPropCorTable": vpSecurityPropCorTable,
       "vpSecurityPropCorEntry": vpSecurityPropCorEntry,
       "vpSecCorPropOrder": vpSecCorPropOrder,
       "vpSecCorPropRef": vpSecCorPropRef,
       "vpSecurityAhCorTable": vpSecurityAhCorTable,
       "vpSecurityAhCorEntry": vpSecurityAhCorEntry,
       "vpSecAhTransCorOrder": vpSecAhTransCorOrder,
       "vpSecAhTransCorName": vpSecAhTransCorName,
       "vpSecurityEspCorTable": vpSecurityEspCorTable,
       "vpSecurityEspCorEntry": vpSecurityEspCorEntry,
       "vpSecEspTransCorOrder": vpSecEspTransCorOrder,
       "vpSecEspTransCorName": vpSecEspTransCorName,
       "vpSecurityIpcompCorTable": vpSecurityIpcompCorTable,
       "vpSecurityIpcompCorEntry": vpSecurityIpcompCorEntry,
       "vpSecIpcompTransCorOrder": vpSecIpcompTransCorOrder,
       "vpSecIpcompTransCorName": vpSecIpcompTransCorName,
       "vpSecurityActiveInstTable": vpSecurityActiveInstTable,
       "vpSecurityActiveInstEntry": vpSecurityActiveInstEntry,
       "vpSecActInstOrder": vpSecActInstOrder,
       "vpSecActInstTunnelId": vpSecActInstTunnelId,
       "vpSecActInstTunnelIndex": vpSecActInstTunnelIndex,
       "vpTests": vpTests,
       "vpTestPolicyTable": vpTestPolicyTable,
       "vpTestPolicyEntry": vpTestPolicyEntry,
       "vpTestPolIndex": vpTestPolIndex,
       "vpTestPolSrcAddr": vpTestPolSrcAddr,
       "vpTestPolSrcPort": vpTestPolSrcPort,
       "vpTestPolDstAddr": vpTestPolDstAddr,
       "vpTestPolDstPort": vpTestPolDstPort,
       "vpTestPolProtocol": vpTestPolProtocol,
       "vpTestPolTosByte": vpTestPolTosByte,
       "vpTestPolIngressAddr": vpTestPolIngressAddr,
       "vpTestPolEgressAddr": vpTestPolEgressAddr,
       "vpTestPolResult": vpTestPolResult,
       "vpTestPolStatus": vpTestPolStatus,
       "vpTestPolRsvpPolicy": vpTestPolRsvpPolicy,
       "vpTestPolRsvpAction": vpTestPolRsvpAction,
       "vpTestPolDiffServPolicy": vpTestPolDiffServPolicy,
       "vpTestPolDiffServAction": vpTestPolDiffServAction,
       "vpTestPolIsakmpPolicy": vpTestPolIsakmpPolicy,
       "vpTestPolIsakmpAction": vpTestPolIsakmpAction,
       "vpTestPolIPSecPolicy": vpTestPolIPSecPolicy,
       "vpTestPolIPSecAction": vpTestPolIPSecAction}
)
