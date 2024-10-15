# SNMP MIB module (XYLAN-AVL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-AVL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:55 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xylanAVLArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanAVLArch")


# MODULE-IDENTITY


# Types definitions



class XylanAVLtelportStatCodes(Integer32):
    """Custom type XylanAVLtelportStatCodes based on Integer32"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanAVLConfig_ObjectIdentity = ObjectIdentity
xylanAVLConfig = _XylanAVLConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1)
)
_XylanAVLloginbanner_Type = DisplayString
_XylanAVLloginbanner_Object = MibScalar
xylanAVLloginbanner = _XylanAVLloginbanner_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 1),
    _XylanAVLloginbanner_Type()
)
xylanAVLloginbanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLloginbanner.setStatus("mandatory")
_XylanAVLTproxyports_Object = MibTable
xylanAVLTproxyports = _XylanAVLTproxyports_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 2)
)
if mibBuilder.loadTexts:
    xylanAVLTproxyports.setStatus("mandatory")
_XylanAVLTproxyentry_Object = MibTableRow
xylanAVLTproxyentry = _XylanAVLTproxyentry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 2, 1)
)
xylanAVLTproxyentry.setIndexNames(
    (0, "XYLAN-AVL-MIB", "xylanAVLTproxyIntfAddr"),
)
if mibBuilder.loadTexts:
    xylanAVLTproxyentry.setStatus("mandatory")
_XylanAVLTproxyIntfAddr_Type = IpAddress
_XylanAVLTproxyIntfAddr_Object = MibTableColumn
xylanAVLTproxyIntfAddr = _XylanAVLTproxyIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 2, 1, 1),
    _XylanAVLTproxyIntfAddr_Type()
)
xylanAVLTproxyIntfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLTproxyIntfAddr.setStatus("mandatory")
_XylanAVLTproxyProxyAddr_Type = IpAddress
_XylanAVLTproxyProxyAddr_Object = MibTableColumn
xylanAVLTproxyProxyAddr = _XylanAVLTproxyProxyAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 2, 1, 2),
    _XylanAVLTproxyProxyAddr_Type()
)
xylanAVLTproxyProxyAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLTproxyProxyAddr.setStatus("mandatory")
_XylanAVLtelports_Object = MibTable
xylanAVLtelports = _XylanAVLtelports_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 3)
)
if mibBuilder.loadTexts:
    xylanAVLtelports.setStatus("mandatory")
_XylanAVLtelportentry_Object = MibTableRow
xylanAVLtelportentry = _XylanAVLtelportentry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 3, 1)
)
xylanAVLtelportentry.setIndexNames(
    (0, "XYLAN-AVL-MIB", "xylanAVLtelportslot"),
    (0, "XYLAN-AVL-MIB", "xylanAVLtelportport"),
)
if mibBuilder.loadTexts:
    xylanAVLtelportentry.setStatus("mandatory")
_XylanAVLtelportslot_Type = Integer32
_XylanAVLtelportslot_Object = MibTableColumn
xylanAVLtelportslot = _XylanAVLtelportslot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 3, 1, 1),
    _XylanAVLtelportslot_Type()
)
xylanAVLtelportslot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLtelportslot.setStatus("mandatory")
_XylanAVLtelportport_Type = Integer32
_XylanAVLtelportport_Object = MibTableColumn
xylanAVLtelportport = _XylanAVLtelportport_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 3, 1, 2),
    _XylanAVLtelportport_Type()
)
xylanAVLtelportport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLtelportport.setStatus("mandatory")
_XylanAVLtelportstat_Type = XylanAVLtelportStatCodes
_XylanAVLtelportstat_Object = MibTableColumn
xylanAVLtelportstat = _XylanAVLtelportstat_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 3, 1, 3),
    _XylanAVLtelportstat_Type()
)
xylanAVLtelportstat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLtelportstat.setStatus("mandatory")
_XylanAVLoptionprompt_Type = DisplayString
_XylanAVLoptionprompt_Object = MibScalar
xylanAVLoptionprompt = _XylanAVLoptionprompt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 4),
    _XylanAVLoptionprompt_Type()
)
xylanAVLoptionprompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLoptionprompt.setStatus("mandatory")
_XylanAVLgroupprompt_Type = DisplayString
_XylanAVLgroupprompt_Object = MibScalar
xylanAVLgroupprompt = _XylanAVLgroupprompt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 5),
    _XylanAVLgroupprompt_Type()
)
xylanAVLgroupprompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLgroupprompt.setStatus("mandatory")
_XylanAVLuserprompt_Type = DisplayString
_XylanAVLuserprompt_Object = MibScalar
xylanAVLuserprompt = _XylanAVLuserprompt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 6),
    _XylanAVLuserprompt_Type()
)
xylanAVLuserprompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLuserprompt.setStatus("mandatory")
_XylanAVLpassprompt_Type = DisplayString
_XylanAVLpassprompt_Object = MibScalar
xylanAVLpassprompt = _XylanAVLpassprompt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 7),
    _XylanAVLpassprompt_Type()
)
xylanAVLpassprompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLpassprompt.setStatus("mandatory")
_XylanAVLchalprompt_Type = DisplayString
_XylanAVLchalprompt_Object = MibScalar
xylanAVLchalprompt = _XylanAVLchalprompt_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 8),
    _XylanAVLchalprompt_Type()
)
xylanAVLchalprompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLchalprompt.setStatus("mandatory")
_XylanAVLsucceedmsg_Type = DisplayString
_XylanAVLsucceedmsg_Object = MibScalar
xylanAVLsucceedmsg = _XylanAVLsucceedmsg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 9),
    _XylanAVLsucceedmsg_Type()
)
xylanAVLsucceedmsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLsucceedmsg.setStatus("mandatory")
_XylanAVLfailmsg_Type = DisplayString
_XylanAVLfailmsg_Object = MibScalar
xylanAVLfailmsg = _XylanAVLfailmsg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 10),
    _XylanAVLfailmsg_Type()
)
xylanAVLfailmsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLfailmsg.setStatus("mandatory")


class _XylanAVLauthmode_Type(Integer32):
    """Custom type xylanAVLauthmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiple-authority", 2),
          ("single-authority", 1))
    )


