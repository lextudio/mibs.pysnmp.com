# SNMP MIB module (CISCO-DSL-PROVISION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DSL-PROVISION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:09 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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


# MODULE-IDENTITY

ciscoDslProvisionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDslProvMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDslProvMIBObjects = _CiscoDslProvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1)
)
_CdslNrpSlot_ObjectIdentity = ObjectIdentity
cdslNrpSlot = _CdslNrpSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 1)
)


class _CdslMaxNrps_Type(Unsigned32):
    """Custom type cdslMaxNrps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslMaxNrps_Type.__name__ = "Unsigned32"
_CdslMaxNrps_Object = MibScalar
cdslMaxNrps = _CdslMaxNrps_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 1, 1),
    _CdslMaxNrps_Type()
)
cdslMaxNrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslMaxNrps.setStatus("current")


class _CdslNrpNumber_Type(Gauge32):
    """Custom type cdslNrpNumber based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslNrpNumber_Type.__name__ = "Gauge32"
_CdslNrpNumber_Object = MibScalar
cdslNrpNumber = _CdslNrpNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 1, 2),
    _CdslNrpNumber_Type()
)
cdslNrpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslNrpNumber.setStatus("current")
_CdslNrpIpAddressTable_Object = MibTable
cdslNrpIpAddressTable = _CdslNrpIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cdslNrpIpAddressTable.setStatus("current")
_CdslNrpIpAddressEntry_Object = MibTableRow
cdslNrpIpAddressEntry = _CdslNrpIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 1, 3, 1)
)
cdslNrpIpAddressEntry.setIndexNames(
    (0, "CISCO-DSL-PROVISION-MIB", "cdslNrpSlotIndex"),
)
if mibBuilder.loadTexts:
    cdslNrpIpAddressEntry.setStatus("current")


class _CdslNrpSlotIndex_Type(Integer32):
    """Custom type cdslNrpSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CdslNrpSlotIndex_Type.__name__ = "Integer32"
_CdslNrpSlotIndex_Object = MibTableColumn
cdslNrpSlotIndex = _CdslNrpSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 1, 3, 1, 1),
    _CdslNrpSlotIndex_Type()
)
cdslNrpSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdslNrpSlotIndex.setStatus("current")
_CdslNrpIpAddress_Type = IpAddress
_CdslNrpIpAddress_Object = MibTableColumn
cdslNrpIpAddress = _CdslNrpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 1, 3, 1, 2),
    _CdslNrpIpAddress_Type()
)
cdslNrpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslNrpIpAddress.setStatus("current")
_CdslVirtualTemplate_ObjectIdentity = ObjectIdentity
cdslVirtualTemplate = _CdslVirtualTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2)
)
_CdslVirtualTemplateNumberTable_Object = MibTable
cdslVirtualTemplateNumberTable = _CdslVirtualTemplateNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdslVirtualTemplateNumberTable.setStatus("current")
_CdslVirtualTemplateNumberEntry_Object = MibTableRow
cdslVirtualTemplateNumberEntry = _CdslVirtualTemplateNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 1, 1)
)
cdslVirtualTemplateNumberEntry.setIndexNames(
    (0, "CISCO-DSL-PROVISION-MIB", "cdslNrpSlotIndex"),
)
if mibBuilder.loadTexts:
    cdslVirtualTemplateNumberEntry.setStatus("current")


class _CdslMaxVirtualTemplates_Type(Unsigned32):
    """Custom type cdslMaxVirtualTemplates based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslMaxVirtualTemplates_Type.__name__ = "Unsigned32"
_CdslMaxVirtualTemplates_Object = MibTableColumn
cdslMaxVirtualTemplates = _CdslMaxVirtualTemplates_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 1, 1, 1),
    _CdslMaxVirtualTemplates_Type()
)
cdslMaxVirtualTemplates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslMaxVirtualTemplates.setStatus("current")


class _CdslVirtualTemplates_Type(Gauge32):
    """Custom type cdslVirtualTemplates based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslVirtualTemplates_Type.__name__ = "Gauge32"
_CdslVirtualTemplates_Object = MibTableColumn
cdslVirtualTemplates = _CdslVirtualTemplates_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 1, 1, 2),
    _CdslVirtualTemplates_Type()
)
cdslVirtualTemplates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslVirtualTemplates.setStatus("current")
_CdslVirtualTemplateTable_Object = MibTable
cdslVirtualTemplateTable = _CdslVirtualTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cdslVirtualTemplateTable.setStatus("current")
_CdslVirtualTemplateEntry_Object = MibTableRow
cdslVirtualTemplateEntry = _CdslVirtualTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1)
)
cdslVirtualTemplateEntry.setIndexNames(
    (0, "CISCO-DSL-PROVISION-MIB", "cdslNrpSlotIndex"),
    (0, "CISCO-DSL-PROVISION-MIB", "cdslVTIndex"),
)
if mibBuilder.loadTexts:
    cdslVirtualTemplateEntry.setStatus("current")


class _CdslVTIndex_Type(Integer32):
    """Custom type cdslVTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CdslVTIndex_Type.__name__ = "Integer32"
_CdslVTIndex_Object = MibTableColumn
cdslVTIndex = _CdslVTIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 1),
    _CdslVTIndex_Type()
)
cdslVTIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdslVTIndex.setStatus("current")


class _CdslVTIpAddressMethod_Type(Integer32):
    """Custom type cdslVTIpAddressMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interfaceIp", 2),
          ("ipAddress", 1),
          ("negotiate", 3),
          ("none", 0))
    )


_CdslVTIpAddressMethod_Type.__name__ = "Integer32"
_CdslVTIpAddressMethod_Object = MibTableColumn
cdslVTIpAddressMethod = _CdslVTIpAddressMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 2),
    _CdslVTIpAddressMethod_Type()
)
cdslVTIpAddressMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTIpAddressMethod.setStatus("current")


class _CdslVTIpAddress_Type(IpAddress):
    """Custom type cdslVTIpAddress based on IpAddress"""
    defaultValue = 0


_CdslVTIpAddress_Object = MibTableColumn
cdslVTIpAddress = _CdslVTIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 3),
    _CdslVTIpAddress_Type()
)
cdslVTIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTIpAddress.setStatus("current")


class _CdslVTIpAddressMask_Type(IpAddress):
    """Custom type cdslVTIpAddressMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_CdslVTIpAddressMask_Object = MibTableColumn
cdslVTIpAddressMask = _CdslVTIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 4),
    _CdslVTIpAddressMask_Type()
)
cdslVTIpAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTIpAddressMask.setStatus("current")


class _CdslVTIpIfIndex_Type(InterfaceIndexOrZero):
    """Custom type cdslVTIpIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CdslVTIpIfIndex_Object = MibTableColumn
cdslVTIpIfIndex = _CdslVTIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 5),
    _CdslVTIpIfIndex_Type()
)
cdslVTIpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTIpIfIndex.setStatus("current")


class _CdslVTPeerIpAddressMethod_Type(Integer32):
    """Custom type cdslVTPeerIpAddressMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipAddressPool", 2),
          ("negotiate", 1),
          ("none", 0))
    )


_CdslVTPeerIpAddressMethod_Type.__name__ = "Integer32"
_CdslVTPeerIpAddressMethod_Object = MibTableColumn
cdslVTPeerIpAddressMethod = _CdslVTPeerIpAddressMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 6),
    _CdslVTPeerIpAddressMethod_Type()
)
cdslVTPeerIpAddressMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPeerIpAddressMethod.setStatus("current")


class _CdslVTPeerIpAddrPool_Type(DisplayString):
    """Custom type cdslVTPeerIpAddrPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CdslVTPeerIpAddrPool_Type.__name__ = "DisplayString"
_CdslVTPeerIpAddrPool_Object = MibTableColumn
cdslVTPeerIpAddrPool = _CdslVTPeerIpAddrPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 7),
    _CdslVTPeerIpAddrPool_Type()
)
cdslVTPeerIpAddrPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPeerIpAddrPool.setStatus("current")


class _CdslVTPppAuthChap_Type(Integer32):
    """Custom type cdslVTPppAuthChap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdslVTPppAuthChap_Type.__name__ = "Integer32"
_CdslVTPppAuthChap_Object = MibTableColumn
cdslVTPppAuthChap = _CdslVTPppAuthChap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 8),
    _CdslVTPppAuthChap_Type()
)
cdslVTPppAuthChap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPppAuthChap.setStatus("current")


class _CdslVTPppAuthMSChap_Type(Integer32):
    """Custom type cdslVTPppAuthMSChap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdslVTPppAuthMSChap_Type.__name__ = "Integer32"
_CdslVTPppAuthMSChap_Object = MibTableColumn
cdslVTPppAuthMSChap = _CdslVTPppAuthMSChap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 9),
    _CdslVTPppAuthMSChap_Type()
)
cdslVTPppAuthMSChap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPppAuthMSChap.setStatus("current")


class _CdslVTPppAuthPap_Type(Integer32):
    """Custom type cdslVTPppAuthPap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdslVTPppAuthPap_Type.__name__ = "Integer32"
_CdslVTPppAuthPap_Object = MibTableColumn
cdslVTPppAuthPap = _CdslVTPppAuthPap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 10),
    _CdslVTPppAuthPap_Type()
)
cdslVTPppAuthPap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPppAuthPap.setStatus("current")


