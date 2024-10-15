# SNMP MIB module (EXTREME-DLCS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
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

extremeDlcs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeDlcsEnable_Type = TruthValue
_ExtremeDlcsEnable_Object = MibScalar
extremeDlcsEnable = _ExtremeDlcsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 1),
    _ExtremeDlcsEnable_Type()
)
extremeDlcsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDlcsEnable.setStatus("current")
_ExtremeDlcsNetbiosEnable_Type = TruthValue
_ExtremeDlcsNetbiosEnable_Object = MibScalar
extremeDlcsNetbiosEnable = _ExtremeDlcsNetbiosEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 2),
    _ExtremeDlcsNetbiosEnable_Type()
)
extremeDlcsNetbiosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDlcsNetbiosEnable.setStatus("current")
_ExtremeDlcsKerberos5Enable_Type = TruthValue
_ExtremeDlcsKerberos5Enable_Object = MibScalar
extremeDlcsKerberos5Enable = _ExtremeDlcsKerberos5Enable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 3),
    _ExtremeDlcsKerberos5Enable_Type()
)
extremeDlcsKerberos5Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDlcsKerberos5Enable.setStatus("current")
_ExtremeDlcsRsvpEnable_Type = TruthValue
_ExtremeDlcsRsvpEnable_Object = MibScalar
extremeDlcsRsvpEnable = _ExtremeDlcsRsvpEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 4),
    _ExtremeDlcsRsvpEnable_Type()
)
extremeDlcsRsvpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDlcsRsvpEnable.setStatus("current")
_ExtremeDlcsDnsEnable_Type = TruthValue
_ExtremeDlcsDnsEnable_Object = MibScalar
extremeDlcsDnsEnable = _ExtremeDlcsDnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 5),
    _ExtremeDlcsDnsEnable_Type()
)
extremeDlcsDnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDlcsDnsEnable.setStatus("current")
_ExtremeDlcsBindingTable_Object = MibTable
extremeDlcsBindingTable = _ExtremeDlcsBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 6)
)
if mibBuilder.loadTexts:
    extremeDlcsBindingTable.setStatus("current")
_ExtremeDlcsBindingEntry_Object = MibTableRow
extremeDlcsBindingEntry = _ExtremeDlcsBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 6, 1)
)
extremeDlcsBindingEntry.setIndexNames(
    (0, "EXTREME-DLCS-MIB", "extremeDlcsBindingIndex"),
)
if mibBuilder.loadTexts:
    extremeDlcsBindingEntry.setStatus("current")
_ExtremeDlcsBindingIndex_Type = Integer32
_ExtremeDlcsBindingIndex_Object = MibTableColumn
extremeDlcsBindingIndex = _ExtremeDlcsBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 6, 1, 1),
    _ExtremeDlcsBindingIndex_Type()
)
extremeDlcsBindingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDlcsBindingIndex.setStatus("current")


class _ExtremeDlcsBindingType_Type(Bits):
    """Custom type extremeDlcsBindingType based on Bits"""
    namedValues = NamedValues(
        *(("application2ip", 4),
          ("application2user", 3),
          ("group2ip", 6),
          ("group2port", 7),
          ("host2ip", 5),
          ("ip2port", 2),
          ("user2group", 8),
          ("user2ip", 0),
          ("user2port", 1))
    )

_ExtremeDlcsBindingType_Type.__name__ = "Bits"
_ExtremeDlcsBindingType_Object = MibTableColumn
extremeDlcsBindingType = _ExtremeDlcsBindingType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 6, 1, 2),
    _ExtremeDlcsBindingType_Type()
)
extremeDlcsBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDlcsBindingType.setStatus("current")


class _ExtremeDlcsBindingSource_Type(Integer32):
    """Custom type extremeDlcsBindingSource based on Integer32"""
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
        *(("dns", 5),
          ("kerberos5", 6),
          ("local", 2),
          ("netbiosbind", 4),
          ("netbiosquery", 3),
          ("other", 1),
          ("rsvp", 7))
    )