_XylanAVLauthmode_Type.__name__ = "Integer32"
_XylanAVLauthmode_Object = MibScalar
xylanAVLauthmode = _XylanAVLauthmode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 11),
    _XylanAVLauthmode_Type()
)
xylanAVLauthmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLauthmode.setStatus("mandatory")
_XylanAVLtimeout_Type = Integer32
_XylanAVLtimeout_Object = MibScalar
xylanAVLtimeout = _XylanAVLtimeout_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 12),
    _XylanAVLtimeout_Type()
)
xylanAVLtimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLtimeout.setStatus("mandatory")
_XylanAVLRadiusServers_Object = MibTable
xylanAVLRadiusServers = _XylanAVLRadiusServers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13)
)
if mibBuilder.loadTexts:
    xylanAVLRadiusServers.setStatus("mandatory")
_XylanAVLradiusentry_Object = MibTableRow
xylanAVLradiusentry = _XylanAVLradiusentry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1)
)
xylanAVLradiusentry.setIndexNames(
    (0, "XYLAN-AVL-MIB", "xylanAVLRadiusAddress"),
    (0, "XYLAN-AVL-MIB", "xylanAVLRadiusGroup"),
)
if mibBuilder.loadTexts:
    xylanAVLradiusentry.setStatus("mandatory")