class _CdslVTPppChapHost_Type(DisplayString):
    """Custom type cdslVTPppChapHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CdslVTPppChapHost_Type.__name__ = "DisplayString"
_CdslVTPppChapHost_Object = MibTableColumn
cdslVTPppChapHost = _CdslVTPppChapHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 11),
    _CdslVTPppChapHost_Type()
)
cdslVTPppChapHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPppChapHost.setStatus("current")


class _CdslVTPppChapPassword_Type(DisplayString):
    """Custom type cdslVTPppChapPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_CdslVTPppChapPassword_Type.__name__ = "DisplayString"
_CdslVTPppChapPassword_Object = MibTableColumn
cdslVTPppChapPassword = _CdslVTPppChapPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 12),
    _CdslVTPppChapPassword_Type()
)
cdslVTPppChapPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPppChapPassword.setStatus("current")


class _CdslVTPppChapEncrypType_Type(TruthValue):
    """Custom type cdslVTPppChapEncrypType based on TruthValue"""


_CdslVTPppChapEncrypType_Object = MibTableColumn
cdslVTPppChapEncrypType = _CdslVTPppChapEncrypType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 13),
    _CdslVTPppChapEncrypType_Type()
)
cdslVTPppChapEncrypType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPppChapEncrypType.setStatus("current")


class _CdslVTPppChapRefuse_Type(Integer32):
    """Custom type cdslVTPppChapRefuse based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("refuse", 2),
          ("refuseCallinOnly", 3))
    )


_CdslVTPppChapRefuse_Type.__name__ = "Integer32"
_CdslVTPppChapRefuse_Object = MibTableColumn
cdslVTPppChapRefuse = _CdslVTPppChapRefuse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 14),
    _CdslVTPppChapRefuse_Type()
)
cdslVTPppChapRefuse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPppChapRefuse.setStatus("current")


class _CdslVTPppChapWaitPeer_Type(TruthValue):
    """Custom type cdslVTPppChapWaitPeer based on TruthValue"""


_CdslVTPppChapWaitPeer_Object = MibTableColumn
cdslVTPppChapWaitPeer = _CdslVTPppChapWaitPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 15),
    _CdslVTPppChapWaitPeer_Type()
)
cdslVTPppChapWaitPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPppChapWaitPeer.setStatus("current")


class _CdslVTPppPapUserName_Type(DisplayString):
    """Custom type cdslVTPppPapUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CdslVTPppPapUserName_Type.__name__ = "DisplayString"
_CdslVTPppPapUserName_Object = MibTableColumn
cdslVTPppPapUserName = _CdslVTPppPapUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 16),
    _CdslVTPppPapUserName_Type()
)
cdslVTPppPapUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPppPapUserName.setStatus("current")


class _CdslVTPppPapPassword_Type(DisplayString):
    """Custom type cdslVTPppPapPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CdslVTPppPapPassword_Type.__name__ = "DisplayString"
_CdslVTPppPapPassword_Object = MibTableColumn
cdslVTPppPapPassword = _CdslVTPppPapPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 17),
    _CdslVTPppPapPassword_Type()
)
cdslVTPppPapPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPppPapPassword.setStatus("current")


class _CdslVTPppPapEncrypType_Type(TruthValue):
    """Custom type cdslVTPppPapEncrypType based on TruthValue"""


_CdslVTPppPapEncrypType_Object = MibTableColumn
cdslVTPppPapEncrypType = _CdslVTPppPapEncrypType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 18),
    _CdslVTPppPapEncrypType_Type()
)
cdslVTPppPapEncrypType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPppPapEncrypType.setStatus("current")


class _CdslVTPppUseTacacs_Type(Integer32):
    """Custom type cdslVTPppUseTacacs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("singleLine", 3),
          ("yes", 2))
    )


_CdslVTPppUseTacacs_Type.__name__ = "Integer32"
_CdslVTPppUseTacacs_Object = MibTableColumn
cdslVTPppUseTacacs = _CdslVTPppUseTacacs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 19),
    _CdslVTPppUseTacacs_Type()
)
cdslVTPppUseTacacs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTPppUseTacacs.setStatus("current")


class _CdslVTRowStatus_Type(RowStatus):
    """Custom type cdslVTRowStatus based on RowStatus"""


_CdslVTRowStatus_Object = MibTableColumn
cdslVTRowStatus = _CdslVTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 2, 2, 1, 20),
    _CdslVTRowStatus_Type()
)
cdslVTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVTRowStatus.setStatus("current")
_CdslLocalIpAddrPool_ObjectIdentity = ObjectIdentity
cdslLocalIpAddrPool = _CdslLocalIpAddrPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3)
)
_CdslLocalIpAddrPoolNumberTable_Object = MibTable
cdslLocalIpAddrPoolNumberTable = _CdslLocalIpAddrPoolNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdslLocalIpAddrPoolNumberTable.setStatus("current")
_CdslLocalIpAddrPoolNumberEntry_Object = MibTableRow
cdslLocalIpAddrPoolNumberEntry = _CdslLocalIpAddrPoolNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 1, 1)
)
cdslLocalIpAddrPoolNumberEntry.setIndexNames(
    (0, "CISCO-DSL-PROVISION-MIB", "cdslNrpSlotIndex"),
)
if mibBuilder.loadTexts:
    cdslLocalIpAddrPoolNumberEntry.setStatus("current")


class _CdslMaxLocalIpAddrPools_Type(Unsigned32):
    """Custom type cdslMaxLocalIpAddrPools based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslMaxLocalIpAddrPools_Type.__name__ = "Unsigned32"
_CdslMaxLocalIpAddrPools_Object = MibTableColumn
cdslMaxLocalIpAddrPools = _CdslMaxLocalIpAddrPools_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 1, 1, 1),
    _CdslMaxLocalIpAddrPools_Type()
)
cdslMaxLocalIpAddrPools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslMaxLocalIpAddrPools.setStatus("current")


class _CdslLocalIpAddrPools_Type(Gauge32):
    """Custom type cdslLocalIpAddrPools based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslLocalIpAddrPools_Type.__name__ = "Gauge32"
_CdslLocalIpAddrPools_Object = MibTableColumn
cdslLocalIpAddrPools = _CdslLocalIpAddrPools_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 1, 1, 2),
    _CdslLocalIpAddrPools_Type()
)
cdslLocalIpAddrPools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslLocalIpAddrPools.setStatus("current")
_CdslLocalIpAddrPoolTable_Object = MibTable
cdslLocalIpAddrPoolTable = _CdslLocalIpAddrPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cdslLocalIpAddrPoolTable.setStatus("current")
_CdslLocalIpAddrPoolEntry_Object = MibTableRow
cdslLocalIpAddrPoolEntry = _CdslLocalIpAddrPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 2, 1)
)
cdslLocalIpAddrPoolEntry.setIndexNames(
    (0, "CISCO-DSL-PROVISION-MIB", "cdslNrpSlotIndex"),
    (1, "CISCO-DSL-PROVISION-MIB", "cdslLocalIpAddrPoolName"),
)
if mibBuilder.loadTexts:
    cdslLocalIpAddrPoolEntry.setStatus("current")


class _CdslLocalIpAddrPoolName_Type(DisplayString):
    """Custom type cdslLocalIpAddrPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CdslLocalIpAddrPoolName_Type.__name__ = "DisplayString"
_CdslLocalIpAddrPoolName_Object = MibTableColumn
cdslLocalIpAddrPoolName = _CdslLocalIpAddrPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 2, 1, 1),
    _CdslLocalIpAddrPoolName_Type()
)
cdslLocalIpAddrPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdslLocalIpAddrPoolName.setStatus("current")


class _CdslLocalIpAddrPoolFreeAddresses_Type(Unsigned32):
    """Custom type cdslLocalIpAddrPoolFreeAddresses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslLocalIpAddrPoolFreeAddresses_Type.__name__ = "Unsigned32"
_CdslLocalIpAddrPoolFreeAddresses_Object = MibTableColumn
cdslLocalIpAddrPoolFreeAddresses = _CdslLocalIpAddrPoolFreeAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 2, 1, 2),
    _CdslLocalIpAddrPoolFreeAddresses_Type()
)
cdslLocalIpAddrPoolFreeAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslLocalIpAddrPoolFreeAddresses.setStatus("current")


