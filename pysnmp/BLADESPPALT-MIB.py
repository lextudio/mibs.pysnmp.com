# SNMP MIB module (BLADESPPALT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLADESPPALT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:00 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_SupportProcessor_ObjectIdentity = ObjectIdentity
supportProcessor = _SupportProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 158)
)
_MmRemoteSupTrapMIB_ObjectIdentity = ObjectIdentity
mmRemoteSupTrapMIB = _MmRemoteSupTrapMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3)
)
_RemoteSupTrapMibObjects_ObjectIdentity = ObjectIdentity
remoteSupTrapMibObjects = _RemoteSupTrapMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1)
)
_SpTrapInfo_ObjectIdentity = ObjectIdentity
spTrapInfo = _SpTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1)
)
_SpTrapDateTime_Type = DisplayString
_SpTrapDateTime_Object = MibScalar
spTrapDateTime = _SpTrapDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 1),
    _SpTrapDateTime_Type()
)
spTrapDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapDateTime.setStatus("mandatory")
_SpTrapAppId_Type = DisplayString
_SpTrapAppId_Object = MibScalar
spTrapAppId = _SpTrapAppId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 2),
    _SpTrapAppId_Type()
)
spTrapAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapAppId.setStatus("mandatory")
_SpTrapSpTxtId_Type = DisplayString
_SpTrapSpTxtId_Object = MibScalar
spTrapSpTxtId = _SpTrapSpTxtId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 3),
    _SpTrapSpTxtId_Type()
)
spTrapSpTxtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapSpTxtId.setStatus("mandatory")
_SpTrapSysUuid_Type = DisplayString
_SpTrapSysUuid_Object = MibScalar
spTrapSysUuid = _SpTrapSysUuid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 4),
    _SpTrapSysUuid_Type()
)
spTrapSysUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapSysUuid.setStatus("mandatory")
_SpTrapSysSern_Type = DisplayString
_SpTrapSysSern_Object = MibScalar
spTrapSysSern = _SpTrapSysSern_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 5),
    _SpTrapSysSern_Type()
)
spTrapSysSern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapSysSern.setStatus("mandatory")


class _SpTrapAppType_Type(Integer32):
    """Custom type spTrapAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SpTrapAppType_Type.__name__ = "Integer32"
_SpTrapAppType_Object = MibScalar
spTrapAppType = _SpTrapAppType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 6),
    _SpTrapAppType_Type()
)
spTrapAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapAppType.setStatus("mandatory")


class _SpTrapPriority_Type(Integer32):
    """Custom type spTrapPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SpTrapPriority_Type.__name__ = "Integer32"
_SpTrapPriority_Object = MibScalar
spTrapPriority = _SpTrapPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 7),
    _SpTrapPriority_Type()
)
spTrapPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapPriority.setStatus("mandatory")
_SpTrapMsgText_Type = DisplayString
_SpTrapMsgText_Object = MibScalar
spTrapMsgText = _SpTrapMsgText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 8),
    _SpTrapMsgText_Type()
)
spTrapMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapMsgText.setStatus("mandatory")
_SpTrapHostContact_Type = DisplayString
_SpTrapHostContact_Object = MibScalar
spTrapHostContact = _SpTrapHostContact_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 9),
    _SpTrapHostContact_Type()
)
spTrapHostContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapHostContact.setStatus("mandatory")
_SpTrapHostLocation_Type = DisplayString
_SpTrapHostLocation_Object = MibScalar
spTrapHostLocation = _SpTrapHostLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 10),
    _SpTrapHostLocation_Type()
)
spTrapHostLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapHostLocation.setStatus("mandatory")
_SpTrapBladeName_Type = DisplayString
_SpTrapBladeName_Object = MibScalar
spTrapBladeName = _SpTrapBladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 11),
    _SpTrapBladeName_Type()
)
spTrapBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapBladeName.setStatus("mandatory")
_SpTrapBladeSern_Type = DisplayString
_SpTrapBladeSern_Object = MibScalar
spTrapBladeSern = _SpTrapBladeSern_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 12),
    _SpTrapBladeSern_Type()
)
spTrapBladeSern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapBladeSern.setStatus("mandatory")
_SpTrapBladeUuid_Type = DisplayString
_SpTrapBladeUuid_Object = MibScalar
spTrapBladeUuid = _SpTrapBladeUuid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 13),
    _SpTrapBladeUuid_Type()
)
spTrapBladeUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapBladeUuid.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mmTrapTempC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 0)
)
mmTrapTempC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapTempC.setStatus(
        ""
    )

mmTrapVoltC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 1)
)
mmTrapVoltC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapVoltC.setStatus(
        ""
    )

mmTrapTampC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 2)
)
mmTrapTampC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapTampC.setStatus(
        ""
    )

mmTrapMffC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 3)
)
mmTrapMffC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapMffC.setStatus(
        ""
    )

mmTrapPsC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 4)
)
mmTrapPsC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapPsC.setStatus(
        ""
    )

mTrapHdC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 5)
)
mTrapHdC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mTrapHdC.setStatus(
        ""
    )

mmTrapVrmC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 6)
)
mmTrapVrmC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapVrmC.setStatus(
        ""
    )