_XylanAVLRadiusGroup_Type = Integer32
_XylanAVLRadiusGroup_Object = MibTableColumn
xylanAVLRadiusGroup = _XylanAVLRadiusGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1, 1),
    _XylanAVLRadiusGroup_Type()
)
xylanAVLRadiusGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLRadiusGroup.setStatus("mandatory")
_XylanAVLRadiusAddress_Type = IpAddress
_XylanAVLRadiusAddress_Object = MibTableColumn
xylanAVLRadiusAddress = _XylanAVLRadiusAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1, 2),
    _XylanAVLRadiusAddress_Type()
)
xylanAVLRadiusAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLRadiusAddress.setStatus("mandatory")


class _XylanAVLRadiusPriority_Type(Integer32):
    """Custom type xylanAVLRadiusPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XylanAVLRadiusPriority_Type.__name__ = "Integer32"
_XylanAVLRadiusPriority_Object = MibTableColumn
xylanAVLRadiusPriority = _XylanAVLRadiusPriority_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1, 3),
    _XylanAVLRadiusPriority_Type()
)
xylanAVLRadiusPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLRadiusPriority.setStatus("mandatory")
_XylanAVLRadiusPort_Type = Integer32
_XylanAVLRadiusPort_Object = MibTableColumn
xylanAVLRadiusPort = _XylanAVLRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1, 4),
    _XylanAVLRadiusPort_Type()
)
xylanAVLRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLRadiusPort.setStatus("mandatory")
_XylanAVLRadiusSecret_Type = DisplayString
_XylanAVLRadiusSecret_Object = MibTableColumn
xylanAVLRadiusSecret = _XylanAVLRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1, 5),
    _XylanAVLRadiusSecret_Type()
)
xylanAVLRadiusSecret.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    xylanAVLRadiusSecret.setStatus("mandatory")


class _XylanAVLRadiusAdminState_Type(Integer32):
    """Custom type xylanAVLRadiusAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanAVLRadiusAdminState_Type.__name__ = "Integer32"
_XylanAVLRadiusAdminState_Object = MibTableColumn
xylanAVLRadiusAdminState = _XylanAVLRadiusAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1, 6),
    _XylanAVLRadiusAdminState_Type()
)
xylanAVLRadiusAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLRadiusAdminState.setStatus("mandatory")
_XylanAVLRadiusAcctServers_Object = MibTable
xylanAVLRadiusAcctServers = _XylanAVLRadiusAcctServers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14)
)
if mibBuilder.loadTexts:
    xylanAVLRadiusAcctServers.setStatus("mandatory")
_XylanAVLradiusacctentry_Object = MibTableRow
xylanAVLradiusacctentry = _XylanAVLradiusacctentry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1)
)
xylanAVLradiusacctentry.setIndexNames(
    (0, "XYLAN-AVL-MIB", "xylanAVLRadiusAcctAddress"),
    (0, "XYLAN-AVL-MIB", "xylanAVLRadiusAcctGroup"),
)
if mibBuilder.loadTexts:
    xylanAVLradiusacctentry.setStatus("mandatory")
_XylanAVLRadiusAcctGroup_Type = Integer32
_XylanAVLRadiusAcctGroup_Object = MibTableColumn
xylanAVLRadiusAcctGroup = _XylanAVLRadiusAcctGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1, 1),
    _XylanAVLRadiusAcctGroup_Type()
)
xylanAVLRadiusAcctGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLRadiusAcctGroup.setStatus("mandatory")
_XylanAVLRadiusAcctAddress_Type = IpAddress
_XylanAVLRadiusAcctAddress_Object = MibTableColumn
xylanAVLRadiusAcctAddress = _XylanAVLRadiusAcctAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1, 2),
    _XylanAVLRadiusAcctAddress_Type()
)
xylanAVLRadiusAcctAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLRadiusAcctAddress.setStatus("mandatory")