class _CdslLocalIpAddrPoolInUseAddresses_Type(Unsigned32):
    """Custom type cdslLocalIpAddrPoolInUseAddresses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslLocalIpAddrPoolInUseAddresses_Type.__name__ = "Unsigned32"
_CdslLocalIpAddrPoolInUseAddresses_Object = MibTableColumn
cdslLocalIpAddrPoolInUseAddresses = _CdslLocalIpAddrPoolInUseAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 2, 1, 3),
    _CdslLocalIpAddrPoolInUseAddresses_Type()
)
cdslLocalIpAddrPoolInUseAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslLocalIpAddrPoolInUseAddresses.setStatus("current")
_CdslLocalIpAddrRangeTable_Object = MibTable
cdslLocalIpAddrRangeTable = _CdslLocalIpAddrRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cdslLocalIpAddrRangeTable.setStatus("current")
_CdslLocalIpAddrRangeEntry_Object = MibTableRow
cdslLocalIpAddrRangeEntry = _CdslLocalIpAddrRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 3, 1)
)
cdslLocalIpAddrRangeEntry.setIndexNames(
    (0, "CISCO-DSL-PROVISION-MIB", "cdslNrpSlotIndex"),
    (0, "CISCO-DSL-PROVISION-MIB", "cdslLocalIpAddrRangeLowAddr"),
    (0, "CISCO-DSL-PROVISION-MIB", "cdslLocalIpAddrRangeHighAddr"),
    (1, "CISCO-DSL-PROVISION-MIB", "cdslLocalIpAddrPoolName"),
)
if mibBuilder.loadTexts:
    cdslLocalIpAddrRangeEntry.setStatus("current")
_CdslLocalIpAddrRangeLowAddr_Type = IpAddress
_CdslLocalIpAddrRangeLowAddr_Object = MibTableColumn
cdslLocalIpAddrRangeLowAddr = _CdslLocalIpAddrRangeLowAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 3, 1, 1),
    _CdslLocalIpAddrRangeLowAddr_Type()
)
cdslLocalIpAddrRangeLowAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdslLocalIpAddrRangeLowAddr.setStatus("current")
_CdslLocalIpAddrRangeHighAddr_Type = IpAddress
_CdslLocalIpAddrRangeHighAddr_Object = MibTableColumn
cdslLocalIpAddrRangeHighAddr = _CdslLocalIpAddrRangeHighAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 3, 1, 2),
    _CdslLocalIpAddrRangeHighAddr_Type()
)
cdslLocalIpAddrRangeHighAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdslLocalIpAddrRangeHighAddr.setStatus("current")
_CdslLocalIpAddrRangeRowStatus_Type = RowStatus
_CdslLocalIpAddrRangeRowStatus_Object = MibTableColumn
cdslLocalIpAddrRangeRowStatus = _CdslLocalIpAddrRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 3, 3, 1, 3),
    _CdslLocalIpAddrRangeRowStatus_Type()
)
cdslLocalIpAddrRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslLocalIpAddrRangeRowStatus.setStatus("current")
_CdslAtmPvc_ObjectIdentity = ObjectIdentity
cdslAtmPvc = _CdslAtmPvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4)
)
_CdslPppOverAtmPvcNumberTable_Object = MibTable
cdslPppOverAtmPvcNumberTable = _CdslPppOverAtmPvcNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cdslPppOverAtmPvcNumberTable.setStatus("current")
_CdslPppOverAtmPvcNumberEntry_Object = MibTableRow
cdslPppOverAtmPvcNumberEntry = _CdslPppOverAtmPvcNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 1, 1)
)
cdslPppOverAtmPvcNumberEntry.setIndexNames(
    (0, "CISCO-DSL-PROVISION-MIB", "cdslNrpSlotIndex"),
)
if mibBuilder.loadTexts:
    cdslPppOverAtmPvcNumberEntry.setStatus("current")


class _CdslPppOverAtmPvcs_Type(Gauge32):
    """Custom type cdslPppOverAtmPvcs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslPppOverAtmPvcs_Type.__name__ = "Gauge32"
_CdslPppOverAtmPvcs_Object = MibTableColumn
cdslPppOverAtmPvcs = _CdslPppOverAtmPvcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 1, 1, 1),
    _CdslPppOverAtmPvcs_Type()
)
cdslPppOverAtmPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslPppOverAtmPvcs.setStatus("current")
_CdslAtmPvcTable_Object = MibTable
cdslAtmPvcTable = _CdslAtmPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cdslAtmPvcTable.setStatus("current")
_CdslAtmPvcEntry_Object = MibTableRow
cdslAtmPvcEntry = _CdslAtmPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1)
)
cdslAtmPvcEntry.setIndexNames(
    (0, "CISCO-DSL-PROVISION-MIB", "cdslNrpSlotIndex"),
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DSL-PROVISION-MIB", "cdslAtmPvcVpi"),
    (0, "CISCO-DSL-PROVISION-MIB", "cdslAtmPvcVci"),
)
if mibBuilder.loadTexts:
    cdslAtmPvcEntry.setStatus("current")


class _CdslAtmPvcVpi_Type(Integer32):
    """Custom type cdslAtmPvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdslAtmPvcVpi_Type.__name__ = "Integer32"
_CdslAtmPvcVpi_Object = MibTableColumn
cdslAtmPvcVpi = _CdslAtmPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 1),
    _CdslAtmPvcVpi_Type()
)
cdslAtmPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdslAtmPvcVpi.setStatus("current")


class _CdslAtmPvcVci_Type(Integer32):
    """Custom type cdslAtmPvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdslAtmPvcVci_Type.__name__ = "Integer32"
_CdslAtmPvcVci_Object = MibTableColumn
cdslAtmPvcVci = _CdslAtmPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 2),
    _CdslAtmPvcVci_Type()
)
cdslAtmPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdslAtmPvcVci.setStatus("current")


class _CdslAtmPvcName_Type(DisplayString):
    """Custom type cdslAtmPvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CdslAtmPvcName_Type.__name__ = "DisplayString"
_CdslAtmPvcName_Object = MibTableColumn
cdslAtmPvcName = _CdslAtmPvcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 3),
    _CdslAtmPvcName_Type()
)
cdslAtmPvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslAtmPvcName.setStatus("current")


class _CdslAtmPvcSubIfNumber_Type(Integer32):
    """Custom type cdslAtmPvcSubIfNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdslAtmPvcSubIfNumber_Type.__name__ = "Integer32"
_CdslAtmPvcSubIfNumber_Object = MibTableColumn
cdslAtmPvcSubIfNumber = _CdslAtmPvcSubIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 4),
    _CdslAtmPvcSubIfNumber_Type()
)
cdslAtmPvcSubIfNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslAtmPvcSubIfNumber.setStatus("current")


class _CdslAtmPvcClass_Type(DisplayString):
    """Custom type cdslAtmPvcClass based on DisplayString"""
    defaultValue = OctetString("default-vc-class")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CdslAtmPvcClass_Type.__name__ = "DisplayString"
_CdslAtmPvcClass_Object = MibTableColumn
cdslAtmPvcClass = _CdslAtmPvcClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 5),
    _CdslAtmPvcClass_Type()
)
cdslAtmPvcClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslAtmPvcClass.setStatus("current")


class _CdslAtmPvcQosType_Type(Integer32):
    """Custom type cdslAtmPvcQosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abr", 6),
          ("cbr", 1),
          ("max", 7),
          ("ubr", 2),
          ("ubrDefault", 0),
          ("ubrPlus", 3),
          ("vbrNrt", 5),
          ("vbrRt", 4))
    )


_CdslAtmPvcQosType_Type.__name__ = "Integer32"
_CdslAtmPvcQosType_Object = MibTableColumn
cdslAtmPvcQosType = _CdslAtmPvcQosType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 6),
    _CdslAtmPvcQosType_Type()
)
cdslAtmPvcQosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcQosType.setStatus("current")


class _CdslAtmPvcAbrPCR_Type(Unsigned32):
    """Custom type cdslAtmPvcAbrPCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslAtmPvcAbrPCR_Type.__name__ = "Unsigned32"
_CdslAtmPvcAbrPCR_Object = MibTableColumn
cdslAtmPvcAbrPCR = _CdslAtmPvcAbrPCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 7),
    _CdslAtmPvcAbrPCR_Type()
)
cdslAtmPvcAbrPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcAbrPCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslAtmPvcAbrPCR.setUnits("kbps")


class _CdslAtmPvcAbrMCR_Type(Unsigned32):
    """Custom type cdslAtmPvcAbrMCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CdslAtmPvcAbrMCR_Type.__name__ = "Unsigned32"
_CdslAtmPvcAbrMCR_Object = MibTableColumn
cdslAtmPvcAbrMCR = _CdslAtmPvcAbrMCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 8),
    _CdslAtmPvcAbrMCR_Type()
)
cdslAtmPvcAbrMCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcAbrMCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslAtmPvcAbrMCR.setUnits("kbps")


class _CdslAtmPvcAbrIORIF_Type(Unsigned32):
    """Custom type cdslAtmPvcAbrIORIF based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslAtmPvcAbrIORIF_Type.__name__ = "Unsigned32"
_CdslAtmPvcAbrIORIF_Object = MibTableColumn
cdslAtmPvcAbrIORIF = _CdslAtmPvcAbrIORIF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 9),
    _CdslAtmPvcAbrIORIF_Type()
)
cdslAtmPvcAbrIORIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcAbrIORIF.setStatus("current")


class _CdslAtmPvcAbrIORDF_Type(Unsigned32):
    """Custom type cdslAtmPvcAbrIORDF based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslAtmPvcAbrIORDF_Type.__name__ = "Unsigned32"
_CdslAtmPvcAbrIORDF_Object = MibTableColumn
cdslAtmPvcAbrIORDF = _CdslAtmPvcAbrIORDF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 10),
    _CdslAtmPvcAbrIORDF_Type()
)
cdslAtmPvcAbrIORDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcAbrIORDF.setStatus("current")


class _CdslAtmPvcBroadcast_Type(Integer32):
    """Custom type cdslAtmPvcBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_CdslAtmPvcBroadcast_Type.__name__ = "Integer32"