_ExtremeDlcsBindingSource_Type.__name__ = "Integer32"
_ExtremeDlcsBindingSource_Object = MibTableColumn
extremeDlcsBindingSource = _ExtremeDlcsBindingSource_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 6, 1, 3),
    _ExtremeDlcsBindingSource_Type()
)
extremeDlcsBindingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDlcsBindingSource.setStatus("current")
_ExtremeDlcsBindingUser_Type = DisplayString
_ExtremeDlcsBindingUser_Object = MibTableColumn
extremeDlcsBindingUser = _ExtremeDlcsBindingUser_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 6, 1, 4),
    _ExtremeDlcsBindingUser_Type()
)
extremeDlcsBindingUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDlcsBindingUser.setStatus("current")
_ExtremeDlcsBindingGroup_Type = DisplayString
_ExtremeDlcsBindingGroup_Object = MibTableColumn
extremeDlcsBindingGroup = _ExtremeDlcsBindingGroup_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 6, 1, 5),
    _ExtremeDlcsBindingGroup_Type()
)
extremeDlcsBindingGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDlcsBindingGroup.setStatus("current")
_ExtremeDlcsBindingApplication_Type = DisplayString
_ExtremeDlcsBindingApplication_Object = MibTableColumn
extremeDlcsBindingApplication = _ExtremeDlcsBindingApplication_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 6, 1, 6),
    _ExtremeDlcsBindingApplication_Type()
)
extremeDlcsBindingApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDlcsBindingApplication.setStatus("current")
_ExtremeDlcsBindingHost_Type = DisplayString
_ExtremeDlcsBindingHost_Object = MibTableColumn
extremeDlcsBindingHost = _ExtremeDlcsBindingHost_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 6, 1, 7),
    _ExtremeDlcsBindingHost_Type()
)
extremeDlcsBindingHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDlcsBindingHost.setStatus("current")
_ExtremeDlcsBindingIpAddress_Type = IpAddress
_ExtremeDlcsBindingIpAddress_Object = MibTableColumn
extremeDlcsBindingIpAddress = _ExtremeDlcsBindingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 6, 1, 8),
    _ExtremeDlcsBindingIpAddress_Type()
)
extremeDlcsBindingIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDlcsBindingIpAddress.setStatus("current")
_ExtremeDlcsBindingPhysPort_Type = Integer32
_ExtremeDlcsBindingPhysPort_Object = MibTableColumn
extremeDlcsBindingPhysPort = _ExtremeDlcsBindingPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 6, 1, 9),
    _ExtremeDlcsBindingPhysPort_Type()
)
extremeDlcsBindingPhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDlcsBindingPhysPort.setStatus("current")
_ExtremeDlcsBindingUpdateTime_Type = TimeTicks
_ExtremeDlcsBindingUpdateTime_Object = MibTableColumn
extremeDlcsBindingUpdateTime = _ExtremeDlcsBindingUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8, 6, 1, 10),
    _ExtremeDlcsBindingUpdateTime_Type()
)
extremeDlcsBindingUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDlcsBindingUpdateTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-DLCS-MIB",
    **{"extremeDlcs": extremeDlcs,
       "extremeDlcsEnable": extremeDlcsEnable,
       "extremeDlcsNetbiosEnable": extremeDlcsNetbiosEnable,
       "extremeDlcsKerberos5Enable": extremeDlcsKerberos5Enable,
       "extremeDlcsRsvpEnable": extremeDlcsRsvpEnable,
       "extremeDlcsDnsEnable": extremeDlcsDnsEnable,
       "extremeDlcsBindingTable": extremeDlcsBindingTable,
       "extremeDlcsBindingEntry": extremeDlcsBindingEntry,
       "extremeDlcsBindingIndex": extremeDlcsBindingIndex,
       "extremeDlcsBindingType": extremeDlcsBindingType,
       "extremeDlcsBindingSource": extremeDlcsBindingSource,
       "extremeDlcsBindingUser": extremeDlcsBindingUser,
       "extremeDlcsBindingGroup": extremeDlcsBindingGroup,
       "extremeDlcsBindingApplication": extremeDlcsBindingApplication,
       "extremeDlcsBindingHost": extremeDlcsBindingHost,
       "extremeDlcsBindingIpAddress": extremeDlcsBindingIpAddress,
       "extremeDlcsBindingPhysPort": extremeDlcsBindingPhysPort,
       "extremeDlcsBindingUpdateTime": extremeDlcsBindingUpdateTime}
)