class _XylanAVLRadiusAcctPri_Type(Integer32):
    """Custom type xylanAVLRadiusAcctPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XylanAVLRadiusAcctPri_Type.__name__ = "Integer32"
_XylanAVLRadiusAcctPri_Object = MibTableColumn
xylanAVLRadiusAcctPri = _XylanAVLRadiusAcctPri_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1, 3),
    _XylanAVLRadiusAcctPri_Type()
)
xylanAVLRadiusAcctPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLRadiusAcctPri.setStatus("mandatory")
_XylanAVLRadiusAcctPort_Type = Integer32
_XylanAVLRadiusAcctPort_Object = MibTableColumn
xylanAVLRadiusAcctPort = _XylanAVLRadiusAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1, 4),
    _XylanAVLRadiusAcctPort_Type()
)
xylanAVLRadiusAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLRadiusAcctPort.setStatus("mandatory")
_XylanAVLRadiusAcctSecret_Type = DisplayString
_XylanAVLRadiusAcctSecret_Object = MibTableColumn
xylanAVLRadiusAcctSecret = _XylanAVLRadiusAcctSecret_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1, 5),
    _XylanAVLRadiusAcctSecret_Type()
)
xylanAVLRadiusAcctSecret.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    xylanAVLRadiusAcctSecret.setStatus("mandatory")


class _XylanAVLRadiusAcctAdminState_Type(Integer32):
    """Custom type xylanAVLRadiusAcctAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanAVLRadiusAcctAdminState_Type.__name__ = "Integer32"
_XylanAVLRadiusAcctAdminState_Object = MibTableColumn
xylanAVLRadiusAcctAdminState = _XylanAVLRadiusAcctAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1, 6),
    _XylanAVLRadiusAcctAdminState_Type()
)
xylanAVLRadiusAcctAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLRadiusAcctAdminState.setStatus("mandatory")
_XylanAVLlastuser_Type = DisplayString
_XylanAVLlastuser_Object = MibScalar
xylanAVLlastuser = _XylanAVLlastuser_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 16),
    _XylanAVLlastuser_Type()
)
xylanAVLlastuser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanAVLlastuser.setStatus("mandatory")


class _XylanAVLlastauthevent_Type(Integer32):
    """Custom type xylanAVLlastauthevent based on Integer32"""
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
          ("logout", 3),
          ("success", 1))
    )


_XylanAVLlastauthevent_Type.__name__ = "Integer32"
_XylanAVLlastauthevent_Object = MibScalar
xylanAVLlastauthevent = _XylanAVLlastauthevent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 17),
    _XylanAVLlastauthevent_Type()
)
xylanAVLlastauthevent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanAVLlastauthevent.setStatus("mandatory")
_XylanAVLlastauthmac_Type = MacAddress
_XylanAVLlastauthmac_Object = MibScalar
xylanAVLlastauthmac = _XylanAVLlastauthmac_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 18),
    _XylanAVLlastauthmac_Type()
)
xylanAVLlastauthmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanAVLlastauthmac.setStatus("mandatory")
_XylanAVLlastport_Type = Integer32
_XylanAVLlastport_Object = MibScalar
xylanAVLlastport = _XylanAVLlastport_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 19),
    _XylanAVLlastport_Type()
)
xylanAVLlastport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanAVLlastport.setStatus("mandatory")
_XylanAVLlastslot_Type = Integer32
_XylanAVLlastslot_Object = MibScalar
xylanAVLlastslot = _XylanAVLlastslot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 20),
    _XylanAVLlastslot_Type()
)
xylanAVLlastslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanAVLlastslot.setStatus("mandatory")
_XylanAVLversion_Type = DisplayString
_XylanAVLversion_Object = MibScalar
xylanAVLversion = _XylanAVLversion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 21),
    _XylanAVLversion_Type()
)
xylanAVLversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanAVLversion.setStatus("mandatory")
_XylanAVLdropmac_Type = MacAddress
_XylanAVLdropmac_Object = MibScalar
xylanAVLdropmac = _XylanAVLdropmac_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 22),
    _XylanAVLdropmac_Type()
)
xylanAVLdropmac.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    xylanAVLdropmac.setStatus("mandatory")
_XylanAVLradretries_Type = Integer32
_XylanAVLradretries_Object = MibScalar
xylanAVLradretries = _XylanAVLradretries_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 23),
    _XylanAVLradretries_Type()
)
xylanAVLradretries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLradretries.setStatus("mandatory")
_XylanAVLradtimeout_Type = Integer32
_XylanAVLradtimeout_Object = MibScalar
xylanAVLradtimeout = _XylanAVLradtimeout_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 24),
    _XylanAVLradtimeout_Type()
)
xylanAVLradtimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLradtimeout.setStatus("mandatory")
_XylanAVLBootpIfAddr_Type = IpAddress
_XylanAVLBootpIfAddr_Object = MibScalar
xylanAVLBootpIfAddr = _XylanAVLBootpIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 25),
    _XylanAVLBootpIfAddr_Type()
)
xylanAVLBootpIfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLBootpIfAddr.setStatus("mandatory")
_XylanAVLDNSName_Type = DisplayString
_XylanAVLDNSName_Object = MibScalar
xylanAVLDNSName = _XylanAVLDNSName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 26),
    _XylanAVLDNSName_Type()
)
xylanAVLDNSName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLDNSName.setStatus("mandatory")
_XylanAVLPathRestriction_Type = DisplayString
_XylanAVLPathRestriction_Object = MibScalar
xylanAVLPathRestriction = _XylanAVLPathRestriction_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 27),
    _XylanAVLPathRestriction_Type()
)
xylanAVLPathRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLPathRestriction.setStatus("mandatory")
_XylanAVLLdapServers_Object = MibTable
xylanAVLLdapServers = _XylanAVLLdapServers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28)
)
if mibBuilder.loadTexts:
    xylanAVLLdapServers.setStatus("mandatory")