_CdslAtmPvcBroadcast_Object = MibTableColumn
cdslAtmPvcBroadcast = _CdslAtmPvcBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 11),
    _CdslAtmPvcBroadcast_Type()
)
cdslAtmPvcBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcBroadcast.setStatus("current")


class _CdslAtmPvcEncapsulation_Type(Integer32):
    """Custom type cdslAtmPvcEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aal34smds", 4),
          ("aal5ciscoppp", 7),
          ("aal5ilmi", 5),
          ("aal5mux", 2),
          ("aal5nlpid", 3),
          ("aal5qsaal", 6),
          ("aal5snap", 1),
          ("default", 0))
    )


_CdslAtmPvcEncapsulation_Type.__name__ = "Integer32"
_CdslAtmPvcEncapsulation_Object = MibTableColumn
cdslAtmPvcEncapsulation = _CdslAtmPvcEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 12),
    _CdslAtmPvcEncapsulation_Type()
)
cdslAtmPvcEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcEncapsulation.setStatus("current")


class _CdslAtmPvcMuxLinkType_Type(Integer32):
    """Custom type cdslAtmPvcMuxLinkType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ppp", 2))
    )


_CdslAtmPvcMuxLinkType_Type.__name__ = "Integer32"
_CdslAtmPvcMuxLinkType_Object = MibTableColumn
cdslAtmPvcMuxLinkType = _CdslAtmPvcMuxLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 13),
    _CdslAtmPvcMuxLinkType_Type()
)
cdslAtmPvcMuxLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslAtmPvcMuxLinkType.setStatus("current")


class _CdslAtmPvcVirtualTemplate_Type(Integer32):
    """Custom type cdslAtmPvcVirtualTemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdslAtmPvcVirtualTemplate_Type.__name__ = "Integer32"
_CdslAtmPvcVirtualTemplate_Object = MibTableColumn
cdslAtmPvcVirtualTemplate = _CdslAtmPvcVirtualTemplate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 14),
    _CdslAtmPvcVirtualTemplate_Type()
)
cdslAtmPvcVirtualTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslAtmPvcVirtualTemplate.setStatus("current")


class _CdslAtmPvcILMIManage_Type(Integer32):
    """Custom type cdslAtmPvcILMIManage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_CdslAtmPvcILMIManage_Type.__name__ = "Integer32"
_CdslAtmPvcILMIManage_Object = MibTableColumn
cdslAtmPvcILMIManage = _CdslAtmPvcILMIManage_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 15),
    _CdslAtmPvcILMIManage_Type()
)
cdslAtmPvcILMIManage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcILMIManage.setStatus("current")


class _CdslAtmPvcInarp_Type(Unsigned32):
    """Custom type cdslAtmPvcInarp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CdslAtmPvcInarp_Type.__name__ = "Unsigned32"
_CdslAtmPvcInarp_Object = MibTableColumn
cdslAtmPvcInarp = _CdslAtmPvcInarp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 16),
    _CdslAtmPvcInarp_Type()
)
cdslAtmPvcInarp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcInarp.setStatus("current")


class _CdslAtmPvcOamRetryUpCount_Type(Unsigned32):
    """Custom type cdslAtmPvcOamRetryUpCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CdslAtmPvcOamRetryUpCount_Type.__name__ = "Unsigned32"
_CdslAtmPvcOamRetryUpCount_Object = MibTableColumn
cdslAtmPvcOamRetryUpCount = _CdslAtmPvcOamRetryUpCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 17),
    _CdslAtmPvcOamRetryUpCount_Type()
)
cdslAtmPvcOamRetryUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcOamRetryUpCount.setStatus("current")


class _CdslAtmPvcOamRetryDownCount_Type(Unsigned32):
    """Custom type cdslAtmPvcOamRetryDownCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CdslAtmPvcOamRetryDownCount_Type.__name__ = "Unsigned32"
_CdslAtmPvcOamRetryDownCount_Object = MibTableColumn
cdslAtmPvcOamRetryDownCount = _CdslAtmPvcOamRetryDownCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 18),
    _CdslAtmPvcOamRetryDownCount_Type()
)
cdslAtmPvcOamRetryDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcOamRetryDownCount.setStatus("current")


class _CdslAtmPvcOamPvcManaged_Type(Integer32):
    """Custom type cdslAtmPvcOamPvcManaged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_CdslAtmPvcOamPvcManaged_Type.__name__ = "Integer32"
_CdslAtmPvcOamPvcManaged_Object = MibTableColumn
cdslAtmPvcOamPvcManaged = _CdslAtmPvcOamPvcManaged_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 19),
    _CdslAtmPvcOamPvcManaged_Type()
)
cdslAtmPvcOamPvcManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcOamPvcManaged.setStatus("current")


class _CdslAtmPvcOamPvcLF_Type(Unsigned32):
    """Custom type cdslAtmPvcOamPvcLF based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CdslAtmPvcOamPvcLF_Type.__name__ = "Unsigned32"
_CdslAtmPvcOamPvcLF_Object = MibTableColumn
cdslAtmPvcOamPvcLF = _CdslAtmPvcOamPvcLF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 20),
    _CdslAtmPvcOamPvcLF_Type()
)
cdslAtmPvcOamPvcLF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcOamPvcLF.setStatus("current")
_CdslAtmPvcProtocolIpBC_Type = TruthValue
_CdslAtmPvcProtocolIpBC_Object = MibTableColumn
cdslAtmPvcProtocolIpBC = _CdslAtmPvcProtocolIpBC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 21),
    _CdslAtmPvcProtocolIpBC_Type()
)
cdslAtmPvcProtocolIpBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcProtocolIpBC.setStatus("current")
_CdslAtmPvcProtocolIpxBC_Type = TruthValue
_CdslAtmPvcProtocolIpxBC_Object = MibTableColumn
cdslAtmPvcProtocolIpxBC = _CdslAtmPvcProtocolIpxBC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 22),
    _CdslAtmPvcProtocolIpxBC_Type()
)
cdslAtmPvcProtocolIpxBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcProtocolIpxBC.setStatus("current")


class _CdslAtmPvcUbrPCR_Type(Unsigned32):
    """Custom type cdslAtmPvcUbrPCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 155000),
    )


_CdslAtmPvcUbrPCR_Type.__name__ = "Unsigned32"
_CdslAtmPvcUbrPCR_Object = MibTableColumn
cdslAtmPvcUbrPCR = _CdslAtmPvcUbrPCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 23),
    _CdslAtmPvcUbrPCR_Type()
)
cdslAtmPvcUbrPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcUbrPCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslAtmPvcUbrPCR.setUnits("kbps")


class _CdslAtmPvcUbrPlusPCR_Type(Unsigned32):
    """Custom type cdslAtmPvcUbrPlusPCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 155000),
    )


_CdslAtmPvcUbrPlusPCR_Type.__name__ = "Unsigned32"
_CdslAtmPvcUbrPlusPCR_Object = MibTableColumn
cdslAtmPvcUbrPlusPCR = _CdslAtmPvcUbrPlusPCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 24),
    _CdslAtmPvcUbrPlusPCR_Type()
)
cdslAtmPvcUbrPlusPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcUbrPlusPCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslAtmPvcUbrPlusPCR.setUnits("kbps")


class _CdslAtmPvcUbrPlusMCR_Type(Unsigned32):
    """Custom type cdslAtmPvcUbrPlusMCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CdslAtmPvcUbrPlusMCR_Type.__name__ = "Unsigned32"
_CdslAtmPvcUbrPlusMCR_Object = MibTableColumn
cdslAtmPvcUbrPlusMCR = _CdslAtmPvcUbrPlusMCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 25),
    _CdslAtmPvcUbrPlusMCR_Type()
)
cdslAtmPvcUbrPlusMCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcUbrPlusMCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslAtmPvcUbrPlusMCR.setUnits("kbps")


class _CdslAtmPvcVbrNrtPCR_Type(Unsigned32):
    """Custom type cdslAtmPvcVbrNrtPCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 155000),
    )


_CdslAtmPvcVbrNrtPCR_Type.__name__ = "Unsigned32"
_CdslAtmPvcVbrNrtPCR_Object = MibTableColumn
cdslAtmPvcVbrNrtPCR = _CdslAtmPvcVbrNrtPCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 26),
    _CdslAtmPvcVbrNrtPCR_Type()
)
cdslAtmPvcVbrNrtPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcVbrNrtPCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslAtmPvcVbrNrtPCR.setUnits("kbps")


class _CdslAtmPvcVbrNrtSCR_Type(Unsigned32):
    """Custom type cdslAtmPvcVbrNrtSCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CdslAtmPvcVbrNrtSCR_Type.__name__ = "Unsigned32"
_CdslAtmPvcVbrNrtSCR_Object = MibTableColumn
cdslAtmPvcVbrNrtSCR = _CdslAtmPvcVbrNrtSCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 27),
    _CdslAtmPvcVbrNrtSCR_Type()
)
cdslAtmPvcVbrNrtSCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslAtmPvcVbrNrtSCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslAtmPvcVbrNrtSCR.setUnits("kbps")


class _CdslAtmPvcRowStatus_Type(RowStatus):
    """Custom type cdslAtmPvcRowStatus based on RowStatus"""