mmTrapRdpsN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 10)
)
mmTrapRdpsN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapRdpsN.setStatus(
        ""
    )

mmTrapSffC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 11)
)
mmTrapSffC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapSffC.setStatus(
        ""
    )

mmTrapTempN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 12)
)
mmTrapTempN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapTempN.setStatus(
        ""
    )

mmTrapVoltN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 13)
)
mmTrapVoltN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapVoltN.setStatus(
        ""
    )

mmTrapSecDvS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 15)
)
mmTrapSecDvS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapSecDvS.setStatus(
        ""
    )

mmTrapPostToS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 20)
)
mmTrapPostToS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapPostToS.setStatus(
        ""
    )

mmTrapOsToS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 21)
)
mmTrapOsToS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapOsToS.setStatus(
        ""
    )

mmTrapAppS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 22)
)
mmTrapAppS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapAppS.setStatus(
        ""
    )

mmTrapPoffS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 23)
)
mmTrapPoffS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapPoffS.setStatus(
        ""
    )

mmTrapPonS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 24)
)
mmTrapPonS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapPonS.setStatus(
        ""
    )

mmTrapBootS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 25)
)
mmTrapBootS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapBootS.setStatus(
        ""
    )

mmTrapLdrToS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 26)
)
mmTrapLdrToS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapLdrToS.setStatus(
        ""
    )

mmTrapPFAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 27)
)
mmTrapPFAS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapPFAS.setStatus(
        ""
    )

mmTrapMsC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 31)
)
mmTrapMsC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapMsC.setStatus(
        ""
    )

mmTrapRmN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 32)
)
mmTrapRmN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapRmN.setStatus(
        ""
    )

mmTrapKVMSwitchS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 33)
)
mmTrapKVMSwitchS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapKVMSwitchS.setStatus(
        ""
    )

mmTrapSysInvS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 34)
)
mmTrapSysInvS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapSysInvS.setStatus(
        ""
    )

mmTrapSysLogS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 35)
)
mmTrapSysLogS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapSysLogS.setStatus(
        ""
    )

mmTrapIhcC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 36)
)
mmTrapIhcC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapIhcC.setStatus(
        ""
    )

mmTrapNwChangeS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 37)
)
mmTrapNwChangeS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapNwChangeS.setStatus(
        ""
    )

mmTrapBlThrS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 39)
)
mmTrapBlThrS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapBlThrS.setStatus(
        ""
    )

mmTrapPwrMgntS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 40)
)
mmTrapPwrMgntS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"))
)
if mibBuilder.loadTexts:
    mmTrapPwrMgntS.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLADESPPALT-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "supportProcessor": supportProcessor,
       "mmRemoteSupTrapMIB": mmRemoteSupTrapMIB,
       "mmTrapTempC": mmTrapTempC,
       "mmTrapVoltC": mmTrapVoltC,
       "mmTrapTampC": mmTrapTampC,
       "mmTrapMffC": mmTrapMffC,
       "mmTrapPsC": mmTrapPsC,
       "mTrapHdC": mTrapHdC,
       "mmTrapVrmC": mmTrapVrmC,
       "mmTrapRdpsN": mmTrapRdpsN,
       "mmTrapSffC": mmTrapSffC,
       "mmTrapTempN": mmTrapTempN,
       "mmTrapVoltN": mmTrapVoltN,
       "mmTrapSecDvS": mmTrapSecDvS,
       "mmTrapPostToS": mmTrapPostToS,
       "mmTrapOsToS": mmTrapOsToS,
       "mmTrapAppS": mmTrapAppS,
       "mmTrapPoffS": mmTrapPoffS,
       "mmTrapPonS": mmTrapPonS,
       "mmTrapBootS": mmTrapBootS,
       "mmTrapLdrToS": mmTrapLdrToS,
       "mmTrapPFAS": mmTrapPFAS,
       "mmTrapMsC": mmTrapMsC,
       "mmTrapRmN": mmTrapRmN,
       "mmTrapKVMSwitchS": mmTrapKVMSwitchS,
       "mmTrapSysInvS": mmTrapSysInvS,
       "mmTrapSysLogS": mmTrapSysLogS,
       "mmTrapIhcC": mmTrapIhcC,
       "mmTrapNwChangeS": mmTrapNwChangeS,
       "mmTrapBlThrS": mmTrapBlThrS,
       "mmTrapPwrMgntS": mmTrapPwrMgntS,
       "remoteSupTrapMibObjects": remoteSupTrapMibObjects,
       "spTrapInfo": spTrapInfo,
       "spTrapDateTime": spTrapDateTime,
       "spTrapAppId": spTrapAppId,
       "spTrapSpTxtId": spTrapSpTxtId,
       "spTrapSysUuid": spTrapSysUuid,
       "spTrapSysSern": spTrapSysSern,
       "spTrapAppType": spTrapAppType,
       "spTrapPriority": spTrapPriority,
       "spTrapMsgText": spTrapMsgText,
       "spTrapHostContact": spTrapHostContact,
       "spTrapHostLocation": spTrapHostLocation,
       "spTrapBladeName": spTrapBladeName,
       "spTrapBladeSern": spTrapBladeSern,
       "spTrapBladeUuid": spTrapBladeUuid}
)