_XylanAVLLdapentry_Object = MibTableRow
xylanAVLLdapentry = _XylanAVLLdapentry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1)
)
xylanAVLLdapentry.setIndexNames(
    (0, "XYLAN-AVL-MIB", "xylanAVLLdapGroup"),
)
if mibBuilder.loadTexts:
    xylanAVLLdapentry.setStatus("mandatory")
_XylanAVLLdapGroup_Type = Integer32
_XylanAVLLdapGroup_Object = MibTableColumn
xylanAVLLdapGroup = _XylanAVLLdapGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 1),
    _XylanAVLLdapGroup_Type()
)
xylanAVLLdapGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLLdapGroup.setStatus("mandatory")
_XylanAVLLdapUserId_Type = DisplayString
_XylanAVLLdapUserId_Object = MibTableColumn
xylanAVLLdapUserId = _XylanAVLLdapUserId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 2),
    _XylanAVLLdapUserId_Type()
)
xylanAVLLdapUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLLdapUserId.setStatus("mandatory")
_XylanAVLLdapUserPassword_Type = DisplayString
_XylanAVLLdapUserPassword_Object = MibTableColumn
xylanAVLLdapUserPassword = _XylanAVLLdapUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 3),
    _XylanAVLLdapUserPassword_Type()
)
xylanAVLLdapUserPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    xylanAVLLdapUserPassword.setStatus("mandatory")
_XylanAVLLdapSearchBase_Type = DisplayString
_XylanAVLLdapSearchBase_Object = MibTableColumn
xylanAVLLdapSearchBase = _XylanAVLLdapSearchBase_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 4),
    _XylanAVLLdapSearchBase_Type()
)
xylanAVLLdapSearchBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLLdapSearchBase.setStatus("mandatory")
_XylanAVLLdapChain_Type = DisplayString
_XylanAVLLdapChain_Object = MibTableColumn
xylanAVLLdapChain = _XylanAVLLdapChain_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 5),
    _XylanAVLLdapChain_Type()
)
xylanAVLLdapChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLLdapChain.setStatus("mandatory")


class _XylanAVLLdapType_Type(Integer32):
    """Custom type xylanAVLLdapType based on Integer32"""
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
        *(("generic-schema", 1),
          ("netscape-directory-server", 2),
          ("novell-NDS", 3),
          ("sun-directory-services", 4))
    )