_CdslAtmPvcRowStatus_Object = MibTableColumn
cdslAtmPvcRowStatus = _CdslAtmPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 4, 2, 1, 28),
    _CdslAtmPvcRowStatus_Type()
)
cdslAtmPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslAtmPvcRowStatus.setStatus("current")
_CdslVcClass_ObjectIdentity = ObjectIdentity
cdslVcClass = _CdslVcClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5)
)
_CdslVcClassNumberTable_Object = MibTable
cdslVcClassNumberTable = _CdslVcClassNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cdslVcClassNumberTable.setStatus("current")
_CdslVcClassNumberEntry_Object = MibTableRow
cdslVcClassNumberEntry = _CdslVcClassNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 1, 1)
)
cdslVcClassNumberEntry.setIndexNames(
    (0, "CISCO-DSL-PROVISION-MIB", "cdslNrpSlotIndex"),
)
if mibBuilder.loadTexts:
    cdslVcClassNumberEntry.setStatus("current")


class _CdslMaxVcClasses_Type(Unsigned32):
    """Custom type cdslMaxVcClasses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslMaxVcClasses_Type.__name__ = "Unsigned32"
_CdslMaxVcClasses_Object = MibTableColumn
cdslMaxVcClasses = _CdslMaxVcClasses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 1, 1, 1),
    _CdslMaxVcClasses_Type()
)
cdslMaxVcClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslMaxVcClasses.setStatus("current")


class _CdslVcClasses_Type(Gauge32):
    """Custom type cdslVcClasses based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdslVcClasses_Type.__name__ = "Gauge32"
_CdslVcClasses_Object = MibTableColumn
cdslVcClasses = _CdslVcClasses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 1, 1, 2),
    _CdslVcClasses_Type()
)
cdslVcClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslVcClasses.setStatus("current")
_CdslVcClassTable_Object = MibTable
cdslVcClassTable = _CdslVcClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cdslVcClassTable.setStatus("current")
_CdslVcClassEntry_Object = MibTableRow
cdslVcClassEntry = _CdslVcClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1)
)
cdslVcClassEntry.setIndexNames(
    (0, "CISCO-DSL-PROVISION-MIB", "cdslNrpSlotIndex"),
    (1, "CISCO-DSL-PROVISION-MIB", "cdslVcClassName"),
)
if mibBuilder.loadTexts:
    cdslVcClassEntry.setStatus("current")


class _CdslVcClassName_Type(DisplayString):
    """Custom type cdslVcClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CdslVcClassName_Type.__name__ = "DisplayString"
_CdslVcClassName_Object = MibTableColumn
cdslVcClassName = _CdslVcClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 1),
    _CdslVcClassName_Type()
)
cdslVcClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdslVcClassName.setStatus("current")


class _CdslVcClassType_Type(Integer32):
    """Custom type cdslVcClassType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 1),
          ("funi", 2))
    )


_CdslVcClassType_Type.__name__ = "Integer32"
_CdslVcClassType_Object = MibTableColumn
cdslVcClassType = _CdslVcClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 2),
    _CdslVcClassType_Type()
)
cdslVcClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdslVcClassType.setStatus("current")


class _CdslVcClassQosType_Type(Integer32):
    """Custom type cdslVcClassQosType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abr", 6),
          ("cbr", 1),
          ("max", 7),
          ("ubr", 2),
          ("ubrDefault", 0),
          ("ubrPlus", 3),
          ("vbrNrt", 5),
          ("vbrRt", 4))
    )


_CdslVcClassQosType_Type.__name__ = "Integer32"
_CdslVcClassQosType_Object = MibTableColumn
cdslVcClassQosType = _CdslVcClassQosType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 3),
    _CdslVcClassQosType_Type()
)
cdslVcClassQosType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassQosType.setStatus("current")


class _CdslVcClassAbrPCR_Type(Integer32):
    """Custom type cdslVcClassAbrPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56, 155000),
    )


_CdslVcClassAbrPCR_Type.__name__ = "Integer32"
_CdslVcClassAbrPCR_Object = MibTableColumn
cdslVcClassAbrPCR = _CdslVcClassAbrPCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 4),
    _CdslVcClassAbrPCR_Type()
)
cdslVcClassAbrPCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassAbrPCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassAbrPCR.setUnits("kbps")


class _CdslVcClassAbrMcr_Type(Integer32):
    """Custom type cdslVcClassAbrMcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 155000),
    )


_CdslVcClassAbrMcr_Type.__name__ = "Integer32"
_CdslVcClassAbrMcr_Object = MibTableColumn
cdslVcClassAbrMcr = _CdslVcClassAbrMcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 5),
    _CdslVcClassAbrMcr_Type()
)
cdslVcClassAbrMcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassAbrMcr.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassAbrMcr.setUnits("kbps")


class _CdslVcClassAbrIORIF_Type(Integer32):
    """Custom type cdslVcClassAbrIORIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CdslVcClassAbrIORIF_Type.__name__ = "Integer32"
_CdslVcClassAbrIORIF_Object = MibTableColumn
cdslVcClassAbrIORIF = _CdslVcClassAbrIORIF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 6),
    _CdslVcClassAbrIORIF_Type()
)
cdslVcClassAbrIORIF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassAbrIORIF.setStatus("current")


class _CdslVcClassAbrIORDF_Type(Integer32):
    """Custom type cdslVcClassAbrIORDF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CdslVcClassAbrIORDF_Type.__name__ = "Integer32"
_CdslVcClassAbrIORDF_Object = MibTableColumn
cdslVcClassAbrIORDF = _CdslVcClassAbrIORDF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 7),
    _CdslVcClassAbrIORDF_Type()
)
cdslVcClassAbrIORDF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassAbrIORDF.setStatus("current")


class _CdslVcClassBroadcast_Type(Integer32):
    """Custom type cdslVcClassBroadcast based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_CdslVcClassBroadcast_Type.__name__ = "Integer32"
_CdslVcClassBroadcast_Object = MibTableColumn
cdslVcClassBroadcast = _CdslVcClassBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 8),
    _CdslVcClassBroadcast_Type()
)
cdslVcClassBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassBroadcast.setStatus("current")


class _CdslVcClassEncapsulation_Type(Integer32):
    """Custom type cdslVcClassEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aal34smds", 4),
          ("aal5ciscoppp", 7),
          ("aal5ilmi", 5),
          ("aal5mux", 2),
          ("aal5nlpid", 3),
          ("aal5qsaal", 6),
          ("aal5snap", 1),
          ("default", 0))
    )


_CdslVcClassEncapsulation_Type.__name__ = "Integer32"
_CdslVcClassEncapsulation_Object = MibTableColumn
cdslVcClassEncapsulation = _CdslVcClassEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 9),
    _CdslVcClassEncapsulation_Type()
)
cdslVcClassEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassEncapsulation.setStatus("current")


class _CdslVcClassMuxLinkType_Type(Integer32):
    """Custom type cdslVcClassMuxLinkType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ppp", 2))
    )


_CdslVcClassMuxLinkType_Type.__name__ = "Integer32"
_CdslVcClassMuxLinkType_Object = MibTableColumn
cdslVcClassMuxLinkType = _CdslVcClassMuxLinkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 10),
    _CdslVcClassMuxLinkType_Type()
)
cdslVcClassMuxLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassMuxLinkType.setStatus("current")


class _CdslVcClassVirtualTemplate_Type(Integer32):
    """Custom type cdslVcClassVirtualTemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdslVcClassVirtualTemplate_Type.__name__ = "Integer32"
_CdslVcClassVirtualTemplate_Object = MibTableColumn
cdslVcClassVirtualTemplate = _CdslVcClassVirtualTemplate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 11),
    _CdslVcClassVirtualTemplate_Type()
)
cdslVcClassVirtualTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassVirtualTemplate.setStatus("current")


class _CdslVcClassIdleTimeout_Type(Integer32):
    """Custom type cdslVcClassIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_CdslVcClassIdleTimeout_Type.__name__ = "Integer32"
_CdslVcClassIdleTimeout_Object = MibTableColumn
cdslVcClassIdleTimeout = _CdslVcClassIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 12),
    _CdslVcClassIdleTimeout_Type()
)
cdslVcClassIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassIdleTimeout.setStatus("current")


class _CdslVcClassIdleMTR_Type(Integer32):
    """Custom type cdslVcClassIdleMTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000),
    )


_CdslVcClassIdleMTR_Type.__name__ = "Integer32"
_CdslVcClassIdleMTR_Object = MibTableColumn
cdslVcClassIdleMTR = _CdslVcClassIdleMTR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 13),
    _CdslVcClassIdleMTR_Type()
)
cdslVcClassIdleMTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassIdleMTR.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassIdleMTR.setUnits("kbps")


class _CdslVcClassILMIManage_Type(Integer32):
    """Custom type cdslVcClassILMIManage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_CdslVcClassILMIManage_Type.__name__ = "Integer32"
_CdslVcClassILMIManage_Object = MibTableColumn
cdslVcClassILMIManage = _CdslVcClassILMIManage_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 14),
    _CdslVcClassILMIManage_Type()
)
cdslVcClassILMIManage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassILMIManage.setStatus("current")


