#
# PySNMP MIB module HM2-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-DNS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:31:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
HmActionValue, HmEnabledStatus, hm2ConfigurationMibs = mibBuilder.importSymbols("HM2-TC-MIB", "HmActionValue", "HmEnabledStatus", "hm2ConfigurationMibs")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Unsigned32, ModuleIdentity, NotificationType, TimeTicks, Counter32, Integer32, Counter64, IpAddress, MibIdentifier, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "ModuleIdentity", "NotificationType", "TimeTicks", "Counter32", "Integer32", "Counter64", "IpAddress", "MibIdentifier", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
hm2DnsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 90))
hm2DnsMib.setRevisions(('2011-06-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hm2DnsMib.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hm2DnsMib.setLastUpdated('201106170000Z')
if mibBuilder.loadTexts: hm2DnsMib.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hm2DnsMib.setContactInfo('Postal: Stuttgarter Str. 45-51 72654 Neckartenzlingen Germany Phone: +49 7127 140 E-mail: hac.support@belden.com')
if mibBuilder.loadTexts: hm2DnsMib.setDescription('Hirschmann DNS MIB for DNS client, DNS client cache and DNS caching server. Copyright (C) 2011. All Rights Reserved.')
hm2DnsMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 90, 0))
hm2DnsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 90, 1))
hm2DnsMibSNMPExtensionGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 90, 3))
hm2DnsClientGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1))
hm2DnsCacheGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 2))
hm2DnsCachingServerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 3))
hm2DnsClientAdminState = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 1), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DnsClientAdminState.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientAdminState.setDescription('The operational status of DNS client. If disabled, no host name lookups will be done for names entered on the CLI and in the configuration of services e.g. NTP.')
hm2DnsClientConfigSource = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("user", 1), ("mgmt-dhcp", 2), ("provider", 3))).clone('mgmt-dhcp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DnsClientConfigSource.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientConfigSource.setDescription('DNS client server source. If the value is set to user(1), the variables from hm2DnsClientServerCfgTable will be used. If the value is set to mgmt-dhcp(2), the DNS servers received by DHCP on the management interface will be used. If the value is set to provider(3), the DNS configuration will be taken from DHCP, PPP or PPPoE on the primary WAN link.')
hm2DnsClientServerCfgTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 3), )
if mibBuilder.loadTexts: hm2DnsClientServerCfgTable.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientServerCfgTable.setDescription('The table that contains the DNS Servers entries configured by the user in the system.')
hm2DnsClientServerCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 3, 1), ).setIndexNames((0, "HM2-DNS-MIB", "hm2DnsClientServerIndex"))
if mibBuilder.loadTexts: hm2DnsClientServerCfgEntry.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientServerCfgEntry.setDescription('An entry contains the IP address of a DNS server configured in the system.')
hm2DnsClientServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: hm2DnsClientServerIndex.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientServerIndex.setDescription('The unique index used for each server added in the DNS servers table.')
hm2DnsClientServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 3, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DnsClientServerAddressType.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientServerAddressType.setDescription('Address type for DNS server. Currently, only ipv4 is supported.')
hm2DnsClientServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 3, 1, 3), InetAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DnsClientServerAddress.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientServerAddress.setDescription('The IP address of the DNS server.')
hm2DnsClientServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DnsClientServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientServerRowStatus.setDescription('Describes the status of a row in the table.')
hm2DnsClientServerDiagTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 4), )
if mibBuilder.loadTexts: hm2DnsClientServerDiagTable.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientServerDiagTable.setDescription('The table that contains the DNS Servers entries configured and used in the system.')
hm2DnsClientServerDiagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 4, 1), ).setIndexNames((0, "HM2-DNS-MIB", "hm2DnsClientServerDiagIndex"))
if mibBuilder.loadTexts: hm2DnsClientServerDiagEntry.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientServerDiagEntry.setDescription('An entry contains the IP address of a DNS server used in the system.')
hm2DnsClientServerDiagIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: hm2DnsClientServerDiagIndex.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientServerDiagIndex.setDescription('The unique index used for each server added in the DNS servers table.')
hm2DnsClientServerDiagAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 4, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DnsClientServerDiagAddressType.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientServerDiagAddressType.setDescription('Address type for DNS server used. Currently, only ipv4 is supported.')
hm2DnsClientServerDiagAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 4, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2DnsClientServerDiagAddress.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientServerDiagAddress.setDescription('The IP address of the DNS server used by the system. The entry can be configured by the provider, e.g. through DHCP client or PPPoE client.')
hm2DnsClientGlobalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 5))
hm2DnsClientDefaultDomainName = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 5, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DnsClientDefaultDomainName.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientDefaultDomainName.setDescription('The default domain name for unqualified hostnames.')
hm2DnsClientRequestTimeout = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DnsClientRequestTimeout.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientRequestTimeout.setDescription('The timeout before retransmitting a request to the server. The timeout value is configured and displayed in seconds.')
hm2DnsClientRequestRetransmits = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DnsClientRequestRetransmits.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientRequestRetransmits.setDescription('The number of times the request is retransmitted. The request is retransmitted provided the maximum timeout value allows this many number of retransmits.')
hm2DnsClientCacheAdminState = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 5, 4), HmEnabledStatus().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DnsClientCacheAdminState.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientCacheAdminState.setDescription('Enables/Disables DNS client cache functionality of the device.')
hm2DnsClientStaticHostConfigTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 6), )
if mibBuilder.loadTexts: hm2DnsClientStaticHostConfigTable.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientStaticHostConfigTable.setDescription('Static table of DNS hostname to IP address table')
hm2DnsClientStaticHostConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 6, 1), ).setIndexNames((0, "HM2-DNS-MIB", "hm2DnsClientStaticIndex"))
if mibBuilder.loadTexts: hm2DnsClientStaticHostConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientStaticHostConfigEntry.setDescription('An entry in the static DNS hostname IP address list. Rows may be created or deleted at any time by the DNS resolver and by SNMP SET requests.')
hm2DnsClientStaticIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: hm2DnsClientStaticIndex.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientStaticIndex.setDescription('The index of the entry.')
hm2DnsClientStaticHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 6, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DnsClientStaticHostName.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientStaticHostName.setDescription('The static hostname.')
hm2DnsClientStaticHostAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 6, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DnsClientStaticHostAddressType.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientStaticHostAddressType.setDescription('Address type for static hosts used. Currently, only ipv4 is supported.')
hm2DnsClientStaticHostIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 6, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DnsClientStaticHostIPAddress.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientStaticHostIPAddress.setDescription('The IP address of the static host.')
hm2DnsClientStaticHostStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 1, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2DnsClientStaticHostStatus.setStatus('current')
if mibBuilder.loadTexts: hm2DnsClientStaticHostStatus.setDescription('Describes the status of a row in the table.')
hm2DnsCachingServerGlobalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 3, 1))
hm2DnsCachingServerAdminState = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 3, 1, 1), HmEnabledStatus().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DnsCachingServerAdminState.setStatus('current')
if mibBuilder.loadTexts: hm2DnsCachingServerAdminState.setDescription('Enables/Disables DNS caching server functionality of the device.')
hm2DnsCacheAdminState = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 2, 1), HmEnabledStatus().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DnsCacheAdminState.setStatus('deprecated')
if mibBuilder.loadTexts: hm2DnsCacheAdminState.setDescription('Enables/Disables DNS cache functionality of the device. **NOTE: this object is deprecated and replaced by hm2DnsClientCacheAdminState/hm2DnsCachingServerAdminState**.')
hm2DnsCacheFlushAction = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 90, 1, 2, 2), HmActionValue().clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2DnsCacheFlushAction.setStatus('deprecated')
if mibBuilder.loadTexts: hm2DnsCacheFlushAction.setDescription('Setting this value to action will flush the DNS cache. After flushing the cache, it will be set to noop automatically. **NOTE: this object is deprecated and replaced by hm2DevMgmtActionFlushDnsClientCache/hm2DevMgmtActionFlushDnsCachingServerCache**.')
hm2DnsCHHostNameAlreadyExistsSESError = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 90, 3, 1))
if mibBuilder.loadTexts: hm2DnsCHHostNameAlreadyExistsSESError.setStatus('current')
if mibBuilder.loadTexts: hm2DnsCHHostNameAlreadyExistsSESError.setDescription('The host name entered exists and is associated with an IP. The change attempt was canceled.')
hm2DnsCHBadIpNotAcceptedSESError = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 90, 3, 2))
if mibBuilder.loadTexts: hm2DnsCHBadIpNotAcceptedSESError.setStatus('current')
if mibBuilder.loadTexts: hm2DnsCHBadIpNotAcceptedSESError.setDescription('The Ip Adress entered is not a valid one for a host. The change attempt was canceled.')
hm2DnsCHBadRowCannotBeActivatedSESError = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 11, 90, 3, 3))
if mibBuilder.loadTexts: hm2DnsCHBadRowCannotBeActivatedSESError.setStatus('current')
if mibBuilder.loadTexts: hm2DnsCHBadRowCannotBeActivatedSESError.setDescription('The instance cannot be activated due to compliance issues. Please modify the entry and try again.')
mibBuilder.exportSymbols("HM2-DNS-MIB", hm2DnsCachingServerGlobalGroup=hm2DnsCachingServerGlobalGroup, hm2DnsClientServerIndex=hm2DnsClientServerIndex, hm2DnsClientServerAddress=hm2DnsClientServerAddress, hm2DnsClientServerCfgTable=hm2DnsClientServerCfgTable, PYSNMP_MODULE_ID=hm2DnsMib, hm2DnsClientServerDiagAddress=hm2DnsClientServerDiagAddress, hm2DnsClientStaticHostConfigTable=hm2DnsClientStaticHostConfigTable, hm2DnsClientGlobalGroup=hm2DnsClientGlobalGroup, hm2DnsCacheGroup=hm2DnsCacheGroup, hm2DnsClientServerDiagEntry=hm2DnsClientServerDiagEntry, hm2DnsMibSNMPExtensionGroup=hm2DnsMibSNMPExtensionGroup, hm2DnsClientGroup=hm2DnsClientGroup, hm2DnsMibObjects=hm2DnsMibObjects, hm2DnsClientDefaultDomainName=hm2DnsClientDefaultDomainName, hm2DnsClientStaticHostStatus=hm2DnsClientStaticHostStatus, hm2DnsCacheAdminState=hm2DnsCacheAdminState, hm2DnsClientRequestTimeout=hm2DnsClientRequestTimeout, hm2DnsClientServerDiagAddressType=hm2DnsClientServerDiagAddressType, hm2DnsCachingServerGroup=hm2DnsCachingServerGroup, hm2DnsClientServerDiagTable=hm2DnsClientServerDiagTable, hm2DnsCHBadIpNotAcceptedSESError=hm2DnsCHBadIpNotAcceptedSESError, hm2DnsClientAdminState=hm2DnsClientAdminState, hm2DnsClientStaticHostName=hm2DnsClientStaticHostName, hm2DnsClientRequestRetransmits=hm2DnsClientRequestRetransmits, hm2DnsMibNotifications=hm2DnsMibNotifications, hm2DnsClientConfigSource=hm2DnsClientConfigSource, hm2DnsClientServerRowStatus=hm2DnsClientServerRowStatus, hm2DnsClientServerDiagIndex=hm2DnsClientServerDiagIndex, hm2DnsClientCacheAdminState=hm2DnsClientCacheAdminState, hm2DnsCHHostNameAlreadyExistsSESError=hm2DnsCHHostNameAlreadyExistsSESError, hm2DnsCacheFlushAction=hm2DnsCacheFlushAction, hm2DnsClientStaticIndex=hm2DnsClientStaticIndex, hm2DnsClientStaticHostAddressType=hm2DnsClientStaticHostAddressType, hm2DnsCachingServerAdminState=hm2DnsCachingServerAdminState, hm2DnsCHBadRowCannotBeActivatedSESError=hm2DnsCHBadRowCannotBeActivatedSESError, hm2DnsClientServerAddressType=hm2DnsClientServerAddressType, hm2DnsMib=hm2DnsMib, hm2DnsClientStaticHostIPAddress=hm2DnsClientStaticHostIPAddress, hm2DnsClientServerCfgEntry=hm2DnsClientServerCfgEntry, hm2DnsClientStaticHostConfigEntry=hm2DnsClientStaticHostConfigEntry)