_XylanAVLLdapType_Type.__name__ = "Integer32"
_XylanAVLLdapType_Object = MibTableColumn
xylanAVLLdapType = _XylanAVLLdapType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 6),
    _XylanAVLLdapType_Type()
)
xylanAVLLdapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLLdapType.setStatus("mandatory")


class _XylanAVLLdapRetry_Type(Integer32):
    """Custom type xylanAVLLdapRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_XylanAVLLdapRetry_Type.__name__ = "Integer32"
_XylanAVLLdapRetry_Object = MibTableColumn
xylanAVLLdapRetry = _XylanAVLLdapRetry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 7),
    _XylanAVLLdapRetry_Type()
)
xylanAVLLdapRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLLdapRetry.setStatus("mandatory")


class _XylanAVLLdapResponseTime_Type(Integer32):
    """Custom type xylanAVLLdapResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_XylanAVLLdapResponseTime_Type.__name__ = "Integer32"
_XylanAVLLdapResponseTime_Object = MibTableColumn
xylanAVLLdapResponseTime = _XylanAVLLdapResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 8),
    _XylanAVLLdapResponseTime_Type()
)
xylanAVLLdapResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLLdapResponseTime.setStatus("mandatory")


class _XylanAVLLdapAcctStatus_Type(Integer32):
    """Custom type xylanAVLLdapAcctStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_XylanAVLLdapAcctStatus_Type.__name__ = "Integer32"
_XylanAVLLdapAcctStatus_Object = MibTableColumn
xylanAVLLdapAcctStatus = _XylanAVLLdapAcctStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 9),
    _XylanAVLLdapAcctStatus_Type()
)
xylanAVLLdapAcctStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLLdapAcctStatus.setStatus("mandatory")
_XylanAVLLdapLoginFailId_Type = DisplayString
_XylanAVLLdapLoginFailId_Object = MibTableColumn
xylanAVLLdapLoginFailId = _XylanAVLLdapLoginFailId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 10),
    _XylanAVLLdapLoginFailId_Type()
)
xylanAVLLdapLoginFailId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLLdapLoginFailId.setStatus("mandatory")


class _XylanAVLLdapMultiGroup_Type(Integer32):
    """Custom type xylanAVLLdapMultiGroup based on Integer32"""
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


_XylanAVLLdapMultiGroup_Type.__name__ = "Integer32"
_XylanAVLLdapMultiGroup_Object = MibTableColumn
xylanAVLLdapMultiGroup = _XylanAVLLdapMultiGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 11),
    _XylanAVLLdapMultiGroup_Type()
)
xylanAVLLdapMultiGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLLdapMultiGroup.setStatus("mandatory")


class _XylanAVLLdapAdminState_Type(Integer32):
    """Custom type xylanAVLLdapAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanAVLLdapAdminState_Type.__name__ = "Integer32"