class _CdslVcClassInarp_Type(Integer32):
    """Custom type cdslVcClassInarp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CdslVcClassInarp_Type.__name__ = "Integer32"
_CdslVcClassInarp_Object = MibTableColumn
cdslVcClassInarp = _CdslVcClassInarp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 15),
    _CdslVcClassInarp_Type()
)
cdslVcClassInarp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassInarp.setStatus("current")


class _CdslVcClassOamRetryUpCount_Type(Integer32):
    """Custom type cdslVcClassOamRetryUpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CdslVcClassOamRetryUpCount_Type.__name__ = "Integer32"
_CdslVcClassOamRetryUpCount_Object = MibTableColumn
cdslVcClassOamRetryUpCount = _CdslVcClassOamRetryUpCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 16),
    _CdslVcClassOamRetryUpCount_Type()
)
cdslVcClassOamRetryUpCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassOamRetryUpCount.setStatus("current")


class _CdslVcClassOamRetryDownCount_Type(Integer32):
    """Custom type cdslVcClassOamRetryDownCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CdslVcClassOamRetryDownCount_Type.__name__ = "Integer32"
_CdslVcClassOamRetryDownCount_Object = MibTableColumn
cdslVcClassOamRetryDownCount = _CdslVcClassOamRetryDownCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 17),
    _CdslVcClassOamRetryDownCount_Type()
)
cdslVcClassOamRetryDownCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassOamRetryDownCount.setStatus("current")


class _CdslVcClassOamPvcManaged_Type(Integer32):
    """Custom type cdslVcClassOamPvcManaged based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_CdslVcClassOamPvcManaged_Type.__name__ = "Integer32"
_CdslVcClassOamPvcManaged_Object = MibTableColumn
cdslVcClassOamPvcManaged = _CdslVcClassOamPvcManaged_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 18),
    _CdslVcClassOamPvcManaged_Type()
)
cdslVcClassOamPvcManaged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassOamPvcManaged.setStatus("current")


class _CdslVcClassOamPvcLF_Type(Integer32):
    """Custom type cdslVcClassOamPvcLF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CdslVcClassOamPvcLF_Type.__name__ = "Integer32"
_CdslVcClassOamPvcLF_Object = MibTableColumn
cdslVcClassOamPvcLF = _CdslVcClassOamPvcLF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 19),
    _CdslVcClassOamPvcLF_Type()
)
cdslVcClassOamPvcLF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassOamPvcLF.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassOamPvcLF.setUnits("seconds")


class _CdslVcClassOamSvcManaged_Type(Integer32):
    """Custom type cdslVcClassOamSvcManaged based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_CdslVcClassOamSvcManaged_Type.__name__ = "Integer32"
_CdslVcClassOamSvcManaged_Object = MibTableColumn
cdslVcClassOamSvcManaged = _CdslVcClassOamSvcManaged_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 20),
    _CdslVcClassOamSvcManaged_Type()
)
cdslVcClassOamSvcManaged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassOamSvcManaged.setStatus("current")


class _CdslVcClassOamSvcLF_Type(Integer32):
    """Custom type cdslVcClassOamSvcLF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CdslVcClassOamSvcLF_Type.__name__ = "Integer32"
_CdslVcClassOamSvcLF_Object = MibTableColumn
cdslVcClassOamSvcLF = _CdslVcClassOamSvcLF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 21),
    _CdslVcClassOamSvcLF_Type()
)
cdslVcClassOamSvcLF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassOamSvcLF.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassOamSvcLF.setUnits("seconds")
_CdslVcClassProtocolIpBC_Type = TruthValue
_CdslVcClassProtocolIpBC_Object = MibTableColumn
cdslVcClassProtocolIpBC = _CdslVcClassProtocolIpBC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 22),
    _CdslVcClassProtocolIpBC_Type()
)
cdslVcClassProtocolIpBC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassProtocolIpBC.setStatus("current")
_CdslVcClassProtocolIpxBC_Type = TruthValue
_CdslVcClassProtocolIpxBC_Object = MibTableColumn
cdslVcClassProtocolIpxBC = _CdslVcClassProtocolIpxBC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 23),
    _CdslVcClassProtocolIpxBC_Type()
)
cdslVcClassProtocolIpxBC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassProtocolIpxBC.setStatus("current")


class _CdslVcClassTransmitPriority_Type(Integer32):
    """Custom type cdslVcClassTransmitPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdslVcClassTransmitPriority_Type.__name__ = "Integer32"
_CdslVcClassTransmitPriority_Object = MibTableColumn
cdslVcClassTransmitPriority = _CdslVcClassTransmitPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 24),
    _CdslVcClassTransmitPriority_Type()
)
cdslVcClassTransmitPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassTransmitPriority.setStatus("current")


class _CdslVcClassUbrPCR_Type(Integer32):
    """Custom type cdslVcClassUbrPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 155000),
    )


_CdslVcClassUbrPCR_Type.__name__ = "Integer32"
_CdslVcClassUbrPCR_Object = MibTableColumn
cdslVcClassUbrPCR = _CdslVcClassUbrPCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 25),
    _CdslVcClassUbrPCR_Type()
)
cdslVcClassUbrPCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassUbrPCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassUbrPCR.setUnits("kbps")


class _CdslVcClassUbrInputPCR_Type(Integer32):
    """Custom type cdslVcClassUbrInputPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 155000),
    )


_CdslVcClassUbrInputPCR_Type.__name__ = "Integer32"
_CdslVcClassUbrInputPCR_Object = MibTableColumn
cdslVcClassUbrInputPCR = _CdslVcClassUbrInputPCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 26),
    _CdslVcClassUbrInputPCR_Type()
)
cdslVcClassUbrInputPCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassUbrInputPCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassUbrInputPCR.setUnits("kbps")


class _CdslVcClassUbrPlusPCR_Type(Integer32):
    """Custom type cdslVcClassUbrPlusPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 155000),
    )


_CdslVcClassUbrPlusPCR_Type.__name__ = "Integer32"
_CdslVcClassUbrPlusPCR_Object = MibTableColumn
cdslVcClassUbrPlusPCR = _CdslVcClassUbrPlusPCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 27),
    _CdslVcClassUbrPlusPCR_Type()
)
cdslVcClassUbrPlusPCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassUbrPlusPCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassUbrPlusPCR.setUnits("kbps")


class _CdslVcClassUbrPlusMCR_Type(Integer32):
    """Custom type cdslVcClassUbrPlusMCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000),
    )


_CdslVcClassUbrPlusMCR_Type.__name__ = "Integer32"
_CdslVcClassUbrPlusMCR_Object = MibTableColumn
cdslVcClassUbrPlusMCR = _CdslVcClassUbrPlusMCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 28),
    _CdslVcClassUbrPlusMCR_Type()
)
cdslVcClassUbrPlusMCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassUbrPlusMCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassUbrPlusMCR.setUnits("kbps")


class _CdslVcClassUbrPlusInputPCR_Type(Integer32):
    """Custom type cdslVcClassUbrPlusInputPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 155000),
    )


_CdslVcClassUbrPlusInputPCR_Type.__name__ = "Integer32"
_CdslVcClassUbrPlusInputPCR_Object = MibTableColumn
cdslVcClassUbrPlusInputPCR = _CdslVcClassUbrPlusInputPCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 29),
    _CdslVcClassUbrPlusInputPCR_Type()
)
cdslVcClassUbrPlusInputPCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassUbrPlusInputPCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassUbrPlusInputPCR.setUnits("kbps")


class _CdslVcClassUbrPlusInputMCR_Type(Integer32):
    """Custom type cdslVcClassUbrPlusInputMCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000),
    )


_CdslVcClassUbrPlusInputMCR_Type.__name__ = "Integer32"
_CdslVcClassUbrPlusInputMCR_Object = MibTableColumn
cdslVcClassUbrPlusInputMCR = _CdslVcClassUbrPlusInputMCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 30),
    _CdslVcClassUbrPlusInputMCR_Type()
)
cdslVcClassUbrPlusInputMCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassUbrPlusInputMCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassUbrPlusInputMCR.setUnits("kbps")


class _CdslVcClassVbrNrtPCR_Type(Integer32):
    """Custom type cdslVcClassVbrNrtPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 155000),
    )


_CdslVcClassVbrNrtPCR_Type.__name__ = "Integer32"
_CdslVcClassVbrNrtPCR_Object = MibTableColumn
cdslVcClassVbrNrtPCR = _CdslVcClassVbrNrtPCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 31),
    _CdslVcClassVbrNrtPCR_Type()
)
cdslVcClassVbrNrtPCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassVbrNrtPCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassVbrNrtPCR.setUnits("kbps")


class _CdslVcClassVbrNrtSCR_Type(Integer32):
    """Custom type cdslVcClassVbrNrtSCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CdslVcClassVbrNrtSCR_Type.__name__ = "Integer32"
_CdslVcClassVbrNrtSCR_Object = MibTableColumn
cdslVcClassVbrNrtSCR = _CdslVcClassVbrNrtSCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 32),
    _CdslVcClassVbrNrtSCR_Type()
)
cdslVcClassVbrNrtSCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassVbrNrtSCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassVbrNrtSCR.setUnits("kbps")