_XylanAVLLdapAdminState_Object = MibTableColumn
xylanAVLLdapAdminState = _XylanAVLLdapAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 12),
    _XylanAVLLdapAdminState_Type()
)
xylanAVLLdapAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanAVLLdapAdminState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-AVL-MIB",
    **{"XylanAVLtelportStatCodes": XylanAVLtelportStatCodes,
       "xylanAVLConfig": xylanAVLConfig,
       "xylanAVLloginbanner": xylanAVLloginbanner,
       "xylanAVLTproxyports": xylanAVLTproxyports,
       "xylanAVLTproxyentry": xylanAVLTproxyentry,
       "xylanAVLTproxyIntfAddr": xylanAVLTproxyIntfAddr,
       "xylanAVLTproxyProxyAddr": xylanAVLTproxyProxyAddr,
       "xylanAVLtelports": xylanAVLtelports,
       "xylanAVLtelportentry": xylanAVLtelportentry,
       "xylanAVLtelportslot": xylanAVLtelportslot,
       "xylanAVLtelportport": xylanAVLtelportport,
       "xylanAVLtelportstat": xylanAVLtelportstat,
       "xylanAVLoptionprompt": xylanAVLoptionprompt,
       "xylanAVLgroupprompt": xylanAVLgroupprompt,
       "xylanAVLuserprompt": xylanAVLuserprompt,
       "xylanAVLpassprompt": xylanAVLpassprompt,
       "xylanAVLchalprompt": xylanAVLchalprompt,
       "xylanAVLsucceedmsg": xylanAVLsucceedmsg,
       "xylanAVLfailmsg": xylanAVLfailmsg,
       "xylanAVLauthmode": xylanAVLauthmode,
       "xylanAVLtimeout": xylanAVLtimeout,
       "xylanAVLRadiusServers": xylanAVLRadiusServers,
       "xylanAVLradiusentry": xylanAVLradiusentry,
       "xylanAVLRadiusGroup": xylanAVLRadiusGroup,
       "xylanAVLRadiusAddress": xylanAVLRadiusAddress,
       "xylanAVLRadiusPriority": xylanAVLRadiusPriority,
       "xylanAVLRadiusPort": xylanAVLRadiusPort,
       "xylanAVLRadiusSecret": xylanAVLRadiusSecret,
       "xylanAVLRadiusAdminState": xylanAVLRadiusAdminState,
       "xylanAVLRadiusAcctServers": xylanAVLRadiusAcctServers,
       "xylanAVLradiusacctentry": xylanAVLradiusacctentry,
       "xylanAVLRadiusAcctGroup": xylanAVLRadiusAcctGroup,
       "xylanAVLRadiusAcctAddress": xylanAVLRadiusAcctAddress,
       "xylanAVLRadiusAcctPri": xylanAVLRadiusAcctPri,
       "xylanAVLRadiusAcctPort": xylanAVLRadiusAcctPort,
       "xylanAVLRadiusAcctSecret": xylanAVLRadiusAcctSecret,
       "xylanAVLRadiusAcctAdminState": xylanAVLRadiusAcctAdminState,
       "xylanAVLlastuser": xylanAVLlastuser,
       "xylanAVLlastauthevent": xylanAVLlastauthevent,
       "xylanAVLlastauthmac": xylanAVLlastauthmac,
       "xylanAVLlastport": xylanAVLlastport,
       "xylanAVLlastslot": xylanAVLlastslot,
       "xylanAVLversion": xylanAVLversion,
       "xylanAVLdropmac": xylanAVLdropmac,
       "xylanAVLradretries": xylanAVLradretries,
       "xylanAVLradtimeout": xylanAVLradtimeout,
       "xylanAVLBootpIfAddr": xylanAVLBootpIfAddr,
       "xylanAVLDNSName": xylanAVLDNSName,
       "xylanAVLPathRestriction": xylanAVLPathRestriction,
       "xylanAVLLdapServers": xylanAVLLdapServers,
       "xylanAVLLdapentry": xylanAVLLdapentry,
       "xylanAVLLdapGroup": xylanAVLLdapGroup,
       "xylanAVLLdapUserId": xylanAVLLdapUserId,
       "xylanAVLLdapUserPassword": xylanAVLLdapUserPassword,
       "xylanAVLLdapSearchBase": xylanAVLLdapSearchBase,
       "xylanAVLLdapChain": xylanAVLLdapChain,
       "xylanAVLLdapType": xylanAVLLdapType,
       "xylanAVLLdapRetry": xylanAVLLdapRetry,
       "xylanAVLLdapResponseTime": xylanAVLLdapResponseTime,
       "xylanAVLLdapAcctStatus": xylanAVLLdapAcctStatus,
       "xylanAVLLdapLoginFailId": xylanAVLLdapLoginFailId,
       "xylanAVLLdapMultiGroup": xylanAVLLdapMultiGroup,
       "xylanAVLLdapAdminState": xylanAVLLdapAdminState}
)