class _CdslVcClassVbrNrtInputBP_Type(Integer32):
    """Custom type cdslVcClassVbrNrtInputBP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_CdslVcClassVbrNrtInputBP_Type.__name__ = "Integer32"
_CdslVcClassVbrNrtInputBP_Object = MibTableColumn
cdslVcClassVbrNrtInputBP = _CdslVcClassVbrNrtInputBP_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 33),
    _CdslVcClassVbrNrtInputBP_Type()
)
cdslVcClassVbrNrtInputBP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassVbrNrtInputBP.setStatus("current")


class _CdslVcClassVbrNrtInputPCR_Type(Integer32):
    """Custom type cdslVcClassVbrNrtInputPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 155000),
    )


_CdslVcClassVbrNrtInputPCR_Type.__name__ = "Integer32"
_CdslVcClassVbrNrtInputPCR_Object = MibTableColumn
cdslVcClassVbrNrtInputPCR = _CdslVcClassVbrNrtInputPCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 34),
    _CdslVcClassVbrNrtInputPCR_Type()
)
cdslVcClassVbrNrtInputPCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassVbrNrtInputPCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassVbrNrtInputPCR.setUnits("kbps")


class _CdslVcClassVbrNrtInputSCR_Type(Integer32):
    """Custom type cdslVcClassVbrNrtInputSCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CdslVcClassVbrNrtInputSCR_Type.__name__ = "Integer32"
_CdslVcClassVbrNrtInputSCR_Object = MibTableColumn
cdslVcClassVbrNrtInputSCR = _CdslVcClassVbrNrtInputSCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 35),
    _CdslVcClassVbrNrtInputSCR_Type()
)
cdslVcClassVbrNrtInputSCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassVbrNrtInputSCR.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassVbrNrtInputSCR.setUnits("kbps")


class _CdslVcClassVbrNrtInputMBS_Type(Integer32):
    """Custom type cdslVcClassVbrNrtInputMBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_CdslVcClassVbrNrtInputMBS_Type.__name__ = "Integer32"
_CdslVcClassVbrNrtInputMBS_Object = MibTableColumn
cdslVcClassVbrNrtInputMBS = _CdslVcClassVbrNrtInputMBS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 36),
    _CdslVcClassVbrNrtInputMBS_Type()
)
cdslVcClassVbrNrtInputMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassVbrNrtInputMBS.setStatus("current")
if mibBuilder.loadTexts:
    cdslVcClassVbrNrtInputMBS.setUnits("cells")


class _CdslVcClassRowStatus_Type(RowStatus):
    """Custom type cdslVcClassRowStatus based on RowStatus"""


_CdslVcClassRowStatus_Object = MibTableColumn
cdslVcClassRowStatus = _CdslVcClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 1, 5, 2, 1, 37),
    _CdslVcClassRowStatus_Type()
)
cdslVcClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdslVcClassRowStatus.setStatus("current")
_CiscoDslProvMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoDslProvMIBNotificationPrefix = _CiscoDslProvMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 2)
)
_CiscoDslProvMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDslProvMIBConformance = _CiscoDslProvMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 3)
)
_CiscoDslProvMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDslProvMIBCompliances = _CiscoDslProvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 3, 1)
)
_CiscoDslProvMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDslProvMIBGroups = _CiscoDslProvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 3, 2)
)

# Managed Objects groups

ciscoNrpSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 3, 2, 1)
)
ciscoNrpSlotGroup.setObjects(
      *(("CISCO-DSL-PROVISION-MIB", "cdslMaxNrps"),
        ("CISCO-DSL-PROVISION-MIB", "cdslNrpNumber"),
        ("CISCO-DSL-PROVISION-MIB", "cdslNrpIpAddress"))
)
if mibBuilder.loadTexts:
    ciscoNrpSlotGroup.setStatus("current")

ciscoVirtualTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 3, 2, 2)
)
ciscoVirtualTemplateGroup.setObjects(
      *(("CISCO-DSL-PROVISION-MIB", "cdslMaxVirtualTemplates"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVirtualTemplates"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTIpAddressMethod"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTIpAddress"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTIpAddressMask"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTIpIfIndex"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPeerIpAddressMethod"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPeerIpAddrPool"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPppAuthPap"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPppAuthChap"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPppAuthMSChap"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPppChapHost"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPppChapPassword"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPppChapEncrypType"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPppChapRefuse"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPppChapWaitPeer"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPppPapUserName"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPppPapPassword"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPppPapEncrypType"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTPppUseTacacs"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVTRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoVirtualTemplateGroup.setStatus("current")

ciscoIpPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 3, 2, 3)
)
ciscoIpPoolGroup.setObjects(
      *(("CISCO-DSL-PROVISION-MIB", "cdslLocalIpAddrPools"),
        ("CISCO-DSL-PROVISION-MIB", "cdslMaxLocalIpAddrPools"),
        ("CISCO-DSL-PROVISION-MIB", "cdslLocalIpAddrPoolFreeAddresses"),
        ("CISCO-DSL-PROVISION-MIB", "cdslLocalIpAddrPoolInUseAddresses"),
        ("CISCO-DSL-PROVISION-MIB", "cdslLocalIpAddrRangeRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpPoolGroup.setStatus("current")

ciscoDslPVCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 3, 2, 4)
)
ciscoDslPVCGroup.setObjects(
      *(("CISCO-DSL-PROVISION-MIB", "cdslPppOverAtmPvcs"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcName"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcSubIfNumber"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcClass"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcAbrPCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcAbrIORIF"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcAbrIORDF"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcBroadcast"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcEncapsulation"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcMuxLinkType"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcILMIManage"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcInarp"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcOamRetryUpCount"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcOamRetryDownCount"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcOamPvcManaged"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcOamPvcLF"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcProtocolIpBC"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcProtocolIpxBC"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcUbrPCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcUbrPlusPCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcUbrPlusMCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcVbrNrtPCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcVbrNrtSCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcVirtualTemplate"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcRowStatus"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcQosType"),
        ("CISCO-DSL-PROVISION-MIB", "cdslAtmPvcAbrMCR"))
)
if mibBuilder.loadTexts:
    ciscoDslPVCGroup.setStatus("current")

ciscoVcClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 3, 2, 5)
)
ciscoVcClassGroup.setObjects(
      *(("CISCO-DSL-PROVISION-MIB", "cdslVcClasses"),
        ("CISCO-DSL-PROVISION-MIB", "cdslMaxVcClasses"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassType"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassQosType"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassAbrPCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassAbrMcr"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassAbrIORIF"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassAbrIORDF"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassBroadcast"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassEncapsulation"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassMuxLinkType"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassIdleTimeout"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassIdleMTR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassILMIManage"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassInarp"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassOamRetryUpCount"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassOamRetryDownCount"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassOamPvcManaged"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassOamPvcLF"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassOamSvcManaged"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassOamSvcLF"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassProtocolIpBC"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassProtocolIpxBC"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassTransmitPriority"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassUbrPCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassUbrInputPCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassUbrPlusPCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassUbrPlusMCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassUbrPlusInputPCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassUbrPlusInputMCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassVbrNrtPCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassVbrNrtSCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassVbrNrtInputBP"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassVbrNrtInputPCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassVbrNrtInputSCR"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassVbrNrtInputMBS"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassVirtualTemplate"),
        ("CISCO-DSL-PROVISION-MIB", "cdslVcClassRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoVcClassGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDslProvMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 30, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDslProvMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DSL-PROVISION-MIB",
    **{"ciscoDslProvisionMIB": ciscoDslProvisionMIB,
       "ciscoDslProvMIBObjects": ciscoDslProvMIBObjects,
       "cdslNrpSlot": cdslNrpSlot,
       "cdslMaxNrps": cdslMaxNrps,
       "cdslNrpNumber": cdslNrpNumber,
       "cdslNrpIpAddressTable": cdslNrpIpAddressTable,
       "cdslNrpIpAddressEntry": cdslNrpIpAddressEntry,
       "cdslNrpSlotIndex": cdslNrpSlotIndex,
       "cdslNrpIpAddress": cdslNrpIpAddress,
       "cdslVirtualTemplate": cdslVirtualTemplate,
       "cdslVirtualTemplateNumberTable": cdslVirtualTemplateNumberTable,
       "cdslVirtualTemplateNumberEntry": cdslVirtualTemplateNumberEntry,
       "cdslMaxVirtualTemplates": cdslMaxVirtualTemplates,
       "cdslVirtualTemplates": cdslVirtualTemplates,
       "cdslVirtualTemplateTable": cdslVirtualTemplateTable,
       "cdslVirtualTemplateEntry": cdslVirtualTemplateEntry,
       "cdslVTIndex": cdslVTIndex,
       "cdslVTIpAddressMethod": cdslVTIpAddressMethod,
       "cdslVTIpAddress": cdslVTIpAddress,
       "cdslVTIpAddressMask": cdslVTIpAddressMask,
       "cdslVTIpIfIndex": cdslVTIpIfIndex,
       "cdslVTPeerIpAddressMethod": cdslVTPeerIpAddressMethod,
       "cdslVTPeerIpAddrPool": cdslVTPeerIpAddrPool,
       "cdslVTPppAuthChap": cdslVTPppAuthChap,
       "cdslVTPppAuthMSChap": cdslVTPppAuthMSChap,
       "cdslVTPppAuthPap": cdslVTPppAuthPap,
       "cdslVTPppChapHost": cdslVTPppChapHost,
       "cdslVTPppChapPassword": cdslVTPppChapPassword,
       "cdslVTPppChapEncrypType": cdslVTPppChapEncrypType,
       "cdslVTPppChapRefuse": cdslVTPppChapRefuse,
       "cdslVTPppChapWaitPeer": cdslVTPppChapWaitPeer,
       "cdslVTPppPapUserName": cdslVTPppPapUserName,
       "cdslVTPppPapPassword": cdslVTPppPapPassword,
       "cdslVTPppPapEncrypType": cdslVTPppPapEncrypType,
       "cdslVTPppUseTacacs": cdslVTPppUseTacacs,
       "cdslVTRowStatus": cdslVTRowStatus,
       "cdslLocalIpAddrPool": cdslLocalIpAddrPool,
       "cdslLocalIpAddrPoolNumberTable": cdslLocalIpAddrPoolNumberTable,
       "cdslLocalIpAddrPoolNumberEntry": cdslLocalIpAddrPoolNumberEntry,
       "cdslMaxLocalIpAddrPools": cdslMaxLocalIpAddrPools,
       "cdslLocalIpAddrPools": cdslLocalIpAddrPools,
       "cdslLocalIpAddrPoolTable": cdslLocalIpAddrPoolTable,
       "cdslLocalIpAddrPoolEntry": cdslLocalIpAddrPoolEntry,
       "cdslLocalIpAddrPoolName": cdslLocalIpAddrPoolName,
       "cdslLocalIpAddrPoolFreeAddresses": cdslLocalIpAddrPoolFreeAddresses,
       "cdslLocalIpAddrPoolInUseAddresses": cdslLocalIpAddrPoolInUseAddresses,
       "cdslLocalIpAddrRangeTable": cdslLocalIpAddrRangeTable,
       "cdslLocalIpAddrRangeEntry": cdslLocalIpAddrRangeEntry,
       "cdslLocalIpAddrRangeLowAddr": cdslLocalIpAddrRangeLowAddr,
       "cdslLocalIpAddrRangeHighAddr": cdslLocalIpAddrRangeHighAddr,
       "cdslLocalIpAddrRangeRowStatus": cdslLocalIpAddrRangeRowStatus,
       "cdslAtmPvc": cdslAtmPvc,
       "cdslPppOverAtmPvcNumberTable": cdslPppOverAtmPvcNumberTable,
       "cdslPppOverAtmPvcNumberEntry": cdslPppOverAtmPvcNumberEntry,
       "cdslPppOverAtmPvcs": cdslPppOverAtmPvcs,
       "cdslAtmPvcTable": cdslAtmPvcTable,
       "cdslAtmPvcEntry": cdslAtmPvcEntry,
       "cdslAtmPvcVpi": cdslAtmPvcVpi,
       "cdslAtmPvcVci": cdslAtmPvcVci,
       "cdslAtmPvcName": cdslAtmPvcName,
       "cdslAtmPvcSubIfNumber": cdslAtmPvcSubIfNumber,
       "cdslAtmPvcClass": cdslAtmPvcClass,
       "cdslAtmPvcQosType": cdslAtmPvcQosType,
       "cdslAtmPvcAbrPCR": cdslAtmPvcAbrPCR,
       "cdslAtmPvcAbrMCR": cdslAtmPvcAbrMCR,
       "cdslAtmPvcAbrIORIF": cdslAtmPvcAbrIORIF,
       "cdslAtmPvcAbrIORDF": cdslAtmPvcAbrIORDF,
       "cdslAtmPvcBroadcast": cdslAtmPvcBroadcast,
       "cdslAtmPvcEncapsulation": cdslAtmPvcEncapsulation,
       "cdslAtmPvcMuxLinkType": cdslAtmPvcMuxLinkType,
       "cdslAtmPvcVirtualTemplate": cdslAtmPvcVirtualTemplate,
       "cdslAtmPvcILMIManage": cdslAtmPvcILMIManage,
       "cdslAtmPvcInarp": cdslAtmPvcInarp,
       "cdslAtmPvcOamRetryUpCount": cdslAtmPvcOamRetryUpCount,
       "cdslAtmPvcOamRetryDownCount": cdslAtmPvcOamRetryDownCount,
       "cdslAtmPvcOamPvcManaged": cdslAtmPvcOamPvcManaged,
       "cdslAtmPvcOamPvcLF": cdslAtmPvcOamPvcLF,
       "cdslAtmPvcProtocolIpBC": cdslAtmPvcProtocolIpBC,
       "cdslAtmPvcProtocolIpxBC": cdslAtmPvcProtocolIpxBC,
       "cdslAtmPvcUbrPCR": cdslAtmPvcUbrPCR,
       "cdslAtmPvcUbrPlusPCR": cdslAtmPvcUbrPlusPCR,
       "cdslAtmPvcUbrPlusMCR": cdslAtmPvcUbrPlusMCR,
       "cdslAtmPvcVbrNrtPCR": cdslAtmPvcVbrNrtPCR,
       "cdslAtmPvcVbrNrtSCR": cdslAtmPvcVbrNrtSCR,
       "cdslAtmPvcRowStatus": cdslAtmPvcRowStatus,
       "cdslVcClass": cdslVcClass,
       "cdslVcClassNumberTable": cdslVcClassNumberTable,
       "cdslVcClassNumberEntry": cdslVcClassNumberEntry,
       "cdslMaxVcClasses": cdslMaxVcClasses,
       "cdslVcClasses": cdslVcClasses,
       "cdslVcClassTable": cdslVcClassTable,
       "cdslVcClassEntry": cdslVcClassEntry,
       "cdslVcClassName": cdslVcClassName,
       "cdslVcClassType": cdslVcClassType,
       "cdslVcClassQosType": cdslVcClassQosType,
       "cdslVcClassAbrPCR": cdslVcClassAbrPCR,
       "cdslVcClassAbrMcr": cdslVcClassAbrMcr,
       "cdslVcClassAbrIORIF": cdslVcClassAbrIORIF,
       "cdslVcClassAbrIORDF": cdslVcClassAbrIORDF,
       "cdslVcClassBroadcast": cdslVcClassBroadcast,
       "cdslVcClassEncapsulation": cdslVcClassEncapsulation,
       "cdslVcClassMuxLinkType": cdslVcClassMuxLinkType,
       "cdslVcClassVirtualTemplate": cdslVcClassVirtualTemplate,
       "cdslVcClassIdleTimeout": cdslVcClassIdleTimeout,
       "cdslVcClassIdleMTR": cdslVcClassIdleMTR,
       "cdslVcClassILMIManage": cdslVcClassILMIManage,
       "cdslVcClassInarp": cdslVcClassInarp,
       "cdslVcClassOamRetryUpCount": cdslVcClassOamRetryUpCount,
       "cdslVcClassOamRetryDownCount": cdslVcClassOamRetryDownCount,
       "cdslVcClassOamPvcManaged": cdslVcClassOamPvcManaged,
       "cdslVcClassOamPvcLF": cdslVcClassOamPvcLF,
       "cdslVcClassOamSvcManaged": cdslVcClassOamSvcManaged,
       "cdslVcClassOamSvcLF": cdslVcClassOamSvcLF,
       "cdslVcClassProtocolIpBC": cdslVcClassProtocolIpBC,
       "cdslVcClassProtocolIpxBC": cdslVcClassProtocolIpxBC,
       "cdslVcClassTransmitPriority": cdslVcClassTransmitPriority,
       "cdslVcClassUbrPCR": cdslVcClassUbrPCR,
       "cdslVcClassUbrInputPCR": cdslVcClassUbrInputPCR,
       "cdslVcClassUbrPlusPCR": cdslVcClassUbrPlusPCR,
       "cdslVcClassUbrPlusMCR": cdslVcClassUbrPlusMCR,
       "cdslVcClassUbrPlusInputPCR": cdslVcClassUbrPlusInputPCR,
       "cdslVcClassUbrPlusInputMCR": cdslVcClassUbrPlusInputMCR,
       "cdslVcClassVbrNrtPCR": cdslVcClassVbrNrtPCR,
       "cdslVcClassVbrNrtSCR": cdslVcClassVbrNrtSCR,
       "cdslVcClassVbrNrtInputBP": cdslVcClassVbrNrtInputBP,
       "cdslVcClassVbrNrtInputPCR": cdslVcClassVbrNrtInputPCR,
       "cdslVcClassVbrNrtInputSCR": cdslVcClassVbrNrtInputSCR,
       "cdslVcClassVbrNrtInputMBS": cdslVcClassVbrNrtInputMBS,
       "cdslVcClassRowStatus": cdslVcClassRowStatus,
       "ciscoDslProvMIBNotificationPrefix": ciscoDslProvMIBNotificationPrefix,
       "ciscoDslProvMIBConformance": ciscoDslProvMIBConformance,
       "ciscoDslProvMIBCompliances": ciscoDslProvMIBCompliances,
       "ciscoDslProvMIBBasicCompliance": ciscoDslProvMIBBasicCompliance,
       "ciscoDslProvMIBGroups": ciscoDslProvMIBGroups,
       "ciscoNrpSlotGroup": ciscoNrpSlotGroup,
       "ciscoVirtualTemplateGroup": ciscoVirtualTemplateGroup,
       "ciscoIpPoolGroup": ciscoIpPoolGroup,
       "ciscoDslPVCGroup": ciscoDslPVCGroup,
       "ciscoVcClassGroup": ciscoVcClassGroup}
)
